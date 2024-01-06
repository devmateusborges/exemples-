class funcs_sql:

    # ============================================================
    @staticmethod
    def getResultSql(sql, fields, session, page=0, per_page=50):
        offset = per_page * (page - 1)
        limit = per_page
        result = []
        resultObj = {}
        rowCountAux = 0

        queries = str(sql)

        if queries.find("[paginate]") > 0:
            isPaginate = True
        else:
            isPaginate = False

        if isPaginate:
            if page > 0:
                paginate = f"limit {limit} offset {offset}"
            else:
                paginate = ""

            queriesCount = queries.replace("[paginate]", "")
            rsCount = session.execute(
                f"select count(1) as count from ({queriesCount}) t1"
            )
            queries = queries.replace("[paginate]", paginate)

        rs = session.execute(queries)

        keys = fields
        for row in rs:
            rowCountAux += 1
            result.append((dict(zip(keys, row))))

        resultObj["items"] = result

        if isPaginate:
            for rowCount in rsCount:
                rowCountAux = rowCount[0]
        else:
            resultObj["total"] = rowCountAux

        resultObj["total"] = rowCountAux
        return resultObj

    # ============================================================
    @staticmethod
    def execProcSql(sqlfunction, session, commit, **kwargs):
        rs = session.execute(f"select {sqlfunction} ", kwargs)
        if commit:
            session.commit()
        if rs is not None:
            for row in rs:
                return row[0]
        else:
            return None

    # ============================================================
    @staticmethod
    def strClean(pstr: str, pdefault="", pReplace=True):

        if pstr is None or pstr == "":
            vstr = pdefault
        else:
            if pReplace:
                vstr = pstr.replace("'", "''")
            else:
                vstr = pstr

        return vstr

    # ============================================================
    @staticmethod
    def getFieldFilter(pFilters, pFieldsFilters=[], pDefault="", pReplace=True):
        vRet = None
        try:
            vRet = pFilters[pFieldsFilters[0]][pFieldsFilters[1]][pFieldsFilters[2]]
        except Exception as e:
            pass

        return funcs_sql.strClean(vRet, pDefault, pReplace)
