from flask import url_for


from generic_tests import generic_tests
import module_tests_fin
import module_tests_fis
import module_tests_ger
import module_tests_ope
import module_tests_sys


class module_tests_mov(generic_tests):

    # ===========================================================
    # mov_tipo
    # ===========================================================

    # ====================

    def mov_tipo_id1(self):

        req_post = {
            "id": self.get_id_fixed("mov_tipo_id1"),
            "tipo_mov": "TESTE",
            "configuracao": "TESTE [CRUD]",
            "ativo": "S",
            "nome": "TESTE [CRUD]",
            "sigla_mov_tipo": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("movtipo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_tipo_id2(self):

        req_post = {
            "id": self.get_id_fixed("mov_tipo_id2"),
            "tipo_mov": "TESTE",
            "configuracao": "TESTE [CRUD]",
            "ativo": "S",
            "nome": "TESTE [CRUD]",
            "sigla_mov_tipo": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("movtipo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_tipo_get(self):
        response = self.client.get(
            url_for("movtipo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def mov_tipo_get_by_id(self):
        response = self.client.get(
            url_for("movtipo.find_by_id", id=self.get_id_fixed("mov_tipo_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def mov_tipo_delete(self):

        response = self.client.delete(
            url_for("movtipo.delete", id=self.get_id_fixed("mov_tipo_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # mov_status
    # ===========================================================

    # ====================

    def mov_status_id1(self):

        req_post = {
            "id": self.get_id_fixed("mov_status_id1"),
            "ativo": "S",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "sigla_mov_status": "TESTE [CRUD]",
            "nome": "TESTE [CRUD]",
            "tipo_status": "F",
        }

        response = self.client.post(
            url_for("movstatus.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_status_id2(self):

        req_post = {
            "id": self.get_id_fixed("mov_status_id2"),
            "ativo": "S",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "sigla_mov_status": "TESTE [CRUD]",
            "nome": "TESTE [CRUD]",
            "tipo_status": "F",
        }

        response = self.client.post(
            url_for("movstatus.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_status_get(self):
        response = self.client.get(
            url_for("movstatus.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def mov_status_get_by_id(self):
        response = self.client.get(
            url_for("movstatus.find_by_id", id=self.get_id_fixed("mov_status_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def mov_status_delete(self):
        response = self.client.delete(
            url_for("movstatus.delete", id=self.get_id_fixed("mov_status_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # mov_unit_param
    # ===========================================================

    # ====================

    def mov_unit_param_id1(self):

        req_post = {
            "id": self.get_id_fixed("mov_unit_param_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_valid_ini": "2022-12-29T00:00:00",
        }

        response = self.client.post(
            url_for("movunitparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_unit_param_id2(self):

        req_post = {
            "id": self.get_id_fixed("mov_unit_param_id2"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_valid_ini": "2022-12-29T00:00:00",
        }

        response = self.client.post(
            url_for("movunitparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_unit_param_get(self):
        response = self.client.get(
            url_for("movunitparam.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def mov_unit_param_get_by_id(self):
        response = self.client.get(
            url_for(
                "movunitparam.find_by_id", id=self.get_id_fixed("mov_unit_param_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def mov_unit_param_delete(self):

        response = self.client.delete(
            url_for("movunitparam.delete", id=self.get_id_fixed("mov_unit_param_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # mov_operacao
    # ===========================================================

    # ====================

    def mov_operacao_id1(self):

        req_post = {
            "id": self.get_id_fixed("mov_operacao_id1"),
            "finalidade_doc": "1",
            "ger_numeracao_id": module_tests_ger.module_tests_ger.ger_numeracao_id1(
                self
            ),
            "tipo_es": "E",
            "ativo": "S",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "nome": "TESTE [CRUD]",
            "configuracao": "TESTE [CRUD]",
            "mov_tipo_id": module_tests_mov.mov_tipo_id1(self),
            "sigla_mov_operacao": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("movoperacao.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_operacao_id2(self):

        req_post = {
            "id": self.get_id_fixed("mov_operacao_id2"),
            "finalidade_doc": "1",
            "ger_numeracao_id": module_tests_ger.module_tests_ger.ger_numeracao_id1(
                self
            ),
            "tipo_es": "E",
            "ativo": "S",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "nome": "TESTE [CRUD]",
            "configuracao": "TESTE [CRUD]",
            "mov_tipo_id": module_tests_mov.mov_tipo_id1(self),
            "sigla_mov_operacao": "TESTE [CRUD]",
            "mov_operacao_status_childs": [
                {
                    "id": self.get_id_fixed("mov_operacao_status_id1"),
                    "mov_status_id_prox": module_tests_mov.mov_status_id1(self),
                    "mov_status_id": module_tests_mov.mov_status_id1(self),
                    "mov_operacao_id_prox": module_tests_mov.mov_operacao_id1(self),
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                }
            ],
        }

        response = self.client.post(
            url_for("movoperacao.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_operacao_get(self):
        response = self.client.get(
            url_for("movoperacao.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def mov_operacao_get_by_id(self):
        response = self.client.get(
            url_for("movoperacao.find_by_id", id=self.get_id_fixed("mov_operacao_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def mov_operacao_delete(self):
        response = self.client.delete(
            url_for("movoperacao.delete", id=self.get_id_fixed("mov_operacao_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # mov
    # ===========================================================

    # ====================

    def mov_id1(self):

        module_tests_ger.module_tests_ger.ger_pessoa_id1(self)

        req_post = {
            "id": self.get_id_fixed("mov_id1"),
            "tipo_umedida_carga": "01",
            "ger_cidade_id_descarreg": module_tests_ger.module_tests_ger.ger_cidade_id1(
                self
            ),
            "serie_mov": "5",
            "fis_doc_tipo_id": module_tests_fis.module_tests_fis.fis_doc_tipo_id1(self),
            "observacao_fiscal": "5",
            "ger_pessoa_endereco_id_dest": self.get_id_fixed("ger_pessoa_endereco_id1"),
            "ger_pessoa_endereco_id_expe": self.get_id_fixed("ger_pessoa_endereco_id1"),
            "qnt_carga": "5",
            "tipo_carga": "07",
            "observacao_item": "5",
            "sys_user_id_resp": module_tests_sys.module_tests_sys.sys_user_id1(self),
            "tipo_frete": "2",
            "ger_pessoa_id": module_tests_ger.module_tests_ger.ger_pessoa_id1(self),
            "cep_descarreg": "TESTE [CRUD]",
            "ger_pessoa_endereco_id_fiscal": self.get_id_fixed(
                "ger_pessoa_endereco_id1"
            ),
            "valor_item_frete_total": "5",
            "fin_cond_pagrec_id": module_tests_fin.module_tests_fin.fin_cond_pagrec_id1(
                self
            ),
            "taf": "5",
            "data_entrada_saida": "15/07/2001",
            "ger_pessoa_endereco_id_entrega": self.get_id_fixed(
                "ger_pessoa_endereco_id1"
            ),
            "data_anulacao": "15/07/2001",
            "fis_exig_iss_nfs": "1",
            "data_emissao": "15/07/2001",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "serio_mov_pre": "5",
            "fis_iss_retido_nfs": "S",
            "fis_tipo_resp_reten": "1",
            "valor_carga": "5",
            "tipo_emissao_carga": "1",
            "fis_nat_ope_nfs": "6",
            "tipo_tomador_serv_frete": "5",
            "observacao_serv": "TESTE [CRUD]",
            "ger_pessoa_endereco_id_reme": self.get_id_fixed("ger_pessoa_endereco_id1"),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "data_mov": "15/07/2001",
            "ger_pessoa_endereco_id_rece": self.get_id_fixed("ger_pessoa_endereco_id1"),
            "valor_total": "5",
            "numero_mov_pre": "5",
            "ger_cidade_id_carreg": module_tests_ger.module_tests_ger.ger_cidade_id1(
                self
            ),
            "nr_externo": "5",
            "observacao_transp": "5",
            "ger_pessoa_endereco_id_inter": self.get_id_fixed(
                "ger_pessoa_endereco_id1"
            ),
            "numero_mov": "5",
            "mov_operacao_id": module_tests_mov.mov_operacao_id1(self),
            "tipo_modal_carga": "5",
            "tipo_fretamento": "5",
            "tipo_transportador_carga": "5",
            "tipo_serv_frete": "5",
            "data_valid": "15/07/2001",
            "valor_financeiro_total": "5",
            "mov_status_id": module_tests_mov.mov_status_id1(self),
            "observacao": "TESTE [CRUD]",
            "data_entrega": "15/07/2001",
            "cep_carreg": "5",
        }

        response = self.client.post(
            url_for("mov.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_id2(self):
        module_tests_ger.module_tests_ger.ger_pessoa_id1(self)

        req_post = {
            "id": self.get_id_fixed("mov_id2"),
            "tipo_umedida_carga": "01",
            "ger_cidade_id_descarreg": module_tests_ger.module_tests_ger.ger_cidade_id1(
                self
            ),
            "serie_mov": "5",
            "fis_doc_tipo_id": module_tests_fis.module_tests_fis.fis_doc_tipo_id1(self),
            "observacao_fiscal": "5",
            "ger_pessoa_endereco_id_dest": self.get_id_fixed("ger_pessoa_endereco_id1"),
            "ger_pessoa_endereco_id_expe": self.get_id_fixed("ger_pessoa_endereco_id1"),
            "qnt_carga": "5",
            "tipo_carga": "07",
            "observacao_item": "5",
            "sys_user_id_resp": module_tests_sys.module_tests_sys.sys_user_id1(self),
            "tipo_frete": "2",
            "ger_pessoa_id": module_tests_ger.module_tests_ger.ger_pessoa_id1(self),
            "cep_descarreg": module_tests_ger.module_tests_ger.ger_pessoa_id1(self),
            "ger_pessoa_endereco_id_fiscal": self.get_id_fixed(
                "ger_pessoa_endereco_id1"
            ),
            "valor_item_frete_total": "5",
            "fin_cond_pagrec_id": module_tests_fin.module_tests_fin.fin_cond_pagrec_id1(
                self
            ),
            "taf": "5",
            "data_entrada_saida": "15/07/2001",
            "ger_pessoa_endereco_id_entrega": self.get_id_fixed(
                "ger_pessoa_endereco_id1"
            ),
            "data_anulacao": "15/07/2001",
            "fis_exig_iss_nfs": "1",
            "data_emissao": "15/07/2001",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "serio_mov_pre": "5",
            "fis_iss_retido_nfs": "S",
            "fis_tipo_resp_reten": "1",
            "valor_carga": "5",
            "tipo_emissao_carga": "1",
            "fis_nat_ope_nfs": "6",
            "tipo_tomador_serv_frete": "5",
            "observacao_serv": "TESTE [CRUD]",
            "ger_pessoa_endereco_id_reme": self.get_id_fixed("ger_pessoa_endereco_id1"),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "data_mov": "15/07/2001",
            "ger_pessoa_endereco_id_rece": self.get_id_fixed("ger_pessoa_endereco_id1"),
            "valor_total": "5",
            "numero_mov_pre": "5",
            "ger_cidade_id_carreg": module_tests_ger.module_tests_ger.ger_cidade_id1(
                self
            ),
            "nr_externo": "5",
            "observacao_transp": "5",
            "ger_pessoa_endereco_id_inter": self.get_id_fixed(
                "ger_pessoa_endereco_id1"
            ),
            "numero_mov": "5",
            "mov_operacao_id": module_tests_mov.mov_operacao_id1(self),
            "tipo_modal_carga": "5",
            "tipo_fretamento": "5",
            "tipo_transportador_carga": "5",
            "tipo_serv_frete": "5",
            "data_valid": "15/07/2001",
            "valor_financeiro_total": "5",
            "mov_status_id": module_tests_mov.mov_status_id1(self),
            "observacao": "TESTE [CRUD]",
            "data_entrega": "15/07/2001",
            "cep_carreg": "5",
        }

        response = self.client.post(
            url_for("mov.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_get(self):
        response = self.client.get(url_for("mov.find_all"), headers=self.create_token())
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def mov_get_by_id(self):
        response = self.client.get(
            url_for("mov.find_by_id", id=self.get_id_fixed("mov_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def mov_delete(self):
        response = self.client.delete(
            url_for("mov.delete", id=self.get_id_fixed("mov_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # mov_est_nivel
    # ===========================================================

    def mov_est_nivel_id1(self):

        req_post = {
            "id": self.get_id_fixed("mov_est_nivel_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "qnt_min": "5",
            "qnt_nesc": "5",
            "ger_itemserv_id": module_tests_ger.module_tests_ger.ger_itemserv_id1(self),
            "qnt_max": "200",
            "ger_est_nivel_id": module_tests_ger.module_tests_ger.ger_est_nivel_id1(
                self
            ),
            "observacao": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("movestnivel.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_est_nivel_id2(self):

        req_post = {
            "id": self.get_id_fixed("mov_est_nivel_id2"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "qnt_min": "5",
            "qnt_nesc": "5",
            "ger_itemserv_id": module_tests_ger.module_tests_ger.ger_itemserv_id1(self),
            "qnt_max": "200",
            "ger_est_nivel_id": module_tests_ger.module_tests_ger.ger_est_nivel_id1(
                self
            ),
            "observacao": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("movestnivel.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_est_nivel_get(self):
        response = self.client.get(
            url_for("movestnivel.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def mov_est_nivel_get_by_id(self):
        response = self.client.get(
            url_for(
                "movestnivel.find_by_id", id=self.get_id_fixed("mov_est_nivel_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def mov_est_nivel_delete(self):
        response = self.client.delete(
            url_for("movestnivel.delete", id=self.get_id_fixed("mov_est_nivel_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # mov_ciot
    # ===========================================================

    def mov_ciot_id1(self):

        req_post = {
            "id": self.get_id_fixed("mov_ciot_id1"),
            "nr_ciot": "5",
            "ger_pessoa_id_responsavel": module_tests_ger.module_tests_ger.ger_pessoa_id1(
                self
            ),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "mov_id": module_tests_mov.mov_id1(self),
        }

        response = self.client.post(
            url_for("movciot.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_ciot_id2(self):

        req_post = {
            "id": self.get_id_fixed("mov_ciot_id2"),
            "nr_ciot": "5",
            "ger_pessoa_id_responsavel": module_tests_ger.module_tests_ger.ger_pessoa_id1(
                self
            ),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "mov_id": module_tests_mov.mov_id1(self),
        }

        response = self.client.post(
            url_for("movciot.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_ciot_get(self):
        response = self.client.get(
            url_for("movciot.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def mov_ciot_get_by_id(self):
        response = self.client.get(
            url_for("movciot.find_by_id", id=self.get_id_fixed("mov_ciot_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def mov_ciot_delete(self):
        response = self.client.delete(
            url_for("movciot.delete", id=self.get_id_fixed("mov_ciot_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # mov_comp
    # ===========================================================

    def mov_comp_id1(self):

        req_post = {
            "id": self.get_id_fixed("mov_comp_id1"),
            "nome_comp": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "mov_id": module_tests_mov.mov_id1(self),
            "qnt_comp": "5",
        }

        response = self.client.post(
            url_for("movcomp.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_comp_id2(self):

        req_post = {
            "id": self.get_id_fixed("mov_comp_id2"),
            "nome_comp": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "mov_id": module_tests_mov.mov_id1(self),
            "qnt_comp": "5",
        }

        response = self.client.post(
            url_for("movcomp.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_comp_get(self):
        response = self.client.get(
            url_for("movcomp.find_all"), headers=self.create_token()
        )
        result = len(response.json) > 0

        self.assertTrue(result)

    # ====================

    def mov_comp_get_by_id(self):
        response = self.client.get(
            url_for("movcomp.find_by_id", id=self.get_id_fixed("mov_comp_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def mov_comp_delete(self):
        response = self.client.delete(
            url_for("movcomp.delete", id=self.get_id_fixed("mov_comp_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # mov_condutor
    # ===========================================================

    def mov_condutor_id1(self):

        req_post = {
            "id": self.get_id_fixed("mov_condutor_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "mov_id": module_tests_mov.mov_id1(self),
            "ger_pessoa_id_condutor": module_tests_ger.module_tests_ger.ger_pessoa_id1(
                self
            ),
        }

        response = self.client.post(
            url_for("movcondutor.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_condutor_id2(self):

        req_post = {
            "id": self.get_id_fixed("mov_condutor_id2"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "mov_id": module_tests_mov.mov_id1(self),
            "ger_pessoa_id_condutor": module_tests_ger.module_tests_ger.ger_pessoa_id1(
                self
            ),
        }

        response = self.client.post(
            url_for("movcondutor.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_condutor_get(self):
        response = self.client.get(
            url_for("movcondutor.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def mov_condutor_get_by_id(self):
        response = self.client.get(
            url_for("movcondutor.find_by_id", id=self.get_id_fixed("mov_condutor_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def mov_condutor_delete(self):
        response = self.client.delete(
            url_for("movcondutor.delete", id=self.get_id_fixed("mov_condutor_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # mov_entrega
    # ===========================================================

    def mov_entrega_id1(self):

        req_post = {
            "id": self.get_id_fixed("mov_entrega_id1"),
            "ger_cidade_id": module_tests_ger.module_tests_ger.ger_cidade_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "mov_id": module_tests_mov.mov_id1(self),
            "mov_entrega_doc_childs": [
                {
                    "id": self.get_id_fixed("mov_entrega_doc_id1"),
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "mov_id_interno": module_tests_mov.mov_id1(self),
                    "modelo_documento": "TS",
                    "mov_id": module_tests_mov.mov_id1(self),
                    "data_emissao": "2022-12-29T00:00:00",
                    "chave_documento": "TS",
                    "valor_total": "5",
                    "subserie_documento": "TS",
                    "serie_documento": "12",
                    "nr_documento": "5",
                }
            ],
        }

        response = self.client.post(
            url_for("moventrega.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_entrega_id2(self):

        req_post = {
            "id": self.get_id_fixed("mov_entrega_id2"),
            "ger_cidade_id": module_tests_ger.module_tests_ger.ger_cidade_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "mov_id": module_tests_mov.mov_id1(self),
            "mov_entrega_doc_childs": [
                {
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "mov_id_interno": module_tests_mov.mov_id1(self),
                    "modelo_documento": "TS",
                    "mov_id": module_tests_mov.mov_id1(self),
                    "data_emissao": "2022-12-29T00:00:00",
                    "chave_documento": "TS",
                    "valor_total": "5",
                    "subserie_documento": "TS",
                    "serie_documento": "12",
                    "nr_documento": "5",
                }
            ],
        }

        response = self.client.post(
            url_for("moventrega.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_entrega_get(self):
        response = self.client.get(
            url_for("moventrega.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def mov_entrega_get_by_id(self):
        response = self.client.get(
            url_for("moventrega.find_by_id", id=self.get_id_fixed("mov_entrega_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def mov_entrega_delete(self):
        response = self.client.delete(
            url_for("moventrega.delete", id=self.get_id_fixed("mov_entrega_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # mov_cotacao
    # ===========================================================

    def mov_cotacao_id1(self):
        module_tests_ger.module_tests_ger.ger_pessoa_id1(self)
        req_post = {
            "id": self.get_id_fixed("mov_cotacao_id1"),
            "fin_cond_pagrec_id": module_tests_fin.module_tests_fin.fin_cond_pagrec_id1(
                self
            ),
            "ger_itemserv_id": module_tests_ger.module_tests_ger.ger_itemserv_id1(self),
            "valor_total_cot": "5",
            "qnt_cot": "5",
            "mov_id": module_tests_mov.mov_id1(self),
            "valor_frete_cot": "5",
            "valor_total_trib_cot": "5",
            "sys_user_id_aprov": module_tests_sys.module_tests_sys.sys_user_id1(self),
            "ger_pessoa_endereco_id": self.get_id_fixed("ger_pessoa_endereco_id1"),
            "observacao1": "TESTE [CRUD]",
            "ger_pessoa_id": module_tests_ger.module_tests_ger.ger_pessoa_id1(self),
            "valor_unit_cot": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor_desc_cot": "5",
            "status": "A",
            "valor_outro_cot": "5",
            "data_status": "15/07/2009",
            "observacao2": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("movcotacao.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_cotacao_id2(self):
        module_tests_ger.module_tests_ger.ger_pessoa_id1(self)
        req_post = {
            "id": self.get_id_fixed("mov_cotacao_id2"),
            "fin_cond_pagrec_id": module_tests_fin.module_tests_fin.fin_cond_pagrec_id1(
                self
            ),
            "ger_itemserv_id": module_tests_ger.module_tests_ger.ger_itemserv_id1(self),
            "valor_total_cot": "5",
            "qnt_cot": "5",
            "mov_id": module_tests_mov.mov_id1(self),
            "valor_frete_cot": "5",
            "valor_total_trib_cot": "5",
            "sys_user_id_aprov": module_tests_sys.module_tests_sys.sys_user_id1(self),
            "ger_pessoa_endereco_id": self.get_id_fixed("ger_pessoa_endereco_id1"),
            "observacao1": "TESTE [CRUD]",
            "ger_pessoa_id": module_tests_ger.module_tests_ger.ger_pessoa_id1(self),
            "valor_unit_cot": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor_desc_cot": "5",
            "status": "A",
            "valor_outro_cot": "5",
            "data_status": "15/07/2009",
            "observacao2": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("movcotacao.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_cotacao_get(self):
        response = self.client.get(
            url_for("movcotacao.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def mov_cotacao_get_by_id(self):
        response = self.client.get(
            url_for("movcotacao.find_by_id", id=self.get_id_fixed("mov_cotacao_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def mov_cotacao_delete(self):
        response = self.client.delete(
            url_for("movcotacao.delete", id=self.get_id_fixed("mov_cotacao_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # mov_itemserv
    # ===========================================================

    def mov_itemserv_id1(self):
        module_tests_ger.module_tests_ger.ger_itemserv_id1(self)
        req_post = {
            "id": self.get_id_fixed("mov_itemserv_id1"),
            "qnt_orig": "5",
            "valor_outros": "5",
            "nome_itemserv": "tsy",
            "fis_cfop_id": module_tests_fis.module_tests_fis.fis_cfop_id1(self),
            "valor_unit_orig": "5",
            "ger_itemserv_lote_id": self.get_id_fixed("ger_itemserv_lote_id1"),
            "valor_acrecimo": "5",
            "valor_desconto_cond": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "fis_obra_cei": "TESTE [CRUD]",
            "qnt_largura": "5",
            "valor_outros_tributo_ret": "5",
            "valor_liquido": "5",
            "valor_unit_conv": "5",
            "qnt_min_pessoa_cot": "5",
            "fis_numero_proc_susp_nfs": "5",
            "mov_id": module_tests_mov.mov_id1(self),
            "data_valid": "15/07/2001",
            "qnt_altura": "5",
            "qnt_comprimento": "5",
            "qnt_devolvida": "5",
            "valor_frete": "5",
            "ger_itemserv_id": module_tests_ger.module_tests_ger.ger_itemserv_id1(self),
            "valor_desconto": "5",
            "fis_doc_cnae_nfs": "TESTE [CRUD]",
            "qnt_conv": "5",
            "valor_tributo_retido": "5",
            "valor_bruto": "5",
            "ger_itemserv_var_id": module_tests_ger.module_tests_ger.ger_itemserv_var_id1(
                self
            ),
            "valor_tributo_total": "5",
            "valor_seguro": "5",
            "valor_deducao": "5",
            "observacao": "TESTE [CRUD]",
            "ger_umedida_id_conv": module_tests_ger.module_tests_ger.ger_umedida_id1(
                self
            ),
            "valor_desconto_incond": "5",
            "fis_obra_art": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("movitemserv.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_itemserv_id2(self):
        module_tests_ger.module_tests_ger.ger_itemserv_id1(self)
        req_post = {
            "id": self.get_id_fixed("mov_itemserv_id2"),
            "qnt_orig": "5",
            "valor_outros": "5",
            "nome_itemserv": "tsy",
            "fis_cfop_id": module_tests_fis.module_tests_fis.fis_cfop_id1(self),
            "valor_unit_orig": "5",
            "ger_itemserv_lote_id": self.get_id_fixed("ger_itemserv_lote_id1"),
            "valor_acrecimo": "5",
            "valor_desconto_cond": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "fis_obra_cei": "TESTE [CRUD]",
            "qnt_largura": "5",
            "valor_outros_tributo_ret": "5",
            "valor_liquido": "5",
            "valor_unit_conv": "5",
            "qnt_min_pessoa_cot": "5",
            "fis_numero_proc_susp_nfs": "5",
            "mov_id": module_tests_mov.mov_id1(self),
            "data_valid": "15/07/2001",
            "qnt_altura": "5",
            "qnt_comprimento": "5",
            "qnt_devolvida": "5",
            "valor_frete": "5",
            "ger_itemserv_id": module_tests_ger.module_tests_ger.ger_itemserv_id1(self),
            "valor_desconto": "5",
            "fis_doc_cnae_nfs": "TESTE [CRUD]",
            "qnt_conv": "5",
            "valor_tributo_retido": "5",
            "valor_bruto": "5",
            "ger_itemserv_var_id": module_tests_ger.module_tests_ger.ger_itemserv_var_id1(
                self
            ),
            "valor_tributo_total": "5",
            "valor_seguro": "5",
            "valor_deducao": "5",
            "observacao": "TESTE [CRUD]",
            "ger_umedida_id_conv": module_tests_ger.module_tests_ger.ger_umedida_id1(
                self
            ),
            "valor_desconto_incond": "5",
            "fis_obra_art": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("movitemserv.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_itemserv_get(self):
        response = self.client.get(
            url_for("movitemserv.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def mov_itemserv_get_by_id(self):
        response = self.client.get(
            url_for("movitemserv.find_by_id", id=self.get_id_fixed("mov_itemserv_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def mov_itemserv_delete(self):
        response = self.client.delete(
            url_for("movitemserv.delete", id=self.get_id_fixed("mov_itemserv_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # mov_lacre
    # ===========================================================

    def mov_lacre_id1(self):

        req_post = {
            "id": self.get_id_fixed("mov_lacre_id1"),
            "mov_id": module_tests_mov.mov_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "lacres": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("movlacre.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_lacre_id2(self):

        req_post = {
            "id": self.get_id_fixed("mov_lacre_id2"),
            "mov_id": module_tests_mov.mov_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "lacres": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("movlacre.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_lacre_get(self):
        response = self.client.get(
            url_for("movlacre.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def mov_lacre_get_by_id(self):
        response = self.client.get(
            url_for("movlacre.find_by_id", id=self.get_id_fixed("mov_lacre_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def mov_lacre_delete(self):
        response = self.client.delete(
            url_for("movlacre.delete", id=self.get_id_fixed("mov_lacre_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # mov_medida
    # ===========================================================

    def mov_medida_id1(self):

        req_post = {
            "id": self.get_id_fixed("mov_medida_id1"),
            "ger_umedida_id": module_tests_ger.module_tests_ger.ger_umedida_id1(self),
            "marca": "5",
            "tipo_medida": "5",
            "mov_id": module_tests_mov.mov_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "nr_volume": "5",
            "peso_liquido": "5",
            "qnt_medida": "5",
            "peso_bruto": "5",
        }

        response = self.client.post(
            url_for("movmedida.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_medida_id2(self):

        req_post = {
            "id": self.get_id_fixed("mov_medida_id2"),
            "ger_umedida_id": module_tests_ger.module_tests_ger.ger_umedida_id1(self),
            "marca": "5",
            "tipo_medida": "5",
            "mov_id": module_tests_mov.mov_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "nr_volume": "5",
            "peso_liquido": "5",
            "qnt_medida": "5",
            "peso_bruto": "5",
        }

        response = self.client.post(
            url_for("movmedida.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_medida_get(self):

        response = self.client.get(
            url_for("movmedida.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def mov_medida_get_by_id(self):
        response = self.client.get(
            url_for("movmedida.find_by_id", id=self.get_id_fixed("mov_medida_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def mov_medida_delete(self):
        response = self.client.delete(
            url_for("movmedida.delete", id=self.get_id_fixed("mov_medida_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # mov_pedagio
    # ===========================================================

    def mov_pedagio_id1(self):

        req_post = {
            "id": self.get_id_fixed("mov_pedagio_id1"),
            "ger_pessoa_id_emp_pedagio": module_tests_ger.module_tests_ger.ger_pessoa_id1(
                self
            ),
            "nr_comprovante": "5",
            "ger_pessoa_id_responsavel": module_tests_ger.module_tests_ger.ger_pessoa_id1(
                self
            ),
            "mov_id": module_tests_mov.mov_id1(self),
            "valor_pedagio": "50",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("movpedagio.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_pedagio_id2(self):

        req_post = {
            "id": self.get_id_fixed("mov_pedagio_id2"),
            "ger_pessoa_id_emp_pedagio": module_tests_ger.module_tests_ger.ger_pessoa_id1(
                self
            ),
            "nr_comprovante": "5",
            "ger_pessoa_id_responsavel": module_tests_ger.module_tests_ger.ger_pessoa_id1(
                self
            ),
            "mov_id": module_tests_mov.mov_id1(self),
            "valor_pedagio": "50",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("movpedagio.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_pedagio_get(self):
        response = self.client.get(
            url_for("movpedagio.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def mov_pedagio_get_by_id(self):
        response = self.client.get(
            url_for("movpedagio.find_by_id", id=self.get_id_fixed("mov_pedagio_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def mov_pedagio_delete(self):
        response = self.client.delete(
            url_for("movpedagio.delete", id=self.get_id_fixed("mov_pedagio_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # mov_percurso
    # ===========================================================

    def mov_percurso_id1(self):

        req_post = {
            "id": self.get_id_fixed("mov_percurso_id1"),
            "ger_cidade_id": module_tests_ger.module_tests_ger.ger_cidade_id1(self),
            "mov_id": module_tests_mov.mov_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("movpercurso.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_percurso_id2(self):

        req_post = {
            "id": self.get_id_fixed("mov_percurso_id2"),
            "ger_cidade_id": module_tests_ger.module_tests_ger.ger_cidade_id1(self),
            "mov_id": module_tests_mov.mov_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("movpercurso.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_percurso_get(self):
        response = self.client.get(
            url_for("movpercurso.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def mov_percurso_get_by_id(self):
        response = self.client.get(
            url_for("movpercurso.find_by_id", id=self.get_id_fixed("mov_percurso_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def mov_percurso_delete(self):
        response = self.client.delete(
            url_for("movpercurso.delete", id=self.get_id_fixed("mov_percurso_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # mov_seguradora
    # ===========================================================

    def mov_seguradora_id1(self):

        req_post = {
            "id": self.get_id_fixed("mov_seguradora_id1"),
            "valor": "5",
            "nr_averbacao": "5",
            "tipo_responsavel": "5",
            "ger_pessoa_id_seguradora": module_tests_ger.module_tests_ger.ger_pessoa_id1(
                self
            ),
            "ger_pessoa_id_responsavel": module_tests_ger.module_tests_ger.ger_pessoa_id1(
                self
            ),
            "mov_id": module_tests_mov.mov_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "nr_apolice": "5",
        }

        response = self.client.post(
            url_for("movseguradora.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_seguradora_id2(self):

        req_post = {
            "id": self.get_id_fixed("mov_seguradora_id2"),
            "valor": "5",
            "nr_averbacao": "5",
            "tipo_responsavel": "5",
            "ger_pessoa_id_seguradora": module_tests_ger.module_tests_ger.ger_pessoa_id1(
                self
            ),
            "ger_pessoa_id_responsavel": module_tests_ger.module_tests_ger.ger_pessoa_id1(
                self
            ),
            "mov_id": module_tests_mov.mov_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "nr_apolice": "5",
        }

        response = self.client.post(
            url_for("movseguradora.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_seguradora_get(self):
        response = self.client.get(
            url_for("movseguradora.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def mov_seguradora_get_by_id(self):
        response = self.client.get(
            url_for(
                "movseguradora.find_by_id", id=self.get_id_fixed("mov_seguradora_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def mov_seguradora_delete(self):
        response = self.client.delete(
            url_for("movseguradora.delete", id=self.get_id_fixed("mov_seguradora_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # mov_tomador
    # ===========================================================

    def mov_tomador_id1(self):

        req_post = {
            "id": self.get_id_fixed("mov_tomador_id1"),
            "ger_pessoa_id_responsavel": module_tests_ger.module_tests_ger.ger_pessoa_id1(
                self
            ),
            "mov_id": module_tests_mov.mov_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("movtomador.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_tomador_id2(self):

        req_post = {
            "id": self.get_id_fixed("mov_tomador_id2"),
            "ger_pessoa_id_responsavel": module_tests_ger.module_tests_ger.ger_pessoa_id1(
                self
            ),
            "mov_id": module_tests_mov.mov_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("movtomador.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_tomador_get(self):
        response = self.client.get(
            url_for("movtomador.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def mov_tomador_get_by_id(self):
        response = self.client.get(
            url_for("movtomador.find_by_id", id=self.get_id_fixed("mov_tomador_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def mov_tomador_delete(self):
        response = self.client.delete(
            url_for("movtomador.delete", id=self.get_id_fixed("mov_tomador_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # mov_frete
    # ===========================================================

    def mov_frete_id1(self):
        module_tests_ger.module_tests_ger.ger_pessoa_id1(self)
        req_post = {
            "id": self.get_id_fixed("mov_frete_id1"),
            "valor_base_calc": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "perc_aliquota": "5",
            "valor_frete": "5",
            "valor_imposto": "5",
            "ger_pessoa_endereco_id_condutor": self.get_id_fixed(
                "ger_pessoa_endereco_id1"
            ),
            "ger_pessoa_endereco_id_transp": self.get_id_fixed(
                "ger_pessoa_endereco_id1"
            ),
            "valor_pis": "5",
            "mov_id": module_tests_mov.mov_id1(self),
            "ope_centro2_id_equip": module_tests_ope.module_tests_ope.ope_centro2_equip_id1(
                self
            ),
            "valor_cofins": "5",
            "adic_frete_base_cal_icms": "5",
        }

        response = self.client.post(
            url_for("movfrete.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_frete_id2(self):
        module_tests_ger.module_tests_ger.ger_pessoa_id1(self)
        req_post = {
            "id": self.get_id_fixed("mov_frete_id2"),
            "valor_base_calc": "5",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "perc_aliquota": "5",
            "valor_frete": "5",
            "valor_imposto": "5",
            "ger_pessoa_endereco_id_condutor": self.get_id_fixed(
                "ger_pessoa_endereco_id1"
            ),
            "ger_pessoa_endereco_id_transp": self.get_id_fixed(
                "ger_pessoa_endereco_id1"
            ),
            "valor_pis": "5",
            "mov_id": module_tests_mov.mov_id1(self),
            "ope_centro2_id_equip": module_tests_ope.module_tests_ope.ope_centro2_equip_id1(
                self
            ),
            "valor_cofins": "5",
            "adic_frete_base_cal_icms": "5",
        }

        response = self.client.post(
            url_for("movfrete.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_frete_get(self):
        response = self.client.get(
            url_for("movfrete.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def mov_frete_get_by_id(self):
        response = self.client.get(
            url_for("movfrete.find_by_id", id=self.get_id_fixed("mov_frete_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def mov_frete_delete(self):
        response = self.client.delete(
            url_for("movfrete.delete", id=self.get_id_fixed("mov_frete_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #    mov_origem
    # ===========================================================

    def mov_origem_id1(self):

        req_post = {
            "id": self.get_id_fixed("mov_origem_id1"),
            "mov_itemserv_id_origem": module_tests_mov.mov_itemserv_id1(self),
            "mov_id": module_tests_mov.mov_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "tipo": "TESTE [CRUD]",
            "mov_itemserv_id": module_tests_mov.mov_itemserv_id1(self),
            "mov_id_origem": module_tests_mov.mov_id1(self),
        }

        response = self.client.post(
            url_for("movorigem.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_origem_id2(self):

        req_post = {
            "id": self.get_id_fixed("mov_origem_id2"),
            "mov_itemserv_id_origem": module_tests_mov.mov_itemserv_id1(self),
            "mov_id": module_tests_mov.mov_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "tipo": "TESTE [CRUD]",
            "mov_itemserv_id": module_tests_mov.mov_itemserv_id1(self),
            "mov_id_origem": module_tests_mov.mov_id1(self),
        }

        response = self.client.post(
            url_for("movorigem.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_origem_get(self):
        response = self.client.get(
            url_for("movorigem.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def mov_origem_get_by_id(self):
        response = self.client.get(
            url_for("movorigem.find_by_id", id=self.get_id_fixed("mov_origem_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def mov_origem_delete(self):
        response = self.client.delete(
            url_for("movorigem.delete", id=self.get_id_fixed("mov_origem_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  mov_reboque
    # ===========================================================

    def mov_reboque_id1(self):

        req_post = {
            "id": self.get_id_fixed("mov_reboque_id1"),
            "ope_centro2_id_equip": module_tests_ope.module_tests_ope.ope_centro2_equip_id1(
                self
            ),
            "mov_id": module_tests_mov.mov_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("movreboque.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_reboque_id2(self):

        req_post = {
            "id": self.get_id_fixed("mov_reboque_id2"),
            "ope_centro2_id_equip": module_tests_ope.module_tests_ope.ope_centro2_equip_id1(
                self
            ),
            "mov_id": module_tests_mov.mov_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("movreboque.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def mov_reboque_get(self):
        response = self.client.get(
            url_for("movreboque.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def mov_reboque_get_by_id(self):
        response = self.client.get(
            url_for("movreboque.find_by_id", id=self.get_id_fixed("mov_reboque_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def mov_reboque_delete(self):
        response = self.client.delete(
            url_for("movreboque.delete", id=self.get_id_fixed("mov_reboque_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)
