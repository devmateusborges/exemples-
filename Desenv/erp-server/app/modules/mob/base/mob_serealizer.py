import app

from app.generics.generic_schema import generic_schema
from marshmallow import fields

from app.modules.mob.base.mob_model import MobUnitParam


# ==========================================================


class MobUnitParamSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = MobUnitParam
        sqla_session = app.db.session
        load_instance = True

    unit_id = fields.Str(required=True)
    data_valid_ini = fields.Str(required=True)


# ==========================================================
