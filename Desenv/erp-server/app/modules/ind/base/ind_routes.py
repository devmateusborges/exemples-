def configure_ind(app):
    # ======
    from app.modules.ind.ind_cnd_resource import routes_ind_cnd

    app.register_blueprint(routes_ind_cnd)
    # ======
    from app.modules.ind.ind_cjd_resource import routes_ind_cjd

    app.register_blueprint(routes_ind_cjd)
    # ======
    from app.modules.ind.ind_pnl_resource import routes_ind_pnl

    app.register_blueprint(routes_ind_pnl)
    # ======
    from app.modules.ind.ind_legenda_resource import routes_ind_legenda

    app.register_blueprint(routes_ind_legenda)
    # ======
    from app.modules.ind.ind_prm_resource import routes_ind_prm

    app.register_blueprint(routes_ind_prm)
    # ======
    from app.modules.ind.ind_indic_resource import routes_ind_indic

    app.register_blueprint(routes_ind_indic)
    # ======
    from app.modules.ind.ind_ftd_resource import routes_ind_ftd

    app.register_blueprint(routes_ind_ftd)
    # ======
    from app.modules.ind.ind_grupo_resource import routes_ind_grupo

    app.register_blueprint(routes_ind_grupo)
    # ======
    from app.modules.ind.ind_subgrupo_resource import routes_ind_subgrupo

    app.register_blueprint(routes_ind_subgrupo)
    # ======
    from app.modules.ind.ind_unit_param_resource import routes_ind_unit_param

    app.register_blueprint(routes_ind_unit_param)
    # ======
    from app.modules.ind.ind_rel_resource import routes_ind_rel

    app.register_blueprint(routes_ind_rel)
    # ======
    from app.modules.ind.ind_vr_ano_resource import routes_ind_vr_ano

    app.register_blueprint(routes_ind_vr_ano)
    # ======
    from app.modules.ind.ind_vr_bimestre_resource import routes_ind_vr_bimestre

    app.register_blueprint(routes_ind_vr_bimestre)
    # ======
    from app.modules.ind.ind_vr_dia_resource import routes_ind_vr_dia

    app.register_blueprint(routes_ind_vr_dia)
    # ======
    from app.modules.ind.ind_vr_mes_resource import routes_ind_vr_mes

    app.register_blueprint(routes_ind_vr_mes)
    # ======
    from app.modules.ind.ind_vr_quadrimestre_resource import routes_ind_vr_quadrimestre

    app.register_blueprint(routes_ind_vr_quadrimestre)
    # ======
    from app.modules.ind.ind_vr_quinzena_resource import routes_ind_vr_quinzena

    app.register_blueprint(routes_ind_vr_quinzena)
    # ======
    from app.modules.ind.ind_vr_semana_resource import routes_ind_vr_semana

    app.register_blueprint(routes_ind_vr_semana)
    # ======
    from app.modules.ind.ind_vr_semestre_resource import routes_ind_vr_semestre

    app.register_blueprint(routes_ind_vr_semestre)
    # ======
    from app.modules.ind.ind_vr_trimestre_resource import routes_ind_vr_trimestre

    app.register_blueprint(routes_ind_vr_trimestre)
    # ======
    from app.modules.ind.ind_vr_meta_resource import routes_ind_vr_meta

    app.register_blueprint(routes_ind_vr_meta)
    # ======
    from app.modules.ind.ind_dash_resource import routes_ind_dash

    app.register_blueprint(routes_ind_dash)
    # ======
