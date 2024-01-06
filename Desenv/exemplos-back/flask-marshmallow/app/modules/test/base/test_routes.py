
def configure_test(app):
    #======
    from app.modules.test.test1_resource import routes_test1
    app.register_blueprint(routes_test1)
    #======
