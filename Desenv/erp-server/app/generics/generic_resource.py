from flask import jsonify
from app.utils.resource_util import resource_util


class generic_resource:

    # ==============================
    @staticmethod
    def find_all(service, model, schema, db_session, enabled_filter_fields=[]):
        srv = service(model, schema)
        req_param = resource_util.req_param_default()
        result = srv.find_all(
            page=req_param["ppage"],
            per_page=req_param["pper_page"],
            filters=req_param["pfilters"],
            enabled_filter_fields=enabled_filter_fields,
        )
        db_session.close()
        return result, 200

    # ==============================
    @staticmethod
    def find_by_id(id, service, model, schema, db_session):
        srv = service(model)
        result = srv.find_by_id(id)
        resultJson = schema().jsonify(result)
        db_session.close()
        return resultJson, 200

    # ==============================
    @staticmethod
    def save(
        body, service, model, schema, db_session, unique_fields=None, autoCommit=True
    ):
        srv = service(model, schema=None, unique_fields=unique_fields)

        obj = schema().load(body)

        result = srv.save(obj)
        resultJson = result

        if autoCommit:
            db_session.commit()
            resultJson = schema().jsonify(result), 201
            db_session.close()

        return resultJson

    # ==============================
    def delete(id, service, model, db_session):
        srv = service(model)
        result = srv.delete(id)
        db_session.commit()
        db_session.close()
        return jsonify(result), 204

    # ==============================
