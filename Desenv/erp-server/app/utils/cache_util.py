from flask import request


class cache_util:

    # ============================================================
    @staticmethod
    def make_key():

        unitid = request.headers.get("x-unitid")
        query = request.args.to_dict(flat=True)
        path = request.full_path
        hashStr = str(query)
        result = "key-" + str(path) + "-" + str(unitid) + "-" + str(hash(hashStr))
        return result
