import app

from app.modules.tst.base.tst_model import Test1, Test1Child, Test1Fk, Test1aChild
from app.modules.tst.base.tst_types import (
    TypeTst1Radio,
    TypeTstTipoTest1,
)
from app.generics.generic_schema import generic_schema
from app.generics.generic_schema_field import (
    fields_DateTime_Gmt,
    fields_Type_Obj,
    fields_Type_Obj_Sql,
    fields_UnitId,
)
from app.utils.validator_util import valid_type_choice, valid_type_choice_sql
from marshmallow import (
    EXCLUDE,
    fields,
)


# ===============================
class Test1Schema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = Test1
        sqla_session = app.db.session
        load_instance = True
        include_fk = True
        unknown = EXCLUDE

    unit_id = fields_UnitId()
    codigo = fields.Str(required=True)
    descricao = fields.Str(required=True)
    cpfcnpj = fields.Str(required=True)
    dt_nascimento = fields_DateTime_Gmt(required=True)
    dthr_nascimento = fields_DateTime_Gmt(required=True)
    hr_nascimento = fields_DateTime_Gmt(required=True)
    test1_fk_id = fields.Str(required=False)
    test1_fk_id_obj = fields.Nested("Test1FkSchema", allow_none=True, dump_only=True)
    valor = fields.Decimal(places=2, required=False)
    quantidade = fields.Decimal(places=6, required=False)
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
    radio = fields.Str(required=True, validate=valid_type_choice(TypeTst1Radio.choices))
    radio_obj = fields_Type_Obj(field_choice="radio", type_choice=TypeTst1Radio.choices)

    test1_childs = fields.Nested("Test1ChildSchema", many=True)
    test1a_childs = fields.Nested("Test1aChildSchema", many=True)
    sys_document_childs = fields.Nested("SysDocumentSchema", many=True)


# ===============================
class Test1FkSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = Test1Fk
        sqla_session = app.db.session
        load_instance = True

    unit_id = fields_UnitId()
    codigo = fields.Str(required=True)
    descricao = fields.Str(required=True)
    tipo_test1 = fields.Str(
        required=True, validate=valid_type_choice(TypeTstTipoTest1.choices)
    )
    tipo_test1_obj = fields_Type_Obj(
        field_choice="tipo_test1", type_choice=TypeTstTipoTest1.choices
    )


# ===============================


class Test1ChildSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = Test1Child
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields_UnitId()
    codigo = fields.Str(required=True)
    quantidade = fields.Decimal(places=6, required=True)
    valor_total = fields.Decimal(places=2, required=True)
    valor_unit = fields.Decimal(places=2, required=True)
    sys_document_foto = fields.Nested("SysDocumentSchema", many=True)


class Test1aChildSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = Test1aChild
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields_UnitId()
    observacao = fields.Str(required=True)
    foto_analizada = fields.Nested("SysDocumentSchema", many=True)
