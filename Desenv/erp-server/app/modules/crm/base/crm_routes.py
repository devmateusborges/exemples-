def configure_crm(app):
    # ======
    from app.modules.crm.crm_aviso_resource import routes_crm_aviso

    app.register_blueprint(routes_crm_aviso)
    # ======
    from app.modules.crm.crm_chat_grupo_resource import routes_crm_chat_grupo

    app.register_blueprint(routes_crm_chat_grupo)
    # ======
    from app.modules.crm.crm_class_grupo_resource import routes_crm_class_grupo

    app.register_blueprint(routes_crm_class_grupo)
    # ======
    from app.modules.crm.crm_etapa_resource import routes_crm_etapa

    app.register_blueprint(routes_crm_etapa)
    # ======
    from app.modules.crm.crm_org_resource import routes_crm_org

    app.register_blueprint(routes_crm_org)
    # ======
    from app.modules.crm.crm_prioridade_resource import routes_crm_prioridade

    app.register_blueprint(routes_crm_prioridade)
    # ======
    from app.modules.crm.crm_resposta_resource import routes_crm_resposta

    app.register_blueprint(routes_crm_resposta)
    # ======
    from app.modules.crm.crm_status_resource import routes_crm_status

    app.register_blueprint(routes_crm_status)
    # ======
    from app.modules.crm.crm_tag_resource import routes_crm_tag

    app.register_blueprint(routes_crm_tag)
    # ======
    from app.modules.crm.crm_unit_param_resource import routes_crm_unit_param

    app.register_blueprint(routes_crm_unit_param)
    # ======
    from app.modules.crm.crm_aviso_org_resource import routes_crm_aviso_org

    app.register_blueprint(routes_crm_aviso_org)
    # ======
    from app.modules.crm.crm_chat_msg_resource import routes_crm_chat_msg

    app.register_blueprint(routes_crm_chat_msg)
    # ======
    from app.modules.crm.crm_etapa_prox_resource import routes_crm_etapa_prox

    app.register_blueprint(routes_crm_etapa_prox)
    # ======
    from app.modules.crm.crm_mov_resource import routes_crm_mov

    app.register_blueprint(routes_crm_mov)
    # ======
    from app.modules.crm.crm_class_resource import routes_crm_class

    app.register_blueprint(routes_crm_class)
    # ======
    from app.modules.crm.crm_mov_hist_resource import routes_crm_mov_hist

    app.register_blueprint(routes_crm_mov_hist)
    # ======
    from app.modules.crm.crm_mov_tag_resource import routes_crm_mov_tag

    app.register_blueprint(routes_crm_mov_tag)
    # ======
    from app.modules.crm.crm_class_subgrupo_resource import routes_crm_class_subgrupo

    app.register_blueprint(routes_crm_class_subgrupo)
