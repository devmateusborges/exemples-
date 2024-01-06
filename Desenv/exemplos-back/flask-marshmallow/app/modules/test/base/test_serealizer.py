from app import db
from app.modules.test.base.test_model import Test1, Test1Child, Test1Fk
from app.utils.generic_schema import generic_schema
from flask_marshmallow import Marshmallow
from marshmallow import fields

ma = Marshmallow()

#================================================================
class Test1Schema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = Test1
        sqla_session = db.session
        load_instance = True
        include_fk = True

    codigo = fields.Str(required=True)
    descricao = fields.Str(required=True)
    dt_nascimento = fields.Date(required=True,format="%d/%m/%Y")
    test1_fk_id = fields.Str(required=True)
    test1_fk_id_obj = fields.Nested('Test1FkSchema')
    test1_childs = fields.Nested('Test1ChildSchema', many=True)
    

#================================================================
class Test1FkSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = Test1Fk
        sqla_session = db.session
        load_instance = True

    codigo = fields.Str(required=True)
    descricao = fields.Str(required=True)
    


#================================================================
class Test1ChildSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = Test1Child
        sqla_session = db.session
        load_instance = True
        
    codigo = fields.Str(required=True)
    quantidade = fields.Number(required=True)
    valor_total = fields.Number(required=True)
    valor_unit = fields.Number(required=True)
        
