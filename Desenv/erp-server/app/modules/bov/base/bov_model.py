import app
from app.generics.generic_model import generic_model


# ==========================================================


class BovUnitParam(generic_model, app.db.Model):
    __tablename__ = "bov_unit_param"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    unit_id_obj = app.db.relationship("SysUnit")
    data_valid_ini = app.db.Column(app.db.Date)


# ==========================================================
