import app
from app.modules.pto.base.pto_model import PtoMarcacao, PtoMedidor, PtoUnitParam
from app.generics.generic_schema import generic_schema
from marshmallow import EXCLUDE, fields
from app.generics.generic_schema_field import fields_Type_Obj_Sql
from app.utils.validator_util import valid_type_choice_sql


# ==========================================================


class PtoMarcacaoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = PtoMarcacao
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)

    marc_data = fields.Str(required=True)
    marc_dia = fields.Str(required=True)
    marc_mes = fields.Str(required=True)
    marc_ano = fields.Str(required=True)
    marc_hora = fields.Str(required=True)
    marc_minuto = fields.Str(required=True)

    process_id = fields.Str(required=True)
    process_id_obj = fields.Nested("SysProcessLogSchema", dump_only=True)

    pto_medidor_id = fields.Str(required=True)
    pto_medidor_id_obj = fields.Nested("PtoMedidorSchema", dump_only=True)


# ==========================================================


class PtoMedidorSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = PtoMedidor
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    sigla_medidor = fields.Str(required=True)


# ==========================================================


class PtoUnitParamSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = PtoUnitParam
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    data_valid_ini = fields.Str(required=True)
