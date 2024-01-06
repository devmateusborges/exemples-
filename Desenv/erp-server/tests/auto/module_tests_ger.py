from flask import url_for
from generic_tests import generic_tests
import module_tests_fis
import module_tests_ctb
import module_tests_fin
import module_tests_sys
import module_tests_ope


class module_tests_ger(generic_tests):

    # ===========================================================
    # ger_device
    # ===========================================================

    # ====================

    def ger_device_id1(self):

        req_post = {
            "id": self.get_id_fixed("ger_device_id1"),
            "sigla_device": "t",
            "nome": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ger_device_param_childs": [
                {
                    "id": self.get_id_fixed("ger_device_param_id1"),
                    "sigla_param": "TESTE [CRUD]1",
                    "observacao": "TESTE [CRUD]1",
                    "valor_dt": "29/12/2003",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "valor_nm": "5",
                    "valor_tx": "5",
                }
            ],
        }

        response = self.client.post(
            url_for("gerdevice.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_device_id2(self):

        req_post = {
            "id": self.get_id_fixed("ger_device_id2"),
            "sigla_device": "t",
            "nome": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ger_device_param_childs": [
                {
                    "sigla_param": "TESTE [CRUD]1",
                    "observacao": "TESTE [CRUD]1",
                    "valor_dt": "29/12/2003",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "valor_nm": "5",
                    "valor_tx": "5",
                }
            ],
        }

        response = self.client.post(
            url_for("gerdevice.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_device_get(self):
        response = self.client.get(
            url_for("gerdevice.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ger_device_get_by_id(self):
        response = self.client.get(
            url_for("gerdevice.find_by_id", id=self.get_id_fixed("ger_device_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ger_device_delete(self):
        response = self.client.delete(
            url_for("gerdevice.delete", id=self.get_id_fixed("ger_device_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ger_index_mov
    # ===========================================================

    # ====================

    def ger_index_mov_id1(self):

        req_post = {
            "id": self.get_id_fixed("ger_index_mov_id1"),
            "data_mov": "12/05/2022",
            "ger_index_id": module_tests_ger.ger_index_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor1": "12",
            "valor2": "1",
        }

        response = self.client.post(
            url_for("gerindexmov.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_index_mov_id2(self):

        req_post = {
            "id": self.get_id_fixed("ger_index_mov_id2"),
            "data_mov": "12/05/2022",
            "ger_index_id": module_tests_ger.ger_index_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "valor1": "12",
            "valor2": "1",
        }

        response = self.client.post(
            url_for("gerindexmov.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_index_mov_get(self):
        response = self.client.get(
            url_for("gerindexmov.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ger_index_mov_get_by_id(self):
        response = self.client.get(
            url_for(
                "gerindexmov.find_by_id", id=self.get_id_fixed("ger_index_mov_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ger_index_mov_delete(self):
        response = self.client.delete(
            url_for("gerindexmov.delete", id=self.get_id_fixed("ger_index_mov_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ger_itemserv_var
    # ===========================================================

    # ====================

    def ger_itemserv_var_id1(self):

        req_post = {
            "id": self.get_id_fixed("ger_itemserv_var_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_itemserv_var": "s",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ope_ciclo_var_id": module_tests_ope.module_tests_ope.ope_ciclo_var_id1(
                self
            ),
        }

        response = self.client.post(
            url_for("geritemservvar.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_itemserv_var_id2(self):

        req_post = {
            "id": self.get_id_fixed("ger_itemserv_var_id2"),
            "nome": "TESTE [CRUD]",
            "sigla_itemserv_var": "s",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ope_ciclo_var_id": module_tests_ope.module_tests_ope.ope_ciclo_var_id1(
                self
            ),
        }

        response = self.client.post(
            url_for("geritemservvar.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_itemserv_var_get(self):
        response = self.client.get(
            url_for("geritemservvar.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ger_itemserv_var_get_by_id(self):
        response = self.client.get(
            url_for(
                "geritemservvar.find_by_id",
                id=self.get_id_fixed("ger_itemserv_var_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ger_itemserv_var_delete(self):
        response = self.client.delete(
            url_for(
                "geritemservvar.delete", id=self.get_id_fixed("ger_itemserv_var_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ger_empresa
    # ===========================================================

    # ====================

    def ger_empresa_id1(self):

        req_post = {
            "id": self.get_id_fixed("ger_empresa_id1"),
            "contato_1": "TESTE [CRUD]",
            "contato_2": "TESTE [CRUD]",
            "contato_3": "TESTE [CRUD]",
            "data_abertura": "12/05/2021",
            "data_validade_a1": "12/05/2022",
            "data_validade_a3": "12/05/2022",
            "doc_cnae": "TESTE [CRUD]",
            "doc_cnpj": "TESTE [CRUD]",
            "doc_cpf": "TESTE [CRUD]",
            "doc_ie": "TESTE [CRUD]",
            "doc_im": "TESTE [CRUD]",
            "doc_junta": "TESTE [CRUD]",
            "doc_rntrc": "TESTE [CRUD]",
            "email_1": "TESTE [CRUD]",
            "end_bairro": "TESTE [CRUD]",
            "end_cep": "TESTE [CRUD]",
            "end_complemento": "TESTE [CRUD]",
            "end_ger_cidade_id": module_tests_ger.ger_cidade_id1(self),
            "end_logradouro": "TESTE",
            "end_logradouro_nr": "TESTE",
            "fis_dfe_ambiente": "t",
            "fis_dfe_api_token": "sts",
            "fis_incent_cultura": "S",
            "fis_incent_fiscal_nfs": "S",
            "fis_provedor_nfs": "1",
            "fis_regime": "1",
            "fis_regime_trib_nfs": "5",
            "fone_1": "TESTE [CRUD]",
            "fone_2": "TESTE [CRUD]",
            "fone_3": "sts",
            "ger_empresa_grupo_id": module_tests_ger.ger_empresa_grupo_id1(self),
            "ger_per_tipo_id": module_tests_ger.ger_per_tipo_id1(self),
            "nome": "TESTE [CRUD] - SERVER",
            "razao_social": "TESTE",
            "sigla_empresa": "TESTE",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "S",
            "fis_certificado_id": module_tests_fis.module_tests_fis.fis_certificado_id1(
                self
            ),
            "ger_empresa_pessoa_childs": [
                {
                    "id": self.get_id_fixed("ger_empresa_pessoa_id1"),
                    "tipo": "1",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "ger_pessoa_id": module_tests_ger.ger_pessoa_id1(self),
                    "observacao": "TESTE [CRUD]",
                }
            ],
        }

        response = self.client.post(
            url_for("gerempresa.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_empresa_id2(self):

        req_post = {
            "id": self.get_id_fixed("ger_empresa_id2"),
            "contato_1": "TESTE [CRUD]",
            "contato_2": "TESTE [CRUD]",
            "contato_3": "TESTE [CRUD]",
            "data_abertura": "12/05/2021",
            "data_validade_a1": "12/05/2022",
            "data_validade_a3": "12/05/2022",
            "doc_cnae": "TESTE [CRUD]",
            "doc_cnpj": "TESTE [CRUD]",
            "doc_cpf": "TESTE [CRUD]",
            "doc_ie": "TESTE [CRUD]",
            "doc_im": "TESTE [CRUD]",
            "doc_junta": "TESTE [CRUD]",
            "doc_rntrc": "TESTE [CRUD]",
            "email_1": "TESTE [CRUD]",
            "end_bairro": "TESTE [CRUD]",
            "end_cep": "TESTE [CRUD]",
            "end_complemento": "TESTE [CRUD]",
            "end_ger_cidade_id": module_tests_ger.ger_cidade_id1(self),
            "end_logradouro": "TESTE",
            "end_logradouro_nr": "TESTE",
            "fis_dfe_ambiente": "t",
            "fis_dfe_api_token": "sts",
            "fis_incent_cultura": "S",
            "fis_incent_fiscal_nfs": "S",
            "fis_provedor_nfs": "1",
            "fis_regime": "1",
            "fis_regime_trib_nfs": "5",
            "fone_1": "TESTE [CRUD]",
            "fone_2": "TESTE [CRUD]",
            "fone_3": "sts",
            "ger_empresa_grupo_id": module_tests_ger.ger_empresa_grupo_id1(self),
            "ger_per_tipo_id": module_tests_ger.ger_per_tipo_id1(self),
            "nome": "TESTE [CRUD] - SERVER",
            "razao_social": "TESTE",
            "sigla_empresa": "TESTE",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "S",
            "fis_certificado_id": module_tests_fis.module_tests_fis.fis_certificado_id1(
                self
            ),
            "ger_empresa_pessoa_childs": [
                {
                    "tipo": "1",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "ger_pessoa_id": module_tests_ger.ger_pessoa_id1(self),
                    "observacao": "TESTE [CRUD]1",
                }
            ],
        }

        response = self.client.post(
            url_for("gerempresa.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_empresa_get(self):
        response = self.client.get(
            url_for("gerempresa.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ger_empresa_get_by_id(self):
        response = self.client.get(
            url_for("gerempresa.find_by_id", id=self.get_id_fixed("ger_empresa_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ger_empresa_delete(self):
        response = self.client.delete(
            url_for("gerempresa.delete", id=self.get_id_fixed("ger_empresa_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ger_itemserv
    # ===========================================================

    # ====================

    def ger_itemserv_id1(self):
        module_tests_ger.ger_itemserv_grupo_id1(self)
        req_post = {
            "id": self.get_id_fixed("ger_itemserv_id1"),
            "ativo": "S",
            "fis_doc_cnae_nfs": "TESTE [CRUD]",
            "fis_sigla_servico": "TESTE [CRUD]",
            "fis_sigla_servico_municipio": "TESTE [CRUD]",
            "ger_itemserv_subgrupo_id": self.get_id_fixed("ger_itemserv_subgrupo_id1"),
            "ger_umedida_id": module_tests_ger.ger_umedida_id1(self),
            "nome": "TESTE [CRUD]",
            "nome_alternativo": "TESTE [CRUD]",
            "origem_fiscal": "1",
            "referencia1": "st",
            "referencia2": "st",
            "referencia3": "st",
            "sigla_itemserv": "st",
            "tipo": "S",
            "tipo_composicao": "K",
            "tipo_ctb_comp": "C",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ctb_comp_id": module_tests_ctb.module_tests_ctb.ctb_comp_id1(self),
            "fis_nbs_id": module_tests_fis.module_tests_fis.fis_nbs_id1(self),
            "fis_cest_id": module_tests_fis.module_tests_fis.fis_cest_id1(self),
            "fis_ncm_id": module_tests_fis.module_tests_fis.fis_ncm_id1(self),
            "ger_itemserv_barra_childs": [
                {
                    "id": self.get_id_fixed("ger_itemserv_barra_id1"),
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "codigo_barra": "TESTE [CRUD]1",
                }
            ],
            "ger_itemserv_pessoa_childs": [
                {
                    "id": self.get_id_fixed("ger_itemserv_pessoa_id1"),
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "ativo": "S",
                    "cod_itemserv_ext": "TESTE [CRUD]1",
                    "ger_pessoa_id": module_tests_ger.ger_pessoa_id1(self),
                }
            ],
            "ger_itemserv_local_childs": [
                {
                    "id": self.get_id_fixed("ger_itemserv_local_id1"),
                    "desc_local3": "TESTE [CRUD]1",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "desc_local1": "TESTE [CRUD]1",
                    "observacao": "TESTE [CRUD]1",
                    "desc_local2": "TESTE [CRUD]1",
                    "ativo": "S",
                }
            ],
            "ger_itemserv_lote_childs": [
                {
                    "id": self.get_id_fixed("ger_itemserv_lote_id1"),
                    "observacao": "TESTE [CRUD]1",
                    "data_validade": "29/12/2003",
                    "sigla_ger_itemserv_lote": "TESTE [CRUD]1",
                    "data_ini": "29/12/2003",
                    "data_fin": "29/12/2003",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                }
            ],
        }

        response = self.client.post(
            url_for("geritemserv.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_itemserv_id2(self):
        module_tests_ger.ger_itemserv_grupo_id1(self)
        req_post = {
            "id": self.get_id_fixed("ger_itemserv_id2"),
            "ativo": "S",
            "fis_doc_cnae_nfs": "TESTE [CRUD]",
            "fis_sigla_servico": "TESTE [CRUD]",
            "fis_sigla_servico_municipio": "TESTE [CRUD]",
            "ger_itemserv_subgrupo_id": self.get_id_fixed("ger_itemserv_subgrupo_id1"),
            "ger_umedida_id": module_tests_ger.ger_umedida_id1(self),
            "nome": "TESTE [CRUD]",
            "nome_alternativo": "TESTE [CRUD]",
            "origem_fiscal": "1",
            "referencia1": "st",
            "referencia2": "st",
            "referencia3": "st",
            "sigla_itemserv": "st",
            "tipo": "S",
            "tipo_composicao": "K",
            "tipo_ctb_comp": "C",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ctb_comp_id": module_tests_ctb.module_tests_ctb.ctb_comp_id1(self),
            "fis_nbs_id": module_tests_fis.module_tests_fis.fis_nbs_id1(self),
            "fis_cest_id": module_tests_fis.module_tests_fis.fis_cest_id1(self),
            "fis_ncm_id": module_tests_fis.module_tests_fis.fis_ncm_id1(self),
            "ger_itemserv_barra_childs": [
                {
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "codigo_barra": "TESTE [CRUD]1",
                }
            ],
            "ger_itemserv_pessoa_childs": [
                {
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "ativo": "S",
                    "cod_itemserv_ext": "TESTE [CRUD]1",
                    "ger_pessoa_id": module_tests_ger.ger_pessoa_id1(self),
                }
            ],
            "ger_itemserv_local_childs": [
                {
                    "desc_local3": "TESTE [CRUD]1",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "desc_local1": "TESTE [CRUD]1",
                    "observacao": "TESTE [CRUD]1",
                    "desc_local2": "TESTE [CRUD]1",
                    "ativo": "S",
                }
            ],
            "ger_itemserv_lote_childs": [
                {
                    "observacao": "TESTE [CRUD]1",
                    "data_validade": "29/12/2003",
                    "sigla_ger_itemserv_lote": "TESTE [CRUD]1",
                    "data_ini": "29/12/2003",
                    "data_fin": "29/12/2003",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                }
            ],
        }

        response = self.client.post(
            url_for("geritemserv.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_itemserv_get(self):
        response = self.client.get(
            url_for("geritemserv.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ger_itemserv_get_by_id(self):

        response = self.client.get(
            url_for("geritemserv.find_by_id", id=self.get_id_fixed("ger_itemserv_id1")),
            headers=self.create_token(),
        )

        self.assertEqual(response.status_code, 200)

    # ====================

    def ger_itemserv_delete(self):
        response = self.client.delete(
            url_for("geritemserv.delete", id=self.get_id_fixed("ger_itemserv_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ger_itemserv_grupo
    # ===========================================================

    # ====================

    def ger_itemserv_grupo_id1(self):

        req_post = {
            "id": self.get_id_fixed("ger_itemserv_grupo_id1"),
            "nome": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "sigla_ger_itemserv_grupo": "TESTE [CRUD]",
            "ger_itemserv_subgrupo_childs": [
                {
                    "id": self.get_id_fixed("ger_itemserv_subgrupo_id1"),
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "nome": "TESTE [CRUD]1",
                    "ctb_comp_id": module_tests_ctb.module_tests_ctb.ctb_comp_id1(self),
                    "sigla_ger_itemserv_subgrupo": "TESTE [CRUD]1",
                }
            ],
        }

        response = self.client.post(
            url_for("geritemservgrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_itemserv_grupo_id2(self):

        req_post = {
            "id": self.get_id_fixed("ger_itemserv_grupo_id2"),
            "nome": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "sigla_ger_itemserv_grupo": "TESTE [CRUD]",
            "ger_itemserv_subgrupo_childs": [
                {
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "nome": "TESTE [CRUD]1",
                    "ctb_comp_id": module_tests_ctb.module_tests_ctb.ctb_comp_id1(self),
                    "sigla_ger_itemserv_subgrupo": "TESTE [CRUD]1",
                }
            ],
        }

        response = self.client.post(
            url_for("geritemservgrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_itemserv_grupo_get(self):
        response = self.client.get(
            url_for("geritemservgrupo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ger_itemserv_grupo_get_by_id(self):
        response = self.client.get(
            url_for(
                "geritemservgrupo.find_by_id",
                id=self.get_id_fixed("ger_itemserv_grupo_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ger_itemserv_grupo_delete(self):
        response = self.client.delete(
            url_for(
                "geritemservgrupo.delete",
                id=self.get_id_fixed("ger_itemserv_grupo_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ger_numeracao
    # ===========================================================

    # ====================

    def ger_numeracao_id1(self):

        req_post = {
            "id": self.get_id_fixed("ger_numeracao_id1"),
            "nome": "TESTE [CRUD]",
            "serie": "1",
            "ultimo_nr": "1",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "sigla_ger_numeracao": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("gernumeracao.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_numeracao_id2(self):

        req_post = {
            "id": self.get_id_fixed("ger_numeracao_id2"),
            "nome": "TESTE [CRUD]",
            "serie": "1",
            "ultimo_nr": "1",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "sigla_ger_numeracao": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("gernumeracao.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_numeracao_get(self):
        response = self.client.get(
            url_for("gernumeracao.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ger_numeracao_get_by_id(self):
        response = self.client.get(
            url_for(
                "gernumeracao.find_by_id", id=self.get_id_fixed("ger_numeracao_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ger_numeracao_delete(self):
        response = self.client.delete(
            url_for("gernumeracao.delete", id=self.get_id_fixed("ger_numeracao_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ger_per
    # ===========================================================

    # ====================

    def ger_per_id1(self):

        req_post = {
            "id": self.get_id_fixed("ger_per_id1"),
            "ano_nome": "TESTE [CRUD]",
            "bimestre_nome": "TESTE [CRUD]",
            "data_ano_inicial": "05/02/2021",
            "data_bimestre_inicial": "05/02/2021",
            "data_dia_inicial": "05/02/2021",
            "data_mes_inicial": "05/02/2021",
            "data_quadrimestre_inicial": "05/02/2021",
            "data_quinzena_inicial": "05/02/2021",
            "data_semana_inicial": "05/02/2021",
            "data_semestre_inicial": "05/02/2021",
            "data_trimestre_inicial": "05/02/2021",
            "dia_nome": "TESTE [CRUD]",
            "mes_nome": "TESTE [CRUD]",
            "quadrimestre_nome": "TESTE [CRUD]",
            "quinzena_nome": "TESTE [CRUD]",
            "semana_nome": "TESTE [CRUD]",
            "semestre_nome": "TESTE [CRUD]",
            "trimestre_nome": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ger_per_tipo_id": module_tests_ger.ger_per_tipo_id1(self),
            "data_dia_final": "2022-12-29T00:00:00",
            "data_quinzena_final": "2022-12-29T00:00:00",
            "data_semana_final": "2022-12-29T00:00:00",
            "data_mes_final": "2022-12-29T00:00:00",
            "data_bimestre_final": "2022-12-29T00:00:00",
            "data_trimestre_final": "2022-12-29T00:00:00",
            "data_quadrimestre_final": "2022-12-29T00:00:00",
            "data_semestre_final": "2022-12-29T00:00:00",
            "data_ano_final": "2022-12-29T00:00:00",
            "dia_numero": "5",
            "quinzena_numero": "5",
            "semana_numero": "5",
            "mes_numero": "5",
            "bimestre_numero": "5",
            "trimestre_numero": "5",
            "quadrimestre_numero": "5",
            "semestre_numero": "5",
            "ano_numero": "5",
            "dia_tipo": "S",
            "quinzena_tipo": "S",
            "semana_tipo": "S",
            "mes_tipo": "S",
            "bimestre_tipo": "S",
            "trimestre_tipo": "S",
            "quadrimestre_tipo": "S",
            "semestre_tipo": "S",
            "ano_tipo": "S",
            "sys_process_log_id": module_tests_sys.module_tests_sys.sys_process_log_id1(
                self
            ),
        }

        response = self.client.post(
            url_for("gerper.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_per_id2(self):

        req_post = {
            "id": self.get_id_fixed("ger_per_id2"),
            "ano_nome": "TESTE [CRUD]",
            "bimestre_nome": "TESTE [CRUD]",
            "data_ano_inicial": "05/02/2021",
            "data_bimestre_inicial": "05/02/2021",
            "data_dia_inicial": "05/02/2021",
            "data_mes_inicial": "05/02/2021",
            "data_quadrimestre_inicial": "05/02/2021",
            "data_quinzena_inicial": "05/02/2021",
            "data_semana_inicial": "05/02/2021",
            "data_semestre_inicial": "05/02/2021",
            "data_trimestre_inicial": "05/02/2021",
            "dia_nome": "TESTE [CRUD]",
            "mes_nome": "TESTE [CRUD]",
            "quadrimestre_nome": "TESTE [CRUD]",
            "quinzena_nome": "TESTE [CRUD]",
            "semana_nome": "TESTE [CRUD]",
            "semestre_nome": "TESTE [CRUD]",
            "trimestre_nome": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ger_per_tipo_id": module_tests_ger.ger_per_tipo_id1(self),
            "data_dia_final": "2022-12-29T00:00:00",
            "data_quinzena_final": "2022-12-29T00:00:00",
            "data_semana_final": "2022-12-29T00:00:00",
            "data_mes_final": "2022-12-29T00:00:00",
            "data_bimestre_final": "2022-12-29T00:00:00",
            "data_trimestre_final": "2022-12-29T00:00:00",
            "data_quadrimestre_final": "2022-12-29T00:00:00",
            "data_semestre_final": "2022-12-29T00:00:00",
            "data_ano_final": "2022-12-29T00:00:00",
            "dia_numero": "5",
            "quinzena_numero": "5",
            "semana_numero": "5",
            "mes_numero": "5",
            "bimestre_numero": "5",
            "trimestre_numero": "5",
            "quadrimestre_numero": "5",
            "semestre_numero": "5",
            "ano_numero": "5",
            "dia_tipo": "S",
            "quinzena_tipo": "S",
            "semana_tipo": "S",
            "mes_tipo": "S",
            "bimestre_tipo": "S",
            "trimestre_tipo": "S",
            "quadrimestre_tipo": "S",
            "semestre_tipo": "S",
            "ano_tipo": "S",
            "sys_process_log_id": module_tests_sys.module_tests_sys.sys_process_log_id1(
                self
            ),
        }

        response = self.client.post(
            url_for("gerper.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_per_get(self):

        response = self.client.get(
            url_for("gerper.find_all"), headers=self.create_token()
        )
        result = len(response.json) > 0

        self.assertTrue(result)

    # ====================

    def ger_per_get_by_id(self):
        response = self.client.get(
            url_for("gerper.find_by_id", id=self.get_id_fixed("ger_per_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ger_per_delete(self):
        response = self.client.delete(
            url_for("gerper.delete", id=self.get_id_fixed("ger_per_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ger_pessoa
    # ===========================================================

    # ====================

    def ger_pessoa_id1(self):

        req_post = {
            "id": self.get_id_fixed("ger_pessoa_id1"),
            "ativo": "S",
            "contato_1": "CONTATO 1 EXEMPLE TESTE",
            "contato_2": "CONTATO 2 EXEMPLE TESTE",
            "contato_3": "CONTATO 3 EXEMPLE TESTE",
            "contrib_icms": "1",
            "data_abertura": "07/05/2022",
            "data_valid": "07/05/2022",
            "doc_cnae": "DOCS EXEMPLE TESTE",
            "doc_cnpj": "DOCS EXEMPLE TESTE",
            "doc_cpf": "DOCS EXEMPLE TESTE",
            "doc_crc": "DOCS EXEMPLES TESTE",
            "doc_crc_org_exp": "DOCS EXEMPLE TESTE",
            "doc_crc_seq": "DOCS EXEMPLE TESTE",
            "doc_ie": "DOCS EXEMPLE TESTE",
            "doc_im": "DOCS EXEMPLE TESTE",
            "doc_junta": "DOCS EXEMPLE TESTE",
            "doc_rg": "DOCS EXEMPLE TESTE",
            "doc_rg_org_exp": "DOCS EXEMPLE TESTE",
            "doc_taf": "DOCS EXEMPLE TESTE",
            "fis_regime": "FISCAL REGIME EXEMPLE",
            "fone_1": "FONE 1 EXEMPLE TESTE",
            "fone_2": "FONE 2 EXEMPLE TESTE",
            "fone_3": "FONE 3 EXEMPLE TESTE",
            "nome": "NOME [TESTE]",
            "nr_registro_est_cte": "NUMERO TESTE REGISTRO",
            "nr_rntrc": "1",
            "razao_social": "st",
            "sigla_pes": "st",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ger_pessoa_conta_banco_childs": [
                {
                    "id": self.get_id_fixed("ger_pessoa_conta_banco_id1"),
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "agencia": "5",
                    "conta": "5",
                    "observacao": "TESTE [CRUD]1",
                    "fin_banco_id": module_tests_fin.module_tests_fin.fin_banco_id1(
                        self
                    ),
                }
            ],
            "ger_pessoa_endereco_childs": [
                {
                    "id": self.get_id_fixed("ger_pessoa_endereco_id1"),
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "end_bairro": "XXXXXXXXXX",
                    "email": "XXXXXXXXXX",
                    "fone": "XXXXXXXX",
                    "end_logradouro": "",
                    "contato": "XXXXXXX",
                    "end_complemento": "XXXXXXX",
                    "end_cep": "XXXXXXXXXX",
                    "end_ger_cidade_id": module_tests_ger.ger_cidade_id1(self),
                    "tipo": "F",
                    "end_logradouro_nr": "XX",
                    "padrao": "S",
                }
            ],
        }

        response = self.client.post(
            url_for("gerpessoa.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_pessoa_id2(self):

        req_post = {
            "id": self.get_id_fixed("ger_pessoa_id2"),
            "ativo": "S",
            "contato_1": "CONTATO 1 EXEMPLE TESTE",
            "contato_2": "CONTATO 2 EXEMPLE TESTE",
            "contato_3": "CONTATO 3 EXEMPLE TESTE",
            "contrib_icms": "1",
            "data_abertura": "07/05/2022",
            "data_valid": "07/05/2022",
            "doc_cnae": "DOCS EXEMPLE TESTE",
            "doc_cnpj": "DOCS EXEMPLE TESTE",
            "doc_cpf": "DOCS EXEMPLE TESTE",
            "doc_crc": "DOCS EXEMPLES TESTE",
            "doc_crc_org_exp": "DOCS EXEMPLE TESTE",
            "doc_crc_seq": "DOCS EXEMPLE TESTE",
            "doc_ie": "DOCS EXEMPLE TESTE",
            "doc_im": "DOCS EXEMPLE TESTE",
            "doc_junta": "DOCS EXEMPLE TESTE",
            "doc_rg": "DOCS EXEMPLE TESTE",
            "doc_rg_org_exp": "DOCS EXEMPLE TESTE",
            "doc_taf": "DOCS EXEMPLE TESTE",
            "fis_regime": "FISCAL REGIME EXEMPLE",
            "fone_1": "FONE 1 EXEMPLE TESTE",
            "fone_2": "FONE 2 EXEMPLE TESTE",
            "fone_3": "FONE 3 EXEMPLE TESTE",
            "nome": "NOME [TESTE]",
            "nr_registro_est_cte": "NUMERO TESTE REGISTRO",
            "nr_rntrc": "1",
            "razao_social": "TESTE",
            "sigla_pes": "TESTE",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("gerpessoa.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_pessoa_get(self):
        response = self.client.get(
            url_for("gerpessoa.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ger_pessoa_get_by_id(self):
        response = self.client.get(
            url_for("gerpessoa.find_by_id", id=self.get_id_fixed("ger_pessoa_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ger_pessoa_delete(self):
        response = self.client.delete(
            url_for("gerpessoa.delete", id=self.get_id_fixed("ger_pessoa_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ger_unit_param
    # ===========================================================

    # ====================

    def ger_unit_param_id1(self):

        req_post = {
            "id": self.get_id_fixed("ger_unit_param_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_valid_ini": "2022-12-29T00:00:00",
        }

        response = self.client.post(
            url_for("gerunitparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_unit_param_id2(self):

        req_post = {
            "id": self.get_id_fixed("ger_unit_param_id2"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_valid_ini": "2022-12-29T00:00:00",
        }

        response = self.client.post(
            url_for("gerunitparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_unit_param_get(self):
        response = self.client.get(
            url_for("gerunitparam.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ger_unit_param_get_by_id(self):
        response = self.client.get(
            url_for(
                "gerunitparam.find_by_id", id=self.get_id_fixed("ger_unit_param_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ger_unit_param_delete(self):
        response = self.client.delete(
            url_for("gerunitparam.delete", id=self.get_id_fixed("ger_unit_param_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ger_processo_bloq
    # ===========================================================

    # ====================

    def ger_processo_bloq_id1(self):

        req_post = {
            "id": self.get_id_fixed("ger_processo_bloq_id1"),
            "data_lib_final": "05/06/2022",
            "data_lib_inicial": "05/06/2022",
            "ger_empresa_id": module_tests_ger.ger_empresa_id1(self),
            "observacao": "TESTE [CRUD]1",
            "tipo_processo": "S",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ger_processo_bloq_user_childs": [
                {
                    "id": self.get_id_fixed("ger_processo_bloq_user_id1"),
                    "tipo_bloq": "E",
                    "sys_user_id": module_tests_sys.module_tests_sys.sys_user_id1(self),
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                }
            ],
        }

        response = self.client.post(
            url_for("gerprocessobloq.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_processo_bloq_id2(self):

        req_post = {
            "id": self.get_id_fixed("ger_processo_bloq_id2"),
            "data_lib_final": "05/06/2022",
            "data_lib_inicial": "05/06/2022",
            "ger_empresa_id": module_tests_ger.ger_empresa_id1(self),
            "observacao": "TESTE [CRUD]",
            "tipo_processo": "S",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ger_processo_bloq_user_childs": [
                {
                    "tipo_bloq": "E",
                    "sys_user_id": module_tests_sys.module_tests_sys.sys_user_id1(self),
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                }
            ],
        }

        response = self.client.post(
            url_for("gerprocessobloq.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_processo_bloq_get(self):
        response = self.client.get(
            url_for("gerprocessobloq.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ger_processo_bloq_get_by_id(self):
        response = self.client.get(
            url_for(
                "gerprocessobloq.find_by_id",
                id=self.get_id_fixed("ger_processo_bloq_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ger_processo_bloq_delete(self):
        response = self.client.delete(
            url_for(
                "gerprocessobloq.delete", id=self.get_id_fixed("ger_processo_bloq_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ger_empresa_grupo
    # ===========================================================

    # ====================

    def ger_empresa_grupo_id1(self):

        req_post = {
            "id": self.get_id_fixed("ger_empresa_grupo_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_ger_empresa_grupo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("gerempresagrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_empresa_grupo_id2(self):

        req_post = {
            "id": self.get_id_fixed("ger_empresa_grupo_id2"),
            "nome": "TESTE [CRUD]",
            "sigla_ger_empresa_grupo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("gerempresagrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_empresa_grupo_get(self):
        response = self.client.get(
            url_for("gerempresagrupo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ger_empresa_grupo_get_by_id(self):
        response = self.client.get(
            url_for(
                "gerempresagrupo.find_by_id",
                id=self.get_id_fixed("ger_empresa_grupo_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ger_empresa_grupo_delete(self):
        response = self.client.delete(
            url_for(
                "gerempresagrupo.delete", id=self.get_id_fixed("ger_empresa_grupo_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ger_est_nivel
    # ===========================================================

    # ====================

    def ger_est_nivel_id1(self):

        req_post = {
            "id": self.get_id_fixed("ger_est_nivel_id1"),
            "bloq_mov_pedido": "S",
            "bloq_mov_solic": "N",
            "nome": "TESTE [CRUD]",
            "observacao": "TESTE [CRUD]",
            "sigla_ger_est_nivel": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("gerestnivel.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_est_nivel_id2(self):

        req_post = {
            "id": self.get_id_fixed("ger_est_nivel_id2"),
            "bloq_mov_pedido": "S",
            "bloq_mov_solic": "N",
            "nome": "TESTE [CRUD]",
            "observacao": "TESTE [CRUD]",
            "sigla_ger_est_nivel": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("gerestnivel.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_est_nivel_get(self):
        response = self.client.get(
            url_for("gerestnivel.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ger_est_nivel_get_by_id(self):
        response = self.client.get(
            url_for(
                "gerestnivel.find_by_id", id=self.get_id_fixed("ger_est_nivel_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ger_est_nivel_delete(self):
        response = self.client.delete(
            url_for("gerestnivel.delete", id=self.get_id_fixed("ger_est_nivel_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ger_pais
    # ===========================================================

    # ====================

    def ger_pais_id1(self):
        req_post = {
            "id": self.get_id_fixed("ger_pais_id1"),
            "nome": "TESTE [CRUD]1",
            "nr_pais": "1",
            "sigla_pais": "s",
            "ger_uf_childs": [
                {
                    "id": self.get_id_fixed("ger_uf_id1"),
                    "sigla_uf": "TESTE [CRUD]1",
                    "nr_uf": "1",
                    "nome": "TESTE [CRUD]1",
                }
            ],
        }

        response = self.client.post(
            url_for("gerpais.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_pais_id2(self):

        req_post = {
            "id": self.get_id_fixed("ger_pais_id2"),
            "nome": "TESTE [CRUD]2",
            "nr_pais": "1",
            "sigla_pais": "s",
            "ger_uf_childs": [
                {"sigla_uf": "TESTE [CRUD]2", "nr_uf": "1", "nome": "TESTE [CRUD]2"}
            ],
        }

        response = self.client.post(
            url_for("gerpais.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_pais_get(self):
        response = self.client.get(
            url_for("gerpais.find_all"), headers=self.create_token()
        )
        result = len(response.json) > 0
        self.assertTrue(result)

    # ====================

    def ger_pais_get_by_id(self):
        response = self.client.get(
            url_for("gerpais.find_by_id", id=self.get_id_fixed("ger_pais_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ger_pais_delete(self):
        response = self.client.delete(
            url_for("gerpais.delete", id=self.get_id_fixed("ger_pais_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ger_index
    # ===========================================================

    # ====================

    def ger_index_id1(self):

        req_post = {
            "id": self.get_id_fixed("ger_index_id1"),
            "ativo": "S",
            "nome": "TESTE [CRUD]",
            "sigla_index": "S",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("gerindex.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_index_id2(self):

        req_post = {
            "id": self.get_id_fixed("ger_index_id2"),
            "ativo": "S",
            "nome": "TESTE [CRUD]",
            "sigla_index": "S",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("gerindex.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_index_get(self):
        response = self.client.get(
            url_for("gerindex.find_all"), headers=self.create_token()
        )
        result = len(response.json) > 0
        self.assertTrue(result)

    # ====================

    def ger_index_get_by_id(self):
        response = self.client.get(
            url_for("gerindex.find_by_id", id=self.get_id_fixed("ger_index_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ger_index_delete(self):
        response = self.client.delete(
            url_for("gerindex.delete", id=self.get_id_fixed("ger_index_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ger_marca
    # ===========================================================

    # ====================

    def ger_marca_id1(self):

        req_post = {
            "id": self.get_id_fixed("ger_marca_id1"),
            "nome": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "sigla_ger_marca": "TESTE [CRUD]",
            "ger_marca_modelo_childs": [
                {
                    "id": self.get_id_fixed("ger_marca_modelo_id1"),
                    "sigla_ger_marca_modelo": "TESTE [CRUD]2",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "nome": "TESTE [CRUD]1",
                }
            ],
            "ger_marca_pessoa_childs": [
                {
                    "id": self.get_id_fixed("ger_marca_pessoa_id1"),
                    "ger_pessoa_id": module_tests_ger.ger_pessoa_id1(self),
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "observacao": "TESTE [CRUD]2",
                }
            ],
        }

        response = self.client.post(
            url_for("germarca.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_marca_id2(self):

        req_post = {
            "id": self.get_id_fixed("ger_marca_id2"),
            "nome": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "sigla_ger_marca": "TESTE [CRUD]",
            "ger_marca_modelo_childs": [
                {
                    "sigla_ger_marca_modelo": "TESTE [CRUD]2",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "nome": "TESTE [CRUD]1",
                }
            ],
            "ger_marca_pessoa_childs": [
                {
                    "ger_pessoa_id": module_tests_ger.ger_pessoa_id1(self),
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "observacao": "TESTE [CRUD]2",
                }
            ],
        }

        response = self.client.post(
            url_for("germarca.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_marca_get(self):
        response = self.client.get(
            url_for("germarca.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ger_marca_get_by_id(self):
        response = self.client.get(
            url_for("germarca.find_by_id", id=self.get_id_fixed("ger_marca_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ger_marca_delete(self):
        response = self.client.delete(
            url_for("germarca.delete", id=self.get_id_fixed("ger_marca_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ger_cidade gercidade
    # ===========================================================

    # ====================

    def ger_cidade_id1(self):
        module_tests_ger.ger_pais_id1(self)
        req_post = {
            "id": self.get_id_fixed("ger_cidade_id1"),
            "nome": "TESTE [CRUD]",
            "nr_cidade": "16",
            "ger_uf_id": self.get_id_fixed("ger_uf_id1"),
        }

        response = self.client.post(
            url_for("gercidade.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_cidade_id2(self):
        module_tests_ger.ger_pais_id1(self)
        req_post = {
            "id": self.get_id_fixed("ger_cidade_id2"),
            "nome": "TESTE [CRUD]",
            "nr_cidade": "16",
            "ger_uf_id": self.get_id_fixed("ger_uf_id1"),
        }

        response = self.client.post(
            url_for("gercidade.save"), json=req_post, headers=self.create_token()
        )

        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_cidade_get(self):
        response = self.client.get(
            url_for("gercidade.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ger_cidade_get_by_id(self):
        response = self.client.get(
            url_for("gercidade.find_by_id", id=self.get_id_fixed("ger_cidade_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ger_cidade_delete(self):
        response = self.client.delete(
            url_for("gercidade.delete", id=self.get_id_fixed("ger_cidade_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ger_umedida
    # ===========================================================

    # ====================

    def ger_umedida_id1(self):

        req_post = {
            "id": self.get_id_fixed("ger_umedida_id1"),
            "nome": "TESTE [CRUD]1",
            "sigla_umedida": "TESTE [CRUD]1",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("gerumedida.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_umedida_id2(self):

        req_post = {
            "id": self.get_id_fixed("ger_umedida_id2"),
            "nome": "TESTE [CRUD]2",
            "sigla_umedida": "TESTE [CRUD]2",
            "ativo": "S",
            "ger_umedida_conv_childs": [
                {
                    "ger_umedida_id_para": module_tests_ger.ger_umedida_id1(self),
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "fator_mult": "5",
                }
            ],
        }

        response = self.client.post(
            url_for("gerumedida.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_umedida_get(self):
        response = self.client.get(
            url_for("gerumedida.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ger_umedida_get_by_id(self):
        response = self.client.get(
            url_for("gerumedida.find_by_id", id=self.get_id_fixed("ger_umedida_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ger_umedida_delete(self):
        response = self.client.delete(
            url_for("gerumedida.delete", id=self.get_id_fixed("ger_umedida_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ger_itemserv_compos
    # ===========================================================

    # ====================

    def ger_itemserv_compos_id1(self):

        req_post = {
            "id": self.get_id_fixed("ger_itemserv_compos_id1"),
            "ativo": "S",
            "fator_mult": "12",
            "ger_itemserv_compos_tipo_id": module_tests_ger.ger_itemserv_compos_tipo_id1(
                self
            ),
            "ger_itemserv_id_de": module_tests_ger.ger_itemserv_id1(self),
            "ger_itemserv_id_para": module_tests_ger.ger_itemserv_id1(self),
            "observacao": "TESTE [CRUD]",
            "ordem": "TESTE [CRUD]",
            "qnt_altura": "12",
            "qnt_compos": "12",
            "qnt_comprimento": "12",
            "qnt_largura": "12",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("geritemservcompos.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_itemserv_compos_id2(self):

        req_post = {
            "id": self.get_id_fixed("ger_itemserv_compos_id2"),
            "ativo": "S",
            "fator_mult": "12",
            "ger_itemserv_compos_tipo_id": module_tests_ger.ger_itemserv_compos_tipo_id1(
                self
            ),
            "ger_itemserv_id_de": module_tests_ger.ger_itemserv_id1(self),
            "ger_itemserv_id_para": module_tests_ger.ger_itemserv_id1(self),
            "observacao": "TESTE [CRUD]2",
            "ordem": "TESTE [CRUD]",
            "qnt_altura": "12",
            "qnt_compos": "12",
            "qnt_comprimento": "12",
            "qnt_largura": "12",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("geritemservcompos.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_itemserv_compos_get(self):
        response = self.client.get(
            url_for("geritemservcompos.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ger_itemserv_compos_get_by_id(self):
        response = self.client.get(
            url_for(
                "geritemservcompos.find_by_id",
                id=self.get_id_fixed("ger_itemserv_compos_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ger_itemserv_compos_delete(self):
        response = self.client.delete(
            url_for(
                "geritemservcompos.delete",
                id=self.get_id_fixed("ger_itemserv_compos_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ger_itemserv_compos_tipo
    # ===========================================================

    # ====================

    def ger_itemserv_compos_tipo_id1(self):

        req_post = {
            "id": self.get_id_fixed("ger_itemserv_compos_tipo_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_ger_itemserv_compos_tipo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("geritemservcompostipo.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_itemserv_compos_tipo_id2(self):

        req_post = {
            "id": self.get_id_fixed("ger_itemserv_compos_tipo_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_ger_itemserv_compos_tipo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("geritemservcompostipo.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_itemserv_compos_tipo_get(self):
        response = self.client.get(
            url_for("geritemservcompostipo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ger_itemserv_compos_tipo_get_by_id(self):
        response = self.client.get(
            url_for(
                "geritemservcompostipo.find_by_id",
                id=self.get_id_fixed("ger_itemserv_compos_tipo_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ger_itemserv_compos_tipo_delete(self):
        response = self.client.delete(
            url_for(
                "geritemservcompostipo.delete",
                id=self.get_id_fixed("ger_itemserv_compos_tipo_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # ger_per_tipo
    # ===========================================================

    # ====================

    def ger_per_tipo_id1(self):

        req_post = {
            "id": self.get_id_fixed("ger_per_tipo_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "nome": "TESTE [CRUD]1",
            "ativo": "S",
            "sigla_per_tipo": "TESTE [CRUD]1",
            "ini_semana": "S",
        }

        response = self.client.post(
            url_for("gerpertipo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_per_tipo_id2(self):

        req_post = {
            "id": self.get_id_fixed("ger_per_tipo_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_ger_per_tipo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ini_semana": "S",
        }

        response = self.client.post(
            url_for("gerpertipo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def ger_per_tipo_get(self):
        response = self.client.get(
            url_for("gerpertipo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def ger_per_tipo_get_by_id(self):
        response = self.client.get(
            url_for("gerpertipo.find_by_id", id=self.get_id_fixed("ger_per_tipo_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def ger_per_tipo_delete(self):
        response = self.client.delete(
            url_for("gerpertipo.delete", id=self.get_id_fixed("ger_per_tipo_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)
