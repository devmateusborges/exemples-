Drop VIEW IF EXISTS vwmov_mov_cotacao_anal;
CREATE OR REPLACE VIEW vwmov_mov_cotacao_anal AS
	select 	 
		t1.unit_id as mov_cot_anal_unit_id,
		t1.id as mov_cot_anal_id,
		t1.mov_id as mov_cot_anal_mov_id,
		t1.c01_ger_pessoa_id as mov_cot_anal_c01_ger_pessoa_id,
		t1.c01_ger_pessoa_endereco_id as mov_cot_anal_c01_ger_pessoa_endereco_id,
		t1.c01_observacao1 as mov_cot_anal_c01_observacao1,
		t1.c01_observacao2 as mov_cot_anal_c01_observacao2,
		t1.c01_qnt_cot as mov_cot_anal_c01_qnt_cot,
		t1.c01_valor_unit_cot as mov_cot_anal_c01_valor_unit_cot,
		t1.c01_valor_total_cot as mov_cot_anal_c01_valor_total_cot,
		t1.c01_valor_desc_cot as mov_cot_anal_c01_valor_desc_cot,
		t1.c01_valor_frete_cot as mov_cot_anal_c01_valor_frete_cot,
		t1.c01_valor_outro_cot as mov_cot_anal_c01_valor_outro_cot,
		t1.c01_valor_total_trib_cot as mov_cot_anal_c01_valor_total_trib_cot,
		t1.c01_status as mov_cot_anal_c01_status,
		t1.c01_data_status as mov_cot_anal_c01_data_status,
		t1.c01_system_user_id_aprov as mov_cot_anal_c01_system_user_id_aprov,
		--Ger Pessoa
		t3.id as c01_ger_pessoa_id,
		t3.nome as c01_ger_pessoa_nome,
		
		t3.ativo as c01_ger_pessoa_ativo,
		fnstd('SN','default',t3.ativo) as c01_ger_pessoa_ativo_desc,
	
		t3.doc_cpf as c01_ger_pessoa_doc_cpf,
		t3.doc_cnpj as c01_ger_pessoa_doc_cnpj,
		fnutil_formatcpfcnpj(t3.id, true) as c01_ger_pessoa_doc_cpf_cnpj_desc,
		t3.sigla_pes as c01_ger_pessoa_sigla,
		t3.fone_1||' - '||t3.contato_1 as c01_ger_pessoa_contato,
		-- Ger Pessoa Endereco
		t4.id as c01_ger_pessoa_endereco_id,
		t4.ger_pessoa_id as c01_ger_pessoa_endereco_pessoa_id,
		t4.ativo as c01_ger_pessoa_endereco_ativo,
		fnstd('SN','default',t4.ativo) as c01_ger_pessoa_endereco_ativo_desc,
		
		t4.tipo as c01_ger_pessoa_endereco_tipo,
		fnstd('ger_pessoa_endereco','tipo',t4.tipo) as c01_ger_pessoa_endereco_tipo_desc,
		
		t4.padrao as c01_ger_pessoa_endereco_padrao,
		fnstd('SN','default',t4.padrao) as c01_ger_pessoa_endereco_padrao_desc,
		t4.end_logradouro as c01_ger_pessoa_endereco_end_logradouro,
		t4.end_logradouro_nr as c01_ger_pessoa_endereco_end_logradouro_nr,
		t4.end_bairro as c01_ger_pessoa_endereco_end_bairro,
		t4.end_complemento as c01_ger_pessoa_endereco_end_complemento,
		t4.end_cep as c01_ger_pessoa_endereco_end_cep,
		t4.end_ger_cidade_id as c01_ger_pessoa_endereco_end_ger_cidade_id,
		---CondPagrec
		t35.id as c01_fin_cond_pagrec_id,
		t35.nome as c01_fin_cond_pagrec_nome,
		t35.sigla_cond_pagamento as c01_fin_cond_pagrec_sigla,
		-- System User
		t5.id as c01_system_user_id,
		t5.name as c01_system_user_name,
		t5.active as c01_system_user_active,
		fnstd('SN','default',t5.active) as c01_system_user_active_desc,

		t1.c02_ger_pessoa_id as mov_cot_anal_c02_ger_pessoa_id,
		t1.c02_ger_pessoa_endereco_id as mov_cot_anal_c02_ger_pessoa_endereco_id,
		t1.c02_observacao1 as mov_cot_anal_c02_observacao1,
		t1.c02_observacao2 as mov_cot_anal_c02_observacao2,
		t1.c02_qnt_cot as mov_cot_anal_c02_qnt_cot,
		t1.c02_valor_unit_cot as mov_cot_anal_c02_valor_unit_cot,
		t1.c02_valor_total_cot as mov_cot_anal_c02_valor_total_cot,
		t1.c02_valor_desc_cot as mov_cot_anal_c02_valor_desc_cot,
		t1.c02_valor_frete_cot as mov_cot_anal_c02_valor_frete_cot,
		t1.c02_valor_outro_cot as mov_cot_anal_c02_valor_outro_cot,
		t1.c02_valor_total_trib_cot as mov_cot_anal_c02_valor_total_trib_cot,
		t1.c02_status as mov_cot_anal_c02_status,
		t1.c02_data_status as mov_cot_anal_c02_data_status,
		t1.c02_system_user_id_aprov as mov_cot_anal_c02_system_user_id_aprov,
		--Ger Pessoa
		t6.id as c02_ger_pessoa_id,
		t6.nome as c02_ger_pessoa_nome,
		t6.ativo as c02_ger_pessoa_ativo,
		fnstd('SN','default',t6.ativo) as c02_ger_pessoa_ativo_desc,
		t6.doc_cpf as c02_ger_pessoa_doc_cpf,
		t6.doc_cnpj as c02_ger_pessoa_doc_cnpj,
		fnutil_formatcpfcnpj(t6.id, true) as c02_ger_pessoa_doc_cpf_cnpj_desc,
		t6.sigla_pes as c02_ger_pessoa_sigla,
		t6.fone_1||' - '||t6.contato_1 as c02_ger_pessoa_contato,

		-- Ger Pessoa Endereco
		t7.id as c02_ger_pessoa_endereco_id,
		t7.ger_pessoa_id as c02_ger_pessoa_endereco_pessoa_id,
		t7.ativo as c02_ger_pessoa_endereco_ativo,
		fnstd('SN','default',t7.ativo) as c02_ger_pessoa_endereco_ativo_desc,
		t7.tipo as c02_ger_pessoa_endereco_tipo,
		fnstd('ger_pessoa_endereco','tipo',t7.tipo) as c02_ger_pessoa_endereco_tipo_desc,
		t7.padrao as c02_ger_pessoa_endereco_padrao,
		fnstd('SN','default',t7.padrao) as c02_ger_pessoa_endereco_padrao_desc,
		t7.end_logradouro as c02_ger_pessoa_endereco_end_logradouro,
		t7.end_logradouro_nr as c02_ger_pessoa_endereco_end_logradouro_nr,
		t7.end_bairro as c02_ger_pessoa_endereco_end_bairro,
		t7.end_complemento as c02_ger_pessoa_endereco_end_complemento,
		t7.end_cep as c02_ger_pessoa_endereco_end_cep,
		t7.end_ger_cidade_id as c02_ger_pessoa_endereco_end_ger_cidade_id,
		---CondPagrec
		t36.id as c02_fin_cond_pagrec_id,
		t36.nome as c02_fin_cond_pagrec_nome,
		t36.sigla_cond_pagamento as c02_fin_cond_pagrec_sigla,
		
		-- System User
		t8.id as c02_system_user_id,
		t8.name as c02_system_user_name,
		t8.active as c02_system_user_active,
		fnstd('SN','default',t8.active) as c02_system_user_active_desc,

		t1.c03_ger_pessoa_id as mov_cot_anal_c03_ger_pessoa_id,
		t1.c03_ger_pessoa_endereco_id as mov_cot_anal_c03_ger_pessoa_endereco_id,
		t1.c03_observacao1 as mov_cot_anal_c03_observacao1,
		t1.c03_observacao2 as mov_cot_anal_c03_observacao2,
		t1.c03_qnt_cot as mov_cot_anal_c03_qnt_cot,
		t1.c03_valor_unit_cot as mov_cot_anal_c03_valor_unit_cot,
		t1.c03_valor_total_cot as mov_cot_anal_c03_valor_total_cot,
		t1.c03_valor_desc_cot as mov_cot_anal_c03_valor_desc_cot,
		t1.c03_valor_frete_cot as mov_cot_anal_c03_valor_frete_cot,
		t1.c03_valor_outro_cot as mov_cot_anal_c03_valor_outro_cot,
		t1.c03_valor_total_trib_cot as mov_cot_anal_c03_valor_total_trib_cot,
		t1.c03_status as mov_cot_anal_c03_status,
		t1.c03_data_status as mov_cot_anal_c03_data_status,
		t1.c03_system_user_id_aprov as mov_cot_anal_c03_system_user_id_aprov,
		--Ger Pessoa
		t9.id as c03_ger_pessoa_id,
		t9.nome as c03_ger_pessoa_nome,
		t9.ativo as c03_ger_pessoa_ativo,
		fnstd('SN','default',t9.ativo) as c03_ger_pessoa_ativo_desc,
		t9.doc_cpf as c03_ger_pessoa_doc_cpf,
		t9.doc_cnpj as c03_ger_pessoa_doc_cnpj,
		fnutil_formatcpfcnpj(t9.id, true) as c03_ger_pessoa_doc_cpf_cnpj_desc,
		t9.sigla_pes as c03_ger_pessoa_sigla,
		t9.fone_1||' - '||t9.contato_1 as c03_ger_pessoa_contato,

		-- Ger Pessoa Endereco
		t10.id as c03_ger_pessoa_endereco_id,
		t10.ger_pessoa_id as c03_ger_pessoa_endereco_pessoa_id,
		t10.ativo as c03_ger_pessoa_endereco_ativo,
		fnstd('SN','default',t10.ativo) as c03_ger_pessoa_endereco_ativo_desc,
		t10.tipo as c03_ger_pessoa_endereco_tipo,
		fnstd('ger_pessoa_endereco','tipo',t10.tipo) as c03_ger_pessoa_endereco_tipo_desc,
		t10.padrao as c03_ger_pessoa_endereco_padrao,
		fnstd('SN','default',t10.padrao) as c03_ger_pessoa_endereco_padrao_desc,
		t10.end_logradouro as c03_ger_pessoa_endereco_end_logradouro,
		t10.end_logradouro_nr as c03_ger_pessoa_endereco_end_logradouro_nr,
		t10.end_bairro as c03_ger_pessoa_endereco_end_bairro,
		t10.end_complemento as c03_ger_pessoa_endereco_end_complemento,
		t10.end_cep as c03_ger_pessoa_endereco_end_cep,
		t10.end_ger_cidade_id as c03_ger_pessoa_endereco_end_ger_cidade_id,
		---CondPagrec
		t37.id as c03_fin_cond_pagrec_id,
		t37.nome as c03_fin_cond_pagrec_nome,
		t37.sigla_cond_pagamento as c03_fin_cond_pagrec_sigla,		
		-- System User
		t11.id as c03_system_user_id,
		t11.name as c03_system_user_name,
		t11.active as c03_system_user_active,
		fnstd('SN','default',t11.active) as c03_system_user_active_desc,

		t1.c04_ger_pessoa_id as mov_cot_anal_c04_ger_pessoa_id,
		t1.c04_ger_pessoa_endereco_id as mov_cot_anal_c04_ger_pessoa_endereco_id,
		t1.c04_observacao1 as mov_cot_anal_c04_observacao1,
		t1.c04_observacao2 as mov_cot_anal_c04_observacao2,
		t1.c04_qnt_cot as mov_cot_anal_c04_qnt_cot,
		t1.c04_valor_unit_cot as mov_cot_anal_c04_valor_unit_cot,
		t1.c04_valor_total_cot as mov_cot_anal_c04_valor_total_cot,
		t1.c04_valor_desc_cot as mov_cot_anal_c04_valor_desc_cot,
		t1.c04_valor_frete_cot as mov_cot_anal_c04_valor_frete_cot,
		t1.c04_valor_outro_cot as mov_cot_anal_c04_valor_outro_cot,
		t1.c04_valor_total_trib_cot as mov_cot_anal_c04_valor_total_trib_cot,
		t1.c04_status as mov_cot_anal_c04_status,
		t1.c04_data_status as mov_cot_anal_c04_data_status,
		t1.c04_system_user_id_aprov as mov_cot_anal_c04_system_user_id_aprov,
		--Ger Pessoa
		t12.id as c04_ger_pessoa_id,
		t12.nome as c04_ger_pessoa_nome,
		t12.ativo as c04_ger_pessoa_ativo,
		fnstd('SN','default',t12.ativo) as c04_ger_pessoa_ativo_desc,
		t12.doc_cpf as c04_ger_pessoa_doc_cpf,
		t12.doc_cnpj as c04_ger_pessoa_doc_cnpj,
		fnutil_formatcpfcnpj(t12.id, true) as c04_ger_pessoa_doc_cpf_cnpj_desc,
		t12.sigla_pes as c04_ger_pessoa_sigla,
		t12.fone_1||' - '||t12.contato_1 as c04_ger_pessoa_contato,
		
		-- Ger Pessoa Endereco
		t13.id as c04_ger_pessoa_endereco_id,
		t13.ger_pessoa_id as c04_ger_pessoa_endereco_pessoa_id,
		t13.ativo as c04_ger_pessoa_endereco_ativo,
		fnstd('SN','default',t13.ativo) as c04_ger_pessoa_endereco_ativo_desc,
		t13.tipo as c04_ger_pessoa_endereco_tipo,
		fnstd('ger_pessoa_endereco','tipo',t13.tipo) as c04_ger_pessoa_endereco_tipo_desc,
		t13.padrao as c04_ger_pessoa_endereco_padrao,
		fnstd('SN','default',t13.padrao) as c04_ger_pessoa_endereco_padrao_desc,
		t13.end_logradouro as c04_ger_pessoa_endereco_end_logradouro,
		t13.end_logradouro_nr as c04_ger_pessoa_endereco_end_logradouro_nr,
		t13.end_bairro as c04_ger_pessoa_endereco_end_bairro,
		t13.end_complemento as c04_ger_pessoa_endereco_end_complemento,
		t13.end_cep as c04_ger_pessoa_endereco_end_cep,
		t13.end_ger_cidade_id as c04_ger_pessoa_endereco_end_ger_cidade_id,
		---CondPagrec
		t38.id as c04_fin_cond_pagrec_id,
		t38.nome as c04_fin_cond_pagrec_nome,
		t38.sigla_cond_pagamento as c04_fin_cond_pagrec_sigla,
		
		-- System User
		t14.id as c04_system_user_id,
		t14.name as c04_system_user_name,
		t14.active as c04_system_user_active,
		fnstd('SN','default',t14.active) as c04_system_user_active_desc,

		t1.c05_ger_pessoa_id as mov_cot_anal_c05_ger_pessoa_id,
		t1.c05_ger_pessoa_endereco_id as mov_cot_anal_c05_ger_pessoa_endereco_id,
		t1.c05_observacao1 as mov_cot_anal_c05_observacao1,
		t1.c05_observacao2 as mov_cot_anal_c05_observacao2,
		t1.c05_qnt_cot as mov_cot_anal_c05_qnt_cot,
		t1.c05_valor_unit_cot as mov_cot_anal_c05_valor_unit_cot,
		t1.c05_valor_total_cot as mov_cot_anal_c05_valor_total_cot,
		t1.c05_valor_desc_cot as mov_cot_anal_c05_valor_desc_cot,
		t1.c05_valor_frete_cot as mov_cot_anal_c05_valor_frete_cot,
		t1.c05_valor_outro_cot as mov_cot_anal_c05_valor_outro_cot,
		t1.c05_valor_total_trib_cot as mov_cot_anal_c05_valor_total_trib_cot,
		t1.c05_status as mov_cot_anal_c05_status,
		t1.c05_data_status as mov_cot_anal_c05_data_status,
		t1.c05_system_user_id_aprov as mov_cot_anal_c05_system_user_id_aprov,

		--Ger Pessoa
		t15.id as c05_ger_pessoa_id,
		t15.nome as c05_ger_pessoa_nome,
		t15.ativo as c05_ger_pessoa_ativo,
		fnstd('SN','default',t15.ativo) as c05_ger_pessoa_ativo_desc,
		t15.doc_cpf as c05_ger_pessoa_doc_cpf,
		t15.doc_cnpj as c05_ger_pessoa_doc_cnpj,
		fnutil_formatcpfcnpj(t15.id, true) as c05_ger_pessoa_doc_cpf_cnpj_desc,
		t15.sigla_pes as c05_ger_pessoa_sigla,
		t15.fone_1||' - '||t15.contato_1 as c05_ger_pessoa_contato,

		-- Ger Pessoa Endereco
		t16.id as c05_ger_pessoa_endereco_id,
		t16.ger_pessoa_id as c05_ger_pessoa_endereco_pessoa_id,
		t16.ativo as c05_ger_pessoa_endereco_ativo,
		fnstd('SN','default',t16.ativo) as c05_ger_pessoa_endereco_ativo_desc,
		t16.tipo as c05_ger_pessoa_endereco_tipo,
		fnstd('ger_pessoa_endereco','tipo',t16.tipo) as c05_ger_pessoa_endereco_tipo_desc,
		t16.padrao as c05_ger_pessoa_endereco_padrao,
		fnstd('SN','default',t16.padrao) as c05_ger_pessoa_endereco_padrao_desc,
		t16.end_logradouro as c05_ger_pessoa_endereco_end_logradouro,
		t16.end_logradouro_nr as c05_ger_pessoa_endereco_end_logradouro_nr,
		t16.end_bairro as c05ger_pessoa_endereco_end_bairro,
		t16.end_complemento as c05_ger_pessoa_endereco_end_complemento,
		t16.end_cep as c05_ger_pessoa_endereco_end_cep,
		t16.end_ger_cidade_id as c05_ger_pessoa_endereco_end_ger_cidade_id,
		---CondPagrec
		t39.id as c05_fin_cond_pagrec_id,
		t39.nome as c05_fin_cond_pagrec_nome,
		t39.sigla_cond_pagamento as c05_fin_cond_pagrec_sigla,
		-- System User
		t17.id as c05_system_user_id,
		t17.name as c05_system_user_name,
		t17.active as c05_system_user_active,
		fnstd('SN','default',t17.active) as c05_system_user_active_desc,


		t1.c06_ger_pessoa_id as mov_cot_anal_c06_ger_pessoa_id,
		t1.c06_ger_pessoa_endereco_id as mov_cot_anal_c06_ger_pessoa_endereco_id,
		t1.c06_observacao1 as mov_cot_anal_c06_observacao1,
		t1.c06_observacao2 as mov_cot_anal_c06_observacao2,
		t1.c06_qnt_cot as mov_cot_anal_c06_qnt_cot,
		t1.c06_valor_unit_cot as mov_cot_anal_c06_valor_unit_cot,
		t1.c06_valor_total_cot as mov_cot_anal_c06_valor_total_cot,
		t1.c06_valor_desc_cot as mov_cot_anal_c06_valor_desc_cot,
		t1.c06_valor_frete_cot as mov_cot_anal_c06_valor_frete_cot,
		t1.c06_valor_outro_cot as mov_cot_anal_c06_valor_outro_cot,
		t1.c06_valor_total_trib_cot as mov_cot_anal_c06_valor_total_trib_cot,
		t1.c06_status as mov_cot_anal_c06_status,
		t1.c06_data_status as mov_cot_anal_c06_data_status,
		t1.c06_system_user_id_aprov as mov_cot_anal_c06_system_user_id_aprov,

		--Ger Pessoa
		t18.id as c06_ger_pessoa_id,
		t18.nome as c06_ger_pessoa_nome,
		t18.ativo as c06_ger_pessoa_ativo,
		fnstd('SN','default',t18.ativo) as c06_ger_pessoa_ativo_desc,
		t18.doc_cpf as c06_ger_pessoa_doc_cpf,
		t18.doc_cnpj as c06_ger_pessoa_doc_cnpj,
		fnutil_formatcpfcnpj(t18.id, true) as c06_ger_pessoa_doc_cpf_cnpj_desc,
		t18.sigla_pes as c06_ger_pessoa_sigla,
		t18.fone_1||' - '||t18.contato_1 as c06_ger_pessoa_contato,

		-- Ger Pessoa Endereco
		t19.id as c06_ger_pessoa_endereco_id,
		t19.ger_pessoa_id as c06_ger_pessoa_endereco_pessoa_id,
		t19.ativo as c06_ger_pessoa_endereco_ativo,
		fnstd('SN','default',t19.ativo) as c06_ger_pessoa_endereco_ativo_desc,
		t19.tipo as c06_ger_pessoa_endereco_tipo,
		fnstd('ger_pessoa_endereco','tipo',t19.tipo) as c06_ger_pessoa_endereco_tipo_desc,
		t19.padrao as c06_ger_pessoa_endereco_padrao,
		fnstd('SN','default',t19.padrao) as c06_ger_pessoa_endereco_padrao_desc,
		t19.end_logradouro as c06_ger_pessoa_endereco_end_logradouro,
		t19.end_logradouro_nr as c06_ger_pessoa_endereco_end_logradouro_nr,
		t19.end_bairro as c06ger_pessoa_endereco_end_bairro,
		t19.end_complemento as c06_ger_pessoa_endereco_end_complemento,
		t19.end_cep as c06_ger_pessoa_endereco_end_cep,
		t19.end_ger_cidade_id as c06_ger_pessoa_endereco_end_ger_cidade_id,
		---CondPagrec
		t40.id as c06_fin_cond_pagrec_id,
		t40.nome as c06_fin_cond_pagrec_nome,
		t40.sigla_cond_pagamento as c06_fin_cond_pagrec_sigla,
		-- System User
		t20.id as c06_system_user_id,
		t20.name as c06_system_user_name,
		t20.active as c06_system_user_active,
		fnstd('SN','default',t20.active) as c06_system_user_active_desc,

		t1.c07_ger_pessoa_id as mov_cot_anal_c07_ger_pessoa_id,
		t1.c07_ger_pessoa_endereco_id as mov_cot_anal_c07_ger_pessoa_endereco_id,
		t1.c07_observacao1 as mov_cot_anal_c07_observacao1,
		t1.c07_observacao2 as mov_cot_anal_c07_observacao2,
		t1.c07_qnt_cot as mov_cot_anal_c07_qnt_cot,
		t1.c07_valor_unit_cot as mov_cot_anal_c07_valor_unit_cot,
		t1.c07_valor_total_cot as mov_cot_anal_c07_valor_total_cot,
		t1.c07_valor_desc_cot as mov_cot_anal_c07_valor_desc_cot,
		t1.c07_valor_frete_cot as mov_cot_anal_c07_valor_frete_cot,
		t1.c07_valor_outro_cot as mov_cot_anal_c07_valor_outro_cot,
		t1.c07_valor_total_trib_cot as mov_cot_anal_c07_valor_total_trib_cot,
		t1.c07_status as mov_cot_anal_c07_status,
		t1.c07_data_status as mov_cot_anal_c07_data_status,
		t1.c07_system_user_id_aprov as mov_cot_anal_c07_system_user_id_aprov,

		--Ger Pessoa
		t21.id as c07_ger_pessoa_id,
		t21.nome as c07_ger_pessoa_nome,
		t21.ativo as c07_ger_pessoa_ativo,
		fnstd('SN','default',t21.ativo) as c07_ger_pessoa_ativo_desc,
		t21.doc_cpf as c07_ger_pessoa_doc_cpf,
		t21.doc_cnpj as c07_ger_pessoa_doc_cnpj,
		fnutil_formatcpfcnpj(t21.id, true) as c07_ger_pessoa_doc_cpf_cnpj_desc,
		t21.sigla_pes as c07_ger_pessoa_sigla,
		t21.fone_1||' - '||t21.contato_1 as c07_ger_pessoa_contato,

		-- Ger Pessoa Endereco
		t22.id as c07_ger_pessoa_endereco_id,
		t22.ger_pessoa_id as c07_ger_pessoa_endereco_pessoa_id,
		t22.ativo as c07_ger_pessoa_endereco_ativo,
		fnstd('SN','default',t22.ativo) as c07_ger_pessoa_endereco_ativo_desc,
		t22.tipo as c07_ger_pessoa_endereco_tipo,
		fnstd('ger_pessoa_endereco','tipo',t22.tipo) as c07_ger_pessoa_endereco_tipo_desc,
		t22.padrao as c07_ger_pessoa_endereco_padrao,
		fnstd('SN','default',t22.padrao) as c07_ger_pessoa_endereco_padrao_desc,
		t22.end_logradouro as c07_ger_pessoa_endereco_end_logradouro,
		t22.end_logradouro_nr as c07_ger_pessoa_endereco_end_logradouro_nr,
		t22.end_bairro as c07_ger_pessoa_endereco_end_bairro,
		t22.end_complemento as c07_ger_pessoa_endereco_end_complemento,
		t22.end_cep as c07_ger_pessoa_endereco_end_cep,
		t22.end_ger_cidade_id as c07_ger_pessoa_endereco_end_ger_cidade_id,
		---CondPagrec
		t41.id as c07_fin_cond_pagrec_id,
		t41.nome as c07_fin_cond_pagrec_nome,
		t41.sigla_cond_pagamento as c07_fin_cond_pagrec_sigla,
		-- System User
		t23.id as c07_system_user_id,
		t23.name as c07_system_user_name,
		t23.active as c07_system_user_active,
		fnstd('SN','default',t23.active) as c07_system_user_active_desc,

		t1.c08_ger_pessoa_id as mov_cot_anal_c08_ger_pessoa_id,
		t1.c08_ger_pessoa_endereco_id as mov_cot_anal_c08_ger_pessoa_endereco_id,
		t1.c08_observacao1 as mov_cot_anal_c08_observacao1,
		t1.c08_observacao2 as mov_cot_anal_c08_observacao2,
		t1.c08_qnt_cot as mov_cot_anal_c08_qnt_cot,
		t1.c08_valor_unit_cot as mov_cot_anal_c08_valor_unit_cot,
		t1.c08_valor_total_cot as mov_cot_anal_c08_valor_total_cot,
		t1.c08_valor_desc_cot as mov_cot_anal_c08_valor_desc_cot,
		t1.c08_valor_frete_cot as mov_cot_anal_c08_valor_frete_cot,
		t1.c08_valor_outro_cot as mov_cot_anal_c08_valor_outro_cot,
		t1.c08_valor_total_trib_cot as mov_cot_anal_c08_valor_total_trib_cot,
		t1.c08_status as mov_cot_anal_c08_status,
		t1.c08_data_status as mov_cot_anal_c08_data_status,
		t1.c08_system_user_id_aprov as mov_cot_anal_c08_system_user_id_aprov,
		--Ger Pessoa
		t24.id as c08_ger_pessoa_id,
		t24.nome as c08_ger_pessoa_nome,
		t24.ativo as c08_ger_pessoa_ativo,
		fnstd('SN','default',t24.ativo) as c08_ger_pessoa_ativo_desc,
		t24.doc_cpf as c08_ger_pessoa_doc_cpf,
		t24.doc_cnpj as c08_ger_pessoa_doc_cnpj,		
		fnutil_formatcpfcnpj(t24.id, true) as c08_ger_pessoa_doc_cpf_cnpj_desc,
		t24.sigla_pes as c08_ger_pessoa_sigla,
		t24.fone_1||' - '||t24.contato_1 as c08_ger_pessoa_contato,	

		-- Ger Pessoa Endereco
		t25.id as c08_ger_pessoa_endereco_id,
		t25.ger_pessoa_id as c08_ger_pessoa_endereco_pessoa_id,
		t25.ativo as c08_ger_pessoa_endereco_ativo,
		fnstd('SN','default',t25.ativo) as c08_ger_pessoa_endereco_ativo_desc,
		t25.tipo as c08_ger_pessoa_endereco_tipo,
		fnstd('ger_pessoa_endereco','tipo',t25.tipo) as c08_ger_pessoa_endereco_tipo_desc,
		t25.padrao as c08_ger_pessoa_endereco_padrao,
		fnstd('SN','default',t25.padrao) as c08_ger_pessoa_endereco_padrao_desc,
		t25.end_logradouro as c08_ger_pessoa_endereco_end_logradouro,
		t25.end_logradouro_nr as c08_ger_pessoa_endereco_end_logradouro_nr,
		t25.end_bairro as c08_ger_pessoa_endereco_end_bairro,
		t25.end_complemento as c08_ger_pessoa_endereco_end_complemento,
		t25.end_cep as c08_ger_pessoa_endereco_end_cep,
		t25.end_ger_cidade_id as c08_ger_pessoa_endereco_end_ger_cidade_id,
		---CondPagrec
		t42.id as c08_fin_cond_pagrec_id,
		t42.nome as c08_fin_cond_pagrec_nome,
		t42.sigla_cond_pagamento as c08_fin_cond_pagrec_sigla,
		-- System User
		t26.id as c08_system_user_id,
		t26.name as c08_system_user_name,
		t26.active as c08_system_user_active,
		fnstd('SN','default',t26.active) as c08_system_user_active_desc,


		t1.c09_ger_pessoa_id as mov_cot_anal_c09_ger_pessoa_id,
		t1.c09_ger_pessoa_endereco_id as mov_cot_anal_c09_ger_pessoa_endereco_id,
		t1.c09_observacao1 as mov_cot_anal_c09_observacao1,
		t1.c09_observacao2 as mov_cot_anal_c09_observacao2,
		t1.c09_qnt_cot as mov_cot_anal_c09_qnt_cot,
		t1.c09_valor_unit_cot as mov_cot_anal_c09_valor_unit_cot,
		t1.c09_valor_total_cot as mov_cot_anal_c09_valor_total_cot,
		t1.c09_valor_desc_cot as mov_cot_anal_c09_valor_desc_cot,
		t1.c09_valor_frete_cot as mov_cot_anal_c09_valor_frete_cot,
		t1.c09_valor_outro_cot as mov_cot_anal_c09_valor_outro_cot,
		t1.c09_valor_total_trib_cot as mov_cot_anal_c09_valor_total_trib_cot,
		t1.c09_status as mov_cot_anal_c09_status,
		t1.c09_data_status as mov_cot_anal_c09_data_status,
		t1.c09_system_user_id_aprov as mov_cot_anal_c09_system_user_id_aprov,
		--Ger Pessoa
		t27.id as c09_ger_pessoa_id,
		t27.nome as c09_ger_pessoa_nome,
		t27.ativo as c09_ger_pessoa_ativo,
		fnstd('SN','default',t27.ativo) as c09_ger_pessoa_ativo_desc,
		t27.doc_cpf as c09_ger_pessoa_doc_cpf,
		t27.doc_cnpj as c09_ger_pessoa_doc_cnpj,
		fnutil_formatcpfcnpj(t27.id, true) as c09_ger_pessoa_doc_cpf_cnpj_desc,
		t27.sigla_pes as c09_ger_pessoa_sigla,
		t27.fone_1||' - '||t27.contato_1 as c09_ger_pessoa_contato,

		-- Ger Pessoa Endereco
		t28.id as c09_ger_pessoa_endereco_id,
		t28.ger_pessoa_id as c09_ger_pessoa_endereco_pessoa_id,
		t28.ativo as c09_ger_pessoa_endereco_ativo,
		fnstd('SN','default',t28.ativo) as c09_ger_pessoa_endereco_ativo_desc,
		t28.tipo as c09_ger_pessoa_endereco_tipo,
		fnstd('ger_pessoa_endereco','tipo',t28.tipo) as c09_ger_pessoa_endereco_tipo_desc,
		t28.padrao as c09_ger_pessoa_endereco_padrao,
		fnstd('SN','default',t28.padrao) as c09_ger_pessoa_endereco_padrao_desc,
		t28.end_logradouro as c09_ger_pessoa_endereco_end_logradouro,
		t28.end_logradouro_nr as c09_ger_pessoa_endereco_end_logradouro_nr,
		t28.end_bairro as c09_ger_pessoa_endereco_end_bairro,
		t28.end_complemento as c09_ger_pessoa_endereco_end_complemento,
		t28.end_cep as c09_ger_pessoa_endereco_end_cep,
		t28.end_ger_cidade_id as c09_ger_pessoa_endereco_end_ger_cidade_id,
		---CondPagrec
		t43.id as c09_fin_cond_pagrec_id,
		t43.nome as c09_fin_cond_pagrec_nome,
		t43.sigla_cond_pagamento as c09_fin_cond_pagrec_sigla,
		-- System User
		t29.id as c09_system_user_id,
		t29.name as c09_system_user_name,
		t29.active as c09_system_user_active,
		fnstd('SN','default',t29.active) as c09_system_user_active_desc,

		t1.c10_ger_pessoa_id as mov_cot_anal_c10_ger_pessoa_id,
		t1.c10_ger_pessoa_endereco_id as mov_cot_anal_c10_ger_pessoa_endereco_id,
		t1.c10_observacao1 as mov_cot_anal_c10_observacao1,
		t1.c10_observacao2 as mov_cot_anal_c10_observacao2,
		t1.c10_qnt_cot as mov_cot_anal_c10_qnt_cot,
		t1.c10_valor_unit_cot as mov_cot_anal_c10_valor_unit_cot,
		t1.c10_valor_total_cot as mov_cot_anal_c10_valor_total_cot,
		t1.c10_valor_desc_cot as mov_cot_anal_c10_valor_desc_cot,
		t1.c10_valor_frete_cot as mov_cot_anal_c10_valor_frete_cot,
		t1.c10_valor_outro_cot as mov_cot_anal_c10_valor_outro_cot,
		t1.c10_valor_total_trib_cot as mov_cot_anal_c10_valor_total_trib_cot,
		t1.c10_status as mov_cot_anal_c10_status,
		t1.c10_data_status as mov_cot_anal_c10_data_status,
		t1.c10_system_user_id_aprov as mov_cot_anal_c10_system_user_id_aprov,
		t1.ger_itemserv_id as mov_cot_anal_ger_itemserv_id,
		--Ger Pessoa
		t30.id as c10_ger_pessoa_id,
		t30.nome as c10_ger_pessoa_nome,
		t30.ativo as c10_ger_pessoa_ativo,
		fnstd('SN','default',t30.ativo) as c10_ger_pessoa_ativo_desc,
		t30.doc_cpf as c10_ger_pessoa_doc_cpf,
		t30.doc_cnpj as c10_ger_pessoa_doc_cnpj,		
		fnutil_formatcpfcnpj(t30.id, true) as c10_ger_pessoa_doc_cpf_cnpj_desc,
		t30.sigla_pes as c10_ger_pessoa_sigla,
		t30.fone_1||' - '||t30.contato_1 as c10_ger_pessoa_contato,		

		-- Ger Pessoa Endereco
		t31.id as c10_ger_pessoa_endereco_id,
		t31.ger_pessoa_id as c10_ger_pessoa_endereco_pessoa_id,
		t31.ativo as c10_ger_pessoa_endereco_ativo,
		fnstd('SN','default',t31.ativo) as c10_ger_pessoa_endereco_ativo_desc,
		t31.tipo as c10_ger_pessoa_endereco_tipo,
		fnstd('ger_pessoa_endereco','tipo',t31.tipo) as c10_ger_pessoa_endereco_tipo_desc,
		t31.padrao as c10_ger_pessoa_endereco_padrao,
		fnstd('SN','default',t31.padrao) as c10_ger_pessoa_endereco_padrao_desc,
		t31.end_logradouro as c10_ger_pessoa_endereco_end_logradouro,
		t31.end_logradouro_nr as c10_ger_pessoa_endereco_end_logradouro_nr,
		t31.end_bairro as c10_ger_pessoa_endereco_end_bairro,
		t31.end_complemento as c10_ger_pessoa_endereco_end_complemento,
		t31.end_cep as c10_ger_pessoa_endereco_end_cep,
		t31.end_ger_cidade_id as c10_ger_pessoa_endereco_end_ger_cidade_id,
		---CondPagrec
		t44.id as c10_fin_cond_pagrec_id,
		t44.nome as c10_fin_cond_pagrec_nome,
		t44.sigla_cond_pagamento as c10_fin_cond_pagrec_sigla,
		-- System User
		t32.id as c10_system_user_id,
		t32.name as c10_system_user_name,
		t32.active as c10_system_user_active,
		fnstd('SN','default',t32.active) as c10_system_user_active_desc,

		--Mov
		t2.id as mov_id,
		t2.nr_externo as mov_nr_externo,
		t2.data_mov as mov_data_mov,
		t2.numero_mov as mov_numero_mov,
		t2.data_emissao as mov_data_emissao,
		t2.serie_mov as mov_serie_mov,
		t2.valor_total as mov_valor_total,
		t2.observacao as mov_obs,
		t2.tipo_frete as mov_tipo_frete,
		fnstd('mov','tipo_frete',(t2.tipo_frete)::VARCHAR) as mov_tipo_frete_desc,
		t2.data_entrega as mov_data_entrega,
		t2.data_entrada_saida as mov_data_entrada_saida,
		t2.tipo_emissao_carga as mov_tipo_emissao_carga,
		fnstd('mov','tipo_emissao_carga',(t2.tipo_emissao_carga)::VARCHAR) as mov_tipo_emissao_carga_desc,
		t2.tipo_modal_carga as mov_tipo_modal_carga,
		t2.tipo_transportador_carga as mov_tipo_transportador_carga,
		t2.valor_carga as mov_valor_carga,
		t2.tipo_umedida_carga as mov_tipo_umedida_carga,
		fnstd('mov','tipo_umedida_carga',t2.tipo_umedida_carga) as mov_tipo_umedida_carga_desc,
		t2.qnt_carga as mov_qnt_carga,
		t2.observacao_transp as mov_obs_transp,
		t2.observacao_serv as mov_obs_serv,
		t2.tipo_fretamento as mov_tipo_fretamenti,
		t2.tipo_serv_frete as mov_tipo_serv_frete,
		t2.tipo_tomador_serv_frete as mov_tipo_tomador_serv_frete,
		t2.taf as mov_taf,
		t2.data_anulacao as mov_data_anulacao,
		t2.observacao_item as mov_obs_item,
		t2.valor_financeiro_total as mov_valor_financeiro_total,
		t2.valor_item_frete_total as mov_valor_item_frete_total,
		t2.observacao_fiscal as mov_obs_fiscal,
		t2.fis_tipo_resp_reten as mov_fis_tipo_resp_reten,
		fnstd('mov','fis_tipo_resp_reten',t2.fis_tipo_resp_reten) as mov_fis_tipo_resp_reten_desc,
		t2.fis_exig_iss_nfs as mov_fis_exig_iss_nfs,
		fnstd('mov','fis_exig_iss_nfs',t2.fis_exig_iss_nfs) as mov_fis_exig_iss_nfs_desc,
		t2.fis_iss_retido_nfs as mov_fis_iss_retido_nfs,
		fnstd('SN','default',t2.fis_iss_retido_nfs) as mov_fis_iss_retido_nfs_desc,
		t2.fis_nat_ope_nfs as mov_fis_nat_ope_nfs,
		fnstd('mov','fis_nat_ope_nfs',t2.fis_nat_ope_nfs) as mov_fis_nat_ope_nfs_desc,
		t2.numero_mov_pre as mov_numero_mov_pre,
		t2.serio_mov_pre as mov_serio_mov_pre,
		t2.cep_carreg as mov_cep_carreg,
		t2.cep_descarreg as mov_cep_descarreg,
		t2.tipo_carga as mov_tipo_carga,
		fnstd('mov','tipo_carga',t2.tipo_carga) as mov_tipo_carga_desc,

		-- Item/Serv
		t33.id as ger_itemserv_id,
		t33.nome as ger_itemserv_nome,
		t33.ativo as ger_itemserv_ativo,
		fnstd('SN','default',t33.ativo) as ger_itemserv_ativo_desc,
		t33.sigla_itemserv as ger_itemserv_sigla,
		t33.tipo as ger_itemserv_tipo,
		fnstd('ger_itemserv','tipo',t33.tipo) as ger_itemserv_tipo_desc,

		-- GerUmedidaItemServ
		t34.id as ger_umedida_itemserv_id,
		t34.nome as ger_umedida_itemserv_nome,
		t34.sigla_umedida as ger_umedida_itemserv_sigla,
		t34.ativo as ger_umedida_itemserv_ativo,
		
		
		t1.log_user_ins,
		t1.log_date_ins,
		t1.log_user_upd,
		t1.log_date_upd,

		-- Sigla desc

		t3.sigla_pes||' - '||t3.nome as c01_ger_pessoa_sigla_desc,
		t6.sigla_pes||' - '||t6.nome as c02_ger_pessoa_sigla_desc,
		t9.sigla_pes||' - '||t9.nome as c03_ger_pessoa_sigla_desc,
		t12.sigla_pes||' - '||t12.nome as c04_ger_pessoa_sigla_desc,
		t15.sigla_pes||' - '||t15.nome as c05_ger_pessoa_sigla_desc,
		t18.sigla_pes||' - '||t18.nome as c06_ger_pessoa_sigla_desc,
		t21.sigla_pes||' - '||t21.nome as c07_ger_pessoa_sigla_desc,
		t24.sigla_pes||' - '||t24.nome as c08_ger_pessoa_sigla_desc,
		t27.sigla_pes||' - '||t27.nome as c09_ger_pessoa_sigla_desc,
		t30.sigla_pes||' - '||t30.nome as c10_ger_pessoa_sigla_desc,
		t33.sigla_itemserv||' - '||t33.nome as ger_itemserv_sigla_desc


	from mov_cotacao_anal t1
		inner join mov t2
		on t1.mov_id = t2.id
		-- C01
		inner join ger_pessoa t3
		on t1.c01_ger_pessoa_id = t3.id
		inner join ger_pessoa_endereco t4
		on t1.c01_ger_pessoa_endereco_id = t4.id
		left join system_user t5
		on  t1.c01_system_user_id_aprov = t5.id
		-- C02
		left join ger_pessoa t6
		on t1.c02_ger_pessoa_id = t6.id

		left join ger_pessoa_endereco t7
		on t1.c02_ger_pessoa_endereco_id = t7.id

		left join system_user t8
		on t1.c02_system_user_id_aprov = t8.id
		-- C03
		left join ger_pessoa t9
		on t1.c03_ger_pessoa_id = t9.id

		left join ger_pessoa_endereco t10
		on t1.c03_ger_pessoa_endereco_id = t10.id

		left join system_user t11
		on t1.c03_system_user_id_aprov = t11.id
		-- C04
		left join ger_pessoa t12
		on t1.c04_ger_pessoa_id = t12.id

		left join ger_pessoa_endereco t13
		on t1.c04_ger_pessoa_endereco_id = t13.id

		left join system_user t14
		on t1.c04_system_user_id_aprov = t14.id
		-- C05
		left join ger_pessoa t15
		on t1.c05_ger_pessoa_id = t15.id

		left join ger_pessoa_endereco t16
		on t1.c05_ger_pessoa_endereco_id = t16.id

		left join system_user t17
		on t1.c05_system_user_id_aprov = t17.id
		-- C06
		left join ger_pessoa t18
		on t1.c06_ger_pessoa_id = t18.id

		left join ger_pessoa_endereco t19
		on t1.c06_ger_pessoa_endereco_id = t19.id

		left join system_user t20
		on t1.c06_system_user_id_aprov = t20.id
		-- C07
		left join ger_pessoa t21
		on t1.c07_ger_pessoa_id = t21.id

		left join ger_pessoa_endereco t22
		on t1.c07_ger_pessoa_endereco_id = t22.id

		left join system_user t23
		on t1.c07_system_user_id_aprov = t23.id
		-- C08
		left join ger_pessoa t24
		on t1.c08_ger_pessoa_id = t24.id

		left join ger_pessoa_endereco t25
		on t1.c08_ger_pessoa_endereco_id = t25.id

		left join system_user t26
		on t1.c08_system_user_id_aprov = t26.id

		-- C09
		left join ger_pessoa t27
		on t1.c09_ger_pessoa_id = t27.id

		left join ger_pessoa_endereco t28
		on t1.c09_ger_pessoa_endereco_id = t28.id

		left join system_user t29
		on t1.c09_system_user_id_aprov = t29.id

		-- C10
		left join ger_pessoa t30
		on t1.c10_ger_pessoa_id = t30.id

		left join ger_pessoa_endereco t31
		on t1.c10_ger_pessoa_endereco_id = t31.id

		left join system_user t32
		on t1.c10_system_user_id_aprov = t32.id

		-- Item/Serv
		inner join ger_itemserv t33
		on  t1.ger_itemserv_id = t33.id
		-- Umedida Item/Serv
		inner join ger_umedida t34
		on t33.ger_umedida_id = t34.id
		
		--Cond Pagrec 01
		left join fin_cond_pagrec t35
		on t1.c01_fin_cond_pagrec_id = t35.id
		--Cond Pagrec 02
		left join fin_cond_pagrec t36
		on t1.c02_fin_cond_pagrec_id = t36.id		
		--Cond Pagrec 03
		left join fin_cond_pagrec t37
		on t1.c03_fin_cond_pagrec_id = t37.id				
		--Cond Pagrec 04
		left join fin_cond_pagrec t38
		on t1.c04_fin_cond_pagrec_id = t38.id						
		--Cond Pagrec 05
		left join fin_cond_pagrec t39
		on t1.c05_fin_cond_pagrec_id = t39.id								
		--Cond Pagrec 06
		left join fin_cond_pagrec t40
		on t1.c06_fin_cond_pagrec_id = t40.id
		--Cond Pagrec 07
		left join fin_cond_pagrec t41
		on t1.c07_fin_cond_pagrec_id = t41.id
		--Cond Pagrec 08
		left join fin_cond_pagrec t42
		on t1.c08_fin_cond_pagrec_id = t42.id
		--Cond Pagrec 09
		left join fin_cond_pagrec t43
		on t1.c09_fin_cond_pagrec_id = t43.id		
		--Cond Pagrec 10
		left join fin_cond_pagrec t44
		on t1.c10_fin_cond_pagrec_id = t44.id