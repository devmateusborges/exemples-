import app

from app.generics.generic_model import generic_model


# ==========================================================


class MobUnitParam(generic_model, app.db.Model):
    __tablename__ = "mob_unit_param"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    data_valid_ini = app.db.Column(app.db.Date)


# ==========================================================
