from flask import url_for

from generic_tests import generic_tests
import module_tests_ger
import module_tests_mov
import module_tests_sys


class module_tests_fis(generic_tests):

    # ===========================================================
    # fis_cest
    # ===========================================================

    # ====================

    def fis_cest_id1(self):
        req_post = {
            "id": self.get_id_fixed("fis_cest_id1"),
            "data_validade": "06/08/2022",
            "nome": "TESTE [CRUD]",
            "nr_cest": "TESTE [CRUD]1",
            "ativo": "S",
            "fis_cest_ncm_childs": [
                {
                    "id": self.get_id_fixed("fis_cest_ncm_id1"),
                    "fis_ncm_id": module_tests_fis.fis_ncm_id1(self),
                }
            ],
        }

        response = self.client.post(
            url_for("fiscest.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fis_cest_id2(self):

        req_post = {
            "id": self.get_id_fixed("fis_cest_id2"),
            "data_validade": "06/08/2022",
            "nome": "TESTE [CRUD]",
            "nr_cest": "8",
            "ativo": "S",
            "fis_cest_ncm_childs": [{"fis_ncm_id": module_tests_fis.fis_ncm_id1(self)}],
        }

        response = self.client.post(
            url_for("fiscest.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fis_cest_get(self):
        response = self.client.get(
            url_for("fiscest.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fis_cest_get_by_id(self):
        response = self.client.get(
            url_for("fiscest.find_by_id", id=self.get_id_fixed("fis_cest_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def fis_cest_delete(self):
        response = self.client.delete(
            url_for("fiscest.delete", id=self.get_id_fixed("fis_cest_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fis_cfop
    # ===========================================================

    # ====================

    def fis_cfop_id1(self):

        req_post = {
            "id": self.get_id_fixed("fis_cfop_id1"),
            "data_validade": "06/08/2022",
            "nome": "TESTE [CRUD]",
            "nr_cfop": "8",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("fiscfop.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fis_cfop_id2(self):

        req_post = {
            "id": self.get_id_fixed("fis_cfop_id2"),
            "data_validade": "06/08/2022",
            "nome": "TESTE [CRUD]",
            "nr_cfop": "8",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("fiscfop.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fis_cfop_get(self):
        response = self.client.get(
            url_for("fiscfop.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fis_cfop_get_by_id(self):
        response = self.client.get(
            url_for("fiscfop.find_by_id", id=self.get_id_fixed("fis_cfop_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def fis_cfop_delete(self):

        response = self.client.delete(
            url_for("fiscfop.delete", id=self.get_id_fixed("fis_cfop_id2")),
            headers=self.create_token(),
        )

        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fis_doc_tipo
    # ===========================================================

    # ====================

    def fis_doc_tipo_id1(self):

        req_post = {
            "id": self.get_id_fixed("fis_doc_tipo_id1"),
            "nome": "TESTE [CRUD]1",
            "modelo": "TESTE [CRUD]1",
            "sigla_fis_doc_tipo": "TESTE [CRUD]1",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("fisdoctipo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fis_doc_tipo_id2(self):

        req_post = {
            "id": self.get_id_fixed("fis_doc_tipo_id2"),
            "nome": "TESTE [CRUD]2",
            "modelo": "TESTE [CRUD]2",
            "sigla_fis_doc_tipo": "TESTE [CRUD]2",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("fisdoctipo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fis_doc_tipo_get(self):
        response = self.client.get(
            url_for("fisdoctipo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fis_doc_tipo_get_by_id(self):
        response = self.client.get(
            url_for("fisdoctipo.find_by_id", id=self.get_id_fixed("fis_doc_tipo_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def fis_doc_tipo_delete(self):
        response = self.client.delete(
            url_for("fisdoctipo.delete", id=self.get_id_fixed("fis_doc_tipo_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fis_nbs
    # ===========================================================

    # ====================

    def fis_nbs_id1(self):

        req_post = {
            "id": self.get_id_fixed("fis_nbs_id1"),
            "data_validade": "2022-12-29T00:00:00",
            "nome": "TESTE [CRUD]",
            "nr_nbs": "8",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("fisnbs.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fis_nbs_id2(self):

        req_post = {
            "id": self.get_id_fixed("fis_nbs_id2"),
            "data_validade": "2022-12-29T00:00:00",
            "nome": "TESTE [CRUD]",
            "nr_nbs": "8",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("fisnbs.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fis_nbs_get(self):
        response = self.client.get(
            url_for("fisnbs.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fis_nbs_get_by_id(self):
        response = self.client.get(
            url_for("fisnbs.find_by_id", id=self.get_id_fixed("fis_nbs_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def fis_nbs_delete(self):
        response = self.client.delete(
            url_for("fisnbs.delete", id=self.get_id_fixed("fis_nbs_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fis_ncm
    # ===========================================================

    # ====================

    def fis_ncm_id1(self):

        req_post = {
            "id": self.get_id_fixed("fis_ncm_id1"),
            "data_validade": "06/08/2022",
            "nome": "TESTE [CRUD]",
            "nr_ncm": "8",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("fisncm.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fis_ncm_id2(self):

        req_post = {
            "id": self.get_id_fixed("fis_ncm_id2"),
            "data_validade": "06/08/2022",
            "nome": "TESTE [CRUD]",
            "nr_ncm": "8",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("fisncm.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fis_ncm_get(self):
        response = self.client.get(
            url_for("fisncm.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fis_ncm_get_by_id(self):
        response = self.client.get(
            url_for("fisncm.find_by_id", id=self.get_id_fixed("fis_ncm_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def fis_ncm_delete(self):
        response = self.client.delete(
            url_for("fisncm.delete", id=self.get_id_fixed("fis_ncm_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fis_tributo
    # ===========================================================

    # ====================

    def fis_tributo_id1(self):

        req_post = {
            "id": self.get_id_fixed("fis_tributo_id1"),
            "nome": "TESTE [CRUD]",
            "nr_tributo": "8",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("fistributo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fis_tributo_id2(self):

        req_post = {
            "id": self.get_id_fixed("fis_tributo_id2"),
            "nome": "TESTE [CRUD]",
            "nr_tributo": "8",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("fistributo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fis_tributo_get(self):
        response = self.client.get(
            url_for("fistributo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fis_tributo_get_by_id(self):
        response = self.client.get(
            url_for("fistributo.find_by_id", id=self.get_id_fixed("fis_tributo_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def fis_tributo_delete(self):
        response = self.client.delete(
            url_for("fistributo.delete", id=self.get_id_fixed("fis_tributo_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fis_certificado
    # ===========================================================

    # ====================

    def fis_certificado_id1(self):

        req_post = {
            "id": self.get_id_fixed("fis_certificado_id1"),
            "nome": "TESTE [CRUD]",
            "nome_arq_certificado": "TESTE [CRUD]",
            "senha": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "S",
        }

        response = self.client.post(
            url_for("fiscertificado.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fis_certificado_id2(self):

        req_post = {
            "id": self.get_id_fixed("fis_certificado_id2"),
            "nome": "TESTE [CRUD]",
            "nome_arq_certificado": "TESTE [CRUD]",
            "senha": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "S",
        }

        response = self.client.post(
            url_for("fiscertificado.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fis_certificado_get(self):
        response = self.client.get(
            url_for("fiscertificado.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fis_certificado_get_by_id(self):
        response = self.client.get(
            url_for(
                "fiscertificado.find_by_id", id=self.get_id_fixed("fis_certificado_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def fis_certificado_delete(self):
        response = self.client.delete(
            url_for(
                "fiscertificado.delete", id=self.get_id_fixed("fis_certificado_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fis_obs
    # ===========================================================

    # ====================

    def fis_obs_id1(self):

        req_post = {
            "id": self.get_id_fixed("fis_obs_id1"),
            "nome": "TESTE [CRUD]",
            "observacao": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "S",
        }

        response = self.client.post(
            url_for("fisobs.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fis_obs_id2(self):

        req_post = {
            "id": self.get_id_fixed("fis_obs_id2"),
            "nome": "TESTE [CRUD]",
            "observacao": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "S",
        }

        response = self.client.post(
            url_for("fisobs.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fis_obs_get(self):
        response = self.client.get(
            url_for("fisobs.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fis_obs_get_by_id(self):
        response = self.client.get(
            url_for("fisobs.find_by_id", id=self.get_id_fixed("fis_obs_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def fis_obs_delete(self):
        response = self.client.delete(
            url_for("fisobs.delete", id=self.get_id_fixed("fis_obs_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fis_unit_param
    # ===========================================================

    # ====================

    def fis_unit_param_id1(self):

        req_post = {
            "id": self.get_id_fixed("fis_unit_param_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_valid_ini": "2022-12-29T00:00:00",
        }

        response = self.client.post(
            url_for("fisunitparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fis_unit_param_id2(self):

        req_post = {
            "id": self.get_id_fixed("fis_unit_param_id2"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_valid_ini": "2022-12-29T00:00:00",
        }

        response = self.client.post(
            url_for("fisunitparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fis_unit_param_get(self):
        response = self.client.get(
            url_for("fisunitparam.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fis_unit_param_get_by_id(self):
        response = self.client.get(
            url_for(
                "fisunitparam.find_by_id", id=self.get_id_fixed("fis_unit_param_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def fis_unit_param_delete(self):
        response = self.client.delete(
            url_for("fisunitparam.delete", id=self.get_id_fixed("fis_unit_param_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fis_ibpt
    # ===========================================================

    # ====================

    def fis_ibpt_id1(self):
        module_tests_ger.module_tests_ger.ger_pais_id1(self)
        req_post = {
            "id": self.get_id_fixed("fis_ibpt_id1"),
            "data_validade_fin": "2022-12-29T00:00:00",
            "data_validade_ini": "2022-12-29T00:00:00",
            "fis_nbs_id": module_tests_fis.fis_nbs_id1(self),
            "fis_ncm_id": module_tests_fis.fis_ncm_id1(self),
            "ger_uf_id": self.get_id_fixed("ger_uf_id1"),
            "perc_importado": "8",
            "perc_municipal": "8",
            "perc_nacional": "8",
        }

        response = self.client.post(
            url_for("fisibpt.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fis_ibpt_id2(self):
        module_tests_ger.module_tests_ger.ger_pais_id1(self)
        req_post = {
            "id": self.get_id_fixed("fis_ibpt_id2"),
            "data_validade_fin": "2022-12-29T00:00:00",
            "data_validade_ini": "2022-12-29T00:00:00",
            "fis_nbs_id": module_tests_fis.fis_nbs_id1(self),
            "fis_ncm_id": module_tests_fis.fis_ncm_id1(self),
            "ger_uf_id": self.get_id_fixed("ger_uf_id1"),
            "perc_importado": "8",
            "perc_municipal": "8",
            "perc_nacional": "8",
        }

        response = self.client.post(
            url_for("fisibpt.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fis_ibpt_get(self):
        response = self.client.get(
            url_for("fisibpt.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fis_ibpt_get_by_id(self):
        response = self.client.get(
            url_for("fisibpt.find_by_id", id=self.get_id_fixed("fis_ibpt_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def fis_ibpt_delete(self):
        response = self.client.delete(
            url_for("fisibpt.delete", id=self.get_id_fixed("fis_ibpt_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fis_doc
    # ===========================================================

    # ====================

    def fis_doc_id1(self):

        req_post = {
            "id": self.get_id_fixed("fis_doc_id1"),
            "ambiente": "1",
            "chave": "TESTE [CRUD]",
            "data_autorizado": "2022-12-29T00:00:00",
            "data_cancelado": "28/12/2022",
            "data_emissao": "2022-12-29T00:00:00",
            "data_encerrado": "2022-12-29T00:00:00",
            "fis_doc_tipo_id": module_tests_fis.fis_doc_tipo_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "numero": "8",
            "numero_fin": "8",
            "numero_ini": "8",
            "numero_pre": "8",
            "pdf_emitido": "N",
            "serie": "8",
            "serie_pre": "8",
            "status_sefaz": "8",
            "tipo_emissao": "2",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "xml_assinado": "N",
            "xml_protocolado": "N",
            "mov_id": module_tests_mov.module_tests_mov.mov_id1(self),
            "fis_doc_evento_childs": [
                {
                    "id": self.get_id_fixed("fis_doc_evento_id1"),
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "qnt_evento": "1",
                    "nr_protocolo": "1",
                    "pdf_retorno": "TESTE [CRUD]1",
                    "xml_retorno": "TESTE [CRUD]1",
                    "tipo_evento": "2",
                    "descricao_evento": "TESTE [CRUD]1",
                }
            ],
        }

        response = self.client.post(
            url_for("fisdoc.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fis_doc_id2(self):

        req_post = {
            "id": self.get_id_fixed("fis_doc_id2"),
            "ambiente": "1",
            "chave": "TESTE [CRUD]",
            "data_autorizado": "2022-12-29T00:00:00",
            "data_cancelado": "28/12/2022",
            "data_emissao": "2022-12-29T00:00:00",
            "data_encerrado": "2022-12-29T00:00:00",
            "fis_doc_tipo_id": module_tests_fis.fis_doc_tipo_id1(self),
            "ger_empresa_id": module_tests_ger.module_tests_ger.ger_empresa_id1(self),
            "numero": "8",
            "numero_fin": "8",
            "numero_ini": "8",
            "numero_pre": "8",
            "pdf_emitido": "N",
            "serie": "8",
            "serie_pre": "8",
            "status_sefaz": "8",
            "tipo_emissao": "2",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "xml_assinado": "N",
            "xml_protocolado": "N",
            "mov_id": module_tests_mov.module_tests_mov.mov_id1(self),
            "fis_doc_evento_childs": [
                {
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "qnt_evento": "1",
                    "nr_protocolo": "1",
                    "pdf_retorno": "TESTE [CRUD]1",
                    "xml_retorno": "TESTE [CRUD]1",
                    "tipo_evento": "2",
                    "descricao_evento": "TESTE [CRUD]1",
                }
            ],
        }

        response = self.client.post(
            url_for("fisdoc.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fis_doc_get(self):
        response = self.client.get(
            url_for("fisdoc.find_all"), headers=self.create_token()
        )
        result = len(response.json) > 0
        self.assertTrue(result)

    # ====================

    def fis_doc_get_by_id(self):
        response = self.client.get(
            url_for("fisdoc.find_by_id", id=self.get_id_fixed("fis_doc_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def fis_doc_delete(self):
        response = self.client.delete(
            url_for("fisdoc.delete", id=self.get_id_fixed("fis_doc_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # fis_tributacao
    # ===========================================================

    # ====================

    def fis_tributacao_id1(self):

        req_post = {
            "id": self.get_id_fixed("fis_tributacao_id1"),
            "descricao_evento": "TESTE [CRUD]",
            "fis_doc_id": module_tests_fis.fis_doc_id1(self),
            "nr_protocolo": "8",
            "pdf_retorno": "n",
            "qnt_evento": "5",
            "tipo_evento": "1",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "xml_retorno": "N",
        }

        response = self.client.post(
            url_for("fistributacao.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fis_tributacao_id2(self):

        req_post = {
            "id": self.get_id_fixed("fis_tributacao_id2"),
            "descricao_evento": "TESTE [CRUD]",
            "fis_doc_id": module_tests_fis.fis_doc_id1(self),
            "nr_protocolo": "8",
            "pdf_retorno": "n",
            "qnt_evento": "5",
            "tipo_evento": "1",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "xml_retorno": "N",
        }

        response = self.client.post(
            url_for("fistributacao.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def fis_tributacao_get(self):
        response = self.client.get(
            url_for("fistributacao.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def fis_tributacao_get_by_id(self):
        response = self.client.get(
            url_for(
                "fistributacao.find_by_id", id=self.get_id_fixed("fis_tributacao_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def fis_tributacao_delete(self):
        response = self.client.delete(
            url_for("fistributacao.delete", id=self.get_id_fixed("fis_tributacao_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)
