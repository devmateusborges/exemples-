def configure_bor(app):
    # ======
    from app.modules.bor.bor_dispositivo_resource import routes_bor_dispositivo

    app.register_blueprint(routes_bor_dispositivo)
    # ======
    from app.modules.bor.bor_unit_param_resource import routes_bor_unit_param

    app.register_blueprint(routes_bor_unit_param)
