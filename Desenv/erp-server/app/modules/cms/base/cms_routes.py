def configure_cms(app):
    # ======
    from app.modules.cms.cms_grupo_resource import routes_cms_grupo

    app.register_blueprint(routes_cms_grupo)
    # ======
    from app.modules.cms.cms_post_resource import routes_cms_post

    app.register_blueprint(routes_cms_post)
    # ======
    from app.modules.cms.cms_post_hist_resource import routes_cms_post_hist

    app.register_blueprint(routes_cms_post_hist)
    # ======
    from app.modules.cms.cms_tag_resource import routes_cms_tag

    app.register_blueprint(routes_cms_tag)
