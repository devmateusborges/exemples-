import app
from app.modules.rhm.base.rhm_model import RhmUnitParam
from app.generics.generic_schema import generic_schema
from marshmallow import fields


# ==========================================================


class RhmUnitParamSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = RhmUnitParam
        sqla_session = app.db.session
        load_instance = True

    unit_id = fields.Str(required=True)
    data_valid_ini = fields.Str(required=True)


# ==========================================================
