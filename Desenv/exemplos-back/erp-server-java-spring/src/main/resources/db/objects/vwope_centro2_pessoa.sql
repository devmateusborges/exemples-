drop view if exists vwope_centro2_pessoa;

CREATE OR REPLACE VIEW vwope_centro2_pessoa AS
 SELECT 
    a.unit_id,
		a.unit_id as ope_centro1_unit_id,
    c.id as ope_centro2_pessoa_id,
		c.pto_idenf_tipo as ope_centro2_pessoa_pto_idenf_tipo,
		c.pto_idenf as ope_centro2_pessoa_pto_idenf,
    a.id as ope_centro1_id,
    a.sigla_centro1 as ope_centro1_sigla,
		a.ativo as ope_centro1_ativo,
		fnstd('SN','default',a.ativo) as ope_centro1_ativo_desc,
    a.nome  as ope_centro1_nome,
    a.ope_centro_subtipo_id as ope_centro_subtipo_id,
    d.nome as ope_centro_subtipo_nome,
    b.id as ope_centro2_id,
    b.sigla_centro2 as ope_centro2_sigla,
    b.nome as ope_centro2_nome,
		b.ativo as ope_centro2_ativo,
		fnstd('SN','default',b.ativo) as ope_centro2_ativo_desc,
		e.id as ger_pessoa_id,
		e.nome as ger_pessoa_nome,
		e.razao_social as ger_pessoa_razao_social,
		e.doc_cpf as ope_centro1_pessoa_doc_cpf,
		e.doc_cnpj as ope_centro1_pessoa_doc_cnpj,
		fnutil_formatcpfcnpj(e.id, true) as ope_centro1_pessoa_doc_cpf_cpnj,
		e.ativo as ger_pessoa_ativo,
		fnstd('SN','default',e.ativo) as ger_pessoa_ativo_desc,
		e.sigla_pes as  ger_pessoa_sigla,
		f.id as ope_frente_trabalho_id,
		f.nome as ope_frente_trabalho_nome,
		f.sigla_frente_trabalho as ope_frente_trabalho_sigla,
		f.ativo as ope_frente_trabalho_ativo,
		fnstd('SN','default',f.ativo) as ope_frente_trabalho_ativo_desc,
		c.log_user_ins,
		c.log_date_ins,
		c.log_user_upd,
		c.log_date_upd,
		
		-- Sigla desc
		a.sigla_centro1||' - '||a.nome as ope_centro1_sigla_desc,
		b.sigla_centro2||' - '||b.nome as ope_centro2_sigla_desc,
		e.sigla_pes||' - '||e.nome as  ger_pessoa_sigla_desc,
		f.sigla_frente_trabalho||' - '||e.nome as ope_frente_trabalho_sigla_desc,
		b.tipo_ctb_comp as ope_centro2_tipo_ctb_comp,
		fnstd('ope_centro2'::text,
		'tipo_ctb_comp'::text,
		b.tipo_ctb_comp::text) as ope_centro2_tipo_ctb_comp_desc,
		b.ctb_comp_id as ope_centro2_ctb_comp_id,
		ccomp.nome as ope_centro2_ctb_comp_nome,
		ccomp.sigla_comp as ope_centro2_ctb_comp_sigla,
		(ccomp.sigla_comp || ' - ') || ccomp.nome as ope_centro2_ctb_comp_sigla_desc,
		ccomp.ativo as ope_centro2_ctb_comp_ativo
		
   FROM ope_centro_subtipo d
		join ope_centro1 a
		on d.id = a.ope_centro_subtipo_id
		join ope_centro2 b
		on b.ope_centro1_id = a.id
    join ope_centro2_pessoa c
		on c.ope_centro2_id = b.id
		left join ger_pessoa e
		on a.ger_pessoa_id = e.id
		left join ope_frente_trabalho f
		on c.ope_frente_trabalho_id = f.id
		left join ctb_comp ccomp on b.ctb_comp_id = ccomp.id;
