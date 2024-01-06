# ==========================================================
SQL_SYS_UNIT_BY_USER_LOGIN = """SELECT sys_unit.id, sys_unit.name, sys_unit.code_unit, sys_unit.active 
                                   FROM sys_unit, sys_user, sys_user_unit
                                  WHERE sys_unit.id = sys_user_unit.sys_unit_id 
                                    AND sys_user_unit.sys_user_id = sys_user.id 
                                    AND sys_user.login = '{pvuserlogin}'
                                    AND sys_unit.name ilike '%{name}%' 
                                    AND sys_unit.id ilike '{id}'
                                    order by sys_unit.name
                                    [paginate]
                                    """
SQL_SYS_UNIT_BY_USER_LOGIN_FIELD = ["id", "name", "code_unit", "active"]
# ==========================================================
# TODO sys_id precisa mudar
SQL_SYS_PROGRAM_BY_USER_LOGIN = """SELECT           t1.sys_program_id,
                                                    t1.sys_program_name,
                                                    t1.sys_program_code_program,
                                                    t1.sys_program_code_program_desc,
                                                    t1.sys_program_controller,
                                                    t1.sys_program_type_program,
                                                    t1.sys_program_icon,
                                                    t1.sys_module_id,
                                                    t1.sys_module_name,
                                                    t1.sys_module_icon,
                                                    t1.sys_module_code_module,
                                                    t1.sys_module_code_module_desc,
                                                    t1.sys_module_color,
                                                    t1.sys_module_order_visual,
                                                    t1.sys_program_is_favorite
                                                FROM fnsys_program_acesso('e8329d00-443f-4c03-8e73-c161f0d4f37d','{pvuserlogin}','{pvsysprogramadmin}','{pvsysprogrammenu}','{pvsysprogramfavorite}','{pvsysprogramid}') t1"""
SQL_SYS_PROGRAM_BY_USER_LOGIN_FIELD = [
    "sys_program_id",
    "sys_program_name",
    "sys_program_code_program",
    "sys_program_code_program_desc",
    "sys_program_controller",
    "sys_program_type_program",
    "sys_program_icon",
    "sys_module_id",
    "sys_module_name",
    "sys_module_icon",
    "sys_module_code_module",
    "sys_module_code_module_desc",
    "sys_module_color",
    "sys_module_order_visual",
    "sys_program_is_favorite",
]

# ==========================================================
SQL_SYS_MODULE_BY_USER_LOGIN = """SELECT distinct
                                        t1.sys_module_id,
                                        t1.sys_module_name,
                                        t1.sys_module_icon,
                                        t1.sys_module_code_module,
                                        t1.sys_module_code_module_desc,
                                        t1.sys_module_color,
                                        t1.sys_module_order_visual
                                    FROM fnsys_program_acesso('e8329d00-443f-4c03-8e73-c161f0d4f37d','{pvuserlogin}','{pvsysprogramadmin}','{pvsysprogrammenu}','{pvsysprogramfavorite}','{pvsysprogramid}') t1"""
SQL_SYS_MODULE_BY_USER_LOGIN_FIELD = [
    "sys_module_id",
    "sys_module_name",
    "sys_module_icon",
    "sys_module_code_module",
    "sys_module_code_module_desc",
    "sys_module_color",
    "sys_module_order_visual",
]
# ==========================================================

SQL_SYS_PROGRAM_ACTION_ACESSO = """SELECT distinct
                                         t1.sys_action_id,
                                         t1.sys_action_name,
                                         t1.sys_action_code,
                                         t1.sys_program_id,
                                         t1.sys_program_name,
                                         t1.sys_program_controller
                                    FROM fnsys_program_action_acesso('e8329d00-443f-4c03-8e73-c161f0d4f37d', '{pvuserlogin}', '{pvsysprogramid}') t1"""
SQL_SYS_PROGRAM_ACTION_ACESSO_FIELD = [
    "sys_action_id",
    "sys_action_name",
    "sys_action_code",
    "sys_program_id",
    "sys_program_name",
    "sys_program_controller",
]
