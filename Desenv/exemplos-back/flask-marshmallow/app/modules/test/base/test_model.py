import uuid
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import pbkdf2_sha256

from app.utils.generic_model import generic_model

db = SQLAlchemy()

#================================================================
class Test1(generic_model, db.Model):
    __tablename__ = 'test1'
    __table_args__ = {'comment': 'Testes - Tabela Pai'}    
    
    codigo = db.Column(db.String(50),name='codigo',comment='Código')
    descricao = db.Column(db.String(100),name='descricao',comment='Descrição')
    dt_nascimento = db.Column(db.DateTime,name='dt_nascimento',comment='Data de nascimento')   
    test1_fk_id = db.Column(db.String(36),  db.ForeignKey("test1_fk.id"), name='test1_fk_id',comment='Test1 FK')
    test1_fk_id_obj = db.relationship("Test1Fk")
    test1_childs = db.relationship("Test1Child",cascade='all,delete-orphan')    

#================================================================
class Test1Fk(generic_model, db.Model):
    __tablename__ = 'test1_fk'
    __table_args__ = {'comment': 'Testes - Tabela FK'}    
    
    codigo = db.Column(db.String(50),name='codigo',comment='Código')
    descricao = db.Column(db.String(100),name='descricao',comment='Descrição')

#================================================================
class Test1Child(generic_model, db.Model):
    __tablename__ = 'test1_child'
    __table_args__ = {'comment': 'Testes - Tabela filha de Test1'}
    
    codigo = db.Column(db.String(50),name='codigo',comment='Código')
    quantidade = db.Column(db.Numeric(18, 6),name='quantidade',comment='Quantidade')
    valor_total = db.Column(db.Numeric(18, 2),name='valor_total',comment='Valor total')
    valor_unit = db.Column(db.Numeric(18, 2),name='valor_unit',comment='Valor unit')
    test1_id = db.Column(db.ForeignKey('test1.id'),name='test1_id',comment='Valor unit')


