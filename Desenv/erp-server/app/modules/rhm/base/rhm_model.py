import app
from sqlalchemy import Index, Integer, Text, text
from app.generics.generic_model import generic_model


# ==========================================================  

class RhmUnitParam(generic_model, app.db.Model):
    __tablename__ = 'rhm_unit_param'

    unit_id = app.db.Column(app.db.ForeignKey('sys_unit.id'))
    data_valid_ini = app.db.Column(app.db.Date)
# ==========================================================  