import logging
import json
import traceback
from flask import Response, jsonify, request
from datetime import datetime
from http.client import HTTPException

from marshmallow import ValidationError
import sentry_sdk


from app.exceptions.ApiException import ApiException


def configure(e):
    try:
        req = request
        try:
            body = json.loads(req.data.decode())
        except:
            body = req.data.decode()

        if isinstance(e, HTTPException):
            sentry_sdk.capture_exception(e)
            logging.error(e.name + " - " + e.description)
            response = e.get_response()
            response.data = json.dumps(
                {
                    "datetime": datetime.now().strftime("%d/%m/%YT%H:%M:%S.%f"),
                    "code": e.code,
                    "name": "HTTP_ERROR",
                    "msg": e.description,
                }
            )
            response.content_type = "application/json"
            return response

        elif isinstance(e, ApiException):
            response = jsonify(e.to_dict())
            response.status_code = e.status_code
            return response
        elif isinstance(e, ValidationError):

            response = Response()
            response.data = json.dumps(
                {
                    "datetime": datetime.now().strftime("%d/%m/%YT%H:%M:%S.%f"),
                    "code": 400,
                    "name": "VALIDATION_ERROR",
                    "msg": e.messages,
                    "data": {"base_url": req.base_url, "body": body},
                }
            )
            response.content_type = "application/json"
            response.status_code = 400
            return response

        else:
            sentry_sdk.capture_exception(e)
            logging.error("Internal Error - " + traceback.format_exc())
            description = str(traceback.format_exc())
            description = description.replace("\n", " ")
            description = description.replace("  ", " ")
            # ===============
            index1 = description.find("RuntimeError:")

            # ===============
            if index1 < 0:
                index1 = description.find("ValueError:")

            descriptionStart = int(index1)
            descriptionEnd = int(len(description) - descriptionStart)
            description = description[-descriptionEnd:]
            response = Response()
            response.status_code = 500

            # ===============
            if index1 < 0:
                index1 = description.find("sqlalchemy.exc.IntegrityError:")
                if index1 > 0:
                    description = "Unique constraint violate"

            # ===============
            if index1 < 0:
                index1 = description.find(
                    "duplicate key value violates unique constraint"
                )
                if index1 > 0:
                    description = "Unique constraint violate"

            # ===============
            if index1 < 0:
                index1 = description.find("Failed to decode JSON object")
                if index1 > 0:
                    description = "Json body invalid"

            # ===============
            if index1 < 0:
                index1 = description.find("jinja2.exceptions.TemplateNotFound:")
                if index1 > 0:
                    description = "Template not found"

            # ===============
            if index1 < 0:
                index1 = description.find(" werkzeug.exceptions.NotFound:")
                if index1 > 0:
                    description = "Data or Page not found"
                    response.status_code = 404

            response.data = json.dumps(
                {
                    "datetime": datetime.now().strftime("%d/%m/%YT%H:%M:%S.%f"),
                    "code": response.status_code,
                    "name": "INTERNAL_ERROR",
                    "msg": description,
                    "data": {"base_url": req.base_url, "body": body},
                }
            )
            response.content_type = "application/json"
            return response
    except Exception as e:
        sentry_sdk.capture_exception(e)
        response = Response()
        response.status_code = 500
        response.data = json.dumps(
            {
                "datetime": datetime.now().strftime("%d/%m/%YT%H:%M:%S.%f"),
                "code": response.status_code,
                "name": "INTERNAL_ERROR",
                "msg": str(traceback.format_exc()),
                "data": {"base_url": req.base_url, "body": body},
            }
        )
        response.content_type = "application/json"
        return response
