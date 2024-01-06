

def configure_fin(app):
    # ======
    from app.modules.fin.fin_recibo_resource import routes_fin_recibo
    app.register_blueprint(routes_fin_recibo)
    # ======
    from app.modules.fin.fin_banco_resource import routes_fin_banco
    app.register_blueprint(routes_fin_banco)
    # ======
    from app.modules.fin.fin_class_resource import routes_fin_class
    app.register_blueprint(routes_fin_class)
    # ======
    from app.modules.fin.fin_class_agrup_resource import routes_fin_class_agrup
    app.register_blueprint(routes_fin_class_agrup)
    # ======
    from app.modules.fin.fin_recibo_tipo_resource import routes_fin_recibo_tipo
    app.register_blueprint(routes_fin_recibo_tipo)
    # ======
    from app.modules.fin.fin_tipo_variacao_resource import routes_fin_tipo_variacao
    app.register_blueprint(routes_fin_tipo_variacao)
    # ======
    from app.modules.fin.fin_class_grupo_resource import routes_fin_class_grupo
    app.register_blueprint(routes_fin_class_grupo)
    # ======
    from app.modules.fin.fin_cond_pagrec_resource import  routes_fin_cond_pagrec
    app.register_blueprint(routes_fin_cond_pagrec)
    # ======
    from app.modules.fin.fin_unit_param_resource import routes_fin_unit_param
    app.register_blueprint(routes_fin_unit_param)
    # ======
    from app.modules.fin.fin_cond_pagrec_config_resource import routes_fin_cond_pagrec_config
    app.register_blueprint(routes_fin_cond_pagrec_config)
    # ======
    from app.modules.fin.fin_doc_tipo_resource import routes_fin_doc_tipo
    app.register_blueprint(routes_fin_doc_tipo)
    # ======
    from app.modules.fin.fin_conta_resource import routes_fin_conta
    app.register_blueprint(routes_fin_conta)
    # ======
    from app.modules.fin.fin_pagrec_tipo_resource import routes_fin_pagrec_tipo
    app.register_blueprint(routes_fin_pagrec_tipo)
    # ======
    from app.modules.fin.fin_pagrec_prev_resource import routes_fin_pagrec_prev
    app.register_blueprint(routes_fin_pagrec_prev)
    # ======
    from app.modules.fin.fin_pagrec_banco_resource import routes_fin_pagrec_banco
    app.register_blueprint(routes_fin_pagrec_banco)
    # ======
    from app.modules.fin.fin_pagrec_banco_extrato_resource import routes_fin_pagrec_banco_extrato
    app.register_blueprint(routes_fin_pagrec_banco_extrato)
    # ======
    from app.modules.fin.fin_pagrec_banco_transf_resource import routes_fin_pagrec_banco_transf
    app.register_blueprint(routes_fin_pagrec_banco_transf)
    # ======
    from app.modules.fin.fin_pagrec_baixa_resource import routes_fin_pagrec_baixa
    app.register_blueprint(routes_fin_pagrec_baixa)
    # ======
    from app.modules.fin.fin_pagrec_class_resouce import routes_fin_pagrec_class
    app.register_blueprint(routes_fin_pagrec_class)
    # ======
    from app.modules.fin.fin_pagrec_origem_resource import routes_fin_pagrec_origem
    app.register_blueprint(routes_fin_pagrec_origem)
    # ======
    from app.modules.fin.fin_lote_resource import routes_fin_lote
    app.register_blueprint(routes_fin_lote)
    # ======
    from app.modules.fin.fin_pagrec_resource import routes_fin_pagrec
    app.register_blueprint(routes_fin_pagrec)
    # ======
    from app.modules.fin.fin_pagrec_versao_resource import routes_fin_pagrec_versao
    app.register_blueprint(routes_fin_pagrec_versao)