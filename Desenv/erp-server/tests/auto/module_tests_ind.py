from flask import url_for
from generic_tests import generic_tests

import module_tests_sys
import module_tests_ger


class module_tests_ind(generic_tests):

    # ===========================================================
    # ind_cnd
    # ===========================================================

    # ====================

    def ind_cnd_id1(self):

        req_post = {
            "id": self.get_id_fixed("ind_cnd_id1"),
            "config_cnd": "TESTE [CRUD]1",
            "nome": "TESTE [CRUD]1",
            "ativo": "S",
            "tipo": "S1",
            "sigla_ind_cnd": "TESTE [CRUD]1",
        }

        response = self.client.post(
            url_for("indcnd.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_cnd_id2(self):

        req_post = {
            "id": self.get_id_fixed("ind_cnd_id2"),
            "config_cnd": "TESTE [CRUD]1",
            "nome": "TESTE [CRUD]1",
            "ativo": "S",
            "tipo": "S1",
            "sigla_ind_cnd": "TESTE [CRUD]1",
        }

        response = self.client.post(
            url_for("indcnd.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_cnd_get(self):
        response = self.client.get(
            url_for("indcnd.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ind_cnd_get_by_id(self):
        response = self.client.get(
            url_for("indcnd.find_by_id", id=self.get_id_fixed("ind_cnd_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ind_cnd_delete(self):
        response = self.client.delete(
            url_for("indcnd.delete", id=self.get_id_fixed("ind_cnd_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ind_cjd
    # ===========================================================

    # ====================

    def ind_cjd_id1(self):

        req_post = {
            "id": self.get_id_fixed("ind_cjd_id1"),
            "nome": "TESTE [CRUD]1",
            "nome_tecnico": "TESTE [CRUD]1",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("indcjd.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_cjd_id2(self):

        req_post = {
            "id": self.get_id_fixed("ind_cjd_id2"),
            "nome": "TESTE [CRUD]1",
            "nome_tecnico": "TESTE [CRUD]1",
            "ativo": "S",
            "ind_cjd_ftd_childs": [{"ind_ftd_id": module_tests_ind.ind_ftd_id1(self)}],
        }

        response = self.client.post(
            url_for("indcjd.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_cjd_get(self):
        response = self.client.get(
            url_for("indcjd.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ind_cjd_get_by_id(self):
        response = self.client.get(
            url_for("indcjd.find_by_id", id=self.get_id_fixed("ind_cjd_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ind_cjd_delete(self):
        response = self.client.delete(
            url_for("indcjd.delete", id=self.get_id_fixed("ind_cjd_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ind_pnl
    # ===========================================================

    # ====================

    def ind_pnl_id1(self):

        req_post = {
            "id": self.get_id_fixed("ind_pnl_id1"),
            "tipo": "1",
            "icon": "TESTE [CRUD]1",
            "nome": "TESTE [CRUD]1",
        }

        response = self.client.post(
            url_for("indpnl.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_pnl_id2(self):

        req_post = {
            "id": self.get_id_fixed("ind_pnl_id2"),
            "tipo": "1",
            "icon": "TESTE [CRUD]1",
            "nome": "TESTE [CRUD]1",
            "ind_pnl_rel_childs": [{"ind_rel_id": module_tests_ind.ind_rel_id1(self)}],
        }

        response = self.client.post(
            url_for("indpnl.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_pnl_get(self):
        response = self.client.get(
            url_for("indpnl.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ind_pnl_get_by_id(self):
        response = self.client.get(
            url_for("indpnl.find_by_id", id=self.get_id_fixed("ind_pnl_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ind_pnl_delete(self):
        response = self.client.delete(
            url_for("indpnl.delete", id=self.get_id_fixed("ind_pnl_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ind_legenda
    # ===========================================================

    # ====================

    def ind_legenda_id1(self):

        req_post = {
            "id": self.get_id_fixed("ind_legenda_id1"),
            "sigla_ind_legenda": "TESTE [CRUD]1",
            "nome": "TESTE [CRUD]1",
            "ativo": "S",
            "ind_legenda_config_childs": [
                {
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "qnt_de": 0,
                    "qnt_ate": 100,
                    "icon": "fa-star",
                    "cor": "#121212",
                    "observacao": "xxxxx",
                },
                {
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "qnt_de": 101,
                    "qnt_ate": 200,
                    "icon": "fa-star",
                    "cor": "#g1g1g1",
                    "observacao": "yyyy",
                },
            ],
        }

        response = self.client.post(
            url_for("indlegenda.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_legenda_id2(self):

        req_post = {
            "id": self.get_id_fixed("ind_legenda_id2"),
            "sigla_ind_legenda": "TESTE [CRUD]2",
            "nome": "TESTE [CRUD]2",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("indlegenda.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_legenda_get(self):
        response = self.client.get(
            url_for("indlegenda.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ind_legenda_get_by_id(self):
        response = self.client.get(
            url_for("indlegenda.find_by_id", id=self.get_id_fixed("ind_legenda_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ind_legenda_delete(self):
        response = self.client.delete(
            url_for("indlegenda.delete", id=self.get_id_fixed("ind_legenda_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ind_prm
    # ===========================================================

    # ====================

    def ind_prm_id1(self):

        req_post = {
            "id": self.get_id_fixed("ind_prm_id1"),
            "busca_tabela": "TESTE [CRUD]1",
            "busca_campo_id": "TESTE [CRUD]1",
            "busca_campo_nome": "TESTE [CRUD]1",
            "valor_sufixo": "5",
            "busca_tabela_classe": "TESTE [CRUD]1",
            "busca_campo_nome_classe": "TESTE [CRUD]1",
            "busca_campo_id_classe": "TESTE [CRUD]1",
            "nome": "TESTE [CRUD]1",
            "obrigatorio": "S",
            "internal": "S",
            "tipo_entrada": "IS",
            "valor_prefixo": "TESTE [CRUD]1",
            "busca_valores": "TESTE [CRUD]1",
            "nome_tecnico": "TESTE [CRUD]1",
            "valor_padrao": "TESTE [CRUD]1",
            "tipo_dado": "TX",
            "ativo": "S",
            "visivel": "S",
            "ind_ftd_id": module_tests_ind.ind_ftd_id1(self),
        }

        response = self.client.post(
            url_for("indprm.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_prm_id2(self):

        req_post = {
            "id": self.get_id_fixed("ind_prm_id2"),
            "busca_tabela": "TESTE [CRUD]2",
            "busca_campo_id": "TESTE [CRUD]2",
            "valor_sufixo": "5",
            "busca_tabela_classe": "TESTE [CRUD]2",
            "nome": "TESTE [CRUD]2",
            "obrigatorio": "S",
            "internal": "S",
            "busca_campo_nome": "TESTE [CRUD]2",
            "tipo_entrada": "IS",
            "valor_prefixo": "TESTE [CRUD]2",
            "busca_valores": "TESTE [CRUD]2",
            "nome_tecnico": "TESTE [CRUD]2",
            "valor_padrao": "TESTE [CRUD]2",
            "tipo_dado": "TX",
            "ativo": "S",
            "visivel": "S",
            "busca_campo_nome_classe": "TESTE [CRUD]2",
            "busca_campo_id_classe": "TESTE [CRUD]2",
            "ind_ftd_id": module_tests_ind.ind_ftd_id1(self),
        }

        response = self.client.post(
            url_for("indprm.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_prm_get(self):
        response = self.client.get(
            url_for("indprm.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ind_prm_get_by_id(self):
        response = self.client.get(
            url_for("indprm.find_by_id", id=self.get_id_fixed("ind_prm_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ind_prm_delete(self):
        response = self.client.delete(
            url_for("indprm.delete", id=self.get_id_fixed("ind_prm_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ind
    # ===========================================================

    # ====================

    def ind_indic_id1(self):

        req_post = {
            "id": self.get_id_fixed("ind_indic_id1"),
            "acumular_trimestre": "S",
            "exibir_trimestre": "S",
            "exibir_bimestre": "S",
            "exibir_mes": "S",
            "totalizador_atributo": "1",
            "exibir_media_meta": "S",
            "acumular_quinzena": "S",
            "metodo_ordenacao": "1",
            "exibir_ano": "S",
            "grafico_tipo_atributo": "1",
            "acumular_quadrimestre": "S",
            "exibir_dia": "S",
            "grafico_valor_vazio_zero": "5",
            "grafico_tipo_ind": "1",
            "acumular_semestre": "S",
            "exibir_semestre": "S",
            "exibir_quinzena": "S",
            "acumular_bimestre": "S",
            "exibir_semana": "S",
            "acumular_mes": "S",
            "campo_ordenacao": "1",
            "exibir_media_real": "S",
            "exibir_quadrimestre": "S",
            "nome": "TESTE [CRUD]1",
            "acumular_ano": "S",
            "acumular_semana": "S",
            "casas_dec": "0101",
            "ger_umedida_id": module_tests_ger.module_tests_ger.ger_umedida_id1(self),
            "sigla_ind": "TESTE [CRUD]1",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "tipo_acumulo": "1",
            "tipo_meta": "1",
            "tipo_meta_var": "1",
            "exibir_dia_ant": "90",
            "exibir_dia_pos": "90",
            "exibir_semana_ant": "12",
            "exibir_semana_pos": "12",
            "exibir_quinzena_ant": "6",
            "exibir_quinzena_pos": "6",
            "exibir_mes_ant": "12",
            "exibir_mes_pos": "12",
            "exibir_bimestre_ant": "6",
            "exibir_bimestre_pos": "6",
            "exibir_trimestre_ant": "9",
            "exibir_trimestre_pos": "9",
            "exibir_quadrimestre_ant": "6",
            "exibir_quadrimestre_pos": "6",
            "exibir_semestre_ant": "4",
            "exibir_semestre_pos": "4",
            "exibir_ano_ant": "6",
            "exibir_ano_pos": "6",
            "ind_legenda_id": module_tests_ind.ind_legenda_id1(self),
        }

        response = self.client.post(
            url_for("ind_indic.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_indic_id2(self):

        req_post = {
            "id": self.get_id_fixed("ind_indic_id2"),
            "acumular_trimestre": "S",
            "exibir_trimestre": "S",
            "exibir_bimestre": "S",
            "exibir_mes": "S",
            "totalizador_atributo": "1",
            "exibir_media_meta": "S",
            "acumular_quinzena": "S",
            "metodo_ordenacao": "1",
            "exibir_ano": "S",
            "grafico_tipo_atributo": "1",
            "acumular_quadrimestre": "S",
            "exibir_dia": "S",
            "grafico_valor_vazio_zero": "5",
            "grafico_tipo_ind": "1",
            "acumular_semestre": "S",
            "exibir_semestre": "S",
            "exibir_quinzena": "S",
            "acumular_bimestre": "S",
            "exibir_semana": "S",
            "acumular_mes": "S",
            "campo_ordenacao": "1",
            "exibir_media_real": "S",
            "exibir_quadrimestre": "S",
            "ind_id_ponderacao": module_tests_ind.ind_indic_id1(self),
            "nome": "TESTE [CRUD]2",
            "acumular_ano": "S",
            "acumular_semana": "S",
            "casas_dec": "5",
            "ger_umedida_id": module_tests_ger.module_tests_ger.ger_umedida_id1(self),
            "sigla_ind": "TESTE [CRUD]2",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "tipo_acumulo": "1",
            "tipo_meta": "1",
            "tipo_meta_var": "1",
            "exibir_dia_ant": "90",
            "exibir_dia_pos": "90",
            "exibir_semana_ant": "12",
            "exibir_semana_pos": "12",
            "exibir_quinzena_ant": "6",
            "exibir_quinzena_pos": "6",
            "exibir_mes_ant": "12",
            "exibir_mes_pos": "12",
            "exibir_bimestre_ant": "6",
            "exibir_bimestre_pos": "6",
            "exibir_trimestre_ant": "9",
            "exibir_trimestre_pos": "9",
            "exibir_quadrimestre_ant": "6",
            "exibir_quadrimestre_pos": "6",
            "exibir_semestre_ant": "4",
            "exibir_semestre_pos": "4",
            "exibir_ano_ant": "6",
            "exibir_ano_pos": "6",
            "ind_legenda_id": module_tests_ind.ind_legenda_id1(self),
            "ind_indic_indic_childs": [
                {
                    "ind_indic_id_relac": module_tests_ind.ind_indic_id1(self),
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                }
            ],
            "ind_indic_subgrupo_childs": [
                {
                    "ind_subgrupo_id": module_tests_ind.ind_subgrupo_id1(self),
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                }
            ],
        }

        response = self.client.post(
            url_for("ind_indic.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_indic_get(self):
        response = self.client.get(
            url_for("ind_indic.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ind_indic_get_by_id(self):
        response = self.client.get(
            url_for("ind_indic.find_by_id", id=self.get_id_fixed("ind_indic_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ind_indic_delete(self):
        response = self.client.delete(
            url_for("ind_indic.delete", id=self.get_id_fixed("ind_indic_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ind_ftd
    # ===========================================================

    # ====================

    def ind_ftd_id1(self):

        req_post = {
            "id": self.get_id_fixed("ind_ftd_id1"),
            "nome": "TESTE [CRUD]1",
            "nome_tecnico": "TESTE [CRUD]1",
            "ativo": "S",
            "ind_cnd_id": module_tests_ind.ind_cnd_id1(self),
            "config_ftd": "S",
        }

        response = self.client.post(
            url_for("indftd.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_ftd_id2(self):

        req_post = {
            "id": self.get_id_fixed("ind_ftd_id2"),
            "nome": "TESTE [CRUD]2",
            "nome_tecnico": "TESTE [CRUD]2",
            "ativo": "S",
            "ind_cnd_id": module_tests_ind.ind_cnd_id1(self),
            "config_ftd": "S",
            "ind_ftd_prm_childs": [
                {
                    "ind_ftd_id": module_tests_ind.ind_ftd_id1(self),
                    "ind_prm_id": module_tests_ind.ind_prm_id1(self),
                }
            ],
        }

        response = self.client.post(
            url_for("indftd.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_ftd_get(self):
        response = self.client.get(
            url_for("indftd.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ind_ftd_get_by_id(self):
        response = self.client.get(
            url_for("indftd.find_by_id", id=self.get_id_fixed("ind_ftd_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ind_ftd_delete(self):
        response = self.client.delete(
            url_for("indftd.delete", id=self.get_id_fixed("ind_ftd_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ind_grupo
    # ===========================================================

    # ====================

    def ind_grupo_id1(self):

        req_post = {
            "id": self.get_id_fixed("ind_grupo_id1"),
            "nome": "TESTE [CRUD]1",
            "ativo": "S",
            "sigla_grupo": "TESTE [CRUD]1",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ordem_exibicao": "2",
        }

        response = self.client.post(
            url_for("indgrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_grupo_id2(self):

        req_post = {
            "id": self.get_id_fixed("ind_grupo_id2"),
            "nome": "TESTE [CRUD]2",
            "ativo": "S",
            "sigla_grupo": "TESTE [CRUD]2",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ordem_exibicao": "2",
            "ind_grupo_subgrupo_childs": [
                {
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "ind_subgrupo_id": module_tests_ind.ind_subgrupo_id1(self),
                }
            ],
        }

        response = self.client.post(
            url_for("indgrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_grupo_get(self):
        response = self.client.get(
            url_for("indgrupo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ind_grupo_get_by_id(self):
        response = self.client.get(
            url_for("indgrupo.find_by_id", id=self.get_id_fixed("ind_grupo_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ind_grupo_delete(self):
        response = self.client.delete(
            url_for("indgrupo.delete", id=self.get_id_fixed("ind_grupo_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ind_subgrupo
    # ===========================================================

    # ====================

    def ind_subgrupo_id1(self):

        req_post = {
            "id": self.get_id_fixed("ind_subgrupo_id1"),
            "sigla_subgrupo": "TESTE [CRUD]1",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ordem_exibicao": "2",
            "nome": "TESTE [CRUD]1",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("indsubgrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_subgrupo_id2(self):

        req_post = {
            "id": self.get_id_fixed("ind_subgrupo_id2"),
            "sigla_subgrupo": "TESTE [CRUD]2",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ordem_exibicao": "2",
            "nome": "TESTE [CRUD]1",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("indsubgrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_subgrupo_get(self):
        response = self.client.get(
            url_for("indsubgrupo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ind_subgrupo_get_by_id(self):
        response = self.client.get(
            url_for("indsubgrupo.find_by_id", id=self.get_id_fixed("ind_subgrupo_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ind_subgrupo_delete(self):
        response = self.client.delete(
            url_for("indsubgrupo.delete", id=self.get_id_fixed("ind_subgrupo_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ind_unit_param
    # ===========================================================

    # ====================

    def ind_unit_param_id1(self):

        req_post = {
            "id": self.get_id_fixed("ind_unit_param_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_valid_ini": "2022-12-29T00:00:00",
        }

        response = self.client.post(
            url_for("indunitparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_unit_param_id2(self):

        req_post = {
            "id": self.get_id_fixed("ind_unit_param_id2"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_valid_ini": "2022-12-29T00:00:00",
        }

        response = self.client.post(
            url_for("indunitparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_unit_param_get(self):
        response = self.client.get(
            url_for("indunitparam.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ind_unit_param_get_by_id(self):
        response = self.client.get(
            url_for(
                "indunitparam.find_by_id", id=self.get_id_fixed("ind_unit_param_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ind_unit_param_delete(self):
        response = self.client.delete(
            url_for("indunitparam.delete", id=self.get_id_fixed("ind_unit_param_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ind_rel
    # ===========================================================

    # ====================

    def ind_rel_id1(self):

        req_post = {
            "id": self.get_id_fixed("ind_rel_id1"),
            "ind_cjd_id": module_tests_ind.ind_cjd_id1(self),
            "ind_ftd_id": module_tests_ind.ind_ftd_id1(self),
            "tipo": "R",
            "nome": "TESTE [CRUD]1",
            "ativo": "S",
            "nome_tecnico": "TESTE [CRUD]1",
        }

        response = self.client.post(
            url_for("indrel.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_rel_id2(self):

        req_post = {
            "id": self.get_id_fixed("ind_rel_id2"),
            "ind_cjd_id": module_tests_ind.ind_cjd_id1(self),
            "ind_ftd_id": module_tests_ind.ind_ftd_id1(self),
            "tipo": "R",
            "nome": "TESTE [CRUD]2",
            "ativo": "S",
            "nome_tecnico": "TESTE [CRUD]2",
            "ind_rel_prm_childs": [
                {
                    "ind_prm_id": module_tests_ind.ind_prm_id1(self),
                    "ordem_exib": "2",
                    "valor_padrao": "5",
                }
            ],
            "ind_rel_var_childs": [
                {
                    "ordem_padrao": "1",
                    "var_nome_tecnico": "TESTE [CRUD]2",
                    "var_nome_tecnico_prefixo": "TESTE [CRUD]2",
                    "var_nome_descritivo": "TESTE [CRUD]2",
                    "largura": "5",
                    "var_agrupavel": "S",
                    "visivel": "S",
                }
            ],
        }

        response = self.client.post(
            url_for("indrel.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_rel_get(self):
        response = self.client.get(
            url_for("indrel.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ind_rel_get_by_id(self):
        response = self.client.get(
            url_for("indrel.find_by_id", id=self.get_id_fixed("ind_rel_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ind_rel_delete(self):
        response = self.client.delete(
            url_for("indrel.delete", id=self.get_id_fixed("ind_rel_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ind_vr_ano
    # ===========================================================

    # ====================

    def ind_vr_ano_id1(self):

        req_post = {
            "id": self.get_id_fixed("ind_vr_ano_id1"),
            "valor_real": "5",
            "valor_meta": "5",
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "atributo": "5",
            "ger_per_id": module_tests_ger.module_tests_ger.ger_per_id1(self),
            "ind_indic_id": module_tests_ind.ind_indic_id1(self),
            "aprovado_exibicao": "S",
            "import_id": "TESTE [CRUD]1",
            "import_arquivo": "TESTE [CRUD]1",
        }

        response = self.client.post(
            url_for("indvrano.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_vr_ano_id2(self):

        req_post = {
            "id": self.get_id_fixed("ind_vr_ano_id2"),
            "valor_real": "5",
            "valor_meta": "5",
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "atributo": "5",
            "ger_per_id": module_tests_ger.module_tests_ger.ger_per_id1(self),
            "ind_indic_id": module_tests_ind.ind_indic_id1(self),
            "aprovado_exibicao": "S",
            "import_id": "TESTE [CRUD]1",
            "import_arquivo": "TESTE [CRUD]1",
        }

        response = self.client.post(
            url_for("indvrano.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_vr_ano_get(self):
        response = self.client.get(
            url_for("indvrano.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ind_vr_ano_get_by_id(self):
        response = self.client.get(
            url_for("indvrano.find_by_id", id=self.get_id_fixed("ind_vr_ano_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ind_vr_ano_delete(self):
        response = self.client.delete(
            url_for("indvrano.delete", id=self.get_id_fixed("ind_vr_ano_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ind_vr_bimestre
    # ===========================================================

    # ====================

    def ind_vr_bimestre_id1(self):

        req_post = {
            "id": self.get_id_fixed("ind_vr_bimestre_id1"),
            "ind_indic_id": module_tests_ind.ind_indic_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "aprovado_exibicao": "S",
            "ger_per_id": module_tests_ger.module_tests_ger.ger_per_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "valor_real": "5",
            "valor_meta": "5",
            "atributo": "5",
            "import_id": "TESTE [CRUD]1",
            "import_arquivo": "TESTE [CRUD]1",
        }

        response = self.client.post(
            url_for("indvrbimestre.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_vr_bimestre_id2(self):

        req_post = {
            "id": self.get_id_fixed("ind_vr_bimestre_id2"),
            "ind_indic_id": module_tests_ind.ind_indic_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "aprovado_exibicao": "S",
            "ger_per_id": module_tests_ger.module_tests_ger.ger_per_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "valor_real": "5",
            "valor_meta": "5",
            "atributo": "5",
            "import_id": "TESTE [CRUD]1",
            "import_arquivo": "TESTE [CRUD]1",
        }

        response = self.client.post(
            url_for("indvrbimestre.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_vr_bimestre_get(self):
        response = self.client.get(
            url_for("indvrbimestre.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ind_vr_bimestre_get_by_id(self):
        response = self.client.get(
            url_for(
                "indvrbimestre.find_by_id", id=self.get_id_fixed("ind_vr_bimestre_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ind_vr_bimestre_delete(self):
        response = self.client.delete(
            url_for(
                "indvrbimestre.delete", id=self.get_id_fixed("ind_vr_bimestre_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ind_vr_dia
    # ===========================================================

    # ====================

    def ind_vr_dia_id1(self):

        req_post = {
            "id": self.get_id_fixed("ind_vr_dia_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ind_indic_id": module_tests_ind.ind_indic_id1(self),
            "valor_meta": "5",
            "ger_per_id": module_tests_ger.module_tests_ger.ger_per_id1(self),
            "valor_real": "5",
            "aprovado_exibicao": "S",
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "atributo": "S",
            "import_id": "TESTE [CRUD]1",
            "import_arquivo": "TESTE [CRUD]1",
        }

        response = self.client.post(
            url_for("indvrdia.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_vr_dia_id2(self):

        req_post = {
            "id": self.get_id_fixed("ind_vr_dia_id2"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ind_indic_id": module_tests_ind.ind_indic_id1(self),
            "valor_meta": "5",
            "ger_per_id": module_tests_ger.module_tests_ger.ger_per_id1(self),
            "valor_real": "5",
            "aprovado_exibicao": "S",
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "atributo": "S",
            "import_id": "TESTE [CRUD]",
            "import_arquivo": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("indvrdia.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_vr_dia_get(self):
        response = self.client.get(
            url_for("indvrdia.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ind_vr_dia_get_by_id(self):
        response = self.client.get(
            url_for("indvrdia.find_by_id", id=self.get_id_fixed("ind_vr_dia_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ind_vr_dia_delete(self):
        response = self.client.delete(
            url_for("indvrdia.delete", id=self.get_id_fixed("ind_vr_dia_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ind_vr_mes
    # ===========================================================

    # ====================

    def ind_vr_mes_id1(self):

        req_post = {
            "id": self.get_id_fixed("ind_vr_mes_id1"),
            "ger_per_id": module_tests_ger.module_tests_ger.ger_per_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ind_indic_id": module_tests_ind.ind_indic_id1(self),
            "valor_real": "5",
            "aprovado_exibicao": "S",
            "valor_meta": "5",
            "atributo": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "import_id": "TESTE [CRUD]1",
            "import_arquivo": "TESTE [CRUD]1",
        }

        response = self.client.post(
            url_for("indvrmes.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_vr_mes_id2(self):

        req_post = {
            "id": self.get_id_fixed("ind_vr_mes_id2"),
            "ger_per_id": module_tests_ger.module_tests_ger.ger_per_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ind_indic_id": module_tests_ind.ind_indic_id1(self),
            "valor_real": "5",
            "aprovado_exibicao": "S",
            "valor_meta": "5",
            "atributo": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "import_id": "TESTE [CRUD]",
            "import_arquivo": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("indvrmes.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_vr_mes_get(self):
        response = self.client.get(
            url_for("indvrmes.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ind_vr_mes_get_by_id(self):
        response = self.client.get(
            url_for("indvrmes.find_by_id", id=self.get_id_fixed("ind_vr_mes_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ind_vr_mes_delete(self):
        response = self.client.delete(
            url_for("indvrmes.delete", id=self.get_id_fixed("ind_vr_mes_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ind_vr_quadrimestre
    # ===========================================================

    # ====================

    def ind_vr_quadrimestre_id1(self):

        req_post = {
            "id": self.get_id_fixed("ind_vr_quadrimestre_id1"),
            "ger_per_id": module_tests_ger.module_tests_ger.ger_per_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ind_indic_id": module_tests_ind.ind_indic_id1(self),
            "valor_real": "5",
            "aprovado_exibicao": "S",
            "valor_meta": "5",
            "atributo": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "import_id": "TESTE [CRUD]",
            "import_arquivo": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("indvrquadrimestre.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_vr_quadrimestre_id2(self):

        req_post = {
            "id": self.get_id_fixed("ind_vr_quadrimestre_id2"),
            "ger_per_id": module_tests_ger.module_tests_ger.ger_per_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ind_indic_id": module_tests_ind.ind_indic_id1(self),
            "valor_real": "5",
            "aprovado_exibicao": "S",
            "valor_meta": "5",
            "atributo": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "import_id": "TESTE [CRUD]",
            "import_arquivo": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("indvrquadrimestre.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_vr_quadrimestre_get(self):
        response = self.client.get(
            url_for("indvrquadrimestre.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ind_vr_quadrimestre_get_by_id(self):
        response = self.client.get(
            url_for(
                "indvrquadrimestre.find_by_id",
                id=self.get_id_fixed("ind_vr_quadrimestre_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ind_vr_quadrimestre_delete(self):
        response = self.client.delete(
            url_for(
                "indvrquadrimestre.delete",
                id=self.get_id_fixed("ind_vr_quadrimestre_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ind_vr_quinzena
    # ===========================================================

    # ====================

    def ind_vr_quinzena_id1(self):

        req_post = {
            "id": self.get_id_fixed("ind_vr_quinzena_id1"),
            "ger_per_id": module_tests_ger.module_tests_ger.ger_per_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ind_indic_id": module_tests_ind.ind_indic_id1(self),
            "valor_real": "5",
            "aprovado_exibicao": "S",
            "valor_meta": "5",
            "atributo": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "import_id": "TESTE [CRUD]",
            "import_arquivo": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("indvrquinzena.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_vr_quinzena_id2(self):

        req_post = {
            "id": self.get_id_fixed("ind_vr_quinzena_id2"),
            "ger_per_id": module_tests_ger.module_tests_ger.ger_per_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ind_indic_id": module_tests_ind.ind_indic_id1(self),
            "valor_real": "5",
            "aprovado_exibicao": "S",
            "valor_meta": "5",
            "atributo": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "import_id": "TESTE [CRUD]",
            "import_arquivo": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("indvrquinzena.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_vr_quinzena_get(self):
        response = self.client.get(
            url_for("indvrquinzena.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ind_vr_quinzena_get_by_id(self):
        response = self.client.get(
            url_for(
                "indvrquinzena.find_by_id", id=self.get_id_fixed("ind_vr_quinzena_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ind_vr_quinzena_delete(self):
        response = self.client.delete(
            url_for(
                "indvrquinzena.delete", id=self.get_id_fixed("ind_vr_quinzena_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ind_vr_semana
    # ===========================================================

    # ====================

    def ind_vr_semana_id1(self):

        req_post = {
            "id": self.get_id_fixed("ind_vr_semana_id1"),
            "ger_per_id": module_tests_ger.module_tests_ger.ger_per_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ind_indic_id": module_tests_ind.ind_indic_id1(self),
            "valor_real": "5",
            "aprovado_exibicao": "S",
            "valor_meta": "5",
            "atributo": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "import_id": "TESTE [CRUD]",
            "import_arquivo": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("indvrsemana.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_vr_semana_id2(self):

        req_post = {
            "id": self.get_id_fixed("ind_vr_semana_id2"),
            "ger_per_id": module_tests_ger.module_tests_ger.ger_per_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ind_indic_id": module_tests_ind.ind_indic_id1(self),
            "valor_real": "5",
            "aprovado_exibicao": "S",
            "valor_meta": "5",
            "atributo": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "import_id": "TESTE [CRUD]",
            "import_arquivo": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("indvrsemana.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_vr_semana_get(self):
        response = self.client.get(
            url_for("indvrsemana.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ind_vr_semana_get_by_id(self):
        response = self.client.get(
            url_for(
                "indvrsemana.find_by_id", id=self.get_id_fixed("ind_vr_semana_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ind_vr_semana_delete(self):
        response = self.client.delete(
            url_for("indvrsemana.delete", id=self.get_id_fixed("ind_vr_semana_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ind_vr_semestre
    # ===========================================================

    # ====================

    def ind_vr_semestre_id1(self):

        req_post = {
            "id": self.get_id_fixed("ind_vr_semestre_id1"),
            "ger_per_id": module_tests_ger.module_tests_ger.ger_per_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ind_indic_id": module_tests_ind.ind_indic_id1(self),
            "valor_real": "5",
            "aprovado_exibicao": "S",
            "valor_meta": "5",
            "atributo": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "import_id": "TESTE [CRUD]",
            "import_arquivo": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("indvrsemestre.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_vr_semestre_id2(self):

        req_post = {
            "id": self.get_id_fixed("ind_vr_semestre_id2"),
            "ger_per_id": module_tests_ger.module_tests_ger.ger_per_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ind_indic_id": module_tests_ind.ind_indic_id1(self),
            "valor_real": "5",
            "aprovado_exibicao": "S",
            "valor_meta": "5",
            "atributo": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "import_id": "TESTE [CRUD]",
            "import_arquivo": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("indvrsemestre.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_vr_semestre_get(self):
        response = self.client.get(
            url_for("indvrsemestre.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ind_vr_semestre_get_by_id(self):
        response = self.client.get(
            url_for(
                "indvrsemestre.find_by_id", id=self.get_id_fixed("ind_vr_semestre_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ind_vr_semestre_delete(self):
        response = self.client.delete(
            url_for(
                "indvrsemestre.delete", id=self.get_id_fixed("ind_vr_semestre_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ind_vr_trimestre
    # ===========================================================

    # ====================

    def ind_vr_trimestre_id1(self):

        req_post = {
            "id": self.get_id_fixed("ind_vr_trimestre_id1"),
            "ger_per_id": module_tests_ger.module_tests_ger.ger_per_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ind_indic_id": module_tests_ind.ind_indic_id1(self),
            "valor_real": "5",
            "aprovado_exibicao": "S",
            "valor_meta": "5",
            "atributo": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "import_id": "TESTE [CRUD]",
            "import_arquivo": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("indvrtrimestre.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_vr_trimestre_id2(self):

        req_post = {
            "id": self.get_id_fixed("ind_vr_trimestre_id2"),
            "ger_per_id": module_tests_ger.module_tests_ger.ger_per_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ind_indic_id": module_tests_ind.ind_indic_id1(self),
            "valor_real": "5",
            "aprovado_exibicao": "S",
            "valor_meta": "5",
            "atributo": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "import_id": "TESTE [CRUD]",
            "import_arquivo": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("indvrtrimestre.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_vr_trimestre_get(self):
        response = self.client.get(
            url_for("indvrtrimestre.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ind_vr_trimestre_get_by_id(self):
        response = self.client.get(
            url_for(
                "indvrtrimestre.find_by_id",
                id=self.get_id_fixed("ind_vr_trimestre_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ind_vr_trimestre_delete(self):
        response = self.client.delete(
            url_for(
                "indvrtrimestre.delete", id=self.get_id_fixed("ind_vr_trimestre_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ind_vr_meta
    # ===========================================================

    # ====================

    def ind_vr_meta_id1(self):

        req_post = {
            "id": self.get_id_fixed("ind_vr_meta_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ger_per_id": module_tests_ger.module_tests_ger.ger_per_id1(self),
            "ind_indic_id": module_tests_ind.ind_indic_id1(self),
            "atributo": "TESTE [CRUD]1",
            "valor_meta": "5",
            "aprovado_exibicao": "S",
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ordem": "S",
            "import_id": "TESTE [CRUD]1",
            "import_arquivo": "TESTE [CRUD]1",
        }

        response = self.client.post(
            url_for("indvrmeta.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_vr_meta_id2(self):

        req_post = {
            "id": self.get_id_fixed("ind_vr_meta_id2"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ger_per_id": module_tests_ger.module_tests_ger.ger_per_id1(self),
            "ind_indic_id": module_tests_ind.ind_indic_id1(self),
            "atributo": "TESTE [CRUD]1",
            "valor_meta": "5",
            "aprovado_exibicao": "S",
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ordem": "S",
            "import_id": "TESTE [CRUD]1",
            "import_arquivo": "TESTE [CRUD]1",
        }

        response = self.client.post(
            url_for("indvrmeta.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ind_vr_meta_get(self):
        response = self.client.get(
            url_for("indvrmeta.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ind_vr_meta_get_by_id(self):
        response = self.client.get(
            url_for("indvrmeta.find_by_id", id=self.get_id_fixed("ind_vr_meta_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ind_vr_meta_delete(self):
        response = self.client.delete(
            url_for("indvrmeta.delete", id=self.get_id_fixed("ind_vr_meta_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)
