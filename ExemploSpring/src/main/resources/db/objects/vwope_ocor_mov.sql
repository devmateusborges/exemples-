Drop View If Exists vwope_ocor_mov_dest_area;
Drop View If Exists vwope_ocor_mov_dest_equip;
Drop View If Exists vwope_ocor_mov_dest;

CREATE OR REPLACE VIEW vwope_ocor_mov  AS
select 
t1.unit_id,
t1.id as ope_ocor_mov_id,
t1.observacao as ope_ocor_mov_obs,
t1.data_mov as ope_ocor_mov_data_mov,
t1.numero as ope_ocor_mov_numero,
t1.ger_empresa_id as ope_ocor_mov_ger_empresa_id,
t1.ger_pessoa_endereco_id_exec as ope_ocor_mov_pes_endereco_id_exec,
t1.ope_ocor_tipo_id as ope_ocor_mov_ocor_tipo_id,

--
t2.id as ger_empresa_id,
t2.nome as ger_empresa_nome,
t2.razao_social as ger_empresa_razao_social,
t2.ativo as ger_empresa_ativo,
fnstd('SN','default',t2.ativo) as ger_empresa_ativo_desc,
t2.sigla_empresa as ger_empresa_sigla,
t2.doc_cnpj as ger_empresa_doc_cnpj,
t2.doc_cpf as ger_empresa_doc_cpf,

--
t3.id_endereco as ger_pessoa_endereco_id,
t3.endereco as ger_pessoa_endereco,
t3.endereco_numero as ger_pessoa_endereco_nr,
t3.cep_endereco as ger_pessoa_endereco_cep,
t3.id_cidade as ger_pessoa_endereco_id_cidade,
t3.nome_cidade as ger_pessoa_endereco_nome_cidade,
t3.uf_cidade  as ger_pessoa_endereco_uf,
t3.id_pessoa  as ger_pessoa_endereco_id_pes,
t3.nome_pessoa as ger_pessoa_endereco_nome_pes,
t3.doc_cnpj_cpf_pessoa as ger_pessoa_endereco_doc_pes,

--
t4.id as ope_ocor_tipo_id,
t4.nome as ope_ocor_tipo_nome,
t4.ativo as ope_ocor_tipo_ativo,
fnstd('SN','default',t4.ativo) as ope_ocor_tipo_ativo_desc,
t4.sigla_ocor_tipo as ope_ocor_tipo_sigla,
t4.tipo as ope_ocor_tipo_tp,
fnstd('AE','tipo',t4.tipo) as ope_ocor_tipo_tp_desc,
t4.obrig_ope_compart as ope_ocor_tipo_obrig,
fnstd('ope_ocor_tipo','obrig_ope_compart',t4.obrig_ope_compart) as ope_ocor_tipo_obrig_desc,

--
t5.id as ope_ocor_mov_det_id,
t5.observacao as ope_ocor_mov_det_obs,
t5.qnt_ocor as ope_ocor_mov_det_qnt_ocor,
t5.qnt_ocor_calc as ope_ocor_mov_det_qnt_ocor_calc,
t5.data_status as ope_ocor_mov_det_data_status,
t5.long_y as ope_ocor_mov_det_qnt_ocor_long_y,
t5.lat_x as ope_ocor_mov_det_qnt_ocor_lat_x,
t5.ponto as ope_ocor_mov_det_ocor_ponto,

--
t6.id as ope_ocor_id,
t6.nome as ope_ocor_nome,
t6.ativo as ope_ocor_ativo,
fnstd('SN','default',t6.ativo) as ope_ocor_ativo_desc,
t6.sigla_ocor as ope_ocor_sigla,
t6.icon as ope_ocor_icon,
t6.tipo as ope_ocor_tipo,
fnstd('AE','tipo',t6.tipo) as ope_ocor_tipo_desc,
t6.tipo_lanc as ope_ocor_tipo_lanc,
fnstd('ope_ocor','tipo_lanc',t6.tipo_lanc) as ope_ocor_tipo_lanc_desc,

--
t7.id as ope_ocor_grupo_id,
t7.nome as ope_ocor_grupo_nome,
t7.ativo as ope_ocor_grupo_ativo,
fnstd('SN','default',t7.ativo) as ope_ocor_grupo_ativo_desc,
t7.sigla_ocor_grupo as ope_ocor_grupo_sigla,

--
t8.id as ger_umedida_id,
t8.nome as ger_umedida_nome,
t8.ativo as ger_umedida_ativo,
fnstd('SN','default',t8.ativo) as ger_umedida_ativo_desc,
t8.sigla_umedida as ger_umedida_sigla,

--
t9.id as ope_ocor_status_id,
t9.nome as ope_ocor_status_nome,
t9.ativo as ope_ocor_status_ativo,
t9.sigla_ocor_status as ope_ocor_status_sigla,
t9.tipo_status as ope_ocor_status_tipo_status,
fnstd('ope_ocor_status','tipo_status',t9.tipo_status) as ope_ocor_status_tipo_status_desc,

--
t1.log_user_ins,
t1.log_date_ins,
t1.log_user_upd,
t1.log_date_upd,

--Sigla_desc
t2.sigla_empresa||' - '||t2.nome as ger_empresa_sigla_desc,
t4.sigla_ocor_tipo||' - '||t4.nome as ope_ocor_tipo_sigla_desc,
t6.sigla_ocor||' - '||t6.nome as ope_ocor_sigla_desc,
t7.sigla_ocor_grupo||' - '||t7.nome as ope_ocor_grupo_sigla_desc,
t8.sigla_umedida||' - '||t8.nome as ger_umedida_sigla_desc,
t9.sigla_ocor_status||' - '||t9.nome as ope_ocor_status_sigla_desc

from ope_ocor_mov t1

inner join ger_empresa t2
on t1.ger_empresa_id = t2.id

inner join vwger_pessoa t3
on t1.ger_pessoa_endereco_id_exec = t3.id_endereco

inner join ope_ocor_tipo t4
on t1.ope_ocor_tipo_id = t4.id

--
join ope_ocor_mov_det t5
on t5.ope_ocor_mov_id = t1.id

inner join ope_ocor t6
on t5.ope_ocor_id = t6.id

inner join ope_ocor_grupo t7
on t6.ope_ocor_grupo_id = t7.id

inner join ger_umedida t8
on t6.ger_umedida_id = t8.id

inner join ope_ocor_status t9
on t5.ope_ocor_status_id = t9.id

