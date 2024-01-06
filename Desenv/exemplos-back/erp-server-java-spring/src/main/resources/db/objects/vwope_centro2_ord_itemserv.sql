DROP VIEW IF EXISTS vwope_centro2_ord_itemserv;
CREATE OR REPLACE VIEW vwope_centro2_ord_itemserv  AS
 SELECT 
		t1.unit_id as ope_centro2_ord_itemserv_unit_id,
		t1.id as ope_centro2_ord_itemserv_id,
		t1.observacao_interna as ope_centro2_ord_itemserv_observacao_interna,
		t1.observacao_externa as ope_centro2_ord_itemserv_observacao_externa,
		t1.qnt_rend as ope_centro2_ord_itemserv_qnt_rend,
		t1.perc_util as ope_centro2_ord_itemserv_perc_util,
		t1.qnt_total_util as ope_centro2_ord_itemserv_qnt_total_util,
		t1.valor_unit_util as ope_centro2_ord_itemserv_valor_unit_util,
		t1.valor_total_util as ope_centro2_ord_itemserv_valor_total_util,
		t2.observacao_interna as ope_centro2_ord_ativ_observacao_interna,
		t2.observacao_externa as ope_centro2_ord_ativ_observacao_externa,
		t2.ope_atividade_id as ope_centro2_ord_ativ_ope_atividade_id,
		t2.ordem_exec as ope_centro2_ord_ativ_ordem_exec,
		fnstd('ope_centro2_ord_ativ', 'tipo_executor',t2.tipo_executor) as ope_centro2_ord_tipo_executor,
		t3.id as ger_itemserv_id,
		t3.nome as ger_itemserv_nome,
		t3.ativo as ger_itemserv_ativo,
		fnstd('SN','default',t3.ativo) as ger_itemserv_ativo_desc,
		t3.referencia1 as ger_itemserv_referencia1,
		t3.referencia2 as ger_itemserv_nome_referencia2,
		t3.referencia3 as ger_itemserv_nome_referencia3,
		fnstd('ger_itemserv', 'tipo',t3.tipo) as ger_itemserv_tipo_desc,
		t3.origem_fiscal as ger_itemserv_origem_fiscal,
		t3.nome_alternativo as ger_itemserv_nome_alternativo,
		fnstd('ger_itemserv', 'tipo_composicao',t3.tipo_composicao) as ger_itemserv_tipo_composição_desc,
		t3.sigla_itemserv as  ger_itemserv_sigla,
		fnstd('ger_itemserv', 'tipo_ctb_comp',t3.tipo_ctb_comp) as ger_itemserv_tipo_ctb_comp_desc,
		t3.ctb_comp_id as ger_itemserv_ctb_comp_id,
		t4.id as ope_atividade_id,
		t4.nome as ope_atividade_nome,
		t4.ativo as ope_atividade_ativo,
		fnstd('SN','default',t4.ativo) as ope_atividade_ativo_desc,
		t4.sigla_atividade as ope_atividade_sigla,

		-- Ord
		t5.unit_id as ope_centro2_ord_unit_id,
		t5.id as ope_centro2_ord_id,
		t5.data_ini_exec as ope_centro2_ord_data_ini_exec,
		t5.data_fin_exec as ope_centro2_ord_data_fin_exec,
		t5.observacao_interna as ope_centro2_ord_observacao_interna,
		t5.observacao_externa as ope_centro2_ord_observacao_externa,
		t5.data_ini_exec_prev as ope_centro2_ord_data_ini_exec_prev,
		t5.data_fin_exec_prev as ope_centro2_ord_data_fin_exec_prev,
		t5.numero_ord as ope_centro2_ord_numero_ord,
		-- Empresa Ord
		t6.id as ger_empresa_id_ord,
		t6.nome as ger_empresa_nome_ord,
		t6.ativo as ger_empresa_ativo_ord,
		fnstd('SN','default',t6.ativo) as ger_empresa_ativo_desc_ord,
		t6.razao_social as ger_empresa_razao_social_ord,
		t6.sigla_empresa as ger_empresa_sigla_empresa_ord,
		t6.doc_cpf as ger_empresa_doc_cpf_ord,
		t6.doc_cnpj as ger_empresa_cnpj_ord,

		-- Periodo Ord
		t7.id as ope_periodo_id_ord,
		t7.nome as ope_periodo_nome_ord,
		t7.ativo as ope_periodo_ativo_ord,
		fnstd('SN','default',t7.ativo) as ope_periodo_ativo_ord_desc,
		t7.sigla_periodo as ope_periodo_sigla_periodo_ord,
		t7.data_ini as ope_periodo_data_ini_ord,
		t7.data_fin as ope_periodo_data_fin_ord,
		--Pessoa Centro2 Ord
		t8.id as ope_centro2_pessoa_id_ord,
		t9.id as ope_centro2_id_pessoa_ord,
		t9.nome as ope_centro2_nome_pessoa_ord,
		t9.ativo as ope_centro2_ativo_ord_pessoa,
		fnstd('SN','default',t9.ativo) as ope_centro2_ativo_ord_pessoa_desc,
		t9.sigla_centro2 as ope_centro2_sigla_pessoa_ord,

		-- Ctb Centro2
		t22.id as ctb_id,
		t22.nome as ctb_nome,
		t22.ativo as ctb_ativo,
		fnstd('SN','default',t22.ativo) as ctb_ativo_desc,
		t22.sigla_comp as ctb_sigla,

		-- Pessoa Ord
		t11.id as ger_pessoa_id_ord,
		t11.nome as ger_pessoa_nome_ord,
		t11.sigla_pes as ger_pessoa_sigla,
		t11.razao_social as ger_pessoa_razao_social_ord,
		t11.ativo as ger_pessoa_ativo_ord,
		fnstd('SN','default',t11.ativo) as ger_pessoa_ativo_desc_ord,
		t11.doc_cpf as ger_pessoa_doc_cpf,
		t11.doc_cnpj as ger_pessoa_doc_cnpj,
		fnutil_formatcpfcnpj(t11.id,true) as ger_pessoa_doc_cpf_cnpj_ord,


		-- Pessoa Endereco Ord
		t10.id as ger_pessoa_endereco_id_ord,
		t10.ativo as ger_pessoa_endereco_ativo_ord,
		fnstd('SN','default',t10.ativo) as ger_pessoa_endereco_ativo_ord_desc,
		t10.tipo as ger_pessoa_endereco_tipo_ord,
		t10.padrao as ger_pessoa_endereco_padrao_ord,
		t10.end_logradouro as ger_pessoa_endereco_logradouro_ord,
		t10.end_logradouro_nr as ger_pessoa_endereco_logradouro_nr_ord,
		--Ord Tipo
		t12.id as ope_centro2_ord_tipo_id,  
		t12.nome as ope_centro2_ord_tipo_nome,
		t12.ativo as ope_centro2_ord_tipo_ativo,
		fnstd('SN','default',t12.ativo) as ope_centro2_ord_tipo_ativo_desc,
		t12.sigla_ord_tipo as ope_centro2_ord_tipo_sigla,

		-- centro2 Ord
		t13.id as ope_centro2_id_ord,
		t13.nome as ope_centro2_nome_ord,
		t13.ativo as ope_centro2_ativo_ord,
		fnstd('SN','default',t13.ativo) as ope_centro2_ativo_ord_desc,
		t13.sigla_centro2 as ope_centro2_sigla_centro2_ord,

		-- centro1 ord
		t17.id as ope_centro1_id_ord,
		t17.nome as ope_centro1_nome_ord,
		t17.ativo as ope_centro1_ativo_ord,
		fnstd('SN','default',t17.ativo) as ope_centro1_ativo_ord_desc,
		t17.sigla_centro1 as ope_centro1_sigla_ord,

		-- Frente de trabalho
		t14.id as ope_frente_trabalho_id_ord,
		t14.nome as ope_frente_trabalho_nome_ord,
		t14.ativo as ope_frente_trabalho_ativo_ord,
		fnstd('SN','default',t14.ativo) as ope_frente_trabalho_ativo_desc_ord,
		t14.sigla_frente_trabalho as ope_frente_trabalho_sigla_ord,

		-- Ord Status
		t15.id as ope_centro2_ord_status_id,
		t15.nome as ope_centro2_ord_status_nome,
		t15.ativo as ope_centro2_ord_status_ativo, 
		fnstd('SN','default',t15.ativo) as ope_centro2_ord_status_ativo_desc, 
		t15.sigla_ord_status as ope_centro2_ord_status_sigla,
		t15.tipo_status as ope_centro2_ord_status_tipo_status,

		t18.id as ope_centro_subgrupo_id_ord,
		t18.nome as ope_centro_subgrupo_nome_ord,
		t18.ativo as ope_centro_subgrupo_ativo_ord,
		fnstd('SN','default',t18.ativo) as ope_centro_subgrupo_ativo_desc_ord,
		t18.sigla_centro_subgrupo as ope_centro_subgrupo_sigla_ord,

		t19.id as ope_centro_grupo_id_ord,
		t19.nome as ope_centro_grupo_nome_ord,
		t19.ativo as ope_centro_grupo_ativo_ord,
		fnstd('SN','default',t19.ativo) as ope_centro_grupo_ativo_desc_ord,
		t19.sigla_centro_grupo as ope_centro_grupo_sigla_ord,

		t20.id as ope_centro_subtipo_id,
		t20.nome as ope_centro_subtipo_nome,
		t21.id as ope_centro_tipo_id,
		t21.nome as ope_centro_tipo_nome,
		t21.tipo_es as ope_centro_tipo_tipo_es,
		t1.log_user_ins,
		t1.log_date_ins,
		t1.log_user_upd,
		t1.log_date_upd,

		-- Siglas Desc
		t3.sigla_itemserv||' - '||t3.nome as  ger_itemserv_sigla_desc,
		t4.sigla_atividade||' - '||t4.nome as ope_atividade_sigla_desc,
		t6.sigla_empresa||' - '||t6.nome as ger_empresa_sigla_empresa_ord_desc,
		t7.sigla_periodo||' - '||t7.nome as ope_periodo_sigla_periodo_ord_desc,
		t9.sigla_centro2||' - '||t9.nome as ope_centro2_sigla_pessoa_ord_desc,
		t22.sigla_comp||' - '||t22.nome as ctb_sigla_desc,
		t11.sigla_pes||' - '||t11.nome as ger_pessoa_sigla_pes_desc,
		t12.sigla_ord_tipo||' - '||t12.nome as ope_centro2_ord_tipo_sigla_desc,
		t13.sigla_centro2||' - '||t13.nome as ope_centro2_sigla_centro2_ord_desc,
		t17.sigla_centro1||' - '||t17.nome as ope_centro1_sigla_ord_desc,
		t14.sigla_frente_trabalho||' - '||t14.nome as ope_frente_trabalho_sigla_ord_desc,
		t15.sigla_ord_status||' - '||t15.nome as ope_centro2_ord_status_sigla_desc,
		t18.sigla_centro_subgrupo||' - '||t18.nome as ope_centro_subgrupo_sigla_ord_desc,
		t19.sigla_centro_grupo||' - '||t19.nome as ope_centro_grupo_sigla_ord_desc

	FROM ope_centro2_ord_itemserv t1
	  left join ope_centro2_ord_ativ t2
	  on t1.ope_centro2_ord_ativ_id = t2.id
	  left join ger_itemserv t3
	  on  t3.id = t1.ger_itemserv_id
	  left join ope_atividade t4
	  on t2.ope_atividade_id = t4.id
	  left join ope_centro2_ord t5
	  on t2.ope_centro2_ord_id = t5.id
		left join  ger_empresa t6
		on t5.ger_empresa_id  = t6.id

		left join ope_periodo t7
		on t5.ope_periodo_id = t7.id

		left join ope_centro2_pessoa t8
		on t5.ope_centro2_pessoa_id_solic = t8.id

		left join ope_centro2 t9
		on t8.ope_centro2_id = t9.id

		left join ctb_comp t22
		on  t22.id = t9.ctb_comp_id

		left join ger_pessoa_endereco t10
		on  t5.ger_pessoa_endereco_id_exec = t10.id

		left join ger_pessoa t11
		on t10.ger_pessoa_id =  t11.id

		left join ope_centro2_ord_tipo t12
		on t5.ope_centro2_ord_tipo_id = t12.id

		left join ope_centro2 t13
		on t5.ope_centro2_id = t13.id

		left join ope_frente_trabalho t14
		on t5.ope_frente_trabalho_id = t14.id

		left join ope_centro2_ord_status t15
		on t5.ope_centro2_ord_status_id = t15.id

		left join ope_centro1 t17
		on t13.ope_centro1_id = t17.id


		left join ope_centro_subgrupo t18
		on t13.ope_centro_subgrupo_id = t18.id

		left join ope_centro_grupo t19
		on t18.ope_centro_grupo_id = t19.id

		left join ope_centro_subtipo t20
		on t17.ope_centro_subtipo_id = t20.id

		left join ope_centro_tipo t21
		on  t20.ope_centro_tipo_id = t21.id

		-- left join ope_centro_versao t16
		-- on  t5.ope_centro_versao_id = t16.id

		-- left join system_process_log t25
		-- on  t13.process_id = t25.id




	 
	 