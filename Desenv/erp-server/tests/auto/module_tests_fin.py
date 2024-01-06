from flask import url_for

from generic_tests import generic_tests


import module_tests_ger
import module_tests_ope
import module_tests_sys
import module_tests_mov


class module_tests_fin(generic_tests):

    # ===========================================================
    # fin_Banco
    # ===========================================================

    # ====================

    def fin_banco_id1(self):

        req_post = {
            "id": self.get_id_fixed("fin_banco_id1"),
            "nome": "TESTE [CRUD]",
            "nr_banco": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("finbanco.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_banco_id2(self):

        req_post = {
            "id": self.get_id_fixed("fin_banco_id2"),
            "nome": "TESTE [CRUD]",
            "nr_banco": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("finbanco.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_banco_get(self):
        response = self.client.get(
            url_for("finbanco.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fin_banco_get_by_id(self):
        response = self.client.get(
            url_for("finbanco.find_by_id", id=self.get_id_fixed("fin_banco_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def fin_banco_delete(self):
        response = self.client.delete(
            url_for("finbanco.delete", id=self.get_id_fixed("fin_banco_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fin_recibo
    # ===========================================================

    # ====================

    def fin_recibo_id1(self):
        module_tests_ger.module_tests_ger.ger_pessoa_id1(self)

        req_post = {
            "id": self.get_id_fixed("fin_recibo_id1"),
            "conteudo": "TESTE [CRUD]",
            "data_recibo": "29/06/2022",
            "ger_pessoa_endereco_id": self.get_id_fixed("ger_pessoa_endereco_id1"),
            "nome": "TESTE [CRUD]",
            "nome_pessoa": "TESTE [CRUD]",
            "nr_doc_pessoa": "5",
            "status": "PD",
            "status_observacao": "Obserbação",
            "tipo_doc_pessoa": "Tipo de documento",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor": "5",
        }

        response = self.client.post(
            url_for("finrecibo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_recibo_id2(self):
        module_tests_ger.module_tests_ger.ger_pessoa_id1(self)
        req_post = {
            "id": self.get_id_fixed("fin_recibo_id2"),
            "conteudo": "TESTE [CRUD]",
            "data_recibo": "29/06/2022",
            "ger_pessoa_endereco_id": self.get_id_fixed("ger_pessoa_endereco_id1"),
            "nome": "TESTE [CRUD]",
            "nome_pessoa": "TESTE [CRUD]",
            "nr_doc_pessoa": "5",
            "status": "EA",
            "status_observacao": "S",
            "tipo_doc_pessoa": "S",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor": "5",
        }

        response = self.client.post(
            url_for("finrecibo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_recibo_get(self):
        response = self.client.get(
            url_for("finrecibo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fin_recibo_get_by_id(self):
        response = self.client.get(
            url_for("finrecibo.find_by_id", id=self.get_id_fixed("fin_recibo_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def fin_recibo_delete(self):
        response = self.client.delete(
            url_for("finrecibo.delete", id=self.get_id_fixed("fin_recibo_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fin_class
    # ===========================================================

    # ====================

    def fin_class_id1(self):

        req_post = {
            "id": self.get_id_fixed("fin_class_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "fixo_variavel": "F",
            "nome": "TESTE [CRUD]",
            "sigla_class": "TESTE [CRUD]",
            "tipo_es": "S",
            "tipo_fluxo": "PR",
            "tipo_prev": "S",
        }

        response = self.client.post(
            url_for("finclass.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_class_id2(self):

        req_post = {
            "id": self.get_id_fixed("fin_class_id2"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "fixo_variavel": "F",
            "nome": "TESTE [CRUD]",
            "sigla_class": "TESTE [CRUD]",
            "tipo_es": "E",
            "tipo_fluxo": "PR",
            "tipo_prev": "S",
        }

        response = self.client.post(
            url_for("finclass.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_class_get(self):
        response = self.client.get(
            url_for("finclass.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fin_class_get_by_id(self):
        response = self.client.get(
            url_for("finclass.find_by_id", id=self.get_id_fixed("fin_class_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def fin_class_delete(self):
        response = self.client.delete(
            url_for("finclass.delete", id=self.get_id_fixed("fin_class_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fin_class_agrup
    # ===========================================================

    # ====================

    def fin_class_agrup_id1(self):

        req_post = {
            "id": self.get_id_fixed("fin_class_agrup_id1"),
            "nome": "TESTE [CRUD]",
            "padrao": "S",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("finclassagrup.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_class_agrup_id2(self):

        req_post = {
            "id": self.get_id_fixed("fin_class_agrup_id2"),
            "nome": "TESTE [CRUD]",
            "padrao": "S",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "fin_class_agrup_grupo_childs": [
                {
                    "id": self.get_id_fixed("fin_class_agrup_grupo_id1"),
                    "fin_class_grupo_id": module_tests_fin.fin_class_grupo_id1(self),
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "fin_class_id": module_tests_fin.fin_class_id1(self),
                }
            ],
        }

        response = self.client.post(
            url_for("finclassagrup.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_class_agrup_get(self):

        response = self.client.get(
            url_for("finclassagrup.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fin_class_agrup_get_by_id(self):
        response = self.client.get(
            url_for(
                "finclassagrup.find_by_id", id=self.get_id_fixed("fin_class_agrup_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def fin_class_agrup_delete(self):
        response = self.client.delete(
            url_for(
                "finclassagrup.delete", id=self.get_id_fixed("fin_class_agrup_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fin_class_grupo
    # ===========================================================

    # ====================

    def fin_class_grupo_id1(self):

        req_post = {
            "id": self.get_id_fixed("fin_class_grupo_id1"),
            "estrutura": "F",
            "nome": "TESTE [CRUD]",
            "sigla_class_grupo": "Max-ForwardsTESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("finclassgrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_class_grupo_id2(self):

        req_post = {
            "id": self.get_id_fixed("fin_class_grupo_id2"),
            "estrutura": "F",
            "nome": "TESTE [CRUD]",
            "sigla_class_grupo": "Max-TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("finclassgrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_class_grupo_get(self):

        response = self.client.get(
            url_for("finclassgrupo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fin_class_grupo_get_by_id(self):
        response = self.client.get(
            url_for(
                "finclassgrupo.find_by_id", id=self.get_id_fixed("fin_class_grupo_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def fin_class_grupo_delete(self):
        response = self.client.delete(
            url_for(
                "finclassgrupo.delete", id=self.get_id_fixed("fin_class_grupo_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fin_cond_pagrec
    # ===========================================================

    # ====================

    def fin_cond_pagrec_id1(self):

        req_post = {
            "id": self.get_id_fixed("fin_cond_pagrec_id1"),
            "considera_feriado": "S",
            "considera_final_sem": "N",
            "nome": "TESTE [CRUD]",
            "observacao": "TESTE [CRUD]",
            "qnt_dia_ini": "5",
            "sigla_cond_pagamento": "TESTE [CRUD]",
            "tipo_prazo": "S",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("fincondpagrec.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_cond_pagrec_id2(self):

        req_post = {
            "id": self.get_id_fixed("fin_cond_pagrec_id2"),
            "considera_feriado": "S",
            "considera_final_sem": "N",
            "nome": "TESTE [CRUD]",
            "observacao": "TESTE [CRUD]",
            "qnt_dia_ini": "5",
            "sigla_cond_pagamento": "TESTE [CRUD]",
            "tipo_prazo": "S",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("fincondpagrec.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_cond_pagrec_get(self):

        response = self.client.get(
            url_for("fincondpagrec.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fin_cond_pagrec_get_by_id(self):
        response = self.client.get(
            url_for(
                "fincondpagrec.find_by_id", id=self.get_id_fixed("fin_cond_pagrec_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def fin_cond_pagrec_delete(self):
        response = self.client.delete(
            url_for(
                "fincondpagrec.delete", id=self.get_id_fixed("fin_cond_pagrec_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fin_recibo_tipo
    # ===========================================================

    # ====================

    def fin_recibo_tipo_id1(self):

        req_post = {
            "id": self.get_id_fixed("fin_recibo_tipo_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "nome": "TESTE [CRUD]",
            "padrao": "S",
            "ativo": "S",
            "sigla_fin_recibo_tipo": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("finrecibotipo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_recibo_tipo_id2(self):

        req_post = {
            "id": self.get_id_fixed("fin_recibo_tipo_id2"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "nome": "TESTE [CRUD]",
            "padrao": "S",
            "ativo": "S",
            "sigla_fin_recibo_tipo": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("finrecibotipo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_recibo_tipo_get(self):
        response = self.client.get(
            url_for("finrecibotipo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fin_recibo_tipo_get_by_id(self):
        response = self.client.get(
            url_for(
                "finrecibotipo.find_by_id", id=self.get_id_fixed("fin_recibo_tipo_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def fin_recibo_tipo_delete(self):
        response = self.client.delete(
            url_for(
                "finrecibotipo.delete", id=self.get_id_fixed("fin_recibo_tipo_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fin_pagrec_versao
    # ===========================================================

    # ====================

    def fin_pagrec_versao_id1(self):

        req_post = {
            "id": self.get_id_fixed("fin_pagrec_versao_id1"),
            "data_per_fin": "2022-12-29T00:00:00",
            "data_per_ini": "2022-12-29T00:00:00",
            "nome": "TESTE [CRUD]",
            "sigla_versao": "TESTE [CRUD]",
            "tipo_per": "A",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "versao_atual": "S",
        }

        response = self.client.post(
            url_for("finpagrecversao.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_pagrec_versao_id2(self):

        req_post = {
            "id": self.get_id_fixed("fin_pagrec_versao_id2"),
            "data_per_fin": "2022-12-29T00:00:00",
            "data_per_ini": "2022-12-29T00:00:00",
            "nome": "TESTE [CRUD]",
            "sigla_versao": "TESTE [CRUD]",
            "tipo_per": "A",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "versao_atual": "S",
        }

        response = self.client.post(
            url_for("finpagrecversao.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_pagrec_versao_get(self):
        response = self.client.get(
            url_for("finpagrecversao.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fin_pagrec_versao_get_by_id(self):
        response = self.client.get(
            url_for(
                "finpagrecversao.find_by_id",
                id=self.get_id_fixed("fin_pagrec_versao_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def fin_pagrec_versao_delete(self):
        response = self.client.delete(
            url_for(
                "finpagrecversao.delete", id=self.get_id_fixed("fin_pagrec_versao_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fin_tipo_variacao
    # ===========================================================

    # ====================

    def fin_tipo_variacao_id1(self):

        req_post = {
            "id": self.get_id_fixed("fin_tipo_variacao_id1"),
            "ativo": "N",
            "nome": "TESTE [CRUD]",
            "tipo": "A",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor_positivo": "S",
            "sigla_fin_tipo_variacao": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("fintipovariacao.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_tipo_variacao_id2(self):

        req_post = {
            "id": self.get_id_fixed("fin_tipo_variacao_id2"),
            "ativo": "N",
            "nome": "TESTE [CRUD]",
            "tipo": "A",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor_positivo": "S",
            "sigla_fin_tipo_variacao": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("fintipovariacao.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_tipo_variacao_get(self):
        response = self.client.get(
            url_for("fintipovariacao.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fin_tipo_variacao_get_by_id(self):
        response = self.client.get(
            url_for(
                "fintipovariacao.find_by_id",
                id=self.get_id_fixed("fin_tipo_variacao_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def fin_tipo_variacao_delete(self):
        response = self.client.delete(
            url_for(
                "fintipovariacao.delete", id=self.get_id_fixed("fin_tipo_variacao_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fin_unit_param
    # ===========================================================

    # ====================

    def fin_unit_param_id1(self):

        req_post = {
            "id": self.get_id_fixed("fin_unit_param_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_valid_ini": "29/12/2003",
        }

        response = self.client.post(
            url_for("finunitparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_unit_param_id2(self):

        req_post = {
            "id": self.get_id_fixed("fin_unit_param_id2"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_valid_ini": "29/12/2003",
        }

        response = self.client.post(
            url_for("finunitparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_unit_param_get(self):
        response = self.client.get(
            url_for("finunitparam.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fin_unit_param_get_by_id(self):
        response = self.client.get(
            url_for(
                "finunitparam.find_by_id", id=self.get_id_fixed("fin_unit_param_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def fin_unit_param_delete(self):
        response = self.client.delete(
            url_for("finunitparam.delete", id=self.get_id_fixed("fin_unit_param_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fin_cond_pagrec_config
    # ===========================================================

    # ====================

    def fin_cond_pagrec_config_id1(self):

        req_post = {
            "id": self.get_id_fixed("fin_cond_pagrec_config_id1"),
            "fin_cond_pag_rec_id": module_tests_fin.fin_cond_pagrec_id1(self),
            "qnt_dia": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("fincondpagrecconfig.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_cond_pagrec_config_id2(self):

        req_post = {
            "id": self.get_id_fixed("fin_cond_pagrec_config_id2"),
            "fin_cond_pag_rec_id": module_tests_fin.fin_cond_pagrec_id1(self),
            "qnt_dia": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("fincondpagrecconfig.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_cond_pagrec_config_get(self):
        response = self.client.get(
            url_for("fincondpagrecconfig.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fin_cond_pagrec_config_get_by_id(self):
        response = self.client.get(
            url_for(
                "fincondpagrecconfig.find_by_id",
                id=self.get_id_fixed("fin_cond_pagrec_config_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def fin_cond_pagrec_config_delete(self):
        response = self.client.delete(
            url_for(
                "fincondpagrecconfig.delete",
                id=self.get_id_fixed("fin_cond_pagrec_config_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fin_doc_tipo
    # ===========================================================

    # ====================

    def fin_doc_tipo_id1(self):
        req_post = {
            "id": self.get_id_fixed("fin_doc_tipo_id1"),
            "ger_numeracao_id": module_tests_ger.module_tests_ger.ger_numeracao_id1(
                self
            ),
            "nome": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "sigla_fin_doc_tipo": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("findoctipo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_doc_tipo_id2(self):

        req_post = {
            "id": self.get_id_fixed("fin_doc_tipo_id2"),
            "ger_numeracao_id": module_tests_ger.module_tests_ger.ger_numeracao_id1(
                self
            ),
            "nome": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "sigla_fin_doc_tipo": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("findoctipo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_doc_tipo_get(self):
        response = self.client.get(
            url_for("findoctipo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fin_doc_tipo_get_by_id(self):
        response = self.client.get(
            url_for("findoctipo.find_by_id", id=self.get_id_fixed("fin_doc_tipo_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def fin_doc_tipo_delete(self):
        response = self.client.delete(
            url_for("findoctipo.delete", id=self.get_id_fixed("fin_doc_tipo_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fin_conta
    # ===========================================================

    # ====================

    def fin_conta_id1(self):

        req_post = {
            "id": self.get_id_fixed("fin_conta_id1"),
            "fin_banco_id": module_tests_fin.fin_banco_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "nome": "TESTE [CRUD]",
            "nr_agencia": "TESTE [CRUD]",
            "nr_conta": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("finconta.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_conta_id2(self):

        req_post = {
            "id": self.get_id_fixed("fin_conta_id2"),
            "fin_banco_id": module_tests_fin.fin_banco_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "nome": "TESTE [CRUD]",
            "nr_agencia": "TESTE [CRUD]",
            "nr_conta": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("finconta.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_conta_get(self):
        response = self.client.get(
            url_for("finconta.find_all"), headers=self.create_token()
        )
        result = len(response.json) > 0
        self.assertTrue(result)

    # ====================

    def fin_conta_get_by_id(self):
        response = self.client.get(
            url_for("finconta.find_by_id", id=self.get_id_fixed("fin_conta_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ===================

    def fin_conta_delete(self):
        response = self.client.delete(
            url_for("finconta.delete", id=self.get_id_fixed("fin_conta_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fin_lote
    # ===========================================================

    # ====================

    def fin_lote_id1(self):

        req_post = {
            "id": self.get_id_fixed("fin_lote_id1"),
            "data_lote": "20/05/2001",
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "nome": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "sigla_fin_lote": "TESTE [CRUD]",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("finlote.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_lote_id2(self):

        req_post = {
            "id": self.get_id_fixed("fin_lote_id2"),
            "data_lote": "20/05/2001",
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "nome": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "sigla_fin_lote": "TESTE [CRUD]",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("finlote.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_lote_get(self):
        response = self.client.get(
            url_for("finlote.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fin_lote_get_by_id(self):
        response = self.client.get(
            url_for("finlote.find_by_id", id=self.get_id_fixed("fin_lote_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ===================

    def fin_lote_delete(self):
        response = self.client.delete(
            url_for("finlote.delete", id=self.get_id_fixed("fin_lote_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fin_pagrec
    # ===========================================================

    # ====================

    def fin_pagrec_id1(self):

        req_post = {
            "id": self.get_id_fixed("fin_pagrec_id1"),
            "data_mov": "02/02/2001",
            "data_valid": "02/02/2001",
            "fin_cond_pagrec_id": module_tests_fin.fin_cond_pagrec_id1(self),
            "fin_doc_tipo_id": module_tests_fin.fin_doc_tipo_id1(self),
            "fin_pagrec_tipo_id": module_tests_fin.fin_pagrec_tipo_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ger_pessoa_id_pagrec": module_tests_ger.module_tests_ger.ger_pessoa_id1(
                self
            ),
            "ger_pessoa_id": module_tests_ger.module_tests_ger.ger_pessoa_id1(self),
            "ope_centro_rat_tipo_id": module_tests_ope.module_tests_ope.ope_centro_rat_tipo_id1(
                self
            ),
            "numero_doc_pagrec": "2",
            "numero_parc_total": "5",
            "observacao": "2",
            "process_id": module_tests_sys.module_tests_sys.sys_process_log_id1(self),
            "tipo_es": "E",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor_pagrec": "5",
            "fin_pagrec_parc_childs": [
                {
                    "id": self.get_id_fixed("fin_pagrec_parc_id1"),
                    "data_venc": "29/12/2003",
                    "valor_desconto": "5",
                    "valor_pagrec": "5",
                    "valor_multa": "5",
                    "valor_juro": "5",
                    "numero_parc": "5",
                    "fin_doc_tipo_id": module_tests_fin.fin_doc_tipo_id1(self),
                    "data_valid": "29/12/2003",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                }
            ],
        }

        response = self.client.post(
            url_for("finpagrec.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_pagrec_id2(self):

        req_post = {
            "id": self.get_id_fixed("fin_pagrec_id2"),
            "data_mov": "02/02/2001",
            "data_valid": "02/02/2001",
            "fin_cond_pagrec_id": module_tests_fin.fin_cond_pagrec_id1(self),
            "fin_doc_tipo_id": module_tests_fin.fin_doc_tipo_id1(self),
            "fin_pagrec_tipo_id": module_tests_fin.fin_pagrec_tipo_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ger_pessoa_id_pagrec": module_tests_ger.module_tests_ger.ger_pessoa_id1(
                self
            ),
            "ger_pessoa_id": module_tests_ger.module_tests_ger.ger_pessoa_id1(self),
            "ope_centro_rat_tipo_id": module_tests_ope.module_tests_ope.ope_centro_rat_tipo_id1(
                self
            ),
            "numero_doc_pagrec": "2",
            "numero_parc_total": "5",
            "observacao": "2",
            "process_id": module_tests_sys.module_tests_sys.sys_process_log_id1(self),
            "tipo_es": "E",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor_pagrec": "5",
            "fin_pagrec_parc_childs": [
                {
                    "data_venc": "29/12/2003",
                    "valor_desconto": "5",
                    "valor_pagrec": "5",
                    "valor_multa": "5",
                    "valor_juro": "5",
                    "numero_parc": "5",
                    "fin_doc_tipo_id": module_tests_fin.fin_doc_tipo_id1(self),
                    "data_valid": "29/12/2003",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                }
            ],
        }

        response = self.client.post(
            url_for("finpagrec.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_pagrec_get(self):
        response = self.client.get(
            url_for("finpagrec.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fin_pagrec_get_by_id(self):
        response = self.client.get(
            url_for("finpagrec.find_by_id", id=self.get_id_fixed("fin_pagrec_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ===================

    def fin_pagrec_delete(self):
        response = self.client.delete(
            url_for("finpagrec.delete", id=self.get_id_fixed("fin_pagrec_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fin_pagrec_tipo
    # ===========================================================

    # ====================

    def fin_pagrec_tipo_id1(self):

        req_post = {
            "id": self.get_id_fixed("fin_pagrec_tipo_id1"),
            "aceita_entrada": "S",
            "aceita_saida": "S",
            "nome": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "sigla_fin_pagrec_tipo": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("finpagrectipo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_pagrec_tipo_id2(self):

        req_post = {
            "id": self.get_id_fixed("fin_pagrec_tipo_id2"),
            "aceita_entrada": "S",
            "aceita_saida": "S",
            "nome": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "sigla_fin_pagrec_tipo": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("finpagrectipo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_pagrec_tipo_get(self):
        response = self.client.get(
            url_for("finpagrectipo.find_all"), headers=self.create_token()
        )
        result = len(response.json) > 0
        self.assertTrue(result)

    # ====================

    def fin_pagrec_tipo_get_by_id(self):
        response = self.client.get(
            url_for(
                "finpagrectipo.find_by_id", id=self.get_id_fixed("fin_pagrec_tipo_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ===================

    def fin_pagrec_tipo_delete(self):
        response = self.client.delete(
            url_for(
                "finpagrectipo.delete", id=self.get_id_fixed("fin_pagrec_tipo_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fin_pagrec_prev
    # ===========================================================

    # ====================

    def fin_pagrec_prev_id1(self):

        req_post = {
            "id": self.get_id_fixed("fin_pagrec_prev_id1"),
            "data_per": "01/02/2022",
            "data_valid": "01/02/2022",
            "fin_class_id": module_tests_fin.fin_class_id1(self),
            "fin_pagrec_versao_id": module_tests_fin.fin_pagrec_versao_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ger_pessoa_id": module_tests_ger.module_tests_ger.ger_pessoa_id1(self),
            "process_id": module_tests_sys.module_tests_sys.sys_process_log_id1(self),
            "tipo_es": "E",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor01": "12",
            "valor02": "12",
            "valor03": "12",
            "valor04": "12",
            "valor05": "12",
            "valor06": "12",
            "valor07": "12",
            "valor08": "12",
            "valor09": "12",
            "valor10": "12",
            "valor11": "12",
            "valor12": "12",
            "valor13": "12",
            "valor14": "12",
            "valor15": "12",
            "valor16": "12",
            "valor17": "12",
            "valor18": "12",
            "valor19": "12",
            "valor20": "12",
            "valor21": "12",
            "valor22": "12",
            "valor23": "12",
            "valor24": "12",
            "valor25": "12",
            "valor26": "12",
            "valor27": "12",
            "valor28": "12",
            "valor29": "12",
            "valor30": "12",
            "valor31": "12",
        }

        response = self.client.post(
            url_for("finpagrecprev.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_pagrec_prev_id2(self):

        req_post = {
            "id": self.get_id_fixed("fin_pagrec_prev_id2"),
            "data_per": "01/02/2022",
            "data_valid": "01/02/2022",
            "fin_class_id": module_tests_fin.fin_class_id1(self),
            "fin_pagrec_versao_id": module_tests_fin.fin_pagrec_versao_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "ger_pessoa_id": module_tests_ger.module_tests_ger.ger_pessoa_id1(self),
            "process_id": module_tests_sys.module_tests_sys.sys_process_log_id1(self),
            "tipo_es": "E",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor01": "12",
            "valor02": "12",
            "valor03": "12",
            "valor04": "12",
            "valor05": "12",
            "valor06": "12",
            "valor07": "12",
            "valor08": "12",
            "valor09": "12",
            "valor10": "12",
            "valor11": "12",
            "valor12": "12",
            "valor13": "12",
            "valor14": "12",
            "valor15": "12",
            "valor16": "12",
            "valor17": "12",
            "valor18": "12",
            "valor19": "12",
            "valor20": "12",
            "valor21": "12",
            "valor22": "12",
            "valor23": "12",
            "valor24": "12",
            "valor25": "12",
            "valor26": "12",
            "valor27": "12",
            "valor28": "12",
            "valor29": "12",
            "valor30": "12",
            "valor31": "12",
        }

        response = self.client.post(
            url_for("finpagrecprev.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_pagrec_prev_get(self):
        response = self.client.get(
            url_for("finpagrecprev.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fin_pagrec_prev_get_by_id(self):
        response = self.client.get(
            url_for(
                "finpagrecprev.find_by_id", id=self.get_id_fixed("fin_pagrec_prev_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ===================

    def fin_pagrec_prev_delete(self):
        response = self.client.delete(
            url_for(
                "finpagrecprev.delete", id=self.get_id_fixed("fin_pagrec_prev_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fin_pagrec_banco
    # ===========================================================

    # ====================

    def fin_pagrec_banco_id1(self):

        req_post = {
            "id": self.get_id_fixed("fin_pagrec_banco_id1"),
            "data_mov": "30/06/2001",
            "data_valid": "30/06/2001",
            "fin_conta_id": module_tests_fin.fin_conta_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "numero_doc_pagrec": "S",
            "observacao": "G",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor": "5",
        }

        response = self.client.post(
            url_for("finpagrecbanco.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_pagrec_banco_id2(self):

        req_post = {
            "id": self.get_id_fixed("fin_pagrec_banco_id2"),
            "data_mov": "30/06/2001",
            "data_valid": "30/06/2001",
            "fin_conta_id": module_tests_fin.fin_conta_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "numero_doc_pagrec": "S",
            "observacao": "G",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor": "5",
        }

        response = self.client.post(
            url_for("finpagrecbanco.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_pagrec_banco_get(self):
        response = self.client.get(
            url_for("finpagrecbanco.find_all"), headers=self.create_token()
        )
        result = len(response.json) > 0
        self.assertTrue(result)

    # ====================

    def fin_pagrec_banco_get_by_id(self):
        response = self.client.get(
            url_for(
                "finpagrecbanco.find_by_id",
                id=self.get_id_fixed("fin_pagrec_banco_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ===================

    def fin_pagrec_banco_delete(self):
        response = self.client.delete(
            url_for(
                "finpagrecbanco.delete", id=self.get_id_fixed("fin_pagrec_banco_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fin_pagrec_banco_extrato
    # ===========================================================

    # ====================

    def fin_pagrec_banco_extrato_id1(self):

        req_post = {
            "id": self.get_id_fixed("fin_pagrec_banco_extrato_id1"),
            "data_extrato": "15/07/2004",
            "descricao": "TESTE [CRUD]",
            "fin_conta_id": module_tests_fin.fin_conta_id1(self),
            "numero_doc": "5",
            "process_id": module_tests_sys.module_tests_sys.sys_process_log_id1(self),
            "status": "PD",
            "status_observacao": "D",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor": "5",
        }

        response = self.client.post(
            url_for("finpagrecbancoextrato.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_pagrec_banco_extrato_id2(self):

        req_post = {
            "id": self.get_id_fixed("fin_pagrec_banco_extrato_id2"),
            "data_extrato": "15/07/2004",
            "descricao": "TESTE [CRUD]",
            "fin_conta_id": module_tests_fin.fin_conta_id1(self),
            "numero_doc": "5",
            "process_id": module_tests_sys.module_tests_sys.sys_process_log_id1(self),
            "status": "PD",
            "status_observacao": "D",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor": "5",
        }

        response = self.client.post(
            url_for("finpagrecbancoextrato.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_pagrec_banco_extrato_get(self):
        response = self.client.get(
            url_for("finpagrecbancoextrato.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fin_pagrec_banco_extrato_get_by_id(self):
        response = self.client.get(
            url_for(
                "finpagrecbancoextrato.find_by_id",
                id=self.get_id_fixed("fin_pagrec_banco_extrato_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ===================

    def fin_pagrec_banco_extrato_delete(self):
        response = self.client.delete(
            url_for(
                "finpagrecbancoextrato.delete",
                id=self.get_id_fixed("fin_pagrec_banco_extrato_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fin_pagrec_banco_transf
    # ===========================================================

    # ====================

    def fin_pagrec_banco_transf_id1(self):

        req_post = {
            "id": self.get_id_fixed("fin_pagrec_banco_transf_id1"),
            "data_mov": "15/04/2001",
            "data_valid": "15/04/2001",
            "observacao": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor": "5",
            "fin_conta_id_destino": module_tests_fin.fin_conta_id1(self),
            "fin_conta_id_origem": module_tests_fin.fin_conta_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "process_id": module_tests_sys.module_tests_sys.sys_process_log_id1(self),
        }

        response = self.client.post(
            url_for("finpagrecbancotransf.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_pagrec_banco_transf_id2(self):

        req_post = {
            "id": self.get_id_fixed("fin_pagrec_banco_transf_id2"),
            "data_mov": "15/04/2001",
            "data_valid": "15/04/2001",
            "observacao": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor": "5",
            "fin_conta_id_destino": module_tests_fin.fin_conta_id1(self),
            "fin_conta_id_origem": module_tests_fin.fin_conta_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "process_id": module_tests_sys.module_tests_sys.sys_process_log_id1(self),
        }

        response = self.client.post(
            url_for("finpagrecbancotransf.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_pagrec_banco_transf_get(self):
        response = self.client.get(
            url_for("finpagrecbancotransf.find_all"), headers=self.create_token()
        )
        result = len(response.json) > 0
        self.assertTrue(result)

    # ====================

    def fin_pagrec_banco_transf_get_by_id(self):
        response = self.client.get(
            url_for(
                "finpagrecbancotransf.find_by_id",
                id=self.get_id_fixed("fin_pagrec_banco_transf_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ===================

    def fin_pagrec_banco_transf_delete(self):
        response = self.client.delete(
            url_for(
                "finpagrecbancotransf.delete",
                id=self.get_id_fixed("fin_pagrec_banco_transf_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ====================
    # ===========================================================
    # fin_pagrec_baixa
    # ===========================================================

    # ====================

    def fin_pagrec_baixa_id1(self):
        module_tests_fin.fin_pagrec_id1(self)
        req_post = {
            "id": self.get_id_fixed("fin_pagrec_baixa_id1"),
            "data_baixa": "15/05/2022",
            "data_valid": "15/05/2022",
            "fin_conta_id": module_tests_fin.fin_conta_id1(self),
            "fin_doc_tipo_id": module_tests_fin.fin_doc_tipo_id1(self),
            "fin_lote_id": module_tests_fin.fin_lote_id1(self),
            "fin_pagrec_parc_id": self.get_id_fixed("fin_pagrec_parc_id1"),
            "numero_doc_pagrec": "S",
            "tipo": "N",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor_pagrec": "5",
            "fin_pagrec_baixa_var_childs": [
                {
                    "id": self.get_id_fixed("fin_pagrec_baixa_var_id1"),
                    "data_valid": "2022-12-29T00:00:00",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "valor": "5",
                    "observacao": "TESTE [CRUD]2",
                    "fin_tipo_variacao_id": module_tests_fin.fin_tipo_variacao_id1(
                        self
                    ),
                }
            ],
        }

        response = self.client.post(
            url_for("finpagrecbaixa.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_pagrec_baixa_id2(self):
        module_tests_fin.fin_pagrec_id1(self)
        req_post = {
            "id": self.get_id_fixed("fin_pagrec_baixa_id2"),
            "data_baixa": "15/05/2022",
            "data_valid": "15/05/2022",
            "fin_conta_id": module_tests_fin.fin_conta_id1(self),
            "fin_doc_tipo_id": module_tests_fin.fin_doc_tipo_id1(self),
            "fin_lote_id": module_tests_fin.fin_lote_id1(self),
            "fin_pagrec_parc_id": self.get_id_fixed("fin_pagrec_parc_id1"),
            "numero_doc_pagrec": "S",
            "tipo": "N",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor_pagrec": "5",
            "fin_pagrec_baixa_var_childs": [
                {
                    "data_valid": "2022-12-29T00:00:00",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "valor": "5",
                    "observacao": "TESTE [CRUD]2",
                    "fin_tipo_variacao_id": module_tests_fin.fin_tipo_variacao_id1(
                        self
                    ),
                }
            ],
        }

        response = self.client.post(
            url_for("finpagrecbaixa.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_pagrec_baixa_get(self):
        response = self.client.get(
            url_for("finpagrecbaixa.find_all"), headers=self.create_token()
        )
        result = len(response.json) > 0
        self.assertTrue(result)

    # ====================

    def fin_pagrec_baixa_get_by_id(self):
        response = self.client.get(
            url_for(
                "finpagrecbaixa.find_by_id",
                id=self.get_id_fixed("fin_pagrec_baixa_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ===================

    def fin_pagrec_baixa_delete(self):
        response = self.client.delete(
            url_for(
                "finpagrecbaixa.delete", id=self.get_id_fixed("fin_pagrec_baixa_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fin_pagrec_origem
    # ===========================================================

    # ====================

    def fin_pagrec_origem_id1(self):
        module_tests_fin.fin_pagrec_id1(self)
        req_post = {
            "id": self.get_id_fixed("fin_pagrec_origem_id1"),
            "fin_extrato_id": module_tests_fin.fin_pagrec_banco_extrato_id1(self),
            "fin_pagrec_baixa_id": module_tests_fin.fin_pagrec_baixa_id1(self),
            "fin_pagrec_banco_id": module_tests_fin.fin_pagrec_banco_id1(self),
            "fin_pagrec_id": module_tests_fin.fin_pagrec_id1(self),
            "fin_pagrec_id_origem": module_tests_fin.fin_pagrec_id1(self),
            "fin_pagrec_parc1_id_origem": module_tests_fin.fin_pagrec_id1(self),
            "fin_pagrec_parc_id": self.get_id_fixed("fin_pagrec_parc_id1"),
            "fin_recibo_id": module_tests_fin.fin_recibo_id1(self),
            "mov_id": module_tests_mov.module_tests_mov.mov_id1(self),
            "tipo": "S",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("finpagrecorigem.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_pagrec_origem_id2(self):
        module_tests_fin.fin_pagrec_id1(self)
        req_post = {
            "id": self.get_id_fixed("fin_pagrec_origem_id2"),
            "fin_extrato_id": module_tests_fin.fin_pagrec_banco_extrato_id1(self),
            "fin_pagrec_baixa_id": module_tests_fin.fin_pagrec_baixa_id1(self),
            "fin_pagrec_banco_id": module_tests_fin.fin_pagrec_banco_id1(self),
            "fin_pagrec_id": module_tests_fin.fin_pagrec_id1(self),
            "fin_pagrec_id_origem": module_tests_fin.fin_pagrec_id1(self),
            "fin_pagrec_parc1_id_origem": module_tests_fin.fin_pagrec_id1(self),
            "fin_pagrec_parc_id": self.get_id_fixed("fin_pagrec_parc_id1"),
            "fin_recibo_id": module_tests_fin.fin_recibo_id1(self),
            "mov_id": module_tests_mov.module_tests_mov.mov_id1(self),
            "tipo": "S",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("finpagrecorigem.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_pagrec_origem_get(self):

        response = self.client.get(
            url_for("finpagrecorigem.find_all"), headers=self.create_token()
        )
        result = len(response.json) > 0

        self.assertTrue(result)

    # ====================

    def fin_pagrec_origem_get_by_id(self):

        response = self.client.get(
            url_for(
                "finpagrecorigem.find_by_id",
                id=self.get_id_fixed("fin_pagrec_origem_id1"),
            ),
            headers=self.create_token(),
        )

        self.assertEqual(response.status_code, 200)

    # ===================

    def fin_pagrec_origem_delete(self):

        response = self.client.delete(
            url_for(
                "finpagrecorigem.delete", id=self.get_id_fixed("fin_pagrec_origem_id2")
            ),
            headers=self.create_token(),
        )

        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fin_pagrec_origem
    # ===========================================================

    # ====================

    def fin_pagrec_class_id1(self):

        req_post = {
            "id": self.get_id_fixed("fin_pagrec_class_id1"),
            "data_valid": "15/05/2001",
            "fator_rat": "5",
            "fin_class_id": module_tests_fin.fin_class_id1(self),
            "fin_pagrec_banco_id": module_tests_fin.fin_pagrec_banco_id1(self),
            "fin_pagrec_id": module_tests_fin.fin_pagrec_id1(self),
            "perc_rat": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor": "12",
        }

        response = self.client.post(
            url_for("finpagrecclass.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_pagrec_class_id2(self):

        req_post = {
            "id": self.get_id_fixed("fin_pagrec_class_id2"),
            "data_valid": "15/05/2001",
            "fator_rat": "5",
            "fin_class_id": module_tests_fin.fin_class_id1(self),
            "fin_pagrec_banco_id": module_tests_fin.fin_pagrec_banco_id1(self),
            "fin_pagrec_id": module_tests_fin.fin_pagrec_id1(self),
            "perc_rat": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor": "12",
        }

        response = self.client.post(
            url_for("finpagrecclass.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fin_pagrec_class_get(self):

        response = self.client.get(
            url_for("finpagrecclass.find_all"), headers=self.create_token()
        )
        result = len(response.json) > 0

        self.assertTrue(result)

    # ====================

    def fin_pagrec_class_get_by_id(self):

        response = self.client.get(
            url_for(
                "finpagrecclass.find_by_id",
                id=self.get_id_fixed("fin_pagrec_class_id1"),
            ),
            headers=self.create_token(),
        )

        self.assertEqual(response.status_code, 200)

    # ===================

    def fin_pagrec_class_delete(self):

        response = self.client.delete(
            url_for(
                "finpagrecclass.delete", id=self.get_id_fixed("fin_pagrec_class_id2")
            ),
            headers=self.create_token(),
        )

        self.assertEqual(response.status_code, 204)
