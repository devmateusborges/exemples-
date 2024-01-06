from flask import url_for

from generic_tests import generic_tests

import module_tests_ope
import module_tests_sys


class module_tests_bor(generic_tests):

    # ===========================================================
    # bor_unit_param
    # ===========================================================

    # ====================

    def bor_unit_param_id1(self):

        req_post = {
            "id": self.get_id_fixed("bor_unit_param_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_valid_ini": "2022-12-29T00:00:00",
        }

        response = self.client.post(
            url_for("borunitparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def bor_unit_param_id2(self):

        req_post = {
            "id": self.get_id_fixed("bor_unit_param_id2"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_valid_ini": "2022-12-29T00:00:00",
        }

        response = self.client.post(
            url_for("borunitparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def bor_unit_param_get(self):
        response = self.client.get(
            url_for("borunitparam.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def bor_unit_param_get_by_id(self):
        response = self.client.get(
            url_for(
                "borunitparam.find_by_id", id=self.get_id_fixed("bor_unit_param_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def bor_unit_param_delete(self):
        response = self.client.delete(
            url_for("borunitparam.delete", id=self.get_id_fixed("bor_unit_param_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # bor_dispositivo
    # ===========================================================

    # ====================

    def bor_dispositivo_id1(self):

        req_post = {
            "id": self.get_id_fixed("bor_dispositivo_id1"),
            "nome": "TESTE [CRUD]",
            "numero_serie": "1",
            "tipo": "2",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ope_centro2_pessoa_id": module_tests_ope.module_tests_ope.ope_centro2_pessoa_id1(
                self
            ),
            "ope_centro2_equip_id": module_tests_ope.module_tests_ope.ope_centro2_equip_id1(
                self
            ),
        }

        response = self.client.post(
            url_for("bordispositivo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def bor_dispositivo_id2(self):

        req_post = {
            "id": self.get_id_fixed("bor_dispositivo_id2"),
            "nome": "TESTE [CRUD]",
            "numero_serie": "2",
            "tipo": "2",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ope_centro2_pessoa_id": module_tests_ope.module_tests_ope.ope_centro2_pessoa_id1(
                self
            ),
            "ope_centro2_equip_id": module_tests_ope.module_tests_ope.ope_centro2_equip_id1(
                self
            ),
        }

        response = self.client.post(
            url_for("bordispositivo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def bor_dispositivo_get(self):
        response = self.client.get(
            url_for("bordispositivo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def bor_dispositivo_get_by_id(self):
        response = self.client.get(
            url_for(
                "bordispositivo.find_by_id", id=self.get_id_fixed("bor_dispositivo_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def bor_dispositivo_delete(self):
        response = self.client.delete(
            url_for(
                "bordispositivo.delete", id=self.get_id_fixed("bor_dispositivo_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)
