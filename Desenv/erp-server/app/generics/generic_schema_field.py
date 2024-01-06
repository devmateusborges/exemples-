from datetime import timedelta, datetime
from flask import request
from flask_jwt_extended import current_user
from marshmallow import fields
from app.env import LANGUAGE_DEFAULT
from app.exceptions.ApiException import ApiException

from app.generics.generic_type import generic_type


# ==============================
class fields_Type_Obj(fields.Field):
    def __init__(self, field_choice, type_choice):
        super().__init__()
        self.field_choice = field_choice
        self.type_choice = type_choice

    def serialize(self, attr, obj, **kwargs):
        return generic_type.get_type_obj(
            obj=obj, field_choice=self.field_choice, type_choice=self.type_choice
        )


# ==============================
class fields_Type_Obj_Sql(fields.Field):
    def __init__(self, field_choice, table_name, field_name, session, load_default={}):
        super().__init__()
        self.field_choice = field_choice
        self.table_name = table_name
        self.field_name = field_name
        self.load_default = load_default
        self.session = session

    def serialize(self, attr, obj, **kwargs):

        lang = request.headers.get("x-lang", LANGUAGE_DEFAULT)

        return generic_type.get_type_obj_sql(
            obj=obj,
            field_choice=self.field_choice,
            table_name=self.table_name,
            field_name=self.field_name,
            load_default=self.load_default,
            session=self.session,
            lang=lang,
        )


# ==============================
class fields_DateTime_Gmt(fields.Field):
    def __init__(self, required=False):
        super().__init__(required=required)

    def deserialize(self, value, attr, data, **kwargs):
        gmt = request.headers.get("x-gmt")
        if gmt is None:
            gmt = 0
        else:
            gmt = int(gmt)
        vret = None
        # TODO quando campo for nulo ou não existe no json não esta retornador como VALIDATION_ERROR
        self._validate_missing(value)
        if attr in data:
            valueAux = data[attr]
            if valueAux is not None and valueAux != "":
                date_aux = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S") + timedelta(
                    hours=gmt
                )
                vret = datetime.strftime(date_aux, "%Y-%m-%dT%H:%M:%S")
            else:
                vret = None
        else:
            vret = None

        return vret

    def serialize(self, attr, obj, **kwargs):
        gmt = request.headers.get("x-gmt")
        if gmt is None:
            gmt = 0
        else:
            gmt = -int(gmt)

        if type(obj) is dict:
            if obj[attr] is not None:
                return datetime.strftime(
                    obj[attr] + timedelta(hours=gmt), "%Y-%m-%dT%H:%M:%S"
                )
        else:
            if getattr(obj, attr) is not None:
                return datetime.strftime(
                    getattr(obj, attr) + timedelta(hours=gmt), "%Y-%m-%dT%H:%M:%S"
                )
            else:
                return {}


# ==============================
class fields_UnitId(fields.Field):
    def __init__(self):
        super().__init__(required=True)

    def deserialize(self, value, attr, data, **kwargs):

        unitid = request.headers.get("x-unitid")

        if attr is not None in data.keys():
            raise ApiException(
                message={attr: "Unit required in body"},
                name="VALIDATION_ERROR",
                status_code=400,
            )
        elif data[attr] is None or data[attr] == "":
            raise ApiException(
                message={attr: "Unit required"},
                name="VALIDATION_ERROR",
                status_code=400,
            )
        elif data[attr] != current_user[1].id:
            raise ApiException(
                message={attr: "Unit invalid (l)"},
                name="VALIDATION_ERROR",
                status_code=400,
            )
        elif data[attr] != unitid:
            raise ApiException(
                message={attr: "Unit invalid (h)"},
                name="VALIDATION_ERROR",
                status_code=400,
            )

        return data[attr]

    def serialize(self, attr, obj, **kwargs):
        if type(obj) is dict:
            return obj[attr]
        else:
            return getattr(obj, attr)
