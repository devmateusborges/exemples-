

def configure_auth(app):
    # ======
    from app.securities.auth_resource import routes_auth
    app.register_blueprint(routes_auth)
   