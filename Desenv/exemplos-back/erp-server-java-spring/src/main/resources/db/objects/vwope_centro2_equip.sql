CREATE OR REPLACE VIEW vwope_centro2_equip AS
 SELECT 
		c.unit_id,
		c.unit_id as ope_centro2_equip_unit_id,
    c.id as ope_centro2_equip_id,
		c.tipo_rodado as ope_centro2_equip_tipo_rodado,
		fnstd('ope_centro2_equip','tipo_rodado',c.tipo_rodado) as ope_centro2_equip_tipo_rodado_desc,		
		c.tipo_carroceria as  ope_centro2_equip_tipo_carroceria,
		fnstd('ope_centro2_equip','tipo_carroceria',c.tipo_carroceria) as  ope_centro2_equip_tipo_carroceria_desc,
		e.id as ope_centro2_equip_cidade_id,
		e.nome as ope_centro2_equip_cidade_nome,
		e.ativo as ope_centro2_equip_cidade_ativo,
		fnstd('SN','default',e.ativo) as ope_centro2_equip_cidade_ativo_desc,
		f.id as ope_centro2_uf_id,
		f.nome as ope_centro2_uf_nome,
		f.sigla_uf as ope_centro2_uf_sigla,
		c.placa as ope_centro2_equip_placa,
		c.renavam as ope_centro2_equip_renavam,
		c.tara as ope_centro2_equip_tara,
		c.capacidade_kg as ope_centro2_equip_capacidade_kg,
		c.capacidade_m3 as ope_centro2_equip_capacidade_m3,
		c.potencia as ope_centro2_equip_potencia,
		c.nr_chassi as ope_centro2_equip_nr_chassi,
		c.nr_serie as ope_centro2_equip_nr_serie,
		c.liberado_abastec as ope_centro2_equip_liberado_abastec,
		fnstd('SN', 'default',c.liberado_abastec) as ope_centro2_equip_liberado_abastec_desc,
		c.largura as ope_centro2_equip_largura,
		c.altura as ope_centro2_equip_altura,
		c.nr_registro_estadual as ope_centro2_equip_nr_registro_estadual,
		
		
		c.tipo_tracao as ope_centro2_equip_tipo_tracao,
		fnstd('ope_centro2_equip', 'tipo_tracao',(c.tipo_tracao)::TEXT) as ope_centro2_equip_tipo_tracao_desc,
		
		c.tipo_transp_auto_carga as ope_centro2_equip_tipo_transp_auto_carga,
		fnstd('ope_centro2_equip','tipo_transp_auto_carga',(c.tipo_transp_auto_carga)::TEXT) as ope_centro2_equip_tipo_transp_auto_carga_desc,
		
		a.unit_id as ope_centro1_unit_id,
		a.id as ope_centro1_id,
		a.sigla_centro1 as ope_centro1_sigla,
		a.nome as ope_centro1_nome,
		a.ativo as ope_centro1_ativo,
		fnstd('SN','default',a.ativo) as ope_centro1_ativo_desc,
		
		b.id AS ope_centro2_id,
		b.nome AS ope_centro2_nome,
		b.ativo as ope_centro2_ativo,
		fnstd('SN','default',b.ativo) as ope_centro2_ativo_desc,
		b.sigla_centro2 as ope_centro2_sigla,
		
		d.id as ope_frente_trabalho_id,
		d.nome as ope_frente_trabalho_nome,
		d.sigla_frente_trabalho as ope_frente_trabalho_sigla,
		d.ativo as ope_frente_trabalho_ativo,
		fnstd('SN','default',d.ativo) as ope_frente_trabalho_ativo_desc,
		
		h.id as ger_marca_modelo_id,
		h.nome as ger_marca_modelo_nome,
		h.ativo as ger_marca_modelo_ativo,
		fnstd('SN','default',h.ativo) as ger_marca_modelo_ativo_desc,
		
		g.id as ger_marca_id,
		g.nome as ger_marca_nome,
		g.ativo as ger_marca_ativo,
		fnstd('SN','default',g.ativo) as ger_marca_ativo_desc,
		
		i.id as ope_centro_subgrupo_id,
		i.nome as ope_centro_subgrupo_nome,
		i.ativo as ope_centro_subgrupo_ativo,
		fnstd('SN','default',i.ativo) as ope_centro_subgrupo_ativo_desc,
		
		i.sigla_centro_subgrupo as ope_centro_subgrupo_sigla,
		j.id as ope_centro_grupo_id,
		j.nome as ope_centro_grupo_nome,
		j.ativo as ope_centro_grupo_ativo,
		fnstd('SN','default',j.ativo) as ope_centro_grupo_ativo_desc,
		j.sigla_centro_grupo as ope_centro_grupo_sigla,
		
		l.id as ger_pessoa_proprietario_id,
		l.nome as ger_pessoa_proprietario_nome,
		l.razao_social as ger_pessoa_proprietario_razao_social,
		l.ativo as ger_pessoa_proprietario_ativo,
		fnstd('SN','default',l.ativo) as ger_pessoa_proprietario_ativo_desc,
		l.doc_cpf as ger_pessoa_proprietario_doc_cpf,
		l.doc_cnpj as ger_pessoa_proprietario_doc_cnpj,
		fnutil_formatcpfcnpj(l.id, false) as ger_pessoa_proprietario_doc_cpf_cnpj_desc,
		c.log_user_ins,
		c.log_date_ins,
		c.log_user_upd,
		c.log_date_upd,
		-- Sigla Desc
		a.sigla_centro1||' - '||a.nome as ope_centro1_sigla_desc,
		b.sigla_centro2||' - '||b.nome as ope_centro2_sigla_desc,
		d.sigla_frente_trabalho||' - '||d.nome as ope_frente_trabalho_sigla_desc,
		j.sigla_centro_grupo||' - '||j.nome as ope_centro_grupo_sigla_desc,
		b.tipo_ctb_comp as ope_centro2_tipo_ctb_comp,
		fnstd('ope_centro2'::text,
		'tipo_ctb_comp'::text,
		b.tipo_ctb_comp::text) as ope_centro2_tipo_ctb_comp_desc,
		b.ctb_comp_id as ope_centro2_ctb_comp_id,
		ccomp.nome as ope_centro2_ctb_comp_nome,
		ccomp.sigla_comp as ope_centro2_ctb_comp_sigla,
		(ccomp.sigla_comp || ' - ') || ccomp.nome as ope_centro2_ctb_comp_sigla_desc,
		ccomp.ativo as ope_centro2_ctb_comp_ativo,
		csubtp.id AS ope_centro_subtipo_id,
    	csubtp.nome AS ope_centro_subtipo_nome

   FROM ope_centro2_equip c
		join ope_centro2 b
		on c.ope_centro2_id = b.id
		join ope_centro1 a
		on b.ope_centro1_id = a.id
		left join ope_frente_trabalho d
		on c.ope_frente_trabalho_id = d.id
		left join ger_cidade e
		on c.ger_cidade_id = e.id
		left join ger_uf f
		on e.ger_uf_id = f.id
		left join ger_marca_modelo h 
		on b.ger_marca_modelo_id = h.id		
		left join ger_marca g
		on  h.ger_marca_id = g.id
		left join ope_centro_subgrupo i
		on b.ope_centro_subgrupo_id = i.id
		left join ope_centro_grupo j
		on i.ope_centro_grupo_id = j.id
		left join ger_pessoa_endereco k
		on b.ger_pessoa_endereco_id = k.id
		left join ger_pessoa l
		on k.ger_pessoa_id = l.id
		left join ctb_comp ccomp on b.ctb_comp_id = ccomp.id
		left JOIN ope_centro_subtipo csubtp ON a.ope_centro_subtipo_id = csubtp.id;
