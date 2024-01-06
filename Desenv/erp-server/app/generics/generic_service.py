from flask import current_app
from typing import Any
from flask_jwt_extended import current_user
from app.exceptions.ApiException import ApiException
from app.utils.validator_util import validator_util
from app.generics.generic_query import get_generic_query


class generic_service:
    model: Any
    schema: Any

    def __init__(self, model=None, schema=None, unique_fields=None):
        self.model = model
        self.schema = schema
        self.unique_fields = unique_fields

    # ==============================
    def find_all(self, page=1, per_page=50, filters=None, enabled_filter_fields=None):

        if current_user is not None:
            pass
            # print(">>>", current_user[0].login)
            # print(">>>", current_user[1].code_unit)

        qry = get_generic_query(
            self.model, filters, current_app.db.session, enabled_filter_fields
        )

        pagination = qry.paginate(page=page, per_page=per_page)

        items = self.schema(many=True).dump(pagination.items)

        pages = pagination.pages

        if page == 0:
            first = 0
        else:
            first = per_page * page

        result = {
            "items": items,
            "has_next": pagination.has_next,
            "has_prev": pagination.has_prev,
            "next_num": pagination.next_num,
            "page": page,
            "pages": pages,
            "per_page": pagination.per_page,
            "prev_num": pagination.prev_num,
            "first": first,
            "total": pagination.total,
        }

        return result

    # ==============================
    def find_by_id(self, id):
        obj = (
            current_app.db.session.query(self.model).filter(self.model.id == id).first()
        )

        return obj

    # ==============================
    def save(self, obj):
        if self.unique_fields is not None:
            objUnique = validator_util.valid_unique_fields(
                obj, self.model, self.unique_fields, current_app.db.session
            )
            if objUnique["unique"]:
                raise ApiException(
                    message="Record exists, is unique columns [{}]".format(
                        objUnique["msg"]
                    ),
                    name="ERROR_ROW_UNIQUE",
                    status_code=400,
                )

        current_app.db.session.add(obj)

        return obj

    # ==============================
    def delete(self, id):
        obj = (
            current_app.db.session.query(self.model).filter(self.model.id == id).first()
        )
        if obj is None:
            ApiException(
                message="Record id[" + id + "] not found",
                name="ERROR_ROW_NOT_FOUND",
                status_code=400,
            )

        current_app.db.session.query(self.model).filter(self.model.id == id).delete()

        return "deleted"
