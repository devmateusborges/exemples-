from flask import url_for


from generic_tests import generic_tests
import module_tests_sys


class module_tests_rhm(generic_tests):

    # ===========================================================
    # rhm_unit_param
    # ===========================================================

    # ====================

    def rhm_unit_param_id1(self):

        req_post = {
            "id": self.get_id_fixed("rhm_unit_param_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_valid_ini": "2022-12-29T00:00:00",
        }

        response = self.client.post(
            url_for("rhmunitparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def rhm_unit_param_id2(self):

        req_post = {
            "id": self.get_id_fixed("rhm_unit_param_id1"),
            "unit_id": module_tests_sys.module_tests_sys.sys_unit_id1(self),
            "data_valid_ini": "2022-12-29T00:00:00",
        }

        response = self.client.post(
            url_for("rhmunitparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def rhm_unit_param_get(self):
        response = self.client.get(
            url_for("rhmunitparam.find_all"), headers=self.create_token()
        )
        result = len(response.json) > 0
        self.assertTrue(result, "rhm_unit_param_002 code 200")

    # ====================

    def rhm_unit_param_get_by_id(self):
        response = self.client.get(
            url_for(
                "rhmunitparam.find_by_id", id=self.get_id_fixed("rhm_unit_param_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200, "rhm_unit_param_001 code 200")

    # ====================

    def rhm_unit_param_delete(self):
        response = self.client.delete(
            url_for("rhmunitparam.delete", id=self.get_id_fixed("rhm_unit_param_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204, "rhm_unit_param_001 code 204")
