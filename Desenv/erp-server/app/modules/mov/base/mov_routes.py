def configure_mov(app):
    # ======
    from app.modules.mov.mov_tipo_resource import routes_mov_tipo
    app.register_blueprint(routes_mov_tipo)
    # ======
    from app.modules.mov.mov_status_resource import routes_mov_status
    app.register_blueprint(routes_mov_status)
    # ======
    from app.modules.mov.mov_unit_param_resource import routes_mov_unit_param
    app.register_blueprint(routes_mov_unit_param)
    # ======
    from app.modules.mov.mov_operacao_resource import routes_mov_operacao
    app.register_blueprint(routes_mov_operacao)
    # ======
    from app.modules.mov.mov_resource import routes_mov
    app.register_blueprint(routes_mov)
    # ======
    from app.modules.mov.mov_est_nivel_resource import routes_mov_est_nivel
    app.register_blueprint(routes_mov_est_nivel)
    # ======
    from app.modules.mov.mov_ciot_resource import routes_mov_ciot
    app.register_blueprint(routes_mov_ciot)
    # ======
    from app.modules.mov.mov_comp_resource import routes_mov_comp
    app.register_blueprint(routes_mov_comp)
    # ======
    from app.modules.mov.mov_condutor_resource import routes_mov_condutor
    app.register_blueprint(routes_mov_condutor)
    # ======
    from app.modules.mov.mov_entrega_resource import routes_mov_entrega
    app.register_blueprint(routes_mov_entrega)
    # ======
    from app.modules.mov.mov_cotacao_resource import routes_mov_cotacao
    app.register_blueprint(routes_mov_cotacao)
    # ======
    from app.modules.mov.mov_itemserv_resource import routes_mov_itemserv
    app.register_blueprint(routes_mov_itemserv)
    # ======
    from app.modules.mov.mov_lacre_resource import routes_mov_lacre
    app.register_blueprint(routes_mov_lacre)
    # ======
    from app.modules.mov.mov_medida_resource import routes_mov_medida
    app.register_blueprint(routes_mov_medida)
    # ======
    from app.modules.mov.mov_pedagio_resource import routes_mov_pedagio
    app.register_blueprint(routes_mov_pedagio)
    # ======
    from app.modules.mov.mov_percurso_resource import routes_mov_percurso
    app.register_blueprint(routes_mov_percurso)
    # ======
    from app.modules.mov.mov_seguradora_resource import routes_mov_seguradora
    app.register_blueprint(routes_mov_seguradora)
    # ======
    from app.modules.mov.mov_tomador_resource import routes_mov_tomador
    app.register_blueprint(routes_mov_tomador)
    # ======
    from app.modules.mov.mov_frete_resource import routes_mov_frete
    app.register_blueprint(routes_mov_frete)
    # ======
    from app.modules.mov.mov_origem_resource import routes_mov_origem
    app.register_blueprint(routes_mov_origem)
    # ======
    from app.modules.mov.mov_reboque_resource import routes_mov_reboque
    app.register_blueprint(routes_mov_reboque)
    # ======
