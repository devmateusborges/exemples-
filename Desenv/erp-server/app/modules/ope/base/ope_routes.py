

def configure_ope(app):
    # ======
    from app.modules.ope.ope_centro_tipo_resource import routes_ope_centro_tipo
    app.register_blueprint(routes_ope_centro_tipo)
    # ======
    from app.modules.ope.ope_atividade_grupo_resource import routes_ope_atividade_grupo
    app.register_blueprint(routes_ope_atividade_grupo)
    # ======
    from app.modules.ope.ope_atividade_sistema_resource import routes_ope_atividade_sistema
    app.register_blueprint(routes_ope_atividade_sistema)
    # ======
    from app.modules.ope.ope_centro2_ord_status_resource import routes_ope_centro2_ord_status
    app.register_blueprint(routes_ope_centro2_ord_status)
    # ======
    from app.modules.ope.ope_centro2_ord_tipo_resource import routes_ope_centro2_ord_tipo
    app.register_blueprint(routes_ope_centro2_ord_tipo)
    # ======
    from app.modules.ope.ope_centro_subtipo_resource import routes_ope_centro_subtipo
    app.register_blueprint(routes_ope_centro_subtipo)
    # ======
    from app.modules.ope.ope_centro_versao_resource import routes_ope_centro_versao
    app.register_blueprint(routes_ope_centro_versao)
    # ======
    from app.modules.ope.ope_ciclo_var_resource import routes_ope_ciclo_var
    app.register_blueprint(routes_ope_ciclo_var)
    # ======
    from app.modules.ope.ope_compart_grupo_resource import routes_ope_compart_grupo
    app.register_blueprint(routes_ope_compart_grupo)
    # ======
    from app.modules.ope.ope_compart_posicao_resource import routes_ope_compart_posicao
    app.register_blueprint(routes_ope_compart_posicao)
    # ======
    from app.modules.ope.ope_compart_status_resource import routes_ope_compart_status
    app.register_blueprint(routes_ope_compart_status)
    # ======
    from app.modules.ope.ope_compart_medida_resource import routes_ope_compart_medida
    app.register_blueprint(routes_ope_compart_medida)
    # ======
    from app.modules.ope.ope_espac_resource import routes_ope_espac
    app.register_blueprint(routes_ope_espac)
    # ======
    from app.modules.ope.ope_estagio_resource import routes_ope_estagio
    app.register_blueprint(routes_ope_estagio)
    # ======
    from app.modules.ope.ope_ocor_grupo_resource import routes_ope_ocor_grupo
    app.register_blueprint(routes_ope_ocor_grupo)
    # ======
    from app.modules.ope.ope_ocor_tipo_resource import routes_ope_ocor_tipo
    app.register_blueprint(routes_ope_ocor_tipo)
    # ======
    from app.modules.ope.ope_ocor_status_resource import routes_ope_ocor_status
    app.register_blueprint(routes_ope_ocor_status)
    # ======
    from app.modules.ope.ope_periodo_resource import routes_ope_periodo
    app.register_blueprint(routes_ope_periodo)
    # ======
    from app.modules.ope.ope_regiao_resource import routes_ope_regiao
    app.register_blueprint(routes_ope_regiao)
    # ======
    from app.modules.ope.ope_tipo_solo_resource import routes_ope_tipo_solo
    app.register_blueprint(routes_ope_tipo_solo)
    # ======
    from app.modules.ope.ope_unit_param_resource import routes_ope_unit_param
    app.register_blueprint(routes_ope_unit_param)
    # ======
    from app.modules.ope.ope_atividade_resource import routes_ope_atividade
    app.register_blueprint(routes_ope_atividade)
    # ======
    from app.modules.ope.ope_centro_grupo_resource import routes_ope_centro_grupo
    app.register_blueprint(routes_ope_centro_grupo)
    # ======
    from app.modules.ope.ope_centro_rat_tipo_resource import routes_ope_centro_rat_tipo
    app.register_blueprint(routes_ope_centro_rat_tipo)
    # ======
    from app.modules.ope.ope_compart_ocor_resource import routes_ope_compart_ocor
    app.register_blueprint(routes_ope_compart_ocor)
    # ======
    from app.modules.ope.ope_compart_subgrupo_resource import routes_ope_compart_subgrupo
    app.register_blueprint(routes_ope_compart_subgrupo)
    # ======
    from app.modules.ope.ope_compart_tipo_resource import routes_ope_compart_tipo
    app.register_blueprint(routes_ope_compart_tipo)
    # ======
    from app.modules.ope.ope_ocor_resource import routes_ope_ocor
    app.register_blueprint(routes_ope_ocor)
    # ======
    from app.modules.ope.ope_centro1_resource import routes_ope_centro1
    app.register_blueprint(routes_ope_centro1)
    # ======
    from app.modules.ope.ope_centro_subgrupo_resource import routes_ope_centro_subgrupo
    app.register_blueprint(routes_ope_centro_subgrupo)
    # ======
    from app.modules.ope.ope_compart_resource import routes_ope_compart
    app.register_blueprint(routes_ope_compart)
    # ======
    from app.modules.ope.ope_centro2_resource import routes_ope_centro2
    app.register_blueprint(routes_ope_centro2)
    # ======
    from app.modules.ope.ope_compart_itemserv_resource import routes_ope_compart_itemserv
    app.register_blueprint(routes_ope_compart_itemserv)
    # ======
    from app.modules.ope.ope_frente_trabalho_resource import routes_ope_frente_trabalho
    app.register_blueprint(routes_ope_frente_trabalho)
    # ======
    from app.modules.ope.ope_ocor_compart_mov_resource import routes_ope_ocor_compart_mov
    app.register_blueprint(routes_ope_ocor_compart_mov)
    # ======
    from app.modules.ope.ope_ocor_mov_resource import routes_ope_ocor_mov
    app.register_blueprint(routes_ope_ocor_mov)
    # ======
    from app.modules.ope.ope_centro2_area_resource import routes_ope_centro2_area
    app.register_blueprint(routes_ope_centro2_area)
    # ======
    from app.modules.ope.ope_centro_config_resource import routes_ope_centro_config
    app.register_blueprint(routes_ope_centro_config)
    # ======
    from app.modules.ope.ope_centro2_equip_resource import routes_ope_centro2_equip
    app.register_blueprint(routes_ope_centro2_equip)
    # ======
    from app.modules.ope.ope_centro2_estoque_resource import routes_ope_centro2_estoque
    app.register_blueprint(routes_ope_centro2_estoque)
    # ======
    from app.modules.ope.ope_centro2_mov_media_resource import routes_ope_centro2_mov_media
    app.register_blueprint(routes_ope_centro2_mov_media)
    # ======
    from app.modules.ope.ope_centro2_param_per_resource import routes_ope_centro2_param_per
    app.register_blueprint(routes_ope_centro2_param_per)
    # ======
    from app.modules.ope.ope_centro2_pessoa_resource import routes_ope_centro2_pessoa
    app.register_blueprint(routes_ope_centro2_pessoa)
    # ======
    from app.modules.ope.ope_centro_prev_resource import routes_ope_centro_prev
    app.register_blueprint(routes_ope_centro_prev)
    # ======
    from app.modules.ope.ope_centro_rend_resource import routes_ope_centro_rend
    app.register_blueprint(routes_ope_centro_rend)
    # ======
    from app.modules.ope.ope_ocor_prev_resource import routes_ope_ocor_prev
    app.register_blueprint(routes_ope_ocor_prev)
    # ======
    from app.modules.ope.ope_centro2_mapa_geometria_resource import routes_ope_centro2_mapa_geometria
    app.register_blueprint(routes_ope_centro2_mapa_geometria)
    # ======
    from app.modules.ope.ope_centro2_ord_resource import routes_ope_centro2_ord
    app.register_blueprint(routes_ope_centro2_ord)
    # ======
    from app.modules.ope.ope_centro_dest_resource import routes_ope_centro_dest
    app.register_blueprint(routes_ope_centro_dest)
    # ======
    from app.modules.ope.ope_centro2_ord_itemserv_resource import routes_ope_centro2_ord_itemserv
    app.register_blueprint(routes_ope_centro2_ord_itemserv)
    # ======
    from app.modules.ope.ope_centro2_ord_rec_resource import routes_ope_centro2_ord_rec
    app.register_blueprint(routes_ope_centro2_ord_rec)




    

    

    
   