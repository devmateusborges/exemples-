def configure_sys(app):
    # ======
    from app.modules.sys.sys_document_category_resource import (
        routes_sys_document_category,
    )

    app.register_blueprint(routes_sys_document_category)
    # ======
    from app.modules.sys.sys_document_group_resource import routes_sys_document_group

    app.register_blueprint(routes_sys_document_group)
    # ======
    from app.modules.sys.sys_group_resource import routes_sys_group

    app.register_blueprint(routes_sys_group)
    # ======
    from app.modules.sys.sys_document_resource import routes_sys_document

    app.register_blueprint(routes_sys_document)
    # ======
    from app.modules.sys.sys_restriction_resource import routes_sys_restriction

    app.register_blueprint(routes_sys_restriction)
    # ======
    from app.modules.sys.sys_resource import routes_sys

    app.register_blueprint(routes_sys)
    # ======
    from app.modules.sys.sys_module_resource import routes_sys_module

    app.register_blueprint(routes_sys_module)
    # ======
    from app.modules.sys.sys_licence_resource import routes_sys_licence

    app.register_blueprint(routes_sys_licence)
    # ======
    from app.modules.sys.sys_plan_resource import routes_sys_plan

    app.register_blueprint(routes_sys_plan)
    # ======
    from app.modules.sys.sys_program_resource import routes_sys_program

    app.register_blueprint(routes_sys_program)
    # ======
    from app.modules.sys.sys_document_user_resource import routes_sys_document_user

    app.register_blueprint(routes_sys_document_user)
    # ======
    from app.modules.sys.sys_unit_resource import routes_sys_unit

    app.register_blueprint(routes_sys_unit)
    # ======
    from app.modules.sys.sys_user_resource import routes_sys_user

    app.register_blueprint(routes_sys_user)
    # ======
    from app.modules.sys.sys_program_favorite_resource import (
        routes_sys_program_favorite,
    )

    app.register_blueprint(routes_sys_program_favorite)
    # ======

    from app.modules.sys.sys_email_log_resource import routes_sys_email_log

    app.register_blueprint(routes_sys_email_log)
    # ======
    from app.modules.sys.sys_notification_log_resource import (
        routes_sys_notification_log,
    )

    app.register_blueprint(routes_sys_notification_log)
    # ======
    from app.modules.sys.sys_notification_token_resource import (
        routes_sys_notification_token,
    )

    app.register_blueprint(routes_sys_notification_token)
    # ======
    from app.modules.sys.sys_token_resource import routes_sys_token

    app.register_blueprint(routes_sys_token)
    # ======
    from app.modules.sys.sys_type_description_resource import (
        routes_sys_type_description,
    )

    app.register_blueprint(routes_sys_type_description)

    # ======
    from app.modules.sys.sys_process_log_resource import routes_sys_process_log

    app.register_blueprint(routes_sys_process_log)
    # ======
    from app.modules.sys.sys_user_unit_resource import routes_sys_user_unit_resource

    app.register_blueprint(routes_sys_user_unit_resource)
    # ======
    from app.modules.sys.sys_user_ind_pnl_resource import routes_sys_user_ind_pnl

    app.register_blueprint(routes_sys_user_ind_pnl)
    # ======
    from app.modules.sys.sys_access_log_resource import routes_sys_access_log

    app.register_blueprint(routes_sys_access_log)
    # ======
    from app.modules.sys.sys_user_preference_resource import routes_sys_user_preference

    app.register_blueprint(routes_sys_user_preference)
    # ======
    from app.modules.sys.sys_param_resource import routes_sys_param

    app.register_blueprint(routes_sys_param)
    # ======
    from app.modules.sys.sys_unit_param_resource import routes_sys_unit_param

    app.register_blueprint(routes_sys_unit_param)
    # ======
    from app.modules.sys.sys_user_chat_grupo_resource import routes_sys_user_chat_grupo

    app.register_blueprint(routes_sys_user_chat_grupo)
    # ======
    from app.modules.sys.sys_migration_resource import routes_sys_migration

    app.register_blueprint(routes_sys_migration)
    # ======
    from app.modules.sys.sys_user_cms_grupo_resource import routes_sys_user_cms_grupo

    app.register_blueprint(routes_sys_user_cms_grupo)
    # ======
    from app.modules.sys.sys_user_group_resource import routes_sys_user_group

    app.register_blueprint(routes_sys_user_group)
    # ======
    from app.modules.sys.sys_user_program_resource import routes_sys_user_program

    app.register_blueprint(routes_sys_user_program)
    # ======
    from app.modules.sys.sys_translate_lang_resource import routes_sys_translate_lang

    app.register_blueprint(routes_sys_translate_lang)
    # ======
    from app.modules.sys.sys_translate_resource import routes_sys_translate

    app.register_blueprint(routes_sys_translate)
    # ======
    from app.modules.sys.sys_action_resource import routes_sys_action

    app.register_blueprint(routes_sys_action)
    # ======
    from app.modules.sys.sys_program_action_resource import routes_sys_program_action

    app.register_blueprint(routes_sys_program_action)
    # ======
    from app.modules.sys.sys_group_program_action_resource import (
        routes_sys_group_program_action,
    )

    app.register_blueprint(routes_sys_group_program_action)
    # ======
    from app.modules.sys.sys_user_program_action_resource import (
        routes_sys_user_program_action,
    )

    app.register_blueprint(routes_sys_user_program_action)
    # ======
    from app.modules.sys.sys_dic_resource import (
        routes_sys_dic,
    )

    app.register_blueprint(routes_sys_dic)
    # ======
    from app.modules.sys.sys_unit_manager_resource import (
        routes_sys_unit_manager,
    )

    app.register_blueprint(routes_sys_unit_manager)
