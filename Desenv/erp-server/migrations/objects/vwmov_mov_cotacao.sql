Drop VIEW IF EXISTS vwmov_mov_cotacao;
CREATE OR REPLACE VIEW vwmov_mov_cotacao AS
	select 
		t1.unit_id as mov_cotacao_unit_id,
		t1.id as mov_cotacao_id,
		t1.mov_id as mov_cotacao_mov_id,
		t1.ger_pessoa_id as mov_cotacao_ger_pessoa_id,
		t1.ger_pessoa_endereco_id as mov_cotacao_ger_pessoa_endereco_id,
		t1.ger_itemserv_id as mov_cotacao_ger_itemserv_id,
		t1.observacao1 as mov_cotacao_observacao1,
		t1.observacao2 as mov_cotacao_observacao2,
		t1.qnt_cot as mov_cotacao_qnt_cot,
		t1.valor_unit_cot as mov_cotacao_valor_unit_cot,
		t1.valor_total_cot as mov_cotacao_valor_total_cot,
		t1.valor_desc_cot as mov_cotacao_valor_desc_cot,
		t1.valor_frete_cot as mov_cotacao_valor_frete_cot,
		t1.valor_outro_cot as mov_cotacao_valor_outro_cot,
		t1.valor_total_trib_cot as mov_cotacao_valor_total_trib_cot,
		t1.status as mov_cotacao_status,
		fnstd('mov_cotacao','status',t1.status) as mov_cotacao_status_desc,
		t1.data_status as mov_cotacao_data_status,
		t1.system_user_id_aprov as mov_cotacao_system_user_id_aprov,

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
		-- Ger Pessoa
		t3.id as ger_pessoa_id,
		t3.nome as ger_pessoa_nome,
		t3.ativo as ger_pessoa_ativo,
		fnstd('SN','default',t3.ativo) as ger_pessoa_ativo_desc,
		t3.doc_cpf as ger_pessoa_doc_cpf,
		t3.doc_cnpj as ger_pessoa_doc_cnpj,
		fnutil_formatcpfcnpj(t3.id, true) as ger_pessoa_doc_cpf_cnpj_desc,
		t3.sigla_pes as ger_pessoa_sigla,

		-- Ger Pessoa Endereco
		t4.id as ger_pessoa_endereco_id,
		t4.ger_pessoa_id as ger_pessoa_endereco_pessoa_id,
		t4.ativo as ger_pessoa_endereco_ativo,
		fnstd('SN','default',t4.ativo) as ger_pessoa_endereco_ativo_desc,
		t4.tipo as ger_pessoa_endereco_tipo,
		fnstd('ger_pessoa_endereco','tipo',t4.tipo) as ger_pessoa_endereco_tipo_desc,
		t4.padrao as ger_pessoa_endereco_padrao,
		fnstd('SN','default',t4.padrao) as ger_pessoa_endereco_padrao_desc,
		t4.end_logradouro as ger_pessoa_endereco_end_logradouro,
		t4.end_logradouro_nr as ger_pessoa_endereco_end_logradouro_nr,
		t4.end_bairro as ger_pessoa_endereco_end_bairro,
		t4.end_complemento as ger_pessoa_endereco_end_complemento,
		t4.end_cep as ger_pessoa_endereco_end_cep,
		t4.end_ger_cidade_id as ger_pessoa_endereco_end_ger_cidade_id,

		-- Ger Item Serv
		t5.id as ger_itemserv_id,
		t5.nome as ger_itemserv_nome,
		t5.ativo as ger_itemserv_ativo,
		fnstd('SN','default',t5.ativo) as ger_itemserv_ativo_desc,
		t5.sigla_itemserv as ger_itemserv_sigla,
		t5.tipo as ger_itemserv_tipo,
		fnstd('ger_itemserv','tipo',t5.tipo) as ger_itemserv_tipo_desc,

		-- System User
		t6.id as system_user_id,
		t6.name as system_user_name,
		t6.active as system_user_active,
		fnstd('SN','default',t6.active) as system_user_active_desc,

		t1.log_user_ins,
		t1.log_date_ins,
		t1.log_user_upd,
		t1.log_date_upd,

		-- Sigla Desc
		t3.sigla_pes||' - '||t3.nome as ger_pessoa_sigla_desc,
		t5.sigla_itemserv||' - '||t5.nome as ger_itemserv_sigla_desc

	from mov_cotacao t1
		inner join mov t2
		on t1.mov_id = t2.id
		inner join ger_pessoa t3
		on t1.ger_pessoa_id = t3.id
		left join ger_pessoa_endereco t4
		on t1.ger_pessoa_endereco_id = t4.id
		inner join ger_itemserv t5
		on t1.ger_itemserv_id = t5.id
		left join system_user t6
		on t1.system_user_id_aprov = t6.id
