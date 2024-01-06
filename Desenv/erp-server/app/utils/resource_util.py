import json
from flask import request


class resource_util:
    @staticmethod
    def req_param_default():
        ppage = request.args.get("ppage", default=1, type=int)
        pper_page = request.args.get("pper_page", default=100, type=int)
        pfilters = request.args.get("pfilters", default=None)
        if pfilters is not None:
            pfilters = json.loads(pfilters)
        return {"ppage": ppage, "pper_page": pper_page, "pfilters": pfilters}
