from flask import url_for
from generic_tests import generic_tests
import module_tests_sys


class module_tests_crm(generic_tests):

    # ===========================================================
    # crm_aviso
    # ===========================================================

    # ====================

    def crm_aviso_id1(self):

        req_post = {
            "id": self.get_id_fixed("crm_aviso_id1"),
            "nome": "TESTE [CRUD]1",
            "sigla_aviso": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("crmaviso.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_aviso_id2(self):

        req_post = {
            "id": self.get_id_fixed("crm_aviso_id2"),
            "nome": "TESTE [CRUD]2",
            "sigla_aviso": "TESTE [CRUD]2",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("crmaviso.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_aviso_get(self):
        response = self.client.get(
            url_for("crmaviso.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def crm_aviso_get_by_id(self):
        response = self.client.get(
            url_for("crmaviso.find_by_id", id=self.get_id_fixed("crm_aviso_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def crm_aviso_delete(self):
        response = self.client.delete(
            url_for("crmaviso.delete", id=self.get_id_fixed("crm_aviso_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # crm_chat_grupo
    # ===========================================================

    # ====================

    def crm_chat_grupo_id1(self):

        req_post = {
            "id": self.get_id_fixed("crm_chat_grupo_id1"),
            "acesso_privado": "S",
            "nome": "TESTE [CRUD]",
            "senha": "TESTE [CRUD]",
            "sigla_chat_grupo": "t",
            "sys_user_id_dest": module_tests_sys.module_tests_sys.sys_user_id1(self),
            "sys_user_id_orig": module_tests_sys.module_tests_sys.sys_user_id1(self),
            "tipo": "G",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("crmchatgrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_chat_grupo_id2(self):

        req_post = {
            "id": self.get_id_fixed("crm_chat_grupo_id2"),
            "acesso_privado": "S",
            "nome": "TESTE [CRUD]",
            "senha": "TESTE [CRUD]",
            "sigla_chat_grupo": "t",
            "sys_user_id_dest": module_tests_sys.module_tests_sys.sys_user_id1(self),
            "sys_user_id_orig": module_tests_sys.module_tests_sys.sys_user_id1(self),
            "tipo": "G",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("crmchatgrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_chat_grupo_get(self):
        response = self.client.get(
            url_for("crmchatgrupo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def crm_chat_grupo_get_by_id(self):
        response = self.client.get(
            url_for(
                "crmchatgrupo.find_by_id", id=self.get_id_fixed("crm_chat_grupo_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def crm_chat_grupo_delete(self):
        response = self.client.delete(
            url_for("crmchatgrupo.delete", id=self.get_id_fixed("crm_chat_grupo_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # crm_class_grupo
    # ===========================================================

    # ====================

    def crm_class_grupo_id1(self):

        req_post = {
            "id": self.get_id_fixed("crm_class_grupo_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_class_grupo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "S",
            "crm_class_subgrupo_childs": [
                {
                    "id": self.get_id_fixed("crm_class_subgrupo_id1"),
                    "sigla_class_subgrupo": "TESTE [CRUD]2",
                    "nome": "TESTE [CRUD]2",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                }
            ],
        }

        response = self.client.post(
            url_for("crmclassgrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_class_grupo_id2(self):

        req_post = {
            "id": self.get_id_fixed("crm_class_grupo_id2"),
            "nome": "TESTE [CRUD]",
            "sigla_class_grupo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "S",
            "crm_class_subgrupo_childs": [
                {
                    "id": self.get_id_fixed("crm_class_subgrupo_id2"),
                    "sigla_class_subgrupo": "TESTE [CRUD]2",
                    "nome": "TESTE [CRUD]2",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                }
            ],
        }

        response = self.client.post(
            url_for("crmclassgrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_class_grupo_get(self):
        response = self.client.get(
            url_for("crmclassgrupo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def crm_class_grupo_get_by_id(self):
        response = self.client.get(
            url_for(
                "crmclassgrupo.find_by_id", id=self.get_id_fixed("crm_class_grupo_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def crm_class_grupo_delete(self):
        response = self.client.delete(
            url_for(
                "crmclassgrupo.delete", id=self.get_id_fixed("crm_class_grupo_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # crm_etapa
    # ===========================================================

    # ====================

    def crm_etapa_id1(self):

        req_post = {
            "id": self.get_id_fixed("crm_etapa_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_etapa": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "S",
        }

        response = self.client.post(
            url_for("crmetapa.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_etapa_id2(self):

        req_post = {
            "id": self.get_id_fixed("crm_etapa_id2"),
            "nome": "TESTE [CRUD]",
            "sigla_etapa": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "S",
        }

        response = self.client.post(
            url_for("crmetapa.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_etapa_get(self):
        response = self.client.get(
            url_for("crmetapa.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def crm_etapa_get_by_id(self):
        response = self.client.get(
            url_for("crmetapa.find_by_id", id=self.get_id_fixed("crm_etapa_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def crm_etapa_delete(self):
        response = self.client.delete(
            url_for("crmetapa.delete", id=self.get_id_fixed("crm_etapa_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # crm_org
    # ===========================================================

    # ====================

    def crm_org_id1(self):

        req_post = {
            "id": self.get_id_fixed("crm_org_id1"),
            "ger_visual_user": "S",
            "nome": "TESTE [CRUD]",
            "sigla_org": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "user_visual_user": "S",
            "ativo": "N",
        }

        response = self.client.post(
            url_for("crmorg.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_org_id2(self):

        req_post = {
            "id": self.get_id_fixed("crm_org_id2"),
            "ger_visual_user": "S",
            "nome": "TESTE [CRUD]",
            "sigla_org": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "user_visual_user": "S",
            "ativo": "N",
        }

        response = self.client.post(
            url_for("crmorg.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_org_get(self):
        response = self.client.get(
            url_for("crmorg.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def crm_org_get_by_id(self):
        response = self.client.get(
            url_for("crmorg.find_by_id", id=self.get_id_fixed("crm_org_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def crm_org_delete(self):
        response = self.client.delete(
            url_for("crmorg.delete", id=self.get_id_fixed("crm_org_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # crm_prioridade
    # ===========================================================

    # ====================

    def crm_prioridade_id1(self):

        req_post = {
            "id": self.get_id_fixed("crm_prioridade_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_prioridade": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "S",
        }

        response = self.client.post(
            url_for("crmprioridade.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_prioridade_id2(self):

        req_post = {
            "id": self.get_id_fixed("crm_prioridade_id2"),
            "nome": "TESTE [CRUD]",
            "sigla_prioridade": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "S",
        }

        response = self.client.post(
            url_for("crmprioridade.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_prioridade_get(self):
        response = self.client.get(
            url_for("crmprioridade.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def crm_prioridade_get_by_id(self):
        response = self.client.get(
            url_for(
                "crmprioridade.find_by_id", id=self.get_id_fixed("crm_prioridade_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def crm_prioridade_delete(self):
        response = self.client.delete(
            url_for("crmprioridade.delete", id=self.get_id_fixed("crm_prioridade_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # crm_resposta
    # ===========================================================

    # ====================

    def crm_resposta_id1(self):

        req_post = {
            "id": self.get_id_fixed("crm_resposta_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_resposta": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "N",
        }

        response = self.client.post(
            url_for("crmresposta.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_resposta_id2(self):

        req_post = {
            "id": self.get_id_fixed("crm_resposta_id2"),
            "nome": "TESTE [CRUD]",
            "sigla_resposta": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "N",
        }

        response = self.client.post(
            url_for("crmresposta.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_resposta_get(self):
        response = self.client.get(
            url_for("crmresposta.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def crm_resposta_get_by_id(self):
        response = self.client.get(
            url_for("crmresposta.find_by_id", id=self.get_id_fixed("crm_resposta_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def crm_resposta_delete(self):
        response = self.client.delete(
            url_for("crmresposta.delete", id=self.get_id_fixed("crm_resposta_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # crm_status
    # ===========================================================

    # ====================

    def crm_status_id1(self):

        req_post = {
            "id": self.get_id_fixed("crm_status_id1"),
            "nome": "TESTE [CRUD]",
            "obrig_motivo": "S",
            "sigla_status": "TESTE [CRUD]",
            "tipo_status": "AT",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "S",
        }

        response = self.client.post(
            url_for("crmstatus.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_status_id2(self):

        req_post = {
            "id": self.get_id_fixed("crm_status_id2"),
            "nome": "TESTE [CRUD]",
            "obrig_motivo": "S",
            "sigla_status": "TESTE [CRUD]",
            "tipo_status": "AT",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "S",
            "crm_status_prox_childs": [
                {
                    "ordem": "1",
                    "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
                    "crm_status_id_prox": module_tests_crm.crm_status_id1(self),
                    "tipo_status_ant": "AT",
                }
            ],
        }

        response = self.client.post(
            url_for("crmstatus.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_status_get(self):
        response = self.client.get(
            url_for("crmstatus.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def crm_status_get_by_id(self):
        response = self.client.get(
            url_for("crmstatus.find_by_id", id=self.get_id_fixed("crm_status_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def crm_status_delete(self):
        response = self.client.delete(
            url_for("crmstatus.delete", id=self.get_id_fixed("crm_status_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # crm_tag
    # ===========================================================

    # ====================

    def crm_tag_id1(self):

        req_post = {
            "id": self.get_id_fixed("crm_tag_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_tag": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "S",
        }

        response = self.client.post(
            url_for("crmtag.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_tag_id2(self):

        req_post = {
            "id": self.get_id_fixed("crm_tag_id2"),
            "nome": "TESTE [CRUD]",
            "sigla_tag": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "S",
        }

        response = self.client.post(
            url_for("crmtag.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_tag_get(self):
        response = self.client.get(
            url_for("crmtag.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def crm_tag_get_by_id(self):
        response = self.client.get(
            url_for("crmtag.find_by_id", id=self.get_id_fixed("crm_tag_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def crm_tag_delete(self):
        response = self.client.delete(
            url_for("crmtag.delete", id=self.get_id_fixed("crm_tag_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # crm_unit_param
    # ===========================================================

    # ====================

    def crm_unit_param_id1(self):

        req_post = {
            "id": self.get_id_fixed("crm_unit_param_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_valid_ini": "2022-12-29T00:00:00",
        }

        response = self.client.post(
            url_for("crmunitparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_unit_param_id2(self):

        req_post = {
            "id": self.get_id_fixed("crm_unit_param_id2"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_valid_ini": "2022-12-29T00:00:00",
        }

        response = self.client.post(
            url_for("crmunitparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_unit_param_get(self):
        response = self.client.get(
            url_for("crmunitparam.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def crm_unit_param_get_by_id(self):
        response = self.client.get(
            url_for(
                "crmunitparam.find_by_id", id=self.get_id_fixed("crm_unit_param_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def crm_unit_param_delete(self):
        response = self.client.delete(
            url_for("crmunitparam.delete", id=self.get_id_fixed("crm_unit_param_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # crm_aviso_org
    # ===========================================================

    # ====================

    def crm_aviso_org_id1(self):

        req_post = {
            "id": self.get_id_fixed("crm_aviso_org_id1"),
            "crm_aviso_id": module_tests_crm.crm_aviso_id1(self),
            "crm_org_id": module_tests_crm.crm_org_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("crmavisoorg.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_aviso_org_id2(self):

        req_post = {
            "id": self.get_id_fixed("crm_aviso_org_id2"),
            "crm_aviso_id": module_tests_crm.crm_aviso_id1(self),
            "crm_org_id": module_tests_crm.crm_org_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("crmavisoorg.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_aviso_org_get(self):
        response = self.client.get(
            url_for("crmavisoorg.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def crm_aviso_org_get_by_id(self):
        response = self.client.get(
            url_for(
                "crmavisoorg.find_by_id", id=self.get_id_fixed("crm_aviso_org_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def crm_aviso_org_delete(self):
        response = self.client.delete(
            url_for("crmavisoorg.delete", id=self.get_id_fixed("crm_aviso_org_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # crm_chat_msg
    # ===========================================================

    # ====================

    def crm_chat_msg_id1(self):

        req_post = {
            "id": self.get_id_fixed("crm_chat_msg_id1"),
            "corpo": "TESTE [CRUD]",
            "crm_chat_grupo_id": module_tests_crm.crm_chat_grupo_id1(self),
            "data_msg": "2022-12-29T00:00:00",
            "sys_user_id_orig": module_tests_sys.module_tests_sys.sys_user_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("crmchatmsg.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_chat_msg_id2(self):

        req_post = {
            "id": self.get_id_fixed("crm_chat_msg_id2"),
            "corpo": "TESTE [CRUD]",
            "crm_chat_grupo_id": module_tests_crm.crm_chat_grupo_id1(self),
            "data_msg": "2022-12-29T00:00:00",
            "sys_user_id_orig": module_tests_sys.module_tests_sys.sys_user_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("crmchatmsg.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_chat_msg_get(self):
        response = self.client.get(
            url_for("crmchatmsg.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def crm_chat_msg_get_by_id(self):
        response = self.client.get(
            url_for("crmchatmsg.find_by_id", id=self.get_id_fixed("crm_chat_msg_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def crm_chat_msg_delete(self):
        response = self.client.delete(
            url_for("crmchatmsg.delete", id=self.get_id_fixed("crm_chat_msg_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # crm_etapa_prox
    # ===========================================================

    # ====================

    def crm_etapa_prox_id1(self):

        req_post = {
            "id": self.get_id_fixed("crm_etapa_prox_id1"),
            "crm_etapa_id": module_tests_crm.crm_etapa_id1(self),
            "crm_etapa_id_prox": module_tests_crm.crm_etapa_id1(self),
            "ordem": "1",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("crmetapaprox.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_etapa_prox_id2(self):

        req_post = {
            "id": self.get_id_fixed("crm_etapa_prox_id2"),
            "crm_etapa_id": module_tests_crm.crm_etapa_id1(self),
            "crm_etapa_id_prox": module_tests_crm.crm_etapa_id1(self),
            "ordem": "1",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("crmetapaprox.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_etapa_prox_get(self):
        response = self.client.get(
            url_for("crmetapaprox.find_all"), headers=self.create_token()
        )
        result = len(response.json) > 0
        self.assertTrue(result)

    # ====================

    def crm_etapa_prox_get_by_id(self):
        response = self.client.get(
            url_for(
                "crmetapaprox.find_by_id", id=self.get_id_fixed("crm_etapa_prox_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def crm_etapa_prox_delete(self):
        response = self.client.delete(
            url_for("crmetapaprox.delete", id=self.get_id_fixed("crm_etapa_prox_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # crm_mov
    # ===========================================================

    # ====================

    def crm_mov_id1(self):

        req_post = {
            "id": self.get_id_fixed("crm_mov_id1"),
            "crm_etapa_id": module_tests_crm.crm_etapa_id1(self),
            "crm_prioridade_id": module_tests_crm.crm_prioridade_id1(self),
            "crm_status_id": module_tests_crm.crm_status_id1(self),
            "data_mov": "07/07/2022",
            "data_status": "07/07/2022",
            "descritivo_ext": "t",
            "descritivo_int": "t",
            "envia_email_ext": "S",
            "numero": "5",
            "sys_user_id_atend_ant": module_tests_sys.module_tests_sys.sys_user_id1(
                self
            ),
            "sys_user_id_atend_atu": module_tests_sys.module_tests_sys.sys_user_id1(
                self
            ),
            "sys_user_id_solic": module_tests_sys.module_tests_sys.sys_user_id1(self),
            "titulo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("crmmov.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_mov_id2(self):

        req_post = {
            "id": self.get_id_fixed("crm_mov_id2"),
            "crm_etapa_id": module_tests_crm.crm_etapa_id1(self),
            "crm_prioridade_id": module_tests_crm.crm_prioridade_id1(self),
            "crm_status_id": module_tests_crm.crm_status_id1(self),
            "data_mov": "07/07/2022",
            "data_status": "07/07/2022",
            "descritivo_ext": "t",
            "descritivo_int": "t",
            "envia_email_ext": "S",
            "numero": "5",
            "sys_user_id_atend_ant": module_tests_sys.module_tests_sys.sys_user_id1(
                self
            ),
            "sys_user_id_atend_atu": module_tests_sys.module_tests_sys.sys_user_id1(
                self
            ),
            "sys_user_id_solic": module_tests_sys.module_tests_sys.sys_user_id1(self),
            "titulo": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("crmmov.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_mov_get(self):
        response = self.client.get(
            url_for("crmmov.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def crm_mov_get_by_id(self):
        response = self.client.get(
            url_for("crmmov.find_by_id", id=self.get_id_fixed("crm_mov_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def crm_mov_delete(self):
        response = self.client.delete(
            url_for("crmmov.delete", id=self.get_id_fixed("crm_mov_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # crm_class
    # ===========================================================

    # ====================

    def crm_class_id1(self):

        module_tests_crm.crm_class_grupo_id2(self)

        req_post = {
            "id": self.get_id_fixed("crm_class_id1"),
            "crm_class_subgrupo_id": self.get_id_fixed("crm_class_subgrupo_id2"),
            "nome": "TESTE [CRUD]",
            "sigla_class": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("crmclass.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_class_id2(self):

        module_tests_crm.crm_class_grupo_id2(self)
        req_post = {
            "id": self.get_id_fixed("crm_class_id2"),
            "crm_class_subgrupo_id": self.get_id_fixed("crm_class_subgrupo_id2"),
            "nome": "TESTE [CRUD]",
            "sigla_class": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("crmclass.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_class_get(self):
        response = self.client.get(
            url_for("crmclass.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def crm_class_get_by_id(self):
        response = self.client.get(
            url_for("crmclass.find_by_id", id=self.get_id_fixed("crm_class_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def crm_class_delete(self):
        response = self.client.delete(
            url_for("crmclass.delete", id=self.get_id_fixed("crm_class_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # crm_mov_hist
    # ===========================================================

    # ====================

    def crm_mov_hist_id1(self):

        req_post = {
            "id": self.get_id_fixed("crm_mov_hist_id1"),
            "crm_mov_id": module_tests_crm.crm_mov_id1(self),
            "data_hist": "29/05/2022",
            "descritivo": "TESTE [CRUD]",
            "envia_email_ext": "S",
            "sys_user_id_hist": module_tests_sys.module_tests_sys.sys_user_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "visual_ext": "S",
        }

        response = self.client.post(
            url_for("crmmovhist.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_mov_hist_id2(self):

        req_post = {
            "id": self.get_id_fixed("crm_mov_hist_id2"),
            "crm_mov_id": module_tests_crm.crm_mov_id1(self),
            "data_hist": "29/05/2022",
            "descritivo": "TESTE [CRUD]",
            "envia_email_ext": "S",
            "sys_user_id_hist": module_tests_sys.module_tests_sys.sys_user_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "visual_ext": "S",
        }

        response = self.client.post(
            url_for("crmmovhist.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_mov_hist_get(self):
        response = self.client.get(
            url_for("crmmovhist.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def crm_mov_hist_get_by_id(self):
        response = self.client.get(
            url_for("crmmovhist.find_by_id", id=self.get_id_fixed("crm_mov_hist_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def crm_mov_hist_delete(self):
        response = self.client.delete(
            url_for("crmmovhist.delete", id=self.get_id_fixed("crm_mov_hist_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # crm_mov_tag
    # ===========================================================

    # ====================

    def crm_mov_tag_id1(self):

        req_post = {
            "id": self.get_id_fixed("crm_mov_tag_id1"),
            "crm_mov_id": module_tests_crm.crm_mov_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("crmmovtag.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_mov_tag_id2(self):

        req_post = {
            "id": self.get_id_fixed("crm_mov_tag_id2"),
            "crm_mov_id": module_tests_crm.crm_mov_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("crmmovtag.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def crm_mov_tag_get(self):
        response = self.client.get(
            url_for("crmmovtag.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def crm_mov_tag_get_by_id(self):
        response = self.client.get(
            url_for("crmmovtag.find_by_id", id=self.get_id_fixed("crm_mov_tag_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def crm_mov_tag_delete(self):
        response = self.client.delete(
            url_for("crmmovtag.delete", id=self.get_id_fixed("crm_mov_tag_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)
