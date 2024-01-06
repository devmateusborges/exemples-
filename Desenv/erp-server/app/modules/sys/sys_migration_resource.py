from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.sys.sys_migration_service import sys_migration_service

from app.modules.sys.base.sys_serealizer import SysMigrationSchema
from app.modules.sys.base.sys_model import SysMigration
from app.generics.generic_resource import generic_resource


routes_sys_migration = Blueprint(
    "sysmigration", __name__, url_prefix="/api/sys/sysmigration"
)


# ==============================


@routes_sys_migration.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=sys_migration_service,
        model=SysMigration,
        schema=SysMigrationSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_sys_migration.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=sys_migration_service,
        model=SysMigration,
        schema=SysMigrationSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_sys_migration.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=sys_migration_service,
        model=SysMigration,
        schema=SysMigrationSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_sys_migration.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=sys_migration_service,
        model=SysMigration,
        db_session=current_app.db.session,
    )
