# ==========================================================
SQL_IND_INDIC = """
select
igs.ind_grupo_id,
ig.nome as ind_grupo_nome,
igs.ind_subgrupo_id,
isg.nome as ind_subgrupo_nome,
id.id,
id.sigla_ind,
id.nome,
id.ger_umedida_id,
gu.nome as ger_umedida_nome,
gu.sigla_umedida as ger_umedida_sigla_umedida,
id.casas_dec,
id.campo_ordenacao,
id.metodo_ordenacao,
id.totalizador_atributo,
id.exibir_media_real,
id.exibir_media_meta,
id.exibir_dia,
id.exibir_semana,
id.exibir_quinzena,
id.exibir_mes,
id.exibir_bimestre,
id.exibir_trimestre,
id.exibir_quadrimestre,
id.exibir_semestre,
id.exibir_ano,
id.ind_indic_id_pond,
idp.sigla_ind as ind_indic_sigla_ind_pond,
idp.nome as ind_indic_nome_pond,
id.grafico_tipo_atributo,
id.grafico_valor_vazio_zero,
id.grafico_tipo_ind,
id.tipo_meta,
id.ativo,
id.exibir_dia_ant,
id.exibir_dia_pos,
id.exibir_semana_ant,
id.exibir_semana_pos,
id.exibir_quinzena_ant,
id.exibir_quinzena_pos,
id.exibir_mes_ant,
id.exibir_mes_pos,
id.exibir_bimestre_ant,
id.exibir_bimestre_pos,
id.exibir_trimestre_ant,
id.exibir_trimestre_pos,
id.exibir_quadrimestre_ant,
id.exibir_quadrimestre_pos,
id.exibir_semestre_ant,
id.exibir_semestre_pos,
id.exibir_ano_ant,
id.exibir_ano_pos,
id.ind_legenda_id,
ilg.nome as ind_legenda_nome,
ilg.sigla_ind_legenda as ind_legenda_sigla_ind_legenda,
(select json_agg(
      json_build_object(
      'qnt_de', ilc.qnt_de,
      'qnt_ate', ilc.qnt_ate,
      'cor', ilc.cor,
      'icon', ilc.icon,
      'observacao', ilc.observacao
      )) from ind_legenda_config ilc where ilc.ind_legenda_id = id.ind_legenda_id ) as ind_legenda_config_childs
from ind_grupo ig
join ind_grupo_subgrupo igs on(igs.ind_grupo_id = ig.id)
join ind_subgrupo isg on(igs.ind_subgrupo_id = isg.id)
join sys_user_ind_subgrupo suisg on(suisg.ind_subgrupo_id = isg.id)
join ind_indic_subgrupo iisg on(iisg.ind_subgrupo_id = isg.id)
join ind_indic id on (id.id = iisg.ind_indic_id)
join ger_umedida gu on (id.ger_umedida_id = gu.id)
left join ind_indic idp on (id.ind_indic_id_pond = idp.id)
left join ind_legenda ilg on (id.ind_legenda_id = ilg.id)
join sys_user su on(suisg.sys_user_id = su.id)
where ig.ativo = 'S'
and isg.ativo = 'S'
and ig.unit_id = '{pvunitid}'
and su.login = '{pvuserlogin}'
and iisg.ind_subgrupo_id like '{pvindsubgrupoid}'
[paginate]
"""
SQL_IND_INDIC_FIELD = [
    "ind_grupo_id",
    "ind_grupo_nome",
    "ind_subgrupo_id",
    "ind_subgrupo_nome",
    "id",
    "sigla_ind",
    "nome",
    "ger_umedida_id",
    "ger_umedida_nome",
    "ger_umedida_sigla_umedida",
    "casas_dec",
    "campo_ordenacao",
    "metodo_ordenacao",
    "totalizador_atributo",
    "exibir_media_real",
    "exibir_media_meta",
    "exibir_dia",
    "exibir_semana",
    "exibir_quinzena",
    "exibir_mes",
    "exibir_bimestre",
    "exibir_trimestre",
    "exibir_quadrimestre",
    "exibir_semestre",
    "exibir_ano",
    "ind_indic_id_pond",
    "ind_indic_sigla_ind_pond",
    "ind_indic_nome_pond",
    "grafico_tipo_atributo",
    "grafico_valor_vazio_zero",
    "grafico_tipo_ind",
    "tipo_meta",
    "ativo",
    "exibir_dia_ant",
    "exibir_dia_pos",
    "exibir_semana_ant",
    "exibir_semana_pos",
    "exibir_quinzena_ant",
    "exibir_quinzena_pos",
    "exibir_mes_ant",
    "exibir_mes_pos",
    "exibir_bimestre_ant",
    "exibir_bimestre_pos",
    "exibir_trimestre_ant",
    "exibir_trimestre_pos",
    "exibir_quadrimestre_ant",
    "exibir_quadrimestre_pos",
    "exibir_semestre_ant",
    "exibir_semestre_pos",
    "exibir_ano_ant",
    "exibir_ano_pos",
    "ind_legenda_id",
    "ind_legenda_nome",
    "ind_legenda_sigla_ind_legenda",
    "ind_legenda_config_childs",
]
# ==========================================================
SQL_IND_PER = """
select
gp.id,
gp.{pvtipo}_nome as nome,
gp.data_{pvtipo}_inicial as data_incial,
gp.data_{pvtipo}_final as data_final,
gp.{pvtipo}_numero as numero
from ger_per gp
join ger_per_tipo gpt on (gp.ger_per_tipo_id = gpt.id)
join ger_empresa ge on (ge.ger_per_tipo_id = gpt.id)
where gp.unit_id = '{pvunitid}'
and ge.id in ({pvgerempresaids})
and gp.{pvtipo}_tipo = 'S'
and gp.ano_numero in({pvanos})
order by gp.data_{pvtipo}_inicial desc
"""


SQL_IND_PER_FIELD = ["id", "nome", "data_incial", "data_final", "numero"]
# ==========================================================
SQL_IND_GRUPO_SUBGRUPO = """
select ig.id as ind_grupo_id,
			 ig.nome as ind_grupo_nome,
			 (select json_agg(
							json_build_object(
							'ind_subgrupo_id', isg2.id,
							'ind_subgrupo_nome', isg2.nome,
							'ind_subgrupo_ordem_exibicao', isg2.ordem_exibicao
							)) from (select isg1.id, isg1.nome, isg1.ordem_exibicao
							           from ind_subgrupo isg1
                          join ind_grupo_subgrupo igs1 on(igs1.ind_grupo_id = ig.id and igs1.ind_subgrupo_id = isg1.id)
													join sys_user_ind_subgrupo suisg1 on(suisg1.ind_subgrupo_id = igs1.ind_subgrupo_id)
													join sys_user su1 on(suisg1.sys_user_id = su1.id)
												 where isg1.id = igs1.ind_subgrupo_id
												   and isg1.ativo = 'S'
													 and su1.login = '{pvuserlogin}'
										  order by isg1.ordem_exibicao) isg2) as ind_subgrupo_childs
from ind_grupo ig
where ig.ativo = 'S'
	and exists (select 1
	              from ind_grupo_subgrupo igs
								   join sys_user_ind_subgrupo suisg on(suisg.ind_subgrupo_id = igs.ind_subgrupo_id)
									 join sys_user su on(suisg.sys_user_id = su.id)
							 where igs.ind_grupo_id = ig.id
							   and su.login = '{pvuserlogin}')
	and ig.unit_id = '{pvunitid}'
order by ig.ordem_exibicao
"""
SQL_IND_GRUPO_SUBGRUPO_FIELD = ["ind_grupo_id", "ind_grupo_nome", "ind_subgrupo_childs"]
# ==========================================================
SQL_IND_VALOR = """
select ivr1.id,
       ivr1.atributo,
			 round(ivr1.valor_real,ivr1.casas_dec) as valor_real,
			 round(ivr1.valor_meta,ivr1.casas_dec) as valor_meta,
 			 round(ivr1.qnt_var,ivr1.casas_dec) as qnt_var,
			 round(ivr1.qnt_var_perc,ivr1.casas_dec) as qnt_var_perc,
			 ivr1.ind_indic_id,
			 ivr1.sigla_ind,
			 ivr1.nome,
			 ivr1.ger_umedida_id,
			 ivr1.ger_umedida_nome,
			 ivr1.ger_umedida_sigla_umedida,
			 (case when ivr1.tipo_meta_var = '1' then (select ilc.cor from ind_legenda_config ilc where ilc.ind_legenda_id = ivr1.ind_legenda_id and ilc.qnt_de <= ivr1.qnt_var and ilc.qnt_ate >= ivr1.qnt_var limit 1)
						 when ivr1.tipo_meta_var = '2' then (select ilc.cor from ind_legenda_config ilc where ilc.ind_legenda_id = ivr1.ind_legenda_id and ilc.qnt_de <= ivr1.qnt_var_perc and ilc.qnt_ate >= ivr1.qnt_var_perc limit 1)
						 else null end) as ind_legenda_config_cor,
			 (case when ivr1.tipo_meta_var = '1' then (select ilc.icon from ind_legenda_config ilc where ilc.ind_legenda_id = ivr1.ind_legenda_id and ilc.qnt_de <= ivr1.qnt_var and ilc.qnt_ate >= ivr1.qnt_var limit 1)
						 when ivr1.tipo_meta_var = '2' then (select ilc.icon from ind_legenda_config ilc where ilc.ind_legenda_id = ivr1.ind_legenda_id and ilc.qnt_de <= ivr1.qnt_var_perc and ilc.qnt_ate >= ivr1.qnt_var_perc limit 1)
						 else null end) as ind_legenda_config_icon
       from (
select ivr.id,
       ivr.atributo,
			 ivr.valor_real,
			 ivr.valor_meta,
			 (case when id.tipo_meta = '2' then (coalesce(ivr.valor_real,0)-coalesce(ivr.valor_meta,0))
			       when id.tipo_meta = '1' then (coalesce(ivr.valor_meta,0)-coalesce(ivr.valor_real,0))  end) as qnt_var,
			 (case when id.tipo_meta = '2' then (((coalesce(ivr.valor_real,0)/NULLIF(ivr.valor_meta,0))-1)*100)
			       when id.tipo_meta = '1' then (((coalesce(ivr.valor_meta,0)/NULLIF(ivr.valor_real,0))-1)*100) end) as qnt_var_perc,
			 ivr.ind_indic_id,
			 id.sigla_ind,
			 id.nome,
			 id.ger_umedida_id,
			 id.ind_legenda_id,
			 id.tipo_meta_var,
       id.casas_dec,
			 gu.nome as ger_umedida_nome,
			 gu.sigla_umedida as ger_umedida_sigla_umedida
from ind_vr_{pvtipo} ivr --Variavel tipo valor
join ger_empresa ge on(ivr.ger_empresa_id = ge.id)
join ind_indic id on(ivr.ind_indic_id = id.id)
join ind_indic_subgrupo idsg on (idsg.ind_indic_id = id.id)
join sys_user_ind_subgrupo suisg on(suisg.ind_subgrupo_id = idsg.ind_subgrupo_id)
join ind_subgrupo isg on(suisg.ind_subgrupo_id = isg.id)
join ger_per gp on(ivr.ger_per_id = gp.id)
join ger_umedida gu on (id.ger_umedida_id = gu.id)
join sys_user su on (suisg.sys_user_id = su.id)
where ivr.unit_id = '{pvunitid}'
  and ge.id in ({pvgerempresaids})
	and su.login = '{pvuserlogin}'
	and id.ativo = 'S'
	and isg.ativo = 'S'
  and gp.{pvtipo}_tipo = 'S'
	and gp.id in({pvgerperids})
	and id.id like '{pvindindicid}'
order by id.sigla_ind asc,
(case when id.metodo_ordenacao = '1' and id.campo_ordenacao = '2' then ivr.atributo end) asc,
(case when id.metodo_ordenacao = '2' and id.campo_ordenacao = '2' then ivr.atributo end) desc,
(case when id.metodo_ordenacao = '1' and id.campo_ordenacao = '1' then ivr.valor_real end) asc,
(case when id.metodo_ordenacao = '2' and id.campo_ordenacao = '1' then ivr.valor_real end) desc
	) ivr1
"""
SQL_IND_VALOR_FIELD = [
    "id",
    "atributo",
    "valor_real",
    "valor_meta",
    "qnt_var",
    "qnt_var_perc",
    "ind_indic_id",
    "sigla_ind",
    "nome",
    "ger_umedida_id",
    "ger_umedida_nome",
    "ger_umedida_sigla_umedida",
    "ind_legenda_config_cor",
    "ind_legenda_config_icon",
]
