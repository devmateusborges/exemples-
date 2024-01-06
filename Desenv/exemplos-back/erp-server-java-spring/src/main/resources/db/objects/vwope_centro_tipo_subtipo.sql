drop view if exists vwope_centro_tipo_subtipo;
create or replace view vwope_centro_tipo_subtipo as
select t1.id as ope_centro_tipo_id,
       t1.nome as ope_centro_tipo_nome,		 
			 t1.tipo_es as tipo_es,
			 fnstd('default', 'tipo_es',t1.tipo_es) as tipo_es_desc,
			 t2.id as ope_centro_subtipo_id,
			 t2.nome as ope_centro_subtipo_nome,
			 t2.tipo_destinacao,
			 fnstd('default', 'tipo_destinacao',t2.tipo_destinacao) as tipo_destinacao_desc
  from ope_centro_tipo t1
	join ope_centro_subtipo t2 on t1.id = t2.ope_centro_tipo_id