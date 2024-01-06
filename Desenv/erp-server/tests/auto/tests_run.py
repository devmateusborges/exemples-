import os

from generic_tests import generic_tests
from module_tests_ope import module_tests_ope
from module_tests_sys import module_tests_sys
from module_tests_ger import module_tests_ger
from module_tests_fin import module_tests_fin
from module_tests_ctb import module_tests_ctb
from module_tests_fis import module_tests_fis
from module_tests_bor import module_tests_bor
from module_tests_pto import module_tests_pto
from module_tests_rhm import module_tests_rhm
from module_tests_crm import module_tests_crm
from module_tests_mov import module_tests_mov
from module_tests_mob import module_tests_mob
from module_tests_bov import module_tests_bov
from module_tests_cms import module_tests_cms
from module_tests_ind import module_tests_ind


class tests_run(generic_tests):

    tests_scenary = os.environ["TESTS_SCENARY"]
    tests_scenary = tests_scenary.split(",")

    # ===========================================================
    # SYS
    # ===========================================================
    def tests_sys_user_unit_01_id1(self):
        if self.check_scenary(["ALL", "SYS", "sys_user_unit_id1"], self.tests_scenary):
            module_tests_sys.sys_user_unit_id1(self)

    def tests_sys_user_unit_02_id2(self):
        if self.check_scenary(["ALL", "SYS", "sys_user_unit_id2"], self.tests_scenary):
            module_tests_sys.sys_user_unit_id2(self)

    def tests_sys_user_unit_03_get(self):
        if self.check_scenary(["ALL", "SYS", "sys_user_unit_get"], self.tests_scenary):
            module_tests_sys.sys_user_unit_get(self)

    def tests_sys_user_unit_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_unit_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_user_unit_get_by_id(self)

    def tests_sys_user_unit_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_unit_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_user_unit_delete(self)

    def tests_sys_user_preference_02_id2(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_preference_id2"], self.tests_scenary
        ):
            module_tests_sys.sys_user_preference_id2(self)

    def tests_sys_user_preference_01_id1(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_preference_id1"], self.tests_scenary
        ):
            module_tests_sys.sys_user_preference_id1(self)

    def tests_sys_user_preference_03_get(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_preference_get"], self.tests_scenary
        ):
            module_tests_sys.sys_user_preference_get(self)

    def tests_sys_user_preference_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_preference_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_user_preference_delete(self)

    def tests_sys_user_ind_pnl_02_id2(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_ind_pnl_id2"], self.tests_scenary
        ):
            module_tests_sys.sys_user_ind_pnl_id2(self)

    def tests_sys_user_ind_pnl_01_id1(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_ind_pnl_id1"], self.tests_scenary
        ):
            module_tests_sys.sys_user_ind_pnl_id1(self)

    def tests_sys_user_ind_pnl_03_get(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_ind_pnl_get"], self.tests_scenary
        ):
            module_tests_sys.sys_user_ind_pnl_get(self)

    def tests_sys_user_ind_pnl_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_ind_pnl_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_user_ind_pnl_get_by_id(self)

    def tests_sys_user_ind_pnl_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_ind_pnl_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_user_ind_pnl_delete(self)

    def tests_sys_user_02_id2(self):
        if self.check_scenary(["ALL", "SYS", "sys_user_id2"], self.tests_scenary):
            module_tests_sys.sys_user_id2(self)

    def tests_sys_user_01_id1(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_id1", "sys_user_id1"], self.tests_scenary
        ):
            module_tests_sys.sys_user_id1(self)

    def tests_sys_user_03_get(self):
        if self.check_scenary(["ALL", "SYS", "sys_user_get"], self.tests_scenary):
            module_tests_sys.sys_user_get(self)

    def tests_sys_user_04_get_by_id(self):
        if self.check_scenary(["ALL", "SYS", "sys_user_get_by_id"], self.tests_scenary):
            module_tests_sys.sys_user_get_by_id(self)

    def tests_sys_user_05_delete(self):
        if self.check_scenary(["ALL", "SYS", "sys_user_delete"], self.tests_scenary):
            module_tests_sys.sys_user_delete(self)

    def tests_sys_user_cms_grupo_02_id2(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_cms_grupo_id2"], self.tests_scenary
        ):
            module_tests_sys.sys_user_cms_grupo_id2(self)

    def tests_sys_user_cms_grupo_01_id1(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_cms_grupo_id1"], self.tests_scenary
        ):
            module_tests_sys.sys_user_cms_grupo_id1(self)

    def tests_sys_user_cms_grupo_03_get(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_cms_grupo_get"], self.tests_scenary
        ):
            module_tests_sys.sys_user_cms_grupo_get(self)

    def tests_sys_user_cms_grupo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_cms_grupo_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_user_cms_grupo_get_by_id(self)

    def tests_sys_user_cms_grupo_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_cms_grupo_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_user_cms_grupo_delete(self)

    def tests_sys_user_chat_grupo_02_id2(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_chat_grupo_id2"], self.tests_scenary
        ):
            module_tests_sys.sys_user_chat_grupo_id2(self)

    def tests_sys_user_chat_grupo_01_id1(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_chat_grupo_id1"], self.tests_scenary
        ):
            module_tests_sys.sys_user_chat_grupo_id1(self)

    def tests_sys_user_chat_grupo_03_get(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_chat_grupo_get"], self.tests_scenary
        ):
            module_tests_sys.sys_user_chat_grupo_get(self)

    def tests_sys_user_chat_grupo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_chat_grupo_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_user_chat_grupo_get_by_id(self)

    def tests_sys_user_chat_grupo_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_chat_grupo_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_user_chat_grupo_delete(self)

    def tests_sys_unit_param_02_id2(self):
        if self.check_scenary(["ALL", "SYS", "sys_unit_param_id2"], self.tests_scenary):
            module_tests_sys.sys_unit_param_id2(self)

    def tests_sys_unit_param_01_id1(self):
        if self.check_scenary(["ALL", "SYS", "sys_unit_param_id1"], self.tests_scenary):
            module_tests_sys.sys_unit_param_id1(self)

    def tests_sys_unit_param_03_get(self):
        if self.check_scenary(["ALL", "SYS", "sys_unit_param_get"], self.tests_scenary):
            module_tests_sys.sys_unit_param_get(self)

    def tests_sys_unit_param_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_unit_param_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_unit_param_get_by_id(self)

    def tests_sys_unit_param_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_unit_param_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_unit_param_delete(self)

    def tests_sys_unit_02_id2(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_unit_id2", "sys_unit_id2"], self.tests_scenary
        ):
            module_tests_sys.sys_unit_id2(self)

    def tests_sys_unit_01_id1(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_unit_id1", "sys_unit_id1"], self.tests_scenary
        ):
            module_tests_sys.sys_unit_id1(self)

    def tests_sys_unit_03_get(self):
        if self.check_scenary(["ALL", "SYS", "sys_unit_get"], self.tests_scenary):
            module_tests_sys.sys_unit_get(self)

    def tests_sys_unit_04_get_by_id(self):
        if self.check_scenary(["ALL", "SYS", "sys_unit_get_by_id"], self.tests_scenary):
            module_tests_sys.sys_unit_get_by_id(self)

    def tests_sys_unit_05_delete(self):
        if self.check_scenary(["ALL", "SYS", "sys_unit_delete"], self.tests_scenary):
            module_tests_sys.sys_unit_delete(self)

    def tests_sys_type_description_02_id2(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_type_description_id2"], self.tests_scenary
        ):
            module_tests_sys.sys_type_description_id2(self)

    def tests_sys_type_description_01_id1(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_type_description_id1"], self.tests_scenary
        ):
            module_tests_sys.sys_type_description_id1(self)

    def tests_sys_type_description_03_get(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_type_description_get"], self.tests_scenary
        ):
            module_tests_sys.sys_type_description_get(self)

    def tests_sys_type_description_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_type_description_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_type_description_get_by_id(self)

    def tests_sys_type_description_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_type_description_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_type_description_delete(self)

    def tests_sys_token_01_create(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_token_generate_token"], self.tests_scenary
        ):
            module_tests_sys.sys_token_generate_token(self)

    def tests_sys_token_02_get(self):
        if self.check_scenary(["ALL", "SYS", "sys_token_get"], self.tests_scenary):
            module_tests_sys.sys_token_get_token(self)

    def tests_sys_restriction_02_id2(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_restriction_id2"], self.tests_scenary
        ):
            module_tests_sys.sys_restriction_id2(self)

    def tests_sys_restriction_01_id1(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_restriction_id1"], self.tests_scenary
        ):
            module_tests_sys.sys_restriction_id1(self)

    def tests_sys_restriction_03_get(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_restriction_get"], self.tests_scenary
        ):
            module_tests_sys.sys_restriction_get(self)

    def tests_sys_restriction_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_restriction_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_restriction_get_by_id(self)

    def tests_sys_restriction_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_restriction_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_restriction_delete(self)

    def tests_sys_program_02_id2(self):
        if self.check_scenary(["ALL", "SYS", "sys_program_id2"], self.tests_scenary):
            module_tests_sys.sys_program_id2(self)

    def tests_sys_program_01_id1(self):
        if self.check_scenary(["ALL", "SYS", "sys_program_id1"], self.tests_scenary):
            module_tests_sys.sys_program_id1(self)

    def tests_sys_program_03_get(self):
        if self.check_scenary(["ALL", "SYS", "sys_program_get"], self.tests_scenary):
            module_tests_sys.sys_program_get(self)

    def tests_sys_program_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_program_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_program_get_by_id(self)

    def tests_sys_program_favorite_01_id1(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_program_favorite_id1"], self.tests_scenary
        ):
            module_tests_sys.sys_program_favorite_id1(self)

    # def tests_sys_program_favorite_03_get(self):
    #     if self.check_scenary(["ALL","SYS","sys_program_favorite_get"],self.tests_scenary):
    #         module_tests_sys.sys_program_favorite_get(self)
    def tests_sys_program_05_delete(self):
        if self.check_scenary(["ALL", "SYS", "sys_program_delete"], self.tests_scenary):
            module_tests_sys.sys_program_delete(self)

    def tests_sys_process_log_02_id2(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_process_log_id2"], self.tests_scenary
        ):
            module_tests_sys.sys_process_log_id2(self)

    def tests_sys_process_log_01_id1(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_process_log_id1"], self.tests_scenary
        ):
            module_tests_sys.sys_process_log_id1(self)

    def tests_sys_process_log_03_get(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_process_log_get"], self.tests_scenary
        ):
            module_tests_sys.sys_process_log_get(self)

    def tests_sys_process_log_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_process_log_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_process_log_get_by_id(self)

    def tests_sys_process_log_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_process_log_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_process_log_delete(self)

    def tests_sys_plan_02_id2(self):
        if self.check_scenary(["ALL", "SYS", "sys_plan_id2"], self.tests_scenary):
            module_tests_sys.sys_plan_id2(self)

    def tests_sys_plan_01_id1(self):
        if self.check_scenary(["ALL", "SYS", "sys_plan_id1"], self.tests_scenary):
            module_tests_sys.sys_plan_id1(self)

    def tests_sys_plan_03_get(self):
        if self.check_scenary(["ALL", "SYS", "sys_plan_get"], self.tests_scenary):
            module_tests_sys.sys_plan_get(self)

    def tests_sys_plan_04_get_by_id(self):
        if self.check_scenary(["ALL", "SYS", "sys_plan_get_by_id"], self.tests_scenary):
            module_tests_sys.sys_plan_get_by_id(self)

    def tests_sys_plan_05_delete(self):
        if self.check_scenary(["ALL", "SYS", "sys_plan_delete"], self.tests_scenary):
            module_tests_sys.sys_plan_delete(self)

    def tests_sys_param_02_id2(self):
        if self.check_scenary(["ALL", "SYS", "sys_param_id2"], self.tests_scenary):
            module_tests_sys.sys_param_id2(self)

    def tests_sys_param_01_id1(self):
        if self.check_scenary(["ALL", "SYS", "sys_param_id1"], self.tests_scenary):
            module_tests_sys.sys_param_id1(self)

    def tests_sys_param_03_get(self):
        if self.check_scenary(["ALL", "SYS", "sys_param_get"], self.tests_scenary):
            module_tests_sys.sys_param_get(self)

    def tests_sys_param_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_param_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_param_get_by_id(self)

    def tests_sys_param_05_delete(self):
        if self.check_scenary(["ALL", "SYS", "sys_param_delete"], self.tests_scenary):
            module_tests_sys.sys_param_delete(self)

    def tests_sys_notification_log_02_id2(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_notification_log_id2"], self.tests_scenary
        ):
            module_tests_sys.sys_notification_log_id2(self)

    def tests_sys_notification_log_01_id1(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_notification_log_id1"], self.tests_scenary
        ):
            module_tests_sys.sys_notification_log_id1(self)

    def tests_sys_notification_log_03_get(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_notification_log_get"], self.tests_scenary
        ):
            module_tests_sys.sys_notification_log_get(self)

    def tests_sys_notification_log_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_notification_log_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_notification_log_get_by_id(self)

    def tests_sys_notification_log_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_notification_log_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_notification_log_delete(self)


    def tests_sys_notification_token_02_id2(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_notification_token_id2"], self.tests_scenary
        ):
            module_tests_sys.sys_notification_token_id2(self)

    def tests_sys_notification_token_01_id1(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_notification_token_id1"], self.tests_scenary
        ):
            module_tests_sys.sys_notification_token_id1(self)

    def tests_sys_notification_token_03_get(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_notification_token_get"], self.tests_scenary
        ):
            module_tests_sys.sys_notification_token_get(self)

    def tests_sys_notification_token_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_notification_token_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_notification_token_get_by_id(self)

    def tests_sys_notification_token_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_notification_token_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_notification_token_delete(self)


    def tests_sys_module_02_id2(self):
        if self.check_scenary(["ALL", "SYS", "sys_module_id2"], self.tests_scenary):
            module_tests_sys.sys_module_id2(self)

    def tests_sys_module_01_id1(self):
        if self.check_scenary(["ALL", "SYS", "sys_module_id1"], self.tests_scenary):
            module_tests_sys.sys_module_id1(self)

    def tests_sys_module_03_get(self):
        if self.check_scenary(["ALL", "SYS", "sys_module_get"], self.tests_scenary):
            module_tests_sys.sys_module_get(self)

    def tests_sys_module_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_module_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_module_get_by_id(self)

    def tests_sys_module_05_delete(self):
        if self.check_scenary(["ALL", "SYS", "sys_module_delete"], self.tests_scenary):
            module_tests_sys.sys_module_delete(self)

    def tests_sys_licence_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_licenceget_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_licence_get_by_id(self)

    def tests_sys_licence_02_id2(self):
        if self.check_scenary(["ALL", "SYS", "sys_licence_id2"], self.tests_scenary):
            module_tests_sys.sys_licence_id2(self)

    def tests_sys_licence_01_id1(self):
        if self.check_scenary(["ALL", "SYS", "sys_licence_id1"], self.tests_scenary):
            module_tests_sys.sys_licence_id1(self)

    def tests_sys_licence_03_get(self):
        if self.check_scenary(["ALL", "SYS", "sys_licence_get"], self.tests_scenary):
            module_tests_sys.sys_licence_get(self)

    def tests_sys_02_id2(self):
        if self.check_scenary(["ALL", "SYS", "sys_id2"], self.tests_scenary):
            module_tests_sys.sys_id2(self)

    def tests_sys_01_id1(self):
        if self.check_scenary(["ALL", "SYS", "sys_id1", "sys_id1"], self.tests_scenary):
            module_tests_sys.sys_id1(self)

    def tests_sys_group_02_id2(self):
        if self.check_scenary(["ALL", "SYS", "sys_group_id2"], self.tests_scenary):
            module_tests_sys.sys_group_id2(self)

    def tests_sys_group_01_id1(self):
        if self.check_scenary(["ALL", "SYS", "sys_group_id1"], self.tests_scenary):
            module_tests_sys.sys_group_id1(self)

    def tests_sys_group_03_get(self):
        if self.check_scenary(["ALL", "SYS", "sys_group_get"], self.tests_scenary):
            module_tests_sys.sys_group_get(self)

    def tests_sys_group_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_group_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_group_get_by_id(self)

    def tests_sys_group_05_delete(self):
        if self.check_scenary(["ALL", "SYS", "sys_group_delete"], self.tests_scenary):
            module_tests_sys.sys_group_delete(self)

    def tests_sys_03_get(self):
        if self.check_scenary(["ALL", "SYS", "sys_get"], self.tests_scenary):
            module_tests_sys.sys_get(self)

    def tests_sys_04_get_by_id(self):
        if self.check_scenary(["ALL", "SYS", "sys_get_by_id"], self.tests_scenary):
            module_tests_sys.sys_get_by_id(self)

    def tests_sys_email_log_02_id2(self):
        if self.check_scenary(["ALL", "SYS", "sys_email_log_id2"], self.tests_scenary):
            module_tests_sys.sys_email_log_id2(self)

    def tests_sys_email_log_01_id1(self):
        if self.check_scenary(["ALL", "SYS", "sys_email_log_id1"], self.tests_scenary):
            module_tests_sys.sys_email_log_id1(self)

    def tests_sys_email_log_03_get(self):
        if self.check_scenary(["ALL", "SYS", "sys_email_log_get"], self.tests_scenary):
            module_tests_sys.sys_email_log_get(self)

    def tests_sys_email_log_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_email_log_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_email_log_get_by_id(self)

    def tests_sys_email_log_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_email_log_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_email_log_delete(self)

    def tests_sys_document_user_02_id2(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_user_id2"], self.tests_scenary
        ):
            module_tests_sys.sys_document_user_id2(self)

    def tests_sys_document_user_01_id1(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_user_id1", "sys_document_user_id1"],
            self.tests_scenary,
        ):
            module_tests_sys.sys_document_user_id1(self)

    def tests_sys_document_user_03_get(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_user_get"], self.tests_scenary
        ):
            module_tests_sys.sys_document_user_get(self)

    def tests_sys_document_user_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_user_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_document_user_get_by_id(self)

    def tests_sys_document_user_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_user_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_document_user_delete(self)

    def tests_sys_document_group_02_id2(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_group_id2"], self.tests_scenary
        ):
            module_tests_sys.sys_document_group_id2(self)

    def tests_sys_document_group_01_id1(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_group_id1"], self.tests_scenary
        ):
            module_tests_sys.sys_document_group_id1(self)

    def tests_sys_document_group_03_get(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_group_get"], self.tests_scenary
        ):
            module_tests_sys.sys_document_group_get(self)

    def tests_sys_document_group_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_group_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_document_group_get_by_id(self)

    def tests_sys_document_group_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_group_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_document_group_delete(self)

    def tests_sys_document_category_02_id2(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_category_id2"], self.tests_scenary
        ):
            module_tests_sys.sys_document_category_id2(self)

    def tests_sys_document_category_01_id1(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_category_id1", "sys_document_category_id1"],
            self.tests_scenary,
        ):
            module_tests_sys.sys_document_category_id1(self)

    def tests_sys_document_category_03_get(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_category_get"], self.tests_scenary
        ):
            module_tests_sys.sys_document_category_get(self)

    def tests_sys_document_category_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_category_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_document_category_get_by_id(self)

    def tests_sys_document_category_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_category_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_document_category_delete(self)

    def tests_sys_05_delete(self):
        if self.check_scenary(["ALL", "SYS", "sys_delete"], self.tests_scenary):
            module_tests_sys.sys_delete(self)

    def tests_sys_access_log_02_id2(self):
        if self.check_scenary(["ALL", "SYS", "sys_access_log_id2"], self.tests_scenary):
            module_tests_sys.sys_access_log_id2(self)

    def tests_sys_access_log_01_id1(self):
        if self.check_scenary(["ALL", "SYS", "sys_access_log_id1"], self.tests_scenary):
            module_tests_sys.sys_access_log_id1(self)

    def tests_sys_access_log_03_get(self):
        if self.check_scenary(["ALL", "SYS", "sys_access_log_get"], self.tests_scenary):
            module_tests_sys.sys_access_log_get(self)

    def tests_sys_access_log_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_access_log_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_access_log_get_by_id(self)

    def tests_sys_access_log_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_access_log_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_access_log_delete(self)
        # document

    def tests_sys_document_02_id2(self):
        if self.check_scenary(["ALL", "SYS", "sys_document_id2"], self.tests_scenary):
            module_tests_sys.sys_document_id2(self)

    def tests_sys_document_01_id1(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_id1", "sys_document_id1"], self.tests_scenary
        ):
            module_tests_sys.sys_document_id1(self)

    def tests_sys_document_03_get(self):
        if self.check_scenary(["ALL", "SYS", "sys_document_get"], self.tests_scenary):
            module_tests_sys.sys_document_get(self)

    def tests_sys_document_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_document_get_by_id(self)

    def tests_sys_document_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_document_delete(self)
            # create document

    def tests_sys_document_create1_PDF(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_create1_PDF"], self.tests_scenary
        ):
            module_tests_sys.sys_document_create1_PDF(self)

    def tests_sys_document_create_zip(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_create_zip"], self.tests_scenary
        ):
            module_tests_sys.sys_document_create_zip(self)

    def tests_sys_document_create_xlsx(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_create_xlsx"], self.tests_scenary
        ):
            module_tests_sys.sys_document_create_xlsx(self)

    def tests_sys_document_create_txt(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_create_txt"], self.tests_scenary
        ):
            module_tests_sys.sys_document_create_txt(self)
            # upload

    def tests_sys_document_upload_zip(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_upload_zip"], self.tests_scenary
        ):
            module_tests_sys.sys_document_upload_zip(self)

    def tests_sys_document_upload_xlsx(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_upload_xlsx"], self.tests_scenary
        ):
            module_tests_sys.sys_document_upload_xlsx(self)

    def tests_sys_document_upload_txt(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_upload_txt"], self.tests_scenary
        ):
            module_tests_sys.sys_document_upload_txt(self)

    def tests_sys_document_upload_pdf(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_upload_pdf"], self.tests_scenary
        ):
            module_tests_sys.sys_document_upload_pdf(self)
            # downloads

    def tests_sys_document_download_zip(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_download_zip"], self.tests_scenary
        ):
            module_tests_sys.sys_document_download_zip(self)

    def tests_sys_document_download_xlsx(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_download_xlsx"], self.tests_scenary
        ):
            module_tests_sys.sys_document_download_xlsx(self)

    def tests_sys_document_download_txt(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_download_txt"], self.tests_scenary
        ):
            module_tests_sys.sys_document_download_txt(self)

    def tests_sys_document_download_pdf(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_document_download_pdf"], self.tests_scenary
        ):
            module_tests_sys.sys_document_download_pdf(self)
            # end-document

    def tests_sys_user_program_02_id2(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_program_id2"], self.tests_scenary
        ):
            module_tests_sys.sys_user_program_id2(self)

    def tests_sys_user_program_01_id1(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_program_id1"], self.tests_scenary
        ):
            module_tests_sys.sys_user_program_id1(self)

    def tests_sys_user_program_03_get(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_program_get"], self.tests_scenary
        ):
            module_tests_sys.sys_user_program_get(self)

    def tests_sys_user_program_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_program_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_user_program_get_by_id(self)

    def tests_sys_user_program_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_program_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_user_program_delete(self)

    def tests_sys_user_group_02_id2(self):
        if self.check_scenary(["ALL", "SYS", "sys_user_group_id2"], self.tests_scenary):
            module_tests_sys.sys_user_group_id2(self)

    def tests_sys_user_group_01_id1(self):
        if self.check_scenary(["ALL", "SYS", "sys_user_group_id1"], self.tests_scenary):
            module_tests_sys.sys_user_group_id1(self)

    def tests_sys_user_group_03_get(self):
        if self.check_scenary(["ALL", "SYS", "sys_user_group_get"], self.tests_scenary):
            module_tests_sys.sys_user_group_get(self)

    def tests_sys_user_group_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_group_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_user_group_get_by_id(self)

    def tests_sys_user_group_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_group_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_user_group_delete(self)

    def tests_sys_translate_lang_02_id2(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_translate_lang_id2"], self.tests_scenary
        ):
            module_tests_sys.sys_translate_lang_id2(self)

    def tests_sys_translate_lang_01_id1(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_translate_lang_id1"], self.tests_scenary
        ):
            module_tests_sys.sys_translate_lang_id1(self)

    def tests_sys_translate_lang_03_get(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_translate_lang_get"], self.tests_scenary
        ):
            module_tests_sys.sys_translate_lang_get(self)

    def tests_sys_translate_lang_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_translate_lang_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_translate_lang_get_by_id(self)

    def tests_sys_translate_lang_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_translate_lang_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_translate_lang_delete(self)

    def tests_sys_translate_02_id2(self):
        if self.check_scenary(["ALL", "SYS", "sys_translate_id2"], self.tests_scenary):
            module_tests_sys.sys_translate_id2(self)

    def tests_sys_translate_01_id1(self):
        if self.check_scenary(["ALL", "SYS", "sys_translate_id1"], self.tests_scenary):
            module_tests_sys.sys_translate_id1(self)

    def tests_sys_translate_03_get(self):
        if self.check_scenary(["ALL", "SYS", "sys_translate_get"], self.tests_scenary):
            module_tests_sys.sys_translate_get(self)

    def tests_sys_translate_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_translate_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_translate_get_by_id(self)

    def tests_sys_translate_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_translate_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_translate_delete(self)

    def tests_sys_user_program_action_02_id2(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_program_action_id2"], self.tests_scenary
        ):
            module_tests_sys.sys_user_program_action_id2(self)

    def tests_sys_user_program_action_01_id1(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_program_action_id1"], self.tests_scenary
        ):
            module_tests_sys.sys_user_program_action_id1(self)

    def tests_sys_user_program_action_03_get(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_program_action_get"], self.tests_scenary
        ):
            module_tests_sys.sys_user_program_action_get(self)

    def tests_sys_user_program_action_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_program_action_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_user_program_action_get_by_id(self)

    def tests_sys_user_program_action_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_user_program_action_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_user_program_action_delete(self)

    def tests_sys_program_action_02_id2(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_program_action_id2"], self.tests_scenary
        ):
            module_tests_sys.sys_program_action_id2(self)

    def tests_sys_program_action_01_id1(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_program_action_id1"], self.tests_scenary
        ):
            module_tests_sys.sys_program_action_id1(self)

    def tests_sys_program_action_03_get(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_program_action_get"], self.tests_scenary
        ):
            module_tests_sys.sys_program_action_get(self)

    def tests_sys_program_action_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_program_action_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_program_action_get_by_id(self)

    def tests_sys_program_action_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_program_action_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_program_action_delete(self)

    def tests_sys_group_program_action_02_id2(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_group_program_action_id2"], self.tests_scenary
        ):
            module_tests_sys.sys_group_program_action_id2(self)

    def tests_sys_group_program_action_01_id1(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_group_program_action_id1"], self.tests_scenary
        ):
            module_tests_sys.sys_group_program_action_id1(self)

    def tests_sys_group_program_action_03_get(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_group_program_action_get"], self.tests_scenary
        ):
            module_tests_sys.sys_group_program_action_get(self)

    def tests_sys_group_program_action_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_group_program_action_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_group_program_action_get_by_id(self)

    def tests_sys_group_program_action_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_group_program_action_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_group_program_action_delete(self)

    def tests_sys_dic_02_id2(self):
        if self.check_scenary(["ALL", "SYS", "sys_dic_id2"], self.tests_scenary):
            module_tests_sys.sys_dic_id2(self)

    def tests_sys_dic_01_id1(self):
        if self.check_scenary(["ALL", "SYS", "sys_dic_id1"], self.tests_scenary):
            module_tests_sys.sys_dic_id1(self)

    def tests_sys_dic_03_get(self):
        if self.check_scenary(["ALL", "SYS", "sys_dic_get"], self.tests_scenary):
            module_tests_sys.sys_dic_get(self)

    def tests_sys_dic_04_get_by_id(self):
        if self.check_scenary(["ALL", "SYS", "sys_dic_get_by_id"], self.tests_scenary):
            module_tests_sys.sys_dic_get_by_id(self)

    def tests_sys_dic_05_delete(self):
        if self.check_scenary(["ALL", "SYS", "sys_dic_delete"], self.tests_scenary):
            module_tests_sys.sys_dic_delete(self)

    def tests_sys_action_02_id2(self):
        if self.check_scenary(["ALL", "SYS", "sys_action_id2"], self.tests_scenary):
            module_tests_sys.sys_action_id2(self)

    def tests_sys_action_01_id1(self):
        if self.check_scenary(["ALL", "SYS", "sys_action_id1"], self.tests_scenary):
            module_tests_sys.sys_action_id1(self)

    def tests_sys_action_03_get(self):
        if self.check_scenary(["ALL", "SYS", "sys_action_get"], self.tests_scenary):
            module_tests_sys.sys_action_get(self)

    def tests_sys_action_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_action_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_action_get_by_id(self)

    def tests_sys_action_05_delete(self):
        if self.check_scenary(["ALL", "SYS", "sys_action_delete"], self.tests_scenary):
            module_tests_sys.sys_action_delete(self)

    def tests_sys_unit_manager_02_id2(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_unit_manager_id2"], self.tests_scenary
        ):
            module_tests_sys.sys_unit_manager_id2(self)

    def tests_sys_unit_manager_01_id1(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_unit_manager_id1"], self.tests_scenary
        ):
            module_tests_sys.sys_unit_manager_id1(self)

    def tests_sys_unit_manager_03_get(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_unit_manager_get"], self.tests_scenary
        ):
            module_tests_sys.sys_unit_manager_get(self)

    def tests_sys_unit_manager_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_unit_manager_get_by_id"], self.tests_scenary
        ):
            module_tests_sys.sys_unit_manager_get_by_id(self)

    def tests_sys_unit_manager_05_delete(self):
        if self.check_scenary(
            ["ALL", "SYS", "sys_unit_manager_delete"], self.tests_scenary
        ):
            module_tests_sys.sys_unit_manager_delete(self)

    # ===========================================================
    # GER
    # ===========================================================

    def tests_ger_unit_param_02_id2(self):
        if self.check_scenary(["ALL", "GER", "ger_unit_param_id2"], self.tests_scenary):
            module_tests_ger.ger_unit_param_id2(self)

    def tests_ger_unit_param_01_id1(self):
        if self.check_scenary(["ALL", "GER", "ger_unit_param_id1"], self.tests_scenary):
            module_tests_ger.ger_unit_param_id1(self)

    def tests_ger_unit_param_03_get(self):
        if self.check_scenary(["ALL", "GER", "ger_unit_param_get"], self.tests_scenary):
            module_tests_ger.ger_unit_param_get(self)

    def tests_ger_unit_param_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_unit_param_get_by_id"], self.tests_scenary
        ):
            module_tests_ger.ger_unit_param_get_by_id(self)

    def tests_ger_unit_param_05_delete(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_unit_param_delete"], self.tests_scenary
        ):
            module_tests_ger.ger_unit_param_delete(self)

    def tests_ger_umedida_02_id2(self):
        if self.check_scenary(["ALL", "GER", "ger_umedida_id2"], self.tests_scenary):
            module_tests_ger.ger_umedida_id2(self)

    def tests_ger_umedida_01_id1(self):
        if self.check_scenary(["ALL", "GER", "ger_umedida_id1"], self.tests_scenary):
            module_tests_ger.ger_umedida_id1(self)

    def tests_ger_umedida_03_get(self):
        if self.check_scenary(["ALL", "GER", "ger_umedida_get"], self.tests_scenary):
            module_tests_ger.ger_umedida_get(self)

    def tests_ger_umedida_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_umedida_get_by_id"], self.tests_scenary
        ):
            module_tests_ger.ger_umedida_get_by_id(self)

    def tests_ger_umedida_05_delete(self):
        if self.check_scenary(["ALL", "GER", "ger_umedida_delete"], self.tests_scenary):
            module_tests_ger.ger_umedida_delete(self)

    def tests_ger_processo_bloq_02_id2(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_processo_bloq_id2"], self.tests_scenary
        ):
            module_tests_ger.ger_processo_bloq_id2(self)

    def tests_ger_processo_bloq_01_id1(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_processo_bloq_id1"], self.tests_scenary
        ):
            module_tests_ger.ger_processo_bloq_id1(self)

    def tests_ger_processo_bloq_03_get(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_processo_bloq_get"], self.tests_scenary
        ):
            module_tests_ger.ger_processo_bloq_get(self)

    def tests_ger_processo_bloq_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_processo_bloq_get_by_id"], self.tests_scenary
        ):
            module_tests_ger.ger_processo_bloq_get_by_id(self)

    def tests_ger_processo_bloq_05_delete(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_processo_bloq_delete"], self.tests_scenary
        ):
            module_tests_ger.ger_processo_bloq_delete(self)

    def tests_ger_pessoa_02_id2(self):
        if self.check_scenary(["ALL", "GER", "ger_pessoa_id2"], self.tests_scenary):
            module_tests_ger.ger_pessoa_id2(self)

    def tests_ger_pessoa_01_id1(self):
        if self.check_scenary(["ALL", "GER", "ger_pessoa_id1"], self.tests_scenary):
            module_tests_ger.ger_pessoa_id1(self)

    def tests_ger_pessoa_03_get(self):
        if self.check_scenary(["ALL", "GER", "ger_pessoa_get"], self.tests_scenary):
            module_tests_ger.ger_pessoa_get(self)

    def tests_ger_pessoa_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_pessoa_get_by_id"], self.tests_scenary
        ):
            module_tests_ger.ger_pessoa_get_by_id(self)

    def tests_ger_pessoa_05_delete(self):
        if self.check_scenary(["ALL", "GER", "ger_pessoa_delete"], self.tests_scenary):
            module_tests_ger.ger_pessoa_delete(self)

    def tests_ger_per_02_id2(self):
        if self.check_scenary(["ALL", "GER", "ger_per_id2"], self.tests_scenary):
            module_tests_ger.ger_per_id2(self)

    def tests_ger_per_01_id1(self):
        if self.check_scenary(["ALL", "GER", "ger_per_id1"], self.tests_scenary):
            module_tests_ger.ger_per_id1(self)

    def tests_ger_per_03_get(self):
        if self.check_scenary(["ALL", "GER", "ger_per_get"], self.tests_scenary):
            module_tests_ger.ger_per_get(self)

    def tests_ger_per_04_get_by_id(self):
        if self.check_scenary(["ALL", "GER", "ger_per_get_by_id"], self.tests_scenary):
            module_tests_ger.ger_per_get_by_id(self)

    def tests_ger_per_05_delete(self):
        if self.check_scenary(["ALL", "GER", "ger_per_delete"], self.tests_scenary):
            module_tests_ger.ger_per_delete(self)

    def tests_ger_pais_02_id2(self):
        if self.check_scenary(["ALL", "GER", "ger_pais_id2"], self.tests_scenary):
            module_tests_ger.ger_pais_id2(self)

    def tests_ger_pais_01_id1(self):
        if self.check_scenary(["ALL", "GER", "ger_pais_id1"], self.tests_scenary):
            module_tests_ger.ger_pais_id1(self)

    def tests_ger_pais_03_get(self):
        if self.check_scenary(["ALL", "GER", "ger_pais_get"], self.tests_scenary):
            module_tests_ger.ger_pais_get(self)

    def tests_ger_pais_04_get_by_id(self):
        if self.check_scenary(["ALL", "GER", "ger_pais_get_by_id"], self.tests_scenary):
            module_tests_ger.ger_pais_get_by_id(self)

    def tests_ger_pais_05_delete(self):
        if self.check_scenary(["ALL", "GER", "ger_pais_delete"], self.tests_scenary):
            module_tests_ger.ger_pais_delete(self)

    def tests_ger_numeracao_02_id2(self):
        if self.check_scenary(["ALL", "GER", "ger_numeracao_id2"], self.tests_scenary):
            module_tests_ger.ger_numeracao_id2(self)

    def tests_ger_numeracao_01_id1(self):
        if self.check_scenary(["ALL", "GER", "ger_numeracao_id1"], self.tests_scenary):
            module_tests_ger.ger_numeracao_id1(self)

    def tests_ger_numeracao_03_get(self):
        if self.check_scenary(["ALL", "GER", "ger_numeracao_get"], self.tests_scenary):
            module_tests_ger.ger_numeracao_get(self)

    def tests_ger_numeracao_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_numeracao_get_by_id"], self.tests_scenary
        ):
            module_tests_ger.ger_numeracao_get_by_id(self)

    def tests_ger_numeracao_05_delete(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_numeracao_delete"], self.tests_scenary
        ):
            module_tests_ger.ger_numeracao_delete(self)

    def tests_ger_marca_02_id2(self):
        if self.check_scenary(["ALL", "GER", "ger_marca_id2"], self.tests_scenary):
            module_tests_ger.ger_marca_id2(self)

    def tests_ger_marca_01_id1(self):
        if self.check_scenary(["ALL", "GER", "ger_marca_id1"], self.tests_scenary):
            module_tests_ger.ger_marca_id1(self)

    def tests_ger_marca_03_get(self):
        if self.check_scenary(["ALL", "GER", "ger_marca_get"], self.tests_scenary):
            module_tests_ger.ger_marca_get(self)

    def tests_ger_marca_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_marca_get_by_id"], self.tests_scenary
        ):
            module_tests_ger.ger_marca_get_by_id(self)

    def tests_ger_marca_05_delete(self):
        if self.check_scenary(["ALL", "GER", "ger_marca_delete"], self.tests_scenary):
            module_tests_ger.ger_marca_delete(self)

    def tests_ger_itemserv_var_02_id2(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_itemserv_var_id2"], self.tests_scenary
        ):
            module_tests_ger.ger_itemserv_var_id2(self)

    def tests_ger_itemserv_var_01_id1(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_itemserv_var_id1"], self.tests_scenary
        ):
            module_tests_ger.ger_itemserv_var_id1(self)

    def tests_ger_itemserv_var_03_get(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_itemserv_var_get"], self.tests_scenary
        ):
            module_tests_ger.ger_itemserv_var_get(self)

    def tests_ger_itemserv_var_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_itemserv_var_get_by_id"], self.tests_scenary
        ):
            module_tests_ger.ger_itemserv_var_get_by_id(self)

    def tests_ger_itemserv_var_05_delete(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_itemserv_var_delete"], self.tests_scenary
        ):
            module_tests_ger.ger_itemserv_var_delete(self)

    def tests_ger_itemserv_02_id2(self):
        if self.check_scenary(["ALL", "GER", "ger_itemserv_id2"], self.tests_scenary):
            module_tests_ger.ger_itemserv_id2(self)

    def tests_ger_itemserv_01_id1(self):
        if self.check_scenary(["ALL", "GER", "ger_itemserv_id1"], self.tests_scenary):
            module_tests_ger.ger_itemserv_id1(self)

    def tests_ger_itemserv_grupo_02_id2(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_itemserv_grupo_id2"], self.tests_scenary
        ):
            module_tests_ger.ger_itemserv_grupo_id2(self)

    def tests_ger_itemserv_grupo_01_id1(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_itemserv_grupo_id1"], self.tests_scenary
        ):
            module_tests_ger.ger_itemserv_grupo_id1(self)

    def tests_ger_itemserv_grupo_03_get(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_itemserv_grupo_get"], self.tests_scenary
        ):
            module_tests_ger.ger_itemserv_grupo_get(self)

    def tests_ger_itemserv_grupo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_itemserv_grupo_get_by_id"], self.tests_scenary
        ):
            module_tests_ger.ger_itemserv_grupo_get_by_id(self)

    def tests_ger_itemserv_grupo_05_delete(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_itemserv_grupo_delete"], self.tests_scenary
        ):
            module_tests_ger.ger_itemserv_grupo_delete(self)

    def tests_ger_itemserv_03_get(self):
        if self.check_scenary(["ALL", "GER", "ger_itemserv_get"], self.tests_scenary):
            module_tests_ger.ger_itemserv_get(self)

    def tests_ger_itemserv_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_itemserv_get_by_id"], self.tests_scenary
        ):
            module_tests_ger.ger_itemserv_get_by_id(self)

    def tests_ger_itemserv_05_delete(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_itemserv_delete"], self.tests_scenary
        ):
            module_tests_ger.ger_itemserv_delete(self)

    def tests_ger_itemserv_compos_02_id2(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_itemserv_compos_id2"], self.tests_scenary
        ):
            module_tests_ger.ger_itemserv_compos_id2(self)

    def tests_ger_itemserv_compos_01_id1(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_itemserv_compos_id1"], self.tests_scenary
        ):
            module_tests_ger.ger_itemserv_compos_id1(self)

    def tests_ger_itemserv_compos_03_get(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_itemserv_compos_get"], self.tests_scenary
        ):
            module_tests_ger.ger_itemserv_compos_get(self)

    def tests_ger_itemserv_compos_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_itemserv_compos_get_by_id"], self.tests_scenary
        ):
            module_tests_ger.ger_itemserv_compos_get_by_id(self)

    def tests_ger_itemserv_compos_05_delete(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_itemserv_compos_delete"], self.tests_scenary
        ):
            module_tests_ger.ger_itemserv_compos_delete(self)

    def tests_ger_index_mov_02_id2(self):
        if self.check_scenary(["ALL", "GER", "ger_index_mov_id2"], self.tests_scenary):
            module_tests_ger.ger_index_mov_id2(self)

    def tests_ger_index_mov_03_get(self):
        if self.check_scenary(["ALL", "GER", "ger_index_mov_get"], self.tests_scenary):
            module_tests_ger.ger_index_mov_get(self)

    def tests_ger_index_mov_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_index_mov_get_by_id"], self.tests_scenary
        ):
            module_tests_ger.ger_index_mov_get_by_id(self)

    def tests_ger_index_mov_05_delete(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_index_mov_delete"], self.tests_scenary
        ):
            module_tests_ger.ger_index_mov_delete(self)

    def tests_ger_index_02_id2(self):
        if self.check_scenary(["ALL", "GER", "ger_index_id2"], self.tests_scenary):
            module_tests_ger.ger_index_id2(self)

    def tests_ger_index_01_id1(self):
        if self.check_scenary(["ALL", "GER", "ger_index_id1"], self.tests_scenary):
            module_tests_ger.ger_index_id1(self)

    def tests_ger_index_03_get(self):
        if self.check_scenary(["ALL", "GER", "ger_index_get"], self.tests_scenary):
            module_tests_ger.ger_index_get(self)

    def tests_ger_index_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_index_get_by_id"], self.tests_scenary
        ):
            module_tests_ger.ger_index_get_by_id(self)

    def tests_ger_index_05_delete(self):
        if self.check_scenary(["ALL", "GER", "ger_index_delete"], self.tests_scenary):
            module_tests_ger.ger_index_delete(self)

    def tests_ger_est_nivel_02_id2(self):
        if self.check_scenary(["ALL", "GER", "ger_est_nivel_id2"], self.tests_scenary):
            module_tests_ger.ger_est_nivel_id2(self)

    def tests_ger_est_nivel_01_id1(self):
        if self.check_scenary(["ALL", "GER", "ger_est_nivel_id1"], self.tests_scenary):
            module_tests_ger.ger_est_nivel_id1(self)

    def tests_ger_est_nivel_03_get(self):
        if self.check_scenary(["ALL", "GER", "ger_est_nivel_get"], self.tests_scenary):
            module_tests_ger.ger_est_nivel_get(self)

    def tests_ger_est_nivel_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_est_nivel_get_by_id"], self.tests_scenary
        ):
            module_tests_ger.ger_est_nivel_get_by_id(self)

    def tests_ger_est_nivel_05_delete(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_est_nivel_delete"], self.tests_scenary
        ):
            module_tests_ger.ger_est_nivel_delete(self)

    def tests_ger_empresa_02_id2(self):
        if self.check_scenary(["ALL", "GER", "ger_empresa_id2"], self.tests_scenary):
            module_tests_ger.ger_empresa_id2(self)

    def tests_ger_empresa_01_id1(self):
        if self.check_scenary(["ALL", "GER", "ger_empresa_id1"], self.tests_scenary):
            module_tests_ger.ger_empresa_id1(self)

    def tests_ger_empresa_grupo_02_id2(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_empresa_grupo_id2"], self.tests_scenary
        ):
            module_tests_ger.ger_empresa_grupo_id2(self)

    def tests_ger_empresa_grupo_01_id1(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_empresa_grupo_id1"], self.tests_scenary
        ):
            module_tests_ger.ger_empresa_grupo_id1(self)

    def tests_ger_empresa_grupo_03_get(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_empresa_grupo_get"], self.tests_scenary
        ):
            module_tests_ger.ger_empresa_grupo_get(self)

    def tests_ger_empresa_grupo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_empresa_grupo_get_by_id"], self.tests_scenary
        ):
            module_tests_ger.ger_empresa_grupo_get_by_id(self)

    def tests_ger_empresa_grupo_05_delete(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_empresa_grupo_delete"], self.tests_scenary
        ):
            module_tests_ger.ger_empresa_grupo_delete(self)

    def tests_ger_empresa_03_get(self):
        if self.check_scenary(["ALL", "GER", "ger_empresa_get"], self.tests_scenary):
            module_tests_ger.ger_empresa_get(self)

    def tests_ger_empresa_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_empresa_get_by_id"], self.tests_scenary
        ):
            module_tests_ger.ger_empresa_get_by_id(self)

    def tests_ger_empresa_05_delete(self):
        if self.check_scenary(["ALL", "GER", "ger_empresa_delete"], self.tests_scenary):
            module_tests_ger.ger_empresa_delete(self)

    def tests_ger_device_02_id2(self):
        if self.check_scenary(["ALL", "GER", "ger_device_id2"], self.tests_scenary):
            module_tests_ger.ger_device_id2(self)

    def tests_ger_device_01_id1(self):
        if self.check_scenary(["ALL", "GER", "ger_device_id1"], self.tests_scenary):
            module_tests_ger.ger_device_id1(self)

    def tests_ger_device_03_get(self):
        if self.check_scenary(["ALL", "GER", "ger_device_get"], self.tests_scenary):
            module_tests_ger.ger_device_get(self)

    def tests_ger_device_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_device_get_by_id"], self.tests_scenary
        ):
            module_tests_ger.ger_device_get_by_id(self)

    def tests_ger_device_05_delete(self):
        if self.check_scenary(["ALL", "GER", "ger_device_delete"], self.tests_scenary):
            module_tests_ger.ger_device_delete(self)

    def tests_ger_cidade_02_id2(self):
        if self.check_scenary(["ALL", "GER", "ger_cidade_id2"], self.tests_scenary):
            module_tests_ger.ger_cidade_id2(self)

    def tests_ger_cidade_01_id1(self):
        if self.check_scenary(["ALL", "GER", "ger_cidade_id1"], self.tests_scenary):
            module_tests_ger.ger_cidade_id1(self)

    def tests_ger_cidade_03_get(self):
        if self.check_scenary(["ALL", "GER", "ger_cidade_get"], self.tests_scenary):
            module_tests_ger.ger_cidade_get(self)

    def tests_ger_cidade_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_cidade_get_by_id"], self.tests_scenary
        ):
            module_tests_ger.ger_cidade_get_by_id(self)

    def tests_ger_cidade_05_delete(self):
        if self.check_scenary(["ALL", "GER", "ger_cidade_delete"], self.tests_scenary):
            module_tests_ger.ger_cidade_delete(self)

    def ger_per_tipo_id2(self):
        if self.check_scenary(["ALL", "GER", "ger_per_tipo_id2"], self.tests_scenary):
            module_tests_ger.ger_per_tipo_id2(self)

    def ger_per_tipo_id1(self):
        if self.check_scenary(["ALL", "GER", "ger_per_tipo_id1"], self.tests_scenary):
            module_tests_ger.ger_per_tipo_id1(self)

    def ger_per_tipo_get(self):
        if self.check_scenary(["ALL", "GER", "ger_per_tipo_get"], self.tests_scenary):
            module_tests_ger.ger_per_tipo_get(self)

    def ger_per_tipo_get_by_id(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_per_tipo_get_by_id"], self.tests_scenary
        ):
            module_tests_ger.ger_per_tipo_get_by_id(self)

    def ger_per_tipo_delete(self):
        if self.check_scenary(
            ["ALL", "GER", "ger_per_tipo_delete"], self.tests_scenary
        ):
            module_tests_ger.ger_per_tipo_delete(self)

    # ===========================================================
    # FIN
    # ===========================================================

    def tests_fin_banco_05_delete(self):
        if self.check_scenary(["ALL", "FIN", "fin_banco_delete"], self.tests_scenary):
            module_tests_fin.fin_banco_delete(self)

    def tests_fin_banco_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_banco_get_by_id"], self.tests_scenary
        ):
            module_tests_fin.fin_banco_get_by_id(self)

    def tests_fin_banco_03_get(self):
        if self.check_scenary(["ALL", "FIN", "fin_banco_get"], self.tests_scenary):
            module_tests_fin.fin_banco_get(self)

    def tests_fin_banco_01_id1(self):
        if self.check_scenary(["ALL", "FIN", "fin_banco_id1"], self.tests_scenary):
            module_tests_fin.fin_banco_id1(self)

    def tests_fin_banco_02_id2(self):
        if self.check_scenary(["ALL", "FIN", "fin_banco_id2"], self.tests_scenary):
            module_tests_fin.fin_banco_id2(self)

    def tests_fin_class_agrup_05_delete(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_class_agrup_delete"], self.tests_scenary
        ):
            module_tests_fin.fin_class_agrup_delete(self)

    def tests_fin_class_agrup_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_class_agrup_get_by_id"], self.tests_scenary
        ):
            module_tests_fin.fin_class_agrup_get_by_id(self)

    def tests_fin_class_agrup_03_get(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_class_agrup_get"], self.tests_scenary
        ):
            module_tests_fin.fin_class_agrup_get(self)

    def tests_fin_class_agrup_02_id2(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_class_agrup_id2"], self.tests_scenary
        ):
            module_tests_fin.fin_class_agrup_id2(self)

    def tests_fin_class_agrup_01_id1(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_class_agrup_id1"], self.tests_scenary
        ):
            module_tests_fin.fin_class_agrup_id1(self)

    def tests_fin_class_05_delete(self):
        if self.check_scenary(["ALL", "FIN", "fin_class_delete"], self.tests_scenary):
            module_tests_fin.fin_class_delete(self)

    def tests_fin_class_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_class_get_by_id"], self.tests_scenary
        ):
            module_tests_fin.fin_class_get_by_id(self)

    def tests_fin_class_03_get(self):
        if self.check_scenary(["ALL", "FIN", "fin_class_get"], self.tests_scenary):
            module_tests_fin.fin_class_get(self)

    def tests_fin_class_grupo_05_delete(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_class_grupo_delete"], self.tests_scenary
        ):
            module_tests_fin.fin_class_grupo_delete(self)

    def tests_fin_class_grupo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_class_grupo_get_by_id"], self.tests_scenary
        ):
            module_tests_fin.fin_class_grupo_get_by_id(self)

    def tests_fin_class_grupo_03_get(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_class_grupo_get"], self.tests_scenary
        ):
            module_tests_fin.fin_class_grupo_get(self)

    def tests_fin_class_grupo_01_id1(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_class_grupo_id1"], self.tests_scenary
        ):
            module_tests_fin.fin_class_grupo_id1(self)

    def tests_fin_class_grupo_02_id2(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_class_grupo_id2"], self.tests_scenary
        ):
            module_tests_fin.fin_class_grupo_id2(self)

    def tests_fin_class_01_id1(self):
        if self.check_scenary(["ALL", "FIN", "fin_class_id1"], self.tests_scenary):
            module_tests_fin.fin_class_id1(self)

    def tests_fin_class_02_id2(self):
        if self.check_scenary(["ALL", "FIN", "fin_class_id2"], self.tests_scenary):
            module_tests_fin.fin_class_id2(self)

    def tests_fin_cond_pagrec_config_05_delete(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_cond_pagrec_config_delete"], self.tests_scenary
        ):
            module_tests_fin.fin_cond_pagrec_config_delete(self)

    def tests_fin_cond_pagrec_config_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_cond_pagrec_config_get_by_id"], self.tests_scenary
        ):
            module_tests_fin.fin_cond_pagrec_config_get_by_id(self)

    def tests_fin_cond_pagrec_config_03_get(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_cond_pagrec_config_get"], self.tests_scenary
        ):
            module_tests_fin.fin_cond_pagrec_config_get(self)

    def tests_fin_cond_pagrec_config_01_id1(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_cond_pagrec_config_id1"], self.tests_scenary
        ):
            module_tests_fin.fin_cond_pagrec_config_id1(self)

    def tests_fin_cond_pagrec_config_02_id2(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_cond_pagrec_config_id2"], self.tests_scenary
        ):
            module_tests_fin.fin_cond_pagrec_config_id2(self)

    def tests_fin_cond_pagrec_05_delete(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_cond_pagrec_delete"], self.tests_scenary
        ):
            module_tests_fin.fin_cond_pagrec_delete(self)

    def tests_fin_cond_pagrec_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_cond_pagrec_get_by_id"], self.tests_scenary
        ):
            module_tests_fin.fin_cond_pagrec_get_by_id(self)

    def tests_fin_cond_pagrec_03_get(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_cond_pagrec_get"], self.tests_scenary
        ):
            module_tests_fin.fin_cond_pagrec_get(self)

    def tests_fin_cond_pagrec_01_id1(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_cond_pagrec_id1"], self.tests_scenary
        ):
            module_tests_fin.fin_cond_pagrec_id1(self)

    def tests_fin_cond_pagrec_02_id2(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_cond_pagrec_id2"], self.tests_scenary
        ):
            module_tests_fin.fin_cond_pagrec_id2(self)

    def tests_fin_conta_05_delete(self):
        if self.check_scenary(["ALL", "FIN", "fin_conta_delete"], self.tests_scenary):
            module_tests_fin.fin_conta_delete(self)

    def tests_fin_conta_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_conta_get_by_id"], self.tests_scenary
        ):
            module_tests_fin.fin_conta_get_by_id(self)

    def tests_fin_conta_03_get(self):
        if self.check_scenary(["ALL", "FIN", "fin_conta_get"], self.tests_scenary):
            module_tests_fin.fin_conta_get(self)

    def tests_fin_conta_01_id1(self):
        if self.check_scenary(["ALL", "FIN", "fin_conta_id1"], self.tests_scenary):
            module_tests_fin.fin_conta_id1(self)

    def tests_fin_conta_02_id2(self):
        if self.check_scenary(["ALL", "FIN", "fin_conta_id2"], self.tests_scenary):
            module_tests_fin.fin_conta_id2(self)

    def tests_fin_doc_tipo_05_delete(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_doc_tipo_delete"], self.tests_scenary
        ):
            module_tests_fin.fin_doc_tipo_delete(self)

    def tests_fin_doc_tipo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_doc_tipo_get_by_id"], self.tests_scenary
        ):
            module_tests_fin.fin_doc_tipo_get_by_id(self)

    def tests_fin_doc_tipo_03_get(self):
        if self.check_scenary(["ALL", "FIN", "fin_doc_tipo_get"], self.tests_scenary):
            module_tests_fin.fin_doc_tipo_get(self)

    def tests_fin_doc_tipo_01_id1(self):
        if self.check_scenary(["ALL", "FIN", "fin_doc_tipo_id1"], self.tests_scenary):
            module_tests_fin.fin_doc_tipo_id1(self)

    def tests_fin_doc_tipo_02_id2(self):
        if self.check_scenary(["ALL", "FIN", "fin_doc_tipo_id2"], self.tests_scenary):
            module_tests_fin.fin_doc_tipo_id2(self)

    def tests_fin_lote_05_delete(self):
        if self.check_scenary(["ALL", "FIN", "fin_lote_delete"], self.tests_scenary):
            module_tests_fin.fin_lote_delete(self)

    def tests_fin_lote_04_get_by_id(self):
        if self.check_scenary(["ALL", "FIN", "fin_lote_get_by_id"], self.tests_scenary):
            module_tests_fin.fin_lote_get_by_id(self)

    def tests_fin_lote_03_get(self):
        if self.check_scenary(["ALL", "FIN", "fin_lote_get"], self.tests_scenary):
            module_tests_fin.fin_lote_get(self)

    def tests_fin_lote_01_id1(self):
        if self.check_scenary(["ALL", "FIN", "fin_lote_id1"], self.tests_scenary):
            module_tests_fin.fin_lote_id1(self)

    def tests_fin_lote_02_id2(self):
        if self.check_scenary(["ALL", "FIN", "fin_lote_id2"], self.tests_scenary):
            module_tests_fin.fin_lote_id2(self)

    def tests_fin_pagrec_baixa_05_delete(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_baixa_delete"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_baixa_delete(self)

    def tests_fin_pagrec_baixa_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_baixa_get_by_id"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_baixa_get_by_id(self)

    def tests_fin_pagrec_baixa_03_get(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_baixa_get"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_baixa_get(self)

    def tests_fin_pagrec_baixa_01_id1(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_baixa_id1"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_baixa_id1(self)

    def tests_fin_pagrec_baixa_02_id2(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_baixa_id2"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_baixa_id2(self)

    def tests_fin_pagrec_banco_05_delete(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_banco_delete"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_banco_delete(self)

    def tests_fin_pagrec_banco_extrato_05_delete(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_banco_extrato_delete"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_banco_extrato_delete(self)

    def tests_fin_pagrec_banco_extrato_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_banco_extrato_get_by_id"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_banco_extrato_get_by_id(self)

    def tests_fin_pagrec_banco_extrato_03_get(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_banco_extrato_get"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_banco_extrato_get(self)

    def tests_fin_pagrec_banco_extrato_01_id1(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_banco_extrato_id1"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_banco_extrato_id1(self)

    def tests_fin_pagrec_banco_extrato_02_id2(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_banco_extrato_id2"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_banco_extrato_id2(self)

    def tests_fin_pagrec_banco_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_banco_get_by_id"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_banco_get_by_id(self)

    def tests_fin_pagrec_banco_03_get(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_banco_get"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_banco_get(self)

    def tests_fin_pagrec_banco_01_id1(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_banco_id1"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_banco_id1(self)

    def tests_fin_pagrec_banco_02_id2(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_banco_id2"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_banco_id2(self)

    def tests_fin_pagrec_banco_transf_05_delete(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_banco_transf_delete"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_banco_transf_delete(self)

    def tests_fin_pagrec_banco_transf_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_banco_transf_get_by_id"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_banco_transf_get_by_id(self)

    def tests_fin_pagrec_banco_transf_03_get(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_banco_transf_get"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_banco_transf_get(self)

    def tests_fin_pagrec_banco_transf_01_id1(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_banco_transf_id1"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_banco_transf_id1(self)

    def tests_fin_pagrec_banco_transf_02_id2(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_banco_transf_id2"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_banco_transf_id2(self)

    def tests_fin_pagrec_class_05_delete(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_class_delete"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_class_delete(self)

    def tests_fin_pagrec_class_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_class_get_by_id"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_class_get_by_id(self)

    def tests_fin_pagrec_class_03_get(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_class_get"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_class_get(self)

    def tests_fin_pagrec_class_01_id1(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_class_id1"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_class_id1(self)

    def tests_fin_pagrec_class_02_id2(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_class_id2"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_class_id2(self)

    def tests_fin_pagrec_05_delete(self):
        if self.check_scenary(["ALL", "FIN", "fin_pagrec_delete"], self.tests_scenary):
            module_tests_fin.fin_pagrec_delete(self)

    def tests_fin_pagrec_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_get_by_id"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_get_by_id(self)

    def tests_fin_pagrec_03_get(self):
        if self.check_scenary(["ALL", "FIN", "fin_pagrec_get"], self.tests_scenary):
            module_tests_fin.fin_pagrec_get(self)

    def tests_fin_pagrec_01_id1(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_id1", "fin_pagrec_id1"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_id1(self)

    def tests_fin_pagrec_02_id2(self):
        if self.check_scenary(["ALL", "FIN", "fin_pagrec_id2"], self.tests_scenary):
            module_tests_fin.fin_pagrec_id2(self)

    def tests_fin_pagrec_origem_05_delete(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_origem_delete"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_origem_delete(self)

    def tests_fin_pagrec_origem_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_origem_get_by_id"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_origem_get_by_id(self)

    def tests_fin_pagrec_origem_03_get(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_origem_get"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_origem_get(self)

    def tests_fin_pagrec_origem_01_id1(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_origem_id1"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_origem_id1(self)

    def tests_fin_pagrec_origem_02_id2(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_origem_id2"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_origem_id2(self)

    def tests_fin_pagrec_prev_05_delete(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_prev_delete"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_prev_delete(self)

    def tests_fin_pagrec_prev_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_prev_get_by_id"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_prev_get_by_id(self)

    def tests_fin_pagrec_prev_03_get(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_prev_get"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_prev_get(self)

    def tests_fin_pagrec_prev_01_id1(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_prev_id1"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_prev_id1(self)

    def tests_fin_pagrec_prev_02_id2(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_prev_id2"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_prev_id2(self)

    def tests_fin_pagrec_tipo_05_delete(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_tipo_delete"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_tipo_delete(self)

    def tests_fin_pagrec_tipo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_tipo_get_by_id"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_tipo_get_by_id(self)

    def tests_fin_pagrec_tipo_03_get(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_tipo_get"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_tipo_get(self)

    def tests_fin_pagrec_tipo_01_id1(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_tipo_id1"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_tipo_id1(self)

    def tests_fin_pagrec_tipo_02_id2(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_tipo_id2"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_tipo_id2(self)

    def tests_fin_pagrec_versao_05_delete(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_versao_delete"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_versao_delete(self)

    def tests_fin_pagrec_versao_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_versao_get_by_id"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_versao_get_by_id(self)

    def tests_fin_pagrec_versao_03_get(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_versao_get"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_versao_get(self)

    def tests_fin_pagrec_versao_01_id1(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_versao_id1"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_versao_id1(self)

    def tests_fin_pagrec_versao_02_id2(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_pagrec_versao_id2"], self.tests_scenary
        ):
            module_tests_fin.fin_pagrec_versao_id2(self)

    def tests_fin_recibo_05_delete(self):
        if self.check_scenary(["ALL", "FIN", "fin_recibo_delete"], self.tests_scenary):
            module_tests_fin.fin_recibo_delete(self)

    def tests_fin_recibo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_recibo_get_by_id"], self.tests_scenary
        ):
            module_tests_fin.fin_recibo_get_by_id(self)

    def tests_fin_recibo_03_get(self):
        if self.check_scenary(["ALL", "FIN", "fin_recibo_get"], self.tests_scenary):
            module_tests_fin.fin_recibo_get(self)

    def tests_fin_recibo_01_id1(self):
        if self.check_scenary(["ALL", "FIN", "fin_recibo_id1"], self.tests_scenary):
            module_tests_fin.fin_recibo_id1(self)

    def tests_fin_recibo_02_id2(self):
        if self.check_scenary(["ALL", "FIN", "fin_recibo_id2"], self.tests_scenary):
            module_tests_fin.fin_recibo_id2(self)

    def tests_fin_recibo_tipo_05_delete(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_recibo_tipo_delete"], self.tests_scenary
        ):
            module_tests_fin.fin_recibo_tipo_delete(self)

    def tests_fin_recibo_tipo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_recibo_tipo_get_by_id"], self.tests_scenary
        ):
            module_tests_fin.fin_recibo_tipo_get_by_id(self)

    def tests_fin_recibo_tipo_03_get(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_recibo_tipo_get"], self.tests_scenary
        ):
            module_tests_fin.fin_recibo_tipo_get(self)

    def tests_fin_recibo_tipo_01_id1(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_recibo_tipo_id1"], self.tests_scenary
        ):
            module_tests_fin.fin_recibo_tipo_id1(self)

    def tests_fin_recibo_tipo_02_id2(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_recibo_tipo_id2"], self.tests_scenary
        ):
            module_tests_fin.fin_recibo_tipo_id2(self)

    def tests_fin_tipo_variacao_05_delete(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_tipo_variacao_delete"], self.tests_scenary
        ):
            module_tests_fin.fin_tipo_variacao_delete(self)

    def tests_fin_tipo_variacao_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_tipo_variacao_get_by_id"], self.tests_scenary
        ):
            module_tests_fin.fin_tipo_variacao_get_by_id(self)

    def tests_fin_tipo_variacao_03_get(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_tipo_variacao_get"], self.tests_scenary
        ):
            module_tests_fin.fin_tipo_variacao_get(self)

    def tests_fin_tipo_variacao_01_id1(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_tipo_variacao_id1"], self.tests_scenary
        ):
            module_tests_fin.fin_tipo_variacao_id1(self)

    def tests_fin_tipo_variacao_02_id2(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_tipo_variacao_id2"], self.tests_scenary
        ):
            module_tests_fin.fin_tipo_variacao_id2(self)

    def tests_fin_unit_param_05_delete(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_unit_param_delete"], self.tests_scenary
        ):
            module_tests_fin.fin_unit_param_delete(self)

    def tests_fin_unit_param_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIN", "fin_unit_param_get_by_id"], self.tests_scenary
        ):
            module_tests_fin.fin_unit_param_get_by_id(self)

    def tests_fin_unit_param_03_get(self):
        if self.check_scenary(["ALL", "FIN", "fin_unit_param_get"], self.tests_scenary):
            module_tests_fin.fin_unit_param_get(self)

    def tests_fin_unit_param_01_id1(self):
        if self.check_scenary(["ALL", "FIN", "fin_unit_param_id1"], self.tests_scenary):
            module_tests_fin.fin_unit_param_id1(self)

    def tests_fin_unit_param_02_id2(self):
        if self.check_scenary(["ALL", "FIN", "fin_unit_param_id2"], self.tests_scenary):
            module_tests_fin.fin_unit_param_id2(self)

    # ===========================================================
    # CTB
    # ===========================================================

    def tests_ctb_centro_05_delete(self):
        if self.check_scenary(["ALL", "CTB", "ctb_centro_delete"], self.tests_scenary):
            module_tests_ctb.ctb_centro_delete(self)

    def tests_ctb_centro_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_centro_get_by_id"], self.tests_scenary
        ):
            module_tests_ctb.ctb_centro_get_by_id(self)

    def tests_ctb_centro_03_get(self):
        if self.check_scenary(["ALL", "CTB", "ctb_centro_get"], self.tests_scenary):
            module_tests_ctb.ctb_centro_get(self)

    def tests_ctb_centro_grupo_05_delete(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_centro_grupo_delete"], self.tests_scenary
        ):
            module_tests_ctb.ctb_centro_grupo_delete(self)

    def tests_ctb_centro_grupo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_centro_grupo_get_by_id"], self.tests_scenary
        ):
            module_tests_ctb.ctb_centro_grupo_get_by_id(self)

    def tests_ctb_centro_grupo_03_get(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_centro_grupo_get"], self.tests_scenary
        ):
            module_tests_ctb.ctb_centro_grupo_get(self)

    def tests_ctb_centro_grupo_01_id1(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_centro_grupo_id1"], self.tests_scenary
        ):
            module_tests_ctb.ctb_centro_grupo_id1(self)

    def tests_ctb_centro_grupo_02_id2(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_centro_grupo_id2"], self.tests_scenary
        ):
            module_tests_ctb.ctb_centro_grupo_id2(self)

    def tests_ctb_centro_01_id1(self):
        if self.check_scenary(["ALL", "CTB", "ctb_centro_id1"], self.tests_scenary):
            module_tests_ctb.ctb_centro_id1(self)

    def tests_ctb_centro_02_id2(self):
        if self.check_scenary(["ALL", "CTB", "ctb_centro_id2"], self.tests_scenary):
            module_tests_ctb.ctb_centro_id2(self)

    def tests_ctb_comp_05_delete(self):
        if self.check_scenary(["ALL", "CTB", "ctb_comp_delete"], self.tests_scenary):
            module_tests_ctb.ctb_comp_delete(self)

    def tests_ctb_comp_04_get_by_id(self):
        if self.check_scenary(["ALL", "CTB", "ctb_comp_get_by_id"], self.tests_scenary):
            module_tests_ctb.ctb_comp_get_by_id(self)

    def tests_ctb_comp_03_get(self):
        if self.check_scenary(["ALL", "CTB", "ctb_comp_get"], self.tests_scenary):
            module_tests_ctb.ctb_comp_get(self)

    def tests_ctb_comp_grupo_05_delete(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_comp_grupo_delete"], self.tests_scenary
        ):
            module_tests_ctb.ctb_comp_grupo_delete(self)

    def tests_ctb_comp_grupo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_comp_grupo_get_by_id"], self.tests_scenary
        ):
            module_tests_ctb.ctb_comp_grupo_get_by_id(self)

    def tests_ctb_comp_grupo_03_get(self):
        if self.check_scenary(["ALL", "CTB", "ctb_comp_grupo_get"], self.tests_scenary):
            module_tests_ctb.ctb_comp_grupo_get(self)

    def tests_ctb_comp_grupo_01_id1(self):
        if self.check_scenary(["ALL", "CTB", "ctb_comp_grupo_id1"], self.tests_scenary):
            module_tests_ctb.ctb_comp_grupo_id1(self)

    def tests_ctb_comp_grupo_02_id2(self):
        if self.check_scenary(["ALL", "CTB", "ctb_comp_grupo_id2"], self.tests_scenary):
            module_tests_ctb.ctb_comp_grupo_id2(self)

    def tests_ctb_comp_01_id1(self):
        if self.check_scenary(["ALL", "CTB", "ctb_comp_id1"], self.tests_scenary):
            module_tests_ctb.ctb_comp_id1(self)

    def tests_ctb_comp_02_id2(self):
        if self.check_scenary(["ALL", "CTB", "ctb_comp_id2"], self.tests_scenary):
            module_tests_ctb.ctb_comp_id2(self)

    def tests_ctb_conta_05_delete(self):
        if self.check_scenary(["ALL", "CTB", "ctb_conta_delete"], self.tests_scenary):
            module_tests_ctb.ctb_conta_delete(self)

    def tests_ctb_conta_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_conta_get_by_id"], self.tests_scenary
        ):
            module_tests_ctb.ctb_conta_get_by_id(self)

    def tests_ctb_conta_03_get(self):
        if self.check_scenary(["ALL", "CTB", "ctb_conta_get"], self.tests_scenary):
            module_tests_ctb.ctb_conta_get(self)

    def tests_ctb_conta_grupo_05_delete(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_conta_grupo_delete"], self.tests_scenary
        ):
            module_tests_ctb.ctb_conta_grupo_delete(self)

    def tests_ctb_conta_grupo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_conta_grupo_get_by_id"], self.tests_scenary
        ):
            module_tests_ctb.ctb_conta_grupo_get_by_id(self)

    def tests_ctb_conta_grupo_03_get(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_conta_grupo_get"], self.tests_scenary
        ):
            module_tests_ctb.ctb_conta_grupo_get(self)

    def tests_ctb_conta_grupo_01_id1(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_conta_grupo_id1"], self.tests_scenary
        ):
            module_tests_ctb.ctb_conta_grupo_id1(self)

    def tests_ctb_conta_grupo_02_id2(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_conta_grupo_id2"], self.tests_scenary
        ):
            module_tests_ctb.ctb_conta_grupo_id2(self)

    def tests_ctb_conta_01_id1(self):
        if self.check_scenary(["ALL", "CTB", "ctb_conta_id1"], self.tests_scenary):
            module_tests_ctb.ctb_conta_id1(self)

    def tests_ctb_conta_02_id2(self):
        if self.check_scenary(["ALL", "CTB", "ctb_conta_id2"], self.tests_scenary):
            module_tests_ctb.ctb_conta_id2(self)

    def tests_ctb_conta_versao_05_delete(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_conta_versao_delete"], self.tests_scenary
        ):
            module_tests_ctb.ctb_conta_versao_delete(self)

    def tests_ctb_conta_versao_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_conta_versao_get_by_id"], self.tests_scenary
        ):
            module_tests_ctb.ctb_conta_versao_get_by_id(self)

    def tests_ctb_conta_versao_03_get(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_conta_versao_get"], self.tests_scenary
        ):
            module_tests_ctb.ctb_conta_versao_get(self)

    def tests_ctb_conta_versao_01_id1(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_conta_versao_id1"], self.tests_scenary
        ):
            module_tests_ctb.ctb_conta_versao_id1(self)

    def tests_ctb_conta_versao_02_id2(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_conta_versao_id2"], self.tests_scenary
        ):
            module_tests_ctb.ctb_conta_versao_id2(self)

    def tests_ctb_historico_05_delete(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_historico_delete"], self.tests_scenary
        ):
            module_tests_ctb.ctb_historico_delete(self)

    def tests_ctb_historico_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_historico_get_by_id"], self.tests_scenary
        ):
            module_tests_ctb.ctb_historico_get_by_id(self)

    def tests_ctb_historico_03_get(self):
        if self.check_scenary(["ALL", "CTB", "ctb_historico_get"], self.tests_scenary):
            module_tests_ctb.ctb_historico_get(self)

    def tests_ctb_historico_01_id1(self):
        if self.check_scenary(["ALL", "CTB", "ctb_historico_id1"], self.tests_scenary):
            module_tests_ctb.ctb_historico_id1(self)

    def tests_ctb_historico_02_id2(self):
        if self.check_scenary(["ALL", "CTB", "ctb_historico_id2"], self.tests_scenary):
            module_tests_ctb.ctb_historico_id2(self)

    def tests_ctb_lanc_05_delete(self):
        if self.check_scenary(["ALL", "CTB", "ctb_lanc_delete"], self.tests_scenary):
            module_tests_ctb.ctb_lanc_delete(self)

    def tests_ctb_lanc_det_05_delete(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_lanc_det_delete"], self.tests_scenary
        ):
            module_tests_ctb.ctb_lanc_det_delete(self)

    def tests_ctb_lanc_det_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_lanc_det_get_by_id"], self.tests_scenary
        ):
            module_tests_ctb.ctb_lanc_det_get_by_id(self)

    def tests_ctb_lanc_det_03_get(self):
        if self.check_scenary(["ALL", "CTB", "ctb_lanc_det_get"], self.tests_scenary):
            module_tests_ctb.ctb_lanc_det_get(self)

    def tests_ctb_lanc_det_01_id1(self):
        if self.check_scenary(["ALL", "CTB", "ctb_lanc_det_id1"], self.tests_scenary):
            module_tests_ctb.ctb_lanc_det_id1(self)

    def tests_ctb_lanc_det_02_id2(self):
        if self.check_scenary(["ALL", "CTB", "ctb_lanc_det_id2"], self.tests_scenary):
            module_tests_ctb.ctb_lanc_det_id2(self)

    def tests_ctb_lanc_04_get_by_id(self):
        if self.check_scenary(["ALL", "CTB", "ctb_lanc_get_by_id"], self.tests_scenary):
            module_tests_ctb.ctb_lanc_get_by_id(self)

    def tests_ctb_lanc_03_get(self):
        if self.check_scenary(["ALL", "CTB", "ctb_lanc_get"], self.tests_scenary):
            module_tests_ctb.ctb_lanc_get(self)

    def tests_ctb_lanc_01_id1(self):
        if self.check_scenary(["ALL", "CTB", "ctb_lanc_id1"], self.tests_scenary):
            module_tests_ctb.ctb_lanc_id1(self)

    def tests_ctb_lanc_02_id2(self):
        if self.check_scenary(["ALL", "CTB", "ctb_lanc_id2"], self.tests_scenary):
            module_tests_ctb.ctb_lanc_id2(self)

    def tests_ctb_lote_05_delete(self):
        if self.check_scenary(["ALL", "CTB", "ctb_lote_delete"], self.tests_scenary):
            module_tests_ctb.ctb_lote_delete(self)

    def tests_ctb_lote_04_get_by_id(self):
        if self.check_scenary(["ALL", "CTB", "ctb_lote_get_by_id"], self.tests_scenary):
            module_tests_ctb.ctb_lote_get_by_id(self)

    def tests_ctb_lote_03_get(self):
        if self.check_scenary(["ALL", "CTB", "ctb_lote_get"], self.tests_scenary):
            module_tests_ctb.ctb_lote_get(self)

    def tests_ctb_lote_01_id1(self):
        if self.check_scenary(["ALL", "CTB", "ctb_lote_id1"], self.tests_scenary):
            module_tests_ctb.ctb_lote_id1(self)

    def tests_ctb_lote_02_id2(self):
        if self.check_scenary(["ALL", "CTB", "ctb_lote_id2"], self.tests_scenary):
            module_tests_ctb.ctb_lote_id2(self)

    def tests_ctb_tipo_saldo_05_delete(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_tipo_saldo_delete"], self.tests_scenary
        ):
            module_tests_ctb.ctb_tipo_saldo_delete(self)

    def tests_ctb_tipo_saldo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_tipo_saldo_get_by_id"], self.tests_scenary
        ):
            module_tests_ctb.ctb_tipo_saldo_get_by_id(self)

    def tests_ctb_tipo_saldo_03_get(self):
        if self.check_scenary(["ALL", "CTB", "ctb_tipo_saldo_get"], self.tests_scenary):
            module_tests_ctb.ctb_tipo_saldo_get(self)

    def tests_ctb_tipo_saldo_01_id1(self):
        if self.check_scenary(["ALL", "CTB", "ctb_tipo_saldo_id1"], self.tests_scenary):
            module_tests_ctb.ctb_tipo_saldo_id1(self)

    def tests_ctb_tipo_saldo_02_id2(self):
        if self.check_scenary(["ALL", "CTB", "ctb_tipo_saldo_id2"], self.tests_scenary):
            module_tests_ctb.ctb_tipo_saldo_id2(self)

    def tests_ctb_unit_param_05_delete(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_unit_param_delete"], self.tests_scenary
        ):
            module_tests_ctb.ctb_unit_param_delete(self)

    def tests_ctb_unit_param_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_unit_param_get_by_id"], self.tests_scenary
        ):
            module_tests_ctb.ctb_unit_param_get_by_id(self)

    def tests_ctb_unit_param_03_get(self):
        if self.check_scenary(["ALL", "CTB", "ctb_unit_param_get"], self.tests_scenary):
            module_tests_ctb.ctb_unit_param_get(self)

    def tests_ctb_unit_param_01_id1(self):
        if self.check_scenary(["ALL", "CTB", "ctb_unit_param_id1"], self.tests_scenary):
            module_tests_ctb.ctb_unit_param_id1(self)

    def tests_ctb_unit_param_02_id2(self):
        if self.check_scenary(["ALL", "CTB", "ctb_unit_param_id2"], self.tests_scenary):
            module_tests_ctb.ctb_unit_param_id2(self)

    def tests_ctb_versao_05_delete(self):
        if self.check_scenary(["ALL", "CTB", "ctb_versao_delete"], self.tests_scenary):
            module_tests_ctb.ctb_versao_delete(self)

    def tests_ctb_versao_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CTB", "ctb_versao_get_by_id"], self.tests_scenary
        ):
            module_tests_ctb.ctb_versao_get_by_id(self)

    def tests_ctb_versao_03_get(self):
        if self.check_scenary(["ALL", "CTB", "ctb_versao_get"], self.tests_scenary):
            module_tests_ctb.ctb_versao_get(self)

    def tests_ctb_versao_01_id1(self):
        if self.check_scenary(["ALL", "CTB", "ctb_versao_id1"], self.tests_scenary):
            module_tests_ctb.ctb_versao_id1(self)

    def tests_ctb_versao_02_id2(self):
        if self.check_scenary(["ALL", "CTB", "ctb_versao_id2"], self.tests_scenary):
            module_tests_ctb.ctb_versao_id2(self)

    # ===========================================================
    # FIS
    # ===========================================================

    def tests_fis_unit_param_02_id2(self):
        if self.check_scenary(
            ["ALL", "FIS", "fis_unit_param_id2", "fis_unit_param_id2"],
            self.tests_scenary,
        ):
            module_tests_fis.fis_unit_param_id2(self)

    def tests_fis_unit_param_01_id1(self):
        if self.check_scenary(["ALL", "FIS", "fis_unit_param_id1"], self.tests_scenary):
            module_tests_fis.fis_unit_param_id1(self)

    def tests_fis_unit_param_03_get(self):
        if self.check_scenary(["ALL", "FIS", "fis_unit_param_get"], self.tests_scenary):
            module_tests_fis.fis_unit_param_get(self)

    def tests_fis_unit_param_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIS", "fis_unit_param_get_by_id"], self.tests_scenary
        ):
            module_tests_fis.fis_unit_param_get_by_id(self)

    def tests_fis_unit_param_05_delete(self):
        if self.check_scenary(
            ["ALL", "FIS", "fis_unit_param_delete"], self.tests_scenary
        ):
            module_tests_fis.fis_unit_param_delete(self)

    def tests_fis_tributo_02_id2(self):
        if self.check_scenary(["ALL", "FIS", "fis_tributo_id2"], self.tests_scenary):
            module_tests_fis.fis_tributo_id2(self)

    def tests_fis_tributo_01_id1(self):
        if self.check_scenary(["ALL", "FIS", "fis_tributo_id1"], self.tests_scenary):
            module_tests_fis.fis_tributo_id1(self)

    def tests_fis_tributo_03_get(self):
        if self.check_scenary(["ALL", "FIS", "fis_tributo_get"], self.tests_scenary):
            module_tests_fis.fis_tributo_get(self)

    def tests_fis_tributo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIS", "fis_tributo_get_by_id"], self.tests_scenary
        ):
            module_tests_fis.fis_tributo_get_by_id(self)

    def tests_fis_tributo_05_delete(self):
        if self.check_scenary(["ALL", "FIS", "fis_tributo_delete"], self.tests_scenary):
            module_tests_fis.fis_tributo_delete(self)

    def tests_fis_obs_02_id2(self):
        if self.check_scenary(["ALL", "FIS", "fis_obs_id2"], self.tests_scenary):
            module_tests_fis.fis_obs_id2(self)

    def tests_fis_obs_01_id1(self):
        if self.check_scenary(["ALL", "FIS", "fis_obs_id1"], self.tests_scenary):
            module_tests_fis.fis_obs_id1(self)

    def tests_fis_obs_03_get(self):
        if self.check_scenary(["ALL", "FIS", "fis_obs_get"], self.tests_scenary):
            module_tests_fis.fis_obs_get(self)

    def tests_fis_obs_04_get_by_id(self):
        if self.check_scenary(["ALL", "FIS", "fis_obs_get_by_id"], self.tests_scenary):
            module_tests_fis.fis_obs_get_by_id(self)

    def tests_fis_obs_05_delete(self):
        if self.check_scenary(["ALL", "FIS", "fis_obs_delete"], self.tests_scenary):
            module_tests_fis.fis_obs_delete(self)

    def tests_fis_ncm_02_id2(self):
        if self.check_scenary(["ALL", "FIS", "fis_ncm_id2"], self.tests_scenary):
            module_tests_fis.fis_ncm_id2(self)

    def tests_fis_ncm_01_id1(self):
        if self.check_scenary(["ALL", "FIS", "fis_ncm_id1"], self.tests_scenary):
            module_tests_fis.fis_ncm_id1(self)

    def tests_fis_ncm_03_get(self):
        if self.check_scenary(["ALL", "FIS", "fis_ncm_get"], self.tests_scenary):
            module_tests_fis.fis_ncm_get(self)

    def tests_fis_ncm_04_get_by_id(self):
        if self.check_scenary(["ALL", "FIS", "fis_ncm_get_by_id"], self.tests_scenary):
            module_tests_fis.fis_ncm_get_by_id(self)

    def tests_fis_ncm_05_delete(self):
        if self.check_scenary(["ALL", "FIS", "fis_ncm_delete"], self.tests_scenary):
            module_tests_fis.fis_ncm_delete(self)

    def tests_fis_nbs_02_id2(self):
        if self.check_scenary(["ALL", "FIS", "fis_nbs_id2"], self.tests_scenary):
            module_tests_fis.fis_nbs_id2(self)

    def tests_fis_nbs_01_id1(self):
        if self.check_scenary(["ALL", "FIS", "fis_nbs_id1"], self.tests_scenary):
            module_tests_fis.fis_nbs_id1(self)

    def tests_fis_nbs_03_get(self):
        if self.check_scenary(["ALL", "FIS", "fis_nbs_get"], self.tests_scenary):
            module_tests_fis.fis_nbs_get(self)

    def tests_fis_nbs_04_get_by_id(self):
        if self.check_scenary(["ALL", "FIS", "fis_nbs_get_by_id"], self.tests_scenary):
            module_tests_fis.fis_nbs_get_by_id(self)

    def tests_fis_nbs_05_delete(self):
        if self.check_scenary(["ALL", "FIS", "fis_nbs_delete"], self.tests_scenary):
            module_tests_fis.fis_nbs_delete(self)

    def tests_fis_ibpt_02_id2(self):
        if self.check_scenary(["ALL", "FIS", "fis_ibpt_id2"], self.tests_scenary):
            module_tests_fis.fis_ibpt_id2(self)

    def tests_fis_ibpt_01_id1(self):
        if self.check_scenary(["ALL", "FIS", "fis_ibpt_id1"], self.tests_scenary):
            module_tests_fis.fis_ibpt_id1(self)

    def tests_fis_ibpt_03_get(self):
        if self.check_scenary(["ALL", "FIS", "fis_ibpt_get"], self.tests_scenary):
            module_tests_fis.fis_ibpt_get(self)

    def tests_fis_ibpt_04_get_by_id(self):
        if self.check_scenary(["ALL", "FIS", "fis_ibpt_get_by_id"], self.tests_scenary):
            module_tests_fis.fis_ibpt_get_by_id(self)

    def tests_fis_ibpt_05_delete(self):
        if self.check_scenary(["ALL", "FIS", "fis_ibpt_delete"], self.tests_scenary):
            module_tests_fis.fis_ibpt_delete(self)

    def tests_fis_doc_tipo_02_id2(self):
        if self.check_scenary(["ALL", "FIS", "fis_doc_tipo_id2"], self.tests_scenary):
            module_tests_fis.fis_doc_tipo_id2(self)

    def tests_fis_doc_tipo_01_id1(self):
        if self.check_scenary(["ALL", "FIS", "fis_doc_tipo_id1"], self.tests_scenary):
            module_tests_fis.fis_doc_tipo_id1(self)

    def tests_fis_doc_tipo_03_get(self):
        if self.check_scenary(["ALL", "FIS", "fis_doc_tipo_get"], self.tests_scenary):
            module_tests_fis.fis_doc_tipo_get(self)

    def tests_fis_doc_tipo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIS", "fis_doc_tipo_get_by_id"], self.tests_scenary
        ):
            module_tests_fis.fis_doc_tipo_get_by_id(self)

    def tests_fis_doc_tipo_05_delete(self):
        if self.check_scenary(
            ["ALL", "FIS", "fis_doc_tipo_delete"], self.tests_scenary
        ):
            module_tests_fis.fis_doc_tipo_delete(self)

    def tests_fis_doc_02_id2(self):
        if self.check_scenary(["ALL", "FIS", "fis_doc_id2"], self.tests_scenary):
            module_tests_fis.fis_doc_id2(self)

    def tests_fis_doc_01_id1(self):
        if self.check_scenary(["ALL", "FIS", "fis_doc_id1"], self.tests_scenary):
            module_tests_fis.fis_doc_id1(self)

    def tests_fis_doc_03_get(self):
        if self.check_scenary(["ALL", "FIS", "fis_doc_get"], self.tests_scenary):
            module_tests_fis.fis_doc_get(self)

    def tests_fis_doc_04_get_by_id(self):
        if self.check_scenary(["ALL", "FIS", "fis_doc_get_by_id"], self.tests_scenary):
            module_tests_fis.fis_doc_get_by_id(self)

    def tests_fis_doc_05_delete(self):
        if self.check_scenary(["ALL", "FIS", "fis_doc_delete"], self.tests_scenary):
            module_tests_fis.fis_doc_delete(self)

    def tests_fis_cfop_02_id2(self):
        if self.check_scenary(["ALL", "FIS", "fis_cfop_id2"], self.tests_scenary):
            module_tests_fis.fis_cfop_id2(self)

    def tests_fis_cfop_01_id1(self):
        if self.check_scenary(["ALL", "FIS", "fis_cfop_id1"], self.tests_scenary):
            module_tests_fis.fis_cfop_id1(self)

    def tests_fis_cfop_03_get(self):
        if self.check_scenary(["ALL", "FIS", "fis_cfop_get"], self.tests_scenary):
            module_tests_fis.fis_cfop_get(self)

    def tests_fis_cfop_04_get_by_id(self):
        if self.check_scenary(["ALL", "FIS", "fis_cfop_get_by_id"], self.tests_scenary):
            module_tests_fis.fis_cfop_get_by_id(self)

    def tests_fis_cfop_05_delete(self):
        if self.check_scenary(["ALL", "FIS", "fis_cfop_delete"], self.tests_scenary):
            module_tests_fis.fis_cfop_delete(self)

    def tests_fis_cest_02_id2(self):
        if self.check_scenary(["ALL", "FIS", "fis_cest_id2"], self.tests_scenary):
            module_tests_fis.fis_cest_id2(self)

    def tests_fis_cest_01_id1(self):
        if self.check_scenary(["ALL", "FIS", "fis_cest_id1"], self.tests_scenary):
            module_tests_fis.fis_cest_id1(self)

    def tests_fis_cest_03_get(self):
        if self.check_scenary(["ALL", "FIS", "fis_cest_get"], self.tests_scenary):
            module_tests_fis.fis_cest_get(self)

    def tests_fis_cest_04_get_by_id(self):
        if self.check_scenary(["ALL", "FIS", "fis_cest_get_by_id"], self.tests_scenary):
            module_tests_fis.fis_cest_get_by_id(self)

    def tests_fis_cest_05_delete(self):
        if self.check_scenary(["ALL", "FIS", "fis_cest_delete"], self.tests_scenary):
            module_tests_fis.fis_cest_delete(self)

    def tests_fis_certificado_02_id2(self):
        if self.check_scenary(
            ["ALL", "FIS", "fis_certificado_id2"], self.tests_scenary
        ):
            module_tests_fis.fis_certificado_id2(self)

    def tests_fis_certificado_01_id1(self):
        if self.check_scenary(
            ["ALL", "FIS", "fis_certificado_id1"], self.tests_scenary
        ):
            module_tests_fis.fis_certificado_id1(self)

    def tests_fis_certificado_03_get(self):
        if self.check_scenary(
            ["ALL", "FIS", "fis_certificado_get"], self.tests_scenary
        ):
            module_tests_fis.fis_certificado_get(self)

    def tests_fis_certificado_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "FIS", "fis_certificado_get_by_id"], self.tests_scenary
        ):
            module_tests_fis.fis_certificado_get_by_id(self)

    def tests_fis_certificado_05_delete(self):
        if self.check_scenary(
            ["ALL", "FIS", "fis_certificado_delete"], self.tests_scenary
        ):
            module_tests_fis.fis_certificado_delete(self)

    # ===========================================================
    # BOR
    # ===========================================================

    def tests_bor_unit_param_02_id2(self):
        if self.check_scenary(["ALL", "BOR", "bor_unit_param_id2"], self.tests_scenary):
            module_tests_bor.bor_unit_param_id2(self)

    def tests_bor_unit_param_01_id1(self):
        if self.check_scenary(["ALL", "BOR", "bor_unit_param_id1"], self.tests_scenary):
            module_tests_bor.bor_unit_param_id1(self)

    def tests_bor_unit_param_03_get(self):
        if self.check_scenary(["ALL", "BOR", "bor_unit_param_get"], self.tests_scenary):
            module_tests_bor.bor_unit_param_get(self)

    def tests_bor_unit_param_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "BOR", "bor_unit_param_get_by_id"], self.tests_scenary
        ):
            module_tests_bor.bor_unit_param_get_by_id(self)

    def tests_bor_unit_param_05_delete(self):
        if self.check_scenary(
            ["ALL", "BOR", "bor_unit_param_delete"], self.tests_scenary
        ):
            module_tests_bor.bor_unit_param_delete(self)

    def tests_bor_dispositivo_02_id2(self):
        if self.check_scenary(
            ["ALL", "BOR", "bor_dispositivo_id2"], self.tests_scenary
        ):
            module_tests_bor.bor_dispositivo_id2(self)

    def tests_bor_dispositivo_01_id1(self):
        if self.check_scenary(
            ["ALL", "BOR", "bor_dispositivo_id1"], self.tests_scenary
        ):
            module_tests_bor.bor_dispositivo_id1(self)

    def tests_bor_dispositivo_03_get(self):
        if self.check_scenary(
            ["ALL", "BOR", "bor_dispositivo_get"], self.tests_scenary
        ):
            module_tests_bor.bor_dispositivo_get(self)

    def tests_bor_dispositivo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "BOR", "bor_dispositivo_get_by_id"], self.tests_scenary
        ):
            module_tests_bor.bor_dispositivo_get_by_id(self)

    def tests_bor_dispositivo_05_delete(self):
        if self.check_scenary(
            ["ALL", "BOR", "bor_dispositivo_delete"], self.tests_scenary
        ):
            module_tests_bor.bor_dispositivo_delete(self)

    # ===========================================================
    # PTO
    # ===========================================================

    def tests_pto_unit_param_02_id2(self):
        if self.check_scenary(["ALL", "PTO", "pto_unit_param_id2"], self.tests_scenary):
            module_tests_pto.pto_unit_param_id2(self)

    def tests_pto_unit_param_01_id1(self):
        if self.check_scenary(["ALL", "PTO", "pto_unit_param_id1"], self.tests_scenary):
            module_tests_pto.pto_unit_param_id1(self)

    def tests_pto_unit_param_03_get(self):
        if self.check_scenary(["ALL", "PTO", "pto_unit_param_get"], self.tests_scenary):
            module_tests_pto.pto_unit_param_get(self)

    def tests_pto_unit_param_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "PTO", "pto_unit_param_get_by_id"], self.tests_scenary
        ):
            module_tests_pto.pto_unit_param_get_by_id(self)

    def tests_pto_unit_param_05_delete(self):
        if self.check_scenary(
            ["ALL", "PTO", "pto_unit_param_delete"], self.tests_scenary
        ):
            module_tests_pto.pto_unit_param_delete(self)

    def tests_pto_medidor_02_id2(self):
        if self.check_scenary(["ALL", "PTO", "pto_medidor_id2"], self.tests_scenary):
            module_tests_pto.pto_medidor_id2(self)

    def tests_pto_medidor_01_id1(self):
        if self.check_scenary(["ALL", "PTO", "pto_medidor_id1"], self.tests_scenary):
            module_tests_pto.pto_medidor_id1(self)

    def tests_pto_medidor_03_get(self):
        if self.check_scenary(["ALL", "PTO", "pto_medidor_get"], self.tests_scenary):
            module_tests_pto.pto_medidor_get(self)

    def tests_pto_medidor_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "PTO", "pto_medidor_get_by_id"], self.tests_scenary
        ):
            module_tests_pto.pto_medidor_get_by_id(self)

    def tests_pto_medidor_05_delete(self):
        if self.check_scenary(["ALL", "PTO", "pto_medidor_delete"], self.tests_scenary):
            module_tests_pto.pto_medidor_delete(self)

    def tests_pto_marcacao_02_id2(self):
        if self.check_scenary(["ALL", "PTO", "pto_marcacao_id2"], self.tests_scenary):
            module_tests_pto.pto_marcacao_id2(self)

    def tests_pto_marcacao_01_id1(self):
        if self.check_scenary(["ALL", "PTO", "pto_marcacao_id1"], self.tests_scenary):
            module_tests_pto.pto_marcacao_id1(self)

    def tests_pto_marcacao_03_get(self):
        if self.check_scenary(["ALL", "PTO", "pto_marcacao_get"], self.tests_scenary):
            module_tests_pto.pto_marcacao_get(self)

    def tests_pto_marcacao_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "PTO", "pto_marcacao_get_by_id"], self.tests_scenary
        ):
            module_tests_pto.pto_marcacao_get_by_id(self)

    def tests_pto_marcacao_05_delete(self):
        if self.check_scenary(
            ["ALL", "PTO", "pto_marcacao_delete"], self.tests_scenary
        ):
            module_tests_pto.pto_marcacao_delete(self)

    # ===========================================================
    # RHM
    # ===========================================================

    def rhm_unit_param_02_id2(self):
        if self.check_scenary(["ALL", "RHM", "it_param_id2"], self.tests_scenary):
            module_tests_rhm.rhm_unit_param_id2(self)

    def rhm_unit_param_01_id1(self):
        if self.check_scenary(["ALL", "RHM", "it_param_id1"], self.tests_scenary):
            module_tests_rhm.rhm_unit_param_id1(self)

    def rhm_unit_param_03_get(self):
        if self.check_scenary(["ALL", "RHM", "it_param_get"], self.tests_scenary):
            module_tests_rhm.rhm_unit_param_get(self)

    def rhm_unit_param_04_get_by_id(self):
        if self.check_scenary(["ALL", "RHM", "it_param_get_by_id"], self.tests_scenary):
            module_tests_rhm.rhm_unit_param_get_by_id(self)

    def rhm_unit_param_05_delete(self):
        if self.check_scenary(["ALL", "RHM", "it_param_delete"], self.tests_scenary):
            module_tests_rhm.rhm_unit_param_delete(self)

    # ===========================================================
    # CRM
    # ===========================================================

    def tests_crm_unit_param_02_id2(self):
        if self.check_scenary(["ALL", "CRM", "crm_unit_param_id2"], self.tests_scenary):
            module_tests_crm.crm_unit_param_id2(self)

    def tests_crm_unit_param_01_id1(self):
        if self.check_scenary(["ALL", "CRM", "crm_unit_param_id1"], self.tests_scenary):
            module_tests_crm.crm_unit_param_id1(self)

    def tests_crm_unit_param_03_get(self):
        if self.check_scenary(["ALL", "CRM", "crm_unit_param_get"], self.tests_scenary):
            module_tests_crm.crm_unit_param_get(self)

    def tests_crm_unit_param_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_unit_param_get_by_id"], self.tests_scenary
        ):
            module_tests_crm.crm_unit_param_get_by_id(self)

    def tests_crm_unit_param_05_delete(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_unit_param_delete"], self.tests_scenary
        ):
            module_tests_crm.crm_unit_param_delete(self)

    def tests_crm_tag_02_id2(self):
        if self.check_scenary(["ALL", "CRM", "crm_tag_id2"], self.tests_scenary):
            module_tests_crm.crm_tag_id2(self)

    def tests_crm_tag_01_id1(self):
        if self.check_scenary(["ALL", "CRM", "crm_tag_id1"], self.tests_scenary):
            module_tests_crm.crm_tag_id1(self)

    def tests_crm_tag_03_get(self):
        if self.check_scenary(["ALL", "CRM", "crm_tag_get"], self.tests_scenary):
            module_tests_crm.crm_tag_get(self)

    def tests_crm_tag_04_get_by_id(self):
        if self.check_scenary(["ALL", "CRM", "crm_tag_get_by_id"], self.tests_scenary):
            module_tests_crm.crm_tag_get_by_id(self)

    def tests_crm_tag_05_delete(self):
        if self.check_scenary(["ALL", "CRM", "crm_tag_delete"], self.tests_scenary):
            module_tests_crm.crm_tag_delete(self)

    def tests_crm_status_02_id2(self):
        if self.check_scenary(["ALL", "CRM", "crm_status_id2"], self.tests_scenary):
            module_tests_crm.crm_status_id2(self)

    def tests_crm_status_01_id1(self):
        if self.check_scenary(["ALL", "CRM", "crm_status_id1"], self.tests_scenary):
            module_tests_crm.crm_status_id1(self)

    def tests_crm_status_03_get(self):
        if self.check_scenary(["ALL", "CRM", "crm_status_get"], self.tests_scenary):
            module_tests_crm.crm_status_get(self)

    def tests_crm_status_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_status_get_by_id"], self.tests_scenary
        ):
            module_tests_crm.crm_status_get_by_id(self)

    def tests_crm_status_05_delete(self):
        if self.check_scenary(["ALL", "CRM", "crm_status_delete"], self.tests_scenary):
            module_tests_crm.crm_status_delete(self)

    def tests_crm_resposta_02_id2(self):
        if self.check_scenary(["ALL", "CRM", "crm_resposta_id2"], self.tests_scenary):
            module_tests_crm.crm_resposta_id2(self)

    def tests_crm_resposta_01_id1(self):
        if self.check_scenary(["ALL", "CRM", "crm_resposta_id1"], self.tests_scenary):
            module_tests_crm.crm_resposta_id1(self)

    def tests_crm_resposta_03_get(self):
        if self.check_scenary(["ALL", "CRM", "crm_resposta_get"], self.tests_scenary):
            module_tests_crm.crm_resposta_get(self)

    def tests_crm_resposta_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_resposta_get_by_id"], self.tests_scenary
        ):
            module_tests_crm.crm_resposta_get_by_id(self)

    def tests_crm_resposta_05_delete(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_resposta_delete"], self.tests_scenary
        ):
            module_tests_crm.crm_resposta_delete(self)

    def tests_crm_prioridade_02_id2(self):
        if self.check_scenary(["ALL", "CRM", "crm_prioridade_id2"], self.tests_scenary):
            module_tests_crm.crm_prioridade_id2(self)

    def tests_crm_prioridade_01_id1(self):
        if self.check_scenary(["ALL", "CRM", "crm_prioridade_id1"], self.tests_scenary):
            module_tests_crm.crm_prioridade_id1(self)

    def tests_crm_prioridade_03_get(self):
        if self.check_scenary(["ALL", "CRM", "crm_prioridade_get"], self.tests_scenary):
            module_tests_crm.crm_prioridade_get(self)

    def tests_crm_prioridade_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_prioridade_get_by_id"], self.tests_scenary
        ):
            module_tests_crm.crm_prioridade_get_by_id(self)

    def tests_crm_prioridade_05_delete(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_prioridade_delete"], self.tests_scenary
        ):
            module_tests_crm.crm_prioridade_delete(self)

    def tests_crm_org_02_id2(self):
        if self.check_scenary(["ALL", "CRM", "crm_org_id2"], self.tests_scenary):
            module_tests_crm.crm_org_id2(self)

    def tests_crm_org_01_id1(self):
        if self.check_scenary(["ALL", "CRM", "crm_org_id1"], self.tests_scenary):
            module_tests_crm.crm_org_id1(self)

    def tests_crm_org_03_get(self):
        if self.check_scenary(["ALL", "CRM", "crm_org_get"], self.tests_scenary):
            module_tests_crm.crm_org_get(self)

    def tests_crm_org_04_get_by_id(self):
        if self.check_scenary(["ALL", "CRM", "crm_org_get_by_id"], self.tests_scenary):
            module_tests_crm.crm_org_get_by_id(self)

    def tests_crm_org_05_delete(self):
        if self.check_scenary(["ALL", "CRM", "crm_org_delete"], self.tests_scenary):
            module_tests_crm.crm_org_delete(self)

    def tests_crm_mov_tag_02_id2(self):
        if self.check_scenary(["ALL", "CRM", "crm_mov_tag_id2"], self.tests_scenary):
            module_tests_crm.crm_mov_tag_id2(self)

    def tests_crm_mov_tag_01_id1(self):
        if self.check_scenary(["ALL", "CRM", "crm_mov_tag_id1"], self.tests_scenary):
            module_tests_crm.crm_mov_tag_id1(self)

    def tests_crm_mov_tag_03_get(self):
        if self.check_scenary(["ALL", "CRM", "crm_mov_tag_get"], self.tests_scenary):
            module_tests_crm.crm_mov_tag_get(self)

    def tests_crm_mov_tag_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_mov_tag_get_by_id"], self.tests_scenary
        ):
            module_tests_crm.crm_mov_tag_get_by_id(self)

    def tests_crm_mov_tag_05_delete(self):
        if self.check_scenary(["ALL", "CRM", "crm_mov_tag_delete"], self.tests_scenary):
            module_tests_crm.crm_mov_tag_delete(self)

    def tests_crm_mov_02_id2(self):
        if self.check_scenary(["ALL", "CRM", "crm_mov_id2"], self.tests_scenary):
            module_tests_crm.crm_mov_id2(self)

    def tests_crm_mov_01_id1(self):
        if self.check_scenary(["ALL", "CRM", "crm_mov_id1"], self.tests_scenary):
            module_tests_crm.crm_mov_id1(self)

    def tests_crm_mov_hist_02_id2(self):
        if self.check_scenary(["ALL", "CRM", "crm_mov_hist_id2"], self.tests_scenary):
            module_tests_crm.crm_mov_hist_id2(self)

    def tests_crm_mov_hist_01_id1(self):
        if self.check_scenary(["ALL", "CRM", "crm_mov_hist_id1"], self.tests_scenary):
            module_tests_crm.crm_mov_hist_id1(self)

    def tests_crm_mov_hist_03_get(self):
        if self.check_scenary(["ALL", "CRM", "crm_mov_hist_get"], self.tests_scenary):
            module_tests_crm.crm_mov_hist_get(self)

    def tests_crm_mov_hist_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_mov_hist_get_by_id"], self.tests_scenary
        ):
            module_tests_crm.crm_mov_hist_get_by_id(self)

    def tests_crm_mov_hist_05_delete(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_mov_hist_delete"], self.tests_scenary
        ):
            module_tests_crm.crm_mov_hist_delete(self)

    def tests_crm_mov_03_get(self):
        if self.check_scenary(["ALL", "CRM", "crm_mov_get"], self.tests_scenary):
            module_tests_crm.crm_mov_get(self)

    def tests_crm_mov_04_get_by_id(self):
        if self.check_scenary(["ALL", "CRM", "crm_mov_get_by_id"], self.tests_scenary):
            module_tests_crm.crm_mov_get_by_id(self)

    def tests_crm_mov_05_delete(self):
        if self.check_scenary(["ALL", "CRM", "crm_mov_delete"], self.tests_scenary):
            module_tests_crm.crm_mov_delete(self)

    def tests_crm_etapa_prox_02_id2(self):
        if self.check_scenary(["ALL", "CRM", "crm_etapa_prox_id2"], self.tests_scenary):
            module_tests_crm.crm_etapa_prox_id2(self)

    def tests_crm_etapa_prox_01_id1(self):
        if self.check_scenary(["ALL", "CRM", "crm_etapa_prox_id1"], self.tests_scenary):
            module_tests_crm.crm_etapa_prox_id1(self)

    def tests_crm_etapa_prox_03_get(self):
        if self.check_scenary(["ALL", "CRM", "crm_etapa_prox_get"], self.tests_scenary):
            module_tests_crm.crm_etapa_prox_get(self)

    def tests_crm_etapa_prox_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_etapa_prox_get_by_id"], self.tests_scenary
        ):
            module_tests_crm.crm_etapa_prox_get_by_id(self)

    def tests_crm_etapa_prox_05_delete(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_etapa_prox_delete"], self.tests_scenary
        ):
            module_tests_crm.crm_etapa_prox_delete(self)

    def tests_crm_etapa_02_id2(self):
        if self.check_scenary(["ALL", "CRM", "crm_etapa_id2"], self.tests_scenary):
            module_tests_crm.crm_etapa_id2(self)

    def tests_crm_etapa_01_id1(self):
        if self.check_scenary(["ALL", "CRM", "crm_etapa_id1"], self.tests_scenary):
            module_tests_crm.crm_etapa_id1(self)

    def tests_crm_etapa_03_get(self):
        if self.check_scenary(["ALL", "CRM", "crm_etapa_get"], self.tests_scenary):
            module_tests_crm.crm_etapa_get(self)

    def tests_crm_etapa_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_etapa_get_by_id"], self.tests_scenary
        ):
            module_tests_crm.crm_etapa_get_by_id(self)

    def tests_crm_etapa_05_delete(self):
        if self.check_scenary(["ALL", "CRM", "crm_etapa_delete"], self.tests_scenary):
            module_tests_crm.crm_etapa_delete(self)

    def tests_crm_class_02_id2(self):
        if self.check_scenary(["ALL", "CRM", "crm_class_id2"], self.tests_scenary):
            module_tests_crm.crm_class_id2(self)

    def tests_crm_class_01_id1(self):
        if self.check_scenary(["ALL", "CRM", "crm_class_id1"], self.tests_scenary):
            module_tests_crm.crm_class_id1(self)

    def tests_crm_class_grupo_02_id2(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_class_grupo_id2"], self.tests_scenary
        ):
            module_tests_crm.crm_class_grupo_id2(self)

    def tests_crm_class_grupo_01_id1(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_class_grupo_id1"], self.tests_scenary
        ):
            module_tests_crm.crm_class_grupo_id1(self)

    def tests_crm_class_grupo_03_get(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_class_grupo_get"], self.tests_scenary
        ):
            module_tests_crm.crm_class_grupo_get(self)

    def tests_crm_class_grupo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_class_grupo_get_by_id"], self.tests_scenary
        ):
            module_tests_crm.crm_class_grupo_get_by_id(self)

    def tests_crm_class_grupo_05_delete(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_class_grupo_delete"], self.tests_scenary
        ):
            module_tests_crm.crm_class_grupo_delete(self)

    def tests_crm_class_03_get(self):
        if self.check_scenary(["ALL", "CRM", "crm_class_get"], self.tests_scenary):
            module_tests_crm.crm_class_get(self)

    def tests_crm_class_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_class_get_by_id"], self.tests_scenary
        ):
            module_tests_crm.crm_class_get_by_id(self)

    def tests_crm_class_05_delete(self):
        if self.check_scenary(["ALL", "CRM", "crm_class_delete"], self.tests_scenary):
            module_tests_crm.crm_class_delete(self)

    def tests_crm_chat_msg_02_id2(self):
        if self.check_scenary(["ALL", "CRM", "crm_chat_msg_id2"], self.tests_scenary):
            module_tests_crm.crm_chat_msg_id2(self)

    def tests_crm_chat_msg_01_id1(self):
        if self.check_scenary(["ALL", "CRM", "crm_chat_msg_id1"], self.tests_scenary):
            module_tests_crm.crm_chat_msg_id1(self)

    def tests_crm_chat_msg_03_get(self):
        if self.check_scenary(["ALL", "CRM", "crm_chat_msg_get"], self.tests_scenary):
            module_tests_crm.crm_chat_msg_get(self)

    def tests_crm_chat_msg_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_chat_msg_get_by_id"], self.tests_scenary
        ):
            module_tests_crm.crm_chat_msg_get_by_id(self)

    def tests_crm_chat_msg_05_delete(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_chat_msg_delete"], self.tests_scenary
        ):
            module_tests_crm.crm_chat_msg_delete(self)

    def tests_crm_chat_grupo_02_id2(self):
        if self.check_scenary(["ALL", "CRM", "crm_chat_grupo_id2"], self.tests_scenary):
            module_tests_crm.crm_chat_grupo_id2(self)

    def tests_crm_chat_grupo_01_id1(self):
        if self.check_scenary(["ALL", "CRM", "crm_chat_grupo_id1"], self.tests_scenary):
            module_tests_crm.crm_chat_grupo_id1(self)

    def tests_crm_chat_grupo_03_get(self):
        if self.check_scenary(["ALL", "CRM", "crm_chat_grupo_get"], self.tests_scenary):
            module_tests_crm.crm_chat_grupo_get(self)

    def tests_crm_chat_grupo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_chat_grupo_get_by_id"], self.tests_scenary
        ):
            module_tests_crm.crm_chat_grupo_get_by_id(self)

    def tests_crm_chat_grupo_05_delete(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_chat_grupo_delete"], self.tests_scenary
        ):
            module_tests_crm.crm_chat_grupo_delete(self)

    def tests_crm_aviso_org_02_id2(self):
        if self.check_scenary(["ALL", "CRM", "crm_aviso_org_id2"], self.tests_scenary):
            module_tests_crm.crm_aviso_org_id2(self)

    def tests_crm_aviso_org_01_id1(self):
        if self.check_scenary(["ALL", "CRM", "crm_aviso_org_id1"], self.tests_scenary):
            module_tests_crm.crm_aviso_org_id1(self)

    def tests_crm_aviso_org_03_get(self):
        if self.check_scenary(["ALL", "CRM", "crm_aviso_org_get"], self.tests_scenary):
            module_tests_crm.crm_aviso_org_get(self)

    def tests_crm_aviso_org_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_aviso_org_get_by_id"], self.tests_scenary
        ):
            module_tests_crm.crm_aviso_org_get_by_id(self)

    def tests_crm_aviso_org_05_delete(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_aviso_org_delete"], self.tests_scenary
        ):
            module_tests_crm.crm_aviso_org_delete(self)

    def tests_crm_aviso_02_id2(self):
        if self.check_scenary(["ALL", "CRM", "crm_aviso_id2"], self.tests_scenary):
            module_tests_crm.crm_aviso_id2(self)

    def tests_crm_aviso_01_id1(self):
        if self.check_scenary(["ALL", "CRM", "crm_aviso_id1"], self.tests_scenary):
            module_tests_crm.crm_aviso_id1(self)

    def tests_crm_aviso_03_get(self):
        if self.check_scenary(["ALL", "CRM", "crm_aviso_get"], self.tests_scenary):
            module_tests_crm.crm_aviso_get(self)

    def tests_crm_aviso_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CRM", "crm_aviso_get_by_id"], self.tests_scenary
        ):
            module_tests_crm.crm_aviso_get_by_id(self)

    def tests_crm_aviso_05_delete(self):
        if self.check_scenary(["ALL", "CRM", "crm_aviso_delete"], self.tests_scenary):
            module_tests_crm.crm_aviso_delete(self)

    # ===========================================================
    # OPE
    # ===========================================================

    def tests_ope_unit_param_02_id2(self):
        if self.check_scenary(["ALL", "OPE", "ope_unit_param_id2"], self.tests_scenary):
            module_tests_ope.ope_unit_param_id2(self)

    def tests_ope_unit_param_01_id1(self):
        if self.check_scenary(["ALL", "OPE", "ope_unit_param_id1"], self.tests_scenary):
            module_tests_ope.ope_unit_param_id1(self)

    def tests_ope_unit_param_03_get(self):
        if self.check_scenary(["ALL", "OPE", "ope_unit_param_get"], self.tests_scenary):
            module_tests_ope.ope_unit_param_get(self)

    def tests_ope_unit_param_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_unit_param_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_unit_param_get_by_id(self)

    def tests_ope_unit_param_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_unit_param_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_unit_param_delete(self)

    def tests_ope_tipo_solo_02_id2(self):
        if self.check_scenary(["ALL", "OPE", "ope_tipo_solo_id2"], self.tests_scenary):
            module_tests_ope.ope_tipo_solo_id2(self)

    def tests_ope_tipo_solo_01_id1(self):
        if self.check_scenary(["ALL", "OPE", "ope_tipo_solo_id1"], self.tests_scenary):
            module_tests_ope.ope_tipo_solo_id1(self)

    def tests_ope_tipo_solo_03_get(self):
        if self.check_scenary(["ALL", "OPE", "ope_tipo_solo_get"], self.tests_scenary):
            module_tests_ope.ope_tipo_solo_get(self)

    def tests_ope_tipo_solo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_tipo_solo_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_tipo_solo_get_by_id(self)

    def tests_ope_tipo_solo_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_tipo_solo_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_tipo_solo_delete(self)

    def tests_ope_regiao_02_id2(self):
        if self.check_scenary(["ALL", "OPE", "ope_regiao_id2"], self.tests_scenary):
            module_tests_ope.ope_regiao_id2(self)

    def tests_ope_regiao_01_id1(self):
        if self.check_scenary(["ALL", "OPE", "ope_regiao_id1"], self.tests_scenary):
            module_tests_ope.ope_regiao_id1(self)

    def tests_ope_regiao_03_get(self):
        if self.check_scenary(["ALL", "OPE", "ope_regiao_get"], self.tests_scenary):
            module_tests_ope.ope_regiao_get(self)

    def tests_ope_regiao_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_regiao_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_regiao_get_by_id(self)

    def tests_ope_regiao_05_delete(self):
        if self.check_scenary(["ALL", "OPE", "ope_regiao_delete"], self.tests_scenary):
            module_tests_ope.ope_regiao_delete(self)

    def tests_ope_periodo_02_id2(self):
        if self.check_scenary(["ALL", "OPE", "ope_periodo_id2"], self.tests_scenary):
            module_tests_ope.ope_periodo_id2(self)

    def tests_ope_periodo_01_id1(self):
        if self.check_scenary(["ALL", "OPE", "ope_periodo_id1"], self.tests_scenary):
            module_tests_ope.ope_periodo_id1(self)

    def tests_ope_periodo_03_get(self):
        if self.check_scenary(["ALL", "OPE", "ope_periodo_get"], self.tests_scenary):
            module_tests_ope.ope_periodo_get(self)

    def tests_ope_periodo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_periodo_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_periodo_get_by_id(self)

    def tests_ope_periodo_05_delete(self):
        if self.check_scenary(["ALL", "OPE", "ope_periodo_delete"], self.tests_scenary):
            module_tests_ope.ope_periodo_delete(self)

    def tests_ope_ocor_tipo_02_id2(self):
        if self.check_scenary(["ALL", "OPE", "ope_ocor_tipo_id2"], self.tests_scenary):
            module_tests_ope.ope_ocor_tipo_id2(self)

    def tests_ope_ocor_tipo_01_id1(self):
        if self.check_scenary(["ALL", "OPE", "ope_ocor_tipo_id1"], self.tests_scenary):
            module_tests_ope.ope_ocor_tipo_id1(self)

    def tests_ope_ocor_tipo_03_get(self):
        if self.check_scenary(["ALL", "OPE", "ope_ocor_tipo_get"], self.tests_scenary):
            module_tests_ope.ope_ocor_tipo_get(self)

    def tests_ope_ocor_tipo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_ocor_tipo_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_ocor_tipo_get_by_id(self)

    def tests_ope_ocor_tipo_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_ocor_tipo_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_ocor_tipo_delete(self)

    def tests_ope_ocor_status_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_ocor_status_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_ocor_status_id2(self)

    def tests_ope_ocor_status_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_ocor_status_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_ocor_status_id1(self)

    def tests_ope_ocor_status_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_ocor_status_get"], self.tests_scenary
        ):
            module_tests_ope.ope_ocor_status_get(self)

    def tests_ope_ocor_status_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_ocor_status_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_ocor_status_get_by_id(self)

    def tests_ope_ocor_status_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_ocor_status_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_ocor_status_delete(self)

    def tests_ope_ocor_prev_02_id2(self):
        if self.check_scenary(["ALL", "OPE", "ope_ocor_prev_id2"], self.tests_scenary):
            module_tests_ope.ope_ocor_prev_id2(self)

    def tests_ope_ocor_prev_01_id1(self):
        if self.check_scenary(["ALL", "OPE", "ope_ocor_prev_id1"], self.tests_scenary):
            module_tests_ope.ope_ocor_prev_id1(self)

    def tests_ope_ocor_prev_03_get(self):
        if self.check_scenary(["ALL", "OPE", "ope_ocor_prev_get"], self.tests_scenary):
            module_tests_ope.ope_ocor_prev_get(self)

    def tests_ope_ocor_prev_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_ocor_prev_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_ocor_prev_get_by_id(self)

    def tests_ope_ocor_prev_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_ocor_prev_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_ocor_prev_delete(self)

    def tests_ope_ocor_mov_02_id2(self):
        if self.check_scenary(["ALL", "OPE", "ope_ocor_mov_id2"], self.tests_scenary):
            module_tests_ope.ope_ocor_mov_id2(self)

    def tests_ope_ocor_mov_01_id1(self):
        if self.check_scenary(["ALL", "OPE", "ope_ocor_mov_id1"], self.tests_scenary):
            module_tests_ope.ope_ocor_mov_id1(self)

    def tests_ope_ocor_mov_03_get(self):
        if self.check_scenary(["ALL", "OPE", "ope_ocor_mov_get"], self.tests_scenary):
            module_tests_ope.ope_ocor_mov_get(self)

    def tests_ope_ocor_mov_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_ocor_mov_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_ocor_mov_get_by_id(self)

    def tests_ope_ocor_mov_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_ocor_mov_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_ocor_mov_delete(self)

    def tests_ope_ocor_02_id2(self):
        if self.check_scenary(["ALL", "OPE", "ope_ocor_id2"], self.tests_scenary):
            module_tests_ope.ope_ocor_id2(self)

    def tests_ope_ocor_01_id1(self):
        if self.check_scenary(["ALL", "OPE", "ope_ocor_id1"], self.tests_scenary):
            module_tests_ope.ope_ocor_id1(self)

    def tests_ope_ocor_grupo_02_id2(self):
        if self.check_scenary(["ALL", "OPE", "ope_ocor_grupo_id2"], self.tests_scenary):
            module_tests_ope.ope_ocor_grupo_id2(self)

    def tests_ope_ocor_grupo_01_id1(self):
        if self.check_scenary(["ALL", "OPE", "ope_ocor_grupo_id1"], self.tests_scenary):
            module_tests_ope.ope_ocor_grupo_id1(self)

    def tests_ope_ocor_grupo_03_get(self):
        if self.check_scenary(["ALL", "OPE", "ope_ocor_grupo_get"], self.tests_scenary):
            module_tests_ope.ope_ocor_grupo_get(self)

    def tests_ope_ocor_grupo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_ocor_grupo_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_ocor_grupo_get_by_id(self)

    def tests_ope_ocor_grupo_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_ocor_grupo_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_ocor_grupo_delete(self)

    def tests_ope_ocor_03_get(self):
        if self.check_scenary(["ALL", "OPE", "ope_ocor_get"], self.tests_scenary):
            module_tests_ope.ope_ocor_get(self)

    def tests_ope_ocor_04_get_by_id(self):
        if self.check_scenary(["ALL", "OPE", "ope_ocor_get_by_id"], self.tests_scenary):
            module_tests_ope.ope_ocor_get_by_id(self)

    def tests_ope_ocor_05_delete(self):
        if self.check_scenary(["ALL", "OPE", "ope_ocor_delete"], self.tests_scenary):
            module_tests_ope.ope_ocor_delete(self)

    def tests_ope_ocor_compart_mov_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_ocor_compart_mov_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_ocor_compart_mov_id2(self)

    def tests_ope_ocor_compart_mov_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_ocor_compart_mov_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_ocor_compart_mov_id1(self)

    def tests_ope_ocor_compart_mov_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_ocor_compart_mov_get"], self.tests_scenary
        ):
            module_tests_ope.ope_ocor_compart_mov_get(self)

    def tests_ope_ocor_compart_mov_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_ocor_compart_mov_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_ocor_compart_mov_get_by_id(self)

    def tests_ope_ocor_compart_mov_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_ocor_compart_mov_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_ocor_compart_mov_delete(self)

    def tests_ope_frente_trabalho_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_frente_trabalho_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_frente_trabalho_id2(self)

    def tests_ope_frente_trabalho_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_frente_trabalho_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_frente_trabalho_id1(self)

    def tests_ope_frente_trabalho_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_frente_trabalho_get"], self.tests_scenary
        ):
            module_tests_ope.ope_frente_trabalho_get(self)

    def tests_ope_frente_trabalho_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_frente_trabalho_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_frente_trabalho_get_by_id(self)

    def tests_ope_frente_trabalho_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_frente_trabalho_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_frente_trabalho_delete(self)

    def tests_ope_estagio_02_id2(self):
        if self.check_scenary(["ALL", "OPE", "ope_estagio_id2"], self.tests_scenary):
            module_tests_ope.ope_estagio_id2(self)

    def tests_ope_estagio_01_id1(self):
        if self.check_scenary(["ALL", "OPE", "ope_estagio_id1"], self.tests_scenary):
            module_tests_ope.ope_estagio_id1(self)

    def tests_ope_estagio_03_get(self):
        if self.check_scenary(["ALL", "OPE", "ope_estagio_get"], self.tests_scenary):
            module_tests_ope.ope_estagio_get(self)

    def tests_ope_estagio_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_estagio_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_estagio_get_by_id(self)

    def tests_ope_estagio_05_delete(self):
        if self.check_scenary(["ALL", "OPE", "ope_estagio_delete"], self.tests_scenary):
            module_tests_ope.ope_estagio_delete(self)

    def tests_ope_espac_02_id2(self):
        if self.check_scenary(["ALL", "OPE", "ope_espac_id2"], self.tests_scenary):
            module_tests_ope.ope_espac_id2(self)

    def tests_ope_espac_01_id1(self):
        if self.check_scenary(["ALL", "OPE", "ope_espac_id1"], self.tests_scenary):
            module_tests_ope.ope_espac_id1(self)

    def tests_ope_espac_03_get(self):
        if self.check_scenary(["ALL", "OPE", "ope_espac_get"], self.tests_scenary):
            module_tests_ope.ope_espac_get(self)

    def tests_ope_espac_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_espac_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_espac_get_by_id(self)

    def tests_ope_espac_05_delete(self):
        if self.check_scenary(["ALL", "OPE", "ope_espac_delete"], self.tests_scenary):
            module_tests_ope.ope_espac_delete(self)

    def tests_ope_compart_tipo_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_tipo_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_tipo_id2(self)

    def tests_ope_compart_tipo_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_tipo_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_tipo_id1(self)

    def tests_ope_compart_tipo_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_tipo_get"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_tipo_get(self)

    def tests_ope_compart_tipo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_tipo_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_tipo_get_by_id(self)

    def tests_ope_compart_tipo_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_tipo_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_tipo_delete(self)

    def tests_ope_compart_subgrupo_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_subgrupo_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_subgrupo_id2(self)

    def tests_ope_compart_subgrupo_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_subgrupo_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_subgrupo_id1(self)

    def tests_ope_compart_subgrupo_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_subgrupo_get"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_subgrupo_get(self)

    def tests_ope_compart_subgrupo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_subgrupo_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_subgrupo_get_by_id(self)

    def tests_ope_compart_subgrupo_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_subgrupo_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_subgrupo_delete(self)

    def tests_ope_compart_status_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_status_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_status_id2(self)

    def tests_ope_compart_status_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_status_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_status_id1(self)

    def tests_ope_compart_status_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_status_get"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_status_get(self)

    def tests_ope_compart_status_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_status_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_status_get_by_id(self)

    def tests_ope_compart_status_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_status_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_status_delete(self)

    def tests_ope_compart_posicao_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_posicao_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_posicao_id2(self)

    def tests_ope_compart_posicao_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_posicao_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_posicao_id1(self)

    def tests_ope_compart_posicao_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_posicao_get"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_posicao_get(self)

    def tests_ope_compart_posicao_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_posicao_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_posicao_get_by_id(self)

    def tests_ope_compart_posicao_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_posicao_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_posicao_delete(self)

    def tests_ope_compart_ocor_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_ocor_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_ocor_id2(self)

    def tests_ope_compart_ocor_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_ocor_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_ocor_id1(self)

    def tests_ope_compart_ocor_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_ocor_get"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_ocor_get(self)

    def tests_ope_compart_ocor_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_ocor_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_ocor_get_by_id(self)

    def tests_ope_compart_ocor_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_ocor_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_ocor_delete(self)

    def tests_ope_compart_medida_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_medida_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_medida_id2(self)

    def tests_ope_compart_medida_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_medida_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_medida_id1(self)

    def tests_ope_compart_medida_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_medida_get"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_medida_get(self)

    def tests_ope_compart_medida_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_medida_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_medida_get_by_id(self)

    def tests_ope_compart_medida_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_medida_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_medida_delete(self)

    def tests_ope_compart_itemserv_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_itemserv_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_itemserv_id2(self)

    def tests_ope_compart_itemserv_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_itemserv_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_itemserv_id1(self)

    def tests_ope_compart_itemserv_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_itemserv_get"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_itemserv_get(self)

    def tests_ope_compart_itemserv_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_itemserv_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_itemserv_get_by_id(self)

    def tests_ope_compart_itemserv_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_itemserv_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_itemserv_delete(self)

    def tests_ope_compart_02_id2(self):
        if self.check_scenary(["ALL", "OPE", "ope_compart_id2"], self.tests_scenary):
            module_tests_ope.ope_compart_id2(self)

    def tests_ope_compart_01_id1(self):
        if self.check_scenary(["ALL", "OPE", "ope_compart_id1"], self.tests_scenary):
            module_tests_ope.ope_compart_id1(self)

    def tests_ope_compart_grupo_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_grupo_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_grupo_id2(self)

    def tests_ope_compart_grupo_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_grupo_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_grupo_id1(self)

    def tests_ope_compart_grupo_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_grupo_get"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_grupo_get(self)

    def tests_ope_compart_grupo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_grupo_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_grupo_get_by_id(self)

    def tests_ope_compart_grupo_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_grupo_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_grupo_delete(self)

    def tests_ope_compart_03_get(self):
        if self.check_scenary(["ALL", "OPE", "ope_compart_get"], self.tests_scenary):
            module_tests_ope.ope_compart_get(self)

    def tests_ope_compart_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_compart_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_compart_get_by_id(self)

    def tests_ope_compart_05_delete(self):
        if self.check_scenary(["ALL", "OPE", "ope_compart_delete"], self.tests_scenary):
            module_tests_ope.ope_compart_delete(self)

    def tests_ope_ciclo_var_02_id2(self):
        if self.check_scenary(["ALL", "OPE", "ope_ciclo_var_id2"], self.tests_scenary):
            module_tests_ope.ope_ciclo_var_id2(self)

    def tests_ope_ciclo_var_01_id1(self):
        if self.check_scenary(["ALL", "OPE", "ope_ciclo_var_id1"], self.tests_scenary):
            module_tests_ope.ope_ciclo_var_id1(self)

    def tests_ope_ciclo_var_03_get(self):
        if self.check_scenary(["ALL", "OPE", "ope_ciclo_var_get"], self.tests_scenary):
            module_tests_ope.ope_ciclo_var_get(self)

    def tests_ope_ciclo_var_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_ciclo_var_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_ciclo_var_get_by_id(self)

    def tests_ope_ciclo_var_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_ciclo_var_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_ciclo_var_delete(self)

    def tests_ope_centro2_pessoa_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_pessoa_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_pessoa_id2(self)

    def tests_ope_centro2_pessoa_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_pessoa_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_pessoa_id1(self)

    def tests_ope_centro2_pessoa_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_pessoa_get"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_pessoa_get(self)

    def tests_ope_centro2_pessoa_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_pessoa_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_pessoa_get_by_id(self)

    def tests_ope_centro2_pessoa_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_pessoa_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_pessoa_delete(self)

    def tests_ope_centro2_param_per_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_param_per_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_param_per_id2(self)

    def tests_ope_centro2_param_per_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_param_per_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_param_per_id1(self)

    def tests_ope_centro2_param_per_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_param_per_get"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_param_per_get(self)

    def tests_ope_centro2_param_per_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_param_per_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_param_per_get_by_id(self)

    def tests_ope_centro2_param_per_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_param_per_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_param_per_delete(self)

    def tests_ope_centro2_ord_tipo_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_tipo_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_tipo_id2(self)

    def tests_ope_centro2_ord_tipo_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_tipo_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_tipo_id1(self)

    def tests_ope_centro2_ord_tipo_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_tipo_get"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_tipo_get(self)

    def tests_ope_centro2_ord_tipo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_tipo_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_tipo_get_by_id(self)

    def tests_ope_centro2_ord_tipo_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_tipo_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_tipo_delete(self)

    def tests_ope_centro2_ord_status_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_status_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_status_id2(self)

    def tests_ope_centro2_ord_status_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_status_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_status_id1(self)

    def tests_ope_centro2_ord_status_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_status_get"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_status_get(self)

    def tests_ope_centro2_ord_status_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_status_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_status_get_by_id(self)

    def tests_ope_centro2_ord_status_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_status_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_status_delete(self)

    def tests_ope_centro2_ord_rec_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_rec_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_rec_id2(self)

    def tests_ope_centro2_ord_rec_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_rec_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_rec_id1(self)

    def tests_ope_centro2_ord_rec_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_rec_get"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_rec_get(self)

    def tests_ope_centro2_ord_rec_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_rec_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_rec_get_by_id(self)

    def tests_ope_centro2_ord_rec_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_rec_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_rec_delete(self)

    def tests_ope_centro2_ord_itemserv_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_itemserv_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_itemserv_id2(self)

    def tests_ope_centro2_ord_itemserv_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_itemserv_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_itemserv_id1(self)

    def tests_ope_centro2_ord_itemserv_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_itemserv_get"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_itemserv_get(self)

    def tests_ope_centro2_ord_itemserv_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_itemserv_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_itemserv_get_by_id(self)

    def tests_ope_centro2_ord_itemserv_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_itemserv_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_itemserv_delete(self)

    def tests_ope_centro2_ord_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_id2(self)

    def tests_ope_centro2_ord_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_id1(self)

    def tests_ope_centro2_ord_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_get"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_get(self)

    def tests_ope_centro2_ord_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_get_by_id(self)

    def tests_ope_centro2_ord_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_ord_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_ord_delete(self)

    def tests_ope_centro2_mov_media_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_mov_media_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_mov_media_id2(self)

    def tests_ope_centro2_mov_media_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_mov_media_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_mov_media_id1(self)

    def tests_ope_centro2_mov_media_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_mov_media_get"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_mov_media_get(self)

    def tests_ope_centro2_mov_media_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_mov_media_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_mov_media_get_by_id(self)

    def tests_ope_centro2_mov_media_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_mov_media_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_mov_media_delete(self)

    def tests_ope_centro2_02_id2(self):
        if self.check_scenary(["ALL", "OPE", "ope_centro2_id2"], self.tests_scenary):
            module_tests_ope.ope_centro2_id2(self)

    def tests_ope_centro2_01_id1(self):
        if self.check_scenary(["ALL", "OPE", "ope_centro2_id1"], self.tests_scenary):
            module_tests_ope.ope_centro2_id1(self)

    def tests_ope_centro2_03_get(self):
        if self.check_scenary(["ALL", "OPE", "ope_centro2_get"], self.tests_scenary):
            module_tests_ope.ope_centro2_get(self)

    def tests_ope_centro2_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_get_by_id(self)

    def tests_ope_centro2_estoque_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_estoque_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_estoque_id2(self)

    def tests_ope_centro2_estoque_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_estoque_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_estoque_id1(self)

    def tests_ope_centro2_estoque_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_estoque_get"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_estoque_get(self)

    def tests_ope_centro2_estoque_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_estoque_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_estoque_get_by_id(self)

    def tests_ope_centro2_estoque_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_estoque_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_estoque_delete(self)

    def tests_ope_centro2_equip_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_equip_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_equip_id2(self)

    def tests_ope_centro2_equip_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_equip_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_equip_id1(self)

    def tests_ope_centro2_equip_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_equip_get"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_equip_get(self)

    def tests_ope_centro2_equip_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_equip_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_equip_get_by_id(self)

    def tests_ope_centro2_equip_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_equip_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_equip_delete(self)

    def tests_ope_centro2_05_delete(self):
        if self.check_scenary(["ALL", "OPE", "ope_centro2_delete"], self.tests_scenary):
            module_tests_ope.ope_centro2_delete(self)

    def tests_ope_centro2_area_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_area_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_area_id2(self)

    def tests_ope_centro2_area_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_area_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_area_id1(self)

    def tests_ope_centro2_area_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_area_get"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_area_get(self)

    def tests_ope_centro2_area_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_area_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_area_get_by_id(self)

    def tests_ope_centro2_area_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro2_area_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_centro2_area_delete(self)

    def tests_ope_centro1_02_id2(self):
        if self.check_scenary(["ALL", "OPE", "ope_centro1_id2"], self.tests_scenary):
            module_tests_ope.ope_centro1_id2(self)

    def tests_ope_centro1_01_id1(self):
        if self.check_scenary(["ALL", "OPE", "ope_centro1_id1"], self.tests_scenary):
            module_tests_ope.ope_centro1_id1(self)

    def tests_ope_centro1_03_get(self):
        if self.check_scenary(["ALL", "OPE", "ope_centro1_get"], self.tests_scenary):
            module_tests_ope.ope_centro1_get(self)

    def tests_ope_centro1_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro1_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_centro1_get_by_id(self)

    def tests_ope_centro1_05_delete(self):
        if self.check_scenary(["ALL", "OPE", "ope_centro1_delete"], self.tests_scenary):
            module_tests_ope.ope_centro1_delete(self)

    def tests_ope_centro_versao_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_versao_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_versao_id2(self)

    def tests_ope_centro_versao_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_versao_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_versao_id1(self)

    def tests_ope_centro_versao_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_versao_get"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_versao_get(self)

    def tests_ope_centro_versao_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_versao_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_versao_get_by_id(self)

    def tests_ope_centro_versao_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_versao_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_versao_delete(self)

    def tests_ope_centro_tipo_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_tipo_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_tipo_id2(self)

    def tests_ope_centro_tipo_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_tipo_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_tipo_id1(self)

    def tests_ope_centro_tipo_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_tipo_get"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_tipo_get(self)

    def tests_ope_centro_tipo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_tipo_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_tipo_get_by_id(self)

    def tests_ope_centro_tipo_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_tipo_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_tipo_delete(self)

    def tests_ope_centro_subtipo_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_subtipo_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_subtipo_id2(self)

    def tests_ope_centro_subtipo_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_subtipo_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_subtipo_id1(self)

    def tests_ope_centro_subtipo_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_subtipo_get"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_subtipo_get(self)

    def tests_ope_centro_subtipo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_subtipo_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_subtipo_get_by_id(self)

    def tests_ope_centro_subtipo_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_subtipo_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_subtipo_delete(self)

    def tests_ope_centro_subgrupo_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_subgrupo_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_subgrupo_id2(self)

    def tests_ope_centro_subgrupo_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_subgrupo_get"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_subgrupo_get(self)

    def tests_ope_centro_subgrupo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_subgrupo_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_subgrupo_get_by_id(self)

    def tests_ope_centro_subgrupo_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_subgrupo_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_subgrupo_delete(self)

    def tests_ope_centro_rend_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_rend_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_rend_id2(self)

    def tests_ope_centro_rend_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_rend_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_rend_id1(self)

    def tests_ope_centro_rend_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_rend_get"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_rend_get(self)

    def tests_ope_centro_rend_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_rend_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_rend_get_by_id(self)

    def tests_ope_centro_rend_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_rend_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_rend_delete(self)

    def tests_ope_centro_rat_tipo_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_rat_tipo_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_rat_tipo_id2(self)

    def tests_ope_centro_rat_tipo_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_rat_tipo_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_rat_tipo_id1(self)

    def tests_ope_centro_rat_tipo_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_rat_tipo_get"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_rat_tipo_get(self)

    def tests_ope_centro_rat_tipo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_rat_tipo_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_rat_tipo_get_by_id(self)

    def tests_ope_centro_rat_tipo_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_rat_tipo_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_rat_tipo_delete(self)

    def tests_ope_centro_prev_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_prev_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_prev_id2(self)

    def tests_ope_centro_prev_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_prev_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_prev_id1(self)

    def tests_ope_centro_prev_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_prev_get"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_prev_get(self)

    def tests_ope_centro_prev_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_prev_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_prev_get_by_id(self)

    def tests_ope_centro_prev_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_prev_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_prev_delete(self)

    def tests_ope_centro_grupo_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_grupo_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_grupo_id2(self)

    def tests_ope_centro_grupo_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_grupo_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_grupo_id1(self)

    def tests_ope_centro_grupo_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_grupo_get"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_grupo_get(self)

    def tests_ope_centro_grupo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_grupo_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_grupo_get_by_id(self)

    def tests_ope_centro_grupo_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_grupo_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_grupo_delete(self)

    def tests_ope_centro_dest_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_dest_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_dest_id2(self)

    def tests_ope_centro_dest_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_dest_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_dest_id1(self)

    def tests_ope_centro_dest_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_dest_get"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_dest_get(self)

    def tests_ope_centro_dest_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_dest_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_dest_get_by_id(self)

    def tests_ope_centro_dest_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_dest_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_dest_delete(self)

    def tests_ope_centro_config_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_config_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_config_id2(self)

    def tests_ope_centro_config_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_config_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_config_id1(self)

    def tests_ope_centro_config_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_config_get"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_config_get(self)

    def tests_ope_centro_config_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_config_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_config_get_by_id(self)

    def tests_ope_centro_config_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_centro_config_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_centro_config_delete(self)

    def tests_ope_atividade_sistema_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_atividade_sistema_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_atividade_sistema_id2(self)

    def tests_ope_atividade_sistema_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_atividade_sistema_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_atividade_sistema_id1(self)

    def tests_ope_atividade_sistema_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_atividade_sistema_get"], self.tests_scenary
        ):
            module_tests_ope.ope_atividade_sistema_get(self)

    def tests_ope_atividade_sistema_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_atividade_sistema_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_atividade_sistema_get_by_id(self)

    def tests_ope_atividade_sistema_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_atividade_sistema_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_atividade_sistema_delete(self)

    def tests_ope_atividade_02_id2(self):
        if self.check_scenary(["ALL", "OPE", "ope_atividade_id2"], self.tests_scenary):
            module_tests_ope.ope_atividade_id2(self)

    def tests_ope_atividade_01_id1(self):
        if self.check_scenary(["ALL", "OPE", "ope_atividade_id1"], self.tests_scenary):
            module_tests_ope.ope_atividade_id1(self)

    def tests_ope_atividade_grupo_02_id2(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_atividade_grupo_id2"], self.tests_scenary
        ):
            module_tests_ope.ope_atividade_grupo_id2(self)

    def tests_ope_atividade_grupo_01_id1(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_atividade_grupo_id1"], self.tests_scenary
        ):
            module_tests_ope.ope_atividade_grupo_id1(self)

    def tests_ope_atividade_grupo_03_get(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_atividade_grupo_get"], self.tests_scenary
        ):
            module_tests_ope.ope_atividade_grupo_get(self)

    def tests_ope_atividade_grupo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_atividade_grupo_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_atividade_grupo_get_by_id(self)

    def tests_ope_atividade_grupo_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_atividade_grupo_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_atividade_grupo_delete(self)

    def tests_ope_atividade_03_get(self):
        if self.check_scenary(["ALL", "OPE", "ope_atividade_get"], self.tests_scenary):
            module_tests_ope.ope_atividade_get(self)

    def tests_ope_atividade_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_atividade_get_by_id"], self.tests_scenary
        ):
            module_tests_ope.ope_atividade_get_by_id(self)

    def tests_ope_atividade_05_delete(self):
        if self.check_scenary(
            ["ALL", "OPE", "ope_atividade_delete"], self.tests_scenary
        ):
            module_tests_ope.ope_atividade_delete(self)

    # ===========================================================
    # MOV
    # ===========================================================

    def tests_mov_unit_param_02_id2(self):
        if self.check_scenary(["ALL", "MOV", "mov_unit_param_id2"], self.tests_scenary):
            module_tests_mov.mov_unit_param_id2(self)

    def tests_mov_unit_param_01_id1(self):
        if self.check_scenary(["ALL", "MOV", "mov_unit_param_id1"], self.tests_scenary):
            module_tests_mov.mov_unit_param_id1(self)

    def tests_mov_unit_param_03_get(self):
        if self.check_scenary(["ALL", "MOV", "mov_unit_param_get"], self.tests_scenary):
            module_tests_mov.mov_unit_param_get(self)

    def tests_mov_unit_param_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "MOV", "mov_unit_param_get_by_id"], self.tests_scenary
        ):
            module_tests_mov.mov_unit_param_get_by_id(self)

    def tests_mov_unit_param_05_delete(self):
        if self.check_scenary(
            ["ALL", "MOV", "mov_unit_param_delete"], self.tests_scenary
        ):
            module_tests_mov.mov_unit_param_delete(self)

    def tests_mov_tomador_02_id2(self):
        if self.check_scenary(["ALL", "MOV", "mov_tomador_id2"], self.tests_scenary):
            module_tests_mov.mov_tomador_id2(self)

    def tests_mov_tomador_01_id1(self):
        if self.check_scenary(["ALL", "MOV", "mov_tomador_id1"], self.tests_scenary):
            module_tests_mov.mov_tomador_id1(self)

    def tests_mov_tomador_03_get(self):
        if self.check_scenary(["ALL", "MOV", "mov_tomador_get"], self.tests_scenary):
            module_tests_mov.mov_tomador_get(self)

    def tests_mov_tomador_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "MOV", "mov_tomador_get_by_id"], self.tests_scenary
        ):
            module_tests_mov.mov_tomador_get_by_id(self)

    def tests_mov_tomador_05_delete(self):
        if self.check_scenary(["ALL", "MOV", "mov_tomador_delete"], self.tests_scenary):
            module_tests_mov.mov_tomador_delete(self)

    def tests_mov_tipo_02_id2(self):
        if self.check_scenary(["ALL", "MOV", "mov_tipo_id2"], self.tests_scenary):
            module_tests_mov.mov_tipo_id2(self)

    def tests_mov_tipo_01_id1(self):
        if self.check_scenary(["ALL", "MOV", "mov_tipo_id1"], self.tests_scenary):
            module_tests_mov.mov_tipo_id1(self)

    def tests_mov_tipo_03_get(self):
        if self.check_scenary(["ALL", "MOV", "mov_tipo_get"], self.tests_scenary):
            module_tests_mov.mov_tipo_get(self)

    def tests_mov_tipo_04_get_by_id(self):
        if self.check_scenary(["ALL", "MOV", "mov_tipo_get_by_id"], self.tests_scenary):
            module_tests_mov.mov_tipo_get_by_id(self)

    def tests_mov_tipo_05_delete(self):
        if self.check_scenary(["ALL", "MOV", "mov_tipo_delete"], self.tests_scenary):
            module_tests_mov.mov_tipo_delete(self)

    def tests_mov_status_02_id2(self):
        if self.check_scenary(["ALL", "MOV", "mov_status_id2"], self.tests_scenary):
            module_tests_mov.mov_status_id2(self)

    def tests_mov_status_01_id1(self):
        if self.check_scenary(["ALL", "MOV", "mov_status_id1"], self.tests_scenary):
            module_tests_mov.mov_status_id1(self)

    def tests_mov_status_03_get(self):
        if self.check_scenary(["ALL", "MOV", "mov_status_get"], self.tests_scenary):
            module_tests_mov.mov_status_get(self)

    def tests_mov_status_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "MOV", "mov_status_get_by_id"], self.tests_scenary
        ):
            module_tests_mov.mov_status_get_by_id(self)

    def tests_mov_status_05_delete(self):
        if self.check_scenary(["ALL", "MOV", "mov_status_delete"], self.tests_scenary):
            module_tests_mov.mov_status_delete(self)

    def tests_mov_seguradora_02_id2(self):
        if self.check_scenary(["ALL", "MOV", "mov_seguradora_id2"], self.tests_scenary):
            module_tests_mov.mov_seguradora_id2(self)

    def tests_mov_seguradora_01_id1(self):
        if self.check_scenary(["ALL", "MOV", "mov_seguradora_id1"], self.tests_scenary):
            module_tests_mov.mov_seguradora_id1(self)

    def tests_mov_seguradora_03_get(self):
        if self.check_scenary(["ALL", "MOV", "mov_seguradora_get"], self.tests_scenary):
            module_tests_mov.mov_seguradora_get(self)

    def tests_mov_seguradora_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "MOV", "mov_seguradora_get_by_id"], self.tests_scenary
        ):
            module_tests_mov.mov_seguradora_get_by_id(self)

    def tests_mov_seguradora_05_delete(self):
        if self.check_scenary(
            ["ALL", "MOV", "mov_seguradora_delete"], self.tests_scenary
        ):
            module_tests_mov.mov_seguradora_delete(self)

    def tests_mov_reboque_02_id2(self):
        if self.check_scenary(["ALL", "MOV", "mov_reboque_id2"], self.tests_scenary):
            module_tests_mov.mov_reboque_id2(self)

    def tests_mov_reboque_01_id1(self):
        if self.check_scenary(["ALL", "MOV", "mov_reboque_id1"], self.tests_scenary):
            module_tests_mov.mov_reboque_id1(self)

    def tests_mov_reboque_03_get(self):
        if self.check_scenary(["ALL", "MOV", "mov_reboque_get"], self.tests_scenary):
            module_tests_mov.mov_reboque_get(self)

    def tests_mov_reboque_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "MOV", "mov_reboque_get_by_id"], self.tests_scenary
        ):
            module_tests_mov.mov_reboque_get_by_id(self)

    def tests_mov_reboque_05_delete(self):
        if self.check_scenary(["ALL", "MOV", "mov_reboque_delete"], self.tests_scenary):
            module_tests_mov.mov_reboque_delete(self)

    def tests_mov_percurso_02_id2(self):
        if self.check_scenary(["ALL", "MOV", "mov_percurso_id2"], self.tests_scenary):
            module_tests_mov.mov_percurso_id2(self)

    def tests_mov_percurso_01_id1(self):
        if self.check_scenary(["ALL", "MOV", "mov_percurso_id1"], self.tests_scenary):
            module_tests_mov.mov_percurso_id1(self)

    def tests_mov_percurso_03_get(self):
        if self.check_scenary(["ALL", "MOV", "mov_percurso_get"], self.tests_scenary):
            module_tests_mov.mov_percurso_get(self)

    def tests_mov_percurso_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "MOV", "mov_percurso_get_by_id"], self.tests_scenary
        ):
            module_tests_mov.mov_percurso_get_by_id(self)

    def tests_mov_percurso_05_delete(self):
        if self.check_scenary(
            ["ALL", "MOV", "mov_percurso_delete"], self.tests_scenary
        ):
            module_tests_mov.mov_percurso_delete(self)

    def tests_mov_pedagio_02_id2(self):
        if self.check_scenary(["ALL", "MOV", "mov_pedagio_id2"], self.tests_scenary):
            module_tests_mov.mov_pedagio_id2(self)

    def tests_mov_pedagio_01_id1(self):
        if self.check_scenary(["ALL", "MOV", "mov_pedagio_id1"], self.tests_scenary):
            module_tests_mov.mov_pedagio_id1(self)

    def tests_mov_pedagio_03_get(self):
        if self.check_scenary(["ALL", "MOV", "mov_pedagio_get"], self.tests_scenary):
            module_tests_mov.mov_pedagio_get(self)

    def tests_mov_pedagio_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "MOV", "mov_pedagio_get_by_id"], self.tests_scenary
        ):
            module_tests_mov.mov_pedagio_get_by_id(self)

    def tests_mov_pedagio_05_delete(self):
        if self.check_scenary(["ALL", "MOV", "mov_pedagio_delete"], self.tests_scenary):
            module_tests_mov.mov_pedagio_delete(self)

    def tests_mov_origem_02_id2(self):
        if self.check_scenary(["ALL", "MOV", "mov_origem_id2"], self.tests_scenary):
            module_tests_mov.mov_origem_id2(self)

    def tests_mov_origem_01_id1(self):
        if self.check_scenary(["ALL", "MOV", "mov_origem_id1"], self.tests_scenary):
            module_tests_mov.mov_origem_id1(self)

    def tests_mov_origem_03_get(self):
        if self.check_scenary(["ALL", "MOV", "mov_origem_get"], self.tests_scenary):
            module_tests_mov.mov_origem_get(self)

    def tests_mov_origem_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "MOV", "mov_origem_get_by_id"], self.tests_scenary
        ):
            module_tests_mov.mov_origem_get_by_id(self)

    def tests_mov_origem_05_delete(self):
        if self.check_scenary(["ALL", "MOV", "mov_origem_delete"], self.tests_scenary):
            module_tests_mov.mov_origem_delete(self)

    def tests_mov_operacao_02_id2(self):
        if self.check_scenary(["ALL", "MOV", "mov_operacao_id2"], self.tests_scenary):
            module_tests_mov.mov_operacao_id2(self)

    def tests_mov_operacao_01_id1(self):
        if self.check_scenary(["ALL", "MOV", "mov_operacao_id1"], self.tests_scenary):
            module_tests_mov.mov_operacao_id1(self)

    def tests_mov_operacao_03_get(self):
        if self.check_scenary(["ALL", "MOV", "mov_operacao_get"], self.tests_scenary):
            module_tests_mov.mov_operacao_get(self)

    def tests_mov_operacao_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "MOV", "mov_operacao_get_by_id"], self.tests_scenary
        ):
            module_tests_mov.mov_operacao_get_by_id(self)

    def tests_mov_operacao_05_delete(self):
        if self.check_scenary(
            ["ALL", "MOV", "mov_operacao_delete"], self.tests_scenary
        ):
            module_tests_mov.mov_operacao_delete(self)

    def tests_mov_medida_02_id2(self):
        if self.check_scenary(["ALL", "MOV", "mov_medida_id2"], self.tests_scenary):
            module_tests_mov.mov_medida_id2(self)

    def tests_mov_medida_01_id1(self):
        if self.check_scenary(["ALL", "MOV", "mov_medida_id1"], self.tests_scenary):
            module_tests_mov.mov_medida_id1(self)

    def tests_mov_medida_03_get(self):
        if self.check_scenary(["ALL", "MOV", "mov_medida_get"], self.tests_scenary):
            module_tests_mov.mov_medida_get(self)

    def tests_mov_medida_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "MOV", "mov_medida_get_by_id"], self.tests_scenary
        ):
            module_tests_mov.mov_medida_get_by_id(self)

    def tests_mov_medida_05_delete(self):
        if self.check_scenary(["ALL", "MOV", "mov_medida_delete"], self.tests_scenary):
            module_tests_mov.mov_medida_delete(self)

    def tests_mov_lacre_02_id2(self):
        if self.check_scenary(["ALL", "MOV", "mov_lacre_id2"], self.tests_scenary):
            module_tests_mov.mov_lacre_id2(self)

    def tests_mov_lacre_01_id1(self):
        if self.check_scenary(["ALL", "MOV", "mov_lacre_id1"], self.tests_scenary):
            module_tests_mov.mov_lacre_id1(self)

    def tests_mov_lacre_03_get(self):
        if self.check_scenary(["ALL", "MOV", "mov_lacre_get"], self.tests_scenary):
            module_tests_mov.mov_lacre_get(self)

    def tests_mov_lacre_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "MOV", "mov_lacre_get_by_id"], self.tests_scenary
        ):
            module_tests_mov.mov_lacre_get_by_id(self)

    def tests_mov_lacre_05_delete(self):
        if self.check_scenary(["ALL", "MOV", "mov_lacre_delete"], self.tests_scenary):
            module_tests_mov.mov_lacre_delete(self)

    def tests_mov_itemserv_02_id2(self):
        if self.check_scenary(["ALL", "MOV", "mov_itemserv_id2"], self.tests_scenary):
            module_tests_mov.mov_itemserv_id2(self)

    def tests_mov_itemserv_01_id1(self):
        if self.check_scenary(["ALL", "MOV", "mov_itemserv_id1"], self.tests_scenary):
            module_tests_mov.mov_itemserv_id1(self)

    def tests_mov_itemserv_03_get(self):
        if self.check_scenary(["ALL", "MOV", "mov_itemserv_get"], self.tests_scenary):
            module_tests_mov.mov_itemserv_get(self)

    def tests_mov_itemserv_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "MOV", "mov_itemserv_get_by_id"], self.tests_scenary
        ):
            module_tests_mov.mov_itemserv_get_by_id(self)

    def tests_mov_itemserv_05_delete(self):
        if self.check_scenary(
            ["ALL", "MOV", "mov_itemserv_delete"], self.tests_scenary
        ):
            module_tests_mov.mov_itemserv_delete(self)

    def tests_mov_02_id2(self):
        if self.check_scenary(["ALL", "MOV", "mov_id2"], self.tests_scenary):
            module_tests_mov.mov_id2(self)

    def tests_mov_01_id1(self):
        if self.check_scenary(["ALL", "MOV", "mov_id1"], self.tests_scenary):
            module_tests_mov.mov_id1(self)

    def tests_mov_03_get(self):
        if self.check_scenary(["ALL", "MOV", "mov_get"], self.tests_scenary):
            module_tests_mov.mov_get(self)

    def tests_mov_04_get_by_id(self):
        if self.check_scenary(["ALL", "MOV", "mov_get_by_id"], self.tests_scenary):
            module_tests_mov.mov_get_by_id(self)

    def tests_mov_frete_02_id2(self):
        if self.check_scenary(["ALL", "MOV", "mov_frete_id2"], self.tests_scenary):
            module_tests_mov.mov_frete_id2(self)

    def tests_mov_frete_01_id1(self):
        if self.check_scenary(["ALL", "MOV", "mov_frete_id1"], self.tests_scenary):
            module_tests_mov.mov_frete_id1(self)

    def tests_mov_frete_03_get(self):
        if self.check_scenary(["ALL", "MOV", "mov_frete_get"], self.tests_scenary):
            module_tests_mov.mov_frete_get(self)

    def tests_mov_frete_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "MOV", "mov_frete_get_by_id"], self.tests_scenary
        ):
            module_tests_mov.mov_frete_get_by_id(self)

    def tests_mov_frete_05_delete(self):
        if self.check_scenary(["ALL", "MOV", "mov_frete_delete"], self.tests_scenary):
            module_tests_mov.mov_frete_delete(self)

    def tests_mov_est_nivel_02_id2(self):
        if self.check_scenary(["ALL", "MOV", "mov_est_nivel_id2"], self.tests_scenary):
            module_tests_mov.mov_est_nivel_id2(self)

    def tests_mov_est_nivel_01_id1(self):
        if self.check_scenary(["ALL", "MOV", "mov_est_nivel_id1"], self.tests_scenary):
            module_tests_mov.mov_est_nivel_id1(self)

    def tests_mov_est_nivel_03_get(self):
        if self.check_scenary(["ALL", "MOV", "mov_est_nivel_get"], self.tests_scenary):
            module_tests_mov.mov_est_nivel_get(self)

    def tests_mov_est_nivel_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "MOV", "mov_est_nivel_get_by_id"], self.tests_scenary
        ):
            module_tests_mov.mov_est_nivel_get_by_id(self)

    def tests_mov_est_nivel_05_delete(self):
        if self.check_scenary(
            ["ALL", "MOV", "mov_est_nivel_delete"], self.tests_scenary
        ):
            module_tests_mov.mov_est_nivel_delete(self)

    def tests_mov_entrega_02_id2(self):
        if self.check_scenary(["ALL", "MOV", "mov_entrega_id2"], self.tests_scenary):
            module_tests_mov.mov_entrega_id2(self)

    def tests_mov_entrega_01_id1(self):
        if self.check_scenary(["ALL", "MOV", "mov_entrega_id1"], self.tests_scenary):
            module_tests_mov.mov_entrega_id1(self)

    def tests_mov_entrega_03_get(self):
        if self.check_scenary(["ALL", "MOV", "mov_entrega_get"], self.tests_scenary):
            module_tests_mov.mov_entrega_get(self)

    def tests_mov_entrega_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "MOV", "mov_entrega_get_by_id"], self.tests_scenary
        ):
            module_tests_mov.mov_entrega_get_by_id(self)

    def tests_mov_entrega_05_delete(self):
        if self.check_scenary(["ALL", "MOV", "mov_entrega_delete"], self.tests_scenary):
            module_tests_mov.mov_entrega_delete(self)

    def tests_mov_05_delete(self):
        if self.check_scenary(["ALL", "MOV", "mov_delete"], self.tests_scenary):
            module_tests_mov.mov_delete(self)

    def tests_mov_cotacao_02_id2(self):
        if self.check_scenary(["ALL", "MOV", "mov_cotacao_id2"], self.tests_scenary):
            module_tests_mov.mov_cotacao_id2(self)

    def tests_mov_cotacao_01_id1(self):
        if self.check_scenary(["ALL", "MOV", "mov_cotacao_id1"], self.tests_scenary):
            module_tests_mov.mov_cotacao_id1(self)

    def tests_mov_cotacao_03_get(self):
        if self.check_scenary(["ALL", "MOV", "mov_cotacao_get"], self.tests_scenary):
            module_tests_mov.mov_cotacao_get(self)

    def tests_mov_cotacao_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "MOV", "mov_cotacao_get_by_id"], self.tests_scenary
        ):
            module_tests_mov.mov_cotacao_get_by_id(self)

    def tests_mov_cotacao_05_delete(self):
        if self.check_scenary(["ALL", "MOV", "mov_cotacao_delete"], self.tests_scenary):
            module_tests_mov.mov_cotacao_delete(self)

    def tests_mov_condutor_02_id2(self):
        if self.check_scenary(["ALL", "MOV", "mov_condutor_id2"], self.tests_scenary):
            module_tests_mov.mov_condutor_id2(self)

    def tests_mov_condutor_01_id1(self):
        if self.check_scenary(["ALL", "MOV", "mov_condutor_id1"], self.tests_scenary):
            module_tests_mov.mov_condutor_id1(self)

    def tests_mov_condutor_03_get(self):
        if self.check_scenary(["ALL", "MOV", "mov_condutor_get"], self.tests_scenary):
            module_tests_mov.mov_condutor_get(self)

    def tests_mov_condutor_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "MOV", "mov_condutor_get_by_id"], self.tests_scenary
        ):
            module_tests_mov.mov_condutor_get_by_id(self)

    def tests_mov_condutor_05_delete(self):
        if self.check_scenary(
            ["ALL", "MOV", "mov_condutor_delete"], self.tests_scenary
        ):
            module_tests_mov.mov_condutor_delete(self)

    def tests_mov_comp_02_id2(self):
        if self.check_scenary(["ALL", "MOV", "mov_comp_id2"], self.tests_scenary):
            module_tests_mov.mov_comp_id2(self)

    def tests_mov_comp_01_id1(self):
        if self.check_scenary(["ALL", "MOV", "mov_comp_id1"], self.tests_scenary):
            module_tests_mov.mov_comp_id1(self)

    def tests_mov_comp_03_get(self):
        if self.check_scenary(["ALL", "MOV", "mov_comp_get"], self.tests_scenary):
            module_tests_mov.mov_comp_get(self)

    def tests_mov_comp_04_get_by_id(self):
        if self.check_scenary(["ALL", "MOV", "mov_comp_get_by_id"], self.tests_scenary):
            module_tests_mov.mov_comp_get_by_id(self)

    def tests_mov_comp_05_delete(self):
        if self.check_scenary(["ALL", "MOV", "mov_comp_delete"], self.tests_scenary):
            module_tests_mov.mov_comp_delete(self)

    def tests_mov_ciot_02_id2(self):
        if self.check_scenary(["ALL", "MOV", "mov_ciot_id2"], self.tests_scenary):
            module_tests_mov.mov_ciot_id2(self)

    def tests_mov_ciot_01_id1(self):
        if self.check_scenary(["ALL", "MOV", "mov_ciot_id1"], self.tests_scenary):
            module_tests_mov.mov_ciot_id1(self)

    def tests_mov_ciot_03_get(self):
        if self.check_scenary(["ALL", "MOV", "mov_ciot_get"], self.tests_scenary):
            module_tests_mov.mov_ciot_get(self)

    def tests_mov_ciot_04_get_by_id(self):
        if self.check_scenary(["ALL", "MOV", "mov_ciot_get_by_id"], self.tests_scenary):
            module_tests_mov.mov_ciot_get_by_id(self)

    def tests_mov_ciot_05_delete(self):
        if self.check_scenary(["ALL", "MOB", "mov_ciot_delete"], self.tests_scenary):
            module_tests_mov.mov_ciot_delete(self)

    # ===========================================================
    # MOB
    # ===========================================================

    def mob_unit_param_02_id2(self):
        if self.check_scenary(["ALL", "MOB", "it_param_id2"], self.tests_scenary):
            module_tests_mob.mob_unit_param_id2(self)

    def mob_unit_param_01_id1(self):
        if self.check_scenary(["ALL", "MOB", "it_param_id1"], self.tests_scenary):
            module_tests_mob.mob_unit_param_id1(self)

    def mob_unit_param_03_get(self):
        if self.check_scenary(["ALL", "MOB", "it_param_get"], self.tests_scenary):
            module_tests_mob.mob_unit_param_get(self)

    def mob_unit_param_04_get_by_id(self):
        if self.check_scenary(["ALL", "MOB", "it_param_get_by_id"], self.tests_scenary):
            module_tests_mob.mob_unit_param_get_by_id(self)

    def mob_unit_param_05_delete(self):
        if self.check_scenary(["ALL", "MOB", "it_param_delete"], self.tests_scenary):
            module_tests_mob.mob_unit_param_delete(self)

    # ===========================================================
    # BOV
    # ===========================================================

    def tests_bov_unit_param_02_id2(self):
        if self.check_scenary(["ALL", "BOV", "bov_unit_param_id2"], self.tests_scenary):
            module_tests_bov.bov_unit_param_id2(self)

    def tests_bov_unit_param_01_id1(self):
        if self.check_scenary(["ALL", "BOV", "bov_unit_param_id1"], self.tests_scenary):
            module_tests_bov.bov_unit_param_id1(self)

    def tests_bov_unit_param_03_get(self):
        if self.check_scenary(["ALL", "BOV", "bov_unit_param_get"], self.tests_scenary):
            module_tests_bov.bov_unit_param_get(self)

    def tests_bov_unit_param_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "BOV", "bov_unit_param_get_by_id"], self.tests_scenary
        ):
            module_tests_bov.bov_unit_param_get_by_id(self)

    def tests_bov_unit_param_05_delete(self):
        if self.check_scenary(
            ["ALL", "BOV", "bov_unit_param_delete"], self.tests_scenary
        ):
            module_tests_bov.bov_unit_param_delete(self)

    # ===========================================================
    # CMS
    # ===========================================================

    def tests_cms_tag_02_id2(self):
        if self.check_scenary(["ALL", "CMS", "cms_tag_id2"], self.tests_scenary):
            module_tests_cms.cms_tag_id2(self)

    def tests_cms_tag_01_id1(self):
        if self.check_scenary(["ALL", "CMS", "cms_tag_id1"], self.tests_scenary):
            module_tests_cms.cms_tag_id1(self)

    def tests_cms_tag_03_get(self):
        if self.check_scenary(["ALL", "CMS", "cms_tag_get"], self.tests_scenary):
            module_tests_cms.cms_tag_get(self)

    def tests_cms_tag_04_get_by_id(self):
        if self.check_scenary(["ALL", "CMS", "cms_tag_get_by_id"], self.tests_scenary):
            module_tests_cms.cms_tag_get_by_id(self)

    def tests_cms_tag_05_delete(self):
        if self.check_scenary(["ALL", "CMS", "cms_tag_delete"], self.tests_scenary):
            module_tests_cms.cms_tag_delete(self)

    def tests_cms_post_02_id2(self):
        if self.check_scenary(["ALL", "CMS", "cms_post_id2"], self.tests_scenary):
            module_tests_cms.cms_post_id2(self)

    def tests_cms_post_01_id1(self):
        if self.check_scenary(["ALL", "CMS", "cms_post_id1"], self.tests_scenary):
            module_tests_cms.cms_post_id1(self)

    def tests_cms_post_hist_02_id2(self):
        if self.check_scenary(["ALL", "CMS", "cms_post_hist_id2"], self.tests_scenary):
            module_tests_cms.cms_post_hist_id2(self)

    def tests_cms_post_hist_01_id1(self):
        if self.check_scenary(["ALL", "CMS", "cms_post_hist_id1"], self.tests_scenary):
            module_tests_cms.cms_post_hist_id1(self)

    def tests_cms_post_hist_03_get(self):
        if self.check_scenary(["ALL", "CMS", "cms_post_hist_get"], self.tests_scenary):
            module_tests_cms.cms_post_hist_get(self)

    def tests_cms_post_hist_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CMS", "cms_post_hist_get_by_id"], self.tests_scenary
        ):
            module_tests_cms.cms_post_hist_get_by_id(self)

    def tests_cms_post_hist_05_delete(self):
        if self.check_scenary(
            ["ALL", "CMS", "cms_post_hist_delete"], self.tests_scenary
        ):
            module_tests_cms.cms_post_hist_delete(self)

    def tests_cms_post_03_get(self):
        if self.check_scenary(["ALL", "CMS", "cms_post_get"], self.tests_scenary):
            module_tests_cms.cms_post_get(self)

    def tests_cms_post_04_get_by_id(self):
        if self.check_scenary(["ALL", "CMS", "cms_post_get_by_id"], self.tests_scenary):
            module_tests_cms.cms_post_get_by_id(self)

    def tests_cms_post_05_delete(self):
        if self.check_scenary(["ALL", "CMS", "cms_post_delete"], self.tests_scenary):
            module_tests_cms.cms_post_delete(self)

    def tests_cms_grupo_02_id2(self):
        if self.check_scenary(["ALL", "CMS", "cms_grupo_id2"], self.tests_scenary):
            module_tests_cms.cms_grupo_id2(self)

    def tests_cms_grupo_01_id1(self):
        if self.check_scenary(["ALL", "CMS", "cms_grupo_id1"], self.tests_scenary):
            module_tests_cms.cms_grupo_id1(self)

    def tests_cms_grupo_03_get(self):
        if self.check_scenary(["ALL", "CMS", "cms_grupo_get"], self.tests_scenary):
            module_tests_cms.cms_grupo_get(self)

    def tests_cms_grupo_04_get_by_id(self):
        if self.check_scenary(
            ["ALL", "CMS", "cms_grupo_get_by_id"], self.tests_scenary
        ):
            module_tests_cms.cms_grupo_get_by_id(self)

    def tests_cms_grupo_05_delete(self):
        if self.check_scenary(["ALL", "CMS"], self.tests_scenary):
            module_tests_cms.cms_grupo_delete(self)

    # ===========================================================
    # IND
    # ===========================================================

    def tests_ind_vr_trimestre_2_id2(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_trimestre_id2"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_trimestre_id2(self)

    def tests_ind_vr_trimestre_1_id1(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_trimestre_id1"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_trimestre_id1(self)

    def tests_ind_vr_trimestre_3_get(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_trimestre_get"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_trimestre_get(self)

    def tests_ind_vr_trimestre_4_get_by_id(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_trimestre_get_by_id"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_trimestre_get_by_id(self)

    def tests_ind_vr_trimestre_5_delete(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_trimestre_delete"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_trimestre_delete(self)

    def tests_ind_vr_semestre_2_id2(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_semestre_id2"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_semestre_id2(self)

    def tests_ind_vr_semestre_1_id1(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_semestre_id1"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_semestre_id1(self)

    def tests_ind_vr_semestre_3_get(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_semestre_get"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_semestre_get(self)

    def tests_ind_vr_semestre_4_get_by_id(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_semestre_get_by_id"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_semestre_get_by_id(self)

    def tests_ind_vr_semestre_5_delete(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_semestre_delete"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_semestre_delete(self)

    def tests_ind_vr_semana_2_id2(self):
        if self.check_scenary(["ALL", "IND", "ind_vr_semana_id2"], self.tests_scenary):
            module_tests_ind.ind_vr_semana_id2(self)

    def tests_ind_vr_semana_1_id1(self):
        if self.check_scenary(["ALL", "IND", "ind_vr_semana_id1"], self.tests_scenary):
            module_tests_ind.ind_vr_semana_id1(self)

    def tests_ind_vr_semana_3_get(self):
        if self.check_scenary(["ALL", "IND", "ind_vr_semana_get"], self.tests_scenary):
            module_tests_ind.ind_vr_semana_get(self)

    def tests_ind_vr_semana_4_get_by_id(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_semana_get_by_id"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_semana_get_by_id(self)

    def tests_ind_vr_semana_5_delete(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_semana_delete"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_semana_delete(self)

    def tests_ind_vr_quinzena_2_id2(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_quinzena_id2"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_quinzena_id2(self)

    def tests_ind_vr_quinzena_1_id1(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_quinzena_id1"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_quinzena_id1(self)

    def tests_ind_vr_quinzena_3_get(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_quinzena_get"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_quinzena_get(self)

    def tests_ind_vr_quinzena_4_get_by_id(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_quinzena_get_by_id"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_quinzena_get_by_id(self)

    def tests_ind_vr_quinzena_5_delete(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_quinzena_delete"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_quinzena_delete(self)

    def tests_ind_vr_quadrimestre_2_id2(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_quadrimestre_id2"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_quadrimestre_id2(self)

    def tests_ind_vr_quadrimestre_1_id1(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_quadrimestre_id1"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_quadrimestre_id1(self)

    def tests_ind_vr_quadrimestre_3_get(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_quadrimestre_get"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_quadrimestre_get(self)

    def tests_ind_vr_quadrimestre_4_get_by_id(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_quadrimestre_get_by_id"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_quadrimestre_get_by_id(self)

    def tests_ind_vr_quadrimestre_5_delete(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_quadrimestre_delete"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_quadrimestre_delete(self)

    def tests_ind_vr_mes_2_id2(self):
        if self.check_scenary(["ALL", "IND", "ind_vr_mes_id2"], self.tests_scenary):
            module_tests_ind.ind_vr_mes_id2(self)

    def tests_ind_vr_mes_1_id1(self):
        if self.check_scenary(["ALL", "IND", "ind_vr_mes_id1"], self.tests_scenary):
            module_tests_ind.ind_vr_mes_id1(self)

    def tests_ind_vr_mes_3_get(self):
        if self.check_scenary(["ALL", "IND", "ind_vr_mes_get"], self.tests_scenary):
            module_tests_ind.ind_vr_mes_get(self)

    def tests_ind_vr_mes_4_get_by_id(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_mes_get_by_id"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_mes_get_by_id(self)

    def tests_ind_vr_mes_5_delete(self):
        if self.check_scenary(["ALL", "IND", "ind_vr_mes_delete"], self.tests_scenary):
            module_tests_ind.ind_vr_mes_delete(self)

    def tests_ind_vr_dia_2_id2(self):
        if self.check_scenary(["ALL", "IND", "ind_vr_dia_id2"], self.tests_scenary):
            module_tests_ind.ind_vr_dia_id2(self)

    def tests_ind_vr_dia_1_id1(self):
        if self.check_scenary(["ALL", "IND", "ind_vr_dia_id1"], self.tests_scenary):
            module_tests_ind.ind_vr_dia_id1(self)

    def tests_ind_vr_dia_3_get(self):
        if self.check_scenary(["ALL", "IND", "ind_vr_dia_get"], self.tests_scenary):
            module_tests_ind.ind_vr_dia_get(self)

    def tests_ind_vr_dia_4_get_by_id(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_dia_get_by_id"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_dia_get_by_id(self)

    def tests_ind_vr_dia_5_delete(self):
        if self.check_scenary(["ALL", "IND", "ind_vr_dia_delete"], self.tests_scenary):
            module_tests_ind.ind_vr_dia_delete(self)

    def tests_ind_vr_bimestre_2_id2(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_bimestre_id2"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_bimestre_id2(self)

    def tests_ind_vr_bimestre_1_id1(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_bimestre_id1"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_bimestre_id1(self)

    def tests_ind_vr_bimestre_3_get(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_bimestre_get"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_bimestre_get(self)

    def tests_ind_vr_bimestre_4_get_by_id(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_bimestre_get_by_id"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_bimestre_get_by_id(self)

    def tests_ind_vr_bimestre_5_delete(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_bimestre_delete"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_bimestre_delete(self)

    def tests_ind_vr_ano_2_id2(self):
        if self.check_scenary(["ALL", "IND", "ind_vr_ano_id2"], self.tests_scenary):
            module_tests_ind.ind_vr_ano_id2(self)

    def tests_ind_vr_ano_1_id1(self):
        if self.check_scenary(["ALL", "IND", "ind_vr_ano_id1"], self.tests_scenary):
            module_tests_ind.ind_vr_ano_id1(self)

    def tests_ind_vr_ano_3_get(self):
        if self.check_scenary(["ALL", "IND", "ind_vr_ano_get"], self.tests_scenary):
            module_tests_ind.ind_vr_ano_get(self)

    def tests_ind_vr_ano_4_get_by_id(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_vr_ano_get_by_id"], self.tests_scenary
        ):
            module_tests_ind.ind_vr_ano_get_by_id(self)

    def tests_ind_vr_ano_5_delete(self):
        if self.check_scenary(["ALL", "IND", "ind_vr_ano_delete"], self.tests_scenary):
            module_tests_ind.ind_vr_ano_delete(self)

    def tests_ind_unit_param_2_id2(self):
        if self.check_scenary(["ALL", "IND", "ind_unit_param_id2"], self.tests_scenary):
            module_tests_ind.ind_unit_param_id2(self)

    def tests_ind_unit_param_1_id1(self):
        if self.check_scenary(["ALL", "IND", "ind_unit_param_id1"], self.tests_scenary):
            module_tests_ind.ind_unit_param_id1(self)

    def tests_ind_unit_param_3_get(self):
        if self.check_scenary(["ALL", "IND", "ind_unit_param_get"], self.tests_scenary):
            module_tests_ind.ind_unit_param_get(self)

    def tests_ind_unit_param_4_get_by_id(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_unit_param_get_by_id"], self.tests_scenary
        ):
            module_tests_ind.ind_unit_param_get_by_id(self)

    def tests_ind_unit_param_5_delete(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_unit_param_delete"], self.tests_scenary
        ):
            module_tests_ind.ind_unit_param_delete(self)

    def tests_ind_subgrupo_2_id2(self):
        if self.check_scenary(["ALL", "IND", "ind_subgrupo_id2"], self.tests_scenary):
            module_tests_ind.ind_subgrupo_id2(self)

    def tests_ind_subgrupo_1_id1(self):
        if self.check_scenary(["ALL", "IND", "ind_subgrupo_id1"], self.tests_scenary):
            module_tests_ind.ind_subgrupo_id1(self)

    def tests_ind_subgrupo_3_get(self):
        if self.check_scenary(["ALL", "IND", "ind_subgrupo_get"], self.tests_scenary):
            module_tests_ind.ind_subgrupo_get(self)

    def tests_ind_subgrupo_4_get_by_id(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_subgrupo_get_by_id"], self.tests_scenary
        ):
            module_tests_ind.ind_subgrupo_get_by_id(self)

    def tests_ind_subgrupo_5_delete(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_subgrupo_delete"], self.tests_scenary
        ):
            module_tests_ind.ind_subgrupo_delete(self)

    def tests_ind_rel_2_id2(self):
        if self.check_scenary(["ALL", "IND", "ind_rel_id2"], self.tests_scenary):
            module_tests_ind.ind_rel_id2(self)

    def tests_ind_rel_1_id1(self):
        if self.check_scenary(["ALL", "IND", "ind_rel_id1"], self.tests_scenary):
            module_tests_ind.ind_rel_id1(self)

    def tests_ind_rel_3_get(self):
        if self.check_scenary(["ALL", "IND", "ind_rel_get"], self.tests_scenary):
            module_tests_ind.ind_rel_get(self)

    def tests_ind_rel_4_get_by_id(self):
        if self.check_scenary(["ALL", "IND", "ind_rel_get_by_id"], self.tests_scenary):
            module_tests_ind.ind_rel_get_by_id(self)

    def tests_ind_rel_5_delete(self):
        if self.check_scenary(["ALL", "IND", "ind_rel_delete"], self.tests_scenary):
            module_tests_ind.ind_rel_delete(self)

    def tests_ind_prm_2_id2(self):
        if self.check_scenary(["ALL", "IND", "ind_prm_id2"], self.tests_scenary):
            module_tests_ind.ind_prm_id2(self)

    def tests_ind_prm_1_id1(self):
        if self.check_scenary(["ALL", "IND", "ind_prm_id1"], self.tests_scenary):
            module_tests_ind.ind_prm_id1(self)

    def tests_ind_prm_3_get(self):
        if self.check_scenary(["ALL", "IND", "ind_prm_get"], self.tests_scenary):
            module_tests_ind.ind_prm_get(self)

    def tests_ind_prm_4_get_by_id(self):
        if self.check_scenary(["ALL", "IND", "ind_prm_get_by_id"], self.tests_scenary):
            module_tests_ind.ind_prm_get_by_id(self)

    def tests_ind_prm_5_delete(self):
        if self.check_scenary(["ALL", "IND", "ind_prm_delete"], self.tests_scenary):
            module_tests_ind.ind_prm_delete(self)

    def tests_ind_pnl_2_id2(self):
        if self.check_scenary(["ALL", "IND", "ind_pnl_id2"], self.tests_scenary):
            module_tests_ind.ind_pnl_id2(self)

    def tests_ind_pnl_1_id1(self):
        if self.check_scenary(["ALL", "IND", "ind_pnl_id1"], self.tests_scenary):
            module_tests_ind.ind_pnl_id1(self)

    def tests_ind_pnl_3_get(self):
        if self.check_scenary(["ALL", "IND", "ind_pnl_get"], self.tests_scenary):
            module_tests_ind.ind_pnl_get(self)

    def tests_ind_pnl_4_get_by_id(self):
        if self.check_scenary(["ALL", "IND", "ind_pnl_get_by_id"], self.tests_scenary):
            module_tests_ind.ind_pnl_get_by_id(self)

    def tests_ind_pnl_5_delete(self):
        if self.check_scenary(["ALL", "IND", "ind_pnl_delete"], self.tests_scenary):
            module_tests_ind.ind_pnl_delete(self)
            
    def tests_ind_legenda_2_id2(self):
        if self.check_scenary(["ALL", "IND", "ind_legenda_id2"], self.tests_scenary):
            module_tests_ind.ind_legenda_id2(self)

    def tests_ind_legenda_1_id1(self):
        if self.check_scenary(["ALL", "IND", "ind_legenda_id1"], self.tests_scenary):
            module_tests_ind.ind_legenda_id1(self)

    def tests_ind_legenda_3_get(self):
        if self.check_scenary(["ALL", "IND", "ind_legenda_get"], self.tests_scenary):
            module_tests_ind.ind_legenda_get(self)

    def tests_ind_legenda_4_get_by_id(self):
        if self.check_scenary(["ALL", "IND", "ind_legenda_get_by_id"], self.tests_scenary):
            module_tests_ind.ind_legenda_get_by_id(self)

    def tests_ind_legenda_5_delete(self):
        if self.check_scenary(["ALL", "IND", "ind_legenda_delete"], self.tests_scenary):
            module_tests_ind.ind_legenda_delete(self)            

    def tests_ind_2_id2(self):
        if self.check_scenary(["ALL", "IND", "ind_indic_id2"], self.tests_scenary):
            module_tests_ind.ind_indic_id2(self)

    def tests_ind_1_id1(self):
        if self.check_scenary(["ALL", "IND", "ind_indic_id1"], self.tests_scenary):
            module_tests_ind.ind_indic_id1(self)

    def tests_ind_grupo_2_id2(self):
        if self.check_scenary(["ALL", "IND", "ind_grupo_id2"], self.tests_scenary):
            module_tests_ind.ind_grupo_id2(self)

    def tests_ind_grupo_1_id1(self):
        if self.check_scenary(["ALL", "IND", "ind_grupo_id1"], self.tests_scenary):
            module_tests_ind.ind_grupo_id1(self)

    def tests_ind_grupo_3_get(self):
        if self.check_scenary(["ALL", "IND", "ind_grupo_get"], self.tests_scenary):
            module_tests_ind.ind_grupo_get(self)

    def tests_ind_grupo_4_get_by_id(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_grupo_get_by_id"], self.tests_scenary
        ):
            module_tests_ind.ind_grupo_get_by_id(self)

    def tests_ind_grupo_5_delete(self):
        if self.check_scenary(["ALL", "IND", "ind_grupo_delete"], self.tests_scenary):
            module_tests_ind.ind_grupo_delete(self)

    def tests_ind_3_get(self):
        if self.check_scenary(["ALL", "IND", "ind_indic_get"], self.tests_scenary):
            module_tests_ind.ind_indic_get(self)

    def tests_ind_4_get_by_id(self):
        if self.check_scenary(
            ["ALL", "IND", "ind_indic_get_by_id"], self.tests_scenary
        ):
            module_tests_ind.ind_indic_get_by_id(self)

    def tests_ind_ftd_2_id2(self):
        if self.check_scenary(["ALL", "IND", "ind_ftd_id2"], self.tests_scenary):
            module_tests_ind.ind_ftd_id2(self)

    def tests_ind_ftd_1_id1(self):
        if self.check_scenary(["ALL", "IND", "ind_ftd_id1"], self.tests_scenary):
            module_tests_ind.ind_ftd_id1(self)

    def tests_ind_ftd_3_get(self):
        if self.check_scenary(["ALL", "IND", "ind_ftd_get"], self.tests_scenary):
            module_tests_ind.ind_ftd_get(self)

    def tests_ind_ftd_4_get_by_id(self):
        if self.check_scenary(["ALL", "IND", "ind_ftd_get_by_id"], self.tests_scenary):
            module_tests_ind.ind_ftd_get_by_id(self)

    def tests_ind_ftd_5_delete(self):
        if self.check_scenary(["ALL", "IND", "ind_ftd_delete"], self.tests_scenary):
            module_tests_ind.ind_ftd_delete(self)

    def tests_ind_5_delete(self):
        if self.check_scenary(["ALL", "IND", "ind_indic_delete"], self.tests_scenary):
            module_tests_ind.ind_indic_delete(self)

    def tests_ind_cnd_2_id2(self):
        if self.check_scenary(["ALL", "IND", "ind_cnd_id2"], self.tests_scenary):
            module_tests_ind.ind_cnd_id2(self)

    def tests_ind_cnd_1_id1(self):
        if self.check_scenary(["ALL", "IND", "ind_cnd_id1"], self.tests_scenary):
            module_tests_ind.ind_cnd_id1(self)

    def tests_ind_cnd_3_get(self):
        if self.check_scenary(["ALL", "IND", "ind_cnd_get"], self.tests_scenary):
            module_tests_ind.ind_cnd_get(self)

    def tests_ind_cnd_4_get_by_id(self):
        if self.check_scenary(["ALL", "IND", "ind_cnd_get_by_id"], self.tests_scenary):
            module_tests_ind.ind_cnd_get_by_id(self)

    def tests_ind_cnd_5_delete(self):
        if self.check_scenary(["ALL", "IND", "ind_cnd_delete"], self.tests_scenary):
            module_tests_ind.ind_cnd_delete(self)

    def tests_ind_cjd_2_id2(self):
        if self.check_scenary(["ALL", "IND", "ind_cjd_id2"], self.tests_scenary):
            module_tests_ind.ind_cjd_id2(self)

    def tests_ind_cjd_1_id1(self):
        if self.check_scenary(["ALL", "IND", "ind_cjd_id1"], self.tests_scenary):
            module_tests_ind.ind_cjd_id1(self)

    def tests_ind_cjd_3_get(self):
        if self.check_scenary(["ALL", "IND", "ind_cjd_get"], self.tests_scenary):
            module_tests_ind.ind_cjd_get(self)

    def tests_ind_cjd_4_get_by_id(self):
        if self.check_scenary(["ALL", "IND", "ind_cjd_get_by_id"], self.tests_scenary):
            module_tests_ind.ind_cjd_get_by_id(self)

    def tests_ind_cjd_5_delete(self):
        if self.check_scenary(["ALL", "IND", "ind_cjd_delete"], self.tests_scenary):
            module_tests_ind.ind_cjd_delete(self)
