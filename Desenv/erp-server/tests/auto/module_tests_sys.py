import base64
import json
import os
import uuid

from flask import url_for
from generic_tests import generic_tests


import module_tests_fin
import module_tests_ger
import module_tests_mov
import module_tests_cms
import module_tests_ope
import module_tests_crm
import module_tests_ind


class module_tests_sys(generic_tests):

    # ===========================================================
    # sys_unit
    # ===========================================================

    # ====================

    def sys_unit_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_unit_id1"),
            "active": "S",
            "name": "Test1",
            "code_unit": "TESTE  1 [CRUD]",
            "sys_unit_manager_id": module_tests_sys.sys_unit_manager_id1(self),
        }

        response = self.client.post(
            url_for("sysunit.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_unit_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_unit_id2"),
            "active": "S",
            "name": "Test2",
            "code_unit": "TESTE  2 [CRUD]",
            "sys_unit_manager_id": module_tests_sys.sys_unit_manager_id1(self),
        }

        response = self.client.post(
            url_for("sysunit.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_unit_get(self):
        response = self.client.get(
            url_for("sysunit.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_unit_get_by_id(self):
        response = self.client.get(
            url_for("sysunit.find_by_id", id=self.get_id_fixed("sys_unit_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_unit_delete(self):
        response = self.client.delete(
            url_for("sysunit.delete", id=self.get_id_fixed("sys_unit_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_user
    # ===========================================================

    # ====================

    def sys_user_id1(self):
        module_tests_sys.sys_translate_lang_id1(self)
        req_post = {
            "id": self.get_id_fixed("sys_user_id1"),
            "active": "S",
            "email": "USERTESTE1@admin.com",
            "login": "USERTESTE1",
            "name": "USER TESTE 1 - DEV",
            "password": "123",
            "active_message": "S",
            "admin": "S",
            "chat": "S",
            "document": "S",
            "email_verified": "S",
            "image_url": "S",
            "login_ext": "S",
            "origem": "1",
            "phone": "S",
            "provider": "S",
            "provider_code": "S",
            "gtm_default": "TESTE 1",
            "sys_tran_lang_id_default": module_tests_sys.sys_translate_lang_id1(self),
        }

        response = self.client.post(
            url_for("sysuser.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_user_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_user_id2"),
            "active": "S",
            "email": "USERTESTE2@admin.com",
            "login": "USERTESTE2",
            "name": "USER TESTE 2 - DEV",
            "password": "123",
            "active_message": "S",
            "admin": "S",
            "chat": "S",
            "document": "S",
            "email_verified": "S",
            "image_url": "S",
            "login_ext": "S",
            "origem": "1",
            "phone": "S",
            "provider": "S",
            "provider_code": "S",
            "gtm_default": "TESTE 2",
            "sys_tran_lang_id_default": module_tests_sys.sys_translate_lang_id1(self),
        }

        response = self.client.post(
            url_for("sysuser.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_user_get(self):
        response = self.client.get(
            url_for("sysuser.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================
    def sys_user_get_by_id(self):
        response = self.client.get(
            url_for("sysuser.find_by_id", id=self.get_id_fixed("sys_user_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================
    def sys_user_delete(self):
        response = self.client.delete(
            url_for("sysuser.delete", id=self.get_id_fixed("sys_user_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys
    # ===========================================================

    # ====================

    def sys_id1(self):
        req_post = {
            "id": self.get_id_fixed("sys_id1"),
            "name": "SYSTEMA TESTS 1 - DEV",
            "code_sys": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("sys.save"), json=req_post, headers=self.create_token()
        )
        id = str(self.get_id_response(response))
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_id2(self):
        req_post = {
            "id": self.get_id_fixed("sys_id2"),
            "name": "SYSTEMA TESTS 2 - DEV",
            "code_sys": "TESTE 2 [CRUD]",
        }

        response = self.client.post(
            url_for("sys.save"), json=req_post, headers=self.create_token()
        )
        id = str(self.get_id_response(response))
        self.assertEqual(response.status_code, 201)
        return id

    # ====================
    def sys_get(self):
        response = self.client.get(url_for("sys.find_all"), headers=self.create_token())
        self.assertEqual(response.status_code, 200, response.json)

    # ====================
    def sys_get_by_id(self):
        response = self.client.get(
            url_for("sys.find_by_id", id=self.get_id_fixed("sys_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================
    def sys_delete(self):
        response = self.client.delete(
            url_for("sys.delete", id=self.get_id_fixed("sys_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_document_category
    # ===========================================================

    # ====================
    def sys_document_category_id1(self):
        req_post = {
            "id": self.get_id_fixed("sys_document_category_id1"),
            "active": "S",
            "name": "TESTE  1 [CRUD]",
            "code_document_category": "TESTE  1 [CRUD]",
        }
        response = self.client.post(
            url_for("sysdocumentcategory.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = str(self.get_id_response(response))
        self.assertEqual(response.status_code, 201)
        return id

    # ====================
    def sys_document_category_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_document_category_id2"),
            "active": "S",
            "name": "TESTE  2 [CRUD]",
            "code_document_category": "TESTE  2 [CRUD]",
        }
        response = self.client.post(
            url_for("sysdocumentcategory.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_document_category_get(self):
        response = self.client.get(
            url_for("sysdocumentcategory.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_document_category_get_by_id(self):
        response = self.client.get(
            url_for(
                "sysdocumentcategory.find_by_id",
                id=self.get_id_fixed("sys_document_category_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_document_category_delete(self):
        response = self.client.delete(
            url_for(
                "sysdocumentcategory.delete",
                id=self.get_id_fixed("sys_document_category_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_group
    # ===========================================================

    def sys_group_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_group_id1"),
            "name": "TST",
            "active": "S",
            "code_group": "TESTE  1 [CRUD]",
            "sys_group_program_childs": [
                {
                    "id": self.get_id_fixed("sys_group_program_id1"),
                    "sys_program_id": module_tests_sys.sys_program_id1(self),
                }
            ],
        }

        response = self.client.post(
            url_for("sysgroup.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_group_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_group_id2"),
            "name": "TST",
            "active": "S",
            "code_group": "TESTE  2 [CRUD]",
            "sys_group_program_childs": [
                {"sys_program_id": module_tests_sys.sys_program_id1(self)}
            ],
        }

        response = self.client.post(
            url_for("sysgroup.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_group_get(self):
        response = self.client.get(
            url_for("sysgroup.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_group_get_by_id(self):
        response = self.client.get(
            url_for("sysgroup.find_by_id", id=self.get_id_fixed("sys_group_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_group_delete(self):
        response = self.client.delete(
            url_for("sysgroup.delete", id=self.get_id_fixed("sys_group_id2")),
            headers=self.create_token(),
        )
        print(response.data)
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_document_group
    # ===========================================================:module_tests_sys.sys

    # ====================
    def sys_document_group_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_document_group_id1"),
            "document_fk_id": module_tests_sys.sys_document_id1(self),
            "sys_group_fk_id": module_tests_sys.sys_group_id1(self),
            "code_document": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("sysdocumentgroup.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_document_group_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_document_group_id2"),
            "document_fk_id": module_tests_sys.sys_document_id1(self),
            "sys_group_fk_id": module_tests_sys.sys_group_id1(self),
            "code_document": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("sysdocumentgroup.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_document_group_get(self):
        response = self.client.get(
            url_for("sysdocumentgroup.find_all"), headers=self.create_token()
        )
        result = len(response.json) > 0
        self.assertTrue(result)

    # ====================

    def sys_document_group_get_by_id(self):
        response = self.client.get(
            url_for(
                "sysdocumentgroup.find_by_id",
                id=self.get_id_fixed("sys_document_group_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_document_group_delete(self):
        response = self.client.delete(
            url_for(
                "sysdocumentgroup.delete",
                id=self.get_id_fixed("sys_document_group_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_Document
    # ===========================================================

    # ====================

    def sys_document_id1(self):
        req_post = {
            "id": self.get_id_fixed("sys_document_id1"),
            "title": "TESTE  1 [CRUD]",
            "submission_date": "12/05/2022",
            "description": "S",
            "archive_date": "12/05/2022",
            "active": "S",
            "filename": "teste2.txt",
            "content_type": "TXT",
            "code_document": "TESTE  1 [CRUD]",
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "sys_category_id": module_tests_sys.sys_document_category_id1(self),
            "fin_pagrec_id": module_tests_fin.module_tests_fin.fin_pagrec_id1(self),
            "ger_pessoa_id": module_tests_ger.module_tests_ger.ger_pessoa_id1(self),
            "crm_mov_id": module_tests_crm.module_tests_crm.crm_mov_id1(self),
            "ope_centro2_id": module_tests_ope.module_tests_ope.ope_centro2_id1(self),
            "ope_compart_ocor_id": module_tests_ope.module_tests_ope.ope_compart_ocor_id1(
                self
            ),
            "ope_ocor_id": module_tests_ope.module_tests_ope.ope_ocor_id1(self),
            "ope_centro1_id": module_tests_ope.module_tests_ope.ope_centro1_id1(self),
            "ope_centro2_ord_id": module_tests_ope.module_tests_ope.ope_centro2_ord_id1(
                self
            ),
            "ope_compart_id": module_tests_ope.module_tests_ope.ope_compart_id1(self),
            "mov_id": module_tests_mov.module_tests_mov.mov_id1(self),
        }

        response = self.client.post(
            url_for("sysdocument.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_document_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_document_id2"),
            "title": "TESTE  2 [CRUD]",
            "submission_date": "12/05/2022",
            "description": "S",
            "archive_date": "12/05/2022",
            "active": "S",
            "filename": "teste2.txt",
            "content_type": "TXT",
            "code_document": "TESTE  2 [CRUD]",
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "sys_category_id": module_tests_sys.sys_document_category_id1(self),
            "fin_pagrec_id": module_tests_fin.module_tests_fin.fin_pagrec_id1(self),
            "ger_pessoa_id": module_tests_ger.module_tests_ger.ger_pessoa_id1(self),
            "crm_mov_id": module_tests_crm.module_tests_crm.crm_mov_id1(self),
            "ope_centro2_id": module_tests_ope.module_tests_ope.ope_centro2_id1(self),
            "ope_compart_ocor_id": module_tests_ope.module_tests_ope.ope_compart_ocor_id1(
                self
            ),
            "ope_ocor_id": module_tests_ope.module_tests_ope.ope_ocor_id1(self),
            "ope_centro1_id": module_tests_ope.module_tests_ope.ope_centro1_id1(self),
            "ope_centro2_ord_id": module_tests_ope.module_tests_ope.ope_centro2_ord_id1(
                self
            ),
            "ope_compart_id": module_tests_ope.module_tests_ope.ope_compart_id1(self),
            "mov_id": module_tests_mov.module_tests_mov.mov_id1(self),
        }

        response = self.client.post(
            url_for("sysdocument.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_document_get(self):
        response = self.client.get(
            url_for("sysdocument.find_all"), headers=self.create_token()
        )
        result = len(response.json) > 0
        self.assertTrue(result)

    # ====================

    def sys_document_get_by_id(self):
        response = self.client.get(
            url_for("sysdocument.find_by_id", id=self.get_id_fixed("sys_document_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_document_delete(self):
        response = self.client.delete(
            url_for("sysdocument.delete", id=self.get_id_fixed("sys_document_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_document_upload extends sys_document
    # ===========================================================

    # ====================

    def sys_document_create1_PDF(self):

        req_post = {
            "id": self.get_id_fixed("sys_document_pdf_id1"),
            "title": "TSTPDF",
            "submission_date": "12/05/2022",
            "filename": "test1.pdf",
            "content_type": "PDF",
            "description": "S",
            "active": "S",
            "archive_date": "12/05/2022",
            "code_document": "TSTPDF",
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "sys_category_id": module_tests_sys.sys_document_category_id1(self),
            "fin_pagrec_id": module_tests_fin.module_tests_fin.fin_pagrec_id1(self),
            "ger_pessoa_id": module_tests_ger.module_tests_ger.ger_pessoa_id1(self),
            "crm_mov_id": module_tests_crm.module_tests_crm.crm_mov_id1(self),
            "ope_centro2_id": module_tests_ope.module_tests_ope.ope_centro2_id1(self),
            "ope_compart_ocor_id": module_tests_ope.module_tests_ope.ope_compart_ocor_id1(
                self
            ),
            "ope_ocor_id": module_tests_ope.module_tests_ope.ope_ocor_id1(self),
            "ope_centro1_id": module_tests_ope.module_tests_ope.ope_centro1_id1(self),
            "ope_centro2_ord_id": module_tests_ope.module_tests_ope.ope_centro2_ord_id1(
                self
            ),
            "ope_compart_id": module_tests_ope.module_tests_ope.ope_compart_id1(self),
            "mov_id": module_tests_mov.module_tests_mov.mov_id1(self),
        }

        response = self.client.post(
            url_for("sysdocument.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_document_create_zip(self):

        req_post = {
            "id": self.get_id_fixed("sys_document_zip_id1"),
            "title": "TSTZIP",
            "submission_date": "12/05/2022",
            "filename": "test2.zip",
            "content_type": "ZIP",
            "description": "S",
            "active": "S",
            "code_document": "TSTZIP",
            "archive_date": "12/05/2022",
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "sys_category_id": module_tests_sys.sys_document_category_id1(self),
            "fin_pagrec_id": module_tests_fin.module_tests_fin.fin_pagrec_id1(self),
            "ger_pessoa_id": module_tests_ger.module_tests_ger.ger_pessoa_id1(self),
            "crm_mov_id": module_tests_crm.module_tests_crm.crm_mov_id1(self),
            "ope_centro2_id": module_tests_ope.module_tests_ope.ope_centro2_id1(self),
            "ope_compart_ocor_id": module_tests_ope.module_tests_ope.ope_compart_ocor_id1(
                self
            ),
            "ope_ocor_id": module_tests_ope.module_tests_ope.ope_ocor_id1(self),
            "ope_centro1_id": module_tests_ope.module_tests_ope.ope_centro1_id1(self),
            "ope_centro2_ord_id": module_tests_ope.module_tests_ope.ope_centro2_ord_id1(
                self
            ),
            "ope_compart_id": module_tests_ope.module_tests_ope.ope_compart_id1(self),
            "mov_id": module_tests_mov.module_tests_mov.mov_id1(self),
        }

        response = self.client.post(
            url_for("sysdocument.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_document_create_xlsx(self):

        req_post = {
            "id": self.get_id_fixed("sys_document_xlsx_id1"),
            "title": "TSTXLSX",
            "submission_date": "12/05/2022",
            "filename": "test3.xlsx",
            "content_type": "XLSX",
            "description": "S",
            "active": "S",
            "archive_date": "12/05/2022",
            "code_document": "TSTXLSX",
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "sys_category_id": module_tests_sys.sys_document_category_id1(self),
            "fin_pagrec_id": module_tests_fin.module_tests_fin.fin_pagrec_id1(self),
            "ger_pessoa_id": module_tests_ger.module_tests_ger.ger_pessoa_id1(self),
            "crm_mov_id": module_tests_crm.module_tests_crm.crm_mov_id1(self),
            "ope_centro2_id": module_tests_ope.module_tests_ope.ope_centro2_id1(self),
            "ope_compart_ocor_id": module_tests_ope.module_tests_ope.ope_compart_ocor_id1(
                self
            ),
            "ope_ocor_id": module_tests_ope.module_tests_ope.ope_ocor_id1(self),
            "ope_centro1_id": module_tests_ope.module_tests_ope.ope_centro1_id1(self),
            "ope_centro2_ord_id": module_tests_ope.module_tests_ope.ope_centro2_ord_id1(
                self
            ),
            "ope_compart_id": module_tests_ope.module_tests_ope.ope_compart_id1(self),
            "mov_id": module_tests_mov.module_tests_mov.mov_id1(self),
        }

        response = self.client.post(
            url_for("sysdocument.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_document_create_txt(self):
        req_post = {
            "id": self.get_id_fixed("sys_document_txt_id1"),
            "title": "TST",
            "submission_date": "12/05/2022",
            "filename": "test4.txt",
            "content_type": "TXT",
            "description": "S",
            "active": "S",
            "archive_date": "12/05/2022",
            "code_document": "TSTTXT",
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "sys_category_id": module_tests_sys.sys_document_category_id1(self),
            "fin_pagrec_id": module_tests_fin.module_tests_fin.fin_pagrec_id1(self),
            "ger_pessoa_id": module_tests_ger.module_tests_ger.ger_pessoa_id1(self),
            "crm_mov_id": module_tests_crm.module_tests_crm.crm_mov_id1(self),
            "ope_centro2_id": module_tests_ope.module_tests_ope.ope_centro2_id1(self),
            "ope_compart_ocor_id": module_tests_ope.module_tests_ope.ope_compart_ocor_id1(
                self
            ),
            "ope_ocor_id": module_tests_ope.module_tests_ope.ope_ocor_id1(self),
            "ope_centro1_id": module_tests_ope.module_tests_ope.ope_centro1_id1(self),
            "ope_centro2_ord_id": module_tests_ope.module_tests_ope.ope_centro2_ord_id1(
                self
            ),
            "ope_compart_id": module_tests_ope.module_tests_ope.ope_compart_id1(self),
            "mov_id": module_tests_mov.module_tests_mov.mov_id1(self),
        }

        response = self.client.post(
            url_for("sysdocument.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ===========================================================

    def sys_document_upload_pdf(self):
        dir_test = os.path.dirname(__file__)
        path_test = os.path.join(dir_test, "uploads" + os.sep + "test1.pdf")
        id = self.get_id_fixed("sys_document_pdf_id1")
        with open(path_test, "rb") as file:
            tostring = base64.b64encode(file.read())
            file.close()
        req_post = {
            "file_content_type": "PDF",
            "filename": "test1.pdf",
            "file_64": tostring.decode(),
        }
        response = self.client.post(
            url_for("sysdocument.post_file", id=id),
            json=req_post,
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 201)

    # ====================

    def sys_document_upload_zip(self):
        dir_test = os.path.dirname(__file__)
        path_test = os.path.join(dir_test, "uploads" + os.sep + "test2.zip")
        id = self.get_id_fixed("sys_document_zip_id1")
        with open(path_test, "rb") as file:
            tostring = base64.b64encode(file.read())
            file.close()
        req_post = {
            "file_content_type": "ZIP",
            "filename": "test2.zip",
            "file_64": tostring.decode(),
        }
        response = self.client.post(
            url_for("sysdocument.post_file", id=id),
            json=req_post,
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 201)

    # ====================

    def sys_document_upload_xlsx(self):

        dir_test = os.path.dirname(__file__)
        path_test = os.path.join(dir_test, "uploads" + os.sep + "test3.xlsx")
        id = self.get_id_fixed("sys_document_xlsx_id1")
        with open(path_test, "rb") as file:
            tostring = base64.b64encode(file.read())
            file.close()
        req_post = {
            "file_content_type": "XLSX",
            "filename": "test3.xlsx",
            "file_64": tostring.decode(),
        }
        response = self.client.post(
            url_for("sysdocument.post_file", id=id),
            json=req_post,
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 201)

    # ====================

    def sys_document_upload_txt(self):
        dir_test = os.path.dirname(__file__)
        path_test = os.path.join(dir_test, "uploads" + os.sep + "test4.txt")
        id = self.get_id_fixed("sys_document_txt_id1")
        with open(path_test, "rb") as file:
            tostring = base64.b64encode(file.read())
        req_post = {
            "file_content_type": "TXT",
            "filename": "test4.txt",
            "file_64": tostring.decode(),
        }

        response = self.client.post(
            url_for("sysdocument.post_file", id=id),
            json=req_post,
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 201)

    # ===========================================================

    # ====================

    def sys_document_download_pdf(self):
        id = self.get_id_fixed("sys_document_pdf_id1")
        dir_test = os.path.dirname(__file__)
        path_test = os.path.join(dir_test, "downloads" + os.sep + id + "-download.pdf")
        response = self.client.get(
            url_for("sysdocument.get_file", id=id), headers=self.create_token()
        )
        with open(path_test, "wb+") as file:
            file.write(response.data)
            file.close()
        self.assertEqual(response.status_code, 200)
        exist = os.path.exists(path_test)
        self.assertEqual(exist, True, "test_sys_document_001_download exist")

    # #====================
    def sys_document_download_zip(self):
        id = self.get_id_fixed("sys_document_zip_id1")
        dir_test = os.path.dirname(__file__)
        path_test = os.path.join(dir_test, "downloads" + os.sep + id + "-download.zip")
        response = self.client.get(
            url_for("sysdocument.get_file", id=id), headers=self.create_token()
        )
        with open(path_test, "wb") as file:
            file.write(response.data)
            file.close()
        self.assertEqual(response.status_code, 200)
        exist = os.path.exists(path_test)
        self.assertEqual(exist, True, "test_sys_document_011_download_zip exist")

    # #====================

    def sys_document_download_xlsx(self):
        id = self.get_id_fixed("sys_document_xlsx_id1")
        dir_test = os.path.dirname(__file__)
        path_test = os.path.join(dir_test, "downloads" + os.sep + id + "-download.xlsx")
        response = self.client.get(
            url_for("sysdocument.get_file", id=id), headers=self.create_token()
        )
        with open(path_test, "wb") as file:
            file.write(response.data)
            file.close()
        self.assertEqual(response.status_code, 200)
        exist = os.path.exists(path_test)
        self.assertEqual(exist, True, "test_sys_document_011_download_xlsx exist")

    # #====================

    def sys_document_download_txt(self):
        id = self.get_id_fixed("sys_document_txt_id1")
        dir_test = os.path.dirname(__file__)
        path_test = os.path.join(dir_test, "downloads" + os.sep + id + "-download.txt")
        response = self.client.get(
            url_for("sysdocument.get_file", id=id), headers=self.create_token()
        )
        with open(path_test, "wb") as file:
            file.write(response.data)
            file.close()
        self.assertEqual(response.status_code, 200)
        exist = os.path.exists(path_test)
        self.assertEqual(exist, True, "test_sys_document_011_download_txt exist")

    # ====================

    # ===========================================================
    # sys_restriction
    # ===========================================================

    def sys_restriction_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_restriction_id1"),
            "name": "TST",
            "active": "S",
            "type_value": "L",
            "code_restriction": "TESTE  1 [CRUD]",
        }

        response = self.client.post(
            url_for("sysrestriction.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_restriction_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_restriction_id2"),
            "name": "TST",
            "active": "S",
            "type_value": "L",
            "code_restriction": "TESTE  2 [CRUD]",
        }

        response = self.client.post(
            url_for("sysrestriction.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_restriction_get(self):
        response = self.client.get(
            url_for("sysrestriction.find_all"), headers=self.create_token()
        )
        result = len(response.json) > 0
        self.assertTrue(result)

    # ====================

    def sys_restriction_get_by_id(self):
        response = self.client.get(
            url_for(
                "sysrestriction.find_by_id", id=self.get_id_fixed("sys_restriction_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_restriction_delete(self):
        response = self.client.delete(
            url_for(
                "sysrestriction.delete", id=self.get_id_fixed("sys_restriction_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_module
    # ===========================================================

    def sys_module_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_module_id1"),
            "name": "TESTE  1 [CRUD]",
            "color": "tst",
            "icon": "tst",
            "code_module": "TESTE  1 [CRUD]",
            "sys_id": module_tests_sys.sys_id1(self),
            "active": "S",
            "order_visual": "2",
        }

        response = self.client.post(
            url_for("sysmodule.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_module_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_module_id2"),
            "name": "TESTE  2 [CRUD]",
            "color": "tst",
            "icon": "tst",
            "code_module": "TESTE  2 [CRUD]",
            "sys_id": module_tests_sys.sys_id1(self),
            "active": "S",
            "order_visual": "2",
        }

        response = self.client.post(
            url_for("sysmodule.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_module_get(self):
        response = self.client.get(
            url_for("sysmodule.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_module_get_by_id(self):
        response = self.client.get(
            url_for("sysmodule.find_by_id", id=self.get_id_fixed("sys_module_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_module_delete(self):
        response = self.client.delete(
            url_for("sysmodule.delete", id=self.get_id_fixed("sys_module_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_licence
    # ===========================================================

    def sys_licence_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_licence_id1"),
            "doc": "tst",
            "end_uf": "tst",
            "end_bairro": "tst",
            "end_cidade": "tst",
            "end_logradouro": "tst",
            "end_numero": "tst",
            "end_pais": "sts",
            "active": "S",
            "log_date_ins": "12/05/2022",
            "nome_solicitante": "tst",
            "status": "AT",
            "status_data": "12/05/2022",
            "status_observacao": "tst",
            "sys_version": "tst",
            "tipo_doc": "tst",
            "chamado_id": "t",
            "code_licence": "TESTE  1 [CRUD]",
            "sys_id": module_tests_sys.sys_id1(self),
            "sys_plan_id": module_tests_sys.sys_plan_id1(self),
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "sys_licence_restriction_childs": [
                {
                    "id": self.get_id_fixed("sys_licence_restriction_id1"),
                    "sys_restriction_id": module_tests_sys.sys_restriction_id1(self),
                    "days_blocked_extra": "5",
                    "days_blocked": "5",
                    "value_restriction_blocked": "5",
                    "value_restriction": "5",
                }
            ],
        }

        response = self.client.post(
            url_for("syslicence.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_licence_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_licence_id2"),
            "code": "TESTE  2 [CRUD]",
            "doc": "tst",
            "end_uf": "tst",
            "end_bairro": "tst",
            "end_cidade": "tst",
            "end_logradouro": "tst",
            "end_numero": "tst",
            "end_pais": "sts",
            "log_date_ins": "12/05/2022",
            "nome_solicitante": "tst",
            "status": "AT",
            "status_data": "12/05/2022",
            "status_observacao": "tst",
            "sys_version": "tst",
            "tipo_doc": "tst",
            "chamado_id": "t",
            "code_licence": "TESTE  2 [CRUD]",
            "sys_id": module_tests_sys.sys_id1(self),
            "sys_plan_id": module_tests_sys.sys_plan_id1(self),
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "sys_licence_restriction_childs": [
                {
                    "sys_restriction_id": module_tests_sys.sys_restriction_id1(self),
                    "days_blocked_extra": "5",
                    "days_blocked": "5",
                    "value_restriction_blocked": "5",
                    "value_restriction": "5",
                }
            ],
            "sys_licence_device_childs": [
                {
                    "sigla_device": "TESTE  1 [CRUD]",
                    "sys_licence_id": module_tests_sys.sys_licence_id1(self),
                }
            ],
        }

        response = self.client.post(
            url_for("syslicence.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_licence_get(self):
        response = self.client.get(
            url_for("syslicence.find_all"), headers=self.create_token()
        )
        result = len(response.json) > 0
        self.assertTrue(
            result,
        )

    # ====================

    def sys_licence_get_by_id(self):
        response = self.client.get(
            url_for("syslicence.find_by_id", id=self.get_id_fixed("sys_licence_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_licence_delete(self):
        response = self.client.delete(
            url_for("syslicence.delete", id=self.get_id_fixed("sys_licence_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_plan
    # ===========================================================

    def sys_plan_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_plan_id1"),
            "description": "Plano Free",
            "indicated": "S",
            "name": "FreXXe",
            "sys_id": module_tests_sys.sys_id1(self),
            "type_plan": "FR",
            "active": "S",
            "code_plan": "TESTE  1 [CRUD]",
            "sys_plan_restriction_childs": [
                {
                    "id": self.get_id_fixed("sys_plan_restriction_id1"),
                    "value_restriction_blocked": "5",
                    "days_blocked_extra": "5",
                    "value_restriction": "5",
                    "sys_restriction_id": module_tests_sys.sys_restriction_id1(self),
                    "days_blocked": "5",
                }
            ],
        }

        response = self.client.post(
            url_for("sysplan.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_plan_id2(self):
        req_post = {
            "id": self.get_id_fixed("sys_plan_id2"),
            "description": "Plano Free",
            "indicated": "S",
            "name": "FreXXe",
            "sys_id": module_tests_sys.sys_id1(self),
            "type_plan": "FR",
            "active": "S",
            "code_plan": "TESTE  2 [CRUD]",
            "sys_plan_restriction_childs": [
                {
                    "value_restriction_blocked": "5",
                    "days_blocked_extra": "5",
                    "value_restriction": "5",
                    "sys_restriction_id": module_tests_sys.sys_restriction_id1(self),
                    "days_blocked": "5",
                }
            ],
        }

        response = self.client.post(
            url_for("sysplan.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_plan_get(self):
        response = self.client.get(
            url_for("sysplan.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_plan_get_by_id(self):
        response = self.client.get(
            url_for("sysplan.find_by_id", id=self.get_id_fixed("sys_plan_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_plan_delete(self):
        response = self.client.delete(
            url_for("sysplan.delete", id=self.get_id_fixed("sys_plan_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_program
    # ===========================================================

    def sys_program_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_program_id1"),
            "admin": "N",
            "controller": "TESTE  1 [CRUD]",
            "icon": "fas fa-table",
            "menu": "S",
            "name": "Parmetros",
            "type_program": "T",
            "code_program": "TESTE  1 [CRUD]",
            "sys_module_id": module_tests_sys.sys_module_id1(self),
            "active": "S",
        }

        response = self.client.post(
            url_for("sysprogram.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_program_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_program_id2"),
            "admin": "N",
            "controller": "TESTE  2 [CRUD]",
            "icon": "fas fa-table",
            "menu": "S",
            "name": "Parmetros",
            "type_program": "T",
            "code_program": "TESTE  2 [CRUD]",
            "sys_module_id": module_tests_sys.sys_module_id1(self),
        }

        response = self.client.post(
            url_for("sysprogram.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_program_get(self):
        response = self.client.get(
            url_for("sysprogram.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_program_get_by_id(self):
        response = self.client.get(
            url_for("sysprogram.find_by_id", id=self.get_id_fixed("sys_program_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_program_delete(self):
        response = self.client.delete(
            url_for("sysprogram.delete", id=self.get_id_fixed("sys_program_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  sys_program_favorite
    # ===========================================================

    def sys_program_favorite_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_program_favorite_id1"),
            "sys_program_id": module_tests_sys.sys_program_id1(self),
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "favorite": "S",
        }

        response = self.client.post(
            url_for("sysprogramfavorite.favorite"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 200)
        return id

    # ====================

    # def sys_program_favorite_get_by_id(self):
    #     response = self.client.get(url_for('sysprogramfavorite.get_by_user_login'), headers=self.create_token())
    #     print(response)
    #     self.assertEqual(response.status_code, 200)
    # ===========================================================
    #  sys_user_cms_grupo
    # ===========================================================

    def sys_user_cms_grupo_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_user_cms_grupo_id1"),
            "cms_grupo_id": module_tests_cms.module_tests_cms.cms_grupo_id1(self),
            "sys_user_id": module_tests_sys.sys_user_id1(self),
        }

        response = self.client.post(
            url_for("sysusercmsgrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_user_cms_grupo_id2(self):
        req_post = {
            "id": self.get_id_fixed("sys_user_cms_grupo_id2"),
            "cms_grupo_id": module_tests_cms.module_tests_cms.cms_grupo_id1(self),
            "sys_user_id": module_tests_sys.sys_user_id1(self),
        }
        response = self.client.post(
            url_for("sysusercmsgrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_user_cms_grupo_get(self):
        response = self.client.get(
            url_for("sysusercmsgrupo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_user_cms_grupo_get_by_id(self):
        response = self.client.get(
            url_for(
                "sysusercmsgrupo.find_by_id",
                id=self.get_id_fixed("sys_user_cms_grupo_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_user_cms_grupo_delete(self):
        response = self.client.delete(
            url_for(
                "sysusercmsgrupo.delete", id=self.get_id_fixed("sys_user_cms_grupo_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  sys_email_log
    # ===========================================================

    def sys_email_log_id1(self):
        req_post = {
            "id": self.get_id_fixed("sys_email_log_id1"),
            "body": "ts",
            "body_type": "ts",
            "date_log": "050222",
            "date_send": "050222",
            "email_from": "tst",
            "email_to": "st",
            "error_message": "st",
            "login": "st",
            "subject": "st",
            "sys_unit_id": module_tests_sys.sys_unit_id1(self),
            "type_in_out": "ts",
        }

        response = self.client.post(
            url_for("sysemaillog.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_email_log_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_email_log_id2"),
            "body": "ts",
            "body_type": "ts",
            "date_log": "050222",
            "date_send": "050222",
            "email_from": "ts",
            "email_to": "st",
            "error_message": "st",
            "login": "st",
            "subject": "st",
            "sys_unit_id": module_tests_sys.sys_unit_id1(self),
            "type_in_out": "ts",
        }

        response = self.client.post(
            url_for("sysemaillog.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_email_log_get(self):
        response = self.client.get(
            url_for("sysemaillog.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_email_log_get_by_id(self):
        response = self.client.get(
            url_for(
                "sysemaillog.find_by_id", id=self.get_id_fixed("sys_email_log_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_email_log_delete(self):
        response = self.client.delete(
            url_for("sysemaillog.delete", id=self.get_id_fixed("sys_email_log_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  sys_notification_log
    # ===========================================================

    def sys_notification_log_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_notification_log_id1"),
            "action_body1": "ts",
            "action_body2": "st",
            "action_body3": "ts",
            "action_header1": "ts",
            "action_header2": "ts",
            "action_header3": "ts",
            "action_label1": "ts",
            "action_label2": "ts",
            "action_label3": "ts",
            "action_type1": "ts",
            "action_type2": "ts",
            "action_type3": "ts",
            "action_url1": "st",
            "action_url2": "ts",
            "action_url3": "st",
            "checked": "S",
            "dt_message": "ts",
            "email_to": "ts",
            "icon": "ts",
            "message": "tst",
            "subject": "ts",
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "sys_user_to_id": "ts",
            "type_notification": "ts",
        }

        response = self.client.post(
            url_for("sysnotificationlog.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_notification_log_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_notification_log_id2"),
            "action_body1": "ts",
            "action_body2": "st",
            "action_body3": "ts",
            "action_header1": "ts",
            "action_header2": "ts",
            "action_header3": "ts",
            "action_label1": "ts",
            "action_label2": "ts",
            "action_label3": "ts",
            "action_type1": "ts",
            "action_type2": "ts",
            "action_type3": "ts",
            "action_url1": "st",
            "action_url2": "ts",
            "action_url3": "st",
            "checked": "S",
            "dt_message": "ts",
            "email_to": "ts",
            "icon": "ts",
            "message": "tst",
            "subject": "ts",
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "sys_user_to_id": "ts",
            "type_notification": "ts",
        }

        response = self.client.post(
            url_for("sysnotificationlog.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_notification_log_get(self):
        response = self.client.get(
            url_for("sysnotificationlog.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_notification_log_get_by_id(self):
        response = self.client.get(
            url_for(
                "sysnotificationlog.find_by_id",
                id=self.get_id_fixed("sys_notification_log_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_notification_log_delete(self):
        response = self.client.delete(
            url_for(
                "sysnotificationlog.delete",
                id=self.get_id_fixed("sys_notification_log_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  sys_notification_token
    # ===========================================================

    def sys_notification_token_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_notification_token_id1"),
            "action_body1": "ts",
            "action_body2": "st",
            "action_body3": "ts",
            "action_header1": "ts",
            "action_header2": "ts",
            "action_header3": "ts",
            "action_label1": "ts",
            "action_label2": "ts",
            "action_label3": "ts",
            "action_type1": "ts",
            "action_type2": "ts",
            "action_type3": "ts",
            "action_url1": "st",
            "action_url2": "ts",
            "action_url3": "st",
            "checked": "S",
            "dt_message": "ts",
            "email_to": "ts",
            "icon": "ts",
            "message": "tst",
            "subject": "ts",
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "sys_user_to_id": "ts",
            "type_notification": "ts",
        }

        response = self.client.post(
            url_for("sysnotificationtoken.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_notification_token_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_notification_token_id2"),
            "action_body1": "ts",
            "action_body2": "st",
            "action_body3": "ts",
            "action_header1": "ts",
            "action_header2": "ts",
            "action_header3": "ts",
            "action_label1": "ts",
            "action_label2": "ts",
            "action_label3": "ts",
            "action_type1": "ts",
            "action_type2": "ts",
            "action_type3": "ts",
            "action_url1": "st",
            "action_url2": "ts",
            "action_url3": "st",
            "checked": "S",
            "dt_message": "ts",
            "email_to": "ts",
            "icon": "ts",
            "message": "tst",
            "subject": "ts",
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "sys_user_to_id": "ts",
            "type_notification": "ts",
        }

        response = self.client.post(
            url_for("sysnotificationtoken.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_notification_token_get(self):
        response = self.client.get(
            url_for("sysnotificationtoken.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_notification_token_get_by_id(self):
        response = self.client.get(
            url_for(
                "sysnotificationtoken.find_by_id",
                id=self.get_id_fixed("sys_notification_token_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_notification_token_delete(self):
        response = self.client.delete(
            url_for(
                "sysnotificationtoken.delete",
                id=self.get_id_fixed("sys_notification_token_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    #  sys_token
    # ===========================================================

    def sys_token_generate_token(self):
        id = str(uuid.uuid4())
        req_post = {
            "id": id,
            "hours": 5,
            "data_token": '{"login":"admin"}',
        }

        response = self.client.post(
            url_for("systoken.generate_token"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        token = json.loads(response.data.decode())["data"]
        self.session.set("sys_token_token", token)
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_token_get_token(self):
        response = self.client.get(
            url_for(
                "systoken.get_token",
                token=self.session.get("sys_token_token"),
                headers=self.create_token(),
            )
        )
        self.assertEqual(response.status_code, 401)

    # ===========================================================
    # sys_type_description
    # ===========================================================

    def sys_type_description_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_type_description_id1"),
            "description_type": "TESTE  1 [CRUD]",
            "field_name": "TESTE  1 [CRUD]",
            "table_name": "TESTE  1 [CRUD]",
            "value_type": "T",
        }

        response = self.client.post(
            url_for("systypedescription.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_type_description_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_type_description_id2"),
            "description_type": "TESTE  2 [CRUD]",
            "field_name": "TESTE  2 [CRUD]",
            "table_name": "TESTE  2 [CRUD]",
            "value_type": "T",
        }

        response = self.client.post(
            url_for("systypedescription.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_type_description_get(self):
        response = self.client.get(
            url_for("systypedescription.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_type_description_get_by_id(self):
        response = self.client.get(
            url_for(
                "systypedescription.find_by_id",
                id=self.get_id_fixed("sys_type_description_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_type_description_delete(self):
        response = self.client.delete(
            url_for(
                "systypedescription.delete",
                id=self.get_id_fixed("sys_type_description_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_process_log
    # ===========================================================

    def sys_process_log_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_process_log_id1"),
            "date_fin_process": "2022-02-15T01:00:00",
            "date_ini_process": "2022-02-15T12:00:00",
            "param_process": "TESTE PROCESS LOG",
            "error": "N",
            "reversed": "S",
            "sys_unit_id": module_tests_sys.sys_unit_id1(self),
            "type_process": "GER_PER_GENERATE",
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "message_process": "TESTE",
            "unit_id": module_tests_sys.sys_unit_id1(self),
            "code_process": "TESTE [CRUD]",
        }

        response = self.client.post(
            url_for("sysprocesslog.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_process_log_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_process_log_id2"),
            "date_fin_process": "2022-02-15T01:00:00",
            "date_ini_process": "2022-02-15T12:00:00",
            "param_process": "TESTE PROCESS LOG",
            "reversed": "S",
            "sys_unit_id": module_tests_sys.sys_unit_id1(self),
            "type_process": "GER_PER_GENERATE",
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "message_process": "TESTE",
            "unit_id": module_tests_sys.sys_unit_id1(self),
            "code_process": "TESTE [CRUD]",
            "error": "N",
        }
        response = self.client.post(
            url_for("sysprocesslog.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_process_log_get(self):
        response = self.client.get(
            url_for("sysprocesslog.find_all"), headers=self.create_token()
        )
        result = len(response.json) > 0

        self.assertTrue(result)

    # ====================

    def sys_process_log_get_by_id(self):
        response = self.client.get(
            url_for(
                "sysprocesslog.find_by_id", id=self.get_id_fixed("sys_process_log_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_process_log_delete(self):
        response = self.client.delete(
            url_for(
                "sysprocesslog.delete", id=self.get_id_fixed("sys_process_log_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_user_unit
    # ===========================================================

    def sys_user_unit_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_user_unit_id1"),
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "sys_unit_id": module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("sysuserunit.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_user_unit_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_user_unit_id2"),
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "sys_unit_id": module_tests_sys.sys_unit_id1(self),
        }

        response = self.client.post(
            url_for("sysuserunit.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_user_unit_get(self):
        response = self.client.get(
            url_for("sysuserunit.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_user_unit_get_by_id(self):
        response = self.client.get(
            url_for(
                "sysuserunit.find_by_id", id=self.get_id_fixed("sys_user_unit_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_user_unit_delete(self):
        response = self.client.delete(
            url_for("sysuserunit.delete", id=self.get_id_fixed("sys_user_unit_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_user_ind_pnl
    # ===========================================================

    def sys_user_ind_pnl_id1(self):
        module_tests_ind.module_tests_ind.ind_pnl_id1(self)
        req_post = {
            "id": self.get_id_fixed("sys_user_ind_pnl_id1"),
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "ind_pnl_id": module_tests_ind.module_tests_ind.ind_pnl_id1(self),
        }

        response = self.client.post(
            url_for("sysuserindpnl.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_user_ind_pnl_id2(self):
        module_tests_ind.module_tests_ind.ind_pnl_id1(self)
        req_post = {
            "id": self.get_id_fixed("sys_user_ind_pnl_id2"),
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "ind_pnl_id": module_tests_ind.module_tests_ind.ind_pnl_id1(self),
        }

        response = self.client.post(
            url_for("sysuserindpnl.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_user_ind_pnl_get(self):
        response = self.client.get(
            url_for("sysuserindpnl.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_user_ind_pnl_get_by_id(self):
        response = self.client.get(
            url_for(
                "sysuserindpnl.find_by_id", id=self.get_id_fixed("sys_user_ind_pnl_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_user_ind_pnl_delete(self):
        response = self.client.delete(
            url_for(
                "sysuserindpnl.delete", id=self.get_id_fixed("sys_user_ind_pnl_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_access_log
    # ===========================================================

    def sys_access_log_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_access_log_id1"),
            "login_time": "22/07/2022",
            "sys_id": module_tests_sys.sys_id1(self),
            "unit_id": module_tests_sys.sys_unit_id1(self),
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "access_ip": "tst",
        }

        response = self.client.post(
            url_for("sysaccesslog.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_access_log_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_access_log_id2"),
            "login_time": "22/07/2022",
            "sys_id": module_tests_sys.sys_id1(self),
            "unit_id": module_tests_sys.sys_unit_id1(self),
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "access_ip": "tst",
        }

        response = self.client.post(
            url_for("sysaccesslog.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_access_log_get(self):
        response = self.client.get(
            url_for("sysaccesslog.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_access_log_get_by_id(self):
        response = self.client.get(
            url_for(
                "sysaccesslog.find_by_id", id=self.get_id_fixed("sys_access_log_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_access_log_delete(self):
        response = self.client.delete(
            url_for("sysaccesslog.delete", id=self.get_id_fixed("sys_access_log_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_user_preference
    # ===========================================================

    def sys_user_preference_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_user_preference_id1"),
            "object_type": "tst",
            "preference_description": "tst",
            "value": "5",
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "object_id": "tst",
            "isdefault": "S",
            "object_sub_id": "TESTE",
        }

        response = self.client.post(
            url_for("sysuserpreference.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_user_preference_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_user_preference_id2"),
            "object_type": "tst",
            "preference_description": "tst",
            "value": "5",
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "object_id": "tst",
            "isdefault": "S",
            "object_sub_id": "TESTE",
        }

        response = self.client.post(
            url_for("sysuserpreference.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_user_preference_get(self):
        response = self.client.get(
            url_for("sysuserpreference.list"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_user_preference_delete(self):
        response = self.client.delete(
            url_for(
                "sysuserpreference.delete",
                id=self.get_id_fixed("sys_user_preference_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_param
    # ===========================================================

    def sys_param_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_param_id1"),
            "sys_id": module_tests_sys.sys_id1(self),
            "type": "DT",
            "paramkey": "5",
            "paramvalue": "5",
        }

        response = self.client.post(
            url_for("sysparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_param_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_param_id2"),
            "sys_id": module_tests_sys.sys_id1(self),
            "type": "DT",
            "paramkey": "5",
            "paramvalue": "5",
        }

        response = self.client.post(
            url_for("sysparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_param_get(self):
        response = self.client.get(
            url_for("sysparam.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_param_get_by_id(self):
        response = self.client.get(
            url_for("sysparam.find_by_id", id=self.get_id_fixed("sys_param_id1")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_param_delete(self):
        response = self.client.delete(
            url_for("sysparam.delete", id=self.get_id_fixed("sys_param_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_unit_param
    # ===========================================================

    def sys_unit_param_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_unit_param_id1"),
            "unit_id": module_tests_sys.sys_unit_id1(self),
            "data_valid_ini": "2022-12-29T00:00:00",
        }

        response = self.client.post(
            url_for("sysunitparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_unit_param_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_unit_param_id2"),
            "unit_id": module_tests_sys.sys_unit_id1(self),
            "data_valid_ini": "2022-12-29T00:00:00",
        }

        response = self.client.post(
            url_for("sysunitparam.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_unit_param_get(self):
        response = self.client.get(
            url_for("sysunitparam.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_unit_param_get_by_id(self):
        response = self.client.get(
            url_for(
                "sysunitparam.find_by_id", id=self.get_id_fixed("sys_unit_param_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_unit_param_delete(self):
        response = self.client.delete(
            url_for("sysunitparam.delete", id=self.get_id_fixed("sys_unit_param_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_user_chat_grupo
    # ===========================================================

    def sys_user_chat_grupo_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_user_chat_grupo_id1"),
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "crm_chat_grupo_id": module_tests_crm.module_tests_crm.crm_chat_grupo_id1(
                self
            ),
        }

        response = self.client.post(
            url_for("sysuserchatgrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_user_chat_grupo_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_user_chat_grupo_id2"),
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "crm_chat_grupo_id": module_tests_crm.module_tests_crm.crm_chat_grupo_id1(
                self
            ),
        }

        response = self.client.post(
            url_for("sysuserchatgrupo.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_user_chat_grupo_get(self):

        response = self.client.get(
            url_for("sysuserchatgrupo.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_user_chat_grupo_get_by_id(self):
        response = self.client.get(
            url_for(
                "sysuserchatgrupo.find_by_id",
                id=self.get_id_fixed("sys_user_chat_grupo_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_user_chat_grupo_delete(self):
        response = self.client.delete(
            url_for(
                "sysuserchatgrupo.delete",
                id=self.get_id_fixed("sys_user_chat_grupo_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_document_user
    # ===========================================================

    def sys_document_user_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_user_chat_grupo_id2"),
            "sys_document_id": module_tests_sys.sys_document_id1(self),
            "sys_user_id": module_tests_sys.sys_user_id1(self),
        }

        response = self.client.post(
            url_for("sysdocumentuser.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_document_user_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_document_user_id2"),
            "sys_document_id": module_tests_sys.sys_document_id1(self),
            "sys_user_id": module_tests_sys.sys_user_id1(self),
        }

        response = self.client.post(
            url_for("sysdocumentuser.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_document_user_get(self):
        response = self.client.get(
            url_for("sysdocumentuser.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_document_user_get_by_id(self):
        response = self.client.get(
            url_for(
                "sysdocumentuser.find_by_id",
                id=self.get_id_fixed("sys_document_user_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_document_user_delete(self):
        response = self.client.delete(
            url_for(
                "sysdocumentuser.delete", id=self.get_id_fixed("sys_document_user_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_user_group
    # ===========================================================

    def sys_user_group_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_user_group_id1"),
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "sys_group_id": module_tests_sys.sys_group_id1(self),
        }

        response = self.client.post(
            url_for("sysusergroup.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_user_group_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_user_group_id2"),
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "sys_group_id": module_tests_sys.sys_group_id1(self),
        }

        response = self.client.post(
            url_for("sysusergroup.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_user_group_get(self):
        response = self.client.get(
            url_for("sysusergroup.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_user_group_get_by_id(self):
        response = self.client.get(
            url_for(
                "sysusergroup.find_by_id", id=self.get_id_fixed("sys_user_group_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_user_group_delete(self):
        response = self.client.delete(
            url_for("sysusergroup.delete", id=self.get_id_fixed("sys_user_group_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_user_program
    # ===========================================================

    def sys_user_program_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_user_program_id1"),
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "sys_program_id": module_tests_sys.sys_program_id1(self),
        }

        response = self.client.post(
            url_for("sysuserprogram.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_user_program_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_user_program_id2"),
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "sys_program_id": module_tests_sys.sys_program_id1(self),
        }

        response = self.client.post(
            url_for("sysuserprogram.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_user_program_get(self):
        response = self.client.get(
            url_for("sysuserprogram.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_user_program_get_by_id(self):
        response = self.client.get(
            url_for(
                "sysuserprogram.find_by_id",
                id=self.get_id_fixed("sys_user_program_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_user_program_delete(self):
        response = self.client.delete(
            url_for(
                "sysuserprogram.delete", id=self.get_id_fixed("sys_user_program_id2")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_translate
    # ===========================================================

    def sys_translate_id1(self):
        module_tests_sys.sys_translate_lang_id1(self)

        req_post = {
            "id": self.get_id_fixed("sys_translate_id1"),
            "term_orig": "TESTE  1 [CRUD]",
            "term_translate": "TESTE  1 [CRUD]",
            "sys_translate_lang_id": module_tests_sys.sys_translate_lang_id1(self),
            "term_group": "TESTE  1 [CRUD]",
        }

        response = self.client.post(
            url_for("systranslate.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_translate_id2(self):
        module_tests_sys.sys_translate_lang_id1(self)
        req_post = {
            "id": self.get_id_fixed("sys_translate_id2"),
            "term_orig": "TESTE  2 [CRUD]",
            "term_translate": "TESTE  2 [CRUD]",
            "sys_translate_lang_id": module_tests_sys.sys_translate_lang_id1(self),
            "term_group": "TESTE  2 [CRUD]",
        }

        response = self.client.post(
            url_for("systranslate.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_translate_get(self):
        response = self.client.get(
            url_for("systranslate.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_translate_get_by_id(self):
        response = self.client.get(
            url_for(
                "systranslate.find_by_id", id=self.get_id_fixed("sys_translate_id1")
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_translate_delete(self):
        response = self.client.delete(
            url_for("systranslate.delete", id=self.get_id_fixed("sys_translate_id2")),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_translate_lang
    # ===========================================================

    def sys_translate_lang_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_translate_lang_id1"),
            "code": "TESTE  1 [CRUD]",
            "name": "TESTE  1 [CRUD]",
            "default_lang": "S",
            "active": "S",
        }

        response = self.client.post(
            url_for("systranslatelang.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_translate_lang_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_translate_lang_id2"),
            "code": "TESTE  2 [CRUD]",
            "name": "TESTE  2 [CRUD]",
            "default_lang": "S",
            "active": "S",
        }

        response = self.client.post(
            url_for("systranslatelang.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_translate_lang_get(self):
        response = self.client.get(
            url_for("systranslatelang.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_translate_lang_get_by_id(self):
        response = self.client.get(
            url_for(
                "systranslatelang.find_by_id",
                id=self.get_id_fixed("sys_translate_lang_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_translate_lang_delete(self):
        response = self.client.delete(
            url_for(
                "systranslatelang.delete",
                id=self.get_id_fixed("sys_translate_lang_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_dic
    # ===========================================================

    def sys_dic_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_dic_id1"),
            "name": "TESTE  1 [CRUD]",
            "name_item": "TESTE  1 [CRUD]",
            "type_dic": "12",
            "description": "TST",
            "description_help": "TST",
        }

        response = self.client.post(
            url_for("sysdic.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_dic_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_dic_id2"),
            "name": "TESTE  2 [CRUD]",
            "name_item": "TESTE  2 [CRUD]",
            "type_dic": "12",
            "description": "TST",
            "description_help": "TST",
        }

        response = self.client.post(
            url_for("sysdic.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_dic_get(self):
        response = self.client.get(
            url_for("sysdic.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_dic_get_by_id(self):
        response = self.client.get(
            url_for(
                "sysdic.find_by_id",
                id=self.get_id_fixed("sys_dic_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_dic_delete(self):
        response = self.client.delete(
            url_for(
                "sysdic.delete",
                id=self.get_id_fixed("sys_dic_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_action
    # ===========================================================

    def sys_action_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_action_id1"),
            "name": "TESTE  1 [CRUD]",
            "code": "TESTE  1 [CRUD]",
            "active": "S",
        }

        response = self.client.post(
            url_for("sysaction.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_action_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_action_id2"),
            "name": "TESTE  2 [CRUD]",
            "code": "TESTE  2 [CRUD]",
            "active": "S",
        }

        response = self.client.post(
            url_for("sysaction.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_action_get(self):
        response = self.client.get(
            url_for("sysaction.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_action_get_by_id(self):
        response = self.client.get(
            url_for(
                "sysaction.find_by_id",
                id=self.get_id_fixed("sys_action_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_action_delete(self):
        response = self.client.delete(
            url_for(
                "sysaction.delete",
                id=self.get_id_fixed("sys_action_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_program_action
    # ===========================================================

    def sys_program_action_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_program_action_id1"),
            "sys_program_id": module_tests_sys.sys_program_id1(self),
            "sys_action_id": module_tests_sys.sys_action_id1(self),
        }

        response = self.client.post(
            url_for("sysprogramaction.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_program_action_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_program_action_id2"),
            "sys_program_id": module_tests_sys.sys_program_id2(self),
            "sys_action_id": module_tests_sys.sys_action_id2(self),
        }

        response = self.client.post(
            url_for("sysprogramaction.save"), json=req_post, headers=self.create_token()
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_program_action_get(self):
        response = self.client.get(
            url_for("sysprogramaction.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_program_action_get_by_id(self):
        response = self.client.get(
            url_for(
                "sysprogramaction.find_by_id",
                id=self.get_id_fixed("sys_program_action_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_program_action_delete(self):
        response = self.client.delete(
            url_for(
                "sysprogramaction.delete",
                id=self.get_id_fixed("sys_program_action_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_user_program_action
    # ===========================================================

    def sys_user_program_action_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_user_program_action_id1"),
            "sys_user_id": module_tests_sys.sys_user_id1(self),
            "sys_program_action_id": module_tests_sys.sys_program_action_id1(self),
            "exclude_action": "N",
        }

        response = self.client.post(
            url_for("sysuserprogramaction.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_user_program_action_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_user_program_action_id2"),
            "sys_user_id": module_tests_sys.sys_user_id2(self),
            "sys_program_action_id": module_tests_sys.sys_program_action_id2(self),
            "exclude_action": "N",
        }

        response = self.client.post(
            url_for("sysuserprogramaction.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_user_program_action_get(self):
        response = self.client.get(
            url_for("sysuserprogramaction.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_user_program_action_get_by_id(self):
        response = self.client.get(
            url_for(
                "sysuserprogramaction.find_by_id",
                id=self.get_id_fixed("sys_user_program_action_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_user_program_action_delete(self):
        response = self.client.delete(
            url_for(
                "sysuserprogramaction.delete",
                id=self.get_id_fixed("sys_user_program_action_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_group_program_action
    # ===========================================================

    def sys_group_program_action_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_group_program_action_id1"),
            "sys_group_id": module_tests_sys.sys_group_id1(self),
            "sys_program_action_id": module_tests_sys.sys_program_action_id1(self),
        }

        response = self.client.post(
            url_for("sysgroupprogramaction.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_group_program_action_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_group_program_action_id2"),
            "sys_group_id": module_tests_sys.sys_group_id2(self),
            "sys_program_action_id": module_tests_sys.sys_program_action_id2(self),
        }

        response = self.client.post(
            url_for("sysgroupprogramaction.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_group_program_action_get(self):
        response = self.client.get(
            url_for("sysgroupprogramaction.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_group_program_action_get_by_id(self):
        response = self.client.get(
            url_for(
                "sysgroupprogramaction.find_by_id",
                id=self.get_id_fixed("sys_group_program_action_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_group_program_action_delete(self):
        response = self.client.delete(
            url_for(
                "sysgroupprogramaction.delete",
                id=self.get_id_fixed("sys_group_program_action_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)

    # ===========================================================
    # sys_unit_manager
    # ===========================================================

    def sys_unit_manager_id1(self):

        req_post = {
            "id": self.get_id_fixed("sys_unit_manager_id1"),
            "link_website": "TESTE  1 [CRUD]",
            "subdomain_name": "TESTE  1 [CRUD]",
            "color_primary": "TESTE  1 [CRUD]",
            "color_menu_module_background": "TESTE  1 [CRUD]",
            "link_term_of_use": "TESTE  1 [CRUD]",
            "color_secondary": "TESTE  1 [CRUD]",
            "color_general_background": "TESTE  1 [CRUD]",
            "color_menu_module_font": "TESTE  1 [CRUD]",
            "icon_general": "TESTE  1 [CRUD]",
            "link_policy_private": "TESTE  1 [CRUD]",
            "icon_login": "TESTE  1 [CRUD]",
            "name": "TESTE  1 [CRUD]",
            "icon_menu": "TESTE  1 [CRUD]",
            "active": "S",
            "subdomain_active": "S",
        }

        response = self.client.post(
            url_for("sysunitmanager.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_unit_manager_id2(self):

        req_post = {
            "id": self.get_id_fixed("sys_unit_manager_id2"),
            "link_website": "TESTE  2 [CRUD]",
            "subdomain_name": "TESTE  2 [CRUD]",
            "color_primary": "TESTE  2 [CRUD]",
            "color_menu_module_background": "TESTE  2 [CRUD]",
            "link_term_of_use": "TESTE  2 [CRUD]",
            "color_secondary": "TESTE  2 [CRUD]",
            "color_general_background": "TESTE  2 [CRUD]",
            "color_menu_module_font": "TESTE  2 [CRUD]",
            "icon_general": "TESTE  2 [CRUD]",
            "link_policy_private": "TESTE  2 [CRUD]",
            "icon_login": "TESTE  2 [CRUD]",
            "name": "TESTE  2 [CRUD]",
            "icon_menu": "TESTE  2 [CRUD]",
            "active": "S",
            "subdomain_active": "S",
        }

        response = self.client.post(
            url_for("sysunitmanager.save"),
            json=req_post,
            headers=self.create_token(),
        )
        id = self.get_id_response(response)
        self.assertEqual(response.status_code, 201)
        return id

    # ====================

    def sys_unit_manager_get(self):
        response = self.client.get(
            url_for("sysunitmanager.find_all"), headers=self.create_token()
        )
        self.assertEqual(response.status_code, 200, response.json)

    # ====================

    def sys_unit_manager_get_by_id(self):
        response = self.client.get(
            url_for(
                "sysunitmanager.find_by_id",
                id=self.get_id_fixed("sys_unit_manager_id1"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 200)

    # ====================

    def sys_unit_manager_delete(self):
        response = self.client.delete(
            url_for(
                "sysunitmanager.delete",
                id=self.get_id_fixed("sys_unit_manager_id2"),
            ),
            headers=self.create_token(),
        )
        self.assertEqual(response.status_code, 204)
