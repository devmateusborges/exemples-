DROP VIEW IF EXISTS vwind_rel;
CREATE OR replace VIEW vwind_rel
AS
select 
 t1.id as ind_rel_id,
 t1.nome as ind_rel_nome,
 t1.ativo as ind_rel_ativo,
 t1.nome_tecnico as ind_rel_nome_tecnico,
 t1.tipo as ind_rel_tipo,
 
 t3.id as ind_prm_id, 
 t3.nome as ind_prm_nome,
 t3.ativo as ind_prm_ativo,
 t3.nome_tecnico as ind_prm_nome_tecnico,
 t3.tipo_dado as ind_prm_tipo_dado,
 t3.tipo_entrada as ind_prm_tipo_entrada,
 t3.internal as ind_prm_internal,
 t3.busca_tabela as ind_prm_busca_tabela,
 t3.busca_campo_nome as ind_prm_busca_campo_nome,
 t3.busca_campo_id as ind_prm_busca_campo_id, 
 t3.busca_valores as ind_prm_busca_valores, 
 t3.obrigatorio as ind_prm_obrigatorio,
 t3.valor_padrao as ind_prm_valor_padrao, 
 t3.visivel as ind_prm_visivel, 
 t3.busca_tabela_classe as ind_prm_busca_tabela_classe,
 t3.busca_campo_nome_classe as ind_prm_busca_campo_nome_classe,
 t3.busca_campo_id_classe as ind_prm_busca_campo_id_classe,
 
 
 t4.id as ind_ftd_id,
 t4.nome as ind_ftd_nome,
 t4.ativo as ind_ftd_ativo,
 t4.nome_tecnico as ind_ftd_nome_tecnico,
 t4.config_ftd as ind_ftd_config_ftd,
 
 t5.id as ind_cjd_id,
 t5.nome as ind_cjd_nome,
 t5.ativo as ind_cjd_ativo,
 t5.nome_tecnico as ind_cjd_nome_tecnico,
 t2.ordem_exib
 
from ind_rel t1
	inner join ind_rel_relac_prm t2
	on t1.id = t2.ind_rel_id
	inner join ind_prm t3
	on t3.id = t2.ind_prm_id
	left join ind_ftd t4
	on t1.ind_ftd_id = t4.id
	left join ind_cjd t5
	on t1.ind_cjd_id = t5.id
	order by t1.id asc