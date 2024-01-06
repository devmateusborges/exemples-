from flask import url_for


from generic_tests import generic_tests
import module_tests_sys


class module_tests_pto(generic_tests):

    # ===========================================================
    # pto_marcacao
    # ===========================================================

    # ====================

    def pto_marcacao_id1(self):

        req_post = {
            "id": self.get_id_fixed("pto_marcacao_id1"),
            "marc_ano": "29",
            "marc_data": "2022-05-19 09:44:48.000",
            "marc_dia": "2",
            "marc_hora": "2",
            "marc_mes": "2",
            "marc_minuto": "55",
            "process_id": module_tests_sys.module_tests_sys.sys_process_log_id1(self),
            "pto_medidor_id": module_tests_pto.pto_medidor_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("ptomarcacao.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def pto_marcacao_id2(self):

        req_post = {
            "id": self.get_id_fixed("pto_marcacao_id2"),
            "marc_ano": "29",
            "marc_data": "2022-05-19 09:44:48.000",
            "marc_dia": "2",
            "marc_hora": "2",
            "marc_mes": "2",
            "marc_minuto": "55",
            "process_id": module_tests_sys.module_tests_sys.sys_process_log_id1(self),
            "pto_medidor_id": module_tests_pto.pto_medidor_id1(self),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("ptomarcacao.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def pto_marcacao_get(self):
        response = self.client.get(
            url_for("ptomarcacao.find_all"), headers=self.create_token()
        )
        result = len(response.json) > 0
        self.assertTrue(result)

    # ====================

    def pto_marcacao_get_by_id(self):
        response = self.client.get(
            url_for("ptomarcacao.find_by_id", id=self.get_id_fixed("pto_marcacao_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def pto_marcacao_delete(self):
        response = self.client.delete(
            url_for("ptomarcacao.delete", id=self.get_id_fixed("pto_marcacao_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # pto_medidor
    # ===========================================================

    # ====================

    def pto_medidor_id1(self):

        req_post = {
            "id": self.get_id_fixed("pto_medidor_id1"),
            "nome": "TESTE [CRUD]",
            "sigla_medidor": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "S",
        }

        response = self.client.post(
            url_for("ptomedidor.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def pto_medidor_id2(self):

        req_post = {
            "id": self.get_id_fixed("pto_medidor_id2"),
            "nome": "TESTE [CRUD]",
            "sigla_medidor": "TESTE [CRUD]",
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "ativo": "S",
        }

        response = self.client.post(
            url_for("ptomedidor.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def pto_medidor_get(self):
        response = self.client.get(
            url_for("ptomedidor.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def pto_medidor_get_by_id(self):
        response = self.client.get(
            url_for("ptomedidor.find_by_id", id=self.get_id_fixed("pto_medidor_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def pto_medidor_delete(self):
        response = self.client.delete(
            url_for("ptomedidor.delete", id=self.get_id_fixed("pto_medidor_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # pto_unit_param
    # ===========================================================

    # ====================

    def pto_unit_param_id1(self):

        req_post = {
            "id": self.get_id_fixed("pto_unit_param_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_valid_ini": "2022-12-29T00:00:00",
        }

        response = self.client.post(
            url_for("ptounitparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def pto_unit_param_id2(self):

        req_post = {
            "id": self.get_id_fixed("pto_unit_param_id2"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_valid_ini": "2022-12-29T00:00:00",
        }

        response = self.client.post(
            url_for("ptounitparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def pto_unit_param_get(self):
        response = self.client.get(
            url_for("ptounitparam.find_all"), headers=self.create_token()
        )
        result = len(response.json) > 0
        self.assertTrue(result)

    # ====================

    def pto_unit_param_get_by_id(self):
        response = self.client.get(
            url_for(
                "ptounitparam.find_by_id", id=self.get_id_fixed("pto_unit_param_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def pto_unit_param_delete(self):
        response = self.client.delete(
            url_for("ptounitparam.delete", id=self.get_id_fixed("pto_unit_param_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)
