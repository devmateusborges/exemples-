import app

from app.modules.bov.base.bov_model import BovUnitParam

from app.generics.generic_schema import generic_schema
from marshmallow import EXCLUDE, fields

# ==========================================================


class BovUnitParamSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = BovUnitParam
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    unit_id_obj = fields.Nested("SysUnitSchema", dump_only=True)
    data_valid_ini = fields.Str(required=True)


# ==========================================================
