drop view if exists vwope_centro2_estoque;
CREATE OR REPLACE VIEW public.vwope_centro2_estoque AS
	Select 
		a.unit_id,
		a.unit_id as ope_centro2_estoque_unit_id,	
		a.id as ope_centro2_estoque_id,
		a.tipo as ope_centro2_estoque_tipo,
		fnstd('ope_centro2_estoque', 'tipo',a.tipo) as ope_centro2_estoque_tipo_desc,
		b.id as ope_centro2_id,
		b.nome as ope_centro2_nome,
		b.ativo as ope_centro2_ativo,
		fnstd('SN','default',b.ativo) as ope_centro2_ativo_desc,
		b.sigla_centro2 as ope_centro2_sigla_centro2,
		b.sigla_centro2||' - '||b.nome as ope_centro2_sigla_centro2_desc,
		b.tipo_destinacao as ope_centro2_tipo_destinacao,
		fnstd('ope_centro2', 'tipo_destinacao',b.tipo_destinacao) as ope_centro2_tipo_destinacao_desc,
		b.tipo_ctb_comp as ope_centro2_tipo_ctb_comp,
		fnstd('ope_centro2', 'tipo_ctb_comp',b.tipo_ctb_comp) as ope_centro2_tipo_ctb_comp_desc,
		b.ctb_comp_id	as ope_centro2_ctb_comp_id,
		a.log_user_ins,
		a.log_date_ins,
		a.log_user_upd,
		a.log_date_upd,
		ccomp.nome as ope_centro2_ctb_comp_nome,
		ccomp.sigla_comp as ope_centro2_ctb_comp_sigla,
		(ccomp.sigla_comp || ' - ') || ccomp.nome as ope_centro2_ctb_comp_sigla_desc,
		ccomp.ativo as ope_centro2_ctb_comp_ativo,
		c1.id AS ope_centro1_id,
		c1.sigla_centro1 AS ope_centro1_sigla,
		c1.nome AS ope_centro1_nome,
		c1.ativo AS ope_centro1_ativo,
		fnstd ('SN', 'default'::text, c1.ativo::text) AS ope_centro1_ativo_desc,
		(c1.sigla_centro1::text || ' - '::text) || c1.nome::text AS ope_centro1_sigla_desc,
		d.id AS ope_centro_subtipo_id,
    	d.nome AS ope_centro_subtipo_nome,
		g.id AS ope_centro_grupo_id,
		g.nome AS ope_centro_grupo_nome,
		g.sigla_centro_grupo AS ope_centro_grupo_sigla,
		g.ativo AS ope_centro_grupo_ativo,
		fnstd ('SN'::text, 'default'::text, g.ativo::text) AS ope_centro_grupo_ativo_desc,
		f.id AS ope_centro_subgrupo_id,
		f.nome AS ope_centro_subgrupo_nome,
		f.sigla_centro_subgrupo AS ope_centro_subgrupo_sigla,
		f.ativo AS ope_centro_subgrupo_ativo,
		fnstd ('SN'::text, 'default'::text, f.ativo::text) AS ope_centro_subgrupo_ativo_desc,
		(f.sigla_centro_subgrupo::text || ' - '::text) || f.nome::text AS ope_centro_subgrupo_sigla_desc
	from ope_centro2_estoque a
	left join ope_centro2 b
	on a.ope_centro2_id = b.id
	left JOIN ope_centro1 c1 ON b.ope_centro1_id = c1.id
	left JOIN ope_centro_subtipo d ON c1.ope_centro_subtipo_id = d.id
	left join ctb_comp ccomp on b.ctb_comp_id = ccomp.id
    LEFT JOIN ope_centro_subgrupo f ON b.ope_centro_subgrupo_id = f.id
    LEFT JOIN ope_centro_grupo g ON f.ope_centro_grupo_id = g.id;