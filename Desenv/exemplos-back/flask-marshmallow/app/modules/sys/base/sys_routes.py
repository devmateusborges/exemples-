

def configure_sys(app):
    #======
    from app.securities.resource_auth import routes_auth
    app.register_blueprint(routes_auth)
    #======
    from app.modules.sys.sys_document_category_resource import routes_sys_document_category
    app.register_blueprint(routes_sys_document_category)
    #====== 
    from app.modules.sys.sys_document_group_resource import routes_sys_document_group
    app.register_blueprint(routes_sys_document_group)
    #====== 
    from app.modules.sys.sys_group_resource import routes_sys_group
    app.register_blueprint(routes_sys_group)
    #======
    from app.modules.sys.sys_document_resource import routes_sys_document
    app.register_blueprint(routes_sys_document)
    #======  
    from app.modules.sys.sys_group_program_resource import routes_sys_group_program
    app.register_blueprint(routes_sys_group_program)
    #======  
    from app.modules.sys.sys_restriction_resource import routes_sys_restriction
    app.register_blueprint(routes_sys_restriction)
    #======  
    from app.modules.sys.sys_resource  import routes_sys
    app.register_blueprint(routes_sys)
    #======  
    from app.modules.sys.sys_user_group_resource  import routes_sys_user_group
    app.register_blueprint(routes_sys_user_group)
    #======  
    from app.modules.sys.sys_module_resource  import routes_sys_module
    app.register_blueprint(routes_sys_module)
    #======  
    from app.modules.sys.sys_licence_resource  import routes_sys_licence
    app.register_blueprint(routes_sys_licence)
    #====== 
    from app.modules.sys.sys_plan_resource import routes_sys_plan
    app.register_blueprint(routes_sys_plan)
    #====== 
    from app.modules.sys.sys_restriction_licence_resource import routes_sys_restriction_licence
    app.register_blueprint(routes_sys_restriction_licence)
    #====== 
    from app.modules.sys.sys_plan_restriction_resource import routes_sys_plan_restriction
    app.register_blueprint(routes_sys_plan_restriction)
    #====== 
    from app.modules.sys.sys_program_resource import routes_sys_program
    app.register_blueprint(routes_sys_program)
    #====== 
    from app.modules.sys.sys_document_user_resource import routes_sys_document_user
    app.register_blueprint(routes_sys_document_user)
    #====== 
    from app.modules.sys.sys_unit_resource import routes_sys_unit
    app.register_blueprint(routes_sys_unit)
    #====== 
    from app.modules.sys.sys_user_resource import routes_sys_user
    app.register_blueprint(routes_sys_user)
    #======
    from app.modules.sys.sys_group_program_feature_resource import routes_sys_group_program_feature
    app.register_blueprint(routes_sys_group_program_feature)
    #======
    from app.modules.sys.sys_licence_device_resource import routes_sys_licence_device
    app.register_blueprint(routes_sys_licence_device)
    #======
    from app.modules.sys.sys_program_favorite_resource import routes_sys_program_favorite
    app.register_blueprint(routes_sys_program_favorite)
    #======
    from app.modules.sys.sys_user_program_feature_resource import routes_sys_user_program_feature
    app.register_blueprint(routes_sys_user_program_feature)
    #======
    from app.modules.sys.sys_change_log_resource import routes_sys_change_log
    app.register_blueprint(routes_sys_change_log)
    #======
    from app.modules.sys.sys_email_log_resource import routes_sys_email_log
    app.register_blueprint(routes_sys_email_log)
    #======
    from app.modules.sys.sys_notification_log_resource import routes_sys_notification_log
    app.register_blueprint(routes_sys_notification_log)
    #======
    from app.modules.sys.sys_token_resource import routes_sys_token
    app.register_blueprint(routes_sys_token)
    #======
    from app.modules.sys.sys_type_description_resource import routes_sys_type_description
    app.register_blueprint(routes_sys_type_description)
    #======
    from app.modules.sys.sys_program_feature_resource import routes_sys_program_feature
    app.register_blueprint(routes_sys_program_feature)
    #======
    