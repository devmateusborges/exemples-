

def configure_pto(app):
    # ======
    from app.modules.pto.pto_marcacao_resource import routes_pto_marcacao
    app.register_blueprint(routes_pto_marcacao)
    # ======
    from app.modules.pto.pto_medidor_resource import routes_pto_medidor
    app.register_blueprint(routes_pto_medidor)
    # ======
    from app.modules.pto.pto_unit_param_resource import routes_pto_unit_param
    app.register_blueprint(routes_pto_unit_param)
    # ======