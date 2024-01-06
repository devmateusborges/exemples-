import app
from marshmallow import EXCLUDE, fields

# ==========================================================
class LoginSchema(app.ma.Schema):
    class Meta:
        unknown = EXCLUDE

    login = fields.Str(required=True)
    password = fields.Str(required=True)
    unit_id = fields.Str(required=True)
