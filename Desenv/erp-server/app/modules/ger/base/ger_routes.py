def configure_ger(app):
    # ======
    from app.modules.ger.ger_marca_resource import routes_ger_marca

    app.register_blueprint(routes_ger_marca)
    # ======
    from app.modules.ger.ger_pais_resource import routes_ger_pais

    app.register_blueprint(routes_ger_pais)
    # ======
    from app.modules.ger.ger_umedida_resource import routes_ger_umedida

    app.register_blueprint(routes_ger_umedida)
    # ======
    from app.modules.ger.ger_cidade_resource import routes_ger_cidade

    app.register_blueprint(routes_ger_cidade)
    # ======
    from app.modules.ger.ger_itemserv_compos_tipo_resource import (
        routes_ger_itemserv_compos_tipo,
    )

    app.register_blueprint(routes_ger_itemserv_compos_tipo)
    # ======
    from app.modules.ger.ger_index_mov_resource import routes_ger_index_mov

    app.register_blueprint(routes_ger_index_mov)
    # ======
    from app.modules.ger.ger_itemserv_var_resource import routes_ger_itemserv_var

    app.register_blueprint(routes_ger_itemserv_var)
    # ======
    from app.modules.ger.ger_empresa_resource import routes_ger_empresa

    app.register_blueprint(routes_ger_empresa)
    # ======
    from app.modules.ger.ger_itemserv_resouce import routes_ger_itemserv

    app.register_blueprint(routes_ger_itemserv)
    # ======
    from app.modules.ger.ger_itemserv_grupo_resource import routes_ger_itemserv_grupo

    app.register_blueprint(routes_ger_itemserv_grupo)
    # ======
    from app.modules.ger.ger_numeracao_resource import routes_ger_numeracao

    app.register_blueprint(routes_ger_numeracao)
    # ======
    from app.modules.ger.ger_per_resource import routes_ger_per

    app.register_blueprint(routes_ger_per)
    # ======
    from app.modules.ger.ger_pessoa_resource import routes_ger_pessoa

    app.register_blueprint(routes_ger_pessoa)
    # ======
    from app.modules.ger.ger_unit_param_resource import routes_ger_unit_param

    app.register_blueprint(routes_ger_unit_param)
    # ======
    from app.modules.ger.ger_itemserv_compos_resource import routes_ger_itemserv_compos

    app.register_blueprint(routes_ger_itemserv_compos)
    # ======
    from app.modules.ger.ger_processo_bloq_resource import routes_ger_processo_bloq

    app.register_blueprint(routes_ger_processo_bloq)
    # ====
    from app.modules.ger.ger_device_resource import routes_ger_device

    app.register_blueprint(routes_ger_device)
    # ====
    from app.modules.ger.ger_index_resource import routes_ger_index

    app.register_blueprint(routes_ger_index)
    # ====
    from app.modules.ger.ger_empresa_grupo_resource import routes_ger_empresa_grupo

    app.register_blueprint(routes_ger_empresa_grupo)
    # ====
    from app.modules.ger.ger_est_nivel_resource import routes_ger_est_nivel

    app.register_blueprint(routes_ger_est_nivel)
    # ====
    from app.modules.ger.ger_per_tipo_resource import routes_ger_per_tipo

    app.register_blueprint(routes_ger_per_tipo)
    # ====
    from app.modules.ger.ger_uf_resource import routes_ger_uf

    app.register_blueprint(routes_ger_uf)
    # ====
    from app.modules.ger.ger_itemserv_subgrupo_resource import (
        routes_ger_itemserv_subgrupo,
    )

    app.register_blueprint(routes_ger_itemserv_subgrupo)
    # ====
    from app.modules.ger.ger_pessoa_endereco_resource import (
        routes_ger_pessoa_endereco,
    )

    app.register_blueprint(routes_ger_pessoa_endereco)
    # ====
