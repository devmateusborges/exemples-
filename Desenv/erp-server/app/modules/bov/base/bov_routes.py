def configure_bov(app):
    # ======
    from app.modules.bov.bov_unit_param_resource import routes_bov_unit_param

    app.register_blueprint(routes_bov_unit_param)
    # ======
