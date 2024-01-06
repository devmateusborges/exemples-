

def configure_ctb(app):
    # ======
    from app.modules.ctb.ctb_versao_resource import routes_ctb_versao
    app.register_blueprint(routes_ctb_versao)
    # ======
    from app.modules.ctb.ctb_centro_grupo_resource import routes_ctb_centro_grupo
    app.register_blueprint(routes_ctb_centro_grupo)
    # ======
    from app.modules.ctb.ctb_comp_grupo_resource import routes_ctb_comp_grupo
    app.register_blueprint(routes_ctb_comp_grupo)
    # ======
    from app.modules.ctb.ctb_conta_versao_resource import routes_ctb_conta_versao
    app.register_blueprint(routes_ctb_conta_versao)
    # ======
    from app.modules.ctb.ctb_historico_resource import routes_ctb_historico
    app.register_blueprint(routes_ctb_historico)
    # ======
    from app.modules.ctb.ctb_lote_resource import routes_ctb_lote
    app.register_blueprint(routes_ctb_lote)
    # ======
    from app.modules.ctb.ctb_tipo_saldo_resource import routes_ctb_tipo_saldo
    app.register_blueprint(routes_ctb_tipo_saldo)
    # ======
    from app.modules.ctb.ctb_unit_param_resource import routes_ctb_unit_param
    app.register_blueprint(routes_ctb_unit_param)
    # ======
    from app.modules.ctb.ctb_centro_resource import routes_ctb_centro
    app.register_blueprint(routes_ctb_centro)
    # ======
    from app.modules.ctb.ctb_comp_resource import routes_ctb_comp
    app.register_blueprint(routes_ctb_comp)
    # ======
    from app.modules.ctb.ctb_conta_grupo_resource import routes_ctb_conta_grupo
    app.register_blueprint(routes_ctb_conta_grupo)
    # ======
    from app.modules.ctb.ctb_conta_resource import routes_ctb_conta
    app.register_blueprint(routes_ctb_conta)
    # ======
    from app.modules.ctb.ctb_lanc_resource import routes_ctb_lanc
    app.register_blueprint(routes_ctb_lanc)
    # ======
    from app.modules.ctb.ctb_lanc_det_resource import routes_ctb_lanc_det
    app.register_blueprint(routes_ctb_lanc_det)

     