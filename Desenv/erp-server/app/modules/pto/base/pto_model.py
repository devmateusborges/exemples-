import app
from app.generics.generic_model import generic_model


# ==========================================================


class PtoMarcacao(generic_model, app.db.Model):
    __tablename__ = "pto_marcacao"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    pto_medidor_id = app.db.Column(app.db.ForeignKey("pto_medidor.id"))
    marc_data = app.db.Column(app.db.TIMESTAMP())
    marc_dia = app.db.Column(app.db.Integer)
    marc_mes = app.db.Column(app.db.Integer)
    marc_ano = app.db.Column(app.db.Integer)
    marc_hora = app.db.Column(app.db.Integer)
    marc_minuto = app.db.Column(app.db.Integer)
    process_id = app.db.Column(app.db.ForeignKey("sys_process_log.id"))

    process_id_obj = app.db.relationship("SysProcessLog")
    pto_medidor_id_obj = app.db.relationship("PtoMedidor")


# ==========================================================


class PtoMedidor(generic_model, app.db.Model):
    __tablename__ = "pto_medidor"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_medidor = app.db.Column(app.db.String(50))


# ==========================================================


class PtoUnitParam(generic_model, app.db.Model):
    __tablename__ = "pto_unit_param"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    data_valid_ini = app.db.Column(app.db.Date)
