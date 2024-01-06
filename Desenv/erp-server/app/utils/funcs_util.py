import json
from sqlalchemy import or_
from sqlalchemy.orm import class_mapper
from flask import Response
from sqlalchemy.sql import text
from app.utils.json_encoder_util import json_encoder_util
from app.exceptions.ApiException import ApiException


class funcs_util:

    # ============================================================
    @staticmethod
    def getResponseJson(jsonData):
        response = Response()
        response.data = json.dumps(jsonData, cls=json_encoder_util, ensure_ascii=False)
        response.content_type = "application/json"
        response.status_code = 200
        return response

    # ============================================================
    @staticmethod
    def getResponseJsonList(jsonData):
        response = funcs_util.getResponseJson(
            {"total": jsonData["total"], "items": jsonData["items"]}
        )
        return response

    # ============================================================
    @staticmethod
    def getResponseJsonCode(code, msg, data):
        response = funcs_util.getResponseJson({"code": code, "msg": msg, "data": data})
        return response

    # ============================================================
    @staticmethod
    def qryFilter(qry, col_mapper, pfilters):
        pfiltersObj = pfilters
        for filter in pfiltersObj:
            field_name_aux = filter.get("f")
            if "." in field_name_aux:
                pass

            else:
                if hasattr(col_mapper.columns, field_name_aux):
                    v = str(filter.get("v"))
                    if v is not None and v != "":
                        if filter.get("o") == "=":
                            qry = qry.filter(col_mapper.columns[field_name_aux] == v)
                        if filter.get("o") == "in":
                            qry = qry.filter(
                                col_mapper.columns[field_name_aux].in_(v.split(","))
                            )
                        if filter.get("o") == "like":
                            qry = qry.filter(col_mapper.columns[field_name_aux].like(v))
        return qry

    # ============================================================
    @staticmethod
    def qryFilterGlobal(qry, col_mapper, filter_global_fields, filter_global):
        or_filter = []
        for field in filter_global_fields:
            if "." in field:
                field_items = field.split(".")
                field_name = col_mapper.columns[field]
                class_name = field_name.property.mapper.class_
                col_mapper_items = class_mapper(class_name)
                or_filter.append(
                    col_mapper_items.columns[field_items[1]].like(
                        "%" + filter_global + "%"
                    )
                )
            else:
                if hasattr(col_mapper.columns, field):
                    or_filter.append(
                        col_mapper.columns[field].like("%" + filter_global + "%")
                    )

        if len(or_filter) > 0:
            qry = qry.filter(or_(*or_filter))
        return qry

    # ============================================================
    @staticmethod
    def qryOrder(qry, col_mapper, porders):
        pordersObj = json.loads(porders)

        textOrder = str("")
        for order in pordersObj:
            if order.get("o") == "asc" or order.get("o") == "desc":
                if hasattr(col_mapper.columns, order.get("f")):
                    textOrder = (
                        textOrder
                        + col_mapper.columns[order.get("f")].name
                        + " "
                        + order.get("o")
                        + ","
                    )

        if textOrder is not None and textOrder != "":
            textOrder = textOrder[0 : (len(textOrder) - 1)]
            return qry.order_by(text(textOrder))
        else:
            return qry

    # ============================================================
    @staticmethod
    def getAttr(obj, field, default=None):
        if field in obj:
            return obj[field]
        return default

    # ============================================================
    @staticmethod
    def print(description, e):
        print("============================================================")
        print(description)
        print(e)
        print("============================================================")

    # ============================================================
    @staticmethod
    def ExceptionRollback(session, description, e):
        if session is not None:
            session.rollback()
        funcs_util.print(description, e)
        raise e

    # ============================================================
    @staticmethod
    def ExceptionRequiredValue(value, message):
        if value is None or value == "":
            raise ApiException(
                message=message + " required",
                name="VALIDATION_ERROR",
                status_code=400,
            )

    # ============================================================
    @staticmethod
    def findListDict(ListDict, searchField, searchValue):

        return next(
            (item for item in ListDict if item[searchField] == searchValue), None
        )

    # ============================================================
    @staticmethod
    def findListDictField(ListDict, searchField, searchValue, returnField):

        obj = funcs_util.findListDict(
            ListDict=ListDict, searchField=searchField, searchValue=searchValue
        )
        if obj is not None:
            result = obj[returnField]
        else:
            result = None

        return result

    # ============================================================
    @staticmethod
    def findList(List, searchValue):
        result = None
        for item in List:
            for k in item.keys():
                if k == searchValue:
                    result = item.get(k)

        return result
