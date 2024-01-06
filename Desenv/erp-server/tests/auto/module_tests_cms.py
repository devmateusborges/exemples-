from flask import url_for
from generic_tests import generic_tests
import module_tests_sys


class module_tests_cms(generic_tests):

    # ===========================================================
    #  cms_grupo
    # ===========================================================

    # ====================

    def cms_grupo_id1(self):

        req_post = {
            "id": self.get_id_fixed("cms_grupo_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "sigla_grupo": "TESTE [CRUD]",
            "publico": "S",
            "ativo": "S",
            "nome": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("cmsgrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def cms_grupo_id2(self):

        req_post = {
            "id": self.get_id_fixed("cms_grupo_id2"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "sigla_grupo": "TESTE [CRUD]",
            "publico": "S",
            "ativo": "S",
            "nome": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("cmsgrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def cms_grupo_get(self):
        response = self.client.get(
            url_for("cmsgrupo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def cms_grupo_get_by_id(self):
        response = self.client.get(
            url_for("cmsgrupo.find_by_id", id=self.get_id_fixed("cms_grupo_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def cms_grupo_delete(self):
        response = self.client.delete(
            url_for("cmsgrupo.delete", id=self.get_id_fixed("cms_grupo_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  cms_post
    # ===========================================================

    # ====================

    def cms_post_id1(self):

        req_post = {
            "id": self.get_id_fixed("cms_post_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "titulo": "TESTE [CRUD]",
            "tipo_render": "M",
            "favorito": "S",
            "status": "C",
            "sys_user_id": module_tests_sys.module_tests_sys.sys_user_id1(self),
            "util_blog": "S",
            "util_depoimento": "S",
            "corpo": "TESTE [CRUD]",
            "util_help": "S",
            "util_treinamento": "S",
        }

        response = self.client.post(
            url_for("cmspost.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def cms_post_id2(self):

        req_post = {
            "id": self.get_id_fixed("cms_post_id2"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "titulo": "TESTE [CRUD]",
            "tipo_render": "M",
            "favorito": "S",
            "status": "C",
            "sys_user_id": module_tests_sys.module_tests_sys.sys_user_id1(self),
            "util_blob": "S",
            "util_depoimento": "S",
            "corpo": "TESTE [CRUD]",
            "util_help": "S",
            "util_treinamento": "S",
        }

        response = self.client.post(
            url_for("cmspost.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def cms_post_get(self):
        response = self.client.get(
            url_for("cmspost.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def cms_post_get_by_id(self):
        response = self.client.get(
            url_for("cmspost.find_by_id", id=self.get_id_fixed("cms_post_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def cms_post_delete(self):
        response = self.client.delete(
            url_for("cmspost.delete", id=self.get_id_fixed("cms_post_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  cms_post_hist
    # ===========================================================

    # ====================

    def cms_post_hist_id1(self):

        req_post = {
            "id": self.get_id_fixed("cms_post_hist_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "descricao": "F",
            "tipo_hist": "V",
            "cms_post_id": module_tests_cms.cms_post_id1(self),
            "data_hist": "15/05/2001",
        }

        response = self.client.post(
            url_for("cmsposthist.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def cms_post_hist_id2(self):

        req_post = {
            "id": self.get_id_fixed("cms_post_hist_id2"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "descricao": "F",
            "tipo_hist": "V",
            "cms_post_id": module_tests_cms.cms_post_id1(self),
            "data_hist": "15/05/2001",
        }

        response = self.client.post(
            url_for("cmsposthist.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def cms_post_hist_get(self):
        response = self.client.get(
            url_for("cmsposthist.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def cms_post_hist_get_by_id(self):
        response = self.client.get(
            url_for(
                "cmsposthist.find_by_id", id=self.get_id_fixed("cms_post_hist_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def cms_post_hist_delete(self):
        response = self.client.delete(
            url_for("cmsposthist.delete", id=self.get_id_fixed("cms_post_hist_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  cms_tag
    # ===========================================================

    # ====================

    def cms_tag_id1(self):

        req_post = {
            "id": self.get_id_fixed("cms_tag_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "nome": "TESTE [CRUD]",
            "sigla_tag": "TESTE [CRUD]",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("cmstag.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def cms_tag_id2(self):

        req_post = {
            "id": self.get_id_fixed("cms_tag_id2"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "nome": "TESTE [CRUD]",
            "sigla_tag": "TESTE [CRUD]",
            "ativo": "S",
        }

        response = self.client.post(
            url_for("cmstag.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def cms_tag_get(self):

        response = self.client.get(
            url_for("cmstag.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def cms_tag_get_by_id(self):
        response = self.client.get(
            url_for("cmstag.find_by_id", id=self.get_id_fixed("cms_tag_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def cms_tag_delete(self):
        response = self.client.delete(
            url_for("cmstag.delete", id=self.get_id_fixed("cms_tag_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)
