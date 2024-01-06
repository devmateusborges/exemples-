

def configure_mob(app):
    # ======
    from app.modules.mob.mob_unit_param_resource import routes_mob_unit_param
    app.register_blueprint(routes_mob_unit_param)
    # ======
    
   