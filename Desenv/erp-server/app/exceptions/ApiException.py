from datetime import datetime


class ApiException(Exception):
    status_code = 400

    def __init__(
        self, message, name, status_code=None, payload=None, e_predecessor=None
    ):
        Exception.__init__(self)
        if type(e_predecessor) is ApiException:
            self.message = e_predecessor.message
            self.status_code = e_predecessor.status_code
            self.payload = e_predecessor.payload
            self.name = e_predecessor.name
        else:
            self.message = message
            if status_code is not None:
                self.status_code = status_code
            self.payload = payload
            self.name = name

    def to_dict(self):
        rv = dict(self.payload or ())
        rv["datetime"] = str(datetime.now().strftime("%d/%m/%Y  %H:%M:%S.%f"))
        rv["code"] = str(400)
        rv["msg"] = self.message
        rv["name"] = self.name
        return rv
