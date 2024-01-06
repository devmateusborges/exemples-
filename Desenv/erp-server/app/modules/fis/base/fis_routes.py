

def configure_fis(app):
    # ======
    from app.modules.fis.fis_cest_resource import routes_fis_cest
    app.register_blueprint(routes_fis_cest)
    # ======
    from app.modules.fis.fis_cfop_resource import routes_fis_cfop
    app.register_blueprint(routes_fis_cfop)
    # ======
    from app.modules.fis.fis_doc_tipo_resource import routes_fis_doc_tipo
    app.register_blueprint(routes_fis_doc_tipo)
    # ======
    from app.modules.fis.fis_nbs_resource import routes_fis_nbs
    app.register_blueprint(routes_fis_nbs)
    # ======
    from app.modules.fis.fis_ncm_resource import routes_fis_ncm
    app.register_blueprint(routes_fis_ncm)
    # ======
    from app.modules.fis.fis_certificado_resource import routes_fis_certificado
    app.register_blueprint(routes_fis_certificado)
    # ======
    from app.modules.fis.fis_obs_resource import routes_fis_obs
    app.register_blueprint(routes_fis_obs)
    # ======
    from app.modules.fis.fis_unit_param_resource import routes_fis_unit_param
    app.register_blueprint(routes_fis_unit_param)
    # ======
    from app.modules.fis.fis_ibpt_resource import routes_fis_ibpt
    app.register_blueprint(routes_fis_ibpt)
    # ======
    from app.modules.fis.fis_doc_resource import routes_fis_doc
    app.register_blueprint(routes_fis_doc)
    # ======
    from app.modules.fis.fis_tributacao_resource import routes_fis_tributacao
    app.register_blueprint(routes_fis_tributacao)
    # ======
    from app.modules.fis.fis_tributo_resource import routes_fis_tributo
    app.register_blueprint(routes_fis_tributo)
    # ======