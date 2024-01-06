def configure_tst(app):
    # ======
    from app.modules.tst.test1_resource import routes_test1

    app.register_blueprint(routes_test1)

    from app.modules.tst.test1Fk_resource import routes_test1Fk

    app.register_blueprint(routes_test1Fk)
    # ======
