Drop View If Exists vwger_itemserv;
CREATE OR REPLACE VIEW vwger_itemserv  AS
select 
t1.unit_id as ger_itemserv_unitid,
t1.id as ger_itemserv_id,
t1.nome as ger_itemserv_nome,
t1.ativo as ger_itemserv_ativo,
fnstd('SN','default',t1.ativo) as ger_itemserv_ativo_desc,
t1.tipo as ger_itemserv_tipo,
fnstd('ger_itemserv','tipo',t1.tipo) as ger_itemserv_tipo_desc,
t1.origem_fiscal as ger_itemserv_origem_fiscal,
t1.nome_alternativo as ger_itemserv_nome_alternativo,
t1.tipo_composicao as ger_itemserv_tipo_composicao,
fnstd('ger_itemserv', 'tipo_composicao', t1.tipo_composicao) as ger_itemserv_tipo_composicao_desc,
t1.sigla_itemserv as ger_itemserv_sigla,
t1.tipo_ctb_comp as ger_itemserv_tipo_ctb_comp,
fnstd('ger_itemserv','tipo_ctb_comp',t1.tipo_ctb_comp) as ger_itemserv_tipo_ctb_comp_desc,
t1.fis_sigla_servico  as ger_itemserv_sigla_serviço,
t1.fis_doc_cnae_nfs as ger_itemserv_fis_doc_cnae_nfs,
t1.fis_sigla_servico_municipio as ger_itemserv_fis_sigla_servico_municipio,
t2.id as ger_itemserv_subgrupo_id,
t2.nome as ger_itemserv_subgrupo_nome,
t2.ativo as ger_itemserv_subgrupo_ativo,
fnstd('SN','default',t2.ativo) as ger_itemserv_subgrupo_ativo_desc,

t3.id  as ger_itemserv_grupo_id,t3.nome as ger_itemserv_grupo_nome,
t3.ativo as ger_itemserv_grupo_ativo,
fnstd('SN','default',t3.ativo) as ger_itemserv_grupo_ativo_desc,

t4.id as fis_ncm_id,
t4.nome as fis_ncm_nome,
t4.ativo as fis_ncm_ativo,
fnstd('SN','default',t4.ativo) as fis_ncm_ativo_desc,
t4.data_validade as fis_ncm_dt_validade,
t4.nr_ncm as fis_ncm_nr_ncm,

t5.id as ger_umedida_id,
t5.nome as ger_umedida_nome,
t5.ativo as ger_umedida_ativo,
fnstd('SN','default',t5.ativo) as ger_umedida_ativo_desc,
t5.sigla_umedida as ger_umedida_sigla,


t6.id as fis_cest_id,
t6.nome as fis_cest_nome,
t6.ativo as fis_cest_ativo,
fnstd('SN','default',t6.ativo) as fis_cest_ativo_desc,
t6.data_validade as fis_cest_dt_validade,
t6.nr_cest as fis_cest_nr_cest,

t7.id as fis_nbs_id,
t7.nome as fis_nbs_nome,
t7.ativo as fis_nbs_ativo,
fnstd('SN','default',t7.ativo) as fis_nbs_ativo_desc,
t7.data_validade as fis_nbs_dt_validade,
t7.nr_nbs as fis_nbs_nr_nbs,

t8.id as ctb_comp_id,
t8.nome as ctb_comp_nome,
t8.ativo as ctb_comp_ativo,
fnstd('SN','default',t8.ativo) as ctb_comp_ativo_desc,
t8.sigla_comp as ctb_comp_sigla,
t8.fator_calc_origem as ctb_comp_fator_calc_origem,

t1.log_user_ins,
t1.log_date_ins,
t1.log_user_upd,
t1.log_date_upd,

t1.sigla_itemserv||' - '||t1.nome as ger_itemserv_sigla_desc,
t5.sigla_umedida||' - '||t5.nome as ger_umedida_sigla_desc,
t8.sigla_comp||' - '||t8.nome as ctb_comp_sigla_desc


from ger_itemserv t1
inner join ger_itemserv_subgrupo t2
on t1.ger_itemserv_subgrupo_id = t2.id
inner join ger_itemserv_grupo t3
on t2.ger_grupo_id = t3.id
left join fis_ncm t4
on t1.fis_ncm_id = t4.id
inner join ger_umedida t5
on  t1.ger_umedida_id = t5.id
inner join fis_cest t6
on t1.fis_cest_id = t6.id
left join fis_nbs t7
on t1.fis_nbs_id = t7.id
left join ctb_comp t8
on t1.ctb_comp_id = t8.id

