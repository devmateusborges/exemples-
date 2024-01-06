-- busca o ultimo numero de documento que vai ser utilizado
-- server pra nfe, cte e mdfe
select
	ger_numeracao.ultimo_nr + 1 as ultimo_nr
from
	mov
join mov_operacao on
	mov_operacao.unit_id = mov.unit_id
	and mov_operacao.id = mov.mov_operacao_id
join ger_numeracao on
	ger_numeracao.unit_id = mov_operacao.unit_id
	and ger_numeracao.id = mov_operacao.ger_numeracao_id
where
	mov.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
	and mov.id = $2;

-- NFe
-- busca os dados de identificação da nfe
select
    (select fis_cfop.nome
    from
    mov_itemserv
    join fis_cfop
    on fis_cfop.id = mov_itemserv.fis_cfop_id
    where
    mov_itemserv.unit_id = mov.unit_id
    and mov_itemserv.mov_id = mov.id
    limit 1
    ) AS natureza_operacao,
    fis_doc.serie,
    fis_doc.numero,
    mov.data_mov AS data_emissao,
    mov.data_mov AS data_entrada_saida,
    (case when (mov_tipo.sigla_mov_tipo IN ('NF01', 'NF02')) then '2' else '1' end) AS tipo_documento,
    (case when (uf_empresa.sigla_uf = destinatario_uf.sigla_uf) then '1' else '2' end) AS local_destino,
    mov_operacao.finalidade_doc AS finalidade_emissao,
    '1' As consumidor_final,
    '1' AS presenca_comprador,

    destinatario.doc_cnpj AS cnpj_destinatario,
    destinatario.doc_cpf AS cpf_destinatario,
    destinatario.nome AS nome_destinatario,
    destinatario_endereco.end_logradouro AS logradouro_destinatario,
    destinatario_endereco.end_logradouro_nr AS numero_destinatario,
    destinatario_endereco.end_complemento AS complemento_destinatario,
    destinatario_endereco.end_bairro AS bairro_destinatario,
    destinatario_cidade.nr_cidade AS codigo_municipio_destinatario,
    destinatario_cidade.nome AS municipio_destinatario,
    destinatario_uf.sigla_uf AS uf_destinatario,
    destinatario_endereco.end_cep AS cep_destinatario,
    destinatario_pais.nr_pais AS codigo_pais_destinatario,
    destinatario_pais.nome AS pais_destinatario,
    destinatario_endereco.fone AS telefone_destinatario,
    destinatario.contrib_icms AS indicador_inscricao_estadual_destinatario,
    destinatario.doc_ie AS inscricao_estadual_destinatario,
    '' AS inscricao_suframa_destinatario,
    destinatario.doc_im AS inscricao_municipal_destinatario,
    destinatario_endereco.email AS email_destinatario,

    entrega.doc_cnpj AS cnpj_entrega,
    entrega.doc_cpf AS cpf_entrega,
    entrega.nome AS nome_entrega,
    entrega_endereco.end_logradouro AS logradouro_entrega,
    entrega_endereco.end_logradouro_nr AS numero_entrega,
    entrega_endereco.end_complemento AS complemento_entrega,
    entrega_endereco.end_bairro AS bairro_entrega,
    entrega_cidade.nr_cidade AS codigo_municipio_entrega,
    entrega_cidade.nome AS municipio_entrega,
    entrega_uf.sigla_uf AS uf_entrega,
    entrega_endereco.end_cep AS cep_entrega,
    entrega_pais.nr_pais AS codigo_pais_entrega,
    entrega_pais.nome AS pais_entrega,
    entrega_endereco.fone AS telefone_entrega,
    entrega.contrib_icms AS indicador_inscricao_estadual_entrega,
    entrega.doc_ie AS inscricao_estadual_entrega,
    '' AS inscricao_suframa_entrega,
    entrega.doc_im AS inscricao_municipal_entrega,
    entrega_endereco.email AS email_entrega,

    mov.tipo_frete AS modalidade_frete,

    frete.doc_cnpj AS cnpj_transportador,
    frete.doc_cpf AS cpf_transportador,
    frete.nome AS nome_transportador,
    frete.doc_ie AS inscricao_estadual_transportador,
    frete_endereco.end_logradouro AS endereco_transportador,
    frete_cidade.nome AS municipio_transportador,
    frete_uf.sigla_uf AS uf_transportador,

    ope_centro2_equip.placa AS veiculo_placa,
    veiculo_uf.sigla_uf AS veiculo_uf,
    ope_centro2_equip.nr_registro_estadual AS veiculo_rntc,

    mov.observacao_fiscal AS informacoes_adicionais_fisco,
    -- duplicata
    fin_pagrec.numero_doc_pagrec AS numero_fatura,
    fin_pagrec.valor_pagrec AS valor_original_fatura,
    fin_pagrec.valor_pagrec AS valor_liquido_fatura
  from
    mov

  left join fis_doc on
    fis_doc.unit_id = mov.unit_id
    and fis_doc.mov_id = mov.id
  join mov_operacao on
    mov_operacao.unit_id = mov.unit_id
    and mov_operacao.id = mov.mov_operacao_id
  join mov_tipo on
    mov_tipo.id = mov_operacao.mov_tipo_id
  join ger_empresa on
    mov.unit_id = ger_empresa.unit_id
    and mov.ger_empresa_id = ger_empresa.id
  join ger_cidade as cidade_empresa on
    cidade_empresa.id = ger_empresa.end_ger_cidade_id
  join ger_uf as uf_empresa on
    uf_empresa.id = cidade_empresa.ger_uf_id

  left join ger_pessoa_endereco AS destinatario_endereco on
    destinatario_endereco.unit_id = mov.unit_id
    and destinatario_endereco.id = mov.ger_pessoa_endereco_id_fiscal
  left join ger_cidade as destinatario_cidade on
    destinatario_cidade.id = destinatario_endereco.end_ger_cidade_id
  left join ger_uf as destinatario_uf on
    destinatario_uf.id = destinatario_cidade.ger_uf_id
  left join ger_pais as destinatario_pais on
    destinatario_pais.id = destinatario_uf.ger_pais_id
  left join ger_pessoa AS destinatario on
    destinatario.unit_id = destinatario_endereco.unit_id
    and destinatario.id = destinatario_endereco.ger_pessoa_id

  left join ger_pessoa_endereco AS entrega_endereco on
    entrega_endereco.unit_id = mov.unit_id
    and entrega_endereco.id = mov.ger_pessoa_endereco_id_entrega
  left join ger_cidade as entrega_cidade on
    entrega_cidade.id = entrega_endereco.end_ger_cidade_id
  left join ger_uf as entrega_uf on
    entrega_uf.id = entrega_cidade.ger_uf_id
  left join ger_pais as entrega_pais on
    entrega_pais.id = entrega_uf.ger_pais_id
  left join ger_pessoa AS entrega on
    entrega.unit_id = entrega_endereco.unit_id
    and entrega.id = entrega_endereco.ger_pessoa_id


  left join mov_frete on
    mov_frete.unit_id = mov.unit_id
    and mov_frete.mov_id = mov.id

  left join ger_pessoa_endereco AS frete_endereco on
    frete_endereco.unit_id = mov_frete.unit_id
    and frete_endereco.id = mov_frete.ger_pessoa_endereco_id_transp
  left join ger_cidade as frete_cidade on
    frete_cidade.id = frete_endereco.end_ger_cidade_id
  left join ger_uf as frete_uf on
    frete_uf.id = frete_cidade.ger_uf_id
  left join ger_pessoa AS frete on
    frete.unit_id = frete_endereco.unit_id
    and frete.id = frete_endereco.ger_pessoa_id
          

  left join ope_centro2_equip on
    ope_centro2_equip.unit_id = mov_frete.unit_id
    and ope_centro2_equip.id = mov_frete.ope_centro2_id_equip
  left join ger_cidade as veiculo_cidade on
    veiculo_cidade.id = frete_endereco.end_ger_cidade_id
  left join ger_uf as veiculo_uf on
    veiculo_uf.id = veiculo_cidade.ger_uf_id


  left join fin_pagrec_origem on
    fin_pagrec_origem.unit_id = mov.unit_id
    and fin_pagrec_origem.mov_id = mov.id

  left join fin_pagrec on
    fin_pagrec.unit_id = fin_pagrec_origem.unit_id
    and fin_pagrec.id = fin_pagrec_origem.fin_pagrec_id

  where
    mov.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
    and mov.id = $2;

-- busca os documentos vinculados ao de oridem
  select
    chave
  from
    mov_origem
  join mov on
    mov.unit_id = mov_origem.unit_id
    and mov.id = mov_origem.mov_id_origem
  left join fis_doc on
    fis_doc.unit_id = mov.unit_id
    and fis_doc.mov_id = mov.id
  where
    mov_origem.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
    and mov_origem.mov_id = $2;

-- busca os items do movimento
  select
    '1.2.3.4' AS numero_item,
    ger_itemserv.id AS codigo_produto,
    'SEM GTIN' AS codigo_barras_comercial,
    ger_itemserv.nome AS descricao,
    fis_ncm.nr_ncm AS codigo_ncm,
    fis_cest.nr_cest AS cest,
    fis_cfop.nr_cfop As cfop,
    ger_umedida.sigla_umedida AS unidade_comercial,
    mov_itemserv.qnt_conv AS quantidade_comercial,
    mov_itemserv.valor_unit_orig AS valor_unitario_comercial,
    mov_itemserv.valor_bruto,
    'SEM GTIN' AS codigo_barras_tributavel,
    ger_umedida.sigla_umedida AS unidade_tributavel,
    mov_itemserv.qnt_conv AS quantidade_tributavel,
    mov_itemserv.valor_unit_orig AS valor_unitario_tributavel,
    mov_itemserv.valor_frete,
    mov_itemserv.valor_seguro,
    mov_itemserv.valor_desconto,
    mov_itemserv.valor_outros AS valor_outras_despesas,
    '1' AS inclui_no_total,
    '0' AS valor_total_tributos,
    ger_itemserv.origem_fiscal AS icms_origem 
  from
    mov_itemserv
  left join ger_itemserv on
    ger_itemserv.unit_id = mov_itemserv.unit_id
    and ger_itemserv.id = mov_itemserv.ger_itemserv_id
  left join fis_ncm on
    fis_ncm.id = ger_itemserv.fis_ncm_id
  left join fis_cfop on
    fis_cfop.id = mov_itemserv.fis_cfop_id
  left join fis_cest on
    fis_cest.id = ger_itemserv.fis_cest_id
  left join ger_umedida on
    ger_umedida.id = ger_itemserv.ger_umedida_id
  where
    mov_itemserv.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
    and mov_itemserv.mov_id = $2;

-- busca os impostos da nfe/nfce
select
	sum(icms_situacao_tributaria) as icms_situacao_tributaria,
	sum(icms_modalidade_base_calculo) as icms_modalidade_base_calculo,
	sum(icms_base_calculo) as icms_base_calculo,
	sum(icms_aliquota) as icms_aliquota,
	sum(icms_valor) as icms_valor,
	sum(icms_base_calculo_st) as icms_base_calculo_st,
	sum(icms_margem_valor_adicionado_st) as icms_margem_valor_adicionado_st,
	sum(icms_aliquota_st) as icms_aliquota_st,
	sum(icms_valor_st) as icms_valor_st,
	sum(icms_reducao_base_calculo) as icms_reducao_base_calculo,
	sum(icms_valor_operacao) as icms_valor_operacao,
	sum(icms_valor_diferido) as icms_valor_diferido,
	sum(icms_aliquota_credito_simples) as icms_aliquota_credito_simples,
	sum(icms_valor_credito_simples) as icms_valor_credito_simples,
	sum(fcp_base_calculo) as fcp_base_calculo,
	sum(fcp_percentual) as fcp_percentual,
	sum(fcp_valor) as fcp_valor,
	sum(fcp_base_calculo_st) as fcp_base_calculo_st,
	sum(fcp_percentual_st) as fcp_percentual_st,
	sum(fcp_valor_st) as fcp_valor_st,
	sum(ipi_situacao_tributaria) as ipi_situacao_tributaria,
	sum(ipi_base_calculo) as ipi_base_calculo,
	sum(ipi_aliquota_porcentual) as ipi_aliquota_porcentual,
	sum(ipi_valor) as ipi_valor,
	sum(pis_situacao_tributaria) as pis_situacao_tributaria,
	sum(pis_base_calculo) as pis_base_calculo,
	sum(pis_aliquota_porcentual) as pis_aliquota_porcentual,
	sum(pis_valor) as pis_valor,
	sum(cofins_situacao_tributaria) as cofins_situacao_tributaria,
	sum(cofins_base_calculo) as cofins_base_calculo,
	sum(cofins_aliquota_porcentual) as cofins_aliquota_porcentual,
	sum(cofins_valor) as cofins_valor
from
	(
	select
		cast(cst as integer) as icms_situacao_tributaria,
		modalidade_base_calc as icms_modalidade_base_calculo,
		valor_base_calc as icms_base_calculo,
		perc_aliquota as icms_aliquota,
		valor_imposto as icms_valor,
		valor_base_calc_st as icms_base_calculo_st,
		margem_agregada_st as icms_margem_valor_adicionado_st,
		perc_aliquota_st as icms_aliquota_st,
		valor_imposto_st as icms_valor_st,
		perc_reducao_base_calc as icms_reducao_base_calculo,
		valor_imposto_operacao as icms_valor_operacao,
		valor_imposto_diferido as icms_valor_diferido,
		perc_credito_sn as icms_aliquota_credito_simples,
		valor_credito_sn as icms_valor_credito_simples,
		valor_base_calc_fcp as fcp_base_calculo,
		perc_aliquota_fcp as fcp_percentual,
		valor_imposto_fcp as fcp_valor,
		valor_base_calc_fcp_st as fcp_base_calculo_st,
		perc_aliquota_fcp_st as fcp_percentual_st,
		valor_imposto_fcp_st as fcp_valor_st,
		0 as ipi_situacao_tributaria,
		0 as ipi_base_calculo,
		0 as ipi_aliquota_porcentual,
		0 as ipi_valor,
		0 as pis_situacao_tributaria,
		0 as pis_base_calculo,
		0 as pis_aliquota_porcentual,
		0 as pis_valor,
		0 as cofins_situacao_tributaria,
		0 as cofins_base_calculo,
		0 as cofins_aliquota_porcentual,
		0 as cofins_valor
	from
		fis_tributacao
	join fis_tributo on
		fis_tributo.id = fis_tributacao.fis_tributo_id
		and fis_tributo.nr_tributo in ('1',	'5')
	where
		fis_tributacao.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
		and fis_tributacao.mov_itemserv_id = '72c48d02-813e-4fb3-9e4f-b1e3fe455fb8'
union all
	select
		0 as icms_situacao_tributaria,
		0 as icms_modalidade_base_calculo,
		0 as icms_base_calculo,
		0 as icms_aliquota,
		0 as icms_valor,
		0 as icms_base_calculo_st,
		0 as icms_margem_valor_adicionado_st,
		0 as icms_aliquota_st,
		0 as icms_valor_st,
		0 as icms_reducao_base_calculo,
		0 as icms_valor_operacao,
		0 as icms_valor_diferido,
		0 as icms_aliquota_credito_simples,
		0 as icms_valor_credito_simples,
		0 as fcp_base_calculo,
		0 as fcp_percentual,
		0 as fcp_valor,
		0 as fcp_base_calculo_st,
		0 as fcp_percentual_st,
		0 as fcp_valor_st,
		cast(cst as integer) as ipi_situacao_tributaria,
		valor_base_calc as ipi_base_calculo,
		perc_aliquota as ipi_aliquota_porcentual,
		valor_imposto as ipi_valor,
		0 as pis_situacao_tributaria,
		0 as pis_base_calculo,
		0 as pis_aliquota_porcentual,
		0 as pis_valor,
		0 as cofins_situacao_tributaria,
		0 as cofins_base_calculo,
		0 as cofins_aliquota_porcentual,
		0 as cofins_valor
	from
		fis_tributacao
	join fis_tributo on
		fis_tributo.id = fis_tributacao.fis_tributo_id
		and fis_tributo.nr_tributo = '2'
	where
		fis_tributacao.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
		and fis_tributacao.mov_itemserv_id = '72c48d02-813e-4fb3-9e4f-b1e3fe455fb8'
union all
	select
		0 as icms_situacao_tributaria,
		0 as icms_modalidade_base_calculo,
		0 as icms_base_calculo,
		0 as icms_aliquota,
		0 as icms_valor,
		0 as icms_base_calculo_st,
		0 as icms_margem_valor_adicionado_st,
		0 as icms_aliquota_st,
		0 as icms_valor_st,
		0 as icms_reducao_base_calculo,
		0 as icms_valor_operacao,
		0 as icms_valor_diferido,
		0 as icms_aliquota_credito_simples,
		0 as icms_valor_credito_simples,
		0 as fcp_base_calculo,
		0 as fcp_percentual,
		0 as fcp_valor,
		0 as fcp_base_calculo_st,
		0 as fcp_percentual_st,
		0 as fcp_valor_st,
		0 as ipi_situacao_tributaria,
		0 as ipi_base_calculo,
		0 as ipi_aliquota_porcentual,
		0 as ipi_valor,
		cast(cst as integer) as pis_situacao_tributaria,
		valor_base_calc as pis_base_calculo,
		perc_aliquota as pis_aliquota_porcentual,
		valor_imposto as pis_valor,
		0 as cofins_situacao_tributaria,
		0 as cofins_base_calculo,
		0 as cofins_aliquota_porcentual,
		0 as cofins_valor
	from
		fis_tributacao
	join fis_tributo on
		fis_tributo.id = fis_tributacao.fis_tributo_id
		and fis_tributo.nr_tributo = '9'
	where
		fis_tributacao.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
		and fis_tributacao.mov_itemserv_id = '72c48d02-813e-4fb3-9e4f-b1e3fe455fb8'
union all
	select
		0 as icms_situacao_tributaria,
		0 as icms_modalidade_base_calculo,
		0 as icms_base_calculo,
		0 as icms_aliquota,
		0 as icms_valor,
		0 as icms_base_calculo_st,
		0 as icms_margem_valor_adicionado_st,
		0 as icms_aliquota_st,
		0 as icms_valor_st,
		0 as icms_reducao_base_calculo,
		0 as icms_valor_operacao,
		0 as icms_valor_diferido,
		0 as icms_aliquota_credito_simples,
		0 as icms_valor_credito_simples,
		0 as fcp_base_calculo,
		0 as fcp_percentual,
		0 as fcp_valor,
		0 as fcp_base_calculo_st,
		0 as fcp_percentual_st,
		0 as fcp_valor_st,
		0 as ipi_situacao_tributaria,
		0 as ipi_base_calculo,
		0 as ipi_aliquota_porcentual,
		0 as ipi_valor,
		0 as pis_situacao_tributaria,
		0 as pis_base_calculo,
		0 as pis_aliquota_porcentual,
		0 as pis_valor,
		cast(cst as integer) as cofins_situacao_tributaria,
		valor_base_calc as cofins_base_calculo,
		perc_aliquota as cofins_aliquota_porcentual,
		valor_imposto as cofins_valor
	from
		fis_tributacao
	join fis_tributo on
		fis_tributo.id = fis_tributacao.fis_tributo_id
		and fis_tributo.nr_tributo = '10'
	where
		fis_tributacao.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
		and fis_tributacao.mov_itemserv_id = '72c48d02-813e-4fb3-9e4f-b1e3fe455fb8' )as dados

-- busca os veiculos de reboque
select
  ope_centro2_equip.placa AS veiculo_placa,
  veiculo_uf.sigla_uf AS veiculo_uf,
  ope_centro2_equip.nr_registro_estadual AS veiculo_rntc
from
  mov_reboque
left join ope_centro2_equip on
  ope_centro2_equip.unit_id = mov_reboque.unit_id
  and ope_centro2_equip.id = mov_reboque.ope_centro2_id_equip
left join ger_cidade as veiculo_cidade on
  veiculo_cidade.id = ope_centro2_equip.ger_cidade_id
left join ger_uf as veiculo_uf on
  veiculo_uf.id = veiculo_cidade.ger_uf_id
where
  mov_reboque.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
  and mov_reboque.mov_id = $2;

-- busca os volumes transportados
select
  mov_medida.qnt_medida AS quantidade,
  ger_umedida.nome AS especie,
  mov_medida.marca AS marca,
  mov_medida.nr_volume AS numero,
  mov_medida.peso_liquido AS peso_liquido,
  mov_medida.peso_bruto AS peso_bruto
from
  mov_medida
left join ger_umedida on
  ger_umedida.id = mov_medida.ger_umedida_id
where
  mov_medida.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
  and mov_medida.mov_id = $2;

-- busca as duplicatas
select
  fin_pagrec_parc.numero_parc AS numero,
  fin_pagrec_parc.data_venc AS data_vencimento,
  fin_pagrec_parc.valor_pagrec AS valor
from
  mov
left join fin_pagrec_origem on
  fin_pagrec_origem.unit_id = mov.unit_id
  and fin_pagrec_origem.mov_id = mov.id
left join fin_pagrec on
  fin_pagrec.unit_id = fin_pagrec_origem.unit_id
  and fin_pagrec.id = fin_pagrec_origem.fin_pagrec_id
left join fin_pagrec_parc on
  fin_pagrec_parc.unit_id = fin_pagrec.unit_id
  and fin_pagrec_parc.fin_pagrec_id = fin_pagrec.id
where
  mov.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
  and mov.id = $2;

-- busca as tributações do item

-- CTe
-- identificação do cte
select
  (select
    fis_cfop.nr_cfop
  from
    mov_itemserv
  left join fis_cfop on
    fis_cfop.id = mov_itemserv.fis_cfop_id
  where  
    mov_itemserv.unit_id = mov.unit_id
    and mov_itemserv.mov_id = mov.id
    limit 1
  ) As cfop,
  (select
    fis_cfop.nome
  from
    mov_itemserv
  left join fis_cfop on
    fis_cfop.id = mov_itemserv.fis_cfop_id
  where  
    mov_itemserv.unit_id = mov.unit_id
    and mov_itemserv.mov_id = mov.id
    limit 1
  ) AS natureza_operacao,
  fis_doc.serie,
  fis_doc.numero,
  mov.data_mov AS data_emissao,
  mov_operacao.finalidade_doc AS tipo_documento,
  cidade_empresa.nr_cidade AS codigo_municipio_envio,
  cidade_empresa.nome AS municipio_envio,
  uf_empresa.sigla_uf AS uf_envio,
  mov.tipo_serv_frete AS tipo_servico,
  cidade_carregamento.nr_cidade AS codigo_municipio_inicio,
  cidade_carregamento.nome AS municipio_inicio,
  uf_carregamento.sigla_uf AS uf_inicio,
  cidade_descarregamento.nr_cidade AS codigo_municipio_fim,
  cidade_descarregamento.nome AS municipio_fim,
  uf_descarregamento.sigla_uf AS uf_fim,
  '0' AS retirar_mercadoria,

  'VER DEPOIS' AS indicador_inscricao_estadual_tomador,

  mov.tipo_tomador_serv_frete AS tomador,
  tomador.doc_cnpj AS cnpj_tomador,
  tomador.doc_cpf AS cpf_tomador,
  tomador.doc_ie AS inscricao_estadual_tomador,
  tomador.razao_social AS nome_tomador,
  tomador.nome AS nome_fantasia_tomador,
  tomador_endereco.fone AS telefone_tomador,
  tomador_endereco.end_logradouro AS logradouro_tomador,
  tomador_endereco.end_logradouro_nr AS numero_tomador,
  tomador_endereco.end_complemento AS complemento_tomador,
  tomador_endereco.end_bairro AS bairro_tomador,
  tomador_cidade.nr_cidade AS codigo_municipio_tomador,
  tomador_cidade.nome AS municipio_tomador,
  tomador_uf.sigla_uf AS uf_tomador,
  tomador_pais.nr_pais AS codigo_pais_tomador,
  tomador_pais.nome AS pais_tomador,
  tomador_endereco.email AS email_tomador,

  remetente.doc_cnpj AS cnpj_remetente,
  remetente.doc_cpf AS cpf_remetente,
  remetente.doc_ie AS inscricao_estadual_remetente,
  remetente.razao_social AS nome_remetente,
  remetente.nome AS nome_fantasia_remetente,
  remetente_endereco.fone AS telefone_remetente,
  remetente_endereco.end_logradouro AS logradouro_remetente,
  remetente_endereco.end_logradouro_nr AS numero_remetente,
  remetente_endereco.end_complemento AS complemento_remetente,
  remetente_endereco.end_bairro AS bairro_remetente,
  remetente_cidade.nr_cidade AS codigo_municipio_remetente,
  remetente_cidade.nome AS municipio_remetente,
  remetente_endereco.end_cep AS cep_remetente,
  remetente_uf.sigla_uf AS uf_remetente,
  remetente_pais.nr_pais AS codigo_pais_remetente,
  remetente_pais.nome AS pais_remetente,
  remetente_endereco.email AS email_tomador,

  expedidor.doc_cnpj AS cnpj_expedidor,
  expedidor.doc_cpf AS cpf_expedidor,
  expedidor.doc_ie AS inscricao_estadual_expedidor,
  expedidor.razao_social AS nome_expedidor,
  expedidor.nome AS nome_fantasia_expedidor,
  expedidor_endereco.fone AS telefone_expedidor,
  expedidor_endereco.end_logradouro AS logradouro_expedidor,
  expedidor_endereco.end_logradouro_nr AS numero_expedidor,
  expedidor_endereco.end_complemento AS complemento_expedidor,
  expedidor_endereco.end_bairro AS bairro_expedidor,
  expedidor_cidade.nr_cidade AS codigo_municipio_expedidor,
  expedidor_cidade.nome AS municipio_expedidor,
  expedidor_endereco.end_cep AS cep_expedidor,
  expedidor_uf.sigla_uf AS uf_expedidor,
  expedidor_pais.nr_pais AS codigo_pais_expedidor,
  expedidor_pais.nome AS pais_expedidor,
  expedidor_endereco.email AS email_tomador,

  recebedor.doc_cnpj AS cnpj_recebedor,
  recebedor.doc_cpf AS cpf_recebedor,
  recebedor.doc_ie AS inscricao_estadual_recebedor,
  recebedor.razao_social AS nome_recebedor,
  recebedor.nome AS nome_fantasia_recebedor,
  recebedor_endereco.fone AS telefone_recebedor,
  recebedor_endereco.end_logradouro AS logradouro_recebedor,
  recebedor_endereco.end_logradouro_nr AS numero_recebedor,
  recebedor_endereco.end_complemento AS complemento_recebedor,
  recebedor_endereco.end_bairro AS bairro_recebedor,
  recebedor_cidade.nr_cidade AS codigo_municipio_recebedor,
  recebedor_cidade.nome AS municipio_recebedor,
  recebedor_endereco.end_cep AS cep_recebedor,
  recebedor_uf.sigla_uf AS uf_recebedor,
  recebedor_pais.nr_pais AS codigo_pais_recebedor,
  recebedor_pais.nome AS pais_recebedor,
  recebedor_endereco.email AS email_tomador,

  destinatario.doc_cnpj AS cnpj_destinatario,
  destinatario.doc_cpf AS cpf_destinatario,
  destinatario.doc_ie AS inscricao_estadual_destinatario,
  destinatario.razao_social AS nome_destinatario,
  destinatario.nome AS nome_fantasia_destinatario,
  destinatario_endereco.fone AS telefone_destinatario,
  destinatario_endereco.end_logradouro AS logradouro_destinatario,
  destinatario_endereco.end_logradouro_nr AS numero_destinatario,
  destinatario_endereco.end_complemento AS complemento_destinatario,
  destinatario_endereco.end_bairro AS bairro_destinatario,
  destinatario_cidade.nr_cidade AS codigo_municipio_destinatario,
  destinatario_cidade.nome AS municipio_destinatario,
  destinatario_endereco.end_cep AS cep_destinatario,
  destinatario_uf.sigla_uf AS uf_destinatario,
  destinatario_pais.nr_pais AS codigo_pais_destinatario,
  destinatario_pais.nome AS pais_destinatario,
  destinatario_endereco.email AS email_tomador,

  mov.valor_item_frete_total AS valor_total,
  mov.valor_financeiro_total AS valor_receber,

  mov.valor_item_frete_total AS valor_total_carga,
  (select
    ger_itemserv.nome
  from
    mov_itemserv
  left join ger_itemserv on
    ger_itemserv.unit_id = mov_itemserv.unit_id
    and ger_itemserv.id = mov_itemserv.ger_itemserv_id
  where  
    mov_itemserv.unit_id = mov.unit_id
    and mov_itemserv.mov_id = mov.id
    limit 1
  ) AS produto_predominante,
  '' AS outras_caracteristicas_carga,
  (
    select
    chave
    from
      mov_origem
    join mov AS movOrigem on
      movOrigem.unit_id = mov_origem.unit_id
      and movOrigem.id = mov_origem.mov_id_origem
    left join fis_doc on
      fis_doc.unit_id = movOrigem.unit_id
      and fis_doc.mov_id = movOrigem.id
    where
      mov_origem.unit_id = mov.unit_id
      and mov_origem.mov_id = mov.id
  ) AS chave_cte_complementado,
  (
    select
    chave
    from
      mov_origem
    join mov AS movOrigem on
      movOrigem.unit_id = mov_origem.unit_id
      and movOrigem.id = mov_origem.mov_id_origem
    left join fis_doc on
      fis_doc.unit_id = movOrigem.unit_id
      and fis_doc.mov_id = movOrigem.id
    where
      mov_origem.unit_id = mov.unit_id
      and mov_origem.mov_id = mov.id
  ) AS chave_cte_original_anulado,
  mov.data_anulacao AS data_declaracao_anulacao,
  mov.observacao_transp AS caracteristica_adicional_transporte,
  mov.observacao_serv AS caracteristica_adicional_servico,
  (
    select
      fis_tributacao.valor_imposto
    from
      mov_itemserv
    join fis_tributacao on
      fis_tributacao.unit_id = mov_itemserv.unit_id
      and fis_tributacao.mov_itemserv_id = mov_itemserv.id
    join fis_tributo on
      fis_tributo.id = fis_tributacao.fis_tributo_id
      and fis_tributo.nr_tributo = '9'
    where  
      mov_itemserv.unit_id = mov.unit_id
      and mov_itemserv.mov_id = mov.id
      limit 1
  ) as valor_pis,
  (
    select
      fis_tributacao.valor_imposto
    from
      mov_itemserv
    join fis_tributacao on
      fis_tributacao.unit_id = mov_itemserv.unit_id
      and fis_tributacao.mov_itemserv_id = mov_itemserv.id
    join fis_tributo on
      fis_tributo.id = fis_tributacao.fis_tributo_id
      and fis_tributo.nr_tributo = '10'
    where  
      mov_itemserv.unit_id = mov.unit_id
      and mov_itemserv.mov_id = mov.id
      limit 1
  ) as valor_cofins,
  (
    select
      fis_tributacao.valor_imposto
    from
      mov_itemserv
    join fis_tributacao on
      fis_tributacao.unit_id = mov_itemserv.unit_id
      and fis_tributacao.mov_itemserv_id = mov_itemserv.id
    join fis_tributo on
      fis_tributo.id = fis_tributacao.fis_tributo_id
      and fis_tributo.nr_tributo = '9'
    where  
      mov_itemserv.unit_id = mov.unit_id
      and mov_itemserv.mov_id = mov.id
      limit 1
  ) as valor_pis,
  (
    select
      fis_tributacao.valor_imposto
    from
      mov_itemserv
    join fis_tributacao on
      fis_tributacao.unit_id = mov_itemserv.unit_id
      and fis_tributacao.mov_itemserv_id = mov_itemserv.id
    join fis_tributo on
      fis_tributo.id = fis_tributacao.fis_tributo_id
      and fis_tributo.nr_tributo = '3'
    where  
      mov_itemserv.unit_id = mov.unit_id
      and mov_itemserv.mov_id = mov.id
      limit 1
  ) as valor_ir,
  (
    select
      fis_tributacao.valor_imposto
    from
      mov_itemserv
    join fis_tributacao on
      fis_tributacao.unit_id = mov_itemserv.unit_id
      and fis_tributacao.mov_itemserv_id = mov_itemserv.id
    join fis_tributo on
      fis_tributo.id = fis_tributacao.fis_tributo_id
      and fis_tributo.nr_tributo = '6'
    where  
      mov_itemserv.unit_id = mov.unit_id
      and mov_itemserv.mov_id = mov.id
      limit 1
  ) as valor_inss,
  (
    select
      fis_tributacao.valor_imposto
    from
      mov_itemserv
    join fis_tributacao on
      fis_tributacao.unit_id = mov_itemserv.unit_id
      and fis_tributacao.mov_itemserv_id = mov_itemserv.id
    join fis_tributo on
      fis_tributo.id = fis_tributacao.fis_tributo_id
      and fis_tributo.nr_tributo = '7'
    where  
      mov_itemserv.unit_id = mov.unit_id
      and mov_itemserv.mov_id = mov.id
      limit 1
  ) as valor_csll

from
  mov
left join fis_doc on
  fis_doc.unit_id = mov.unit_id
  and fis_doc.mov_id = mov.id
join mov_operacao on
  mov_operacao.unit_id = mov.unit_id
  and mov_operacao.id = mov.mov_operacao_id
join mov_tipo on
  mov_tipo.id = mov_operacao.mov_tipo_id
left join ger_empresa on
  mov.unit_id = ger_empresa.unit_id
  and mov.ger_empresa_id = ger_empresa.id
left join ger_cidade as cidade_empresa on
  cidade_empresa.id = ger_empresa.end_ger_cidade_id
left join ger_uf as uf_empresa on
  uf_empresa.id = cidade_empresa.ger_uf_id
left join ger_cidade as cidade_carregamento on
  cidade_carregamento.id = mov.ger_cidade_id_carreg
left join ger_uf as uf_carregamento on
  uf_empresa.id = cidade_carregamento.ger_uf_id
left join ger_cidade as cidade_descarregamento on
  cidade_descarregamento.id = mov.ger_cidade_id_descarreg
left join ger_uf as uf_descarregamento on
  uf_empresa.id = cidade_descarregamento.ger_uf_id

left join ger_pessoa_endereco AS tomador_endereco on
  tomador_endereco.unit_id = mov.unit_id
  and tomador_endereco.id = mov.ger_pessoa_endereco_id_fiscal
left join ger_cidade as tomador_cidade on
  tomador_cidade.id = tomador_endereco.end_ger_cidade_id
left join ger_uf as tomador_uf on
  tomador_uf.id = tomador_cidade.ger_uf_id
left join ger_pais as tomador_pais on
  tomador_pais.id = tomador_uf.ger_pais_id
left join ger_pessoa AS tomador on
  tomador.unit_id = tomador_endereco.unit_id
  and tomador.id = tomador_endereco.ger_pessoa_id

left join ger_pessoa_endereco AS remetente_endereco on
  remetente_endereco.unit_id = mov.unit_id
  and remetente_endereco.id = mov.ger_pessoa_endereco_id_reme
left join ger_cidade as remetente_cidade on
  remetente_cidade.id = remetente_endereco.end_ger_cidade_id
left join ger_uf as remetente_uf on
  remetente_uf.id = remetente_cidade.ger_uf_id
left join ger_pais as remetente_pais on
  remetente_pais.id = remetente_uf.ger_pais_id
left join ger_pessoa AS remetente on
  remetente.unit_id = remetente_endereco.unit_id
  and remetente.id = remetente_endereco.ger_pessoa_id

left join ger_pessoa_endereco AS expedidor_endereco on
  expedidor_endereco.unit_id = mov.unit_id
  and expedidor_endereco.id = mov.ger_pessoa_endereco_id_expe
left join ger_cidade as expedidor_cidade on
  expedidor_cidade.id = expedidor_endereco.end_ger_cidade_id
left join ger_uf as expedidor_uf on
  expedidor_uf.id = expedidor_cidade.ger_uf_id
left join ger_pais as expedidor_pais on
  expedidor_pais.id = expedidor_uf.ger_pais_id
left join ger_pessoa AS expedidor on
  expedidor.unit_id = expedidor_endereco.unit_id
  and expedidor.id = expedidor_endereco.ger_pessoa_id

left join ger_pessoa_endereco AS recebedor_endereco on
  recebedor_endereco.unit_id = mov.unit_id
  and recebedor_endereco.id = mov.ger_pessoa_endereco_id_rece
left join ger_cidade as recebedor_cidade on
  recebedor_cidade.id = recebedor_endereco.end_ger_cidade_id
left join ger_uf as recebedor_uf on
  recebedor_uf.id = recebedor_cidade.ger_uf_id
left join ger_pais as recebedor_pais on
  recebedor_pais.id = recebedor_uf.ger_pais_id
left join ger_pessoa AS recebedor on
  recebedor.unit_id = recebedor_endereco.unit_id
  and recebedor.id = recebedor_endereco.ger_pessoa_id

left join ger_pessoa_endereco AS destinatario_endereco on
  destinatario_endereco.unit_id = mov.unit_id
  and destinatario_endereco.id = mov.ger_pessoa_endereco_id_dest
left join ger_cidade as destinatario_cidade on
  destinatario_cidade.id = destinatario_endereco.end_ger_cidade_id
left join ger_uf as destinatario_uf on
  destinatario_uf.id = destinatario_cidade.ger_uf_id
left join ger_pais as destinatario_pais on
  destinatario_pais.id = destinatario_uf.ger_pais_id
left join ger_pessoa AS destinatario on
  destinatario.unit_id = destinatario_endereco.unit_id
  and destinatario.id = destinatario_endereco.ger_pessoa_id

where
  mov.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
  and mov.id = $2;

-- busca os impostos do cte
select
	cst as icms_situacao_tributaria,
	valor_base_calc as icms_base_calculo,
	perc_aliquota as icms_aliquota,
	valor_imposto as icms_valor,
	0 as icms_reducao_base_calculo,
	0 as icms_base_calculo_retido_st,
	0 as icms_valor_retido_st,
	0 as icms_aliquota_retido_st,
	valor_credito_sn as icms_valor_credito_presumido
from
	fis_tributacao
join fis_tributo on
	fis_tributo.id = fis_tributacao.fis_tributo_id
	and fis_tributo.nr_tributo in ('1', '5')
where
	fis_tributacao.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
	and fis_tributacao.mov_itemserv_id = '72c48d02-813e-4fb3-9e4f-b1e3fe455f03'


-- busca os componentes_valor
select
  mov_comp.nome_comp AS nome,
  mov_comp.qnt_comp AS valor
from
  mov_comp
where
  mov_comp.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
  and mov_comp.mov_id = $2;

-- busca as quantidades
select
  ger_umedida.nr_umedida AS codigo_unidade_medida,
  mov_medida.tipo_medida,
  mov_medida.qnt_medida AS quantidade
from
  mov_medida
left join ger_umedida on
  ger_umedida.id = mov_medida.ger_umedida_id
where
  mov_medida.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
  and mov_medida.mov_id = $2;

-- busca as seguros_carga
select
  mov_seguradora.tipo_responsavel AS responsavel_seguro,
  ger_pessoa.nome AS nome_seguradora,
  mov_seguradora.nr_apolice AS numero_apolice 
from
  mov_seguradora
left join ger_pessoa on
  ger_pessoa.unit_id = mov_seguradora.unit_id
  and ger_pessoa.id = mov_seguradora.ger_pessoa_id_seguradora
where
  mov_seguradora.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
  and mov_seguradora.mov_id = $2;

-- busca as nfes
select
  mov_entrega_doc.chave_documento AS chave_nfe
from
  mov_entrega_doc
where
  mov_entrega_doc.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
  and mov_entrega_doc.mov_id = $2;

-- busca os dados do modal_rodoviario
select
  ger_empresa.doc_rntrc AS rntrc,
  mov.taf,
  ope_centro2_equip.nr_registro_estadual AS numero_registro_estadual,
  mov.tipo_fretamento,
  mov.data_entrada_saida AS data_inicio_viagem,

  ope_centro2_equip.placa,
  ope_centro2_equip.renavam,
  ger_pessoa.doc_cnpj AS cnpj_proprietario,
  ger_pessoa.doc_cpf AS cpf_proprietario,
  '' AS taf_proprietario,
  '' AS numero_registro_estadual_proprietario,
  ger_pessoa.razao_social AS razao_social_proprietario,
  ger_pessoa.doc_ie AS inscricao_estadual_proprietario,
  ger_uf.sigla_uf AS uf_proprietario,
  ope_centro2_equip.tipo_transp_auto_carga AS tipo_proprietario,
  veiculo_uf.sigla_uf AS uf_licenciamento
from
  mov
join ger_empresa on
  mov.unit_id = ger_empresa.unit_id
  and mov.ger_empresa_id = ger_empresa.id
left join mov_frete on
    mov_frete.unit_id = mov.unit_id
    and mov_frete.mov_id = mov.id
left join ope_centro2_equip on
  ope_centro2_equip.unit_id = mov_frete.unit_id
  and ope_centro2_equip.id = mov_frete.ope_centro2_id_equip
left join ope_centro2 on
  ope_centro2.unit_id = ope_centro2_equip.unit_id
  and ope_centro2.id = ope_centro2_equip.ope_centro2_id
left join ger_cidade as veiculo_cidade on
  veiculo_cidade.id = ope_centro2_equip.ger_cidade_id
left join ger_uf as veiculo_uf on
  veiculo_uf.id = veiculo_cidade.ger_uf_id
left join ger_pessoa_endereco on
  ger_pessoa_endereco.unit_id = ope_centro2.unit_id
  and ger_pessoa_endereco.id = ope_centro2.ger_pessoa_endereco_id
left join ger_cidade on
  ger_cidade.id = ger_pessoa_endereco.end_ger_cidade_id
left join ger_uf on
  ger_uf.id = ger_cidade.ger_uf_id
left join ger_pessoa on
  ger_pessoa.unit_id = ger_pessoa_endereco.unit_id
  and ger_pessoa.id = ger_pessoa_endereco.ger_pessoa_id
where
  mov.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
  and mov.id = $2;

-- busca os dados de identificação da mdfe
select
  mov.tipo_emissao_carga AS emitente,
  mov.tipo_transportador_carga AS tipo_transporte,
  fis_doc.serie,
  fis_doc.numero,
  mov.data_mov AS data_emissao,
  uf_carregamento.sigla_uf AS uf_inicio,
  uf_descarregamento.sigla_uf AS uf_fim,
  mov.valor_carga AS valor_total_carga,
  mov.tipo_umedida_carga AS codigo_unidade_medida_peso_bruto,
  mov.qnt_carga AS peso_bruto
from
  mov

left join fis_doc on
  fis_doc.unit_id = mov.unit_id
  and fis_doc.mov_id = mov.id
left join ger_cidade as cidade_carregamento on
  cidade_carregamento.id = mov.ger_cidade_id_carreg
left join ger_uf as uf_carregamento on
  uf_carregamento.id = cidade_carregamento.ger_uf_id
left join ger_cidade as cidade_descarregamento on
  cidade_descarregamento.id = mov.ger_cidade_id_descarreg
left join ger_uf as uf_descarregamento on
  uf_descarregamento.id = cidade_descarregamento.ger_uf_id
where
  mov.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
  and mov.id = $2;

-- busca os municipios_carregamento
select
  ger_cidade.nr_cidade AS codigo,
  ger_cidade.nome
from
  mov
join ger_cidade on
  ger_cidade.id = mov.ger_cidade_id_carreg
where
  mov.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
  and mov.id = $2;

-- percursos
select
  ger_uf.sigla_uf AS uf_percurso
from
  mov_percurso
join ger_cidade on
  ger_cidade.id = mov_percurso.ger_cidade_id
join ger_uf on
  ger_uf.id = ger_cidade.ger_uf_id
where
  mov_percurso.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
  and mov_percurso.mov_id = $2;

-- busca os municipios_descarregamento
select
  ger_cidade.nr_cidade AS codigo,
  ger_cidade.nome
from
  mov_entrega
join ger_cidade on
  ger_cidade.id = mov_entrega.ger_cidade_id
where
  mov_entrega.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
  and mov_entrega.mov_id = $2;

-- busca os conhecimentos_transporte
select
  mov_entrega_doc.chave_documento AS chave_cte
from
  mov_entrega_doc
where
  mov_entrega_doc.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
  and mov_entrega_doc.mov_id = $2
  and mov_entrega_doc.mov_entrega_id = $3
  and mov_entrega_doc.modelo_documento = '57';

  -- busca as notas_fiscais 
select
  mov_entrega_doc.chave_documento AS chave_nfe
from
  mov_entrega_doc
where
  mov_entrega_doc.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
  and mov_entrega_doc.mov_id = $2
  and mov_entrega_doc.mov_entrega_id = $3
  and mov_entrega_doc.modelo_documento = '55';

-- busca os seguros_carga
select
  mov_seguradora.tipo_responsavel AS responsavel_seguro,
  responsavel.doc_cnpj AS cnpj_responsavel,
  responsavel.doc_cpf AS cpf_responsavel,
  seguradora.nome AS nome_seguradora,
  seguradora.doc_cnpj AS cnpj_seguradora,
  mov_seguradora.nr_apolice AS numero_apolice,
  mov_seguradora.nr_averbacao AS numero_averbacao
from
  mov_seguradora
left join ger_pessoa AS seguradora on
  seguradora.unit_id = mov_seguradora.unit_id
  and seguradora.id = mov_seguradora.ger_pessoa_id_seguradora
left join ger_pessoa AS responsavel on
  responsavel.unit_id = mov_seguradora.unit_id
  and responsavel.id = mov_seguradora.ger_pessoa_id_responsavel
where
  mov_seguradora.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
  and mov_seguradora.mov_id = $2;

-- busca os dados do modal_rodoviario
select
  ger_empresa.doc_rntrc AS registro_nacional_transporte,
  ope_centro2_equip.id AS codigo_veiculo,
  ope_centro2_equip.placa AS placa_veiculo,
  ope_centro2_equip.renavam AS renavam_veiculo,
  ope_centro2_equip.tara AS tara_veiculo,
  ope_centro2_equip.capacidade_kg AS capacidade_kg_veiculo,
  ope_centro2_equip.capacidade_m3 AS capacidade_m3_veiculo,
  ope_centro2_equip.tipo_rodado AS tipo_rodado_veiculo,
  ope_centro2_equip.tipo_carroceria AS tipo_carroceria_veiculo,
  veiculo_uf.sigla_uf AS uf_licenciamento_veiculo,
  ger_pessoa.doc_cnpj AS cnpj_proprietario_veiculo,
  ger_pessoa.doc_cpf AS cpf_proprietario_veiculo,
  '' AS rntrc_proprietario_veiculo,
  ger_pessoa.razao_social AS razao_social_proprietario_veiculo,
  ger_pessoa.doc_ie AS inscricao_estadual_proprietario_veiculo,
  ger_uf.sigla_uf AS uf_proprietario_veiculo,
  ope_centro2_equip.tipo_transp_auto_carga AS tipo_proprietario_veiculo,
  veiculo_uf.sigla_uf AS uf_licenciamento_veiculo

from
  mov
join ger_empresa on
  mov.unit_id = ger_empresa.unit_id
  and mov.ger_empresa_id = ger_empresa.id
left join mov_frete on
  mov_frete.unit_id = mov.unit_id
  and mov_frete.mov_id = mov.id
left join ope_centro2_equip on
  ope_centro2_equip.unit_id = mov_frete.unit_id
  and ope_centro2_equip.id = mov_frete.ope_centro2_id_equip
left join ope_centro2 on
  ope_centro2.unit_id = ope_centro2_equip.unit_id
  and ope_centro2.id = ope_centro2_equip.ope_centro2_id
left join ger_cidade as veiculo_cidade on
  veiculo_cidade.id = ope_centro2_equip.ger_cidade_id
left join ger_uf as veiculo_uf on
  veiculo_uf.id = veiculo_cidade.ger_uf_id
left join ger_pessoa_endereco on
  ger_pessoa_endereco.unit_id = ope_centro2.unit_id
  and ger_pessoa_endereco.id = ope_centro2.ger_pessoa_endereco_id
left join ger_cidade on
  ger_cidade.id = ger_pessoa_endereco.end_ger_cidade_id
left join ger_uf on
  ger_uf.id = ger_cidade.ger_uf_id
left join ger_pessoa on
  ger_pessoa.unit_id = ger_pessoa_endereco.unit_id
  and ger_pessoa.id = ger_pessoa_endereco.ger_pessoa_id
where
  mov.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
  and mov.id = $2;

-- busca os condutores
select
  ger_pessoa.nome,
  ger_pessoa.doc_cpf AS cpf
from
  mov_condutor
left join ger_pessoa on
  ger_pessoa.unit_id = mov_condutor.unit_id
  and ger_pessoa.id = mov_condutor.ger_pessoa_id_condutor
where
  mov_condutor.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
  and mov_condutor.mov_id = $2;

-- busca os contratantes
select
  ger_pessoa.nome,
  ger_pessoa.doc_cpf AS cpf,
  ger_pessoa.doc_cnpj AS cnpj
from
  mov_tomador
left join ger_pessoa on
  ger_pessoa.unit_id = mov_tomador.unit_id
  and ger_pessoa.id = mov_tomador.ger_pessoa_id_responsavel
where
  mov_tomador.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
  and mov_tomador.mov_id = $2;

-- busca os veiculos_reboque
select
  ope_centro2_equip.id AS codigo,
  ope_centro2_equip.placa AS placa,
  ope_centro2_equip.renavam AS renavam,
  ope_centro2_equip.tara AS tara,
  ope_centro2_equip.capacidade_kg AS capacidade_kg,
  ope_centro2_equip.capacidade_m3 AS capacidade_m3,
  ope_centro2_equip.tipo_rodado AS tipo_rodado,
  ope_centro2_equip.tipo_carroceria AS tipo_carroceria,
  veiculo_uf.sigla_uf AS uf_licenciamento,
  ger_pessoa.doc_cnpj AS cnpj_proprietario,
  ger_pessoa.doc_cpf AS cpf_proprietario,
  '' AS rntrc_proprietario,
  ger_pessoa.razao_social AS razao_social_proprietario,
  ger_pessoa.doc_ie AS inscricao_estadual_proprietario,
  ger_uf.sigla_uf AS uf_proprietario,
  ope_centro2_equip.tipo_transp_auto_carga AS tipo_proprietario,
  veiculo_uf.sigla_uf AS uf_licenciamento

from
  mov_reboque
left join ope_centro2_equip on
  ope_centro2_equip.unit_id = mov_reboque.unit_id
  and ope_centro2_equip.id = mov_reboque.ope_centro2_id_equip
left join ope_centro2 on
  ope_centro2.unit_id = ope_centro2_equip.unit_id
  and ope_centro2.id = ope_centro2_equip.ope_centro2_id
left join ger_cidade as veiculo_cidade on
  veiculo_cidade.id = ope_centro2_equip.ger_cidade_id
left join ger_uf as veiculo_uf on
  veiculo_uf.id = veiculo_cidade.ger_uf_id
left join ger_pessoa_endereco on
  ger_pessoa_endereco.unit_id = ope_centro2.unit_id
  and ger_pessoa_endereco.id = ope_centro2.ger_pessoa_endereco_id
left join ger_cidade on
  ger_cidade.id = ger_pessoa_endereco.end_ger_cidade_id
left join ger_uf on
  ger_uf.id = ger_cidade.ger_uf_id
left join ger_pessoa on
  ger_pessoa.unit_id = ger_pessoa_endereco.unit_id
  and ger_pessoa.id = ger_pessoa_endereco.ger_pessoa_id
where
  mov_reboque.unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75'
  and mov_reboque.mov_id = $2;