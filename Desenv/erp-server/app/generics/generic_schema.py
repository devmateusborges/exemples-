from marshmallow import fields


class generic_schema(object):
    id = fields.Str()
    log_user_ins = fields.Str(dump_only=True)
    log_date_ins = fields.Str(dump_only=True)
    log_user_upd = fields.Str(dump_only=True)
    log_date_upd = fields.Str(dump_only=True)
