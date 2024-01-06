
def configure(app):
    #======
    from ..modules.sys.base.sys_routes import configure_sys
    configure_sys(app)
    #======
    from ..modules.test.base.test_routes import configure_test
    configure_test(app)
    #======

   