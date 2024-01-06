import app
from app.generics.generic_model import generic_model

# ===============================
class Test1(generic_model, app.db.Model):
    __tablename__ = "test1"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    codigo = app.db.Column(app.db.String(50))
    descricao = app.db.Column(app.db.String(100))
    cpfcnpj = app.db.Column(app.db.String(50))
    dt_nascimento = app.db.Column(app.db.Date)
    dthr_nascimento = app.db.Column(app.db.DateTime)
    hr_nascimento = app.db.Column(app.db.Time)
    test1_fk_id = app.db.Column(app.db.String(36), app.db.ForeignKey("test1_fk.id"))
    test1_fk_id_obj = app.db.relationship("Test1Fk")
    test1_childs = app.db.relationship("Test1Child", cascade="all,delete-orphan")
    test1a_childs = app.db.relationship("Test1aChild", cascade="all,delete-orphan")
    valor = app.db.Column(app.db.Numeric(18, 2))
    quantidade = app.db.Column(app.db.Numeric(18, 6))
    ativo = app.db.Column(app.db.String(1))
    radio = app.db.Column(app.db.String(50))
    sys_document_childs = app.db.relationship(
        "SysDocument", cascade="all,delete-orphan"
    )


# ===============================


class Test1Fk(generic_model, app.db.Model):
    __tablename__ = "test1_fk"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    codigo = app.db.Column(app.db.String(50))
    descricao = app.db.Column(app.db.String(100))
    tipo_test1 = app.db.Column(app.db.String(2))


# ===============================


class Test1Child(generic_model, app.db.Model):
    __tablename__ = "test1_child"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    codigo = app.db.Column(app.db.String(50))
    quantidade = app.db.Column(app.db.Numeric(18, 6))
    valor_total = app.db.Column(app.db.Numeric(18, 2))
    valor_unit = app.db.Column(app.db.Numeric(18, 2))
    test1_id = app.db.Column(app.db.ForeignKey("test1.id"))
    sys_document_foto = app.db.relationship("SysDocument", cascade="all,delete-orphan")


class Test1aChild(generic_model, app.db.Model):
    __tablename__ = "test1a_child"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    test1_id = app.db.Column(app.db.ForeignKey("test1.id"))
    observacao = app.db.Column(app.db.String(250))
    foto_analizada = app.db.relationship("SysDocument", cascade="all,delete-orphan")
