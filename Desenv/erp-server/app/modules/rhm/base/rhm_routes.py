

def configure_rhm(app):
    from app.modules.rhm.rhm_unit_param_resource import routes_rhm_unit_param
    app.register_blueprint(routes_rhm_unit_param)
    # ======