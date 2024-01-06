DROP VIEW IF EXISTS vwope_centro2_ord_rec;

CREATE OR REPLACE VIEW vwope_centro2_ord_rec as
	SELECT 
		t1.unit_id as ope_centro2_ord_rec_unitid,
		t1.id as ope_centro2_ord_rec_id,
		t1.observacao_interna as ope_centro2_ord_rec_observacao_interna,
		t1.observacao_externa as ope_centro2_ord_rec_observacao_externa,
		t1.qnt_rend as ope_centro2_ord_rec_qnt_rend,
		t1.perc_util as ope_centro2_ord_rec_perc_util,
		t1.qnt_total_util as ope_centro2_ord_rec_qnt_total_util,
		t1.valor_unit_util as ope_centro2_ord_rec_valor_unit_util,
		t1.valor_total_util as ope_centro2_ord_rec_valor_total_util,
		t2.id as ope_centro2_ord_ativ_id,
		t3.id as ope_centro1_id,
		t3.nome as ope_centro1_nome,
		t3.ativo as ope_centro1_ativo,
		fnstd('SN','default',t3.ativo) as ope_centro1_ativo_desc,
		t3.sigla_centro1 as ope_centro1_sigla,

		t4.id as ope_centro2_id,
		t4.nome as ope_centro2_nome,
		t4.ativo as ope_centro2_ativo,
		fnstd('SN','default',t4.ativo) as ope_centro2_ativo_desc,
		t4.sigla_centro2 as ope_centro2_sigla,

		t25.id as ctb_id,
		t25.nome as ctb_nome,
		t25.sigla_comp as ctb_sigla,
		t25.ativo as ctb_ativo,
		fnstd('SN','default',t25.ativo) as ctb_ativo_desc,

		t5.id as ger_pessoa_endereco_id,
		t5.ativo as ger_pessoa_endereco_ativo,
		fnstd('SN','default',t5.ativo) as ger_pessoa_endereco_ativo_desc,
		t5.tipo as ger_pessoa_endereco_tipo,
		fnstd('ger_pessoa_endereco','tipo', t5.tipo) as ger_pessoa_endereco_tipo_desc,
		t5.padrao as ger_pessoa_endereco_padrao,
		fnstd('SN', 'default',t5.padrao) as ger_pessoa_endereco_padrao_desc, 
		t5.end_logradouro as ger_pessoa_endereco_logradouro,
		t5.end_logradouro_nr as ger_pessoa_endereco_loradouro_nr,
		t5.end_bairro as ger_pessoa_endereco_end_bairro,
		t6.id as ger_pessoa_id,
		t6.nome as ger_pessoa_nome,
		t6.ativo as ger_pessoa_ativo,
		fnstd('SN','default',t6.ativo) as ger_pessoa_ativo_desc,
		t6.doc_cpf as ger_pessoa_doc_cpf,
		t6.doc_cnpj as ger_pessoa_doc_cnpj,
		fnutil_formatcpfcnpj(t6.id, true) as ger_pessoa_doc_cpf_cnpj_desc,
		t6.sigla_pes as ger_pessoa_sigla,


		t7.id as ope_centro1_imp01_id,
		t7.nome as ope_centro1_imp01_nome,
		t7.ativo as ope_centro1_imp01_ativo,
		fnstd('SN','default',t7.ativo) as ope_centro1_imp01_ativo_desc,
		t7.sigla_centro1 as ope_centro1_imp01_sigla,
		t8.id as ope_centro2_imp01_id,
		t8.nome as ope_centro2_imp01_nome,
		t8.ativo as  ope_centro2_imp01_id_ativo,
		fnstd('SN','default',t8.ativo) as  ope_centro2_imp01_id_ativo_desc,
		t8.sigla_centro2  as ope_centro2_imp01_sigla,
		t9.id as ope_centro_subtipo_id,
		t9.nome as ope_centro_subtipo_nome,
		t10.id as ope_centro_tipo_id,
		t10.nome as ope_centro_tipo_nome,

		t11.id as ope_centro_subgrupo_id,
		t11.nome as ope_centro_subgrupo_nome,
		t11.ativo as ope_centro_subgrupo_ativo,
		fnstd('SN','default',t11.ativo) as ope_centro_subgrupo_ativo_desc,
		t11.sigla_centro_subgrupo as ope_centro_subgrupo_sigla,

		t12.id as ope_centro_grupo_id,
		t12.nome as ope_centro_grupo_nome,
		t12.ativo as ope_centro_grupo_ativo,
		fnstd('SN','default',t12.ativo) as ope_centro_grupo_ativo_desc,
		t12.sigla_centro_grupo as ope_centro_grupo_sigla,
		-- Ord
		t13.unit_id as ope_centro2_ord_unit_id,
		t13.id as ope_centro2_ord_id,

		t13.data_ini_exec as ope_centro2_ord_data_ini_exec,
		t13.data_fin_exec as ope_centro2_ord_data_fin_exec,
		t13.observacao_interna as ope_centro2_ord_observacao_interna,
		t13.observacao_externa as ope_centro2_ord_observacao_externa,

		t13.data_ini_exec_prev as ope_centro2_ord_data_ini_exec_prev,
		t13.data_fin_exec_prev as ope_centro2_ord_data_fin_exec_prev,
		t13.numero_ord as ope_centro2_ord_numero_ord,

		-- Empresa Ord
		t14.id as ger_empresa_id_ord,
		t14.nome as ger_empresa_nome_ord,
		t14.ativo as ger_empresa_ativo_ord,
		fnstd('SN','default',t14.ativo) as ger_empresa_ativo_desc_ord,
		t14.razao_social as ger_empresa_razao_social_ord,
		t14.sigla_empresa as ger_empresa_sigla_empresa_ord,
		t14.doc_cpf as ger_empresa_doc_cpf_ord,
		t14.doc_cnpj as ger_empresa_doc_cnpj_ord,

		-- Periodo Ord
		t15.id as ope_periodo_id_ord,
		t15.nome as ope_periodo_nome_ord,
		t15.ativo as ope_periodo_ativo_ord,
		fnstd('SN','default',t15.ativo) as ope_periodo_ativo_ord_desc,
		t15.sigla_periodo as ope_periodo_sigla_periodo_ord,
		t15.data_ini as ope_periodo_data_ini_ord,
		t15.data_fin as ope_periodo_data_fin_ord,
		--Pessoa Centro2 Ord
		t16.id as ope_centro2_pessoa_id_ord,
		t17.id as ope_centro2_id_pessoa_ord,
		t17.nome as ope_centro2_nome_pessoa_ord,
		t17.ativo as ope_centro2_ativo_ord_pessoa,
		fnstd('default','ativo',t17.ativo) as ope_centro2_ativo_ord_pessoa_desc,
		t17.sigla_centro2 as ope_centro2_sigla_pessoa_ord,

		-- Pessoa Ord
		t19.id as ger_pessoa_id_ord,
		t19.nome as ger_pessoa_nome_ord,
		t19.razao_social as ger_pessoa_razao_social_ord,
		t19.ativo as ger_pessoa_ativo_ord,
		fnstd('SN','default',t19.ativo) as ger_pessoa_ativo_desc_ord,
		t19.doc_cpf as ger_pessoa_doc_cpf_ord,
		t19.doc_cnpj as ger_pessoa_doc_cnpj_ord,
		fnutil_formatcpfcnpj(t19.id,true) as ger_pessoa_doc_cpf_cnpj_ord,
		t19.sigla_pes as ger_pessoa_sigla_ord,

		-- Pessoa Endereco Ord
		t18.id as ger_pessoa_endereco_id_ord,
		t18.ativo as ger_pessoa_endereco_ativo_ord,
		fnstd('SN','default',t18.ativo) as ger_pessoa_endereco_ativo_ord_desc,
		t18.tipo as ger_pessoa_endereco_tipo_ord,
		fnstd('ger_pessoa_endereco','tipo',t18.tipo) as ger_pessoa_endereco_tipo_ord_desc,
		t18.padrao as ger_pessoa_endereco_padrao_ord,
		fnstd('SN', 'default',t18.padrao) as ger_pessoa_endereco_padrao_ord_desc,
		t18.end_logradouro as ger_pessoa_endereco_logradouro_ord,
		t18.end_logradouro_nr as ger_pessoa_endereco_logradouro_nr_ord,
		-- Ord Tipo
		t20.id as ope_centro2_ord_tipo_id,  
		t20.nome as ope_centro2_ord_tipo_nome,
		t20.ativo as ope_centro2_ord_tipo_ativo,
		fnstd('SN','default',t20.ativo) as ope_centro2_ord_tipo_ativo_desc,
		t20.sigla_ord_tipo as ope_centro2_ord_tipo_sigla,

		-- centro2 Ord
		t21.id as ope_centro2_id_ord,
		t21.nome as ope_centro2_nome_ord,
		t21.ativo as ope_centro2_ativo_ord,
		fnstd('SN','default',t21.ativo) as ope_centro2_ativo_ord_desc,
		t21.sigla_centro2 as ope_centro2_sigla_centro2_ord,

		-- centro1 ord
		t24.id as ope_centro1_id_ord,
		t24.nome as ope_centro1_nome_ord,
		t24.ativo as ope_centro1_ativo_ord,
		fnstd('SN','default',t24.ativo) as ope_centro1_ativo_ord_desc,
		t24.sigla_centro1 as ope_centro1_sigla_ord,

		-- Frente de trabalho
		t22.id as ope_frente_trabalho_id_ord,
		t22.nome as ope_frente_trabalho_nome_ord,
		t22.ativo as  ope_frente_trabalho_ativo_ord,
		fnstd('SN','default',t22.ativo) as  ope_frente_trabalho_ativo_desc_ord,
		t22.sigla_frente_trabalho as ope_frente_trabalho_sigla_ord,

		-- Ord Status
		t23.id as ope_centro2_ord_status_id,
		t23.nome as ope_centro2_ord_status_nome,
		t23.ativo as ope_centro2_ord_status_ativo,
		fnstd('SN','default',t23.ativo) as ope_centro2_ord_status_ativo_desc,
		t23.sigla_ord_status as ope_centro2_ord_status_sigla,
		t23.tipo_status as ope_centro2_ord_status_tipo_status,

		t26.id as ope_compart_id,
		t26.nome as ope_compart_nome,
		t26.ativo as ope_compart_ativo,
		fnstd('SN','default',t26.ativo) as ope_compart_ativo_desc,
		t26.sigla_compart  as ope_compart_sigla,
		t1.log_user_ins,
		t1.log_date_ins,
		t1.log_user_upd,
		t1.log_date_upd,

		-- Siglas Desc
		t3.sigla_centro1||' - '||t3.nome as ope_centro1_sigla_desc,
		t4.sigla_centro2||' - '||t4.nome as ope_centro2_sigla_desc,
		t25.sigla_comp||' - '||t25.nome as ctb_sigla_desc,
		t6.sigla_pes||' - '||t6.nome as ger_pessoa_sigla_pes_desc,
		t7.sigla_centro1||' - '||t7.nome as ope_centro1_imp01_sigla_desc,
		t8.sigla_centro2||' - '||t9.nome  as ope_centro2_imp01_sigla_desc,
		t11.sigla_centro_subgrupo||' - '||t11.nome as ope_centro_subgrupo_sigla_desc,
		t12.sigla_centro_grupo||' - '||t12.nome as ope_centro_grupo_sigla_desc,
		t14.sigla_empresa||' - '||t14.nome as ger_empresa_sigla_empresa_ord_desc,
		t15.sigla_periodo||' - '||t15.nome as ope_periodo_sigla_periodo_ord_desc,
		t17.sigla_centro2||' - '||t17.nome as ope_centro2_sigla_pessoa_ord_desc,
		t19.sigla_pes||' - '||t19.nome as ger_pessoa_sigla_ord_desc,
		t20.sigla_ord_tipo||' - '||t20.nome as ope_centro2_ord_tipo_sigla_desc,
		t21.nome||' - '||t21.sigla_centro2 as ope_centro2_sigla_centro2_ord_desc,
		t24.nome||' - '||t24.sigla_centro1 as ope_centro1_sigla_ord_desc,
		t22.sigla_frente_trabalho||' - '||t22.nome as ope_frente_trabalho_sigla_ord_desc,
		t23.nome||' - '||t23.sigla_ord_status as ope_centro2_ord_status_sigla_desc,
		t26.sigla_compart||' - '||t26.nome as ope_compart_sigla_desc

	FROM ope_centro2_ord_rec t1
		left join ope_centro2_ord_ativ t2
		on t1.ope_centro2_ord_ativ_id = t2.id
		left join ope_centro1 t3
		on t1.ope_centro1_id = t3.id
		left join ope_centro2 t4
		on t1.ope_centro2_id = t4.id
		 
		left join ctb_comp t25
		on t4.ctb_comp_id = t25.id
		 
		left join ger_pessoa_endereco t5
		on t1.ger_pessoa_endereco_id_exec = t5.id
		left join ger_pessoa t6
		on t5.ger_pessoa_id = t6.id
		left join ope_centro1 t7
		on t1.ope_centro1_id_imp01 = t7.id
		left join ope_centro2 t8
		on t1.ope_centro2_id_imp01 = t8.id
		left join ope_centro_subtipo t9
		on t3.ope_centro_subtipo_id = t9.id
		left join ope_centro_tipo t10
		on t9.ope_centro_tipo_id = t10.id
		left join ope_centro_subgrupo t11
		on  t4.ope_centro_subgrupo_id = t11.id
		left join ope_centro_grupo t12
		on t11.ope_centro_grupo_id = t12.id
		-- Relac Ord

		left join ope_centro2_ord t13
		on t2.ope_centro2_ord_id = t13.id
		-- Empresa
		left join  ger_empresa t14
		on t13.ger_empresa_id  = t14.id
		-- Periodo
		left join ope_periodo t15
		on t13.ope_periodo_id = t15.id
		--
		left join ope_centro2_pessoa t16
		on t13.ope_centro2_pessoa_id_solic = t16.id
		left join ope_centro2 t17
		on t16.ope_centro2_id = t17.id
		left join ger_pessoa_endereco t18
		on  t13.ger_pessoa_endereco_id_exec = t18.id
		left join ger_pessoa t19
		on t18.ger_pessoa_id =  t19.id

		left join ope_centro2_ord_tipo t20
		on t13.ope_centro2_ord_tipo_id = t20.id

		left join ope_centro2 t21
		on t13.ope_centro2_id = t21.id

		left join ope_frente_trabalho t22
		on t13.ope_frente_trabalho_id = t22.id

		left join ope_centro2_ord_status t23
		on t13.ope_centro2_ord_status_id = t23.id

		left join ope_centro1 t24
		on t21.ope_centro1_id = t24.id
		left join ope_compart t26
		on t1.ope_compart_id = t26.id

		-- left join ope_centro_versao t24
		-- on  t13.ope_centro_versao_id = t24.id

		--
		-- left join system_process_log t25
		-- on  t13.process_id = t25.id
 
 

