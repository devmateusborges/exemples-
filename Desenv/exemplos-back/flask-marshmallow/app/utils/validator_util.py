
from marshmallow import ValidationError

#TODO criar validador com type passando por parametro
def app_validate_sn(field_name, data,message='value in S or N'):
        if data[field_name] == 'S' or data[field_name] == 'N':
            pass
        else:
            raise ValidationError("Field "+field_name+" "+message)