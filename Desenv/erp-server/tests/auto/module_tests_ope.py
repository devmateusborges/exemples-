from flask import url_for

from generic_tests import generic_tests
import module_tests_ctb
import module_tests_fin
import module_tests_ger
import module_tests_sys
import module_tests_mov


class module_tests_ope(generic_tests):

    # ===========================================================
    # ope_centro_tipo
    # ===========================================================

    # ====================

    def ope_centro_tipo_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro_tipo_id1"),
            "nome": "TESTE [CRUD]",
            "tipo_es": "E",
        }

        response = self.client.post(
            url_for("opecentrotipo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro_tipo_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro_tipo_id2"),
            "nome": "TESTE [CRUD]",
            "tipo_es": "E",
        }

        response = self.client.post(
            url_for("opecentrotipo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro_tipo_get(self):
        response = self.client.get(
            url_for("opecentrotipo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_centro_tipo_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecentrotipo.find_by_id", id=self.get_id_fixed("ope_centro_tipo_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_centro_tipo_delete(self):
        response = self.client.delete(
            url_for(
                "opecentrotipo.delete", id=self.get_id_fixed("ope_centro_tipo_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_centro_tipo
    # ===========================================================

    # ====================

    def ope_atividade_grupo_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_atividade_grupo_id1"),
            "nome": "TESTE [CRUD]",
            "ordem": "55",
            "sigla_atividade_grupo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opeatividadegrupo.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_atividade_grupo_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_atividade_grupo_id2"),
            "nome": "TESTE [CRUD]",
            "ordem": "55",
            "sigla_atividade_grupo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opeatividadegrupo.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_atividade_grupo_get(self):
        response = self.client.get(
            url_for("opeatividadegrupo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_atividade_grupo_get_by_id(self):
        response = self.client.get(
            url_for(
                "opeatividadegrupo.find_by_id",
                id=self.get_id_fixed("ope_atividade_grupo_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_atividade_grupo_delete(self):
        response = self.client.delete(
            url_for(
                "opeatividadegrupo.delete",
                id=self.get_id_fixed("ope_atividade_grupo_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_atividade_sistema
    # ===========================================================

    # ====================

    def ope_atividade_sistema_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_atividade_sistema_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_atividade_sistema": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opeatividadesistema.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_atividade_sistema_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_atividade_sistema_id2"),
            "nome": "TESTE [CRUD]",
            "sigla_atividade_sistema": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opeatividadesistema.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_atividade_sistema_get(self):
        response = self.client.get(
            url_for("opeatividadesistema.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_atividade_sistema_get_by_id(self):
        response = self.client.get(
            url_for(
                "opeatividadesistema.find_by_id",
                id=self.get_id_fixed("ope_atividade_sistema_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_atividade_sistema_delete(self):
        response = self.client.delete(
            url_for(
                "opeatividadesistema.delete",
                id=self.get_id_fixed("ope_atividade_sistema_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_centro2_ord_status
    # ===========================================================

    # ====================

    def ope_centro2_ord_status_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro2_ord_status_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_ord_status": "TESTE [CRUD]",
            "tipo_status": "L",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opecentro2ordstatus.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro2_ord_status_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro2_ord_status_id2"),
            "nome": "TESTE [CRUD]",
            "sigla_ord_status": "TESTE [CRUD]",
            "tipo_status": "L",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opecentro2ordstatus.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro2_ord_status_get(self):
        response = self.client.get(
            url_for("opecentro2ordstatus.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_centro2_ord_status_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecentro2ordstatus.find_by_id",
                id=self.get_id_fixed("ope_centro2_ord_status_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_centro2_ord_status_delete(self):
        response = self.client.delete(
            url_for(
                "opecentro2ordstatus.delete",
                id=self.get_id_fixed("ope_centro2_ord_status_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_centro2_ord_tipo
    # ===========================================================

    # ====================

    def ope_centro2_ord_tipo_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro2_ord_tipo_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_ord_tipo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valida_itemserv_i": "B",
            "valida_itemserv_s": "B",
            "valida_prev_itemserv": "S",
            "valida_prev_rec": "A",
            "valida_rec_equip": "S",
            "valida_rec_pessoa": "S",
            "valida_regra_config": "S",
            "valida_saldo_area_aberta": "S",
            "valida_tipo_executor": "SP",
            "valida_tipo_prop_rec_equip": "ST",
            "valida_tipo_prop_rec_pessoa": "SP",
        }

        response = self.client.post(
            url_for("opecentro2ordtipo.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro2_ord_tipo_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro2_ord_tipo_id2"),
            "nome": "TESTE [CRUD]",
            "sigla_ord_tipo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valida_itemserv_i": "B",
            "valida_itemserv_s": "B",
            "valida_prev_itemserv": "S",
            "valida_prev_rec": "A",
            "valida_rec_equip": "S",
            "valida_rec_pessoa": "S",
            "valida_regra_config": "S",
            "valida_saldo_area_aberta": "S",
            "valida_tipo_executor": "SP",
            "valida_tipo_prop_rec_equip": "ST",
            "valida_tipo_prop_rec_pessoa": "SP",
        }

        response = self.client.post(
            url_for("opecentro2ordtipo.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro2_ord_tipo_get(self):
        response = self.client.get(
            url_for("opecentro2ordtipo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_centro2_ord_tipo_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecentro2ordtipo.find_by_id",
                id=self.get_id_fixed("ope_centro2_ord_tipo_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_centro2_ord_tipo_delete(self):
        response = self.client.delete(
            url_for(
                "opecentro2ordtipo.delete",
                id=self.get_id_fixed("ope_centro2_ord_tipo_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_centro_subtipo
    # ===========================================================

    # ====================

    def ope_centro_subtipo_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro_subtipo_id1"),
            "nome": "TESTE [CRUD]",
            "ope_centro_tipo_id": module_tests_ope.ope_centro_tipo_id1(self),
            "tipo_destinacao": "T",
            "sigla_centro_subtipo": "TESTE [CRUD]1",
        }

        response = self.client.post(
            url_for("opecentrosubtipo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro_subtipo_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro_subtipo_id2"),
            "nome": "TESTE [CRUD]",
            "ope_centro_tipo_id": module_tests_ope.ope_centro_tipo_id1(self),
            "tipo_destinacao": "T",
            "sigla_centro_subtipo": "TESTE [CRUD]2",
        }

        response = self.client.post(
            url_for("opecentrosubtipo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro_subtipo_get(self):
        response = self.client.get(
            url_for("opecentrosubtipo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_centro_subtipo_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecentrosubtipo.find_by_id",
                id=self.get_id_fixed("ope_centro_subtipo_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_centro_subtipo_delete(self):
        response = self.client.delete(
            url_for(
                "opecentrosubtipo.delete",
                id=self.get_id_fixed("ope_centro_subtipo_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_centro_versao
    # ===========================================================

    # ====================

    def ope_centro_versao_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro_versao_id1"),
            "data_per_fin": "15/07/2022",
            "data_per_ini": "15/07/2022",
            "nome": "TESTE [CRUD]",
            "sigla_versao": "TESTE [CRUD]",
            "tipo_per": "A",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "versao_atual": "S",
        }

        response = self.client.post(
            url_for("opecentroversao.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro_versao_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro_versao_id2"),
            "data_per_fin": "15/07/2022",
            "data_per_ini": "15/07/2022",
            "nome": "TESTE [CRUD]",
            "sigla_versao": "TESTE [CRUD]",
            "tipo_per": "A",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "versao_atual": "S",
        }

        response = self.client.post(
            url_for("opecentroversao.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro_versao_get(self):
        response = self.client.get(
            url_for("opecentroversao.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_centro_versao_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecentroversao.find_by_id",
                id=self.get_id_fixed("ope_centro_versao_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_centro_versao_delete(self):
        response = self.client.delete(
            url_for(
                "opecentroversao.delete", id=self.get_id_fixed("ope_centro_versao_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_ciclo_var
    # ===========================================================

    # ====================

    def ope_ciclo_var_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_ciclo_var_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_ope_ciclo_var": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opeciclovar.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_ciclo_var_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_ciclo_var_id2"),
            "nome": "TESTE [CRUD]",
            "sigla_ope_ciclo_var": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opeciclovar.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_ciclo_var_get(self):
        response = self.client.get(
            url_for("opeciclovar.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_ciclo_var_get_by_id(self):
        response = self.client.get(
            url_for(
                "opeciclovar.find_by_id", id=self.get_id_fixed("ope_ciclo_var_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_ciclo_var_delete(self):
        response = self.client.delete(
            url_for("opeciclovar.delete", id=self.get_id_fixed("ope_ciclo_var_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_compart_grupo
    # ===========================================================

    # ====================

    def ope_compart_grupo_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_compart_grupo_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_compart_grupo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opecompartgrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_compart_grupo_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_compart_grupo_id2"),
            "nome": "TESTE [CRUD]",
            "sigla_compart_grupo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opecompartgrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_compart_grupo_get(self):
        response = self.client.get(
            url_for("opecompartgrupo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_compart_grupo_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecompartgrupo.find_by_id",
                id=self.get_id_fixed("ope_compart_grupo_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_compart_grupo_delete(self):
        response = self.client.delete(
            url_for(
                "opecompartgrupo.delete", id=self.get_id_fixed("ope_compart_grupo_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_compart_medida
    # ===========================================================

    # ====================

    def ope_compart_medida_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_compart_medida_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_compart_medida": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opecompartmedida.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_compart_medida_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_compart_medida_id2"),
            "nome": "TESTE [CRUD]",
            "sigla_compart_medida": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opecompartmedida.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_compart_medida_get(self):
        response = self.client.get(
            url_for("opecompartmedida.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_compart_medida_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecompartmedida.find_by_id",
                id=self.get_id_fixed("ope_compart_medida_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_compart_medida_delete(self):
        response = self.client.delete(
            url_for(
                "opecompartmedida.delete",
                id=self.get_id_fixed("ope_compart_medida_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_compart_posicao
    # ===========================================================

    # ====================

    def ope_compart_posicao_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_compart_posicao_id1"),
            "banda_montagem": "I",
            "lado_montagem": "D",
            "nome": "TESTE [CRUD]",
            "numero_eixo": "2",
            "posicao": "D",
            "sigla_compart_posicao": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opecompartposicao.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_compart_posicao_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_compart_posicao_id2"),
            "banda_montagem": "I",
            "lado_montagem": "D",
            "nome": "TESTE [CRUD]",
            "numero_eixo": "2",
            "posicao": "D",
            "sigla_compart_posicao": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opecompartposicao.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_compart_posicao_get(self):
        response = self.client.get(
            url_for("opecompartposicao.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_compart_posicao_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecompartposicao.find_by_id",
                id=self.get_id_fixed("ope_compart_posicao_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_compart_posicao_delete(self):
        response = self.client.delete(
            url_for(
                "opecompartposicao.delete",
                id=self.get_id_fixed("ope_compart_posicao_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_compart_status
    # ===========================================================

    # ====================

    def ope_compart_status_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_compart_status_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_compart_status": "TESTE [CRUD]",
            "tipo_status": "M",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opecompartstatus.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_compart_status_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_compart_status_id2"),
            "nome": "TESTE [CRUD]",
            "sigla_compart_status": "TESTE [CRUD]",
            "tipo_status": "M",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opecompartstatus.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_compart_status_get(self):
        response = self.client.get(
            url_for("opecompartstatus.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_compart_status_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecompartstatus.find_by_id",
                id=self.get_id_fixed("ope_compart_status_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_compart_status_delete(self):
        response = self.client.delete(
            url_for(
                "opecompartstatus.delete",
                id=self.get_id_fixed("ope_compart_status_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_espac
    # ===========================================================

    # ====================

    def ope_espac_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_espac_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_espac": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opeespac.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_espac_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_espac_id2"),
            "nome": "TESTE [CRUD]",
            "sigla_espac": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opeespac.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_espac_get(self):
        response = self.client.get(
            url_for("opeespac.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_espac_get_by_id(self):
        response = self.client.get(
            url_for("opeespac.find_by_id", id=self.get_id_fixed("ope_espac_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_espac_delete(self):
        response = self.client.delete(
            url_for("opeespac.delete", id=self.get_id_fixed("ope_espac_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_estagio
    # ===========================================================

    # ====================

    def ope_estagio_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_estagio_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_estagio": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opeestagio.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_estagio_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_estagio_id2"),
            "nome": "TESTE [CRUD]",
            "sigla_estagio": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opeestagio.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_estagio_get(self):
        response = self.client.get(
            url_for("opeestagio.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_estagio_get_by_id(self):
        response = self.client.get(
            url_for("opeestagio.find_by_id", id=self.get_id_fixed("ope_estagio_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_estagio_delete(self):
        response = self.client.delete(
            url_for("opeestagio.delete", id=self.get_id_fixed("ope_estagio_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_ocor_grupo
    # ===========================================================

    # ====================

    def ope_ocor_grupo_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_ocor_grupo_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_ocor_grupo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opeocorgrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_ocor_grupo_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_ocor_grupo_id2"),
            "nome": "TESTE [CRUD]",
            "sigla_ocor_grupo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opeocorgrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_ocor_grupo_get(self):
        response = self.client.get(
            url_for("opeocorgrupo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_ocor_grupo_get_by_id(self):
        response = self.client.get(
            url_for(
                "opeocorgrupo.find_by_id", id=self.get_id_fixed("ope_ocor_grupo_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_ocor_grupo_delete(self):
        response = self.client.delete(
            url_for("opeocorgrupo.delete", id=self.get_id_fixed("ope_ocor_grupo_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_ocor_status
    # ===========================================================

    # ====================

    def ope_ocor_status_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_ocor_status_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_ocor_status": "TESTE [CRUD]",
            "tipo_status": "A",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opeocorstatus.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_ocor_status_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_ocor_status_id2"),
            "nome": "TESTE [CRUD]",
            "sigla_ocor_status": "TESTE [CRUD]",
            "tipo_status": "A",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opeocorstatus.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_ocor_status_get(self):
        response = self.client.get(
            url_for("opeocorstatus.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_ocor_status_get_by_id(self):
        response = self.client.get(
            url_for(
                "opeocorstatus.find_by_id", id=self.get_id_fixed("ope_ocor_status_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_ocor_status_delete(self):
        response = self.client.delete(
            url_for(
                "opeocorstatus.delete", id=self.get_id_fixed("ope_ocor_status_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_ocor_tipo
    # ===========================================================

    # ====================

    def ope_ocor_tipo_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_ocor_tipo_id1"),
            "nome": "TESTE [CRUD]",
            "obrig_ope_compart": "S",
            "sigla_ocor_tipo": "TESTE [CRUD]",
            "tipo": "A",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opeocortipo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_ocor_tipo_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_ocor_tipo_id2"),
            "nome": "TESTE [CRUD]",
            "obrig_ope_compart": "S",
            "sigla_ocor_tipo": "TESTE [CRUD]",
            "tipo": "A",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opeocortipo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_ocor_tipo_get(self):
        response = self.client.get(
            url_for("opeocortipo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_ocor_tipo_get_by_id(self):
        response = self.client.get(
            url_for(
                "opeocortipo.find_by_id", id=self.get_id_fixed("ope_ocor_tipo_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_ocor_tipo_delete(self):
        response = self.client.delete(
            url_for("opeocortipo.delete", id=self.get_id_fixed("ope_ocor_tipo_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_periodo
    # ===========================================================

    # ====================

    def ope_periodo_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_periodo_id1"),
            "data_fin": "15/07/2022",
            "data_ini": "15/07/2022",
            "nome": "TESTE [CRUD]",
            "sigla_periodo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opeperiodo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_periodo_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_periodo_id2"),
            "data_fin": "15/07/2022",
            "data_ini": "15/07/2022",
            "nome": "TESTE [CRUD]",
            "sigla_periodo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opeperiodo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_periodo_get(self):
        response = self.client.get(
            url_for("opeperiodo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_periodo_get_by_id(self):
        response = self.client.get(
            url_for("opeperiodo.find_by_id", id=self.get_id_fixed("ope_periodo_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_periodo_delete(self):
        response = self.client.delete(
            url_for("opeperiodo.delete", id=self.get_id_fixed("ope_periodo_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_regiao
    # ===========================================================

    # ====================

    def ope_regiao_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_regiao_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_regiao": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("operegiao.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_regiao_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_regiao_id2"),
            "nome": "TESTE [CRUD]",
            "sigla_regiao": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("operegiao.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_regiao_get(self):
        response = self.client.get(
            url_for("operegiao.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_regiao_get_by_id(self):
        response = self.client.get(
            url_for("operegiao.find_by_id", id=self.get_id_fixed("ope_regiao_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_regiao_delete(self):
        response = self.client.delete(
            url_for("operegiao.delete", id=self.get_id_fixed("ope_regiao_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_tipo_solo
    # ===========================================================

    # ====================

    def ope_tipo_solo_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_tipo_solo_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_tipo_solo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "S",
        }

        response = self.client.post(
            url_for("opetiposolo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_tipo_solo_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_tipo_solo_id2"),
            "nome": "TESTE [CRUD]",
            "sigla_tipo_solo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "S",
        }

        response = self.client.post(
            url_for("opetiposolo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_tipo_solo_get(self):
        response = self.client.get(
            url_for("opetiposolo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_tipo_solo_get_by_id(self):
        response = self.client.get(
            url_for(
                "opetiposolo.find_by_id", id=self.get_id_fixed("ope_tipo_solo_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_tipo_solo_delete(self):
        response = self.client.delete(
            url_for("opetiposolo.delete", id=self.get_id_fixed("ope_tipo_solo_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_unit_param
    # ===========================================================

    # ====================

    def ope_unit_param_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_unit_param_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_valid_ini": "2022-12-29T00:00:00",
        }

        response = self.client.post(
            url_for("opeunitparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_unit_param_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_unit_param_id2"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_valid_ini": "2022-12-29T00:00:00",
        }

        response = self.client.post(
            url_for("opeunitparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_unit_param_get(self):
        response = self.client.get(
            url_for("opeunitparam.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_unit_param_get_by_id(self):
        response = self.client.get(
            url_for(
                "opeunitparam.find_by_id", id=self.get_id_fixed("ope_unit_param_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_unit_param_delete(self):
        response = self.client.delete(
            url_for("opeunitparam.delete", id=self.get_id_fixed("ope_unit_param_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_atividade
    # ===========================================================

    # ====================

    def ope_atividade_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_atividade_id1"),
            "ger_umedida_id": module_tests_ger.module_tests_ger.ger_umedida_id1(self),
            "index_bor": "TESTE [CRUD]",
            "largura": "5",
            "nome": "TESTE [CRUD]",
            "ope_atividade_grupo_id": module_tests_ope.ope_atividade_grupo_id1(self),
            "parada": "S",
            "sigla_atividade": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valida_itemserv_i": "S",
            "valida_itemserv_s": "S",
            "valida_prev_itemserv": "S",
            "valida_prev_rec": "S",
            "valida_rec_equip": "S",
            "valida_rec_pessoa": "S",
            "valida_regra_config": "S",
            "valida_saldo_area_aberta": "A",
            "valida_seq_medicao_trab_centro": "S",
            "valida_tipo_executor": "SP",
            "valida_tipo_prop_rec_equip": "SP",
            "valida_tipo_prop_rec_pessoa": "SP",
            "valida_tot_area_acum_per_centro_exec": "A",
            "valida_tot_area_acum_per_centro_plan": "SP",
            "valida_tot_area_ord_exec": "S",
        }

        response = self.client.post(
            url_for("opeatividade.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_atividade_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_atividade_id2"),
            "ger_umedida_id": module_tests_ger.module_tests_ger.ger_umedida_id1(self),
            "index_bor": "TESTE [CRUD]",
            "largura": "5",
            "nome": "TESTE [CRUD]",
            "ope_atividade_grupo_id": module_tests_ope.ope_atividade_grupo_id1(self),
            "parada": "S",
            "sigla_atividade": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valida_itemserv_i": "S",
            "valida_itemserv_s": "S",
            "valida_prev_itemserv": "S",
            "valida_prev_rec": "S",
            "valida_rec_equip": "S",
            "valida_rec_pessoa": "S",
            "valida_regra_config": "S",
            "valida_saldo_area_aberta": "S",
            "valida_seq_medicao_trab_centro": "S",
            "valida_tipo_executor": "SP",
            "valida_tipo_prop_rec_equip": "SP",
            "valida_tipo_prop_rec_pessoa": "SP",
            "valida_tot_area_acum_per_centro_exec": "A",
            "valida_tot_area_acum_per_centro_plan": "SP",
            "valida_tot_area_ord_exec": "S",
            "ope_atividadeprod_childs": [
                {
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "ope_atividade_id": module_tests_ope.ope_atividade_id1(self),
                    "ordem_visual": "S",
                    "ope_atividade_id_prod": module_tests_ope.ope_atividade_id1(self),
                }
            ],
        }

        response = self.client.post(
            url_for("opeatividade.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_atividade_get(self):
        response = self.client.get(
            url_for("opeatividade.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_atividade_get_by_id(self):
        response = self.client.get(
            url_for(
                "opeatividade.find_by_id", id=self.get_id_fixed("ope_atividade_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_atividade_delete(self):
        response = self.client.delete(
            url_for("opeatividade.delete", id=self.get_id_fixed("ope_atividade_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_centro_grupo
    # ===========================================================

    # ====================

    def ope_centro_grupo_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro_grupo_id1"),
            "nome": "TESTE [CRUD]",
            "ope_centro_subtipo_id": module_tests_ope.ope_centro_subtipo_id1(self),
            "sigla_centro_grupo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opecentrogrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro_grupo_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro_grupo_id2"),
            "nome": "TESTE [CRUD]",
            "ope_centro_subtipo_id": module_tests_ope.ope_centro_subtipo_id1(self),
            "sigla_centro_grupo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opecentrogrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro_grupo_get(self):
        response = self.client.get(
            url_for("opecentrogrupo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_centro_grupo_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecentrogrupo.find_by_id",
                id=self.get_id_fixed("ope_centro_grupo_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_centro_grupo_delete(self):
        response = self.client.delete(
            url_for(
                "opecentrogrupo.delete", id=self.get_id_fixed("ope_centro_grupo_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_centro_rat_tipo
    # ===========================================================

    # ====================

    def ope_centro_rat_tipo_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro_rat_tipo_id1"),
            "nome": "TESTE [CRUD]",
            "observacao": "TESTE [CRUD]",
            "ope_centro_versao_id": module_tests_ope.ope_centro_versao_id1(self),
            "sigla_centro_rat_tipo": "TESTE [CRUD]",
            "tipo_apur": "R",
            "tipo_ps": "P",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "N",
        }

        response = self.client.post(
            url_for("opecentrorattipo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro_rat_tipo_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro_rat_tipo_id2"),
            "nome": "TESTE [CRUD]",
            "observacao": "TESTE [CRUD]",
            "ope_centro_versao_id": module_tests_ope.ope_centro_versao_id1(self),
            "sigla_centro_rat_tipo": "TESTE [CRUD]",
            "tipo_apur": "R",
            "tipo_ps": "P",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "N",
            "ope_centro_rat_periodo_childs": [
                {
                    "data_ini": "29/12/2003",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "tipo_rp": "P",
                    "ope_centro_rat_fator_childs": [
                        {
                            "ope_centro1_id": module_tests_ope.ope_centro1_id1(self),
                            "ctb_centro_id": module_tests_ctb.module_tests_ctb.ctb_centro_id1(
                                self
                            ),
                            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(
                                self
                            ),
                            "ope_periodo_id": module_tests_ope.ope_periodo_id1(self),
                            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(
                                self
                            ),
                            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
                            "perc_rat": "5",
                            "fator_rat": "5",
                            "ope_centro_subtipo_id": module_tests_ope.ope_centro_subtipo_id1(
                                self
                            ),
                        }
                    ],
                }
            ],
        }

        response = self.client.post(
            url_for("opecentrorattipo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro_rat_tipo_get(self):
        response = self.client.get(
            url_for("opecentrorattipo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_centro_rat_tipo_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecentrorattipo.find_by_id",
                id=self.get_id_fixed("ope_centro_rat_tipo_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_centro_rat_tipo_delete(self):
        response = self.client.delete(
            url_for(
                "opecentrorattipo.delete",
                id=self.get_id_fixed("ope_centro_rat_tipo_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_compart_ocor
    # ===========================================================

    # ====================

    def ope_compart_ocor_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_compart_ocor_id1"),
            "nome": "TESTE [CRUD]",
            "tipo_ocor": "M",
            "sigla_compart_ocor": "TESTE [CRUD]",
            "ope_compart_status_id": module_tests_ope.ope_compart_status_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "S",
        }

        response = self.client.post(
            url_for("opecompartocor.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_compart_ocor_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_compart_ocor_id2"),
            "nome": "TESTE [CRUD]",
            "tipo_ocor": "M",
            "sigla_compart_ocor": "TESTE [CRUD]",
            "ope_compart_status_id": module_tests_ope.ope_compart_status_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "S",
        }

        response = self.client.post(
            url_for("opecompartocor.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_compart_ocor_get(self):
        response = self.client.get(
            url_for("opecompartocor.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_compart_ocor_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecompartocor.find_by_id",
                id=self.get_id_fixed("ope_compart_ocor_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_compart_ocor_delete(self):
        response = self.client.delete(
            url_for(
                "opecompartocor.delete", id=self.get_id_fixed("ope_compart_ocor_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  ope_compart_subgrupo
    # ===========================================================

    # ====================

    def ope_compart_subgrupo_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_compart_subgrupo_id1"),
            "ope_compart_grupo_id": module_tests_ope.ope_compart_grupo_id1(self),
            "sigla_compart_subgrupo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "nome": "TESTE [CRUD]",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("opecompartsubgrupo.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_compart_subgrupo_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_compart_subgrupo_id2"),
            "ope_compart_grupo_id": module_tests_ope.ope_compart_grupo_id1(self),
            "sigla_compart_subgrupo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "nome": "TESTE [CRUD]",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("opecompartsubgrupo.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_compart_subgrupo_get(self):
        response = self.client.get(
            url_for("opecompartsubgrupo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_compart_subgrupo_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecompartsubgrupo.find_by_id",
                id=self.get_id_fixed("ope_compart_subgrupo_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_compart_subgrupo_delete(self):
        response = self.client.delete(
            url_for(
                "opecompartsubgrupo.delete",
                id=self.get_id_fixed("ope_compart_subgrupo_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  ope_compart_tipo
    # ===========================================================

    # ====================

    def ope_compart_tipo_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_compart_tipo_id1"),
            "qnt_lonas": "5",
            "ope_compart_medida_id": module_tests_ope.ope_compart_medida_id1(self),
            "sigla_compart_tipo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "qnt_sulco_max": "5",
            "tipo_compart": "P",
            "nome": "TESTE [CRUD]",
            "qnt_sulco_min": "5",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("opecomparttipo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_compart_tipo_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_compart_tipo_id2"),
            "qnt_lonas": "5",
            "ope_compart_medida_id": module_tests_ope.ope_compart_medida_id1(self),
            "sigla_compart_tipo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "qnt_sulco_max": "5",
            "tipo_compart": "P",
            "nome": "TESTE [CRUD]",
            "qnt_sulco_min": "5",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("opecomparttipo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_compart_tipo_get(self):
        response = self.client.get(
            url_for("opecomparttipo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_compart_tipo_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecomparttipo.find_by_id",
                id=self.get_id_fixed("ope_compart_tipo_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_compart_tipo_delete(self):
        response = self.client.delete(
            url_for(
                "opecomparttipo.delete", id=self.get_id_fixed("ope_compart_tipo_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  ope_ocor
    # ===========================================================

    # ====================

    def ope_ocor_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_ocor_id1"),
            "tipo_lanc": "1",
            "nome": "TESTE [CRUD]",
            "sigla_ocor": "TESTE [CRUD]",
            "ger_umedida_id": module_tests_ger.module_tests_ger.ger_umedida_id1(self),
            "icon": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ope_ocor_grupo_id": module_tests_ope.ope_ocor_grupo_id1(self),
            "tipo": "A",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("opeocor.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_ocor_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_ocor_id2"),
            "tipo_lanc": "1",
            "nome": "TESTE [CRUD]",
            "sigla_ocor": "TESTE [CRUD]",
            "ger_umedida_id": module_tests_ger.module_tests_ger.ger_umedida_id1(self),
            "icon": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ope_ocor_grupo_id": module_tests_ope.ope_ocor_grupo_id1(self),
            "tipo": "A",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("opeocor.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_ocor_get(self):
        response = self.client.get(
            url_for("opeocor.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_ocor_get_by_id(self):
        response = self.client.get(
            url_for("opeocor.find_by_id", id=self.get_id_fixed("ope_ocor_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_ocor_delete(self):
        response = self.client.delete(
            url_for("opeocor.delete", id=self.get_id_fixed("ope_ocor_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  ope_centro1
    # ===========================================================

    # ====================

    def ope_centro1_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro1_id1"),
            "observacao": "TESTE [CRUD]",
            "ger_pessoa_id": module_tests_ger.module_tests_ger.ger_pessoa_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ctb_comp_id": module_tests_ctb.module_tests_ctb.ctb_comp_id1(self),
            "ope_centro_subtipo_id": module_tests_ope.ope_centro_subtipo_id1(self),
            "data_valid": "18/07/2022",
            "sigla_centro1": "TESTE [CRUD]",
            "nome": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("opecentro1.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro1_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro1_id2"),
            "observacao": "TESTE [CRUD]",
            "ger_pessoa_id": module_tests_ger.module_tests_ger.ger_pessoa_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ctb_comp_id": module_tests_ctb.module_tests_ctb.ctb_comp_id1(self),
            "ope_centro_subtipo_id": module_tests_ope.ope_centro_subtipo_id1(self),
            "data_valid": "18/07/2022",
            "sigla_centro1": "TESTE [CRUD]",
            "nome": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("opecentro1.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro1_get(self):
        response = self.client.get(
            url_for("opecentro1.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_centro1_get_by_id(self):
        response = self.client.get(
            url_for("opecentro1.find_by_id", id=self.get_id_fixed("ope_centro1_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_centro1_delete(self):
        response = self.client.delete(
            url_for("opecentro1.delete", id=self.get_id_fixed("ope_centro1_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  ope_centro_rend
    # ===========================================================

    # ====================

    def ope_centro_rend_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro_rend_id1"),
            "ope_atividade_id": module_tests_ope.ope_atividade_id1(self),
            "ope_centro_versao_id": module_tests_ope.ope_centro_versao_id1(self),
            "nome": "TESTE [CRUD]",
            "observacao": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ope_centro_rend_fator_childs": [
                {
                    "id": self.get_id_fixed("ope_centro_rend_fator_id1"),
                    "ger_itemserv_id": module_tests_ger.module_tests_ger.ger_itemserv_id1(
                        self
                    ),
                    "ctb_comp_id": module_tests_ctb.module_tests_ctb.ctb_comp_id1(self),
                    "fator_rend": "5",
                    "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
                    "fator_util": "5",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                }
            ],
        }

        response = self.client.post(
            url_for("opecentrorend.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro_rend_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro_rend_id2"),
            "ope_atividade_id": module_tests_ope.ope_atividade_id1(self),
            "ope_centro_versao_id": module_tests_ope.ope_centro_versao_id1(self),
            "nome": "TESTE [CRUD]",
            "observacao": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ope_centro_rend_fator_childs": [
                {
                    "ger_itemserv_id": module_tests_ger.module_tests_ger.ger_itemserv_id1(
                        self
                    ),
                    "ctb_comp_id": module_tests_ctb.module_tests_ctb.ctb_comp_id1(self),
                    "fator_rend": "5",
                    "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
                    "fator_util": "5",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                }
            ],
        }

        response = self.client.post(
            url_for("opecentrorend.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro_rend_get(self):
        response = self.client.get(
            url_for("opecentrorend.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_centro_rend_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecentrorend.find_by_id", id=self.get_id_fixed("ope_centro_rend_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_centro_rend_delete(self):
        response = self.client.delete(
            url_for(
                "opecentrorend.delete", id=self.get_id_fixed("ope_centro_rend_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  ope_centro_subgrupo
    # ===========================================================

    # ====================

    def ope_centro_subgrupo_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro_subgrupo_id1"),
            "ctb_comp_id": module_tests_ctb.module_tests_ctb.ctb_comp_id1(self),
            "ope_centro_grupo_id": module_tests_ope.ope_centro_grupo_id1(self),
            "nome": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "sigla_centro_subgrupo": "TESTE [CRUD]",
            "icon": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("opecentrosubgrupo.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro_subgrupo_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro_subgrupo_id2"),
            "ctb_comp_id": module_tests_ctb.module_tests_ctb.ctb_comp_id1(self),
            "ope_centro_grupo_id": module_tests_ope.ope_centro_grupo_id1(self),
            "nome": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "sigla_centro_subgrupo": "TESTE [CRUD]",
            "icon": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("opecentrosubgrupo.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro_subgrupo_get(self):
        response = self.client.get(
            url_for("opecentrosubgrupo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_centro_subgrupo_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecentrosubgrupo.find_by_id",
                id=self.get_id_fixed("ope_centro_subgrupo_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_centro_subgrupo_delete(self):
        response = self.client.delete(
            url_for(
                "opecentrosubgrupo.delete",
                id=self.get_id_fixed("ope_centro_subgrupo_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  ope_compart
    # ===========================================================

    # ====================

    def ope_compart_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_compart_id1"),
            "ope_compart_subgrupo_id": module_tests_ope.ope_compart_subgrupo_id1(self),
            "observacao": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "capacidade": "10",
            "data_status": "15/07/2022",
            "ope_compart_status_id": module_tests_ope.ope_compart_status_id1(self),
            "numero_serie": "5",
            "valor_aquisicao": "5",
            "nome": "TESTE [CRUD]",
            "medicao_trab_centro": "P",
            "valida_itemserv": "S",
            "sigla_compart": "TESTE [CRUD]",
            "data_baixa": "15/07/2022",
            "data_aquisicao": "15/07/2022",
        }

        response = self.client.post(
            url_for("opecompart.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_compart_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_compart_id2"),
            "ope_compart_subgrupo_id": module_tests_ope.ope_compart_subgrupo_id1(self),
            "observacao": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "capacidade": "10",
            "data_status": "15/07/2022",
            "ope_compart_status_id": module_tests_ope.ope_compart_status_id1(self),
            "numero_serie": "5",
            "valor_aquisicao": "5",
            "nome": "TESTE [CRUD]",
            "medicao_trab_centro": "P",
            "valida_itemserv": "S",
            "sigla_compart": "TESTE [CRUD]",
            "data_baixa": "15/07/2022",
            "data_aquisicao": "15/07/2022",
        }

        response = self.client.post(
            url_for("opecompart.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_compart_get(self):
        response = self.client.get(
            url_for("opecompart.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_compart_get_by_id(self):
        response = self.client.get(
            url_for("opecompart.find_by_id", id=self.get_id_fixed("ope_compart_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_compart_delete(self):
        response = self.client.delete(
            url_for("opecompart.delete", id=self.get_id_fixed("ope_compart_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  ope_compart_itemserv
    # ===========================================================

    # ====================

    def ope_compart_itemserv_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_compart_itemserv_id1"),
            "ger_itemserv_id": module_tests_ger.module_tests_ger.ger_itemserv_id1(self),
            "ope_compart_id": module_tests_ope.ope_compart_id1(self),
            "observacao": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opecompartitemserv.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_compart_itemserv_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_compart_itemserv_id2"),
            "ger_itemserv_id": module_tests_ger.module_tests_ger.ger_itemserv_id1(self),
            "ope_compart_id": module_tests_ope.ope_compart_id1(self),
            "observacao": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opecompartitemserv.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_compart_itemserv_get(self):
        response = self.client.get(
            url_for("opecompartitemserv.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_compart_itemserv_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecompartitemserv.find_by_id",
                id=self.get_id_fixed("ope_compart_itemserv_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_compart_itemserv_delete(self):
        response = self.client.delete(
            url_for(
                "opecompartitemserv.delete",
                id=self.get_id_fixed("ope_compart_itemserv_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  ope_ocor_mov
    # ===========================================================

    # ====================

    def ope_ocor_mov_id1(self):
        module_tests_ger.module_tests_ger.ger_pessoa_id1(self)

        req_post = {
            "id": self.get_id_fixed("ope_ocor_mov_id1"),
            "data_mov": "15/07/2022",
            "ope_ocor_tipo_id": module_tests_ope.ope_ocor_tipo_id1(self),
            "ger_pessoa_endereco_id_exec": self.get_id_fixed("ger_pessoa_endereco_id1"),
            "numero": "5",
            "observacao": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ope_ocor_mov_dest_childs": [
                {
                    "id": self.get_id_fixed("ope_ocor_mov_dest_id1"),
                    "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
                    "observacao": "TESTE [CRUD]1",
                    "ope_compart_id": module_tests_ope.ope_compart_id1(self),
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                }
            ],
            "ope_ocor_mov_det_childs": [
                {
                    "long_y": "5",
                    "ponto": "5",
                    "data_status": "29/07/2003",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "observacao": "5",
                    "qnt_ocor_calc": "5",
                    "ope_ocor_id": module_tests_ope.ope_ocor_id1(self),
                    "ope_ocor_status_id": module_tests_ope.ope_ocor_status_id1(self),
                    "lat_x": "5",
                    "qnt_ocor": "5",
                }
            ],
        }

        response = self.client.post(
            url_for("opeocormov.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_ocor_mov_id2(self):
        module_tests_ger.module_tests_ger.ger_pessoa_id1(self)
        req_post = {
            "id": self.get_id_fixed("ope_ocor_mov_id2"),
            "data_mov": "15/07/2022",
            "ope_ocor_tipo_id": module_tests_ope.ope_ocor_tipo_id1(self),
            "ger_pessoa_endereco_id_exec": self.get_id_fixed("ger_pessoa_endereco_id1"),
            "numero": "5",
            "observacao": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ope_ocor_mov_dest_childs": [
                {
                    "id": self.get_id_fixed("ope_ocor_mov_dest_id1"),
                    "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
                    "observacao": "TESTE [CRUD]1",
                    "ope_compart_id": module_tests_ope.ope_compart_id1(self),
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                }
            ],
            "ope_ocor_mov_det_childs": [
                {
                    "long_y": "5",
                    "ponto": "5",
                    "data_status": "29/07/2003",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "observacao": "5",
                    "qnt_ocor_calc": "5",
                    "ope_ocor_id": module_tests_ope.ope_ocor_id1(self),
                    "ope_ocor_status_id": module_tests_ope.ope_ocor_status_id1(self),
                    "lat_x": "5",
                    "qnt_ocor": "5",
                }
            ],
        }

        response = self.client.post(
            url_for("opeocormov.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_ocor_mov_get(self):
        response = self.client.get(
            url_for("opeocormov.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_ocor_mov_get_by_id(self):
        response = self.client.get(
            url_for("opeocormov.find_by_id", id=self.get_id_fixed("ope_ocor_mov_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_ocor_mov_delete(self):
        response = self.client.delete(
            url_for("opeocormov.delete", id=self.get_id_fixed("ope_ocor_mov_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  ope_centro2_area
    # ===========================================================

    # ====================

    def ope_centro2_area_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro2_area_id1"),
            "qnt_area_improd": "5",
            "long_y": "5",
            "ger_itemserv_id_ult": module_tests_ger.module_tests_ger.ger_itemserv_id1(
                self
            ),
            "data_ult_col": "15/07/2022",
            "ope_atividade_sistema_id_col": module_tests_ope.ope_atividade_sistema_id1(
                self
            ),
            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
            "data_florada_1": "15/07/2022",
            "ope_atividade_sistema_id_cult": module_tests_ope.ope_atividade_sistema_id1(
                self
            ),
            "ger_itemserv_id": module_tests_ger.module_tests_ger.ger_itemserv_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_ini_col": "15/07/2001",
            "ope_tipo_solo_id": module_tests_ope.ope_tipo_solo_id1(self),
            "lat_x": "15",
            "alt_z": "51",
            "data_emerg": "15/07/2001",
            "ger_itemserv_var_id_ult": module_tests_ger.module_tests_ger.ger_itemserv_var_id1(
                self
            ),
            "ope_atividade_sistema_id_plan": module_tests_ope.ope_atividade_sistema_id1(
                self
            ),
            "ope_periodo_id": module_tests_ope.ope_periodo_id1(self),
            "ger_itemserv_var_id": module_tests_ger.module_tests_ger.ger_itemserv_var_id1(
                self
            ),
            "bloco_col": "5",
            "data_fin_col": "15/05/2021",
            "data_fin_plan": "15/05/2021",
            "qnt_area_prod": "5",
            "qnt_plantas_estande": "10",
            "observacao": "TESTE [CRUD]",
            "data_ult_plan": "15/05/2021",
            "ger_umedida_id": module_tests_ger.module_tests_ger.ger_umedida_id1(self),
            "ope_espac_id": module_tests_ope.ope_espac_id1(self),
            "data_ini_plan": "15/05/2021",
            "ope_estagio_id": module_tests_ope.ope_estagio_id1(self),
            "ope_centro2_mapa_coord_childs": [
                {
                    "id": self.get_id_fixed("ope_centro2_mapa_coord_id1"),
                    "long_y": "12",
                    "lat_x": "12",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "ordem": "12",
                }
            ],
        }

        response = self.client.post(
            url_for("opecentro2area.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro2_area_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro2_area_id2"),
            "qnt_area_improd": "5",
            "long_y": "5",
            "ger_itemserv_id_ult": module_tests_ger.module_tests_ger.ger_itemserv_id1(
                self
            ),
            "data_ult_col": "15/07/2022",
            "ope_atividade_sistema_id_col": module_tests_ope.ope_atividade_sistema_id1(
                self
            ),
            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
            "data_florada_1": "15/07/2022",
            "ope_atividade_sistema_id_cult": module_tests_ope.ope_atividade_sistema_id1(
                self
            ),
            "ger_itemserv_id": module_tests_ger.module_tests_ger.ger_itemserv_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_ini_col": "15/07/2001",
            "ope_tipo_solo_id": module_tests_ope.ope_tipo_solo_id1(self),
            "lat_x": "15",
            "alt_z": "51",
            "data_emerg": "15/07/2001",
            "ger_itemserv_var_id_ult": module_tests_ger.module_tests_ger.ger_itemserv_var_id1(
                self
            ),
            "ope_atividade_sistema_id_plan": module_tests_ope.ope_atividade_sistema_id1(
                self
            ),
            "ope_periodo_id": module_tests_ope.ope_periodo_id1(self),
            "ger_itemserv_var_id": module_tests_ger.module_tests_ger.ger_itemserv_var_id1(
                self
            ),
            "bloco_col": "5",
            "data_fin_col": "15/05/2021",
            "data_fin_plan": "15/05/2021",
            "qnt_area_prod": "5",
            "qnt_plantas_estande": "10",
            "observacao": "TESTE [CRUD]",
            "data_ult_plan": "15/05/2021",
            "ger_umedida_id": module_tests_ger.module_tests_ger.ger_umedida_id1(self),
            "ope_espac_id": module_tests_ope.ope_espac_id1(self),
            "data_ini_plan": "15/05/2021",
            "ope_estagio_id": module_tests_ope.ope_estagio_id1(self),
            "ope_centro2_mapa_coord_childs": [
                {
                    "long_y": "12",
                    "lat_x": "12",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "ordem": "12",
                }
            ],
        }

        response = self.client.post(
            url_for("opecentro2area.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro2_area_get(self):
        response = self.client.get(
            url_for("opecentro2area.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_centro2_area_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecentro2area.find_by_id",
                id=self.get_id_fixed("ope_centro2_area_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_centro2_area_delete(self):
        response = self.client.delete(
            url_for(
                "opecentro2area.delete", id=self.get_id_fixed("ope_centro2_area_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  ope_centro2_equip
    # ===========================================================

    # ====================

    def ope_centro2_equip_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro2_equip_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "placa": "4546",
            "capacidade_m3": "5",
            "largura": "4545",
            "nr_registro_estadual": "45",
            "tipo_carroceria": "02",
            "potencia": "5",
            "liberado_abastec": "S",
            "data_venc_licenciamento": "15/07/2001",
            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
            "capacidade_kg": "5",
            "data_venc_imposto": "15/07/2022",
            "tipo_rodado": "00",
            "tipo_tracao": "0",
            "ger_cidade_id": module_tests_ger.module_tests_ger.ger_cidade_id1(self),
            "renavam": "TESTE [CRUD]",
            "tipo_transp_auto_carga": "1",
            "ope_frente_trabalho_id": module_tests_ope.ope_frente_trabalho_id1(self),
            "altura": "5",
            "tara": "5",
            "nr_chassi": "5",
            "nr_serie": "5",
        }

        response = self.client.post(
            url_for("opecentro2equip.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro2_equip_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro2_equip_id2"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "placa": "4546",
            "capacidade_m3": "5",
            "largura": "4545",
            "nr_registro_estadual": "45",
            "tipo_carroceria": "02",
            "potencia": "5",
            "liberado_abastec": "S",
            "data_venc_licenciamento": "15/07/2001",
            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
            "capacidade_kg": "5",
            "data_venc_imposto": "15/07/2022",
            "tipo_rodado": "01",
            "tipo_tracao": "0",
            "ger_cidade_id": module_tests_ger.module_tests_ger.ger_cidade_id1(self),
            "renavam": "TESTE [CRUD]",
            "tipo_transp_auto_carga": "1",
            "ope_frente_trabalho_id": module_tests_ope.ope_frente_trabalho_id1(self),
            "altura": "5",
            "tara": "5",
            "nr_chassi": "5",
            "nr_serie": "5",
        }

        response = self.client.post(
            url_for("opecentro2equip.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro2_equip_get(self):
        response = self.client.get(
            url_for("opecentro2equip.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_centro2_equip_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecentro2equip.find_by_id",
                id=self.get_id_fixed("ope_centro2_equip_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_centro2_equip_delete(self):
        response = self.client.delete(
            url_for(
                "opecentro2equip.delete", id=self.get_id_fixed("ope_centro2_equip_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  ope_centro2_estoque
    # ===========================================================

    # ====================

    def ope_centro2_estoque_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro2_estoque_id1"),
            "tipo": "E",
            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opecentro2estoque.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro2_estoque_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro2_estoque_id2"),
            "tipo": "E",
            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opecentro2estoque.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro2_estoque_get(self):
        response = self.client.get(
            url_for("opecentro2estoque.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_centro2_estoque_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecentro2estoque.find_by_id",
                id=self.get_id_fixed("ope_centro2_estoque_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_centro2_estoque_delete(self):
        response = self.client.delete(
            url_for(
                "opecentro2estoque.delete",
                id=self.get_id_fixed("ope_centro2_estoque_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  ope_centro2_mov_media
    # ===========================================================

    # ====================

    def ope_centro2_mov_media_id1(self):
        module_tests_ger.module_tests_ger.ger_marca_id1(self)
        req_post = {
            "id": self.get_id_fixed("ope_centro2_mov_media_id1"),
            "dt_valid_ini": "15/07/2022",
            "capacidade": "5",
            "ger_itemserv_id": module_tests_ger.module_tests_ger.ger_itemserv_id1(self),
            "qnt_media_min": "5",
            "qnt_media_max": "10",
            "ger_marca_modelo_id": self.get_id_fixed("ger_marca_modelo_id1"),
            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
            "ope_compart_id": module_tests_ope.ope_compart_id1(self),
            "observacao": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opecentro2movmedia.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro2_mov_media_id2(self):
        module_tests_ger.module_tests_ger.ger_marca_id1(self)
        req_post = {
            "id": self.get_id_fixed("ope_centro2_mov_media_id2"),
            "dt_valid_ini": "15/07/2022",
            "capacidade": "5",
            "ger_itemserv_id": module_tests_ger.module_tests_ger.ger_itemserv_id1(self),
            "qnt_media_min": "5",
            "qnt_media_max": "10",
            "ger_marca_modelo_id": self.get_id_fixed("ger_marca_modelo_id1"),
            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
            "ope_compart_id": module_tests_ope.ope_compart_id1(self),
            "observacao": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opecentro2movmedia.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro2_mov_media_get(self):
        response = self.client.get(
            url_for("opecentro2movmedia.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_centro2_mov_media_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecentro2movmedia.find_by_id",
                id=self.get_id_fixed("ope_centro2_mov_media_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_centro2_mov_media_delete(self):
        response = self.client.delete(
            url_for(
                "opecentro2movmedia.delete",
                id=self.get_id_fixed("ope_centro2_mov_media_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  ope_centro2_param_per
    # ===========================================================

    # ====================

    def ope_centro2_param_per_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro2_param_per_id1"),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ope_frente_trabalho_id": module_tests_ope.ope_frente_trabalho_id1(self),
            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "dt_valid_ini": "15/07/2022",
        }

        response = self.client.post(
            url_for("opecentro2paramper.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro2_param_per_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro2_param_per_id2"),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ope_frente_trabalho_id": module_tests_ope.ope_frente_trabalho_id1(self),
            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "dt_valid_ini": "15/07/2022",
        }

        response = self.client.post(
            url_for("opecentro2paramper.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro2_param_per_get(self):
        response = self.client.get(
            url_for("opecentro2paramper.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_centro2_param_per_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecentro2paramper.find_by_id",
                id=self.get_id_fixed("ope_centro2_param_per_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_centro2_param_per_delete(self):
        response = self.client.delete(
            url_for(
                "opecentro2paramper.delete",
                id=self.get_id_fixed("ope_centro2_param_per_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  ope_centro2_pessoa
    # ===========================================================

    # ====================

    def ope_centro2_pessoa_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro2_pessoa_id1"),
            "pto_idenf": "S",
            "ope_frente_trabalho_id": module_tests_ope.ope_frente_trabalho_id1(self),
            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "pto_idenf_tipo": "1",
        }

        response = self.client.post(
            url_for("opecentro2pessoa.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro2_pessoa_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro2_pessoa_id2"),
            "pto_idenf": "S",
            "ope_frente_trabalho_id": module_tests_ope.ope_frente_trabalho_id1(self),
            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "pto_idenf_tipo": "1",
        }

        response = self.client.post(
            url_for("opecentro2pessoa.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro2_pessoa_get(self):
        response = self.client.get(
            url_for("opecentro2pessoa.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_centro2_pessoa_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecentro2pessoa.find_by_id",
                id=self.get_id_fixed("ope_centro2_pessoa_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_centro2_pessoa_delete(self):
        response = self.client.delete(
            url_for(
                "opecentro2pessoa.delete",
                id=self.get_id_fixed("ope_centro2_pessoa_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  ope_centro_config
    # ===========================================================

    # ====================

    def ope_centro_config_id1(self):
        module_tests_ger.module_tests_ger.ger_itemserv_grupo_id1(self)
        req_post = {
            "id": self.get_id_fixed("ope_centro_config_id1"),
            "ope_centro_subtipo_id": module_tests_ope.ope_centro_subtipo_id1(self),
            "ope_compart_subgrupo_id": module_tests_ope.ope_compart_subgrupo_id1(self),
            "ope_estagio_id": module_tests_ope.ope_estagio_id1(self),
            "ope_compart_grupo_id": module_tests_ope.ope_compart_grupo_id1(self),
            "ger_itemserv_subgrupo_id": self.get_id_fixed("ger_itemserv_subgrupo_id1"),
            "ope_centro_tipo_id": module_tests_ope.ope_centro_tipo_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ope_atividade_id": module_tests_ope.ope_atividade_id1(self),
            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
            "ger_itemserv_id": module_tests_ger.module_tests_ger.ger_itemserv_id1(self),
            "ope_centro1_id": module_tests_ope.ope_centro1_id1(self),
            "ger_itemserv_grupo_id": module_tests_ger.module_tests_ger.ger_itemserv_grupo_id1(
                self
            ),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ope_compart_id": module_tests_ope.ope_compart_id1(self),
            "ope_centro2_ord_tipo_id": module_tests_ope.ope_centro2_ord_tipo_id1(self),
            "ope_centro_grupo_id": module_tests_ope.ope_centro_grupo_id1(self),
            "mov_operacao_id": module_tests_mov.module_tests_mov.mov_operacao_id1(self),
            "ope_centro_subgrupo_id": module_tests_ope.ope_centro_subgrupo_id1(self),
            "ativo": "S",
            "observacao": "TESTE [CRUD]",
            "tipo_regra": "E",
        }

        response = self.client.post(
            url_for("opecentroconfig.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro_config_id2(self):
        module_tests_ger.module_tests_ger.ger_itemserv_grupo_id1(self)
        req_post = {
            "id": self.get_id_fixed("ope_centro_config_id2"),
            "ope_centro_subtipo_id": module_tests_ope.ope_centro_subtipo_id1(self),
            "ope_compart_subgrupo_id": module_tests_ope.ope_compart_subgrupo_id1(self),
            "ope_estagio_id": module_tests_ope.ope_estagio_id1(self),
            "ope_compart_grupo_id": module_tests_ope.ope_compart_grupo_id1(self),
            "ger_itemserv_subgrupo_id": self.get_id_fixed("ger_itemserv_subgrupo_id1"),
            "ope_centro_tipo_id": module_tests_ope.ope_centro_tipo_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ope_atividade_id": module_tests_ope.ope_atividade_id1(self),
            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
            "ger_itemserv_id": module_tests_ger.module_tests_ger.ger_itemserv_id1(self),
            "ope_centro1_id": module_tests_ope.ope_centro1_id1(self),
            "ger_itemserv_grupo_id": module_tests_ger.module_tests_ger.ger_itemserv_grupo_id1(
                self
            ),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ope_compart_id": module_tests_ope.ope_compart_id1(self),
            "ope_centro2_ord_tipo_id": module_tests_ope.ope_centro2_ord_tipo_id1(self),
            "ope_centro_grupo_id": module_tests_ope.ope_centro_grupo_id1(self),
            "mov_operacao_id": module_tests_mov.module_tests_mov.mov_operacao_id1(self),
            "ope_centro_subgrupo_id": module_tests_ope.ope_centro_subgrupo_id1(self),
            "ativo": "S",
            "observacao": "TESTE [CRUD]",
            "tipo_regra": "E",
        }

        response = self.client.post(
            url_for("opecentroconfig.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro_config_get(self):
        response = self.client.get(
            url_for("opecentroconfig.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_centro_config_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecentroconfig.find_by_id",
                id=self.get_id_fixed("ope_centro_config_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_centro_config_delete(self):
        response = self.client.delete(
            url_for(
                "opecentroconfig.delete", id=self.get_id_fixed("ope_centro_config_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  ope_centro_prev
    # ===========================================================

    # ====================

    def ope_centro_prev_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro_prev_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "qnt24": "01",
            "data_per": "15/07/2022",
            "qnt14": "01",
            "qnt06": "01",
            "qnt07": "01",
            "qnt31": "01",
            "qnt29": "01",
            "ope_periodo_id": module_tests_ope.ope_periodo_id1(self),
            "qnt05": "01",
            "qnt09": "01",
            "qnt10": "01",
            "qnt18": "01",
            "ope_centro_versao_id": module_tests_ope.ope_centro_versao_id1(self),
            "qnt20": "01",
            "qnt16": "01",
            "ope_centro2_ord_tipo_id": module_tests_ope.ope_centro2_ord_tipo_id1(self),
            "qnt03": "01",
            "qnt02": "01",
            "tipo_executor": "P",
            "qnt21": "01",
            "qnt15": "01",
            "qnt23": "01",
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "qnt11": "01",
            "qnt17": "01",
            "qnt04": "01",
            "qnt26": "01",
            "ope_atividade_id": module_tests_ope.ope_atividade_id1(self),
            "qnt25": "01",
            "process_id": module_tests_sys.module_tests_sys.sys_process_log_id1(self),
            "qnt30": "01",
            "qnt28": "01",
            "qnt19": "01",
            "qnt22": "01",
            "qnt12": "01",
            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
            "qnt13": "01",
            "qnt27": "01",
            "qnt01": "01",
            "ordem_exec": "TST",
            "qnt08": "01",
        }

        response = self.client.post(
            url_for("opecentroprev.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro_prev_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro_prev_id2"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "qnt24": "01",
            "data_per": "15/07/2022",
            "qnt14": "01",
            "qnt06": "01",
            "qnt07": "01",
            "qnt31": "01",
            "qnt29": "01",
            "ope_periodo_id": module_tests_ope.ope_periodo_id1(self),
            "qnt05": "01",
            "qnt09": "01",
            "qnt10": "01",
            "qnt18": "01",
            "ope_centro_versao_id": module_tests_ope.ope_centro_versao_id1(self),
            "qnt20": "01",
            "qnt16": "01",
            "ope_centro2_ord_tipo_id": module_tests_ope.ope_centro2_ord_tipo_id1(self),
            "qnt03": "01",
            "qnt02": "01",
            "tipo_executor": "P",
            "qnt21": "01",
            "qnt15": "01",
            "qnt23": "01",
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "qnt11": "01",
            "qnt17": "01",
            "qnt04": "01",
            "qnt26": "01",
            "ope_atividade_id": module_tests_ope.ope_atividade_id1(self),
            "qnt25": "01",
            "process_id": module_tests_sys.module_tests_sys.sys_process_log_id1(self),
            "qnt30": "01",
            "qnt28": "01",
            "qnt19": "01",
            "qnt22": "01",
            "qnt12": "01",
            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
            "qnt13": "01",
            "qnt27": "01",
            "qnt01": "01",
            "ordem_exec": "TST",
            "qnt08": "01",
        }

        response = self.client.post(
            url_for("opecentroprev.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro_prev_get(self):
        response = self.client.get(
            url_for("opecentroprev.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_centro_prev_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecentroprev.find_by_id", id=self.get_id_fixed("ope_centro_prev_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_centro_prev_delete(self):
        response = self.client.delete(
            url_for(
                "opecentroprev.delete", id=self.get_id_fixed("ope_centro_prev_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  ope_ocor_prev
    # ===========================================================

    # ====================

    def ope_ocor_prev_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_ocor_prev_id1"),
            "qnt_limite": "5",
            "observacao": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "qnt_dia_limite": "5",
            "ope_ocor_id": module_tests_ope.ope_ocor_id1(self),
            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
            "data_ult_solucao": "15/07/2022",
            "qnt_dia_aviso": "5",
            "data_valid_ini": "15/07/2022",
            "ope_compart_id": module_tests_ope.ope_compart_id1(self),
            "qnt_aviso": "5",
        }

        response = self.client.post(
            url_for("opeocorprev.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_ocor_prev_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_ocor_prev_id2"),
            "qnt_limite": "5",
            "observacao": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "qnt_dia_limite": "5",
            "ope_ocor_id": module_tests_ope.ope_ocor_id1(self),
            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
            "data_ult_solucao": "15/07/2022",
            "qnt_dia_aviso": "5",
            "data_valid_ini": "15/07/2022",
            "ope_compart_id": module_tests_ope.ope_compart_id1(self),
            "qnt_aviso": "5",
        }

        response = self.client.post(
            url_for("opeocorprev.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_ocor_prev_get(self):
        response = self.client.get(
            url_for("opeocorprev.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_ocor_prev_get_by_id(self):
        response = self.client.get(
            url_for(
                "opeocorprev.find_by_id", id=self.get_id_fixed("ope_ocor_prev_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_ocor_prev_delete(self):
        response = self.client.delete(
            url_for("opeocorprev.delete", id=self.get_id_fixed("ope_ocor_prev_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  ope_centro2_ord
    # ===========================================================

    # ====================

    def ope_centro2_ord_id1(self):
        module_tests_ger.module_tests_ger.ger_pessoa_id1(self)
        req_post = {
            "id": self.get_id_fixed("ope_centro2_ord_id1"),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ope_periodo_id": module_tests_ope.ope_periodo_id1(self),
            "data_ini_exec_prev": "15/07/2022",
            "ope_centro2_ord_tipo_id": module_tests_ope.ope_centro2_ord_tipo_id1(self),
            "ope_frente_trabalho_id": module_tests_ope.ope_frente_trabalho_id1(self),
            "data_ini_exec": "15/07/2022",
            "data_valid": "15/07/2022",
            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
            "observacao_externa": "TESTE [CRUD]",
            "data_fin_exec_prev": "15/07/2022",
            "observacao_interna": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_status": "15/07/2022",
            "numero_ord": "5",
            "ope_centro2_ord_status_id": module_tests_ope.ope_centro2_ord_status_id1(
                self
            ),
            "data_fin_exec": "15/07/2022",
            "ope_centro_versao_id": module_tests_ope.ope_centro_versao_id1(self),
            "ger_pessoa_endereco_id_exec": self.get_id_fixed("ger_pessoa_endereco_id1"),
            "process_id": module_tests_sys.module_tests_sys.sys_process_log_id1(self),
            "ope_centro2_pessoa_id_solic": module_tests_ope.ope_centro2_pessoa_id1(
                self
            ),
            "ope_centro2_ord_ativ_childs": [
                {
                    "id": self.get_id_fixed("ope_centro2_ord_ativ_id1"),
                    "ordem_exec": "2",
                    "tipo_executor": "T",
                    "ope_frente_trabalho_id": module_tests_ope.ope_frente_trabalho_id1(
                        self
                    ),
                    "observacao_externa": "TESTE [CRUD]1",
                    "ope_atividade_id": module_tests_ope.ope_atividade_id1(self),
                    "observacao_interna": "TESTE [CRUD]1",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "data_valid": "29/12/2003",
                }
            ],
            "ope_centro2_ord_dest_childs": [
                {
                    "id": self.get_id_fixed("ope_centro2_ord_dest_id1"),
                    "qnt_obj": "5",
                    "ope_centro2_id_dest": module_tests_ope.ope_centro2_id1(self),
                    "valor_unit_prev": "5",
                    "observacao_interna": "TESTE [CRUD]1",
                    "observacao_externa": "TESTE [CRUD]1",
                    "ger_umedida_id_dest": module_tests_ger.module_tests_ger.ger_umedida_id1(
                        self
                    ),
                    "valor_unit": "5",
                    "valor_total": "5",
                    "qnt_prev_obj": "5",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "valor_total_prev": "5",
                    "data_valid": "29/12/2003",
                }
            ],
        }

        response = self.client.post(
            url_for("opecentro2ord.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro2_ord_id2(self):
        module_tests_ger.module_tests_ger.ger_pessoa_id1(self)
        req_post = {
            "id": self.get_id_fixed("ope_centro2_ord_id2"),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ope_periodo_id": module_tests_ope.ope_periodo_id1(self),
            "data_ini_exec_prev": "15/07/2022",
            "ope_centro2_ord_tipo_id": module_tests_ope.ope_centro2_ord_tipo_id1(self),
            "ope_frente_trabalho_id": module_tests_ope.ope_frente_trabalho_id1(self),
            "data_ini_exec": "15/07/2022",
            "data_valid": "15/07/2022",
            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
            "observacao_externa": "TESTE [CRUD]",
            "data_fin_exec_prev": "15/07/2022",
            "observacao_interna": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_status": "15/07/2022",
            "numero_ord": "5",
            "ope_centro2_ord_status_id": module_tests_ope.ope_centro2_ord_status_id1(
                self
            ),
            "data_fin_exec": "15/07/2022",
            "ope_centro_versao_id": module_tests_ope.ope_centro_versao_id1(self),
            "ger_pessoa_endereco_id_exec": self.get_id_fixed("ger_pessoa_endereco_id1"),
            "process_id": module_tests_sys.module_tests_sys.sys_process_log_id1(self),
            "ope_centro2_pessoa_id_solic": module_tests_ope.ope_centro2_pessoa_id1(
                self
            ),
            "ope_centro2_ord_ativ_childs": [
                {
                    "ordem_exec": "2",
                    "tipo_executor": "T",
                    "ope_frente_trabalho_id": module_tests_ope.ope_frente_trabalho_id1(
                        self
                    ),
                    "observacao_externa": "TESTE [CRUD]1",
                    "ope_atividade_id": module_tests_ope.ope_atividade_id1(self),
                    "observacao_interna": "TESTE [CRUD]1",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "data_valid": "29/12/2003",
                }
            ],
            "ope_centro2_ord_dest_childs": [
                {
                    "qnt_obj": "5",
                    "ope_centro2_id_dest": module_tests_ope.ope_centro2_id1(self),
                    "valor_unit_prev": "5",
                    "observacao_interna": "TESTE [CRUD]1",
                    "observacao_externa": "TESTE [CRUD]1",
                    "ger_umedida_id_dest": module_tests_ger.module_tests_ger.ger_umedida_id1(
                        self
                    ),
                    "valor_unit": "5",
                    "valor_total": "5",
                    "qnt_prev_obj": "5",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "valor_total_prev": "5",
                    "data_valid": "29/12/2003",
                }
            ],
        }

        response = self.client.post(
            url_for("opecentro2ord.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro2_ord_get(self):
        response = self.client.get(
            url_for("opecentro2ord.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_centro2_ord_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecentro2ord.find_by_id", id=self.get_id_fixed("ope_centro2_ord_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_centro2_ord_delete(self):
        response = self.client.delete(
            url_for(
                "opecentro2ord.delete", id=self.get_id_fixed("ope_centro2_ord_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  ope_centro_dest
    # ===========================================================

    # ====================

    def ope_centro_dest_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro_dest_id1"),
            "ope_periodo_id_desc_sec": module_tests_ope.ope_periodo_id1(self),
            "ope_compart_id_pri": module_tests_ope.ope_compart_id1(self),
            "ope_periodo_id_desc_pri": module_tests_ope.ope_periodo_id1(self),
            "ope_atividade_id": module_tests_ope.ope_atividade_id1(self),
            "fin_pagrec_banco_id": module_tests_fin.module_tests_fin.fin_pagrec_banco_id1(
                self
            ),
            "ope_compart_id_sec": module_tests_ope.ope_compart_id1(self),
            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
            "fin_pagrec_id": module_tests_fin.module_tests_fin.fin_pagrec_id1(self),
            "ope_centro2_id_dest_sec": module_tests_ope.ope_centro2_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor": "5",
            "ope_centro2_id_dest_pri": module_tests_ope.ope_centro2_id1(self),
            "tipo_es": "E",
            "ope_centro1_id_dest_pri": module_tests_ope.ope_centro1_id1(self),
            "ope_centro1_id_dest_sec": module_tests_ope.ope_centro1_id1(self),
            "ope_centro1_id": module_tests_ope.ope_centro1_id1(self),
            "mov_itemserv_id": module_tests_mov.module_tests_mov.mov_itemserv_id1(self),
            "qnt": "5",
        }

        response = self.client.post(
            url_for("opecentrodest.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro_dest_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_centro_dest_id2"),
            "ope_periodo_id_desc_sec": module_tests_ope.ope_periodo_id1(self),
            "ope_compart_id_pri": module_tests_ope.ope_compart_id1(self),
            "ope_periodo_id_desc_pri": module_tests_ope.ope_periodo_id1(self),
            "ope_atividade_id": module_tests_ope.ope_atividade_id1(self),
            "fin_pagrec_banco_id": module_tests_fin.module_tests_fin.fin_pagrec_banco_id1(
                self
            ),
            "ope_compart_id_sec": module_tests_ope.ope_compart_id1(self),
            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
            "fin_pagrec_id": module_tests_fin.module_tests_fin.fin_pagrec_id1(self),
            "ope_centro2_id_dest_sec": module_tests_ope.ope_centro2_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor": "5",
            "ope_centro2_id_dest_pri": module_tests_ope.ope_centro2_id1(self),
            "tipo_es": "E",
            "ope_centro1_id_dest_pri": module_tests_ope.ope_centro1_id1(self),
            "ope_centro1_id_dest_sec": module_tests_ope.ope_centro1_id1(self),
            "ope_centro1_id": module_tests_ope.ope_centro1_id1(self),
            "mov_itemserv_id": module_tests_mov.module_tests_mov.mov_itemserv_id1(self),
            "qnt": "5",
        }

        response = self.client.post(
            url_for("opecentrodest.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro_dest_get(self):
        response = self.client.get(
            url_for("opecentrodest.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_centro_dest_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecentrodest.find_by_id", id=self.get_id_fixed("ope_centro_dest_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_centro_dest_delete(self):
        response = self.client.delete(
            url_for(
                "opecentrodest.delete", id=self.get_id_fixed("ope_centro_dest_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_centro2_ord_itemserv
    # ===========================================================

    # ====================

    def ope_centro2_ord_itemserv_id1(self):
        module_tests_ope.ope_centro2_ord_id1(self)
        req_post = {
            "id": self.get_id_fixed("ope_centro2_ord_itemserv_id1"),
            "valor_total_util": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor_unit_util": "5",
            "observacao_interna": "TESTE [CRUD]",
            "qnt_rend": "5",
            "data_valid": "20/07/2022",
            "ope_centro2_ord_ativ_id": self.get_id_fixed("ope_centro2_ord_ativ_id1"),
            "perc_util": "5",
            "ger_itemserv_id": module_tests_ger.module_tests_ger.ger_itemserv_id1(self),
            "ctb_comp_id": module_tests_ctb.module_tests_ctb.ctb_comp_id1(self),
            "observacao_externa": "TESTE [CRUD]",
            "qnt_total_util": "5",
        }

        response = self.client.post(
            url_for("opecentro2orditemserv.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro2_ord_itemserv_id2(self):
        module_tests_ope.ope_centro2_ord_id1(self)
        req_post = {
            "id": self.get_id_fixed("ope_centro2_ord_itemserv_id2"),
            "valor_total_util": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor_unit_util": "5",
            "observacao_interna": "TESTE [CRUD]",
            "qnt_rend": "5",
            "data_valid": "20/07/2022",
            "ope_centro2_ord_ativ_id": self.get_id_fixed("ope_centro2_ord_ativ_id1"),
            "perc_util": "5",
            "ger_itemserv_id": module_tests_ger.module_tests_ger.ger_itemserv_id1(self),
            "ctb_comp_id": module_tests_ctb.module_tests_ctb.ctb_comp_id1(self),
            "observacao_externa": "TESTE [CRUD]",
            "qnt_total_util": "5",
        }

        response = self.client.post(
            url_for("opecentro2orditemserv.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro2_ord_itemserv_get(self):
        response = self.client.get(
            url_for("opecentro2orditemserv.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_centro2_ord_itemserv_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecentro2orditemserv.find_by_id",
                id=self.get_id_fixed("ope_centro2_ord_itemserv_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_centro2_ord_itemserv_delete(self):
        response = self.client.delete(
            url_for(
                "opecentro2orditemserv.delete",
                id=self.get_id_fixed("ope_centro2_ord_itemserv_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_centro2_ord_rec
    # ===========================================================

    # ====================

    def ope_centro2_ord_rec_id1(self):
        module_tests_ope.ope_centro2_ord_id1(self)
        module_tests_ger.module_tests_ger.ger_pessoa_id1(self)
        req_post = {
            "id": self.get_id_fixed("ope_centro2_ord_rec_id1"),
            "observacao_interna": "5",
            "qnt_rend": "5",
            "data_valid": "2022-12-29T00:00:00",
            "perc_util": "5",
            "ctb_comp_id": module_tests_ctb.module_tests_ctb.ctb_comp_id1(self),
            "qnt_total_util": "5",
            "ope_compart_id": module_tests_ope.ope_compart_id1(self),
            "ctb_comp_id_imp01": module_tests_ctb.module_tests_ctb.ctb_comp_id1(self),
            "valor_unit_util": "5",
            "observacao_externa": "TESTE [CRUD]",
            "ope_centro1_id": module_tests_ope.ope_centro1_id1(self),
            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
            "ope_centro2_ord_ativ_id": self.get_id_fixed("ope_centro2_ord_ativ_id1"),
            "valor_total_util": "5",
            "ger_pessoa_endereco_id_exec": self.get_id_fixed("ger_pessoa_endereco_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ope_centro1_id_imp01": module_tests_ope.ope_centro1_id1(self),
            "ope_centro2_id_imp01": module_tests_ope.ope_centro2_id1(self),
        }

        response = self.client.post(
            url_for("opecentro2ordrec.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro2_ord_rec_id2(self):
        module_tests_ope.ope_centro2_ord_id1(self)
        module_tests_ger.module_tests_ger.ger_pessoa_id1(self)
        req_post = {
            "id": self.get_id_fixed("ope_centro2_ord_rec_id2"),
            "observacao_interna": "5",
            "qnt_rend": "5",
            "data_valid": "2022-12-29T00:00:00",
            "perc_util": "5",
            "ctb_comp_id": module_tests_ctb.module_tests_ctb.ctb_comp_id1(self),
            "qnt_total_util": "5",
            "ope_compart_id": module_tests_ope.ope_compart_id1(self),
            "ctb_comp_id_imp01": module_tests_ctb.module_tests_ctb.ctb_comp_id1(self),
            "valor_unit_util": "5",
            "observacao_externa": "TESTE [CRUD]",
            "ope_centro1_id": module_tests_ope.ope_centro1_id1(self),
            "ope_centro2_id": module_tests_ope.ope_centro2_id1(self),
            "ope_centro2_ord_ativ_id": self.get_id_fixed("ope_centro2_ord_ativ_id1"),
            "valor_total_util": "5",
            "ger_pessoa_endereco_id_exec": self.get_id_fixed("ger_pessoa_endereco_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ope_centro1_id_imp01": module_tests_ope.ope_centro1_id1(self),
            "ope_centro2_id_imp01": module_tests_ope.ope_centro2_id1(self),
        }

        response = self.client.post(
            url_for("opecentro2ordrec.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro2_ord_rec_get(self):
        response = self.client.get(
            url_for("opecentro2ordrec.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_centro2_ord_rec_get_by_id(self):
        response = self.client.get(
            url_for(
                "opecentro2ordrec.find_by_id",
                id=self.get_id_fixed("ope_centro2_ord_rec_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_centro2_ord_rec_delete(self):
        response = self.client.delete(
            url_for(
                "opecentro2ordrec.delete",
                id=self.get_id_fixed("ope_centro2_ord_rec_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_ocor_compart_mov
    # ===========================================================

    # ====================

    def ope_ocor_compart_mov_id1(self):
        module_tests_ger.module_tests_ger.ger_pessoa_id1(self)
        req_post = {
            "id": self.get_id_fixed("ope_ocor_compart_mov_id1"),
            "ger_pessoa_endereco_id_exec": self.get_id_fixed("ger_pessoa_endereco_id1"),
            "observacao": "TESTE [CRUD]",
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "data_mov": "21/07/2022",
            "numero": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ope_ocor_compart_mov_det_childs": [
                {
                    "id": self.get_id_fixed("ope_ocor_compart_mov_det_id1"),
                    "ope_compart_ocor_id": module_tests_ope.ope_compart_ocor_id1(self),
                    "qnt_medicao": "5",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "observacao": "TESTE [CRUD]1",
                    "ope_compart_id": module_tests_ope.ope_compart_id1(self),
                }
            ],
        }

        response = self.client.post(
            url_for("opeocorcompartmov.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_ocor_compart_mov_id2(self):
        module_tests_ger.module_tests_ger.ger_pessoa_id1(self)
        req_post = {
            "id": self.get_id_fixed("ope_ocor_compart_mov_id2"),
            "ger_pessoa_endereco_id_exec": self.get_id_fixed("ger_pessoa_endereco_id1"),
            "observacao": "TESTE [CRUD]",
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "data_mov": "21/07/2022",
            "numero": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ope_ocor_compart_mov_det_childs": [
                {
                    "ope_compart_ocor_id": module_tests_ope.ope_compart_ocor_id1(self),
                    "qnt_medicao": "5",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "observacao": "TESTE [CRUD]2",
                    "ope_compart_id": module_tests_ope.ope_compart_id1(self),
                }
            ],
        }

        response = self.client.post(
            url_for("opeocorcompartmov.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_ocor_compart_mov_get(self):
        response = self.client.get(
            url_for("opeocorcompartmov.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_ocor_compart_mov_get_by_id(self):
        response = self.client.get(
            url_for(
                "opeocorcompartmov.find_by_id",
                id=self.get_id_fixed("ope_ocor_compart_mov_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_ocor_compart_mov_delete(self):
        response = self.client.delete(
            url_for(
                "opeocorcompartmov.delete",
                id=self.get_id_fixed("ope_ocor_compart_mov_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_centro2
    # ===========================================================

    # ====================

    def ope_centro2_id1(self):
        module_tests_ger.module_tests_ger.ger_pessoa_id1(self)
        module_tests_ger.module_tests_ger.ger_marca_id1(self)
        req_post = {
            "id": self.get_id_fixed("ope_centro2_id1"),
            "ger_pessoa_endereco_id": self.get_id_fixed("ger_pessoa_endereco_id1"),
            "ger_umedida_id": module_tests_ger.module_tests_ger.ger_umedida_id1(self),
            "ope_centro_rat_tipo_id": module_tests_ope.ope_centro_rat_tipo_id1(self),
            "medicao_trab_centro": "A",
            "observacao": "TESTE [CRUD]",
            "data_valid": "15/07/2022",
            "ope_centro_subgrupo_id": module_tests_ope.ope_centro_subgrupo_id1(self),
            "ger_marca_modelo_id": self.get_id_fixed("ger_marca_modelo_id1"),
            "ope_centro1_id": module_tests_ope.ope_centro1_id1(self),
            "nome": "TESTE [CRUD]",
            "tipo_destinacao": "P",
            "ctb_comp_id": module_tests_ctb.module_tests_ctb.ctb_comp_id1(self),
            "tipo_ctb_comp": "1",
            "utiliza_compart": "S",
            "sigla_centro2": "TESTE [CRUD]",
            "valida_seq_medicao_trab_centro": "S",
            "ope_regiao_id": module_tests_ope.ope_regiao_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "tipo_prop": "P",
        }

        response = self.client.post(
            url_for("opecentro2.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro2_id2(self):
        module_tests_ger.module_tests_ger.ger_pessoa_id1(self)
        module_tests_ger.module_tests_ger.ger_marca_id1(self)
        req_post = {
            "id": self.get_id_fixed("ope_centro2_id2"),
            "ger_pessoa_endereco_id": self.get_id_fixed("ger_pessoa_endereco_id1"),
            "ger_umedida_id": module_tests_ger.module_tests_ger.ger_umedida_id1(self),
            "ope_centro_rat_tipo_id": module_tests_ope.ope_centro_rat_tipo_id1(self),
            "medicao_trab_centro": "A",
            "observacao": "TESTE [CRUD]",
            "data_valid": "15/07/2022",
            "ope_centro_subgrupo_id": module_tests_ope.ope_centro_subgrupo_id1(self),
            "ger_marca_modelo_id": self.get_id_fixed("ger_marca_modelo_id1"),
            "ope_centro1_id": module_tests_ope.ope_centro1_id1(self),
            "nome": "TESTE [CRUD]",
            "tipo_destinacao": "P",
            "ctb_comp_id": module_tests_ctb.module_tests_ctb.ctb_comp_id1(self),
            "tipo_ctb_comp": "1",
            "utiliza_compart": "S",
            "sigla_centro2": "TESTE [CRUD]",
            "valida_seq_medicao_trab_centro": "S",
            "ope_regiao_id": module_tests_ope.ope_regiao_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "tipo_prop": "P",
        }

        response = self.client.post(
            url_for("opecentro2.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_centro2_get(self):
        response = self.client.get(
            url_for("opecentro2.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_centro2_get_by_id(self):
        response = self.client.get(
            url_for("opecentro2.find_by_id", id=self.get_id_fixed("ope_centro2_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_centro2_delete(self):

        response = self.client.delete(
            url_for("opecentro2.delete", id=self.get_id_fixed("ope_centro2_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ope_frente_trabalho
    # ===========================================================

    # ====================

    def ope_frente_trabalho_id1(self):

        req_post = {
            "id": self.get_id_fixed("ope_frente_trabalho_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_frente_trabalho": "TESTE [CRUD]",
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opefrentetrabalho.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_frente_trabalho_id2(self):

        req_post = {
            "id": self.get_id_fixed("ope_frente_trabalho_id2"),
            "nome": "TESTE [CRUD]",
            "sigla_frente_trabalho": "TESTE [CRUD]",
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("opefrentetrabalho.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ope_frente_trabalho_get(self):
        response = self.client.get(
            url_for("opefrentetrabalho.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ope_frente_trabalho_get_by_id(self):
        response = self.client.get(
            url_for(
                "opefrentetrabalho.find_by_id",
                id=self.get_id_fixed("ope_frente_trabalho_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ope_frente_trabalho_delete(self):
        response = self.client.delete(
            url_for(
                "opefrentetrabalho.delete",
                id=self.get_id_fixed("ope_frente_trabalho_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)
