DROP VIEW IF EXISTS vwope_centro2_ord_dest;
CREATE OR REPLACE VIEW vwope_centro2_ord_dest  AS
	SELECT 
		-- Dest
		t1.unit_id as ope_centro2_ord_dest_unit_id,
		t1.id as ope_centro2_ord_dest_id,

		t1.qnt_prev_obj as ope_centro2_ord_dest_qnt_prev_obj,

		t1.valor_unit_prev as ope_centro2_ord_dest_valor_unit_prev,
		t1.valor_total_prev as ope_centro2_ord_dest_valor_total_prev,
		t1.observacao_interna as ope_centro2_ord_dest_observacao_interna, 
		t1.observacao_externa as ope_centro2_ord_dest_observacao_externa,

		t1.qnt_obj as ope_centro2_ord_dest_qnt_obj,

		t1.valor_unit as ope_centro2_ord_dest_valor_unit,
		t1.valor_total as ope_centro2_ord_dest_valor_total,

		t2.data_ini_exec as ope_centro2_ord_data_ini_exec,
		t2.data_fin_exec as ope_centro2_ord_data_fin_exec,

		t2.data_status as ope_centro2_ord_data_status,
		t2.observacao_interna as ope_centro2_ord_observacao_interna,
		t2.observacao_externa as ope_centro2_ord_observacao_externa,
		t2.ger_pessoa_endereco_id_exec as ope_centro2_ord_ger_pessoa_endereco_id_exec,
		t2.ope_centro2_ord_tipo_id as ope_centro2_ord_ope_centro2_ord_tipo_id,
		t2.ope_centro2_id as ope_centro2_ord_ope_centro2_id,
		t2.ope_frente_trabalho_id as ope_centro2_ord_ope_frente_trabalho_id,

		t2.data_ini_exec_prev as ope_centro2_ord_data_ini_exec_prev,
		t2.data_fin_exec_prev as ope_centro2_ord_data_fin_exec_prev,

		t2.ope_centro2_ord_status_id as ope_centro2_ord_ope_centro2_ord_status_id,
		t2.ope_centro_versao_id as ope_centro2_ord_ope_centro_versao_id,

		t3.id as ope_centro2_id,
		t3.nome as ope_centro2_nome,
		t3.sigla_centro2 as ope_centro2_sigla,
		t3.ativo as ope_centro2_ativo,
		fnstd('SN','default',t3.ativo) as ope_centro2_ativo_desc,

		t21.id as ctb_id,
		t21.nome as ctb_nome,
		t21.ativo as ctb_ativo,
		fnstd('SN','default',t21.ativo) as ctb_ativo_desc,
		t21.sigla_comp as ctb_sigla,

		t4.id as ger_umedida_id,
		t4.nome as ger_umedida_nome,
		t4.ativo as ger_umedida_ativo,
		fnstd('SN','default',t4.ativo) as ger_umedida_ativo_desc,
		t4.sigla_umedida as ger_umedida_sigla,
		-- ord
		t5.id as ope_centro1_id,
		t5.nome as ope_centro1_nome_dest,
		t5.ativo as ope_centro1_ativo,
		fnstd('SN','default',t5.ativo) as ope_centro1_ativo_desc,
		t5.sigla_centro1 as ope_centro1_sigla,

		t6.id as ope_centro_subgrupo_id,
		t6.nome as ope_centro_subgrupo_nome,
		t6.ativo as ope_centro_subgrupo_ativo,
		fnstd('SN','default',t6.ativo) as ope_centro_subgrupo_ativo_desc,
		t6.sigla_centro_subgrupo as ope_centro_subgrupo_sigla,

		t7.id as ope_centro_grupo_id,
		t7.nome as ope_centro_grupo_nome,
		t7.ativo as ope_centro_grupo_ativo,
		fnstd('SN','default',t7.ativo) as ope_centro_grupo_ativo_desc,
		t7.sigla_centro_grupo as ope_centro_grupo_sigla,
		t8.id as ope_centro_subtipo_id,
		t8.nome as ope_centro_subtipo_nome,
		t9.id as ope_centro_tipo_id,
		t9.nome as ope_centro_tipo_nome,

		-- Empresa Ord
		t10.id as ger_empresa_id_ord,
		t10.nome as ger_empresa_nome_ord,
		t10.razao_social as ger_empresa_razao_social_ord,
		t10.ativo as ger_empresa_ativo_ord,
		fnstd('SN','default',t10.ativo) as ger_empresa_ativo_ord_desc,
		t10.sigla_empresa as ger_empresa_sigla_empresa_ord,
		t10.doc_cnpj as ger_empresa_doc_cnpj_ord,
		t10.doc_cpf as ger_empresa_doc_cpf_ord,
		-- Periodo Ord

		t11.id as ope_periodo_id_ord,
		t11.nome  as ope_periodo_nome_ord,
		t11.ativo as ope_periodo_ativo_ord,
		fnstd('SN','default',t11.ativo) as ope_periodo_ativo_ord_desc,
		t11.sigla_periodo  as ope_periodo_sigla_periodo_ord,

		t11.data_ini  as ope_periodo_data_ini_ord,
		t11.data_fin  as ope_periodo_data_fin_ord,
		-- Solicitante ord
		t12.id as ope_centro2_pessoa_id_ord,
		t13.id as ope_centro2_id_pessoa_ord,
		t13.nome as ope_centro2_nome_pessoa_ord,
		t13.sigla_centro2 as ope_centro2_sigla_centro2_pessoa_ord,

		-- Pessoa Endereco
		t14.id as ger_pessoa_endereco_id_ord,
		t14.ativo as ger_pessoa_endereco_ativo_ord,
		fnstd('SN','default',t14.ativo) as ger_pessoa_endereco_ativo_ord_desc,
		t14.tipo as ger_pessoa_endereco_tipo_ord,
		fnstd('ger_pessoa_endereco','tipo',t14.tipo) as ger_pessoa_endereco_tipo_ord_desc,
		t14.padrao as ger_pessoa_endereco_padrao_ord,
		fnstd('SN', 'default',t14.padrao) as ger_pessoa_endereco_padrao_ord_desc,
		t14.end_logradouro as ger_pessoa_endereco_end_logradouro_ord,
		t14.end_logradouro_nr as ger_pessoa_endereco_end_logradouro_nr_ord,
		t14.end_bairro as ger_pessoa_endereco_end_bairro_ord,
		t14.end_complemento as ger_pessoa_endereco_end_complemento_ord,
		t14.ger_pessoa_id as ger_pessoa_id_endereco_ord,
		t15.id as ger_pessoa_id_ord,
		t15.nome as ger_pessoa_nome_ord,
		t15.ativo as ger_pessoa_ativo_ord,
		fnstd('SN','default',t15.ativo) as ger_pessoa_ativo_ord_desc,
		t15.sigla_pes as ger_pessoa_sigla_ord,
		t15.razao_social as ger_pessoa_razao_social_ord,
		t15.doc_cpf as ger_pessoa_doc_cpf_ord,
		t15.doc_cnpj as ger_pessoa_doc_cnpj_ord,
		fnutil_formatcpfcnpj(t15.id, true) as ger_pessoa_doc_cpf_cnpj_ord,
		-- Tipo ord
		t16.id as ope_centro2_ord_tipo_id_ord,
		t16.nome  as ope_centro2_ord_tipo_nome_ord,
		t16.ativo as ope_centro2_ord_tipo_ativo_ord,
		fnstd('SN','default',t16.ativo) as ope_centro2_ord_tipo_ativo_ord_desc,
		t16.sigla_ord_tipo  as ope_centro2_ord_tipo_sigla_ord,
		-- Tipo ord
		t17.id as ope_centro2_id_ord,
		t17.nome as ope_centro2_nome_ord,
		t17.ativo as ope_centro2_ativo_ord,
		fnstd('SN','default',t17.ativo) as ope_centro2_ativo_desc_ord,
		t17.sigla_centro2 as ope_centro2_sigla_centro2_ord,
		t17.ope_centro1_id as ope_centro2_centro1_id_ord,

		t18.id as ope_frente_trabalho_id_ord,
		t18.nome as ope_frente_trabalho_nome_ord,
		t18.ativo as ope_frente_trabalho_ativo,
		fnstd('SN','default',t18.ativo) as ope_frente_trabalho_ativo_desc,
		t18.sigla_frente_trabalho  as ope_frente_trabalho_sigla_frente_trabalho_ord,
		-- Status
		t19.id as ope_centro2_ord_status_id_ord,
		t19.nome as ope_centro2_ord_status_nome_ord,
		t19.ativo as ope_centro2_ord_status_ativo_ord,
		fnstd('SN','default',t19.ativo) as ope_centro2_ord_status_ativo_ord_desc,
		t19.sigla_ord_status as ope_centro2_ord_status_sigla_ord_status_ord,
		t19.tipo_status as ope_centro2_tipo_status_ord,
		fnstd('ope_centro2_ord_status', 'tipo_status',t19.tipo_status) as ope_centro2_tipo_status_ord_desc,
		-- Versão
		t20.id as ope_centro_versao_id_ord,
		t20.nome as ope_centro_versao_nome_ord,
		t20.ativo as ope_centro_versao_ativo_ord,
		fnstd('SN','default',t20.ativo) as ope_centro_versao_ativo_ord_desc,
		t20.sigla_versao as ope_centro_versao_sigla_versão_ord,

		t1.log_user_ins,
		t1.log_date_ins,
		t1.log_user_upd,
		t1.log_date_upd,

		-- Siglas Desc
		t3.sigla_centro2||' - '||t3.nome as ope_centro2_sigla_desc,
		t21.sigla_comp||' - '||t21.nome as ctb_sigla_desc,
		t4.sigla_umedida||' - '||t4.nome as ger_umedida_sigla_desc,
		t5.sigla_centro1||' - '||t5.nome as ope_centro1_sigla_desc,
		t6.sigla_centro_subgrupo||' - '||t6.nome as ope_centro_subgrupo_sigla_desc,
		t7.sigla_centro_grupo||' - '||t7.nome as ope_centro_grupo_sigla_desc,
		t10.sigla_empresa||' - '||t10.nome as ger_empresa_sigla_empresa_ord_desc,
		t11.sigla_periodo||' - '||t11.nome  as ope_periodo_sigla_periodo_ord_desc,
		t13.sigla_centro2||' - '||t13.nome as ope_centro2_sigla_centro2_pessoa_ord_desc,
		t15.sigla_pes||' - '||t15.nome as ger_pessoa_sigla_ord_desc,
		t16.sigla_ord_tipo||' - '||t16.nome  as ope_centro2_ord_tipo_sigla_ord_desc,
		t17.sigla_centro2||' - '||t17.nome as ope_centro2_sigla_centro2_ord_desc,
		t18.sigla_frente_trabalho||' - '||t18.nome  as ope_frente_trabalho_sigla_desc,
		t19.sigla_ord_status||' - '||t19.nome as ope_centro2_ord_status_sigla_ord_status_ord_desc,
		t20.sigla_versao||' - '||t20.nome as ope_centro_versao_sigla_versão_ord_desc

	FROM ope_centro2_ord_dest t1
		left join ope_centro2_ord t2
		on  t1.ope_centro2_ord_id = t2.id
		left join ope_centro2 t3
		on t1.ope_centro2_id_dest =  t3.id
		left join ctb_comp t21
		on t21.id = t3.ctb_comp_id
		left join ger_umedida t4
		on t1.ger_umedida_id_dest = t4.id
		left join ope_centro1 t5
		on t3.ope_centro1_id = t5.id
		left join ope_centro_subgrupo t6
		on t3.ope_centro_subgrupo_id = t6.id
		left join ope_centro_grupo t7
		on  t6.ope_centro_grupo_id = t7.id
		left join ope_centro_subtipo t8
		on  t7.ope_centro_subtipo_id = t8.id
		left join ope_centro_tipo t9
		on t8.ope_centro_tipo_id = t9.id
		-- Join com T2
		left join  ger_empresa t10
		on t2.ger_empresa_id  = t10.id
		left join ope_periodo t11
		on t2.ope_periodo_id = t11.id
		left join ope_centro2_pessoa t12
		on t2.ope_centro2_pessoa_id_solic = t12.id
		left join ope_centro2 t13
		on t12.ope_centro2_id = t13.id
		left join ger_pessoa_endereco t14
		on  t2.ger_pessoa_endereco_id_exec = t14.id
		left join ger_pessoa t15
		on t14.ger_pessoa_id =  t15.id
		left join ope_centro2_ord_tipo t16
		on t2.ope_centro2_ord_tipo_id = t16.id
		left join ope_centro2 t17
		on t2.ope_centro2_id = t17.id
		left join ope_frente_trabalho t18
		on t2.ope_frente_trabalho_id = t18.id
		left join ope_centro2_ord_status t19
		on t2.ope_centro2_ord_status_id = t19.id
		left join ope_centro_versao t20
		on  t2.ope_centro_versao_id = t20.id




