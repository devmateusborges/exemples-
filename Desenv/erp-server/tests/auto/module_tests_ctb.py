from flask import url_for


from generic_tests import generic_tests
import module_tests_ger
import module_tests_sys
import module_tests_ope


class module_tests_ctb(generic_tests):

    # ===========================================================
    # ctb_versao
    # ===========================================================

    # ====================

    def ctb_versao_id1(self):

        req_post = {
            "id": self.get_id_fixed("ctb_versao_id1"),
            "ativo": "S",
            "data_per_fin": "02/01/2022",
            "data_per_ini": "21/07/2022",
            "nome": "TESTE [CRUD]",
            "sigla_versao": "TESTE [CRUD]",
            "tipo_rp": "R",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "versao_atual": "S",
        }

        response = self.client.post(
            url_for("ctbversao.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_versao_id2(self):

        req_post = {
            "id": self.get_id_fixed("ctb_versao_id2"),
            "ativo": "S",
            "data_per_fin": "02/01/2022",
            "data_per_ini": "21/07/2022",
            "nome": "TESTE [CRUD]",
            "sigla_versao": "TESTE [CRUD]",
            "tipo_rp": "R",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "versao_atual": "S",
        }

        response = self.client.post(
            url_for("ctbversao.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_versao_get(self):
        response = self.client.get(
            url_for("ctbversao.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ctb_versao_get_by_id(self):
        response = self.client.get(
            url_for("ctbversao.find_by_id", id=self.get_id_fixed("ctb_versao_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ctb_versao_delete(self):
        response = self.client.delete(
            url_for("ctbversao.delete", id=self.get_id_fixed("ctb_versao_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ctb_centro_grupo
    # ===========================================================

    # ====================

    def ctb_centro_grupo_id1(self):

        req_post = {
            "id": self.get_id_fixed("ctb_centro_grupo_id1"),
            "ativo": "S",
            "nome": "TESTE [CRUD]",
            "sigla_centro_grupo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("ctbcentrogrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_centro_grupo_id2(self):

        req_post = {
            "id": self.get_id_fixed("ctb_centro_grupo_id2"),
            "ativo": "S",
            "nome": "TESTE [CRUD]",
            "sigla_centro_grupo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("ctbcentrogrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_centro_grupo_get(self):
        response = self.client.get(
            url_for("ctbcentrogrupo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ctb_centro_grupo_get_by_id(self):
        response = self.client.get(
            url_for(
                "ctbcentrogrupo.find_by_id",
                id=self.get_id_fixed("ctb_centro_grupo_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ctb_centro_grupo_delete(self):
        response = self.client.delete(
            url_for(
                "ctbcentrogrupo.delete", id=self.get_id_fixed("ctb_centro_grupo_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ctb_comp_grupo
    # ===========================================================

    # ====================

    def ctb_comp_grupo_id1(self):

        req_post = {
            "id": self.get_id_fixed("ctb_comp_grupo_id1"),
            "ativo": "S",
            "nome": "TESTE [CRUD]",
            "sigla_comp_grupo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("ctbcompgrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_comp_grupo_id2(self):

        req_post = {
            "id": self.get_id_fixed("ctb_comp_grupo_id2"),
            "ativo": "S",
            "nome": "TESTE [CRUD]",
            "sigla_comp_grupo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("ctbcompgrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_comp_grupo_get(self):
        response = self.client.get(
            url_for("ctbcompgrupo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ctb_comp_grupo_get_by_id(self):
        response = self.client.get(
            url_for(
                "ctbcompgrupo.find_by_id", id=self.get_id_fixed("ctb_comp_grupo_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ctb_comp_grupo_delete(self):
        response = self.client.delete(
            url_for("ctbcompgrupo.delete", id=self.get_id_fixed("ctb_comp_grupo_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ctb_conta_versao
    # ===========================================================

    # ====================

    def ctb_conta_versao_id1(self):

        req_post = {
            "id": self.get_id_fixed("ctb_conta_versao_id1"),
            "ativo": "S",
            "data_valid_ini": "29/07/2022",
            "nome": "TESTE [CRUD]",
            "sigla_versao": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "versao_atual": "S",
        }

        response = self.client.post(
            url_for("ctbcontaversao.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_conta_versao_id2(self):

        req_post = {
            "id": self.get_id_fixed("ctb_conta_versao_id2"),
            "ativo": "S",
            "data_valid_ini": "29/07/2022",
            "nome": "TESTE [CRUD]",
            "sigla_versao": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "versao_atual": "S",
        }

        response = self.client.post(
            url_for("ctbcontaversao.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_conta_versao_get(self):
        response = self.client.get(
            url_for("ctbcontaversao.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ctb_conta_versao_get_by_id(self):
        response = self.client.get(
            url_for(
                "ctbcontaversao.find_by_id",
                id=self.get_id_fixed("ctb_conta_versao_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ctb_conta_versao_delete(self):
        response = self.client.delete(
            url_for(
                "ctbcontaversao.delete", id=self.get_id_fixed("ctb_conta_versao_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ctb_historico
    # ===========================================================

    # ====================

    def ctb_historico_id1(self):
        req_post = {
            "id": self.get_id_fixed("ctb_historico_id1"),
            "ativo": "S",
            "nome": "TESTE [CRUD]",
            "sigla_historico": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("ctbhistorico.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_historico_id2(self):
        req_post = {
            "id": self.get_id_fixed("ctb_historico_id2"),
            "ativo": "S",
            "nome": "TESTE [CRUD]",
            "sigla_historico": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("ctbhistorico.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_historico_get(self):
        response = self.client.get(
            url_for("ctbhistorico.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ctb_historico_get_by_id(self):
        response = self.client.get(
            url_for(
                "ctbhistorico.find_by_id", id=self.get_id_fixed("ctb_historico_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ctb_historico_delete(self):
        response = self.client.delete(
            url_for("ctbhistorico.delete", id=self.get_id_fixed("ctb_historico_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ctb_lote
    # ===========================================================

    # ====================

    def ctb_lote_id1(self):

        req_post = {
            "id": self.get_id_fixed("ctb_lote_id1"),
            "ativo": "S",
            "nome": "TESTE [CRUD]",
            "sigla_lote": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("ctblote.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_lote_id2(self):

        req_post = {
            "id": self.get_id_fixed("ctb_lote_id2"),
            "ativo": "S",
            "nome": "TESTE [CRUD]",
            "sigla_lote": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("ctblote.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_lote_get(self):
        response = self.client.get(
            url_for("ctblote.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ctb_lote_get_by_id(self):
        response = self.client.get(
            url_for("ctblote.find_by_id", id=self.get_id_fixed("ctb_lote_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ctb_lote_delete(self):
        response = self.client.delete(
            url_for("ctblote.delete", id=self.get_id_fixed("ctb_lote_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ctb_tipo_saldo
    # ===========================================================

    # ====================

    def ctb_tipo_saldo_id1(self):

        req_post = {
            "id": self.get_id_fixed("ctb_tipo_saldo_id1"),
            "ativo": "S",
            "mes_fin_fechamento": "15",
            "mes_ini_fechamento": "23",
            "nome": "TESTE [CRUD]",
            "sigla_lote": "TESTE [CRUD]",
            "sigla_tipo_saldo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("ctbtiposaldo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_tipo_saldo_id2(self):

        req_post = {
            "id": self.get_id_fixed("ctb_tipo_saldo_id2"),
            "ativo": "S",
            "mes_fin_fechamento": "15",
            "mes_ini_fechamento": "23",
            "nome": "TESTE [CRUD]",
            "sigla_lote": "TESTE [CRUD]",
            "sigla_tipo_saldo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("ctbtiposaldo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_tipo_saldo_get(self):
        response = self.client.get(
            url_for("ctbtiposaldo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ctb_tipo_saldo_get_by_id(self):
        response = self.client.get(
            url_for(
                "ctbtiposaldo.find_by_id", id=self.get_id_fixed("ctb_tipo_saldo_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ctb_tipo_saldo_delete(self):
        response = self.client.delete(
            url_for("ctbtiposaldo.delete", id=self.get_id_fixed("ctb_tipo_saldo_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ctb_unit_param
    # ===========================================================

    # ====================

    def ctb_unit_param_id1(self):

        req_post = {
            "id": self.get_id_fixed("ctb_unit_param_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_valid_ini": "2022-12-29T00:00:00",
        }

        response = self.client.post(
            url_for("ctbunitparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_unit_param_id2(self):

        req_post = {
            "id": self.get_id_fixed("ctb_unit_param_id2"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_valid_ini": "2022-12-29T00:00:00",
        }

        response = self.client.post(
            url_for("ctbunitparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_unit_param_get(self):
        response = self.client.get(
            url_for("ctbunitparam.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ctb_unit_param_get_by_id(self):
        response = self.client.get(
            url_for(
                "ctbunitparam.find_by_id", id=self.get_id_fixed("ctb_unit_param_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ctb_unit_param_delete(self):
        response = self.client.delete(
            url_for("ctbunitparam.delete", id=self.get_id_fixed("ctb_unit_param_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ctb_unit_param
    # ===========================================================

    # ====================

    def ctb_centro_id1(self):

        req_post = {
            "id": self.get_id_fixed("ctb_centro_id1"),
            "ativo": "S",
            "sigla_centro": "TESTE [CRUD]",
            "ctb_centro_grupo_id": module_tests_ctb.ctb_centro_grupo_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "nome": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("ctbcentro.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_centro_id2(self):

        req_post = {
            "id": self.get_id_fixed("ctb_centro_id2"),
            "ativo": "S",
            "sigla_centro": "TESTE [CRUD]",
            "ctb_centro_grupo_id": module_tests_ctb.ctb_centro_grupo_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "nome": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("ctbcentro.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_centro_get(self):
        response = self.client.get(
            url_for("ctbcentro.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ctb_centro_get_by_id(self):
        response = self.client.get(
            url_for("ctbcentro.find_by_id", id=self.get_id_fixed("ctb_centro_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ctb_centro_delete(self):
        response = self.client.delete(
            url_for("ctbcentro.delete", id=self.get_id_fixed("ctb_centro_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ctb_comp
    # ===========================================================

    # ====================

    def ctb_comp_id1(self):

        req_post = {
            "id": self.get_id_fixed("ctb_comp_id1"),
            "ativo": "S",
            "ctb_comp_grupo_id": module_tests_ctb.ctb_comp_grupo_id1(self),
            "ctb_comp_id_calc_orig": "S",
            "fator_calc_origem": "12",
            "ger_umedida_id": module_tests_ger.module_tests_ger.ger_umedida_id1(self),
            "nome": "TESTE [CRUD]",
            "sigla_comp": "S",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("ctbcomp.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_comp_id2(self):

        req_post = {
            "id": self.get_id_fixed("ctb_comp_id2"),
            "ativo": "S",
            "ctb_comp_grupo_id": module_tests_ctb.ctb_comp_grupo_id1(self),
            "ctb_comp_id_calc_orig": "S",
            "fator_calc_origem": "12",
            "ger_umedida_id": module_tests_ger.module_tests_ger.ger_umedida_id1(self),
            "nome": "TESTE [CRUD]",
            "sigla_comp": "S",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("ctbcomp.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_comp_get(self):
        response = self.client.get(
            url_for("ctbcomp.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ctb_comp_get_by_id(self):
        response = self.client.get(
            url_for("ctbcomp.find_by_id", id=self.get_id_fixed("ctb_comp_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ctb_comp_delete(self):
        response = self.client.delete(
            url_for("ctbcomp.delete", id=self.get_id_fixed("ctb_comp_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ctb_conta_grupo
    # ===========================================================

    # ====================

    def ctb_conta_grupo_id1(self):

        req_post = {
            "id": self.get_id_fixed("ctb_conta_grupo_id1"),
            "ativo": "S",
            "ctb_conta_versao_id": module_tests_ctb.ctb_conta_versao_id1(self),
            "estrutura": "TESTE [CRUD]",
            "nome": "TESTE [CRUD]",
            "sigla_conta_grupo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("ctbcontagrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_conta_grupo_id2(self):

        req_post = {
            "id": self.get_id_fixed("ctb_conta_grupo_id2"),
            "ativo": "S",
            "ctb_conta_versao_id": module_tests_ctb.ctb_conta_versao_id1(self),
            "estrutura": "TESTE [CRUD]",
            "nome": "TESTE [CRUD]",
            "sigla_conta_grupo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("ctbcontagrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_conta_grupo_get(self):
        response = self.client.get(
            url_for("ctbcontagrupo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ctb_conta_grupo_get_by_id(self):
        response = self.client.get(
            url_for(
                "ctbcontagrupo.find_by_id", id=self.get_id_fixed("ctb_conta_grupo_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ctb_conta_grupo_delete(self):

        response = self.client.delete(
            url_for(
                "ctbcontagrupo.delete", id=self.get_id_fixed("ctb_conta_grupo_id2")
            ),
            headers=self.create_token(),
        )

        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ctb_lanc
    # ===========================================================

    # ====================

    def ctb_lanc_id1(self):

        req_post = {
            "id": self.get_id_fixed("ctb_lanc_id1"),
            "ctb_historico_id": module_tests_ctb.ctb_historico_id1(self),
            "ctb_lote_id": module_tests_ctb.ctb_lote_id1(self),
            "ctb_versao_id": module_tests_ctb.ctb_versao_id1(self),
            "data_lanc": "12/05/2022",
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "historico": "TESTE [CRUD]",
            "numero_lanc": "5",
            "status": "PD",
            "status_observacao": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("ctblanc.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_lanc_id2(self):

        req_post = {
            "id": self.get_id_fixed("ctb_lanc_id2"),
            "ctb_historico_id": module_tests_ctb.ctb_historico_id1(self),
            "ctb_lote_id": module_tests_ctb.ctb_lote_id1(self),
            "ctb_versao_id": module_tests_ctb.ctb_versao_id1(self),
            "data_lanc": "12/05/2022",
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "historico": "TESTE [CRUD]",
            "numero_lanc": "5",
            "status": "PD",
            "status_observacao": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("ctblanc.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_lanc_get(self):
        response = self.client.get(
            url_for("ctblanc.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ctb_lanc_get_by_id(self):
        response = self.client.get(
            url_for("ctblanc.find_by_id", id=self.get_id_fixed("ctb_lanc_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ctb_lanc_delete(self):
        response = self.client.delete(
            url_for("ctblanc.delete", id=self.get_id_fixed("ctb_lanc_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ctb_lanc_det
    # ===========================================================

    # ====================

    def ctb_lanc_det_id1(self):

        req_post = {
            "id": self.get_id_fixed("ctb_lanc_det_id1"),
            "ctb_comp_id": module_tests_ctb.ctb_comp_id1(self),
            "ctb_conta_id": module_tests_ctb.ctb_conta_id1(self),
            "ctb_lanc_id": module_tests_ctb.ctb_lanc_id1(self),
            "observacao": "TESTE [CRUD]",
            "origem_tipo": "t",
            "process_id": module_tests_sys.module_tests_sys.sys_process_log_id1(self),
            "qnt": "5",
            "tipo_dc": "D",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor": "5",
            "ope_centro2_id": module_tests_ope.module_tests_ope.ope_centro2_id1(self),
            "origem_id": "TESTE [CRUD]1",
            "ope_atividade_id": module_tests_ope.module_tests_ope.ope_atividade_id1(
                self
            ),
        }

        response = self.client.post(
            url_for("ctblancdet.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_lanc_det_id2(self):

        req_post = {
            "id": self.get_id_fixed("ctb_lanc_det_id2"),
            "ctb_comp_id": module_tests_ctb.ctb_comp_id1(self),
            "ctb_conta_id": module_tests_ctb.ctb_conta_id1(self),
            "ctb_lanc_id": module_tests_ctb.ctb_lanc_id1(self),
            "observacao": "TESTE [CRUD]",
            "origem_tipo": "t",
            "process_id": module_tests_sys.module_tests_sys.sys_process_log_id1(self),
            "qnt": "5",
            "tipo_dc": "D",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor": "5",
            "ope_centro2_id": module_tests_ope.module_tests_ope.ope_centro2_id1(self),
            "origem_id": "TESTE [CRUD]1",
            "ope_atividade_id": module_tests_ope.module_tests_ope.ope_atividade_id1(
                self
            ),
        }

        response = self.client.post(
            url_for("ctblancdet.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_lanc_det_get(self):
        response = self.client.get(
            url_for("ctblancdet.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ctb_lanc_det_get_by_id(self):
        response = self.client.get(
            url_for("ctblancdet.find_by_id", id=self.get_id_fixed("ctb_lanc_det_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ctb_lanc_det_delete(self):
        response = self.client.delete(
            url_for("ctblancdet.delete", id=self.get_id_fixed("ctb_lanc_det_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ctb_conta
    # ===========================================================

    # ====================

    def ctb_conta_id1(self):

        req_post = {
            "id": self.get_id_fixed("ctb_conta_id1"),
            "ativo": "S",
            "ctb_conta_grupo_id": module_tests_ctb.ctb_conta_grupo_id1(self),
            "ctb_conta_versao_id": module_tests_ctb.ctb_conta_versao_id1(self),
            "nome": "TESTE [CRUD]",
            "sigla_conta": "TESTE [CRUD]",
            "tipo_conta": "1",
            "tipo_dc": "D",
            "tipo_variacao": "F",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("ctbconta.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_conta_id2(self):

        req_post = {
            "id": self.get_id_fixed("ctb_conta_id2"),
            "ativo": "S",
            "ctb_conta_grupo_id": module_tests_ctb.ctb_conta_grupo_id1(self),
            "ctb_conta_versao_id": module_tests_ctb.ctb_conta_versao_id1(self),
            "nome": "TESTE [CRUD]",
            "sigla_conta": "TESTE [CRUD]",
            "tipo_conta": "1",
            "tipo_dc": "D",
            "tipo_variacao": "F",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("ctbconta.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ctb_conta_get(self):
        response = self.client.get(
            url_for("ctbconta.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ctb_conta_get_by_id(self):
        response = self.client.get(
            url_for("ctbconta.find_by_id", id=self.get_id_fixed("ctb_conta_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ctb_conta_delete(self):
        response = self.client.delete(
            url_for("ctbconta.delete", id=self.get_id_fixed("ctb_conta_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)
