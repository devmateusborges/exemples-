import datetime
import decimal
from json import JSONEncoder


class json_encoder_util(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        if isinstance(obj, (decimal.Decimal)):
            return str(obj)
