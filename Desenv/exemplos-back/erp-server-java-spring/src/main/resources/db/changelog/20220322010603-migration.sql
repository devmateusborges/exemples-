        
        CREATE OR REPLACE FUNCTION public.fnsystem_psql_result(pid character varying, psystem_user_id character varying, presultado character varying, pstatus character varying default '')
        RETURNS character varying
        LANGUAGE plpgsql
       AS $function$
       declare 
           vRetornoJson varchar;	
       BEGIN
           --apaga as com mais de 24 horas de idade
           delete from system_psql_result where dt_hr <= NOW() - INTERVAL '24 HOUR';
       
           if (pstatus = '') then
               pstatus := 'S';
           END if;
       
           insert into system_psql_result(id, system_user_id, resultado, status) values (pid, psystem_user_id, presultado, pstatus);
       
           SELECT json_build_object('status','success', 'data','Sucesso') INTO vRetornoJson;
           return vRetornoJson;
           exception
               when others then
                   begin
                   SELECT json_build_object(
                       'status', 'error',
                       'message', sqlerrm) INTO vRetornoJson;
                return vRetornoJson;
               end;   
           
       END;
       $function$;;
       
       
       
       -----------
       
       
       

       CREATE OR REPLACE FUNCTION fnutil_last_day(date)
               RETURNS date AS
               $function$
               SELECT (date_trunc('MONTH', $1) + INTERVAL '1 MONTH - 1 day')::date;
               $function$ LANGUAGE 'sql'
               IMMUTABLE STRICT;;
       
       
       -----------
       
       

       drop function if exists public.fnutil_ini_fim_semana;
       

       CREATE OR REPLACE FUNCTION public.fnutil_ini_fim_semana(p_ger_empresa_id character varying, p_dt_ini date, p_dt_fin integer)
        RETURNS date
        LANGUAGE plpgsql
       AS $function$
       declare
           v_ini_semana integer;
           v_day_of_week integer;
           v_date date;
       begin
       -- Recuperando configuração de início da semana
           select coalesce(ini_semana,0)
           into v_ini_semana
           from ger_empresa t
           where t.id = p_ger_empresa_id;
           v_day_of_week := EXTRACT(DOW from p_dt_ini);
       
           -- data de início da semana
           if p_dt_fin = 0 then
           if (v_day_of_week >= v_ini_semana) then
               v_date := p_dt_ini - (v_day_of_week - v_ini_semana);
           else
               v_date := p_dt_ini - (v_day_of_week - v_ini_semana + 7);
           end if;
           end if;
       
           -- data de Fin da semana
           if p_dt_fin = 1 then
           if (v_ini_semana <= v_day_of_week) then
               v_date := p_dt_ini + (v_ini_semana - v_day_of_week + 6);
           else
               v_date := p_dt_ini + (v_ini_semana - v_day_of_week - 1);
           end if;
           end if;
       
           return v_date;
       exception
           when others then
           Return 'fnutil_ini_fim_semana ERRO: ' || sqlerrm;
       end;
       $function$;;
       
       
       
       -----------
       
       
       

       create or replace function fnutil_formatcpfcnpj(pgerPessoaId varchar,pFormatado boolean)
         RETURNS varchar as $BODY$
       declare
        Vsql varchar;
       begin
               IF pFormatado = TRUE THEN		
                       select
                        (CASE 
                           WHEN p1.doc_cnpj is null THEN regexp_replace(
                           LPAD(p1.doc_cpf, 11),
                           '([0-9]{3})([0-9]{3})([0-9]{3})','\\1.\\2.\\3-')
                           WHEN p1.doc_cpf is null THEN regexp_replace(
                           LPAD(p1.doc_cnpj, 14),'([0-9]{2})([0-9]{3})([0-9]{3})([0-9]{4})','\\1.\\2.\\3/\\4-')
                           WHEN p1.doc_cnpj is not null and p1.doc_cpf is not null THEN regexp_replace(
                           LPAD(p1.doc_cnpj, 14),'([0-9]{2})([0-9]{3})([0-9]{3})([0-9]{4})','\\1.\\2.\\3/\\4-')||
                           ' || '||regexp_replace(LPAD(p1.doc_cpf, 11),'([0-9]{3})([0-9]{3})([0-9]{3})','\\1.\\2.\\3-')
                           ELSE '' END) into Vsql 
                   from ger_pessoa p1 where p1.id = pgerPessoaId;
               
               ELSE
                       select 
                                (CASE 
                                   WHEN p1.doc_cnpj is null THEN p1.doc_cpf
                                   WHEN p1.doc_cpf is null THEN p1.doc_cnpj
                                   WHEN p1.doc_cnpj is not null and p1.doc_cpf is not null THEN p1.doc_cnpj||' || '||p1.doc_cpf
                                   ELSE ''
                                   END
                               ) into vSql
                        from ger_pessoa p1 where p1.id = pgerPessoaId;
               end if;	
             
               return Vsql;
       end;
       $BODY$
       LANGUAGE plpgsql VOLATILE;;
       
       
       -----------
       
       
       

       CREATE OR REPLACE FUNCTION fnstd(ptablename text, pfieldname text, pvaluetype text)
         RETURNS varchar AS $BODY$
       declare
       vSql varchar;
       BEGIN
           
           
           select 
               t1.description_type into vSql
         from system_type_description t1
           where t1.table_name = pTableName
           and t1.field_name = pFieldName
           and t1.value_type = pValueType;
           
           return vSql;
           
       END;
       $BODY$
         LANGUAGE plpgsql VOLATILE;;
           
       
       
       -----------
       
       
       
       DROP VIEW If EXISTS public.vwbor_bor_mov;

       CREATE OR REPLACE VIEW public.vwbor_bor_mov
       AS SELECT a.id,
           a.id_tipo,
           a.numero_serie,
           a.ibutton_rfid,
           a.dthr_track,
           a.gps_altitude,
           a.gps_altitude_status,
           a.gps_lat,
           a.gps_long,
           a.gps_angulo_norte,
           a.gps_posicao_status,
           a.gps_velocidade,
           a.gps_velocidade_media,
           a.equipamento_ignicao,
           a.equipamento_bateria,
           a.equipamento_odometro,
           a.equipamento_rpm,
           a.equipamento_veloc,
           a.equipamento_veloc_odom,
           a.equipamento_veloc_odom_media,
           a.log_user_ins,
           a.log_date_ins,
           a.log_user_upd,
           a.log_date_upd,
           a.geom,
           a.ope_centro2_equip_id_1,
           b.nome as ope_centro2_equip_nome_1, 
           a.ope_centro2_equip_id_2,
           c.nome as ope_centro2_equip_nome_2,
           a.ope_centro2_pessoa_id,
           d.nome as ope_centro2_pessoa_nome,
           a.ger_empresa_id,
           a.ope_centro2_area_id,
           a.buzzer,
           a.unit_id,
           fnstd('bor_mov'::text, 'status'::text, a.status::text) AS status_desc,
           a.status,
           a.dthr_status,
           a.ope_atividade_id,
           a.qnt_ha_trab,
           a.duracao,
           e.sigla_centro2 as sigla_equipamento
          FROM bor_mov a
          LEFT JOIN bor_dispositivo b on b.ope_centro2_equip_id = a.ope_centro2_equip_id_1
          left join ope_centro2     e on e.id = a.ope_centro2_equip_id_1
          LEFT JOIN bor_dispositivo c on c.ope_centro2_equip_id = a.ope_centro2_equip_id_2
          LEFT JOIN bor_dispositivo d on d.ope_centro2_pessoa_id = a.ope_centro2_pessoa_id
         GROUP BY a.id, a.id_tipo, a.numero_serie, a.ibutton_rfid, a.dthr_track, a.gps_altitude, a.gps_altitude_status, 
        a.gps_lat, a.gps_long, a.gps_angulo_norte, a.gps_posicao_status, a.gps_velocidade, a.gps_velocidade_media, 
       a.equipamento_ignicao, a.equipamento_bateria, a.equipamento_odometro, a.equipamento_rpm, a.equipamento_veloc, 
       a.equipamento_veloc_odom, a.equipamento_veloc_odom_media, a.log_user_ins, a.log_date_ins, a.log_user_upd, 
       a.log_date_upd, a.geom, a.ope_centro2_equip_id_1, a.ope_centro2_equip_id_2, a.ope_centro2_pessoa_id, 
       a.ger_empresa_id, a.ope_centro2_area_id, a.buzzer, a.unit_id, a.status, a.dthr_status, 
       a.ope_atividade_id, a.qnt_ha_trab, a.duracao, b.nome, c.nome, d.nome, e.sigla_centro2;;
       
       -- Permissions
       
       ALTER TABLE public.vwbor_bor_mov OWNER TO rf;;
       GRANT ALL ON TABLE public.vwbor_bor_mov TO rf;;
       
       
       
       -----------
       
       
       
       Drop View If Exists vwger_itemserv;

       CREATE OR REPLACE VIEW vwger_itemserv  AS
       select 
       t1.unit_id as ger_itemserv_unitid,
       t1.id as ger_itemserv_id,
       t1.nome as ger_itemserv_nome,
       t1.ativo as ger_itemserv_ativo,
       fnstd('SN','default',t1.ativo) as ger_itemserv_ativo_desc,
       t1.tipo as ger_itemserv_tipo,
       fnstd('ger_itemserv','tipo',t1.tipo) as ger_itemserv_tipo_desc,
       t1.origem_fiscal as ger_itemserv_origem_fiscal,
       t1.nome_alternativo as ger_itemserv_nome_alternativo,
       t1.tipo_composicao as ger_itemserv_tipo_composicao,
       fnstd('ger_itemserv', 'tipo_composicao', t1.tipo_composicao) as ger_itemserv_tipo_composicao_desc,
       t1.sigla_itemserv as ger_itemserv_sigla,
       t1.tipo_ctb_comp as ger_itemserv_tipo_ctb_comp,
       fnstd('ger_itemserv','tipo_ctb_comp',t1.tipo_ctb_comp) as ger_itemserv_tipo_ctb_comp_desc,
       t1.fis_sigla_servico  as ger_itemserv_sigla_serviço,
       t1.fis_doc_cnae_nfs as ger_itemserv_fis_doc_cnae_nfs,
       t1.fis_sigla_servico_municipio as ger_itemserv_fis_sigla_servico_municipio,
       t2.id as ger_itemserv_subgrupo_id,
       t2.nome as ger_itemserv_subgrupo_nome,
       t2.ativo as ger_itemserv_subgrupo_ativo,
       fnstd('SN','default',t2.ativo) as ger_itemserv_subgrupo_ativo_desc,
       
       t3.id  as ger_itemserv_grupo_id,
       t3.nome as ger_itemserv_grupo_nome,
       t3.ativo as ger_itemserv_grupo_ativo,
       fnstd('SN','default',t3.ativo) as ger_itemserv_grupo_ativo_desc,
       
       t4.id as fis_ncm_id,
       t4.nome as fis_ncm_nome,
       t4.ativo as fis_ncm_ativo,
       fnstd('SN','default',t4.ativo) as fis_ncm_ativo_desc,
       t4.data_validade as fis_ncm_dt_validade,
       t4.nr_ncm as fis_ncm_nr_ncm,
       
       t5.id as ger_umedida_id,
       t5.nome as ger_umedida_nome,
       t5.ativo as ger_umedida_ativo,
       fnstd('SN','default',t5.ativo) as ger_umedida_ativo_desc,
       t5.sigla_umedida as ger_umedida_sigla,
       t5.nr_umedida as ger_umedida_nr_umedida,
       
       t6.id as fis_cest_id,
       t6.nome as fis_cest_nome,
       t6.ativo as fis_cest_ativo,
       fnstd('SN','default',t6.ativo) as fis_cest_ativo_desc,
       t6.data_validade as fis_cest_dt_validade,
       t6.nr_cest as fis_cest_nr_cest,
       
       t7.id as fis_nbs_id,
       t7.nome as fis_nbs_nome,
       t7.ativo as fis_nbs_ativo,
       fnstd('SN','default',t7.ativo) as fis_nbs_ativo_desc,
       t7.data_validade as fis_nbs_dt_validade,
       t7.nr_nbs as fis_nbs_nr_nbs,
       
       t8.id as ctb_comp_id,
       t8.nome as ctb_comp_nome,
       t8.ativo as ctb_comp_ativo,
       fnstd('SN','default',t8.ativo) as ctb_comp_ativo_desc,
       t8.sigla_comp as ctb_comp_sigla,
       t8.fator_calc_origem as ctb_comp_fator_calc_origem,
       
       t1.log_user_ins,
       t1.log_date_ins,
       t1.log_user_upd,
       t1.log_date_upd,
       
       t1.sigla_itemserv||' - '||t1.nome as ger_itemserv_sigla_desc,
       t5.sigla_umedida||' - '||t5.nome as ger_umedida_sigla_desc,
       t8.sigla_comp||' - '||t8.nome as ctb_comp_sigla_desc
       
       
       from ger_itemserv t1
       inner join ger_itemserv_subgrupo t2
       on t1.ger_itemserv_subgrupo_id = t2.id
       inner join ger_itemserv_grupo t3
       on t2.ger_grupo_id = t3.id
       left join fis_ncm t4
       on t1.fis_ncm_id = t4.id
       inner join ger_umedida t5
       on  t1.ger_umedida_id = t5.id
       inner join fis_cest t6
       on t1.fis_cest_id = t6.id
       left join fis_nbs t7
       on t1.fis_nbs_id = t7.id
       left join ctb_comp t8
       on t1.ctb_comp_id = t8.id;;
       
       
       
       
       -----------
       
       
       
       -- Verificar Inserção de Type Description 
       DROP View IF EXISTS vwmov_mov;;

       CREATE OR REPLACE VIEW vwmov_mov AS
       select 
       t1.unit_id as mov_unit_id,
       t1.id as mov_id,
       t1.nr_externo as mov_nr_externo,
       t1.ger_pessoa_id as mov_ger_pessoa_id,
       t1.ger_pessoa_endereco_id_fiscal as mov_ger_pessoa_endereco_id_fiscal,
       t1.mov_operacao_id as mov_mov_operacao_id,
       t1.fin_cond_pagrec_id as mov_fin_cond_pagrec_id,
       t1.data_mov as mov_data_mov,
       t1.numero_mov as mov_numero_mov,
       t1.data_emissao as mov_data_emissao,
       t1.fis_doc_tipo_id as mov_fis_doc_tipo_id,
       t1.serie_mov as mov_serie_mov,
       t1.mov_status_id as mov_mov_status_id,
       t1.valor_total as mov_valor_total,
       t1.observacao as mov_observacao,
       t1.tipo_frete as mov_tipo_frete,
       fnstd('mov','tipo_frete',(t1.tipo_frete)::VARCHAR) as mov_tipo_frete_desc,
       t1.data_entrega as mov_data_entrega,
       t1.data_entrada_saida as mov_data_entrada_saida,
       t1.ger_pessoa_endereco_id_entrega as mov_ger_pessoa_endereco_id_entrega,
       t1.ger_cidade_id_carreg as mov_ger_cidade_id_carreg,
       t1.tipo_emissao_carga as mov_tipo_emissao_carga,
       fnstd('mov','tipo_emissao_carga',(t1.tipo_emissao_carga)::VARCHAR) as mov_tipo_emissao_carga_desc,
       t1.tipo_modal_carga as mov_tipo_modal_carga,
       t1.tipo_transportador_carga as mov_tipo_transportador_carga,
       t1.valor_carga as mov_valor_carga,
       t1.tipo_umedida_carga as mov_tipo_umedida_carga,
       fnstd('mov','tipo_umedida_carga',t1.tipo_umedida_carga) as mov_tipo_umedida_carga_desc,
       t1.qnt_carga as mov_qnt_carga,
       t1.ger_empresa_id as mov_empresa_id,
       t1.ger_pessoa_endereco_id_reme as mov_pessoa_endereco_id_reme,
       t1.ger_pessoa_endereco_id_dest as mov_pessoa_endereco_id_dest,
       t1.ger_pessoa_endereco_id_rece as mov_pessoa_endereco_id_rece,
       t1.ger_pessoa_endereco_id_expe as mov_pessoa_endereco_id_expe,
       t1.observacao_transp as mov_obs_transp,
       t1.observacao_serv as mov_obs_serv,
       t1.tipo_fretamento as mov_tipo_fretamento,
       t1.tipo_serv_frete as mov_tipo_serv_frete,
       t1.tipo_tomador_serv_frete as mov_tipo_tomador_serv_frete,
       t1.taf as mov_taf,
       t1.data_anulacao as mov_data_anulacao,
       t1.observacao_item as mov_observacao_item,
       t1.valor_financeiro_total as mov_valor_financeiro_total,
       t1.valor_item_frete_total as mov_valor_item_frete_total,
       t1.observacao_fiscal as mov_observacao_fiscal,
       t1.ger_pessoa_endereco_id_inter as mov_pessoa_endereco_id_inter,
       t1.fis_tipo_resp_reten as mov_fis_tipo_resp_reten,
       fnstd('mov','fis_tipo_resp_reten',t1.fis_tipo_resp_reten) as mov_fis_tipo_resp_reten_desc,
       t1.fis_exig_iss_nfs as mov_fis_exig_iss_nfs,
       fnstd('mov','fis_exig_iss_nfs',t1.fis_exig_iss_nfs) as mov_fis_exig_iss_nfs_desc,
       t1.fis_iss_retido_nfs as mov_fis_iss_retido_nfs,
       fnstd('SN','default',t1.fis_iss_retido_nfs) as mov_fis_iss_retido_nfs_desc,
       t1.fis_nat_ope_nfs as mov_fis_nat_ope_nfs,
       fnstd('mov','fis_nat_ope_nfs',t1.fis_nat_ope_nfs) as mov_fis_nat_ope_nfs_desc,
       t1.numero_mov_pre as mov_numero_mov_pre,
       t1.serio_mov_pre as mov_serio_mov_pre,
       t1.cep_carreg as mov_cep_carreg,
       t1.cep_descarreg as mov_cep_descarreg,
       t1.tipo_carga as mov_tipo_carga,
       fnstd('mov','tipo_carga',t1.tipo_carga) as mov_tipo_carga_desc,
       t1.system_user_id_resp as mov_system_user_id_resp,
       
       -- Ger Pessoa
       t2.id as ger_pessoa_id,
       t2.nome as ger_pessoa_nome,
       t2.ativo as ger_pessoa_ativo,
       fnstd('SN','default',t2.ativo) as ger_pessoa_ativo_desc,
       t2.doc_cpf as ger_pessoa_doc_cpf,
       t2.doc_cnpj as ger_pessoa_doc_cnpj,
       fnutil_formatcpfcnpj(t2.id, true) as ger_pessoa_doc_cpf_cnpj_desc,
       t2.sigla_pes as ger_pessoa_sigla_pes,
       t2.fone_1 as ger_pessoa_fone_1,
       t2.contato_1 as ger_pessoa_contato_1,
       
       -- Ger Pessoa Endereco
       t3.id as ger_pessoa_endereco_id,
       t3.ativo as ger_pessoa_endereco_ativo,
       fnstd('SN','default',t3.ativo) as ger_pessoa_endereco_ativo_desc,
       t3.tipo as ger_pessoa_endereco_tipo,
       fnstd('ger_pessoa_endereco','tipo',t3.tipo) as ger_pessoa_endereco_tipo_desc,
       t3.padrao as ger_pessoa_endereco_padrao,
       fnstd('SN','default',t3.padrao) as ger_pessoa_endereco_padrao_desc,
       t3.end_logradouro as ger_pessoa_endereco_end_lograd,
       t3.end_logradouro_nr as ger_pessoa_endereco_lograd_nr,
       t3.end_bairro as ger_pessoa_endereco_end_bairro,
       t3.end_cep as ger_pessoa_endereco_end_cep,
       
       -- Mov Operacao
       t4.id as mov_operacao_id,
       t4.nome as mov_operacao_nome,
       t4.ativo as mov_operacao_ativo,
       fnstd('SN','default',t4.ativo) as mov_operacao_ativo_desc,
       t4.sigla_mov_operacao as mov_operacao_sigla,
       t4.finalidade_doc as mov_operacao_finalidade_doc,
       t4.tipo_es as mov_operacao_tipo_es,
       fnstd('default','tipo_es',t4.tipo_es) as mov_operacao_tipo_es_desc,
       -- 
       -- -- Mov Tipo
       t5.id as mov_tipo_id,
       t5.nome as mov_tipo_nome,
       t5.ativo as mov_tipo_ativo,
       fnstd('SN','default',t5.ativo) as mov_tipo_ativo_desc,
       t5.sigla_mov_tipo as mov_tipo_sigla,
       t5.tipo_mov as mov_tipo_tipo_mov,
       
       -- Ger Numeracao
       t6.id as ger_numeracao_id,
       t6.nome as ger_numeracao_nome,
       t6.ativo as ger_numeracao_ativo,
       fnstd('SN','default',t6.ativo) as ger_numeracao_ativo_desc,
       t6.serie as ger_numeracao_serie,
       t6.ultimo_nr as ger_numeracao_ultimo_nr,
       
       -- Fin Cond Pagrec
       t7.id as fin_cond_pagrec_id,
       t7.nome as fin_cond_pagrec_nome,
       t7.ativo as fin_cond_pagrec_ativo,
       fnstd('SN','default',t7.ativo) as fin_cond_pagrec_ativo_desc,
       t7.sigla_cond_pagamento as fin_cond_pagrec_sigla,
       t7.considera_feriado as fin_cond_pagrec_considera_feriado,
       fnstd('SN','default',t7.considera_feriado) as fin_cond_pagrec_considera_feriado_desc,
       t7.considera_final_sem as fin_cond_pagrec_considera_final_sem,
       fnstd('SN','default',t7.considera_final_sem) as fin_cond_pagrec_considera_final_sem_desc,
       t7.qnt_dia_ini as fin_cond_pagrec_qnt_dia_ini,
       t7.observacao as fin_cond_pagrec_obs,
       t7.tipo_prazo as fin_cond_pagrec_tipo_prazo,
       
       -- Fis Doc Tipo
       t8.id as fis_doc_tipo_id,
       t8.nome as fis_doc_tipo_nome,
       t8.ativo as fis_doc_tipo_ativo,
       fnstd('SN','default',t8.ativo) as fis_doc_tipo_ativo_desc,
       t8.modelo as fis_doc_tipo_modelo,
       
       --Mov Status
       t9.id as mov_status_id,
       t9.nome as mov_status_nome,
       t9.ativo as mov_status_ativo,
       fnstd('SN','default',t9.ativo) as mov_status_ativo_desc,
       t9.sigla_mov_status as mov_status_sigla,
       t9.tipo_status as mov_status_tipo_status,
       fnstd('mov_status','tipo_status',t9.tipo_status) as mov_status_tipo_status_desc,
       
       --endereco Entrega
       t10.id as ger_pessoa_endereco_entrega_id,
       t10.ativo as ger_pessoa_endereco_entrega_ativo,
       fnstd('SN','default',t10.ativo) as ger_pessoa_endereco_entrega_ativo_desc,
       t10.tipo as ger_pessoa_endereco_entrega_tipo,
       fnstd('ger_pessoa_endereco','tipo',t10.tipo) as ger_pessoa_endereco_entrega_tipo_desc,
       t10.padrao as ger_pessoa_endereco_entrega_padrao,
       fnstd('SN','default',t10.padrao) as ger_pessoa_endereco_entrega_padrao_desc,
       t10.end_logradouro as ger_pessoa_endereco_entrega_end_lograd,
       t10.end_logradouro_nr as ger_pessoa_endereco_entrega_end_lograd_nr,
       t10.end_bairro as ger_pessoa_endereco_entrega_end_bairro,
       t10.end_complemento as ger_pessoa_endereco_entrega_end_complemento,
       t10.end_cep as ger_pessoa_endereco_entrega_end_cep,
       
       --- Pessoa end Entrega
       t11.id as ger_pessoa_entrega_id,
       t11.nome as ger_pessoa_entrega_nome,
       t11.ativo as ger_pessoa_entrega_ativo,
       fnstd('SN','default',t11.ativo) as ger_pessoa_entrega_ativo_desc,
       t11.doc_cpf as ger_pessoa_entrega_doc_cpf,
       t11.doc_cnpj as ger_pessoa_entrega_doc_cnpj,
       fnutil_formatcpfcnpj(t11.id, true) as ger_pessoa_entrega_doc_cpf_cnpj_desc,
       t11.sigla_pes as ger_pessoa_entrega_sigla,
       
       -- Ger Cidade Carregamento
       t12.id as ger_cidade_carreg_id,
       t12.nome as ger_cidade_carreg_nome,
       t12.ativo as ger_cidade_carreg_ativo,
       fnstd('SN','default',t12.ativo) as ger_cidade_carreg_ativo_desc,
       t12.nr_cidade as ger_cidade_carreg_nr_cidade,
       
       -- Ger UF Carregamento
       t13.id as ger_uf_carreg_id,
       t13.nome as ger_uf_carreg_nome,
       t13.ativo as ger_uf_carreg_ativo,
       fnstd('SN','default',t13.ativo) as ger_uf_carreg_ativo_desc,
       t13.nr_uf as ger_uf_carreg_nr_uf,
       t13.sigla_uf as ger_uf_carreg_sigla,
       
       -- Ger Cidade Descarregamento
       t14.id as ger_cidade_descarreg_id,
       t14.nome as ger_cidade_descarreg_nome,
       t14.ativo as ger_cidade_descarreg_ativo,
       fnstd('SN','default',t14.ativo) as ger_cidade_descarreg_ativo_desc,
       t14.nr_cidade as ger_cidade_descarreg_nr_cidade,
       
       -- Ger UF Descarregamento
       t15.id as ger_uf_descarreg_id,
       t15.nome as ger_uf_descarreg_nome,
       t15.ativo as ger_uf_descarreg_ativo,
       fnstd('SN','default',t15.ativo) as ger_uf_descarreg_ativo_desc,
       t15.nr_uf as ger_uf_descarreg_nr_uf,
       t15.sigla_uf as ger_uf_descarreg_sigla,
       
       -- Empresa
       t16.id as ger_empresa_id,
       t16.nome as ger_empresa_nome,
       t16.ativo as ger_empresa_ativo,
       fnstd('SN','default',t16.ativo) as ger_empresa_ativo_desc,
       t16.sigla_empresa as ger_empresa_sigla,
       
       -- Endereco Rementente
       t17.id as ger_pessoa_endereco_reme_id,
       t17.ativo as ger_pessoa_endereco_reme_ativo,
       fnstd('SN','default',t17.ativo) as ger_pessoa_endereco_reme_ativo_desc,
       t17.tipo as ger_pessoa_endereco_reme_tipo,
       fnstd('ger_pessoa_endereco','tipo',t17.tipo) as ger_pessoa_endereco_reme_tipo_desc,
       t17.padrao as ger_pessoa_endereco_reme_padrao,
       fnstd('SN','default',t17.padrao) as ger_pessoa_endereco_reme_padrao_desc,
       t17.end_logradouro as ger_pessoa_endereco_reme_end_lograd,
       t17.end_logradouro_nr as ger_pessoa_endereco_reme_end_lograd_nr,
       t17.end_bairro as ger_pessoa_endereco_reme_end_bairro,
       t17.end_complemento as ger_pessoa_endereco_reme_end_complemento,
       t17.end_cep as ger_pessoa_endereco_reme_end_cep,
       
       --- Pessoa end Rementente
       t18.id as ger_pessoa_reme_id,
       t18.nome as ger_pessoa_reme_nome,
       t18.ativo as ger_pessoa_reme_ativo,
       fnstd('SN','default',t18.ativo) as ger_pessoa_reme_ativo_desc,
       t18.doc_cpf as ger_pessoa_reme_doc_cpf,
       t18.doc_cnpj as ger_pessoa_reme_doc_cnpj,
       fnutil_formatcpfcnpj(t18.id, true) as ger_pessoa_reme_doc_cpf_cnpj_desc,
       t18.sigla_pes as ger_pessoa_reme_sigla,
       
       -- Endereco Destinatário
       t19.id as ger_pessoa_endereco_dest_id,
       t19.ativo as ger_pessoa_endereco_dest_ativo,
       fnstd('SN','default',t19.ativo) as ger_pessoa_endereco_dest_ativo_desc,
       t19.tipo as ger_pessoa_endereco_dest_tipo,
       fnstd('ger_pessoa_endereco','tipo',t19.tipo) as ger_pessoa_endereco_dest_tipo_desc,
       t19.padrao as ger_pessoa_endereco_dest_padrao,
       fnstd('SN','default',t19.padrao) as ger_pessoa_endereco_dest_padrao_desc,
       t19.end_logradouro as ger_pessoa_endereco_dest_end_lograd,
       t19.end_logradouro_nr as ger_pessoa_endereco_dest_end_lograd_nr,
       t19.end_bairro as ger_pessoa_endereco_dest_end_bairro,
       t19.end_complemento as ger_pessoa_endereco_dest_end_complemento,
       t19.end_cep as ger_pessoa_endereco_dest_end_cep,
       
       --- Pessoa end Destinatário
       t20.id as ger_pessoa_dest_id,
       t20.nome as ger_pessoa_dest_nome,
       t20.ativo as ger_pessoa_dest_ativo,
       fnstd('SN','default',t20.ativo) as ger_pessoa_dest_ativo_desc,
       t20.doc_cpf as ger_pessoa_dest_doc_cpf,
       t20.doc_cnpj as ger_pessoa_dest_doc_cnpj,
       fnutil_formatcpfcnpj(t20.id, true) as ger_pessoa_dest_doc_cpf_cnpj_desc,
       t20.sigla_pes as ger_pessoa_dest_sigla,
       
       
       -- Endereco Recebedor
       t21.id as ger_pessoa_endereco_rece_id,
       t21.ativo as ger_pessoa_endereco_rece_ativo,
       fnstd('SN','default',t21.ativo) as ger_pessoa_endereco_rece_ativo_desc,
       t21.tipo as ger_pessoa_endereco_rece_tipo,
       fnstd('ger_pessoa_endereco','tipo',t21.tipo) as ger_pessoa_endereco_rece_tipo_desc,
       t21.padrao as ger_pessoa_endereco_rece_padrao,
       fnstd('SN','default',t21.padrao) as ger_pessoa_endereco_rece_padrao_desc,
       t21.end_logradouro as ger_pessoa_endereco_rece_end_lograd,
       t21.end_logradouro_nr as ger_pessoa_endereco_rece_end_lograd_nr,
       t21.end_bairro as ger_pessoa_endereco_rece_end_bairro,
       t21.end_complemento as ger_pessoa_endereco_rece_end_complemento,
       t21.end_cep as ger_pessoa_endereco_rece_end_cep,
       
       --- Pessoa end Recebedor
       t22.id as ger_pessoa_rece_id,
       t22.nome as ger_pessoa_rece_nome,
       t22.ativo as ger_pessoa_rece_ativo,
       fnstd('SN','default',t22.ativo) as ger_pessoa_rece_ativo_desc,
       t22.doc_cpf as ger_pessoa_rece_doc_cpf,
       t22.doc_cnpj as ger_pessoa_rece_doc_cnpj,
       fnutil_formatcpfcnpj(t22.id, true) as ger_pessoa_rece_doc_cpf_cnpj_desc,
       t22.sigla_pes as ger_pessoa_rece_sigla,
       
       -- Endereco Expedidor
       t23.id as ger_pessoa_endereco_expe_id,
       t23.ativo as ger_pessoa_endereco_expe_ativo,
       fnstd('SN','default',t23.ativo) as ger_pessoa_endereco_expe_ativo_desc,
       t23.tipo as ger_pessoa_endereco_expe_tipo,
       fnstd('ger_pessoa_endereco','tipo',t23.tipo) as ger_pessoa_endereco_expe_tipo_desc,
       t23.padrao as ger_pessoa_endereco_expe_padrao,
       fnstd('SN','default',t23.padrao) as ger_pessoa_endereco_expe_padrao_desc,
       t23.end_logradouro as ger_pessoa_endereco_expe_end_lograd,
       t23.end_logradouro_nr as ger_pessoa_endereco_expe_end_lograd_nr,
       t23.end_bairro as ger_pessoa_endereco_expe_end_bairro,
       t23.end_complemento as ger_pessoa_endereco_expe_end_complemento,
       t23.end_cep as ger_pessoa_endereco_expe_end_cep,
       
       --- Pessoa end Expedidor
       t24.id as ger_pessoa_expe_id,
       t24.nome as ger_pessoa_expe_nome,
       t24.ativo as ger_pessoa_expe_ativo,
       fnstd('SN','default',t24.ativo) as ger_pessoa_expe_ativo_desc,
       t24.doc_cpf as ger_pessoa_expe_doc_cpf,
       t24.doc_cnpj as ger_pessoa_expe_doc_cnpj,
       fnutil_formatcpfcnpj(t24.id, true) as ger_pessoa_expe_doc_cpf_cnpj_desc,
       t24.sigla_pes as ger_pessoa_expe_sigla,
       
       -- Endereco  Intermediário
       t25.id as ger_pessoa_endereco_inter_id,
       t25.ativo as ger_pessoa_endereco_inter_ativo,
       fnstd('SN','default',t25.ativo) as ger_pessoa_endereco_inter_ativo_desc,
       t25.tipo as ger_pessoa_endereco_inter_tipo,
       fnstd('ger_pessoa_endereco','tipo',t25.tipo) as ger_pessoa_endereco_inter_tipo_desc,
       t25.padrao as ger_pessoa_endereco_inter_padrao,
       fnstd('SN','default',t25.padrao) as ger_pessoa_endereco_inter_padrao_desc,
       t25.end_logradouro as ger_pessoa_endereco_inter_end_lograd,
       t25.end_logradouro_nr as ger_pessoa_endereco_inter_end_lograd_nr,
       t25.end_bairro as ger_pessoa_endereco_inter_end_bairro,
       t25.end_complemento as ger_pessoa_endereco_inter_end_complemento,
       t25.end_cep as ger_pessoa_endereco_inter_end_cep,
       
       --- Pessoa end  Intermediário
       t26.id as ger_pessoa_inter_id,
       t26.nome as ger_pessoa_inter_nome,
       t26.ativo as ger_pessoa_inter_ativo,
       fnstd('SN','default',t26.ativo) as ger_pessoa_inter_ativo_desc,
       t26.doc_cpf as ger_pessoa_inter_doc_cpf,
       t26.doc_cnpj as ger_pessoa_inter_doc_cnpj,
       fnutil_formatcpfcnpj(t26.id, true) as ger_pessoa_inter_doc_cpf_cnpj_desc,
       t26.sigla_pes as ger_pessoa_inter_sigla,
       
       t27.id as system_user_id,
       t27.name as system_user_name,
       t27.login as system_user_login,
       t27.active as system_user_ativo,
       fnstd('SN','default',t27.active) as system_user_ativo_desc,
       t27.phone as system_user_phone,
       
       t1.log_user_ins,
       t1.log_date_ins,
       t1.log_user_upd,
       t1.log_date_upd,
       
       -- Sigla Desc 
       t2.sigla_pes||' - '||t2.nome as ger_pessoa_sigla_pes_desc,
       t4.sigla_mov_operacao||' - '||t4.nome as mov_operacao_sigla_desc,
       t5.sigla_mov_tipo||' - '||t5.nome as mov_tipo_sigla_desc,
       t7.sigla_cond_pagamento||' - '||t7.nome  as fin_cond_pagrec_sigla_desc,
       t9.sigla_mov_status||' - '||t9.nome as mov_status_sigla_desc,
       t11.sigla_pes||' - '||t11.nome as ger_pessoa_entrega_sigla_desc,
       t13.sigla_uf||' - '||t13.nome as ger_uf_carreg_sigla_desc,
       t15.sigla_uf||' - '||t15.nome as ger_uf_descarreg_sigla_desc,
       t16.sigla_empresa||' - '||t16.nome as ger_empresa_sigla_desc,
       t18.sigla_pes||' - '||t18.nome as ger_pessoa_reme_sigla_desc,
       t20.sigla_pes||' - '||t20.nome as ger_pessoa_dest_sigla_desc,
       t22.sigla_pes||' - '||t22.nome as ger_pessoa_rece_sigla_desc,
       t24.sigla_pes||' - '||t24.nome as ger_pessoa_expe_sigla_desc,
       t26.sigla_pes||' - '||t26.nome as ger_pessoa_inter_sigla_desc
       
       from mov t1
       inner join ger_pessoa t2
       on t1.ger_pessoa_id = t2.id
       inner join ger_pessoa_endereco t3
       on t1.ger_pessoa_endereco_id_fiscal = t3.id
       left join mov_operacao t4
       on  t1.mov_operacao_id = t4.id
       inner join mov_tipo t5
       on t4.mov_tipo_id = t5.id
       
       inner join ger_numeracao t6
       on t4.ger_numeracao_id = t6.id
       left join fin_cond_pagrec t7
       on  t1.fin_cond_pagrec_id = t7.id
       left join fis_doc_tipo t8
       on  t1.fis_doc_tipo_id = t8.id
       left join mov_status t9
       on t1.mov_status_id = t9.id
       
       inner join ger_pessoa_endereco t10
       on  t1.ger_pessoa_endereco_id_entrega = t10.id
       
       inner join ger_pessoa t11
       on t10.ger_pessoa_id = t11.id
       
       left join ger_cidade t12
       on t1.ger_cidade_id_carreg = t12.id
       
       left join ger_uf t13
       on  t12.ger_uf_id = t13.id
       
       left join ger_cidade t14
       on t1.ger_cidade_id_descarreg = t14.id
       
       left join ger_uf t15
       on  t14.ger_uf_id = t15.id
       
       inner join ger_empresa t16
       on t1.ger_empresa_id = t16.id
       
       left join ger_pessoa_endereco t17
       on t1.ger_pessoa_endereco_id_reme = t17.id
       
       left join ger_pessoa t18
       on t17.ger_pessoa_id = t18.id
       
       left join ger_pessoa_endereco t19
       on t1.ger_pessoa_endereco_id_dest = t19.id
       
       left join ger_pessoa t20
       on t19.ger_pessoa_id = t20.id
       
       left join ger_pessoa_endereco t21
       on t1.ger_pessoa_endereco_id_rece = t21.id
       
       left join ger_pessoa t22
       on t21.ger_pessoa_id = t22.id
       
       left join ger_pessoa_endereco t23
       on t1.ger_pessoa_endereco_id_expe = t23.id
       
       left join ger_pessoa t24
       on t23.ger_pessoa_id = t24.id
       
       left join ger_pessoa_endereco t25
       on t1.ger_pessoa_endereco_id_inter = t25.id
       
       left join ger_pessoa t26
       on t25.ger_pessoa_id = t26.id
       
       left join system_user t27
       on  t1.system_user_id_resp = t27.id;;
       
       
       
       
       
       -----------
       
       
       
       Drop VIEW IF EXISTS vwmov_mov_cotacao;;

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
               on t1.system_user_id_aprov = t6.id;
       
       
       
       -----------
       
       
       
       drop view if exists vwope_centro_tipo_subtipo;;

       create or replace view vwope_centro_tipo_subtipo as
       select t1.id as ope_centro_tipo_id,
              t1.nome as ope_centro_tipo_nome,		 
                    t1.tipo_es as tipo_es,
                    fnstd('default', 'tipo_es',t1.tipo_es) as tipo_es_desc,
                    t2.id as ope_centro_subtipo_id,
                    t2.nome as ope_centro_subtipo_nome,
                    t2.tipo_destinacao,
                    fnstd('default', 'tipo_destinacao',t2.tipo_destinacao) as tipo_destinacao_desc
         from ope_centro_tipo t1
           join ope_centro_subtipo t2 on t1.id = t2.ope_centro_tipo_id;;
       
       
       -----------
       
       
       
       drop view if exists vwope_centro2_estoque;;

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
               a.log_date_upd
           from ope_centro2_estoque a
           left join ope_centro2 b
           on a.ope_centro2_id = b.id;;
       
       
       
       
       -----------
       
       
       
       DROP VIEW IF EXISTS vwope_centro2_ord_dest;;

       CREATE OR REPLACE VIEW public.vwope_centro2_ord_dest
AS SELECT t1.unit_id AS mov_unit_id,
    t1.id AS mov_id,
    t1.nr_externo AS mov_nr_externo,
    t1.ger_pessoa_id AS mov_ger_pessoa_id,
    t1.ger_pessoa_endereco_id_fiscal AS mov_ger_pessoa_endereco_id_fiscal,
    t1.mov_operacao_id AS mov_mov_operacao_id,
    t1.fin_cond_pagrec_id AS mov_fin_cond_pagrec_id,
    t1.data_mov AS mov_data_mov,
    t1.numero_mov AS mov_numero_mov,
    t1.data_emissao AS mov_data_emissao,
    t1.fis_doc_tipo_id AS mov_fis_doc_tipo_id,
    t1.serie_mov AS mov_serie_mov,
    t1.mov_status_id AS mov_mov_status_id,
    t1.valor_total AS mov_valor_total,
    t1.observacao AS mov_observacao,
    t1.tipo_frete AS mov_tipo_frete,
    fnstd('mov'::text, 'tipo_frete'::text, t1.tipo_frete::character varying::text) AS mov_tipo_frete_desc,
    t1.data_entrega AS mov_data_entrega,
    t1.data_entrada_saida AS mov_data_entrada_saida,
    t1.ger_pessoa_endereco_id_entrega AS mov_ger_pessoa_endereco_id_entrega,
    t1.ger_cidade_id_carreg AS mov_ger_cidade_id_carreg,
    t1.tipo_emissao_carga AS mov_tipo_emissao_carga,
    fnstd('mov'::text, 'tipo_emissao_carga'::text, t1.tipo_emissao_carga::character varying::text) AS mov_tipo_emissao_carga_desc,
    t1.tipo_modal_carga AS mov_tipo_modal_carga,
    t1.tipo_transportador_carga AS mov_tipo_transportador_carga,
    t1.valor_carga AS mov_valor_carga,
    t1.tipo_umedida_carga AS mov_tipo_umedida_carga,
    fnstd('mov'::text, 'tipo_umedida_carga'::text, t1.tipo_umedida_carga::text) AS mov_tipo_umedida_carga_desc,
    t1.qnt_carga AS mov_qnt_carga,
    t1.ger_empresa_id AS mov_empresa_id,
    t1.ger_pessoa_endereco_id_reme AS mov_pessoa_endereco_id_reme,
    t1.ger_pessoa_endereco_id_dest AS mov_pessoa_endereco_id_dest,
    t1.ger_pessoa_endereco_id_rece AS mov_pessoa_endereco_id_rece,
    t1.ger_pessoa_endereco_id_expe AS mov_pessoa_endereco_id_expe,
    t1.observacao_transp AS mov_obs_transp,
    t1.observacao_serv AS mov_obs_serv,
    t1.tipo_fretamento AS mov_tipo_fretamento,
    t1.tipo_serv_frete AS mov_tipo_serv_frete,
    t1.tipo_tomador_serv_frete AS mov_tipo_tomador_serv_frete,
    t1.taf AS mov_taf,
    t1.data_anulacao AS mov_data_anulacao,
    t1.observacao_item AS mov_observacao_item,
    t1.valor_financeiro_total AS mov_valor_financeiro_total,
    t1.valor_item_frete_total AS mov_valor_item_frete_total,
    t1.observacao_fiscal AS mov_observacao_fiscal,
    t1.ger_pessoa_endereco_id_inter AS mov_pessoa_endereco_id_inter,
    t1.fis_tipo_resp_reten AS mov_fis_tipo_resp_reten,
    fnstd('mov'::text, 'fis_tipo_resp_reten'::text, t1.fis_tipo_resp_reten::text) AS mov_fis_tipo_resp_reten_desc,
    t1.fis_exig_iss_nfs AS mov_fis_exig_iss_nfs,
    fnstd('mov'::text, 'fis_exig_iss_nfs'::text, t1.fis_exig_iss_nfs::text) AS mov_fis_exig_iss_nfs_desc,
    t1.fis_iss_retido_nfs AS mov_fis_iss_retido_nfs,
    fnstd('SN'::text, 'default'::text, t1.fis_iss_retido_nfs::text) AS mov_fis_iss_retido_nfs_desc,
    t1.fis_nat_ope_nfs AS mov_fis_nat_ope_nfs,
    fnstd('mov'::text, 'fis_nat_ope_nfs'::text, t1.fis_nat_ope_nfs::text) AS mov_fis_nat_ope_nfs_desc,
    t1.numero_mov_pre AS mov_numero_mov_pre,
    t1.serio_mov_pre AS mov_serio_mov_pre,
    t1.cep_carreg AS mov_cep_carreg,
    t1.cep_descarreg AS mov_cep_descarreg,
    t1.tipo_carga AS mov_tipo_carga,
    fnstd('mov'::text, 'tipo_carga'::text, t1.tipo_carga::text) AS mov_tipo_carga_desc,
    t1.system_user_id_resp AS mov_system_user_id_resp,
    t2.id AS ger_pessoa_id,
    t2.nome AS ger_pessoa_nome,
    t2.ativo AS ger_pessoa_ativo,
    fnstd('SN'::text, 'default'::text, t2.ativo::text) AS ger_pessoa_ativo_desc,
    t2.doc_cpf AS ger_pessoa_doc_cpf,
    t2.doc_cnpj AS ger_pessoa_doc_cnpj,
    fnutil_formatcpfcnpj(t2.id, true) AS ger_pessoa_doc_cpf_cnpj_desc,
    t2.sigla_pes AS ger_pessoa_sigla_pes,
    t2.fone_1 AS ger_pessoa_fone_1,
    t2.contato_1 AS ger_pessoa_contato_1,
    t3.id AS ger_pessoa_endereco_id,
    t3.ativo AS ger_pessoa_endereco_ativo,
    fnstd('SN'::text, 'default'::text, t3.ativo::text) AS ger_pessoa_endereco_ativo_desc,
    t3.tipo AS ger_pessoa_endereco_tipo,
    fnstd('ger_pessoa_endereco'::text, 'tipo'::text, t3.tipo::text) AS ger_pessoa_endereco_tipo_desc,
    t3.padrao AS ger_pessoa_endereco_padrao,
    fnstd('SN'::text, 'default'::text, t3.padrao::text) AS ger_pessoa_endereco_padrao_desc,
    t3.end_logradouro AS ger_pessoa_endereco_end_lograd,
    t3.end_logradouro_nr AS ger_pessoa_endereco_lograd_nr,
    t3.end_bairro AS ger_pessoa_endereco_end_bairro,
    t3.end_cep AS ger_pessoa_endereco_end_cep,
    t4.id AS mov_operacao_id,
    t4.nome AS mov_operacao_nome,
    t4.ativo AS mov_operacao_ativo,
    fnstd('SN'::text, 'default'::text, t4.ativo::text) AS mov_operacao_ativo_desc,
    t4.sigla_mov_operacao AS mov_operacao_sigla,
    t4.finalidade_doc AS mov_operacao_finalidade_doc,
    t4.tipo_es AS mov_operacao_tipo_es,
    fnstd('default'::text, 'tipo_es'::text, t4.tipo_es::text) AS mov_operacao_tipo_es_desc,
    t5.id AS mov_tipo_id,
    t5.nome AS mov_tipo_nome,
    t5.ativo AS mov_tipo_ativo,
    fnstd('SN'::text, 'default'::text, t5.ativo::text) AS mov_tipo_ativo_desc,
    t5.sigla_mov_tipo AS mov_tipo_sigla,
    t5.tipo_mov AS mov_tipo_tipo_mov,
    t6.id AS ger_numeracao_id,
    t6.nome AS ger_numeracao_nome,
    t6.ativo AS ger_numeracao_ativo,
    fnstd('SN'::text, 'default'::text, t6.ativo::text) AS ger_numeracao_ativo_desc,
    t6.serie AS ger_numeracao_serie,
    t6.ultimo_nr AS ger_numeracao_ultimo_nr,
    t7.id AS fin_cond_pagrec_id,
    t7.nome AS fin_cond_pagrec_nome,
    t7.ativo AS fin_cond_pagrec_ativo,
    fnstd('SN'::text, 'default'::text, t7.ativo::text) AS fin_cond_pagrec_ativo_desc,
    t7.sigla_cond_pagamento AS fin_cond_pagrec_sigla,
    t7.considera_feriado AS fin_cond_pagrec_considera_feriado,
    fnstd('SN'::text, 'default'::text, t7.considera_feriado::text) AS fin_cond_pagrec_considera_feriado_desc,
    t7.considera_final_sem AS fin_cond_pagrec_considera_final_sem,
    fnstd('SN'::text, 'default'::text, t7.considera_final_sem::text) AS fin_cond_pagrec_considera_final_sem_desc,
    t7.qnt_dia_ini AS fin_cond_pagrec_qnt_dia_ini,
    t7.observacao AS fin_cond_pagrec_obs,
    t7.tipo_prazo AS fin_cond_pagrec_tipo_prazo,
    t8.id AS fis_doc_tipo_id,
    t8.nome AS fis_doc_tipo_nome,
    t8.ativo AS fis_doc_tipo_ativo,
    fnstd('SN'::text, 'default'::text, t8.ativo::text) AS fis_doc_tipo_ativo_desc,
    t8.modelo AS fis_doc_tipo_modelo,
    t9.id AS mov_status_id,
    t9.nome AS mov_status_nome,
    t9.ativo AS mov_status_ativo,
    fnstd('SN'::text, 'default'::text, t9.ativo::text) AS mov_status_ativo_desc,
    t9.sigla_mov_status AS mov_status_sigla,
    t9.tipo_status AS mov_status_tipo_status,
    fnstd('mov_status'::text, 'tipo_status'::text, t9.tipo_status::text) AS mov_status_tipo_status_desc,
    t10.id AS ger_pessoa_endereco_entrega_id,
    t10.ativo AS ger_pessoa_endereco_entrega_ativo,
    fnstd('SN'::text, 'default'::text, t10.ativo::text) AS ger_pessoa_endereco_entrega_ativo_desc,
    t10.tipo AS ger_pessoa_endereco_entrega_tipo,
    fnstd('ger_pessoa_endereco'::text, 'tipo'::text, t10.tipo::text) AS ger_pessoa_endereco_entrega_tipo_desc,
    t10.padrao AS ger_pessoa_endereco_entrega_padrao,
    fnstd('SN'::text, 'default'::text, t10.padrao::text) AS ger_pessoa_endereco_entrega_padrao_desc,
    t10.end_logradouro AS ger_pessoa_endereco_entrega_end_lograd,
    t10.end_logradouro_nr AS ger_pessoa_endereco_entrega_end_lograd_nr,
    t10.end_bairro AS ger_pessoa_endereco_entrega_end_bairro,
    t10.end_complemento AS ger_pessoa_endereco_entrega_end_complemento,
    t10.end_cep AS ger_pessoa_endereco_entrega_end_cep,
    t11.id AS ger_pessoa_entrega_id,
    t11.nome AS ger_pessoa_entrega_nome,
    t11.ativo AS ger_pessoa_entrega_ativo,
    fnstd('SN'::text, 'default'::text, t11.ativo::text) AS ger_pessoa_entrega_ativo_desc,
    t11.doc_cpf AS ger_pessoa_entrega_doc_cpf,
    t11.doc_cnpj AS ger_pessoa_entrega_doc_cnpj,
    fnutil_formatcpfcnpj(t11.id, true) AS ger_pessoa_entrega_doc_cpf_cnpj_desc,
    t11.sigla_pes AS ger_pessoa_entrega_sigla,
    t12.id AS ger_cidade_carreg_id,
    t12.nome AS ger_cidade_carreg_nome,
    t12.ativo AS ger_cidade_carreg_ativo,
    fnstd('SN'::text, 'default'::text, t12.ativo::text) AS ger_cidade_carreg_ativo_desc,
    t12.nr_cidade AS ger_cidade_carreg_nr_cidade,
    t13.id AS ger_uf_carreg_id,
    t13.nome AS ger_uf_carreg_nome,
    t13.ativo AS ger_uf_carreg_ativo,
    fnstd('SN'::text, 'default'::text, t13.ativo::text) AS ger_uf_carreg_ativo_desc,
    t13.nr_uf AS ger_uf_carreg_nr_uf,
    t13.sigla_uf AS ger_uf_carreg_sigla,
    t14.id AS ger_cidade_descarreg_id,
    t14.nome AS ger_cidade_descarreg_nome,
    t14.ativo AS ger_cidade_descarreg_ativo,
    fnstd('SN'::text, 'default'::text, t14.ativo::text) AS ger_cidade_descarreg_ativo_desc,
    t14.nr_cidade AS ger_cidade_descarreg_nr_cidade,
    t15.id AS ger_uf_descarreg_id,
    t15.nome AS ger_uf_descarreg_nome,
    t15.ativo AS ger_uf_descarreg_ativo,
    fnstd('SN'::text, 'default'::text, t15.ativo::text) AS ger_uf_descarreg_ativo_desc,
    t15.nr_uf AS ger_uf_descarreg_nr_uf,
    t15.sigla_uf AS ger_uf_descarreg_sigla,
    t16.id AS ger_empresa_id,
    t16.nome AS ger_empresa_nome,
    t16.ativo AS ger_empresa_ativo,
    fnstd('SN'::text, 'default'::text, t16.ativo::text) AS ger_empresa_ativo_desc,
    t16.sigla_empresa AS ger_empresa_sigla,
    t17.id AS ger_pessoa_endereco_reme_id,
    t17.ativo AS ger_pessoa_endereco_reme_ativo,
    fnstd('SN'::text, 'default'::text, t17.ativo::text) AS ger_pessoa_endereco_reme_ativo_desc,
    t17.tipo AS ger_pessoa_endereco_reme_tipo,
    fnstd('ger_pessoa_endereco'::text, 'tipo'::text, t17.tipo::text) AS ger_pessoa_endereco_reme_tipo_desc,
    t17.padrao AS ger_pessoa_endereco_reme_padrao,
    fnstd('SN'::text, 'default'::text, t17.padrao::text) AS ger_pessoa_endereco_reme_padrao_desc,
    t17.end_logradouro AS ger_pessoa_endereco_reme_end_lograd,
    t17.end_logradouro_nr AS ger_pessoa_endereco_reme_end_lograd_nr,
    t17.end_bairro AS ger_pessoa_endereco_reme_end_bairro,
    t17.end_complemento AS ger_pessoa_endereco_reme_end_complemento,
    t17.end_cep AS ger_pessoa_endereco_reme_end_cep,
    t18.id AS ger_pessoa_reme_id,
    t18.nome AS ger_pessoa_reme_nome,
    t18.ativo AS ger_pessoa_reme_ativo,
    fnstd('SN'::text, 'default'::text, t18.ativo::text) AS ger_pessoa_reme_ativo_desc,
    t18.doc_cpf AS ger_pessoa_reme_doc_cpf,
    t18.doc_cnpj AS ger_pessoa_reme_doc_cnpj,
    fnutil_formatcpfcnpj(t18.id, true) AS ger_pessoa_reme_doc_cpf_cnpj_desc,
    t18.sigla_pes AS ger_pessoa_reme_sigla,
    t19.id AS ger_pessoa_endereco_dest_id,
    t19.ativo AS ger_pessoa_endereco_dest_ativo,
    fnstd('SN'::text, 'default'::text, t19.ativo::text) AS ger_pessoa_endereco_dest_ativo_desc,
    t19.tipo AS ger_pessoa_endereco_dest_tipo,
    fnstd('ger_pessoa_endereco'::text, 'tipo'::text, t19.tipo::text) AS ger_pessoa_endereco_dest_tipo_desc,
    t19.padrao AS ger_pessoa_endereco_dest_padrao,
    fnstd('SN'::text, 'default'::text, t19.padrao::text) AS ger_pessoa_endereco_dest_padrao_desc,
    t19.end_logradouro AS ger_pessoa_endereco_dest_end_lograd,
    t19.end_logradouro_nr AS ger_pessoa_endereco_dest_end_lograd_nr,
    t19.end_bairro AS ger_pessoa_endereco_dest_end_bairro,
    t19.end_complemento AS ger_pessoa_endereco_dest_end_complemento,
    t19.end_cep AS ger_pessoa_endereco_dest_end_cep,
    t20.id AS ger_pessoa_dest_id,
    t20.nome AS ger_pessoa_dest_nome,
    t20.ativo AS ger_pessoa_dest_ativo,
    fnstd('SN'::text, 'default'::text, t20.ativo::text) AS ger_pessoa_dest_ativo_desc,
    t20.doc_cpf AS ger_pessoa_dest_doc_cpf,
    t20.doc_cnpj AS ger_pessoa_dest_doc_cnpj,
    fnutil_formatcpfcnpj(t20.id, true) AS ger_pessoa_dest_doc_cpf_cnpj_desc,
    t20.sigla_pes AS ger_pessoa_dest_sigla,
    t21.id AS ger_pessoa_endereco_rece_id,
    t21.ativo AS ger_pessoa_endereco_rece_ativo,
    fnstd('SN'::text, 'default'::text, t21.ativo::text) AS ger_pessoa_endereco_rece_ativo_desc,
    t21.tipo AS ger_pessoa_endereco_rece_tipo,
    fnstd('ger_pessoa_endereco'::text, 'tipo'::text, t21.tipo::text) AS ger_pessoa_endereco_rece_tipo_desc,
    t21.padrao AS ger_pessoa_endereco_rece_padrao,
    fnstd('SN'::text, 'default'::text, t21.padrao::text) AS ger_pessoa_endereco_rece_padrao_desc,
    t21.end_logradouro AS ger_pessoa_endereco_rece_end_lograd,
    t21.end_logradouro_nr AS ger_pessoa_endereco_rece_end_lograd_nr,
    t21.end_bairro AS ger_pessoa_endereco_rece_end_bairro,
    t21.end_complemento AS ger_pessoa_endereco_rece_end_complemento,
    t21.end_cep AS ger_pessoa_endereco_rece_end_cep,
    t22.id AS ger_pessoa_rece_id,
    t22.nome AS ger_pessoa_rece_nome,
    t22.ativo AS ger_pessoa_rece_ativo,
    fnstd('SN'::text, 'default'::text, t22.ativo::text) AS ger_pessoa_rece_ativo_desc,
    t22.doc_cpf AS ger_pessoa_rece_doc_cpf,
    t22.doc_cnpj AS ger_pessoa_rece_doc_cnpj,
    fnutil_formatcpfcnpj(t22.id, true) AS ger_pessoa_rece_doc_cpf_cnpj_desc,
    t22.sigla_pes AS ger_pessoa_rece_sigla,
    t23.id AS ger_pessoa_endereco_expe_id,
    t23.ativo AS ger_pessoa_endereco_expe_ativo,
    fnstd('SN'::text, 'default'::text, t23.ativo::text) AS ger_pessoa_endereco_expe_ativo_desc,
    t23.tipo AS ger_pessoa_endereco_expe_tipo,
    fnstd('ger_pessoa_endereco'::text, 'tipo'::text, t23.tipo::text) AS ger_pessoa_endereco_expe_tipo_desc,
    t23.padrao AS ger_pessoa_endereco_expe_padrao,
    fnstd('SN'::text, 'default'::text, t23.padrao::text) AS ger_pessoa_endereco_expe_padrao_desc,
    t23.end_logradouro AS ger_pessoa_endereco_expe_end_lograd,
    t23.end_logradouro_nr AS ger_pessoa_endereco_expe_end_lograd_nr,
    t23.end_bairro AS ger_pessoa_endereco_expe_end_bairro,
    t23.end_complemento AS ger_pessoa_endereco_expe_end_complemento,
    t23.end_cep AS ger_pessoa_endereco_expe_end_cep,
    t24.id AS ger_pessoa_expe_id,
    t24.nome AS ger_pessoa_expe_nome,
    t24.ativo AS ger_pessoa_expe_ativo,
    fnstd('SN'::text, 'default'::text, t24.ativo::text) AS ger_pessoa_expe_ativo_desc,
    t24.doc_cpf AS ger_pessoa_expe_doc_cpf,
    t24.doc_cnpj AS ger_pessoa_expe_doc_cnpj,
    fnutil_formatcpfcnpj(t24.id, true) AS ger_pessoa_expe_doc_cpf_cnpj_desc,
    t24.sigla_pes AS ger_pessoa_expe_sigla,
    t25.id AS ger_pessoa_endereco_inter_id,
    t25.ativo AS ger_pessoa_endereco_inter_ativo,
    fnstd('SN'::text, 'default'::text, t25.ativo::text) AS ger_pessoa_endereco_inter_ativo_desc,
    t25.tipo AS ger_pessoa_endereco_inter_tipo,
    fnstd('ger_pessoa_endereco'::text, 'tipo'::text, t25.tipo::text) AS ger_pessoa_endereco_inter_tipo_desc,
    t25.padrao AS ger_pessoa_endereco_inter_padrao,
    fnstd('SN'::text, 'default'::text, t25.padrao::text) AS ger_pessoa_endereco_inter_padrao_desc,
    t25.end_logradouro AS ger_pessoa_endereco_inter_end_lograd,
    t25.end_logradouro_nr AS ger_pessoa_endereco_inter_end_lograd_nr,
    t25.end_bairro AS ger_pessoa_endereco_inter_end_bairro,
    t25.end_complemento AS ger_pessoa_endereco_inter_end_complemento,
    t25.end_cep AS ger_pessoa_endereco_inter_end_cep,
    t26.id AS ger_pessoa_inter_id,
    t26.nome AS ger_pessoa_inter_nome,
    t26.ativo AS ger_pessoa_inter_ativo,
    fnstd('SN'::text, 'default'::text, t26.ativo::text) AS ger_pessoa_inter_ativo_desc,
    t26.doc_cpf AS ger_pessoa_inter_doc_cpf,
    t26.doc_cnpj AS ger_pessoa_inter_doc_cnpj,
    fnutil_formatcpfcnpj(t26.id, true) AS ger_pessoa_inter_doc_cpf_cnpj_desc,
    t26.sigla_pes AS ger_pessoa_inter_sigla,
    t27.id AS system_user_id,
    t27.name AS system_user_name,
    t27.login AS system_user_login,
    t27.active AS system_user_ativo,
    fnstd('SN'::text, 'default'::text, t27.active::text) AS system_user_ativo_desc,
    t27.phone AS system_user_phone,
    t1.log_user_ins,
    t1.log_date_ins,
    t1.log_user_upd,
    t1.log_date_upd,
    (t2.sigla_pes::text || ' - '::text) || t2.nome::text AS ger_pessoa_sigla_pes_desc,
    (t4.sigla_mov_operacao::text || ' - '::text) || t4.nome::text AS mov_operacao_sigla_desc,
    (t5.sigla_mov_tipo::text || ' - '::text) || t5.nome::text AS mov_tipo_sigla_desc,
    (t7.sigla_cond_pagamento::text || ' - '::text) || t7.nome::text AS fin_cond_pagrec_sigla_desc,
    (t9.sigla_mov_status::text || ' - '::text) || t9.nome::text AS mov_status_sigla_desc,
    (t11.sigla_pes::text || ' - '::text) || t11.nome::text AS ger_pessoa_entrega_sigla_desc,
    (t13.sigla_uf::text || ' - '::text) || t13.nome::text AS ger_uf_carreg_sigla_desc,
    (t15.sigla_uf::text || ' - '::text) || t15.nome::text AS ger_uf_descarreg_sigla_desc,
    (t16.sigla_empresa::text || ' - '::text) || t16.nome::text AS ger_empresa_sigla_desc,
    (t18.sigla_pes::text || ' - '::text) || t18.nome::text AS ger_pessoa_reme_sigla_desc,
    (t20.sigla_pes::text || ' - '::text) || t20.nome::text AS ger_pessoa_dest_sigla_desc,
    (t22.sigla_pes::text || ' - '::text) || t22.nome::text AS ger_pessoa_rece_sigla_desc,
    (t24.sigla_pes::text || ' - '::text) || t24.nome::text AS ger_pessoa_expe_sigla_desc,
    (t26.sigla_pes::text || ' - '::text) || t26.nome::text AS ger_pessoa_inter_sigla_desc
   FROM mov t1
     JOIN ger_pessoa t2 ON t1.ger_pessoa_id::text = t2.id::text
     JOIN ger_pessoa_endereco t3 ON t1.ger_pessoa_endereco_id_fiscal::text = t3.id::text
     LEFT JOIN mov_operacao t4 ON t1.mov_operacao_id::text = t4.id::text
     JOIN mov_tipo t5 ON t4.mov_tipo_id::text = t5.id::text
     JOIN ger_numeracao t6 ON t4.ger_numeracao_id::text = t6.id::text
     LEFT JOIN fin_cond_pagrec t7 ON t1.fin_cond_pagrec_id::text = t7.id::text
     LEFT JOIN fis_doc_tipo t8 ON t1.fis_doc_tipo_id::text = t8.id::text
     LEFT JOIN mov_status t9 ON t1.mov_status_id::text = t9.id::text
     JOIN ger_pessoa_endereco t10 ON t1.ger_pessoa_endereco_id_entrega::text = t10.id::text
     JOIN ger_pessoa t11 ON t10.ger_pessoa_id::text = t11.id::text
     LEFT JOIN ger_cidade t12 ON t1.ger_cidade_id_carreg::text = t12.id::text
     LEFT JOIN ger_uf t13 ON t12.ger_uf_id::text = t13.id::text
     LEFT JOIN ger_cidade t14 ON t1.ger_cidade_id_descarreg::text = t14.id::text
     LEFT JOIN ger_uf t15 ON t14.ger_uf_id::text = t15.id::text
     JOIN ger_empresa t16 ON t1.ger_empresa_id::text = t16.id::text
     LEFT JOIN ger_pessoa_endereco t17 ON t1.ger_pessoa_endereco_id_reme::text = t17.id::text
     LEFT JOIN ger_pessoa t18 ON t17.ger_pessoa_id::text = t18.id::text
     LEFT JOIN ger_pessoa_endereco t19 ON t1.ger_pessoa_endereco_id_dest::text = t19.id::text
     LEFT JOIN ger_pessoa t20 ON t19.ger_pessoa_id::text = t20.id::text
     LEFT JOIN ger_pessoa_endereco t21 ON t1.ger_pessoa_endereco_id_rece::text = t21.id::text
     LEFT JOIN ger_pessoa t22 ON t21.ger_pessoa_id::text = t22.id::text
     LEFT JOIN ger_pessoa_endereco t23 ON t1.ger_pessoa_endereco_id_expe::text = t23.id::text
     LEFT JOIN ger_pessoa t24 ON t23.ger_pessoa_id::text = t24.id::text
     LEFT JOIN ger_pessoa_endereco t25 ON t1.ger_pessoa_endereco_id_inter::text = t25.id::text
     LEFT JOIN ger_pessoa t26 ON t25.ger_pessoa_id::text = t26.id::text
     LEFT JOIN system_user t27 ON t1.system_user_id_resp::text = t27.id::text;;
       
       
       
       
       
       
       
       -----------
       
       
       
       DROP VIEW IF EXISTS vwope_centro2_ord_itemserv;;

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
               on  t20.ope_centro_tipo_id = t21.id;;
                            
       
       
            
            
       
       
       -----------
       
       
       
       drop view if exists vwope_centro2_pessoa;;
       

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
               f.sigla_frente_trabalho||' - '||e.nome as ope_frente_trabalho_sigla_desc
               
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
               on c.ope_frente_trabalho_id = f.id;;
       
       
       
       -----------
       
       
       
        DROP VIEW If EXISTS vwfin_pagrec_geral;;
       
 
        create or replace view vwfin_pagrec_geral as
         SELECT t1.unit_id AS fin_pagrec_unit_id,
           t1.id AS fin_pagrec_id,
           t1.fin_cond_pagrec_id,
           t3.nome AS fin_cond_pagrec_nome,
           t3.ativo AS fin_cond_pagrec_ativo,
               fnstd('SN', 'default', t3.ativo) AS fin_cond_pagrec_ativo_desc,
           t3.sigla_cond_pagamento AS fin_cond_pagrec_sigla_cond_pagamento,
               t3.sigla_cond_pagamento||' - '||t3.nome AS fin_cond_pagrec_sigla_cond_pagamento_desc,
           t1.numero_parc_total AS fin_pagrec_numero_parc_total,
               t1.tipo_es AS fin_pagrec_tipo_es,
           fnstd('default', 'tipo_es', t1.tipo_es) AS fin_pagrec_tipo_es_desc,
           t1.data_mov AS fin_pagrec_data_mov,
           t1.fin_pagrec_tipo_id,
           t2.nome AS fin_pagrec_nome,
           t2.ativo AS fin_pagrec_ativo,
               fnstd('SN', 'default', t2.ativo) AS fin_pagrec_ativo_desc,
           t1.numero_doc_pagrec AS fin_pagrec_numero_doc_pagrec,
           t1.ger_pessoa_id,
           t4.nome AS ger_pessoa_nome,
           t4.razao_social AS ger_pessoa_razao_social,
           t4.doc_cpf AS ger_pessoa_cpf,
           t4.doc_cnpj AS ger_pessoa_cpnj,
               fnutil_formatcpfcnpj(t4.id, TRUE) as ger_pesso_doc_cpf_cnj_desc,
           t4.ativo AS ger_pessoa_ativo,
               fnstd('SN', 'default',t4.ativo) AS ger_pessoa_ativo_desc,
           t4.sigla_pes AS ger_pessoa_sigla_pes,
           (((t4.sigla_pes)::text || '-'::text) || (t4.nome)::text) AS ger_pessoa_desc,
           t1.ger_pessoa_id_pagrec,
           t5.nome AS ger_pessoa_pagrec_nome,
           t5.razao_social AS ger_pessoa_pagrec_razao_social,
           t5.doc_cpf AS ger_pessoa_pagrec_cpf,
           t5.doc_cnpj AS ger_pessoa_pagrec_cpnj,
               fnutil_formatcpfcnpj(t5.id, TRUE) as ger_pessoa_pagrec_cpnj_desc,
           t5.ativo AS ger_pessoa_pagrec_ativo,
               fnstd('SN', 'default', t5.ativo) AS ger_pessoa_pagrec_ativo_desc,
           t5.sigla_pes AS ger_pessoa_pagrec_sigla_pes,
           (((t5.sigla_pes)::text || '-'::text) || (t5.nome)::text) AS ger_pessoa_pagrec_desc,
           t6.id AS fin_pagrec_parc_id,
           t6.numero_parc AS fin_pagrec_parc_numero_parc,
           t6.fin_doc_tipo_id,
           t7.nome AS fin_doc_tipo_nome,
           t7.ativo AS fin_doc_tipo_ativo,
           fnstd('SN', 'default',t7.ativo) AS fin_doc_tipo_ativo_desc,		
           t6.valor_pagrec AS fin_pagrec_parc_valor_pagrec,
           t6.valor_juro AS fin_pagrec_parc_valor_juro,
           t6.valor_desconto AS fin_pagrec_parc_valor_desconto,
           t6.valor_multa AS fin_pagrec_parc_valor_multa,
           t6.data_venc AS fin_pagrec_parc_data_venc,
           t1.log_user_ins,
           t1.log_user_upd,
           t1.log_date_ins,
           t1.log_date_upd,
           t8.id AS ger_empresa_id,
           t8.nome AS ger_empresa_nome,
           t8.razao_social AS ger_empresa_razao_social
          FROM (((((((fin_pagrec t1
            JOIN fin_pagrec_parc t6 ON (((t1.id)::text = (t6.fin_pagrec_id)::text)))
            JOIN fin_doc_tipo t7 ON (((t6.fin_doc_tipo_id)::text = (t7.id)::text)))
            LEFT JOIN fin_pagrec_tipo t2 ON (((t1.fin_pagrec_tipo_id)::text = (t2.id)::text)))
            LEFT JOIN fin_cond_pagrec t3 ON (((t1.fin_cond_pagrec_id)::text = (t3.id)::text)))
            LEFT JOIN ger_pessoa t4 ON (((t1.ger_pessoa_id)::text = (t4.id)::text)))
            LEFT JOIN ger_pessoa t5 ON (((t1.ger_pessoa_id_pagrec)::text = (t5.id)::text)))
            LEFT JOIN ger_empresa t8 ON (((t1.ger_empresa_id)::text = (t8.id)::text)));;
       
       
       -----------
       
       
       
       Drop VIEW IF EXISTS vwmov_cotacao_anal;;

       CREATE OR REPLACE VIEW vwmov_cotacao_anal AS
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
               on t1.c10_fin_cond_pagrec_id = t44.id;;
       
       
       -----------
       
       
       

       CREATE OR REPLACE VIEW vwope_centro2_area AS
        SELECT 
               c.unit_id,
               c.unit_id  as ope_centro2_area_unit_id,
           c.id as ope_centro2_area_id,
               c.qnt_area_prod as ope_centro2_area_qnt_area_prod,
               c.qnt_area_improd as ope_centro2_area_qnt_area_improd,
               c.qnt_plantas_estande as ope_centro2_area_qnt_plantas_estande,
               c.bloco_col as ope_centro2_area_bloco_col,
               c.lat_x as ope_centro2_area_lat_x,
               c.long_y as ope_centro2_area_long_y,
               c.alt_z as ope_centro2_area_alt_z,
               c.data_ini_plan as ope_centro2_area_data_ini_plan,
               c.data_fin_plan as ope_centro2_area_data_fin_plan,
               c.data_ult_plan as ope_centro2_area_data_ult_plan,
               c.data_ini_col as ope_centro2_area_data_ini_col,
               c.data_fin_col as ope_centro2_area_data_fin_col,
               c.data_ult_col as ope_centro2_area_data_ult_col,
               c.data_florada_1 as ope_centro2_area_data_florada_1,
               c.data_emerg as ope_centro2_area_data_emerg,
               c.observacao as ope_centro2_area_observacao,
               
               i.id as ope_centro2_area_umedida_id,
               i.nome as ope_centro2_area_umedida_nome,
               i.sigla_umedida as ope_centro2_area_umedida_sigla,
               
               j.id as ope_tipo_solo_id,
               j.nome as ope_centro2_area_tipo_solo_nome,
               j.sigla_tipo_solo as ope_centro2_area_tipo_solo_sigla,
               
               k.id as ope_centro2_area_espacamento_id,
               k.nome as ope_centro2_area_espacamento_nome,
               k.sigla_espac as ope_centro2_area_espacamento_sigla,
               
               l.id as ope_centro2_area_atividade_sistema_cult_id,
               l.nome as ope_centro2_area_atividade_sistema_cult_nome,
               l.sigla_atividade_grupo as ope_centro2_area_atividade_sistema_cult_sigla,
               
               q.id as ope_centro2_area_atividade_sistema_plan_id,
               q.nome as ope_centro2_area_atividade_sistema_plan_nome,
               q.sigla_atividade_grupo as ope_centro2_area_atividade_sistema_plan_sigla,
               
               r.id as ope_centro2_area_atividade_sistema_col_id,
               r.nome as ope_centro2_area_atividade_sistema_col_nome,
               r.sigla_atividade_grupo as ope_centro2_area_atividade_sistema_col_sigla,
               
               m.id as ope_centro2_area_item_serv_id,
               m.nome as ope_centro2_area_item_serv_nome,
               m.sigla_itemserv as ope_centro2_area_item_serv_sigla,
               m.ativo as ope_centro2_area_item_serv_ativo,
               fnstd('SN','default',m.ativo) as ope_centro2_area_item_serv_ativo_desc,
               
               s.nome as ope_centro2_area_item_serv_umedida_nome,	
               s.sigla_umedida as ope_centro2_area_item_serv_umedida_sigla,
               
               n.nome as ope_centro2_area_item_serv_var_nome,
               n.sigla_itemserv as ope_centro2_area_item_serv_var_sigla,
               
               o.nome as ope_centro2_area_item_serv_ultimo_nome,
               o.sigla_itemserv as ope_centro2_area_item_serv_ultimo_sigla,
               
               p.nome as ope_centro2_area_item_serv_var_ultimo_nome,
               p.sigla_itemserv as ope_centro2_area_item_serv_var_ultimo_sigla,
               
               a.unit_id  as ope_centro1_unit_id,
               a.id as ope_centro1_id,
           a.sigla_centro1 as ope_centro1_sigla,
           a.nome as ope_centro1_nome,
               a.observacao as ope_centro1_observacao,
               a.ativo as ope_centro1_ativo,
               fnstd('SN','default',a.ativo) as ope_centro1_ativo_desc,
               u.id as ope_centro1_pessoa_id,
               u.nome as ope_centro1_pessoa_nome,
               u.sigla_pes as ope_centro1_pessoa_sigla,
               u.doc_cpf as ope_centro1_pessoa_doc_cpf,
               u.doc_cnpj as ope_centro1_pessoa_doc_cpnj,
               fnutil_formatcpfcnpj(u.id,False) as ope_centro1_pessoa_doc_cpf_cpnj_desc,
           b.id   as ope_centro2_id,
           b.sigla_centro2 as ope_centro2_sigla,
           b.nome as ope_centro2_nome,
               b.ativo as ope_centro2_ativo,
               fnstd('SN','default',b.ativo) as ope_centro2_ativo_desc,
               b.tipo_destinacao as ope_centro2_tipo_destinacao,
               fnstd('ope_centro2','tipo_destinacao',b.tipo_destinacao) as ope_centro2_tipo_destinacao_desc,
               b.tipo_prop as ope_centro2_tipo_prop,
               fnstd('ope_centro2','tipo_prop',b.tipo_prop) as ope_centro2_tipo_prop_desc,
               t.id as ope_centro_rat_tipo_id,
               t.nome as ope_centro_rat_tipo_nome,
               t.sigla_centro_rat_tipo as ope_centro_rat_tipo_sigla,
               t.ativo as ope_centro_rat_tipo_ativo,
               fnstd('SN','default',t.ativo) as ope_centro_rat_tipo_ativo_desc,
               
               d.id as ope_centro_subtipo_id,
               d.nome as ope_centro_subtipo_nome,
               e.id as ope_centro_tipo_id,
               e.nome as ope_centro_tipo_nome,
               e.tipo_es as ope_centro_tipo_es,
               fnstd('default', 'tipo_es',e.tipo_es) as ope_centro_tipo_es_desc,
               
               f.id as ope_centro_subgrupo_id,
               f.nome as ope_centro_subgrupo_nome,
               f.sigla_centro_subgrupo as ope_centro_subgrupo_sigla,
               f.ativo as ope_centro_subgrupo_ativo,
               fnstd('SN','default',f.ativo) as ope_centro_subgrupo_ativo_desc,
               
               g.id as ope_centro_grupo_id,
               g.nome as ope_centro_grupo_nome,
               g.sigla_centro_grupo as ope_centro_grupo_sigla,
               g.ativo as ope_centro_grupo_ativo,
               fnstd('SN','default',g.ativo) as ope_centro_grupo_ativo_desc,
               
               h.id as ope_periodo_id,
               h.nome as ope_periodo_nome,
               h.sigla_periodo as ope_periodo_sigla,
               h.ativo as ope_periodo_ativo,
               fnstd('SN','default',h.ativo) as ope_periodo_ativo_desc,
               h.data_ini as ope_periodo_data_ini,
               h.data_fin as ope_periodo_data_fin,
               c.log_user_ins,
               c.log_date_ins,
               c.log_user_upd,
               c.log_date_upd,
               
               -- Sigla Desc		
               i.sigla_umedida||' - '||i.nome as ope_centro2_area_umedida_sigla_desc,
               j.sigla_tipo_solo||' - '||j.nome as ope_centro2_area_tipo_solo_sigla_desc,
               k.sigla_espac||' - '||k.nome as ope_centro2_area_espacamento_sigla_desc,
               l.sigla_atividade_grupo||' - '||l.nome as ope_centro2_area_atividade_sistema_cult_sigla_desc,
               q.sigla_atividade_grupo||' - '||q.nome as ope_centro2_area_atividade_sistema_plan_sigla_desc,
               r.sigla_atividade_grupo||' - '||r.nome as ope_centro2_area_atividade_sistema_col_sigla_desc,
               m.sigla_itemserv||' - '||m.nome as ope_centro2_area_item_serv_sigla_desc,
               s.sigla_umedida||' - '||s.nome as ope_centro2_area_item_serv_umedida_sigla_desc,
               n.sigla_itemserv||' - '||n.nome as ope_centro2_area_item_serv_var_sigla_desc,
               o.sigla_itemserv||' - '||o.nome as ope_centro2_area_item_serv_ultimo_sigla_desc,
               p.sigla_itemserv||' - '||p.nome as ope_centro2_area_item_serv_var_ultimo_sigla_desc,
               a.sigla_centro1||' - '||a.nome as ope_centro1_sigla_desc,
               u.sigla_pes||' - '||u.nome as ope_centro1_pessoa_sigla_desc,
               b.sigla_centro2||' - '||b.nome as ope_centro2_sigla_desc,
               t.sigla_centro_rat_tipo||' - '||t.nome as ope_centro_rat_tipo_sigla_desc,
               f.sigla_centro_subgrupo||' - '||f.nome as ope_centro_subgrupo_sigla_desc,
               g.sigla_centro_grupo||' - '||g.nome as ope_centro_grupo_sigla_desc,
               h.sigla_periodo||' - '||h.nome as ope_periodo_sigla_desc
               
          FROM ope_centro2_area c 
           join ope_centro2 b 
               on c.ope_centro2_id = b.id
               left join ope_centro_rat_tipo t
               on b.ope_centro_rat_tipo_id = t.id
           join ope_centro1 a 
               on b.ope_centro1_id = a.id
               left join ger_pessoa u
               on a.ger_pessoa_id  = u.id
               join  ope_centro_subtipo d
               on  a.ope_centro_subtipo_id = d.id
               join ope_centro_tipo e
               on d.ope_centro_tipo_id = e.id
             left join ope_centro_subgrupo f
               on b.ope_centro_subgrupo_id = f.id
               left join ope_centro_grupo g
               on f.ope_centro_grupo_id =  g.id
               left join ope_periodo h
               on c.ope_periodo_id = h.id
               left join ger_umedida i
               on c.ger_umedida_id = i.id
               left join ope_tipo_solo j
               on c.ope_tipo_solo_id = j.id
               left join ope_espac k
               on c.ope_espac_id = k.id
               left join	ope_atividade_sistema l
               on c.ope_atividade_sistema_id_cult = l.id
               left join	ope_atividade_sistema q
               on c.ope_atividade_sistema_id_plan = q.id
               left join	ope_atividade_sistema r
               on c.ope_atividade_sistema_id_col = r.id
               left join  ger_itemserv m
               on c.ger_itemserv_id = m.id
               left join ger_umedida s
               on m.ger_umedida_id = s.id
               left join ger_itemserv n
               on c.ger_itemserv_var_id = n.id
               left join  ger_itemserv o
               on c.ger_itemserv_id_ult = o.id
               left join ger_itemserv  p
               on c.ger_itemserv_var_id_ult = p.id;;
       
           
           
       
       
       -----------
       
       
       

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
               j.sigla_centro_grupo||' - '||j.nome as ope_centro_grupo_sigla_desc
       
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
               on k.ger_pessoa_id = l.id;;
               
               
               
       
       
       -----------
       
       
       
       -- DROP VIEW IF EXISTS vwger_pessoa;

       CREATE OR REPLACE VIEW vwger_pessoa AS
       SELECT gp.id as id_pessoa,
                    gp.nome as nome_pessoa,
                    gp.ativo as ativo_pessoa,
                    fnstd('SN', 'default',gp.ativo) as ativo_pessoa_desc,
                    gp.razao_social as razao_social_pessoa,
                    gp.doc_cnpj as doc_cnpj_pessoa,
                    gp.doc_cpf as doc_cpf_pessoa,
                    (case when gp.doc_cnpj is null then gp.doc_cpf ELSE gp.doc_cnpj end) as doc_cnpj_cpf_pessoa,
                    gp.sigla_pes as sigla_pes,
                    gpe.id as id_endereco,
                    gpe.end_logradouro as endereco,
                    gpe.end_logradouro_nr as endereco_numero,
                    gpe.end_cep as cep_endereco,
                    gc.id as id_cidade,
                    gc.nome as nome_cidade,
                    gUf.sigla_uf as uf_cidade
       FROM ger_pessoa gp
       Left Join ger_pessoa_endereco gpe
       on gp.id = gpe.ger_pessoa_id
       Left Join ger_cidade gc
       on gpe.end_ger_cidade_id = gc.id
       Inner join ger_uf gUf
       on  gc.ger_uf_id = gUf.id
       ORDER BY gp.id;;
       
       
       -----------
       
       
       
DROP TRIGGER IF EXISTS trgbor_bor_mov_bui ON public.bor_mov;;
       Drop FUNCTION IF EXISTS fnbor_bor_mov;;
       

       CREATE OR REPLACE FUNCTION public.fnbor_bor_mov()
        RETURNS trigger
        LANGUAGE plpgsql
       AS $function$
       declare
         vBorMovAtual record;
       begin
         new.geom = ST_GeomFromText('POINT('||new.gps_lat||' '||new.gps_long||')');
         new.geom_circle = ST_SetSRID(ST_Buffer(new.geom::geography , 15)::geometry, 4326);
        
         -- busca data da bor_mov_atual e se a new.dthr_track for maior, atualiza a bor_mov_atual
         select a.dthr_track
           into vBorMovAtual
           from public.bor_mov_atual a
          where a.ope_centro2_equip_id = new.ope_centro2_equip_id_1;
         
        if coalesce(vBorMovAtual.dthr_track, '1900-01-01') = '1900-01-01'
         then
             begin
               insert into public.bor_mov_atual (
                   id_tipo,					      numero_serie,					    ibutton_rfid,						        dthr_track,				
                    gps_altitude,				    gps_altitude_status,			gps_lat,							          gps_long,	
                   gps_angulo_norte,		  	gps_posicao_status,				gps_velocidade,						      gps_velocidade_media,
                   equipamento_ignicao,		equipamento_bateria,			equipamento_odometro,				    equipamento_rpm,			
                   equipamento_veloc,		  equipamento_veloc_odom,		equipamento_veloc_odom_media,		log_user_ins,	
                   log_user_upd,				    ope_centro2_equip_id,			ope_centro2_pessoa_id,				  ger_empresa_id,			
                   ope_centro2_area_id,		geom,							        id,                             dthr_ignicao_last_off)
               values (
                 new.id_tipo,				      new.numero_serie,				      new.ibutton_rfid,					          new.dthr_track,				
                 new.gps_altitude,			    new.gps_altitude_status,		  new.gps_lat,						            new.gps_long,	
                 new.gps_angulo_norte,		  new.gps_posicao_status,			  new.gps_velocidade,					        new.gps_velocidade_media,
                 new.equipamento_ignicao,	new.equipamento_bateria,		  new.equipamento_odometro,			      new.equipamento_rpm,			
                 new.equipamento_veloc,	  new.equipamento_veloc_odom,		new.equipamento_veloc_odom_media,	  new.log_user_ins,	
                 new.log_user_upd,			    new.ope_centro2_equip_id_1,		new.ope_centro2_pessoa_id,			    new.ger_empresa_id,			
                 new.ope_centro2_area_id,	new.geom,						          new.id,                             new.dthr_track);
             exception when others then null;
             end;
         else    
         begin
           update public.bor_mov_atual
              set id_tipo				        = new.id_tipo,				
                  numero_serie				 	  = new.numero_serie,				
                  ibutton_rfid				 	  = new.ibutton_rfid,						
                  dthr_track				      = new.dthr_track,				
                  gps_altitude			      = new.gps_altitude,			
                  gps_altitude_status	  = new.gps_altitude_status,		
                  gps_lat					 	    = new.gps_lat,						
                  gps_long	              = new.gps_long,	
                  gps_angulo_norte		    = new.gps_angulo_norte,		
                  gps_posicao_status  		= new.gps_posicao_status,			
                  gps_velocidade			  	= new.gps_velocidade,						
                  gps_velocidade_media   = new.gps_velocidade_media,
                  equipamento_ignicao  	= new.equipamento_ignicao,	
                  equipamento_bateria  	= new.equipamento_bateria,		
                  equipamento_odometro   = new.equipamento_odometro,				
                  equipamento_rpm			  = new.equipamento_rpm,			
                  equipamento_veloc		  = new.equipamento_veloc,		
                  equipamento_veloc_odom		    = new.equipamento_veloc_odom,		
                  equipamento_veloc_odom_media = new.equipamento_veloc_odom_media,		
                  log_user_ins	          = new.log_user_ins,	
                  log_user_upd			      = new.log_user_upd,		
                            log_date_upd           = now(),
                  ope_centro2_equip_id	  = new.ope_centro2_equip_id_1,		
                  ope_centro2_pessoa_id	= new.ope_centro2_pessoa_id,				
                  ger_empresa_id			    = new.ger_empresa_id,			
                  ope_centro2_area_id	  = new.ope_centro2_area_id,	
                  geom						 	      = new.geom,								
                  id                     = new.id,
                  dthr_ignicao_last_off  = case when new.equipamento_ignicao != 'ON' then new.dthr_track else dthr_ignicao_last_off end
            where ope_centro2_equip_id = new.ope_centro2_equip_id_1;
         exception when others then null;
         end;
         end if;
         return new;
       end; $function$
       ;
       
       CREATE TRIGGER "trgbor_bor_mov_bui" BEFORE INSERT OR UPDATE ON "public"."bor_mov"
       FOR EACH ROW
       EXECUTE PROCEDURE "public"."fnbor_bor_mov"();;
       
       
       
       
       -----------
       
       

       Drop FUNCTION IF EXISTS fnbor_bormovdatagenerationprocess;

       CREATE OR REPLACE FUNCTION public.fnbor_bormovdatagenerationprocess(pdataini timestamp with time zone, hours integer, qtddispositivos integer)
        RETURNS boolean
        LANGUAGE plpgsql
       AS $function$
       declare 
         row Record;
         dispositivo Record;
         --
         vQtdApont int;
         vApontSeq int;
         vDtApont timestamptz;
         --
         vSeqOperador int;
         vOperador varchar;
         vSeqAtividade int;
         vAtividade varchar;
         vhodometroinicial int;
         --
         vLat numeric;
         vLng numeric;
       begin
         -- loop para as horas em segundos (hours * 60)
         vQtdApont = hours * 30;
         if (qtdDispositivos<=0) then qtdDispositivos = 999999; end if;
         
         -- percorre todos os dispositivos para gerar apontamentos
         for dispositivo in SELECT a.numero_serie, a.ope_centro2_equip_id
                              FROM public.bor_dispositivo a
                             WHERE a.tipo = '1' -- Equipamento
                             ORDER BY a.numero_serie
                             LIMIT qtdDispositivos
         loop
           -- busca um operador entre 1 e 8
           vSeqOperador = 1; -- round(random()*1 + 1);
           select w.numero_serie
             into vOperador
             from ( select a.numero_serie, row_number() OVER (ORDER BY a.numero_serie) as seq
                      from bor_dispositivo a
                     where a.tipo = '2') w
            where w.seq = vSeqOperador;
            
           -- busca uma operação entre 1 e 8
           vSeqAtividade = round(random()*99 + 1);
           select w.ope_atividade_id
             into vAtividade
             from ( select a.id as ope_atividade_id, row_number() OVER (ORDER BY a.id) as seq
                      from public.ope_atividade a
                     where unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75') w
            where w.seq = vSeqAtividade;
        
           -- inicia data e quantidade de apontamento
           vDtApont = pdataini;
           vApontSeq = 1;
           vhodometroinicial = trunc(random() * (101000-100000) + 100000);
           --
           loop
             select vDtApont + (1 * interval '1 minute')
               into vDtApont;       
             --
             raise notice 'Data = % - Dispositivo = %', vDtApont, dispositivo.numero_serie;
             --
             -- coordenadas de São Joaquim -> Lat:(random()+22)*-1 / Lng:(random()+47)*-1
             select '-22.59'||substring(random()::varchar, 3, 8)::numeric, '-47.01'||substring(random()::varchar, 3, 8)::numeric
             into vLng, vLat;
             --
             INSERT INTO public.bor_mov (
                id_tipo,                                             numero_serie,                                        ibutton_rfid,                                                   dthr_track, 
                gps_altitude,                                        gps_altitude_status,                                 gps_lat,                                                        gps_long,
                gps_angulo_norte,                                    gps_posicao_status,                                  gps_velocidade,                                                 gps_velocidade_media, 
                equipamento_ignicao,                                 equipamento_bateria,                                 equipamento_odometro,                                           equipamento_rpm,	   
                equipamento_veloc,                                   equipamento_veloc_odom,                              equipamento_veloc_odom_media,                                   log_user_ins, 
                log_date_ins,                                        buzzer,                                              unit_id,                                                        status,
              ope_atividade_id,                                    ope_centro2_equip_id_1 )
             VALUES (
              '198',                                                 dispositivo.numero_serie,                            vOperador,                                                      vDtApont,
              trunc(random() * (1100-600) + 600),                  'VALID',                                             vLat,                                                           vLng,
                trunc(random() * (359)),                             true,                                                trunc(random() * (45-20) + 20),                                 trunc(random() * (45-20) + 20), 
                 case when round(random()) = 0 then '' else 'ON' end, case when round(random()) = 0 then '' else 'ON' end, vHodometroInicial + trunc(random() * (7-2) + 2),                trunc(random() * (3700-1500) + 1500), 
                 trunc(random() * (45-20) + 20),                      trunc(random() * (45-20) + 20),                      trunc(random() * (45-20) + 20),                                 '4e95e778-bf73-441e-a8c1-1db72cb8a7c4',
              now(),                                               case when round(random()) = 0 then '' else 'ON' end, 'f3996813-838e-49af-9649-8dc44e24bc75',                         'NP',
                vAtividade,                                          dispositivo.ope_centro2_equip_id );
             --   
             vApontSeq = vApontSeq + 1;
             exit when vApontSeq > vQtdApont;
           end loop;
           --
         end loop;
         --
         return true;
         --
       exception
         when others then 
             raise notice 'erro: %', sqlerrm;
             return false;
       end;
       $function$;;
       
       
       
       -----------
       
       
      
       
       
      
       Drop FUNCTION IF EXISTS fnbor_bormsgprocess;;

       CREATE OR REPLACE FUNCTION public.fnbor_bormsgprocess(pdataini date, pdatafim date)
        RETURNS boolean
        LANGUAGE plpgsql
       AS $function$
       declare 
         row Record;
         equipamento Record;
         --
         vOpeCentro2EquipId1 varchar;
         vGerEmpresaId varchar;
         vOpeAtividadeId varchar;
       begin
         -- pega todos os equipamentos, o primeiro e o último apontamento no período executado
         -- isso vai facilitar o processo e principalmente ajudar na performance
         for equipamento in SELECT a.numero_serie,
                           max(a.dthr_trans_msg_rast) as max_apont,
                           min(a.dthr_trans_msg_rast) as min_apont
                      FROM public.bor_msg a 
                     WHERE a.dthr_track between pdataini and pdatafim
                     GROUP BY a.numero_serie
                     ORDER BY a.numero_serie 
         loop
           for row in SELECT a.id,
                             a.numero_serie, 
                             a.grupo_msg||'-'||a.index_msg as index_bor
                        FROM public.bor_msg a 
                       WHERE a.numero_serie = equipamento.numero_serie
                         AND a.dthr_track BETWEEN equipamento.min_apont 
                                              AND equipamento.min_apont
                       ORDER BY a.dthr_track 
           loop
             -- busca equipamento na bor_dispositivo
             select a.ope_centro2_equip_id
                into vOpeCentro2EquipId1
                from public.bor_dispositivo a
               where a.numero_serie = row.numero_serie
                 and a.tipo = '1'; -- BORDO
             raise notice 'vOpeCentro2EquipId1 = %', vOpeCentro2EquipId1;
             
             -- busca empresa na ope_centro2_param_per, se existir mais de um registro com validade > now()
             -- retorna o primeiro (com dt_valid_ini mais antiga)
             select a.ger_empresa_id
                into vGerEmpresaId
                from public.ope_centro2_param_per a
               where a.ope_centro2_id = vOpeCentro2EquipId1
                 and row.dthr_track >= a.dt_valid_ini
               order by a.dt_valid_ini
               limit 1;
             raise notice 'vGerEmpresaId = %', vGerEmpresaId;
             
             -- busca ope_atividade na bor_msg
             select a.ope_atividade_id
               into vOpeAtividadeId
               from public.ope_atividade a
              where a.index_bor = row.index_bor
              order by dthr_trans_msg_rast desc
             limit 1;
             raise notice 'vOpeAtividadeId = %', vOpeAtividadeId;
          
             -- atualiza public.bor_msg
             update public.bor_msg
                set ope_centro2_equip_id_1 = vOpeCentro2EquipId1,
                    ope_atividade_id       = vOpeAtividadeId,
                    ger_empresa_id         = vGerEmpresaId
              where id = row.id;
             raise notice 'ID = %', row.id;
             raise notice '********************************************************************';
          
           end loop;
         end loop;
         --
         return true;
         --
       exception
         when others then 
             raise notice 'erro: %', sqlerrm;
             return false;
       end;
       $function$;

       
       Drop FUNCTION IF EXISTS fnbor_querys;

       
       CREATE OR REPLACE FUNCTION public.fnbor_querys(
           -- parâmetros obrigatórios
           pUnitId character varying, 
           pDataIni timestamptz,
           pdataFim timestamptz,
           pStatus numeric, -- 0=Todos / 1=Trabalhando / 2=Ocioso / 3=Desligado / 4=Suspeito
           -- opções de seleção dos dados
           pSelEmpresaId boolean DEFAULT false,
           pSelEquipamentoId boolean DEFAULT false,
           pSelOperadorId boolean DEFAULT false,
           pSelAtividadeId boolean DEFAULT false,
           pSelAreaId boolean DEFAULT false,
           pSelStatus boolean DEFAULT false,
           pSelRpmMin boolean DEFAULT false,
           pSelRpmAvg boolean DEFAULT false,
           pSelRpmMax boolean DEFAULT false,
           pSelHectaresTotal boolean DEFAULT false,
           pSelHectaresAvg boolean DEFAULT false,
           pSelHorasTotal boolean DEFAULT false,
           pSelHorasAvg boolean DEFAULT false,
           pSelVelocidadeMin boolean DEFAULT false,
           pSelVelocidadeAvg boolean DEFAULT false,
           pSelVelocidadeMax boolean DEFAULT false,
           -- opções de filtro da query
           pWhereEmpresaId character varying DEFAULT NULL::character varying,
           pWhereEquipamentoId character varying DEFAULT NULL::character varying,
           pWhereOperadorId character varying DEFAULT NULL::character varying,
           pWhereAtividadeId character varying DEFAULT NULL::character varying,
           pWhereAreaId character varying DEFAULT NULL::character varying)
        RETURNS TABLE( unit_id character varying,
                       empresa_id character varying,
                       equipamento_id character varying,
                       operador_id character varying,
                       atividade_id character varying,
                       area_id character varying,
                       status numeric,
                       rpm_min numeric, 
                       rpm_avg numeric, 
                       rpm_max numeric,
                       hectares_total numeric,
                       hectares_avg numeric,
                       horas_total numeric,
                       horas_avg numeric,
                       velocidade_min numeric,
                       velocidade_avg numeric,
                       velocidade_max numeric)
        LANGUAGE plpgsql
       AS $function$
       declare
             vSql varchar;
             r record;
       begin
           vSql = 'select a.unit_id as unit_id ';
       
           --Columns--
           --==================================
           if (pSelEmpresaId) then
               vSql = vSql || ', a.ger_empresa_id as empresa_id';
           end if;
           -- 
           if (pSelEquipamentoId) then
               vSql = vSql || ', a.ope_centro2_equip_id_1 as equipamento_id';
           end if;
           --
           if (pSelOperadorId) then
               vSql = vSql || ', a.ope_centro2_pessoa_id as operador_id';
           end if;
           --
           if (pSelAtividadeId) then
               vSql = vSql || ', a.ope_atividade_id as atividade_id';
           end if;
           --
           if (pSelAreaId) then
               vSql = vSql || ', a.ope_centro2_area_id as area_id';
           end if;
           --
           if (pSelStatus) then
               vSql = vSql || ', case when (a.equipamento_ignicao = ''ON'' and a.equipamento_veloc::numeric > 0 and a.ope_atividade_id is not null) then 1 ';
               vSql = vSql || '       when (a.equipamento_ignicao = ''ON'' and a.equipamento_veloc::numeric <= 0) then 2 ';
               vSql = vSql || '       when (a.equipamento_ignicao != ''ON'') then 3 ';
               vSql = vSql || '       else 4 '; -- definir melhor a regra do "Suspeito"
               vSql = vSql || '  end as status ';
           end if;
       
              --Agregates--
              --==================================
              if (pSelRpmMin) then
                  vSql = vSql || ', min(equipamento_rpm::numeric) as rpm_min ';
           end if;
           --
           if (pSelRpmAvg) then
                  vSql = vSql || ', round(avg(equipamento_rpm::numeric)) as rpm_avg ';
           end if;
           --
           if (pSelRpmMax) then
                  vSql = vSql || ', max(equipamento_rpm::numeric) as rpm_max ';
           end if;
           --
           if (pSelHectaresTotal) then
                  vSql = vSql || ', round(sum(qnt_ha_trab), 3) as hectares_total ';
           end if;
           --
           if (pSelHectaresAvg) then
                  vSql = vSql || ', round(avg(qnt_ha_trab), 3) as hectares_avg ';
           end if;
           --
           if (pSelHorasTotal) then
                  vSql = vSql || ', round(sum(duration), 3) as horas_total ';
           end if;
           --
           if (pSelHorasAvg) then
                  vSql = vSql || ', round(avg(duration), 3) as horas_avg ';
           end if;
           --
              if (pSelVelocidadeMin) then
                  vSql = vSql || ', min(equipamento_veloc::numeric) as velocidade_min ';
           end if;
           --
           if (pSelVelocidadeAvg) then
               vSql = vSql || ', round(avg(equipamento_veloc::numeric)) as velocidade_avg ';
           end if;
           --
           if (pSelVelocidadeMax) then
               vSql = vSql || ', max(equipamento_veloc::numeric) as velocidade_max ';
           end if;
           
           vSql = vSql || '  from public.bor_mov a ';
           vSql = vSql || ' where a.unit_id = ''' || pUnitId || '''';
           vSql = vSql || '   and a.dthr_track between to_timestamp('''||to_char(pDataIni, 'dd/mm/yyyy hh24:mi:ss')||''', ''dd/mm/yyyy hh24:mi:ss'') ';
           vSql = vSql || '   and to_timestamp('''||to_char(pDataFim, 'dd/mm/yyyy hh24:mi:ss')||''', ''dd/mm/yyyy hh24:mi:ss'') ';
           --And--
           --===================================
           if (pStatus = 1) then -- trabalhando
               vSql = vSql || ' and (a.equipamento_ignicao = ''ON'' and a.equipamento_veloc::numeric > 0 and a.ope_atividade_id is not null) ';
           end if;
           if (pStatus = 2) then -- ocioso
               vSql = vSql || ' and (a.equipamento_ignicao = ''ON'' and a.equipamento_veloc::numeric <= 0) ';
           end if;
           if (pStatus = 3) then -- desligado
               vSql = vSql || ' and (a.equipamento_ignicao != ''ON'') ';
           end if;
           if (pStatus = 4) then -- suspeito
               --vSql = vSql || ' and (a.equipamento_ignicao != ''ON'') ';
           end if;
           if (pWhereEmpresaId is not null and pWhereEmpresaId != '') then
               vSql = vSql || ' and (a.ger_empresa_id = '''|| pWhereEmpresaId ||''') ';
           end if;
           --
           if (pWhereEquipamentoId is not null and pWhereEquipamentoId != '') then
               vSql = vSql || ' and (a.ope_centro2_equip_id_1 = '''|| pWhereEquipamentoId ||''') ';
           end if;
           --
           if (pWhereOperadorId is not null and pWhereOperadorId != '') then
               vSql = vSql || ' and (a.ope_centro2_pessoa_id = '''|| pWhereOperadorId ||''') ';
           end if;
           --
           if (pWhereAtividadeId is not null and pWhereAtividadeId != '') then
               vSql = vSql || ' and (a.ope_atividade_id = '''|| pWhereAtividadeId ||''') ';
           end if;
           --
           if (pWhereAreaId is not null and pWhereAreaId != '') then 
               vSql = vSql || ' and (a.ope_centro2_id_area = '''|| pWhereAreaId ||''') ';
           end if;
           --
           
       
           --Group By
           --===================================
           vSql = vSql || ' group by a.unit_id ';
           if (pSelEmpresaId) then
               vSql = vSql || ', a.ger_empresa_id';
           end if;
           -- 
           if (pSelEquipamentoId) then
               vSql = vSql || ', a.ope_centro2_equip_id_1';
           end if;
          
           if (pSelOperadorId) then
               vSql = vSql || ', a.ope_centro2_pessoa_id';
           end if;
           --
           if (pSelAtividadeId) then
               vSql = vSql || ', a.ope_atividade_id';
           end if;
           --
           if (pSelAreaId) then
               vSql = vSql || ', a.ope_centro2_area_id';
           end if;
           --
           if (pSelStatus) then
               vSql = vSql || ', case when (a.equipamento_ignicao = ''ON'' and a.equipamento_veloc::numeric > 0 and a.ope_atividade_id is not null) then 1 ';
               vSql = vSql || '       when (a.equipamento_ignicao = ''ON'' and a.equipamento_veloc::numeric <= 0) then 2 ';
               vSql = vSql || '       when (a.equipamento_ignicao != ''ON'') then 3 ';
               vSql = vSql || '       else 4 '; -- definir melhor a regra do "Suspeito"
               vSql = vSql || '  end ';
           end if;
               
          
           --Query--
           --===================================
           raise notice 'vSql :%', vSql;
               
           for r in EXECUTE vSql loop
               unit_id = r.unit_id;
               --
               if (pSelEmpresaId) then
                   empresa_id = r.empresa_id;
               else 
                   empresa_id = null;
               end if;
               --
               if (pSelEquipamentoId) then
                   equipamento_id = r.equipamento_id;
               else 
                   equipamento_id = null;
               end if;
               --
               if (pSelOperadorId) then
                   operador_id = r.operador_id;
               else 
                   operador_id = null;
               end if;
               --
               if (pSelAtividadeId) then
                   atividade_id = r.atividade_id;
               else 
                   atividade_id = null;
               end if;
               --
               if (pSelAreaId) then
                   area_id = r.area_id;
               else 
                   area_id = null;
               end if;
               --
               if (pSelStatus) then
                   status = r.status;
               else
                   status = null;
               end if;
               
               --Agregates--
                  --==================================
                  if (pSelRpmMin) then
                   rpm_min = r.rpm_min;
               else 
                   rpm_min = null; 
               end if;
               --
               if (pSelRpmAvg) then
                   rpm_avg = r.rpm_avg;
               else 
                   rpm_avg = null; 
               end if;
               --
               if (pSelRpmMax) then
                   rpm_max = r.rpm_max;
               else 
                   rpm_max = null; 
               end if;
               --
               if (pSelHectaresTotal) then
                   hectares_total = r.hectares_total;
               else 
                   hectares_total = null;
               end if;
               --
               if (pSelHectaresAvg) then
                   hectares_avg = r.hectares_avg;
               else 
                   hectares_avg = null;
               end if;
               --
               if (pSelHorasTotal) then
                   horas_total = r.horas_total;
               else 
                   horas_total = null;
               end if;
               --
               if (pSelHorasAvg) then
                   horas_avg = r.horas_avg;
               else 
                   horas_avg = null;
               end if;
               --
                  if (pSelVelocidadeMin) then
                   velocidade_min = r.velocidade_min;
               else 
                   velocidade_min = null;
               end if;
               --
               if (pSelVelocidadeAvg) then
                   velocidade_avg = r.velocidade_avg;
               else 
                   velocidade_avg = null;
               end if;
               -- 
               if (pSelVelocidadeMax) then
                   velocidade_max = r.velocidade_max;
               else 
                   velocidade_max = null;
               end if;
               --
               return next;
               --
           end loop;
           --
           return;
       end;
       $function$;

       
       

       Drop FUNCTION IF EXISTS fnreport_decodeuri;

       
       create or replace function fnreport_decodeuri(pUri varchar)
       returns varchar as
       $function$
       declare
               vReplace varchar;
       begin
           vReplace = pUri;
               vReplace = REPLACE(vReplace,'%27',chr(39));
               vReplace = REPLACE(vReplace,'%20',chr(45));
               vReplace = REPLACE(vReplace,'%C3%AD',chr(237));		
               vReplace = REPLACE(vReplace,'%22',chr(34));
               if substr(vReplace,1,1) <> chr(39) then
               vReplace = chr(39)||vReplace||chr(39);
               end if;
               
               --raise notice 'Select replace %',vReplace;
               return vReplace;
       end;
       $function$
       language plpgsql;
       

       drop function if EXISTS fnreport_list;

       CREATE OR REPLACE FUNCTION fnreport_list(
       pParUnitId varchar, 
       pParIndRelId varchar,
       pParParams text
       )
       RETURNS TABLE(
        ind_rel_id varchar,
        ind_rel_par1 varchar,
        ind_rel_reportname varchar,
        ind_f1  varchar,
        ind_f2  varchar,
        ind_f3  varchar,
        ind_f4  varchar,
        ind_f5  varchar,
        ind_f6  varchar,
        ind_f7  varchar,
        ind_f8  varchar,
        ind_f9  varchar,
        ind_f10 varchar,
        ind_fd1 varchar,
        ind_fd2 varchar,
        ind_fd3 varchar,
        ind_fd4 varchar,
        ind_fd5 varchar,
        ind_fd6 varchar,
        ind_fd7 varchar,
        ind_fd8 varchar,
        ind_fd9 varchar,
        ind_fd10 varchar,
        ind_fl1 varchar ,
        ind_fl2 varchar ,
        ind_fl3 varchar ,
        ind_fl4 varchar ,
        ind_fl5 varchar ,
        ind_fl6 varchar ,
        ind_fl7 varchar ,
        ind_fl8 varchar ,
        ind_fl9 varchar ,
        ind_fl10 varchar
       ) 
        AS $BODY$
       declare
       vMsg text := '';
       vSql text;
       vPar1 varchar := '';
       r record;
       l record;
       pJ json;
       pJNv json;
       vParBuscaTabela varchar;
       vParBuscaCampoNome varchar;
       vParBuscaCampoId varchar;
       vParNome varchar;
       vParNomeTec varchar;
       vColNomeTec varchar;
       vColNomeTecPrefixo varchar;
       vParValor varchar;
       vParValorDec varchar;
       vParParams varchar;
       vNameReport varchar;
       vParRelVar varchar := '';
       vIdxCol integer := 1;
       pParCampos varchar[];
       
       begin
       
           vMsg = 'Posição 1';
        vParParams = REPLACE(pParParams,'%22',chr(34));
       
        vMsg = 'Posição 3B'||vParParams;		
        select vParParams::json 
           into pJ;
       
       
        vMsg = 'Posição 2';
        select r2.config_ftd::json->>'query'::text, r1.nome as nome
          into vSql
        from ind_rel r1,
             ind_ftd r2
        where r1.ind_ftd_id = r2.id
          and r1.id = pParIndRelId;
            
           vMsg = 'Posição 3';
           SELECT
               r1.nome INTO vNameReport 
           FROM
               ind_rel r1 
           WHERE
               r1.ID = pParIndRelId;
               
           vMsg = 'Posição 4';
         for pJNv in select  * from json_array_elements((pJ->>'cols')::json)
             loop
                   
                   vColNomeTec = pJNv->>'colNomeTec';
                   vColNomeTecPrefixo = pJNv->>'colNomeTecPrefixo';
       
                   if vIdxCol = 1 then
                       vParRelVar = vParRelVar||' '||vColNomeTecPrefixo||'.'||vColNomeTec||' as f'||vIdxCol;
                       
                   else
                       vParRelVar = vParRelVar||' ,'||vColNomeTecPrefixo||'.'||vColNomeTec||' as f'||vIdxCol;
                   end if;			
                   
                   vParRelVar = vParRelVar||' ,(Select r1.var_nome_descritivo as fd'||vIdxCol||'  from ind_rel_var r1 where r1.ind_rel_id = '''||pParIndRelId||''' and r1.var_nome_tecnico = '''||vColNomeTec||''' limit 1 )  ';
               
                   vMsg = 'Posição 14';		
                   vParRelVar = vParRelVar|| ',(Select r1.largura as fl'||vIdxCol||' from ind_rel_var r1 where r1.ind_rel_id = '''||pParIndRelId||''' and r1.var_nome_tecnico = '''||vColNomeTec||''' limit 1)  ';
                   vIdxCol := vIdxCol+1;
                   
          end loop;
        
        
            for x in vIdxCol..10 loop
                       vMsg = 'Posição 14';	
                   
                       vParRelVar = vParRelVar||' ,(Select null as f'||x||') ';
                       vParRelVar = vParRelVar||' ,(Select null as fd'||x||') ';
                       vParRelVar = vParRelVar||' ,(Select null as fl'||x||') ';
                           
       
            end loop;
       
       vMsg = 'Posição 24';		
        vSql = replace(vSql,' /*FIELDS*/ ',vParRelVar);
       
        vMsg = 'Posição 25';		
        vSql = replace(vSql,'\${pParUnitId}',''''||pParUnitId||'''');
           
           vMsg = 'Posição 27';		
           for pJNv in select  * from json_array_elements((pJ->>'params')::json)
           loop
                   vParNomeTec := pJNv->>'parNomeTec';
                   vParValor := pJNv->>'parValor';
                   vParValor := REPLACE((vParValor),'%20',chr(32));
                   vParValor := REPLACE((vParValor),'%C3%AD',chr(237));
                   vParValor := REPLACE((vParValor),'%22',chr(34));
               vMsg = 'Posição 28';
                 if vParValor is null then
       -- 			vSql = replace(vSql,'\${'||vParNomeTec||'}',);

                       vSql = replace(vSql,'\${'||vParNomeTec||'}',null);
                   else
                       vSql = replace(vSql,'\${'||vParNomeTec||'}',''''||vParValor||'''');
                   end if;
                   RAISE NOTICE 'NomeValor % %', pJNv->>'parNomeTec', vParValor;
                   
                   --Busca campos para montar siglas dos parametros
                   vParBuscaTabela := '';
                   vParBuscaCampoNome := '';
                   vParBuscaCampoId := '';
                   vParNome := '';
                   vParValorDec := '';
                   vMsg = 'Posição 28';		
                   select p1.busca_tabela, p1.busca_campo_nome,  p1.busca_campo_id, p1.nome
                       into vParBuscaTabela, vParBuscaCampoNome, vParBuscaCampoId, vParNome
                       from ind_prm p1
                       join ind_rel_relac_prm p2 on(p1.id = p2.ind_prm_id)
                    where p2.ind_rel_id = pParIndRelId
                        and p1.nome_tecnico = vParNomeTec;
                   vMsg = 'Posição 29';		
                       
               if vParBuscaTabela != '' and vParBuscaCampoNome != '' and vParBuscaCampoId != '' and vParValorDec != '' then
               vMsg = 'Posição 30';		
                        vParValorDec := fnreport_decodeuri(vParValor);
                        vPar1 := vPar1||' ['||fnreport_sigla(pParUnitId,vParBuscaTabela,vParBuscaCampoNome,			 	vParBuscaCampoId,vParValorDec)||'] '||chr(13)||chr(10);
       -- 					raise notice 'Parametros 1 % ',vPar1;
                else
                       if vParNome != null or vParNome != '' then
                               vPar1 := vPar1||vParNome||' ['||vParValor||'] '||chr(13)||chr(10);
                       end if;
       -- 			 raise notice 'ParNome 1 % ',vParNome;
                end if;
               
           end loop;
       
        vMsg = 'Posição 30A '||vSql;
        raise notice '%',vSql;
        
       for r in EXECUTE vSql loop
           vMsg = 'Posição 31';			 
           ind_rel_id := pParIndRelId;
           ind_rel_par1 := vPar1;
           ind_rel_reportname := vNameReport;
           ind_f1 := r.f1;
           ind_f2 := r.f2;
           ind_f3 := r.f3;
           ind_f4 := r.f4;
           ind_f5 := r.f5;
           ind_f6 := r.f6;
           ind_f7 := r.f7;
           ind_f8 := r.f8;
           ind_f9 := r.f9;
           ind_f10 := r.f10;
           
           ind_fd1 := r.fd1;
           ind_fd2 := r.fd2;
            ind_fd3 := r.fd3;
           ind_fd4 := r.fd4;
            ind_fd5 := r.fd5;
            ind_fd6 := r.fd6;
           ind_fd7 := r.fd7;
           ind_fd8 := r.fd8;
           ind_fd9 := r.fd9;
           ind_fd10 := r.fd10;
           
            ind_fl1 := r.fl1;
           ind_fl2 := r.fl2;
           ind_fl3 := r.fl3;
           ind_fl4 := r.fl4;
           ind_fl5 := r.fl5;
           ind_fl6 := r.fl6;
           ind_fl7 := r.fl7;
           ind_fl8 := r.fl8;
           ind_fl9 := r.fl9;
           ind_fl10 := r.fl10;
           return next;
           
       end loop;
       
       return;
       
       
       EXCEPTION WHEN others THEN		
           Raise EXCEPTION ' % % ', vMsg, SQLERRM;
       
       end;
       $BODY$
         LANGUAGE plpgsql VOLATILE;;
       
       
       
       -----------
       
       

       Drop FUNCTION IF EXISTS fnreport_par;;

       CREATE OR REPLACE FUNCTION fnreport_par(
       pParUnitId varchar, 
       pParIndRelId varchar,
       pParParams text
       )
       RETURNS varchar
       
       AS $BODY$
       declare
       vSql text;
       vPar1 varchar;
       r record;
       pJ json;
       pJNv json;
       vParNome varchar;
       vParNomeTec varchar;
       vParValor varchar;
       vParValorDec varchar;
       vParParams varchar;
       busca_tabela varchar;
       busca_campo_nome varchar;
       busca_campo_id varchar;
       ind_rel_par1 varchar;
       vSiglas varchar;
       jsonKey varchar;
       paramsrel VARCHAR;
       existParam integer := 0;
       paramVar varchar;
       begin
                   
               vParParams = REPLACE(pParParams,'%22',chr(34));
               vParParams = TRANSLATE(vParParams,chr(35),chr(34));
               ind_rel_par1 = '';
               
               select vParParams::json
           into pJ;
               
           
               
                for pJNv in select  * from json_array_elements((pJ)::json) 
                loop
       
               
                    select json_object_keys(pJNv::json) into jsonKey;
                   
                   vParValor := pJNv->>jsonKey;
                   vParNomeTec := jsonKey;
           
                   
                   
               select id into paramVar from ind_prm where nome_tecnico = vParNomeTec;
       
               select count(*) into existParam from ind_rel_relac_prm relac
                where relac.ind_rel_id = pParIndRelId
                and relac.ind_prm_id = paramVar;
                
                Raise Notice ' Variavel Id%',paramVar;
                
                   raise notice 'Return de Params % ', existParam;
                   
                   If (existParam > 0) Then
                   
                   RAISE NOTICE ' Parametro Existe Para Esse Relatorio %', existParam;	
                   busca_tabela = '';
                   busca_campo_nome = '';
                   busca_campo_id = '';
                   
           
                   
                   select indP.busca_tabela, indP.busca_campo_nome, indP.busca_campo_id, indP.nome
                     into busca_tabela, busca_campo_nome, busca_campo_id, vParNome
                     from ind_prm indP 
                 where indP.nome_tecnico = vParNomeTec;
       
                   If busca_tabela Is Not Null Then
                       
                       vParValorDec := fnreport_decodeuri(vParValor);
                       
                       select fnreport_sigla(pParUnitId,busca_tabela,busca_campo_nome,busca_campo_id,vParValorDec)
                       into vSiglas;
                    
                   If vSiglas Is Null Then
                   vSiglas := '';	
                 End If;
                   
                   ind_rel_par1 := ind_rel_par1 || vParNome||' ['||vSiglas||'] '||chr(13)||chr(10);
                   
                   ELSE
                   
                   ind_rel_par1 := ind_rel_par1 || vParNome||' ['||vParValor||'] '||chr(13)||chr(10);
                   
                 END IF;
                   
       
                   ELSE
                   
                       RAISE NOTICE ' Sem Parametros';	
                   End If;
           
               End Loop;
           
           
               return ind_rel_par1;
       end;
       $BODY$
         LANGUAGE plpgsql VOLATILE;;
       
       
       -----------
       
       

       Drop FUNCTION IF EXISTS fnreport_par_json;;

       create or replace FUNCTION fnreport_par_json(parNomeTec text,parValor text) 
       Returns text 
       AS $BODY$
       declare
       pValue varchar;
       pValueTec varchar;
       pRet varchar;
       contador integer;
       
       begin
         pValue := '{"params":[';
               
           for contador in 1 .. array_upper(parNomeTec, 1) loop
           
                       if  contador = 1 then
                       
                               pValue := pValue||jsonb_build_object('parNomeTec',parNomeTec[contador], 'parValor',parValor[	contador]);	
                               
                       end if;
                       
                       if contador >= 2 then 
                       
                           pValue := pValue||' , '|| jsonb_build_object('parNomeTec',parNomeTec[contador], 'parValor',parValor[contador]);
       
                       end if;
           
           end loop;
               raise notice '%:',pValue;
               pValue := pValue||']}';
               
               return pValue;
       
       end;
       $BODY$
         LANGUAGE plpgsql VOLATILE;;
       
       
       -----------
       
       

       Drop FUNCTION IF EXISTS fnreport_sigla;;

       create or replace function fnreport_sigla(pParUnitId varchar, pTabela varchar, pCampoSigla varchar, pCampoWhere varchar, pValorWhere varchar)
       returns varchar as
       $function$
       declare
           vSql varchar;
               vRet varchar;
               vExistUnitId integer := 0;
       begin
           
               select count(1)
                   into 	vExistUnitId
                   from information_schema.columns  where upper(table_name) = upper(pTabela)  and upper(column_name) = 'UNIT_ID';
       
               vSql := 'select STRING_AGG(t1.'||pCampoSigla||', '' ; '' ORDER BY t1.'||pCampoSigla||') AS grp
                              from '||pTabela||' t1
                             where '||pCampoWhere||' in('||pValorWhere||')';
                   
                   
                   if (vExistUnitId > 0) and (pParUnitId != null) then
                      vSql := vSql || ' and unit_id = '''||pParUnitId||'''' ;
                   end if;
               
                --raise notice 'fnreport_sigla Sql:%', vSql;
       
           execute vSql into vRet;
       
           return vRet;
       
       end;
       $function$
       language plpgsql;;
       
       
       
       
       
       -----------
       
       

       Drop FUNCTION IF EXISTS fnreport0009;;

       CREATE OR REPLACE FUNCTION fnreport0009(
       pParUnitId varchar, 
       pParIndRelId varchar, 
       pVart01 varchar, 
       pVard01 varchar, 
       pVart02 varchar default null,
       pVard02 varchar default null,
       pVart03 varchar default null,
       pVard03 varchar default null,
       pVart04 varchar default null,
       pVard04 varchar default null,
       pVart05 varchar default null,
       pVard05 varchar default null,
       pParFinPagRecES varchar default null,
       pParGerPessoaNome varchar default null,
       pParGerPessoaPagRecNome varchar default null,
       pParFinPagRecDataMovIni varchar default null,
       pParFinPagRecDataMovFin varchar default null,
       pParFinPagRecNumeroDocPagRec varchar default null,
       pParFinPagRecParcValorPagRecIni varchar default null,
       pParFinPagRecParcValorPagRecFin varchar default null,
       pParFinPagRecParcValorJuroIni varchar default null,
       pParFinPagRecParcValorJuroFin  varchar default null,
       pParFinPagRecParcValorDescontoIni varchar default null,
       pParFinPagRecParcValorDescontoFin varchar default null,
       pParFinPagRecParcValorMultaIni varchar default null,
       pParFinPagRecParcValorMultaFin varchar default null,
       pParFinPagRecParcDataVencIni varchar default null,
       pParFinPagRecParcDataVencFin varchar default null,
       pParFinPagRecDataBaixaIni varchar default null,
       pParFinPagRecDataBaixaFin varchar default null,
       pParLogUserIns varchar default null,
       pParLogDateInsIni varchar default null,
       pParLogDateInsFin varchar default null,
       pParLogUserUpd varchar default null,
       pParLogDateUpdIni varchar default null,
       pParLogDateUpdFin varchar default null
       
       
       )
       RETURNS TABLE(
        ind_rel_id varchar,
        ind_rel_par1 varchar,
        ind_rel_par2 varchar,
        ind_rel_par3 varchar,
        vart_01 varchar,
        vard_01 varchar,
        vart_02 varchar,
        vard_02 varchar,
        vart_03 varchar,
        vard_03 varchar,
        vart_04 varchar,
        vard_04 varchar,
        vart_05 varchar,
        vard_05 varchar,
        valor_01 numeric,
        valor_02 numeric,
        valor_03 numeric,
        valor_04 numeric,
        valor_05 numeric,
        valor_06 numeric,
        valor_07 numeric,
        valor_08 numeric,
        valor_09 numeric,
        valor_10 numeric) AS $BODY$
       declare
       vSql varchar;
       vPar1 varchar :='';
       vPar2 varchar :='';
       r record;
       begin
               
       
           
            if pParFinPagRecES != '' then
                vPar1 = vPar1||' Entrada/Saída ['||pParFinPagRecES||']'||chr(13)||chr(10);
            else
                   vPar1 = vPar1||' Entrada/Saída []'||chr(13)||chr(10);
            end if;
            
            if pParGerPessoaNome != '' then
                vPar1 = vPar1||' Nome da Pessoa(s) ['||pParGerPessoaNome||']'||chr(13)||chr(10);
            else
                   vPar1 = vPar1||' Nome da Pessoa(s) []'||chr(13)||chr(10);
            end if;
            
            if pParGerPessoaPagRecNome != '' then
               vPar1 = vPar1||' Nome Pessoa Pag/Rec ['||pParGerPessoaPagRecNome||']'||chr(13)||chr(10);
            else 
               vPar1 = vPar1||' Nome Pessoa Pag/Rec []'||chr(13)||chr(10);
            end if;
       
            if pParFinPagRecNumeroDocPagRec != '' then
               vPar1 = vPar1||' Numero Documento Pag/Rec ['||pParFinPagRecNumeroDocPagRec||']'||chr(13)||chr(10);
           else 
               vPar1 = vPar1||' Numero Documento Pag/Rec []'||chr(13)||chr(10);
           end if;
           
           if pParLogUserIns != '' then
               vPar1 = vPar1||' Usuario(s) de inserção ['||pParLogUserIns||'] '||chr(13)||chr(10);
           else
                   vPar1 = vPar1||' Usuario(s) de inserção [] '||chr(13)||chr(10);
           end if;
            
           if pParLogUserUpd != '' then
               vPar1 = vPar1||' Usuario(s) de alteração ['||pParLogUserUpd||'] '||chr(13)||chr(10);
           else
               vPar1 = vPar1||' Usuario(s) de alteração [] '||chr(13)||chr(10);	
           end if;
            
       
           if pParFinPagRecParcDataVencIni != '' and pParFinPagRecParcDataVencFin != '' then
               vPar1 = vPar1||' Data Vencimento ['||pParFinPagRecParcDataVencIni ||'] até ['||pParFinPagRecParcDataVencFin||'] '||chr(13)||chr(10);
           else
               vPar1 = vPar1||' Data Vencimento [] até [] '||chr(13)||chr(10);
           end if;
           
           ------------------------------------------------------------------------------
        if pParFinPagRecDataMovIni != '' and pParFinPagRecDataMovFin != '' then
               vPar2 = vPar2|| 'Data Movimento ['||pParFinPagRecDataMovIni ||'] até ['||pParFinPagRecDataMovFin||'] '||chr(13)||chr(10);
           else
           vPar2 = vPar2|| 'Data Movimento [] até []'||chr(13)||chr(10);
           end if;
           
           
           
            if pParFinPagRecParcValorPagRecIni != '' and pParFinPagRecParcValorPagRecFin != ''   then
               vPar2 = vPar2|| 'Valor Inicial Pag/Rec ['||pParFinPagRecParcValorPagRecIni ||'] até ['||pParFinPagRecParcValorPagRecFin||'] '||chr(13)||chr(10);
           else
           vPar2 = vPar2|| 'Valor Inicial Pag/Rec [] até [] '||chr(13)||chr(10);
           end if;
       
           if pParFinPagRecParcValorJuroIni != '' and pParFinPagRecParcValorJuroFin != ''  then
               vPar2 = vPar2|| 'Valor De Juros Inicial Pag/Rec  ['||pParFinPagRecParcValorJuroIni ||'] até ['||pParFinPagRecParcValorJuroFin||'] '||chr(13)||chr(10);
       else
               vPar2 = vPar2|| 'Valor De Juros Inicial Pag/Rec [] até [] '||chr(13)||chr(10);
       end if;
       
            if pParFinPagRecParcValorDescontoIni != '' and pParFinPagRecParcValorDescontoFin != ''  then
                   vPar2 = vPar2|| 'Valor De Desconto Inicial ['||pParFinPagRecParcValorDescontoIni ||'] até ['||pParFinPagRecParcValorDescontoFin||'] '||chr(13)||chr(10);
           else
           vPar2 = vPar2|| 'Valor De Desconto Inicial [] até [] '||chr(13)||chr(10);
           end if;
       
       if pParFinPagRecParcValorMultaIni != '' and pParFinPagRecParcValorMultaFin != '' then
               vPar2 = vPar2|| 'Valor Da Multa Inicial ['||pParFinPagRecParcValorMultaIni ||'] até ['||pParFinPagRecParcValorMultaFin||'] '||chr(13)||chr(10);
       else
               vPar2 = vPar2|| 'Valor Da Multa Inicial [] até [] '||chr(13)||chr(10);
       end if;
       
       if pParLogDateInsIni != '' and pParLogDateInsFin != '' then
               vPar2 = vPar2|| 'Data Inserção ['||pParLogDateInsIni ||'] até ['||pParLogDateInsFin||'] '||chr(13)||chr(10);
       else
               vPar2 = vPar2|| 'Data Inserção [] até [] '||chr(13)||chr(10);
       end if;
       
       if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then
               vPar2 = vPar2|| 'Data Alteração ['||pParLogDateUpdIni ||'] até ['||pParLogDateUpdFin||'] '||chr(13)||chr(10);
       else
               vPar2 = vPar2|| 'Data Alteração [] até []'||chr(13)||chr(10);
       end if;
           
               
       if pParFinPagRecDataBaixaIni != '' and pParFinPagRecDataBaixaFin != '' then
               vPar2 = vPar2|| 'Data Baixa ['||pParFinPagRecDataBaixaIni ||'] até ['||pParFinPagRecDataBaixaFin||'] '||chr(13)||chr(10);
       else
               vPar2 = vPar2|| 'Data Baixa [] até []'||chr(13)||chr(10);
       end if;
           
           
               
       vSql = 'select
           '  || pVart01 ||'   as vart_01 '||
               ','''|| pVard01 ||''' as vard_01 ';
               
               if  pVart02 != ''  THEN
                vSql = vSql || ','  || pVart02 ||'   as vart_02 '||
                          ','''|| pVard02 ||''' as vard_02 ';
               else 
                  vSql = vSql || ',null as vart_02'||
                                      ',null as vard_02';
               end if;
           if  pVart03 != '' THEN
                vSql = vSql || ','  || pVart03 ||'   as vart_03 '||
                          ','''|| pVard03 ||''' as vard_03 ';
               else 
                  vSql = vSql || ',null as vart_03'||
                                      ',null as vard_03';
               end if;
           if  pVart04 != '' THEN
                vSql = vSql || ','  || pVart04 ||'   as vart_04 '||
                          ','''|| pVard04 ||''' as vard_04 ';
               else 
                  vSql = vSql || ',null as vart_04'||
                                      ',null as vard_04';
               end if;
           if  pVart05 != ''  THEN
                vSql = vSql || ','  || pVart05 ||'   as vart_05 '||
                          ','''|| pVard05 ||''' as vard_05 ';
               else 
                  vSql = vSql || ',null as vart_05'||
                                      ',null as vard_05';
               end if;
                       
               vSql = vSql||' ,sum(t1.fin_pagrec_parc_valor_pagrec) as valor_01
                                            ,sum(t1.fin_pagrec_parc_valor_juro)  as valor_02
                                            ,sum(t1.fin_pagrec_parc_valor_desconto) as valor_03
                                            ,sum(t1.fin_pagrec_parc_valor_multa) as valor_04
                                            ,sum(COALESCE((select sum(s1.valor_pagrec) 
                                                            from fin_pagrec_baixa s1 
                                                                            where s1.fin_pagrec_parc_id = t1.fin_pagrec_parc_id ';
                                                 if pParFinPagRecDataBaixaIni != '' and pParFinPagRecDataBaixaFin != ''then
                                                       vSql = vSql ||' and '||'CAST(s1.data_baixa AS DATE)'||' >= '''||pParFinPagRecDataBaixaIni||''''||' 
                                                                       and  CAST(s1.data_baixa AS DATE)'||' <= '''||pParFinPagRecDataBaixaFin||'''';
                                               end if;
                                            
                                            vSql = vSql||'),0)) as valor_05,	 
                                            (SUM ( t1.fin_pagrec_parc_valor_pagrec )-sum(t1.fin_pagrec_parc_valor_desconto)+
                                            SUM ( t1.fin_pagrec_parc_valor_juro )+
                                            sum(t1.fin_pagrec_parc_valor_multa)-
                                           sum(COALESCE((select sum(s1.valor_pagrec) 
                                                                                    from fin_pagrec_baixa s1 
                                                                                    where s1.fin_pagrec_parc_id = t1.fin_pagrec_parc_id ';
                                                        if pParFinPagRecDataBaixaIni != '' and pParFinPagRecDataBaixaFin != ''then
                                                               vSql = vSql ||' and '||'CAST(s1.data_baixa AS DATE)'||' >= '''||pParFinPagRecDataBaixaIni||''''||' 
                                                                                               and  CAST(s1.data_baixa AS DATE)'||' <= '''||pParFinPagRecDataBaixaFin||'''';
                                                       end if;
                                            vSql = vSql||'),0))) as valor_06
                                   from vwfin_pagrec_geral t1 where 1=1 ';
               
               -- And--
               --===================================
       
            if pParUnitId != '' then
                   vSql = vSql ||' and t1.fin_pagrec_unit_id '||' in('''||pParUnitId||''')';
            end if;
            
            if pParFinPagRecES != '' then 
               vSql = vSql ||' and '||' t1.fin_pagrec_tipo_es'||' like '||'''' ||pParFinPagRecES||''' ';
            end if;
            
            if pParGerPessoaNome != '' then 
               vSql = vSql ||' and '||'t1.ger_pessoa_nome'||' like '||'''' ||pParGerPessoaNome||''' ';
            end if;	 
            
            if pParGerPessoaPagRecNome != '' then 
               vSql = vSql ||' and '||'t1.ger_pessoa_pagrec_nome'||' like '||'''' ||pParGerPessoaPagRecNome||''' ';
            end if;	 
            
            if pParFinPagRecDataMovIni != '' and pParFinPagRecDataMovFin != '' then 	
                vSql = vSql ||' and '||'t1.fin_pagrec_data_mov'||' >= '''||pParFinPagRecDataMovIni||''''||' and t1.fin_pagrec_data_mov'||' <= '''||pParFinPagRecDataMovFin||'''';
             end if;
            
            if pParFinPagRecNumeroDocPagRec != '' then 
               vSql = vSql ||' and t1.fin_pagrec_numero_doc_pagrec like '||'''' ||pParFinPagRecNumeroDocPagRec||''' ';
            end if;
               
            if pParFinPagRecParcValorPagRecIni != '' and pParFinPagRecParcValorPagRecFin != '' then 
               vSql = vSql ||' and '||'t1.fin_pagrec_parc_valor_pagrec'||' >= '''||pParFinPagRecParcValorPagRecIni||''''||'and t1.fin_pagrec_parc_valor_pagrec'||' <= '''||pParFinPagRecParcValorPagRecFin||'''';
               end if;
       
            if pParFinPagRecParcValorJuroIni != '' and pParFinPagRecParcValorJuroFin != '' then 
               vSql = vSql ||' and '||'t1.fin_pagrec_parc_valor_juro'||' >= '''||pParFinPagRecParcValorJuroIni||''''||'and t1.fin_pagrec_parc_valor_juro'||' <= '''||pParFinPagRecParcValorJuroFin||'''';
            end if;
            
            if pParFinPagRecParcValorDescontoIni != '' and  pParFinPagRecParcValorDescontoFin != '' then 
            vSql = vSql ||' and '||'t1.fin_pagrec_parc_valor_desconto'||' >= '''||pParFinPagRecParcValorDescontoIni||''''||'and t1.fin_pagrec_parc_valor_desconto'||' <= '''||pParFinPagRecParcValorDescontoFin||'''';
            end if;	 
            
            if pParFinPagRecParcValorMultaIni != '' and pParFinPagRecParcValorMultaFin != '' then 
               vSql = vSql ||' and '||'t1.fin_pagrec_parc_valor_multa'||' >= '''||pParFinPagRecParcValorMultaIni||''''||' and '||'t1.fin_pagrec_parc_valor_multa'||' <= '''||pParFinPagRecParcValorMultaFin||'''';
            end if;
       
            if pParFinPagRecParcDataVencIni != '' and pParFinPagRecParcDataVencFin != '' then 
               vSql = vSql ||' and '||'t1.fin_pagrec_parc_data_venc'||' >= '''||pParFinPagRecParcDataVencIni||''''||
            ' and t1.fin_pagrec_parc_data_venc'||' <= '''||pParFinPagRecParcDataVencFin||''''; 
            end if;
            
            if pParLogUserIns != '' then 
               vSql = vSql ||' and '||'t1.log_user_ins'||' in('''||pParLogUserIns||''')';
            end if; 
            
            if pParLogDateInsIni != '' and pParLogDateInsFin != '' then 
               vSql = vSql ||' and '||' CAST(t1.log_date_ins AS DATE)'||' >= '''||pParLogDateInsIni||''''||'and CAST(t1.log_date_ins AS DATE)'||' <= '''||pParLogDateInsFin||'''';
            end if;		 
            
            if pParLogUserUpd != '' then 
               vSql = vSql ||' and '||'t1.log_user_upd'||' in('''||pParLogUserUpd||''')';
            end if;
            
            if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then 
               vSql = vSql ||' and '||'CAST(t1.log_date_upd AS DATE)'||' >= '''||pParLogDateUpdIni||''''||' and  CAST(t1.log_date_upd AS DATE)'||' <= '''||pParLogDateUpdFin||'''';
            end if;	
            
       
       
            
               -- Group By
            -- ===================================
               vSql = vSql||' group by '|| pVart01;
       
               if  pVart02 != ''  THEN
                vSql = vSql||  ','|| pVart02;
               end if;
               
           if  pVart03 != ''  THEN
                vSql = vSql||  ','|| pVart03;
               end if;
               
           if  pVart04 != ''  THEN
                vSql = vSql||  ','|| pVart04;
               end if;
               
           if  pVart05 != ''  THEN
                vSql = vSql||  ','|| pVart05;
               end if;
               
            -- Order By
            -- ===================================
               vSql = vSql||' order by '|| pVart01;
       
               if  pVart02 != ''  THEN
                vSql = vSql||  ','|| pVart02;
               end if;
               
           if  pVart03 != ''  THEN
                vSql = vSql||  ','|| pVart03;
               end if;
               
           if  pVart04 != ''  THEN
                vSql = vSql||  ','|| pVart04;
               end if;
               
           if  pVart05 != ''  THEN
                vSql = vSql||  ','|| pVart05;
               end if;
               
               raise notice 'vSql2 :%', vSql;
       
       for r in EXECUTE vSql loop
       ind_rel_id := pParIndRelId;
       ind_rel_par1 := vPar1;
       ind_rel_par2 := vPar2;
        vart_01 := r.vart_01;
        vard_01 := r.vard_01;
        vart_02 := r.vart_02;
        vard_02 := r.vard_02;
        vart_03 := r.vart_03;
        vard_03 := r.vard_03;
        vart_04 := r.vart_04;
        vard_04 := r.vard_04;
        vart_05 := r.vart_05;
        vard_05 := r.vard_05;
        valor_01 := r.valor_01;
        valor_02 := r.valor_02;
        valor_03 := r.valor_03;
        valor_04 := r.valor_04;
        valor_05 := r.valor_05;
        valor_06 := r.valor_06;
       return next;
       end loop;
       return;
       end;
       $BODY$
         LANGUAGE plpgsql VOLATILE;;
       
       
       
       -----------
       
       

       Drop FUNCTION IF EXISTS fnreport0014;;
       CREATE 	OR REPLACE FUNCTION fnreport0014(
       pParUnitId VARCHAR,
       pParIndRelId VARCHAR,
       pVart01 VARCHAR,
       pVard01 VARCHAR,
       pVart02 VARCHAR DEFAULT NULL,
       pVard02 VARCHAR DEFAULT NULL,
       pVart03 VARCHAR DEFAULT NULL,
       pVard03 VARCHAR DEFAULT NULL,
       pVart04 VARCHAR DEFAULT NULL,
       pVard04 VARCHAR DEFAULT NULL,
       pVart05 VARCHAR DEFAULT NULL,
       pVard05 VARCHAR DEFAULT NULL,
       pVart06 VARCHAR DEFAULT NULL,
       pVard06 VARCHAR DEFAULT NULL,
       pVart07 VARCHAR DEFAULT NULL,
       pVard07 VARCHAR DEFAULT NULL,
       pVart08 VARCHAR DEFAULT NULL,
       pVard08 VARCHAR DEFAULT NULL,
       pVart09 VARCHAR DEFAULT NULL,
       pVard09 VARCHAR DEFAULT NULL,
       pVart10 VARCHAR DEFAULT NULL,
       pVard10 VARCHAR DEFAULT NULL,
       pParCentro2AreaId VARCHAR DEFAULT NULL,
       pParBlocoCol VARCHAR DEFAULT NULL,
       pParTipoSoloId VARCHAR DEFAULT NULL,
       pParTipoSoloNome VARCHAR DEFAULT NULL,
       pParEspacId VARCHAR DEFAULT NULL,
       pParEspacNome VARCHAR DEFAULT NULL,
       pParAtivSisPlanId VARCHAR DEFAULT NULL,
       pParAtivSisPlanNome VARCHAR DEFAULT NULL,
       pParAtivSisCultId VARCHAR DEFAULT NULL,
       pParAtivSisCultNome VARCHAR DEFAULT NULL,
       pParAtivSisColhId VARCHAR DEFAULT NULL,
       pParAtivSisColhNome VARCHAR DEFAULT NULL,
       pParItemServId VARCHAR DEFAULT NULL,
       pParItemServNome VARCHAR DEFAULT NULL,
       pParItemServAtivo VARCHAR DEFAULT NULL,
       pParDataIniPlan VARCHAR DEFAULT NULL,
       pParDataIniPlanFin VARCHAR DEFAULT NULL,
       pParDataFinPlanIni VARCHAR DEFAULT NULL,
       pParDataFinPlan VARCHAR DEFAULT NULL,
       
       pParDataUltPlanIni VARCHAR DEFAULT NULL,
       pParDataUltPlanFin VARCHAR DEFAULT NULL,
       
       pParDataIniCol VARCHAR DEFAULT NULL,
       pParDataIniColFin VARCHAR DEFAULT NULL,
       pParDataFinColIni VARCHAR DEFAULT NULL,
       pParDataFinCol VARCHAR DEFAULT NULL,
       
       pParDataUltColIni VARCHAR DEFAULT NULL,
       pParDataUltColFin VARCHAR DEFAULT NULL,
       
       
       pParDataFloradaIni VARCHAR DEFAULT NULL,
       pParDataFloradaFin VARCHAR DEFAULT NULL,
       
       
       pParDataEmergIni VARCHAR DEFAULT NULL,
       pParDataEmergFin VARCHAR DEFAULT NULL,
       
       pParUnidadeMedId VARCHAR DEFAULT NULL,
       pParUnidadeMedNome VARCHAR DEFAULT NULL,
       pParCentro1Id VARCHAR DEFAULT NULL,
       pParCentro1Nome VARCHAR DEFAULT NULL,
       pParCentro1Ativo VARCHAR DEFAULT NULL,
       pParCentro2Id VARCHAR DEFAULT NULL,
       pParCentro2Nome VARCHAR DEFAULT NULL,
       pParCentro2Ativo VARCHAR DEFAULT NULL,
       pParSubTipoId VARCHAR DEFAULT NULL,
       pParSubTipoNome VARCHAR DEFAULT NULL,
       pParTipoId VARCHAR DEFAULT NULL,
       pParTipoNome VARCHAR DEFAULT NULL,
       pParRatTipoId VARCHAR DEFAULT NULL,
       pParRatTipoNome VARCHAR DEFAULT NULL,
       pParSubGrupoId VARCHAR DEFAULT NULL,
       pParSubGrupoNome VARCHAR DEFAULT NULL,
       pParGrupoId VARCHAR DEFAULT NULL,
       pParGrupoNome VARCHAR DEFAULT NULL,
       pParGrupoAtivo VARCHAR DEFAULT NULL,
       pParPeriodoId VARCHAR DEFAULT NULL,
       pParPeriodoNome VARCHAR DEFAULT NULL,
       pParPeriodoAtivo VARCHAR DEFAULT NULL,
       pParPeriodoDataIni VARCHAR DEFAULT NULL,
       pParPeriodoDataFin VARCHAR DEFAULT NULL,
       pParLogUserIns VARCHAR DEFAULT NULL,
       pParLogDateInsIni VARCHAR DEFAULT NULL, 
       pParLogDateInsFin VARCHAR DEFAULT NULL, 
       pParLogUserUpd VARCHAR DEFAULT NULL,
       pParLogDateUpdIni VARCHAR DEFAULT NULL,
       pParLogDateUpdFin VARCHAR DEFAULT NULL		
           ) 
               RETURNS TABLE (
               ind_rel_id VARCHAR,
               ind_rel_par1 VARCHAR,
               ind_rel_par2 VARCHAR,
               ind_rel_par3 VARCHAR,
               vart_01 VARCHAR,
               vard_01 VARCHAR,
               vart_02 VARCHAR,
               vard_02 VARCHAR,
               vart_03 VARCHAR,
               vard_03 VARCHAR,
               vart_04 VARCHAR,
               vard_04 VARCHAR,
               vart_05 VARCHAR,
               vard_05 VARCHAR,
               vart_06 VARCHAR,
               vard_06 VARCHAR,
               vart_07 VARCHAR,
               vard_07 VARCHAR,
               vart_08 VARCHAR,
               vard_08 VARCHAR,
               vart_09 VARCHAR,
               vard_09 VARCHAR,
               vart_10 VARCHAR,
               vard_10 VARCHAR,
               valor_01 NUMERIC,
               valor_02 NUMERIC,
               valor_03 NUMERIC,
               valor_04 NUMERIC,
               valor_05 NUMERIC,
               valor_06 NUMERIC,
               valor_07 NUMERIC,
               valor_08 NUMERIC,
               valor_09 NUMERIC,
               valor_10 NUMERIC 
           ) AS $BODY$ DECLARE
           vSql VARCHAR;
       vPar1 VARCHAR := '';
       vPar2 VARCHAR := '';
       vPar3 VARCHAR = '';
       r record;
       vRelAgric BOOLEAN;
       
       BEGIN
       
           if pParSubTipoId = 'f4053f31-1832-4653-ac41-99c06edc3cac' then
                   vRelAgric = true;
           else
                   vRelAgric = false;
           end if;
               
           if pParCentro1Nome != '' then
           vPar1 = vPar1 || 'Centro 1 Nome [' || pParCentro1Nome || '] ' || chr(13) || chr(10);
           else
           vPar1 = vPar1 || 'Centro 1 Nome [] ' || chr(13) || chr(10);
           end if;
           
           if pParCentro1Ativo != '' then
           vPar1 = vPar1 || 'Centro 1 Ativo [' || pParCentro1Ativo || '] ' || chr(13) || chr(10);
           else
           vPar1 = vPar1 || 'Centro 1 Ativo [] ' || chr(13) || chr(10);
           end if;
           
           if pParCentro2Nome != '' then
            vPar1 = vPar1 || 'Centro 2 Nome [' || pParCentro2Nome || '] ' || chr(13) || chr(10);
           else
            vPar1 = vPar1 || 'Centro 2 Nome [] ' || chr(13) || chr(10);
           end if;
           
           if  pParCentro2Ativo != '' then
           vPar1 = vPar1|| 'Centro 2 Ativo [' || pParCentro2Ativo || '] ' || chr(13) || chr(10);
           
           else
           vPar1 = vPar1 || 'Centro 2 Ativo [] ' || chr(13) || chr(10);
           end if;
               
           if pParTipoSoloNome != '' then
           vPar1 = vPar1 ||'Nome Solo [' || pParTipoSoloNome || '] ' || chr(13) || chr(10);
           else
           vPar1 = vPar1 ||'Nome Solo [] ' || chr(13) || chr(10);
           end if;
           
           if pParUnidadeMedNome != '' then
           vPar1 = vPar1 || 'Nome Unidade Medida [' || pParUnidadeMedNome || '] ' || chr(13) || chr(10);
           else
           vPar1 = vPar1 || 'Nome Unidade Medida [] ' || chr(13) || chr(10);
           end if;
           
           if pParRatTipoNome != '' then
            vPar1 := vPar1 || 'Nome Tipo de Rateio [' || pParRatTipoNome || '] ' || chr(13) || chr(10);
           else
               vPar1 := vPar1 || 'Nome Tipo de Rateio [] ' || chr(13) || chr(10);
           end if;
           
           if pParTipoNome!= '' then
           vPar1 := vPar1 || 'Nome Centro Tipo [' || pParTipoNome || '] ' || chr(13) || chr(10);
           else
           vPar1 := vPar1 || 'Nome Centro Tipo [] ' || chr(13) || chr(10);
           end if;
               
           if pParSubTipoNome != '' then
           vPar1 := vPar1 || 'Nome Centro SubTipo [' || pParSubTipoNome || '] ' || chr(13) || chr(10);
           else
           vPar1 := vPar1|| 'Nome Centro SubTipo [] ' || chr(13) || chr(10);
           end if;
           
           if  pParEspacNome != '' then
               vPar1 := vPar1 || 'Nome Espaçamento [' || pParEspacNome || '] ' || chr(13) || chr(10);
           else
               vPar1 := vPar1|| 'Nome Espaçamento [] ' || chr(13) || chr(10);
           end if;
           
           if pParAtivSisPlanNome != '' then
           vPar1 := vPar1 || 'Nome Atividade Plantio [' || pParAtivSisPlanNome || '] ' || chr(13) || chr(10);
           else
           vPar1 := vPar1|| 'Nome Atividade Plantio [] ' || chr(13) || chr(10);
           end if;
           
           ------Param 2
           if pParAtivSisCultNome != '' then
           vPar2 = vPar2 || 'Nome Atividade Cultura [' || pParAtivSisCultNome || '] ' || chr(13) || chr(10);
           else
           vPar2 = vPar2 || 'Nome Atividade Cultura [] ' || chr(13) || chr(10);
           end if;
               
           if pParPeriodoNome  != ''  then
               vPar2 := vPar2  || 'Nome Periodo [' || pParPeriodoNome || '] ' || chr(13) || chr(10);
           else
               vPar2 := vPar2  || 'Nome Periodo [] ' || chr(13) || chr(10);
           end if;
           
       
           ---Param 3
           if pParPeriodoAtivo != '' then
               vPar2 = vPar2|| 'Periodo Ativo [' || pParPeriodoAtivo || '] ' || chr(13) || chr(10);
           else
               vPar2 = vPar2|| 'Periodo Ativo [] ' || chr(13) || chr(10);
           end if;
           
           if pParAtivSisColhNome != '' then
           vPar2 = vPar2|| 'Nome Atividade Colheita [' || pParAtivSisColhNome || '] ' || chr(13) || chr(10);
           else
           vPar2 = vPar2|| 'Nome Atividade Colheita [] ' || chr(13) || chr(10);
           end if;
           
           if pParItemServNome != '' then
           vPar2 = vPar2||'Nome Item de Serviço [' || pParItemServNome || '] ' || chr(13) || chr(10);
           else
           vPar2 = vPar2||'Nome Item de Serviço [] ' || chr(13) || chr(10);
           end if;
           
           if pParItemServAtivo!= '' then
           vPar2 = vPar2|| 'Item de Serviço Ativo [' || pParItemServAtivo || '] ' || chr(13) || chr(10);
           else
           vPar2 = vPar2|| 'Item de Serviço Ativo [] ' || chr(13) || chr(10);
           end if;
           
           if  pParGrupoNome != ''  then
           vPar2 = vPar2 || 'Nome Grupo [' || pParGrupoNome || '] ' || chr(13) || chr(10);
           else
           vPar2 = vPar2 || 'Nome Grupo [] ' || chr(13) || chr(10);
           end if;
           if pParGrupoAtivo != ''  then
           vPar2 = vPar2 || 'Ativo Grupo [' || pParGrupoAtivo || '] ' || chr(13) || chr(10);
           else
           vPar2 = vPar2 || 'Ativo Grupo [] ' || chr(13) || chr(10);
           end if;
           
           if pParSubGrupoNome != ''  then
               vPar2 = vPar2 || 'Nome SubGrupo [' || pParSubGrupoNome || '] ' || chr(13) || chr(10);
           else
               vPar2 = vPar2 || 'Nome SubGrupo [] ' || chr(13) || chr(10);
           end if;
           
           
           if pParBlocoCol != '' then
               vPar2 = vPar2  ||'Bloco de Colheita [' || pParBlocoCol || '] ' || chr(13) || chr(10);
           else
               vPar2 = vPar2  ||'Bloco de Colheita [] ' || chr(13) || chr(10);
           end if;
       
           --Param 4
           if pParLogUserIns != '' then
               vPar2 = vPar2 || 'Log Usuario Inserção [' ||pParLogUserIns|| '] ' || chr(13) || chr(10);
           else
               vPar2 = vPar2 || 'Log Usuario Inserção [] ' || chr(13) || chr(10);
           end if;
           
           if pParLogUserUpd != '' then
               vPar3 := vPar3 || 'Log Usuario Alteração [' ||pParLogUserUpd|| '] ' || chr(13) || chr(10);
           else
           vPar3 := vPar3 || 'Log Usuario Alteração [] ' || chr(13) || chr(10);
           end if;
       -- 	--------------------------------------------------------------------------------------------------
       
       -- Datas
       
           if pParDataIniPlan != '' and pParDataIniPlanFin != '' then
           vPar3 := vPar3 || 'Data Inicial do Plantio de [' || pParDataIniPlan || '] até [' || pParDataIniPlanFin || '] ' || chr(13) || chr(10);
        else
           vPar3 := vPar3 ||'Data Inicial do Plantio de [] até [] '|| chr(13) || chr(10);
        end if;
       
           if pParDataFinPlanIni != '' and pParDataFinPlan != '' then
           vPar3 := vPar3 || 'Data Final do Plantio de [' || pParDataFinPlanIni || '] até [' || pParDataFinPlan || '] ' || chr(13) || chr(10);
           else
           vPar3 := vPar3 || 'Data Final do Plantio de [] até [] ' || chr(13) || chr(10);
           end if;
           
           if pParDataUltPlanIni != '' and pParDataUltPlanFin != '' then
           vPar3 := vPar3 || 'Data Ultimo Plantio de [' || pParDataUltPlanIni || '] até' ||'['||pParDataUltPlanFin||']'|| chr(13) || chr(10);
           else 
           vPar3 := vPar3 || 'Data Ultimo Plantio de [] até []' || chr(13) || chr(10);
           end if;
           
           if pParDataIniCol != '' and pParDataIniColFin != '' then
           vPar3 := vPar3 || 'Data Inicial de Colheita de [' || pParDataIniCol || '] até [' || pParDataIniColFin || '] ' || chr(13) || chr(10);
           else
           vPar3 := vPar3 || 'Data Inicial de Colheita de [] até [] ' || chr(13) || chr(10);	
           end if;
           
           if pParDataFinCol != '' and pParDataFinColIni != '' then
           vPar3 := vPar3 || 'Data Final de Colheita de [' || pParDataFinCol || '] até [' || pParDataFinColIni || '] ' || chr(13) || chr(10);
       else
           vPar3 := vPar3 || 'Data Final de Colheita de [] até [] ' || chr(13) || chr(10);
       end if;
       
         if pParDataUltColIni != '' and pParDataUltColFin != '' then
           vPar3 := vPar3 || 'Data Ultima Colheita de [' || pParDataUltColIni || '] Até ' ||'[' || pParDataUltColFin||']'||  chr(13) || chr(10);
           else
           vPar3 := vPar3 || 'Data Ultima Colheita de [] até []' || chr(13) || chr(10);
         end if;
           
           if pParDataFloradaIni != '' and pParDataFloradaFin != '' then
           vPar3 := vPar3 || 'Data 1º Florada de [' || pParDataFloradaIni || '] até'||'['||pParDataFloradaFin||']'|| chr(13) || chr(10);
           else
           vPar3 := vPar3 || 'Data 1º Florada de [] até []' || chr(13) || chr(10);
           end if;
           
           if pParDataEmergIni != '' and pParDataEmergFin != '' then
           vPar3 := vPar3 || 'Data de Emergencia de [' || pParDataEmergIni || '] até' ||'['||pParDataEmergFin||']'|| chr(13) || chr(10);
           else
           vPar3 := vPar3 || 'Data de Emergencia de [] até []' || chr(13) || chr(10);
           end if;
           
           if pParPeriodoDataIni != '' and pParPeriodoDataFin != '' then
           vPar3 := vPar3 || 'Data Inicial Periodo de [' || pParPeriodoDataIni || '] até [' || pParPeriodoDataFin || '] ' || chr(13) || chr(10);
           else
           vPar3 := vPar3 || 'Data Inicial Periodo de [] até [] ' || chr(13) || chr(10);	
           end if;
           
           if pParLogDateInsIni != '' and pParLogDateInsFin != '' then
           vPar3 := vPar3 || 'Data Log Inserção de [' ||pParLogDateInsIni|| '] até ['||pParLogDateInsFin||']'|| chr(13) || chr(10);
           else
           vPar3 := vPar3 || 'Data Log Inserção de [] até []' || chr(13) || chr(10);
           end if;
           
           if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then
           vPar3 := vPar3 || 'Data Log Alteração de [' || pParLogDateUpdIni || '] até [' ||pParLogDateUpdFin||']'|| chr(13) || chr(10);
           else
           vPar3 := vPar3|| 'Data Log Alteração de [] até []' || chr(13) || chr(10);
           end if;
               
               
           vSql = 'select
           ' || pVart01 || '   as vart_01 ' || ',''' || pVard01 || ''' as vard_01 ';
           IF
               pVart02 != '' THEN
                   vSql = vSql || ',' || pVart02 || '   as vart_02 ' || ',''' || pVard02 || ''' as vard_02 ';
               ELSE vSql = vSql || ',null as vart_02' || ',null as vard_02';
               
           END IF;
           IF
               pVart03 != '' THEN
                   vSql = vSql || ',' || pVart03 || '   as vart_03 ' || ',''' || pVard03 || ''' as vard_03 ';
               ELSE vSql = vSql || ',null as vart_03' || ',null as vard_03';
               
           END IF;
           IF
               pVart04 != '' THEN
                   vSql = vSql || ',' || pVart04 || '   as vart_04 ' || ',''' || pVard04 || ''' as vard_04 ';
               ELSE vSql = vSql || ',null as vart_04' || ',null as vard_04';
               
           END IF;
           IF
               pVart05 != '' THEN
                   vSql = vSql || ',' || pVart05 || '   as vart_05 ' || ',''' || pVard05 || ''' as vard_05 ';
               ELSE vSql = vSql || ',null as vart_05' || ',null as vard_05';
               
           END IF;
           IF
               pVart06 != '' THEN
                   vSql = vSql || ',' || pVart06 || '   as vart_06 ' || ',''' || pVard06 || ''' as vard_06 ';
               ELSE vSql = vSql || ',null as vart_06' || ',null as vard_06';
               
           END IF;
           IF
               pVart07 != '' THEN
                   vSql = vSql || ',' || pVart07 || '   as vart_07 ' || ',''' || pVard07 || ''' as vard_07 ';
               ELSE vSql = vSql || ',null as vart_07' || ',null as vard_07';
               
           END IF;
           IF
               pVart08 != '' THEN
                   vSql = vSql || ',' || pVart08 || '   as vart_08 ' || ',''' || pVard08 || ''' as vard_08 ';
               ELSE vSql = vSql || ',null as vart_08' || ',null as vard_08';
               
           END IF;
           IF
               pVart09 != '' THEN
                   vSql = vSql || ',' || pVart09 || '   as vart_09 ' || ',''' || pVard09 || ''' as vard_09 ';
               ELSE vSql = vSql || ',null as vart_09' || ',null as vard_09';
               
           END IF;
           IF
               pVart10 != '' THEN
                   vSql = vSql || ',' || pVart09 || '   as vart_10 ' || ',''' || pVard09 || ''' as vard_10 ';
               ELSE vSql = vSql || ',null as vart_10' || ',null as vard_10 ';
               
           END IF;
           
           vSql = vSql || ',sum(t1.ope_centro2_area_qnt_area_prod) as valor_01,
           sum(t1.ope_centro2_area_qnt_area_improd) as valor_02,
           sum(t1.ope_centro2_area_qnt_plantas_estande) as valor_03
           from vwope_centro2_area t1 where 1=1 ';
           
       
           
           IF pParCentro2AreaId != '' THEN
                   vSql = vSql || ' and ' || ' t1.ope_centro2_area_id' || ' in(''' || pParCentro2AreaId || ''')';
           END IF;
           
           IF pParBlocoCol != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro2_area_bloco_col' || ' like ' || '''%' || pParBlocoCol || '%'' ';
           END IF;
           
           IF pParTipoSoloId != '' THEN
                   vSql = vSql || ' and ' || ' t1.ope_tipo_solo_id ' || ' in(''' || pParTipoSoloId ||''')';
           END IF;
           
           IF pParTipoSoloNome != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro2_area_tipo_solo_nome' || ' like ' || '''%' || pParTipoSoloNome || '%'' ';
           END IF;
           
           
               IF pParUnidadeMedId != '' THEN
                   vSql = vSql || ' and ' || ' t1.ope_centro2_area_umedida_id' || ' in(''' || pParUnidadeMedId || ''')';
           END IF;
           
           IF pParUnidadeMedNome != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro2_area_umedida_nome' || ' like ' || '''%' || pParUnidadeMedNome || '%'' ';
           END IF;
           
           IF pParTipoId != '' THEN
                   vSql = vSql || ' and ' || ' t1.ope_centro_tipo_id' || ' in(''' || pParTipoId || ''')';
           END IF;
           
           IF pParTipoNome != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro_tipo_nome' || ' like ' || '''%' || pParTipoNome || '%'' ';
           END IF;
           
           IF pParSubTipoId != '' THEN
                   vSql = vSql || ' and ' || ' t1.ope_centro_subtipo_id' || ' in(''' || pParSubTipoId || ''')';
           END IF;
           
           IF pParSubTipoNome != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro_subtipo_nome' || ' like ' || '''%' || pParSubTipoNome || '%'' ';
           END IF;	
           
           IF pParEspacId != '' THEN
                   vSql = vSql || ' and ' || ' t1.ope_centro2_area_espacamento_id' || ' in(''' || pParEspacId || ''')';
           END IF;
           
           IF pParEspacNome != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro2_area_espacamento_nome' || ' like ' || '''%' || pParEspacNome || '%'' ';
           END IF;
           
           IF pParAtivSisPlanId != '' THEN
                   vSql = vSql || ' and ' || ' t1.ope_centro2_area_atividade_sistema_plan_id' || ' in(''' || pParAtivSisPlanId || ''')';
           END IF;
           
           IF pParAtivSisPlanNome != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro2_area_atividade_sistema_plan_nome' || ' like ' || '''%' || pParAtivSisPlanNome || '%'' ';		
           END IF;
           
           IF pParAtivSisCultId != '' THEN
                   vSql = vSql || ' and ' || ' t1.ope_centro2_area_atividade_sistema_cult_id ' || ' in(''' || pParAtivSisCultId || ''')';
           END IF;
           
           IF pParAtivSisCultNome != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro2_area_atividade_sistema_cult_nome' || ' like ' || '''%' || pParAtivSisCultNome || '%'' ';
           END IF;
           
           IF pParAtivSisColhId != '' THEN
                   vSql = vSql || ' and ' || ' t1.ope_centro2_area_atividade_sistema_col_id ' || ' in(''' || pParAtivSisColhId || ''')';
           END IF;
           
           IF pParAtivSisColhNome != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro2_area_atividade_sistema_col_nome' || ' like ' || '''%' || pParAtivSisColhNome || '%'' ';
           END IF;
           
           IF pParItemServId != '' THEN
                   vSql = vSql || ' and ' || ' t1.ope_centro2_area_item_serv_id ' || ' in(''' || pParItemServId || ''')';
           END IF;
           
           IF pParItemServNome != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro2_area_item_serv_nome' || ' like ' || '''%' || pParItemServNome || '%'' ';
           END IF;
           
           IF pParItemServAtivo != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro2_area_item_serv_ativo_desc' || ' like ' || '''%' || pParItemServAtivo || '%'' ';
           END IF;
           
           -- Datas
       
           
           
           IF pParDataIniPlan != '' AND pParDataIniPlanFin != '' THEN
                   vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_ini_plan AS DATE)' || ' >= ''' || pParDataIniPlan || '''' || ' and  CAST(t1.ope_centro2_area_data_ini_plan AS DATE)' || ' <= ''' || pParDataIniPlanFin || '''';
           END IF;
           
           
           IF pParDataFinPlanIni != '' AND pParDataFinPlan != '' THEN
                   vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_fin_plan AS DATE)' || ' >= ''' || pParDataFinPlanIni || '''' || ' and  CAST(t1.ope_centro2_area_data_fin_plan AS DATE)' || ' <= ''' || pParDataFinPlan || '''';
           END IF;
           
           IF pParDataUltPlanIni != '' and pParDataUltPlanFin != '' THEN
                   vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_ult_plan AS DATE)' || ' >= ''' || pParDataUltPlanIni || '''' || ' and  CAST(t1.ope_centro2_area_data_ult_plan AS DATE)' || ' <= ''' || pParDataUltPlanFin || '''';
           END IF;
       
           IF pParDataIniCol != ''  AND pParDataIniColFin != '' THEN
                   vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_ini_col AS DATE)' || ' >= ''' || pParDataIniCol || '''' || ' and  CAST(t1.ope_centro2_area_data_ini_col AS DATE)' || ' <= ''' || pParDataIniColFin || '''';
           END IF;
           
           IF pParDataFinColIni != ''  AND pParDataFinCol != '' THEN
                   vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_fin_col AS DATE)' || ' >= ''' || pParDataFinColIni || '''' || ' and  CAST(t1.ope_centro2_area_data_fin_col AS DATE)' || ' <= ''' || pParDataFinCol || '''';
           END IF;
           
           IF pParDataUltColIni != '' and pParDataUltColFin != '' THEN			
            vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_ult_col AS DATE)' || ' >= ''' || pParDataUltColIni || '''' || ' and  CAST(t1.ope_centro2_area_data_ult_col AS DATE)' || ' <= ''' || pParDataUltColFin || '''';
         END IF;	
       
           
           IF pParDataFloradaIni != '' and pParDataFloradaFin != '' THEN
           vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_florada_1 AS DATE)' || ' >= ''' || pParDataFloradaIni || '''' || ' and  CAST(t1.ope_centro2_area_data_florada_1 AS DATE)' || ' <= ''' || pParDataFloradaFin || '''';
           
           END IF;
           
           IF pParDataEmergIni != '' and  pParDataEmergFin != '' THEN
                       vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_emerg AS DATE)' || ' >= ''' || pParDataEmergIni || '''' || ' and  CAST(t1.ope_centro2_area_data_emerg AS DATE)' || ' <= ''' || pParDataEmergFin || '''';
                       
           END IF;
           
           IF pParLogUserIns != '' THEN
                       vSql = vSql || ' and ' ||'t1.log_user_ins'||' like ' || '''%' ||pParLogUserIns|| '%'' ';
         END IF;				
       
           IF pParLogDateInsIni != '' and pParLogDateInsFin != '' THEN
            vSql = vSql || ' and ' || 'CAST(t1.log_date_ins AS DATE)' || ' >= ''' || pParLogDateInsIni || '''' || ' and  CAST(t1.log_date_ins AS DATE)' || ' <= ''' || pParLogDateInsFin || '''';
         END IF;	
           
           IF pParLogUserUpd != '' THEN
                       vSql = vSql || ' and ' ||'t1.log_user_upd'||' like ' || '''%' ||pParLogUserUpd|| '%'' ';
         END IF;				
       
           IF pParLogDateUpdIni != '' and  pParLogDateUpdFin != '' THEN
                     vSql = vSql || ' and ' || 'CAST(t1.log_date_upd AS DATE)' || ' >= ''' || pParLogDateUpdIni || '''' || ' and  CAST(t1.log_date_upd AS DATE)' || ' <= ''' || pParLogDateUpdFin || '''';
         END IF;				
       
       
       
       
           -- fim datas
           
           IF pParCentro1Id != '' THEN
                   vSql = vSql || ' and ' || ' t1.ope_centro1_id ' || ' in(''' || pParCentro1Id || ''')';
           END IF;
           
           IF pParCentro1Nome != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro1_nome' || ' like ' || '''%' || pParCentro1Nome || '%'' ';
           END IF;
           
           IF pParCentro1Ativo != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro1_ativo_desc' || ' like ' || '''%' || pParCentro1Ativo || '%'' ';
           END IF;
           
           IF pParCentro2Id != '' THEN
                   vSql = vSql || ' and ' || ' t1.ope_centro2_id ' || ' in(''' || pParCentro2Id || ''')';
           END IF;
           
           IF pParCentro2Nome != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro2_nome' || ' like ' || '''%' || pParCentro2Nome || '%'' ';
           END IF;
           
           IF pParCentro2Ativo != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro2_ativo_desc ' || ' like ' || '''%' || pParCentro2Ativo || '%'' ';
           END IF;
           
           IF pParGrupoId != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro_grupo_id ' || ' in(''' || pParGrupoId || ''')';
           END IF;
           
           IF pParGrupoNome != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro_grupo_nome' || ' like ' || '''%' || pParGrupoNome || '%'' ';
           END IF;
           
           IF pParGrupoAtivo != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro_grupo_ativo_desc' || ' like ' || '''%' || pParGrupoAtivo || '%'' ';
           END IF;
           
           IF pParSubGrupoId != '' THEN
                   vSql = vSql || ' and ' || ' t1.ope_centro_subgrupo_id' || ' in(''' || pParSubGrupoId || ''')';
           END IF;
           
           IF pParSubGrupoNome != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro_subgrupo_nome' || ' like ' || '''%' || pParSubGrupoNome || '%'' ';
           END IF;	
           
           
           IF pParRatTipoId != '' THEN
                   vSql = vSql || ' and ' || ' t1.ope_centro_rat_tipo_id' || ' in(''' || pParRatTipoId || ''')';
           END IF;
           
           IF pParRatTipoNome != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro_rat_tipo_nome' || ' like ' || '''%' || pParRatTipoNome || '%'' ';
           END IF;		
           
           IF pParPeriodoId != '' THEN
                   vSql = vSql || ' and ' || ' t1.ope_periodo_id ' || ' in(''' || pParPeriodoId || ''')';
           END IF;
           
           IF pParPeriodoNome != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_periodo_nome' || ' like ' || '''%' || pParPeriodoNome || '%'' ';
           END IF;
           
           IF pParPeriodoAtivo != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_periodo_ativo_desc' || ' like ' || '''%' || pParPeriodoAtivo || '%'' ';
           END IF;
           
           IF pParPeriodoDataIni != '' AND pParPeriodoDataFin != '' THEN
                   vSql = vSql || ' and ' || 'CAST(t1.ope_periodo_data_ini AS DATE)' || ' >= ''' || pParPeriodoDataIni || '''' || ' and  CAST(t1.ope_periodo_data_fin AS DATE)' || ' <= ''' || pParPeriodoDataFin || '''';
           END IF;
           
           if pParUnitId != '' then
               vSql = vSql|| ' and t1.ope_centro2_area_unit_id '||' in('''||pParUnitId||''')';
           end if;
           -- GROUP BY
           vSql = vSql || ' group by ' || pVart01;
           
           IF pVart02 != '' THEN
                   vSql = vSql || ',' || pVart02;
           END IF;
           
           IF pVart03 != '' THEN
                   vSql = vSql || ',' || pVart03;		
           END IF;
           
           IF pVart04 != '' THEN
                   vSql = vSql || ',' || pVart04;	
           END IF;
           
           IF pVart05 != '' THEN
                   vSql = vSql || ',' || pVart05;	
           END IF;
           
           IF pVart06 != '' THEN
                   vSql = vSql || ',' || pVart06;	
           END IF;
           
           IF pVart07 != '' THEN
                   vSql = vSql || ',' || pVart07;	
           END IF;
           
           IF pVart08 != '' THEN
                   vSql = vSql || ',' || pVart08;	
           END IF;
           
           IF pVart09 != '' THEN
                   vSql = vSql || ',' || pVart09;
           END IF;
           
           IF pVart10 != '' THEN
                   vSql = vSql || ',' || pVart10;	
           END IF;
           
       -- Order By
       -- ===================================
           vSql = vSql || ' order by ' || pVart01;
           IF pVart02 != '' THEN
                   vSql = vSql || ',' || pVart02;	
           END IF;
           
           IF pVart03 != '' THEN
                   vSql = vSql || ',' || pVart03;	
           END IF;
           
           IF pVart04 != '' THEN
                   vSql = vSql || ',' || pVart04;	
           END IF;
           
           IF pVart05 != '' THEN
                   vSql = vSql || ',' || pVart05;	
           END IF;
           
           IF pVart06 != '' THEN
                   vSql = vSql || ',' || pVart06;	
           END IF;
           
           IF pVart07 != '' THEN
                   vSql = vSql || ',' || pVart07;	
           END IF;
           
           IF pVart08 != '' THEN
                   vSql = vSql || ',' || pVart08;	
           END IF;
           
           IF pVart09 != '' THEN
                   vSql = vSql || ',' || pVart09;	
           END IF;
           
           IF pVart10 != '' THEN
                   vSql = vSql || ',' || pVart10;	
           END IF;
           
       -- 	raise notice'vSql :%', vSql;
           
           raise notice 'Param 2 :%',vPar2;
           raise notice 'Param 3 :%',vPar3;
           FOR r IN EXECUTE vSql loop
           
               ind_rel_id := pParIndRelId;
               ind_rel_par1 := vPar1;
               ind_rel_par2 := vPar2;
               ind_rel_par3 := vPar3;
               vart_01 := r.vart_01;
               vard_01 := r.vard_01;
               vart_02 := r.vart_02;
               vard_02 := r.vard_02;
               vart_03 := r.vart_03;
               vard_03 := r.vard_03;
               vart_04 := r.vart_04;
               vard_04 := r.vard_04;
               vart_05 := r.vart_05;
               vard_05 := r.vard_05;
               vart_06 := r.vart_06;
               vard_06 := r.vard_06;
               vart_07 := r.vart_07;
               vard_07 := r.vard_07;
               vart_08 := r.vart_08;
               vard_08 := r.vard_08;
               vart_09 := r.vart_09;
               vard_09 := r.vard_09;
               vart_10 := r.vart_10;
               vard_10 := r.vard_10;
               valor_01 := r.valor_01;
               valor_02 := r.valor_02;
               valor_03 := r.valor_03;
           RETURN NEXT;
           
       END loop;
       raise notice'vSql :%',vSql;
       RETURN;
       
       END;
       $BODY$ LANGUAGE plpgsql VOLATILE;;
       
       
       -----------
       
       

       drop FUNCTION if EXISTS fnreport0016;;

       CREATE OR REPLACE FUNCTION fnreport0016(
       pParUnitId VARCHAR,
       pParIndRelId VARCHAR,
       pVart01 VARCHAR,
       pVard01 VARCHAR,
       pVart02 VARCHAR DEFAULT NULL,
       pVard02 VARCHAR DEFAULT NULL,
       pVart03 VARCHAR DEFAULT NULL,
       pVard03 VARCHAR DEFAULT NULL,
       pVart04 VARCHAR DEFAULT NULL,
       pVard04 VARCHAR DEFAULT NULL,
       pVart05 VARCHAR DEFAULT NULL,
       pVard05 VARCHAR DEFAULT NULL,
       pVart06 VARCHAR DEFAULT NULL,
       pVard06 VARCHAR DEFAULT NULL,
       pVart07 VARCHAR DEFAULT NULL,
       pVard07 VARCHAR DEFAULT NULL,
       pVart08 VARCHAR DEFAULT NULL,
       pVard08 VARCHAR DEFAULT NULL,
       pVart09 VARCHAR DEFAULT NULL,
       pVard09 VARCHAR DEFAULT NULL,
       pVart10 VARCHAR DEFAULT NULL,
       pVard10 VARCHAR DEFAULT NULL,	
       pParEquipId VARCHAR DEFAULT NULL,	
       pParEquipTipoRodado VARCHAR DEFAULT NULL,	
       pParEquipTipoCarroceria VARCHAR DEFAULT NULL,	
       pParEquipCidId VARCHAR DEFAULT NULL,	
       pParEquipCidNome VARCHAR DEFAULT NULL,
       pParEquipCidAtivo VARCHAR DEFAULT NULL,	
       pParUfId VARCHAR DEFAULT NULL,	
       pParUfNome VARCHAR DEFAULT NULL,	
       pParEquipPlaca VARCHAR DEFAULT NULL,
       pParEquipRenavam VARCHAR DEFAULT NULL,
       pParEquipTara VARCHAR DEFAULT NULL,
       pParEquipCapacidKg VARCHAR DEFAULT NULL,
       pParEquipCapacidM3 VARCHAR DEFAULT NULL,
       pParEquipPotenc VARCHAR DEFAULT NULL,
       pParEquipNrChassi VARCHAR DEFAULT NULL,
       pParEquipNrSerie VARCHAR DEFAULT NULL,
       pParEquipLiberadoAbastec VARCHAR DEFAULT NULL,
       pParEquipLargura VARCHAR DEFAULT NULL,
       pParEquipAltur VARCHAR DEFAULT NULL,
       pParEquipNrRegEstadual VARCHAR DEFAULT NULL,
       pParEquipTipoTracao VARCHAR DEFAULT NULL,
       pParCentro1Id VARCHAR DEFAULT NULL,
       pParCentro1Nome VARCHAR DEFAULT NULL,
       pParCentro1Ativo VARCHAR DEFAULT NULL,
       pParCentro2Id VARCHAR DEFAULT NULL,
       pParCentro2Nome VARCHAR DEFAULT NULL,
       pParCentro2Ativo VARCHAR DEFAULT NULL,
       pParFrentTrabId VARCHAR DEFAULT NULL,
       pParFrentTrabNome VARCHAR DEFAULT NULL,
       pParFrentTrabAtivo VARCHAR DEFAULT NULL,
       pParMarcaModeloId VARCHAR DEFAULT NULL,
       pParMarcaModeloNome VARCHAR DEFAULT NULL,
       pParMarcaModeloAtivo VARCHAR DEFAULT NULL,
       pParMarcaId VARCHAR DEFAULT NULL,
       pParMarcaNome VARCHAR DEFAULT NULL,
       pParMarcaAtivo VARCHAR DEFAULT NULL,
       pParSubGrupId VARCHAR DEFAULT NULL,
       pParSubGrupoNome VARCHAR DEFAULT NULL,
       pParSubGrupoAtivo VARCHAR DEFAULT NULL,
       pParGrupoId VARCHAR DEFAULT NULL,
       pParGrupoNome VARCHAR DEFAULT NULL,
       pParGrupoAtivo VARCHAR DEFAULT NULL,
       pParProprietarioId VARCHAR DEFAULT NULL,
       pParProprietarioNome VARCHAR DEFAULT NULL,
       pParProprietarioAtivo VARCHAR DEFAULT NULL,
       pParProprietarioDoc VARCHAR DEFAULT NULL,
       pParLogUserIns VARCHAR DEFAULT NULL,
       
       pParLogDateInsIni VARCHAR DEFAULT NULL, 
       pParLogDateInsFin VARCHAR DEFAULT NULL, 
       
       pParLogUserUpd VARCHAR DEFAULT NULL,
       
       pParLogDateUpdIni VARCHAR DEFAULT NULL,
       pParLogDateUpdFin VARCHAR DEFAULT NULL		
       
       ) 
       RETURNS TABLE ( 
       ind_rel_id VARCHAR,
       ind_rel_par1 VARCHAR,
       ind_rel_par2 VARCHAR,
       ind_rel_par3 VARCHAR,
       ind_rel_par4 VARCHAR,
       vart_01 VARCHAR,
       vard_01 VARCHAR,
       vart_02 VARCHAR,
       vard_02 VARCHAR,
       vart_03 VARCHAR,
       vard_03 VARCHAR,
       vart_04 VARCHAR,
       vard_04 VARCHAR,
       vart_05 VARCHAR,
       vard_05 VARCHAR,
       vart_06 VARCHAR,
       vard_06 VARCHAR,
       vart_07 VARCHAR,
       vard_07 VARCHAR,
       vart_08 VARCHAR,
       vard_08 VARCHAR,
       vart_09 VARCHAR,
       vard_09 VARCHAR,
       vart_10 VARCHAR,
       vard_10 VARCHAR,
       valor_01 integer,
       valor_02 integer,
       valor_03 integer,
       valor_04 integer,
       valor_05 integer,
       valor_06 integer,
       valor_07 integer,
       valor_08 integer,
       valor_09 integer,
       valor_10 integer
       ) AS $BODY$ 
       DECLARE
       vSql text;
       vPar1 VARCHAR := '';
       vPar2 VARCHAR := '';
       vPar3 VARCHAR := '';
       vPar4 VARCHAR := '';
       r record;
       
       
       BEGIN
       
       -- Param 1
       if pParCentro1Nome != ''  then
       vPar1 := vPar1|| 'Nome Centro 1 [' ||pParCentro1Nome|| '] ' || chr(13) || chr(10);
       else
       vPar1 := vPar1|| 'Nome Centro 1 [] ' || chr(13) || chr(10);
       end if;
       
       if pParCentro1Ativo != ''  then
       vPar1 := vPar1|| 'Centro 1 Ativo [' ||pParCentro1Ativo|| '] ' || chr(13) || chr(10);
       else
       vPar1 := vPar1|| 'Centro 1 Ativo [] ' || chr(13) || chr(10);
       end if;
        
       if pParCentro2Nome != '' then
       vPar1 := vPar1|| 'Centro 2 Nome [' ||pParCentro2Nome|| '] ' || chr(13) || chr(10);
       else
       vPar1 := vPar1|| 'Centro 2 Nome [] ' || chr(13) || chr(10);
       end if;
       
       if pParCentro2Ativo != ''  then
       vPar1 := vPar1|| 'Centro 2 Ativo [' ||pParCentro2Ativo|| '] ' || chr(13) || chr(10);
       else
       vPar1 := vPar1|| 'Centro 2 Ativo [] ' || chr(13) || chr(10);
       end if;
        
        if pParEquipCidNome != ''  then
           vPar1 := vPar1 || 'Cidade Nome [' || pParEquipCidNome || '] ' || chr(13) || chr(10);
        else
           vPar1 := vPar1 || 'Cidade Nome [] ' || chr(13) || chr(10);
        end if;
        
           if pParUfNome != '' then
           vPar1 := vPar1 || 'Estado Nome [' || pParUfNome || '] ' || chr(13) || chr(10);
           else
           vPar1 := vPar1 || 'Estado Nome []' || chr(13) || chr(10);
           end if;
         
           if pParEquipCidAtivo != '' then
           vPar1 := vPar1 || 'Equipamento Ativo [' || pParEquipCidAtivo || '] ' || chr(13) || chr(10);
           else
           vPar1 := vPar1 || 'Equipamento Ativo []' || chr(13) || chr(10);
           end if;
           
           if pParEquipTipoRodado != '' then
               vPar1 := vPar1||'Tipo Rodadado [' || pParEquipTipoRodado || '] ' || chr(13) || chr(10);
           else 
               vPar1 := vPar1||'Tipo Rodadado [] ' || chr(13) || chr(10);
           end if;
       
           if pParEquipTipoCarroceria != '' then
               vPar1 := vPar1|| 'Tipo Carroceira [' || pParEquipTipoCarroceria || '] ' || chr(13) || chr(10);
           else
               vPar1 := vPar1|| 'Tipo Carroceira [] ' || chr(13) || chr(10);
           end if;
       
           if pParEquipPlaca != '' then
           vPar1 := vPar1 || 'Placa Equipamento [' ||pParEquipPlaca|| '] ' || chr(13) || chr(10);
           else
           vPar1 := vPar1 || 'Placa Equipamento []' || chr(13) || chr(10);
           end if;
       
           if pParEquipRenavam != '' then
           vPar1 := vPar1 || 'Reg Nacional de Veículos Automotores [' ||pParEquipRenavam|| '] ' || chr(13) || chr(10);
           else
           vPar1 := vPar1 || 'Reg Nacional de Veículos Automotores [] ' || chr(13) || chr(10);
           end if;
       
       -- Param 2
           if pParEquipTara != '' then
           vPar2 := vPar2 || 'Peso Veículo em Ordem de Marcha [' ||pParEquipTara|| '] ' || chr(13) || chr(10);
           else
           vPar2 := vPar2 || 'Peso Veículo em Ordem de Marcha []' || chr(13) || chr(10);
           end if;
       
           if pParEquipCapacidKg != '' then
           vPar2 := vPar2 || 'Capacidade Kg Equipamento [' ||pParEquipCapacidKg|| '] ' || chr(13) || chr(10);
           else
           vPar2 := vPar2 || 'Capacidade Kg Equipamento [] ' || chr(13) || chr(10);
           end if;
       
           if pParEquipCapacidKg != '' then
           vPar2 := vPar2 || 'Capacidade Kg Equipamento [' ||pParEquipCapacidKg|| '] ' || chr(13) || chr(10);
           else
           vPar2 := vPar2 || 'Capacidade Kg Equipamento []' || chr(13) || chr(10);
           end if;
       
           if pParEquipCapacidM3 != '' then
           vPar2 := vPar2 || 'Capacidade M3 Equipamento [' ||pParEquipCapacidM3|| '] ' || chr(13) || chr(10);
           else
           vPar2 := vPar2 || 'Capacidade M3 Equipamento []' || chr(13) || chr(10);
           end if;
       
           if pParEquipPotenc != '' then
           vPar2 := vPar2|| 'Potência do Equipamento [' ||pParEquipPotenc|| '] ' || chr(13) || chr(10);
           else
           vPar2 := vPar2 || 'Potência do Equipamento []' || chr(13) || chr(10);
           end if;
       
           if pParEquipNrChassi != '' then
           vPar2 := vPar2 || 'Nº Chassi do Equipamento [' ||pParEquipNrChassi|| '] ' || chr(13) || chr(10);
           else
           vPar2 := vPar2 || 'Nº Chassi do Equipamento []' || chr(13) || chr(10);
           end if;
       
           if pParEquipNrSerie != '' then
           vPar2 := vPar2 || 'Nº Série  do Equipamento [' ||pParEquipNrSerie|| '] ' || chr(13) || chr(10);
           else
           vPar2 := vPar2 || 'Nº Série  do Equipamento [] ' || chr(13) || chr(10);
           end if;
           
           if pParEquipNrRegEstadual != '' then
           vPar2 := vPar2|| 'Nº Registro Estadual do Equipamento [' ||pParEquipNrRegEstadual|| '] ' || chr(13) || chr(10);
           else
           vPar2 := vPar2|| 'Nº Registro Estadual do Equipamento [] ' || chr(13) || chr(10);
           end if;
       
           if pParEquipLiberadoAbastec != '' then
           vPar3 := vPar3|| 'Equipamento Liberado para Abastecimento [' ||pParEquipLiberadoAbastec|| '] ' || chr(13) || chr(10);
           else
           vPar2 := vPar2|| 'Equipamento Liberado para Abastecimento []' || chr(13) || chr(10);
           end if;
       
       -- Param 3
           if pParEquipLargura != '' then
           vPar3 := vPar3|| 'Largura do Equipamento [' ||pParEquipLargura|| '] ' || chr(13) || chr(10);
           else
           vPar3 := vPar3|| 'Largura do Equipamento []' || chr(13) || chr(10);
           end if;
       
           if pParEquipAltur != '' then
           vPar3 := vPar3|| 'Altura do Equipamento [' ||pParEquipAltur|| '] ' || chr(13) || chr(10);
           else
           vPar3 := vPar3|| 'Altura do Equipamento [] ' || chr(13) || chr(10);
           end if;
       
           if pParEquipTipoTracao != '' then
           vPar3 := vPar3|| 'Tipo de Tração Equipamento [' ||pParEquipTipoTracao|| '] ' || chr(13) || chr(10);
           else
           vPar3 := vPar3|| 'Tipo de Tração Equipamento [] ' || chr(13) || chr(10);
           end if;
        
        if pParFrentTrabNome != '' then
           vPar3 := vPar3|| 'Nome Frente de Trabalho [' ||pParFrentTrabNome|| '] ' || chr(13) || chr(10);
        else
           vPar3 := vPar3|| 'Nome Frente de Trabalho [] ' || chr(13) || chr(10);
        end if;
       
           if pParFrentTrabAtivo != ''  then
           vPar3 := vPar3|| 'Frente de Trabalho Ativo [' ||pParFrentTrabAtivo|| '] ' || chr(13) || chr(10);
           else
           vPar3 := vPar3|| 'Frente de Trabalho Ativo [] ' || chr(13) || chr(10);
           end if;
        
           if pParMarcaModeloNome != '' then
               vPar3 := vPar3|| 'Modelo Nome [' ||pParMarcaModeloNome|| '] ' || chr(13) || chr(10);
           else
               vPar3 := vPar3|| 'Modelo Nome []' || chr(13) || chr(10);
           end if;
       
           if pParMarcaModeloAtivo != '' then
           vPar3 := vPar3|| 'Modelo Ativo [' ||pParMarcaModeloAtivo|| '] ' || chr(13) || chr(10);
           else
           vPar3 := vPar3|| 'Modelo Ativo [] ' || chr(13) || chr(10);
           end if;
       
       
            if pParMarcaNome!= '' then
           vPar3 := vPar3|| 'Nome Marca [' ||pParMarcaNome|| '] ' || chr(13) || chr(10);
           else
           vPar3 := vPar3|| 'Nome Marca [] ' || chr(13) || chr(10);
           end if;
       
           if pParMarcaAtivo != '' then
           vPar3 := vPar3|| 'Ativo Marca [' ||pParMarcaAtivo|| '] ' || chr(13) || chr(10);
           else
           vPar3 := vPar3|| 'Ativo Marca [] ' || chr(13) || chr(10);
           end if;
       -- Param 4
       
         if pParGrupoNome != '' then
               vPar4 := vPar4|| 'Grupo Nome [' ||pParGrupoNome|| '] ' || chr(13) || chr(10);
           else
               vPar4 := vPar4|| 'Grupo Nome [] ' || chr(13) || chr(10);
           end if;
       
           if pParGrupoAtivo != ''  then
           vPar4 := vPar4|| 'Grupo Ativo [' ||pParGrupoAtivo|| '] ' || chr(13) || chr(10);
           else
           vPar4 := vPar4|| 'Grupo Ativo [] ' || chr(13) || chr(10);
           end if;
       
           if pParSubGrupoNome != '' then
           vPar4 := vPar4|| 'Nome SubGrupo [' ||pParSubGrupoNome|| '] ' || chr(13) || chr(10);
           else
           vPar4 := vPar4|| 'Nome SubGrupo [] ' || chr(13) || chr(10);
           end if;
       
           if pParSubGrupoAtivo != '' then
           vPar4 := vPar4|| 'SubGrupo Ativo [' ||pParSubGrupoAtivo|| '] ' || chr(13) || chr(10);
           else
           vPar4 := vPar4|| 'SubGrupo Ativo [] ' || chr(13) || chr(10);
           end if;
       
        if pParProprietarioNome != '' then
           vPar4 := vPar4|| 'Nome do Proprietario [' ||pParProprietarioNome|| '] ' || chr(13) || chr(10);
        else
           vPar4 := vPar4|| 'Nome do Proprietario [] ' || chr(13) || chr(10);
        end if;
       
           if pParProprietarioAtivo != '' then
           vPar4 := vPar4|| 'Proprietário Ativo [' ||pParProprietarioAtivo|| '] ' || chr(13) || chr(10);
           else
           vPar4 := vPar4|| 'Proprietário Ativo []' || chr(13) || chr(10);
           end if;
       
           if pParProprietarioDoc != '' then
           vPar4 := vPar4|| 'Documento Proprietário [' ||pParProprietarioDoc|| '] ' || chr(13) || chr(10);
           else
           vPar4 := vPar4|| 'Documento Proprietário [] ' || chr(13) || chr(10);
           end if;
       
       -- Param 3
           if pParLogUserIns != '' then
               vPar4 := vPar4 || 'Log Usuario Inserção [' ||pParLogUserIns|| '] ' || chr(13) || chr(10);
           else 
               vPar4 := vPar4 || 'Log Usuario Inserção []' || chr(13) || chr(10);
           end if;
           
           if pParLogUserUpd != ''  then
               vPar4 := vPar4 || 'Log Usuario Alteração [' ||pParLogUserUpd|| '] ' || chr(13) || chr(10);
           else 
               vPar4 := vPar4 || 'Log Usuario Alteração [] ' || chr(13) || chr(10);
           end if;
           
           if pParLogDateInsIni != '' and pParLogDateInsFin != '' then
           vPar4 := vPar4 || 'Log Data Inserção de [' ||pParLogDateInsIni|| '] até ['||pParLogDateInsFin||']'|| chr(13) || chr(10);
           else
           vPar4 := vPar4 || 'Log Data Inserção de [] até []' || chr(13) || chr(10);
           end if;
           
           if pParLogDateUpdIni != '' and pParLogDateUpdIni != '' then
           vPar4 := vPar4 || 'Log Data Alteração de [' || pParLogDateUpdIni || '] até [' ||pParLogDateUpdFin||']'|| chr(13) || chr(10);
           else
           vPar4 := vPar4 || 'Log Data Alteração de [] até []' || chr(13) || chr(10);
           end if;
           
       
       vSql = 'select
           ' || pVart01 || '   as vart_01 ' || ',''' || pVard01 || ''' as vard_01 ';
           
           IF pVart02 != '' THEN
                   vSql = vSql || ',' || pVart02 || '   as vart_02 ' || ',''' || pVard02 || ''' as vard_02 ';
               ELSE
               vSql = vSql || ',null as vart_02' || ',null as vard_02';	
           END IF;
           IF pVart03 != '' THEN
                   vSql = vSql || ',' || pVart03 || '   as vart_03 ' || ',''' || pVard03 || ''' as vard_03 ';
           ELSE 	
               vSql = vSql || ',null as vart_03' || ',null as vard_03';
           END IF;
           IF pVart04 != '' THEN
                   vSql = vSql || ',' || pVart04 || '   as vart_04 ' || ',''' || pVard04 || ''' as vard_04 ';
           ELSE
           vSql = vSql || ',null as vart_04' || ',null as vard_04';
           END IF;
           
           IF pVart05 != '' THEN
                   vSql = vSql || ',' || pVart05 || '   as vart_05 ' || ',''' || pVard05 || ''' as vard_05 ';
           ELSE 	
               vSql = vSql || ',null as vart_05' || ',null as vard_05';
           END IF;
           
           IF pVart06 != '' THEN
               vSql = vSql || ',' || pVart06 || '   as vart_06 ' || ',''' || pVard06 || ''' as vard_06 ';
           ELSE 
               vSql = vSql || ',null as vart_06' || ',null as vard_06';	
           END IF;
           
           IF pVart07 != '' THEN
                   vSql = vSql || ',' || pVart07 || '   as vart_07 ' || ',''' || pVard07 || ''' as vard_07 ';
           ELSE
               vSql = vSql || ',null as vart_07' || ',null as vard_07';	
           END IF;
           
           IF pVart08 != '' THEN
                   vSql = vSql || ',' || pVart08 || '   as vart_08 ' || ',''' || pVard08 || ''' as vard_08 ';
           ELSE 
               vSql = vSql || ',null as vart_08' || ',null as vard_08';	
           END IF;
           
           IF pVart09 != '' THEN
                   vSql = vSql || ',' || pVart09 || '   as vart_09 ' || ',''' || pVard09 || ''' as vard_09 ';
           ELSE 
           vSql = vSql || ',null as vart_09' || ',null as vard_09';	
           END IF;
           
           IF pVart10 != '' THEN
                   vSql = vSql || ',' || pVart09 || '   as vart_10 ' || ',''' || pVard09 || ''' as vard_10 ';
           ELSE 
               vSql = vSql || ',null as vart_10' || ',null as vard_10 ';
           END IF;
           
       -- 	vSql = vSql ||',
       -- 				count(1) as valor_01
       -- 				t1.ope_centro2_sigla as valor_02,
       -- 				t1.ope_centro2_ativo_desc as valor_03,
       -- 				t1.ope_frente_trabalho_nome as valor_04,
       -- 				t1.ope_frente_trabalho_sigla as valor_05,
       -- 				t1.ope_frente_trabalho_ativo_desc as valor_06,
       -- 				t1.ger_marca_modelo_nome as valor_07,
       -- 				t1.ger_marca_nome as valor_08,
       -- 				t1.ope_centro_grupo_nome as valor_09,
       -- 				t1.ger_pessoa_proprietario_nome as valor_10
       -- 				from vwope_centro2_equip t1 where 1=1';
       
           vSql = vSql ||',
                       count(1) as valor_01
                       from vwope_centro2_equip t1 where 1=1';
                       
                       
           IF pParEquipId != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro2_equip_id' || ' in(''' ||pParEquipId||''')';
           END IF;
           
           IF pParEquipTipoRodado != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro2_equip_tipo_rodado_desc' || ' like ' || '''%' || pParEquipTipoRodado || '%'' ';
           END IF;
           
           IF pParEquipTipoCarroceria != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro2_equip_tipo_carroceria_desc' || ' like ' || '''%' || pParEquipTipoCarroceria || '%'' ';
           END IF;
       
           IF pParEquipCidId != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro2_equip_cidade_id' || ' in(''' ||pParEquipCidId||''')';
           END IF;
       
           IF pParEquipCidNome != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro2_equip_cidade_nome' || ' like ' || '''%' || pParEquipCidNome || '%'' ';
           END IF;
           
           IF pParEquipCidAtivo != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro2_equip_cidade_ativo_desc' || ' like ' || '''%' || pParEquipCidAtivo || '%'' ';
           END IF;
           
           IF pParUfId != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro2_uf_id' || ' in(''' ||pParUfId||''')';
           END IF;
           
           IF pParUfNome != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro2_uf_nome' || ' like ' || '''%' || pParUfNome || '%'' ';
           END IF;
           
           IF pParEquipPlaca != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro2_equip_placa' || ' like ' || '''%' || pParEquipPlaca || '%'' ';
           END IF;
           
           IF pParEquipRenavam != '' THEN
               vSql = vSql || ' and ' || 't1.ope_centro2_equip_renavam' || ' like ' || '''%' || pParEquipRenavam || '%'' ';
           END IF;
       
       IF pParEquipTara != '' THEN
             vSql = vSql || ' and ' || 't1.ope_centro2_equip_tara' || ' = ' || '''' || pParEquipTara || ''' ';
       END IF;
       
           IF pParEquipCapacidKg != '' THEN
                   vSql = vSql || ' and ' || 't1.ope_centro2_equip_capacidade_kg' || ' = ' || '''' ||pParEquipCapacidKg|| ''' ';
           END IF;
           
           IF pParEquipCapacidM3 != '' THEN
                   vSql = vSql || ' and ' ||'t1.ope_centro2_equip_capacidade_m3'|| ' = ' || '''' ||pParEquipCapacidM3|| ''' ';
           END IF;
           
           IF pParEquipPotenc != '' THEN
                   vSql = vSql || ' and ' ||'t1.ope_centro2_equip_potencia'|| ' = ' || '''' ||pParEquipPotenc|| ''' ';
           END IF;
           
           IF pParEquipNrChassi != '' THEN
                   vSql = vSql || ' and ' ||'t1.ope_centro2_equip_nr_chassi'|| ' = ' || '''' ||pParEquipNrChassi|| ''' ';
           END IF;
           
           IF pParEquipNrSerie != '' THEN
                   vSql = vSql || ' and ' ||'t1.ope_centro2_equip_nr_serie'|| ' = ' || '''' ||pParEquipNrSerie|| ''' ';
           END IF;
           
           IF pParEquipLiberadoAbastec != '' THEN
                   vSql = vSql || ' and ' ||'t1.ope_centro2_equip_liberado_abastec'|| ' like ' || '''%' ||pParEquipLiberadoAbastec|| '%'' ';
           END IF;
       
           IF pParEquipLargura != '' THEN
                   vSql = vSql || ' and ' ||'t1.ope_centro2_equip_largura'|| ' = ' || '''' ||pParEquipLargura|| ''' ';
           END IF;
           
           IF pParEquipAltur != '' THEN
                   vSql = vSql || ' and ' ||'t1.ope_centro2_equip_altura'|| ' = ' || '''' ||pParEquipAltur|| ''' ';
           END IF;
           
           IF pParEquipNrRegEstadual != '' THEN
                   vSql = vSql || ' and ' ||'t1.ope_centro2_equip_nr_registro_estadual'|| ' = ' || '''' ||pParEquipNrRegEstadual|| ''' ';
           END IF;
           
           IF pParEquipTipoTracao != '' THEN
                   vSql = vSql || ' and ' ||'t1.ope_centro2_equip_tipo_tracao'|| ' = ' || '''' ||pParEquipTipoTracao|| ''' ';
        END IF;
        
        
           IF pParCentro1Id != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro1_id' || ' in(''' ||pParCentro1Id||''')';
           END IF;
           
           IF pParCentro1Nome != '' THEN
                   vSql = vSql || ' and ' ||'t1.ope_centro1_nome'||' like ' || '''%' ||pParCentro1Nome|| '%'' ';
         END IF;
           
           IF pParCentro1Ativo != '' THEN
                   vSql = vSql || ' and ' ||'t1.ope_centro1_ativo_desc'||' like ' || '''%' ||pParCentro1Ativo|| '%'' ';
         END IF;
           
           IF pParCentro2Id != '' THEN
                       vSql = vSql || 'and ' || ' t1.ope_centro2_id' || ' in(''' ||pParCentro2Id||''')';
         END IF;
           
           IF pParCentro2Nome != '' THEN
                   vSql = vSql || ' and ' ||'t1.ope_centro2_nome'||' like ' || '''%' ||pParCentro2Nome|| '%'' ';
         END IF;
           
           IF pParCentro2Ativo != '' THEN
                   vSql = vSql || ' and ' ||'t1.ope_centro2_ativo_desc'||' like ' || '''%' ||pParCentro2Ativo|| '%'' ';
         END IF;
           
           IF pParFrentTrabId != '' THEN
                       vSql = vSql || 'and ' || ' t1.ope_frente_trabalho_id' || ' in(''' ||pParFrentTrabId||''')';
         END IF;	
           
           IF pParFrentTrabNome != '' THEN
                   vSql = vSql || ' and ' ||'t1.ope_frente_trabalho_nome'||' like ' || '''%' ||pParFrentTrabNome|| '%'' ';
         END IF;
           
           IF pParFrentTrabAtivo != '' THEN
                   vSql = vSql || ' and ' ||'t1.ope_frente_trabalho_ativo_desc'||' like ' || '''%' ||pParFrentTrabAtivo|| '%'' ';
         END IF;
       
           IF pParMarcaModeloId != '' THEN
                       vSql = vSql || 'and ' || ' t1.ger_marca_modelo_id' || ' in(''' ||pParMarcaModeloId||''')';
         END IF;	
           
           IF pParMarcaModeloNome != '' THEN
                   vSql = vSql || ' and ' ||'t1.ger_marca_modelo_nome'||' like ' || '''%' ||pParMarcaModeloNome|| '%'' ';
         END IF;	
           
           IF pParMarcaModeloAtivo != '' THEN
                   vSql = vSql || ' and ' ||'t1.ger_marca_modelo_ativo_desc'||' like ' || '''%' ||pParMarcaModeloAtivo|| '%'' ';
           END IF;	
           
           IF pParMarcaId != '' THEN
                       vSql = vSql || 'and ' || ' t1.ger_marca_id' || ' in(''' ||pParMarcaId||''')';
         END IF;	
           
           IF pParMarcaNome != '' THEN
                   vSql = vSql || ' and ' ||'t1.ger_marca_nome'||' like ' || '''%' ||pParMarcaNome|| '%'' ';
         END IF;		
           
           IF pParMarcaAtivo != '' THEN
                   vSql = vSql || ' and ' ||'t1.ger_marca_ativo_desc'||' like ' || '''%' ||pParMarcaAtivo|| '%'' ';
         END IF;	
               
           IF pParSubGrupId != '' THEN
                       vSql = vSql || 'and ' || ' t1.ope_centro_subgrupo_id' || ' in(''' ||pParSubGrupId||''')';
         END IF;	
           
           IF pParSubGrupoNome != '' THEN
                   vSql = vSql || ' and ' ||'t1.ope_centro_subgrupo_nome'||' like ' || '''%' ||pParSubGrupoNome|| '%'' ';
         END IF;		
           
           IF pParSubGrupoAtivo != '' THEN
                   vSql = vSql || ' and ' ||'t1.ope_centro_subgrupo_ativo_desc'||' like ' || '''%' ||pParSubGrupoAtivo|| '%'' ';
         END IF;
               
           IF pParGrupoId != '' THEN
                       vSql = vSql || 'and ' || ' t1.ope_centro_grupo_id' || ' in(''' ||pParGrupoId||''')';
         END IF;		
           
           IF pParGrupoNome != '' THEN
                       vSql = vSql || ' and ' ||'t1.ope_centro_grupo_nome'||' like ' || '''%' ||pParGrupoNome|| '%'' ';
         END IF;		
           
           IF pParGrupoAtivo != '' THEN
                       vSql = vSql || ' and ' ||'t1.ope_centro_grupo_ativo_desc'||' like ' || '''%' ||pParGrupoAtivo|| '%'' ';
         END IF;		
           
           IF pParProprietarioId != '' THEN
                       vSql = vSql || 'and ' || ' t1.ger_pessoa_proprietario_id' || ' in(''' ||pParProprietarioId||''')';
         END IF;
           
           IF pParProprietarioNome != '' THEN
                       vSql = vSql || ' and ' ||'t1.ger_pessoa_proprietario_nome'||' like ' || '''%' ||pParProprietarioNome|| '%'' ';
         END IF;		
           
           IF pParProprietarioAtivo != '' THEN
                       vSql = vSql || ' and ' ||'t1.ger_pessoa_proprietario_ativo_desc'||' like ' || '''%' ||pParProprietarioAtivo|| '%'' ';
         END IF;			
       
           IF pParProprietarioDoc != '' THEN
                       vSql = vSql || ' and ' ||'t1.ger_pessoa_proprietario_doc_cpf_cnpj_desc'||' like ' || '''%' ||pParProprietarioDoc|| '%'' ';
         END IF;			
           
           IF pParLogUserIns != '' THEN
                       vSql = vSql || ' and ' ||'t1.log_user_ins'||' like ' || '''%' ||pParLogUserIns|| '%'' ';
         END IF;				
       
           IF pParLogDateInsIni != '' and pParLogDateInsFin != '' THEN
            vSql = vSql || ' and ' || 'CAST(t1.log_date_ins AS DATE)' || ' >= ''' || pParLogDateInsIni || '''' || ' and  CAST(t1.log_date_ins AS DATE)' || ' <= ''' || pParLogDateInsFin || '''';
         END IF;	
           
           IF pParLogUserUpd != '' THEN
                       vSql = vSql || ' and ' ||'t1.log_user_upd'||' like ' || '''%' ||pParLogUserUpd|| '%'' ';
         END IF;				
       
           IF pParLogDateUpdIni != '' and  pParLogDateUpdFin != '' THEN
                     vSql = vSql || ' and ' || 'CAST(t1.log_date_upd AS DATE)' || ' >= ''' || pParLogDateUpdIni || '''' || ' and  CAST(t1.log_date_upd AS DATE)' || ' <= ''' || pParLogDateUpdFin || '''';
         END IF;				
       
       
           
       -- GROUP BY
       -- 	vSql = vSql || ' group by valor_01,valor_02,valor_03,valor_04,valor_05,valor_06,valor_07,valor_08,valor_09,valor_10,' || pVart01;
       
       vSql = vSql || ' group by ' || pVart01;
           
           IF pVart02 != '' THEN
                   vSql = vSql || ',' || pVart02;
           END IF;
           
           IF pVart03 != '' THEN
                   vSql = vSql || ',' || pVart03;		
           END IF;
           
           IF pVart04 != '' THEN
                   vSql = vSql || ',' || pVart04;	
           END IF;
           
           IF pVart05 != '' THEN
                   vSql = vSql || ',' || pVart05;	
           END IF;
           
           IF pVart06 != '' THEN
                   vSql = vSql || ',' || pVart06;	
           END IF;
           
           IF pVart07 != '' THEN
                   vSql = vSql || ',' || pVart07;	
           END IF;
           
           IF pVart08 != '' THEN
                   vSql = vSql || ',' || pVart08;	
           END IF;
           
           IF pVart09 != '' THEN
                   vSql = vSql || ',' || pVart09;
           END IF;
           
           IF pVart10 != '' THEN
                   vSql = vSql || ',' || pVart10;	
           END IF;
           
       -- Order By
       -- ===================================
           vSql = vSql || ' order by ' || pVart01;
           IF pVart02 != '' THEN
                   vSql = vSql || ',' || pVart02;	
           END IF;
           
           IF pVart03 != '' THEN
                   vSql = vSql || ',' || pVart03;	
           END IF;
           
           IF pVart04 != '' THEN
                   vSql = vSql || ',' || pVart04;	
           END IF;
           
           IF pVart05 != '' THEN
                   vSql = vSql || ',' || pVart05;	
           END IF;
           
           IF pVart06 != '' THEN
                   vSql = vSql || ',' || pVart06;	
           END IF;
           
           IF pVart07 != '' THEN
                   vSql = vSql || ',' || pVart07;	
           END IF;
           
           IF pVart08 != '' THEN
                   vSql = vSql || ',' || pVart08;	
           END IF;
           
           IF pVart09 != '' THEN
                   vSql = vSql || ',' || pVart09;	
           END IF;
           
           IF pVart10 != '' THEN
                   vSql = vSql || ',' || pVart10;	
           END IF;
           
           raise notice'vSql :%', vSql;
           
               FOR r IN EXECUTE vSql loop
           
               ind_rel_id := pParIndRelId;
               ind_rel_par1 := vPar1;
               ind_rel_par2 := vPar2;
               ind_rel_par3 := vPar3;
               ind_rel_par4 := vPar4;
               vart_01 := r.vart_01;
               vard_01 := r.vard_01;
               vart_02 := r.vart_02;
               vard_02 := r.vard_02;
               vart_03 := r.vart_03;
               vard_03 := r.vard_03;
               vart_04 := r.vart_04;
               vard_04 := r.vard_04;
               vart_05 := r.vart_05;
               vard_05 := r.vard_05;
               vart_06 := r.vart_06;
               vard_06 := r.vard_06;
               vart_07 := r.vart_07;
               vard_07 := r.vard_07;
               vart_08 := r.vart_08;
               vard_08 := r.vard_08;
               vart_09 := r.vart_09;
               vard_09 := r.vard_09;
               vart_10 := r.vart_10;
               vard_10 := r.vard_10;
               valor_01 := r.valor_01;
       -- 		valor_02 := r.valor_02;
       -- 		valor_03 := r.valor_03;
       -- 		valor_04 := r.valor_04;
       -- 		valor_05 := r.valor_05;
       -- 		valor_06 := r.valor_06;
       -- 		valor_07 := r.valor_07;
       -- 		valor_07 := r.valor_07;
       -- 		valor_08 := r.valor_08;
       -- 		valor_09 := r.valor_09;
       -- 		valor_10 := r.valor_10;
               
           RETURN NEXT;
           
       END loop;
       raise notice'vSql :%',vSql;
       
       END;
       $BODY$ LANGUAGE plpgsql VOLATILE;;
       
       
       -----------
       
       

       Drop FUNCTION IF EXISTS fnreport0017;;

       CREATE OR REPLACE FUNCTION fnreport0017(
       pParUnitId varchar, 
       pParIndRelId varchar, 
       pVart01 varchar, 
       pVard01 varchar, 
       pVart02 varchar default null,
       pVard02 varchar default null,
       pVart03 varchar default null,
       pVard03 varchar default null,
       pVart04 varchar default null,
       pVard04 varchar default null,
       pVart05 varchar default null,
       pVard05 varchar default null,
       pParPessoaPtoIdenfTipo varchar default null,
       pParPessoaPtoIdenf varchar default null,
       pParCentro1Id varchar default null,
       pParCentro1Nome varchar default null,
       pParCentro1Ativo varchar default null,
       pParCentroSubTipoId varchar default null,
       pParCentroSubTipoNome varchar default null,
       pParCentro2Id varchar default null,
       pParCentro2Sigla varchar default null,
       pParCentro2Nome varchar default null,
       pParCentro2Ativo varchar default null,
       pParFrenteTrabalhoId varchar default null,
       pParFrenteTrabalhoNome varchar default null,
       pParFrenteTrabalhoSigla varchar default null,
       pParFrenteTrabalhoAtivo varchar default null,
       pParLogUserIns varchar default null,
       pParLogDateInsIni varchar default null,
       pParLogDateInsFin varchar default null,
       pParLogUserUpd varchar default null,
       pParLogDateUpdIni varchar default null,
       pParLogDateUpdFin varchar default null
       
       )
       RETURNS TABLE(
        ind_rel_id varchar,
        ind_rel_par1 varchar,
        ind_rel_par2 varchar,
        ind_rel_par3 varchar,
        vart_01 varchar,
        vard_01 varchar,
        vart_02 varchar,
        vard_02 varchar,
        vart_03 varchar,
        vard_03 varchar,
        vart_04 varchar,
        vard_04 varchar,
        vart_05 varchar,
        vard_05 varchar,
        valor_01 numeric,
        valor_02 numeric,
        valor_03 numeric,
        valor_04 numeric,
        valor_05 numeric,
        valor_06 numeric,
        valor_07 numeric,
        valor_08 numeric,
        valor_09 numeric,
        valor_10 numeric) AS $BODY$
       declare
       vSql varchar;
       vPar1 varchar :='';
       vPar2 varchar :='';
       vPar3 varchar :='';
       r record;
       
       begin
           
           if pParPessoaPtoIdenfTipo != '' then
               vPar1 := vPar1||'Tipo de Indenficação do Ponto ['||pParPessoaPtoIdenfTipo||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Tipo de Indenficação do Ponto []'||chr(13)||chr(10);
           end if;
           
           if pParPessoaPtoIdenf != '' then
               vPar1 := vPar1||'Indenficação Ponto ['||pParPessoaPtoIdenf||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Indenficação Ponto []'||chr(13)||chr(10);
           end if;
           
           if pParCentro1Id != '' then
                   vPar1 := vPar1||'Centro 1 ['||fnreport_sigla(pParUnitId,'ope_centro1','sigla_centro1','id',''''||pParCentro1Id||'''')||'] '||chr(13)||chr(10);
           else
                   vPar1 := vPar1||'Centro 1 []'||chr(13)||chr(10);
           end if;
           
           if pParCentro1Nome != '' then
                   vPar1 := vPar1||'Nome Centro 1 ['||pParCentro1Nome||']'||chr(13)||chr(10);
           else
                   vPar1 := vPar1||'Nome Centro 1 []'||chr(13)||chr(10);
           end if;
           
           if pParCentro1Ativo != '' then
               vPar1 := vPar1||'Centro 1 Ativo ['||pParCentro1Ativo||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Centro 1 Ativo []'||chr(13)||chr(10);
           end if;
           
           If pParCentroSubTipoId != '' then
               vPar1 := vPar1||'SubTipo ['||fnreport_sigla(pParUnitId,'ope_centro_subtipo','nome','id',''''||pParCentroSubTipoId||'''')||'] '||chr(13)||chr(10);
           else
               vPar1 := vPar1||'SubTipo []'||chr(13)||chr(10);
           end if;
           
           If pParCentroSubTipoNome != '' then
               vPar1 := vPar1||'Nome SubTipo ['||pParCentroSubTipoNome||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Nome SubTipo []'||chr(13)||chr(10);
           end if;
           
               If pParCentro2Id != '' then
               vPar2 := vPar2||'Centro 2 ['||fnreport_sigla(pParUnitId,'ope_centro2','sigla_centro2','id',''''||pParCentro2Id||'''')||'] '||chr(13)||chr(10);
           else
                   vPar2 := vPar2||'Centro 2 []'||chr(13)||chr(10);
           end if;
           
           If pParCentro2Sigla != '' then
                   vPar2 := vPar2||'Centro 2 Sigla['||pParCentro2Sigla||'] '||chr(13)||chr(10);
           else
                   vPar2 := vPar2||'Centro 2 Sigla[]'||chr(13)||chr(10);
           end if;
           
               If pParCentro2Nome != '' then
                   vPar2 := vPar2||'Nome Centro 2 ['||pParCentro2Nome||'] '||chr(13)||chr(10);
           else
                   vPar2 := vPar2||'Nome Centro 2 []'||chr(13)||chr(10);
           end if;
           
           If pParCentro2Ativo != '' then
                   vPar2 := vPar2||'Centro 2 Ativo['||pParCentro2Ativo||'] '||chr(13)||chr(10);
           else
                   vPar2 := vPar2||'Centro 2 Ativo[]'||chr(13)||chr(10);
           end if;	
           
           if pParFrenteTrabalhoId != '' then
                       vPar2 := vPar2||'Frente Trabalho ['||fnreport_sigla(pParUnitId,'ope_frente_trabalho','sigla_frente_trabalho','id',''''||pParFrenteTrabalhoId||'''')||'] '||chr(13)||chr(10);
           else
                   vPar2 := vPar2||'Frente Trabalho []'||chr(13)||chr(10);
           end if;
           
           if pParFrenteTrabalhoNome != '' then
                       vPar2 := vPar2||'Nome Frente Trabalho ['||pParFrenteTrabalhoNome||'] '||chr(13)||chr(10);
           else
                       vPar2 := vPar2||'Nome Frente Trabalho []'||chr(13)||chr(10);
           end if;
           
           if pParFrenteTrabalhoSigla != '' then
                   vPar3 := vPar3||'Sigla Frente Trabalho ['||pParFrenteTrabalhoSigla||'] '||chr(13)||chr(10);
           else
                   vPar3 := vPar3||'Sigla Frente Trabalho []'||chr(13)||chr(10);
           end if;
           
           if pParFrenteTrabalhoAtivo != '' then
                   vPar3 := vPar3||'Frente Trabalho Ativo ['||pParFrenteTrabalhoAtivo||'] '||chr(13)||chr(10);
           else
                   vPar3 := vPar3||'Frente Trabalho Ativo []'||chr(13)||chr(10);
           end if;
           
           if pParLogUserIns != '' then
                   vPar3 := vPar3||'Log Usuario Inserção ['||pParLogUserIns||'] '||chr(13)||chr(10);
           else
                   vPar3 := vPar3||'Log Usuario Inserção []'||chr(13)||chr(10);
           end if;
           
           if pParLogUserUpd != '' then
                   vPar3 := vPar3||'Log Usuario Alteração ['||pParLogUserUpd||'] '||chr(13)||chr(10);
           else
                   vPar3 := vPar3||'Log Usuario Alteração []'||chr(13)||chr(10);
           end if;
           
           if pParLogDateInsIni != '' and pParLogDateInsFin != ''then
                   vPar3 := vPar3||'Data Inserção de ['||pParLogDateInsIni||'] até ['||pParLogDateInsFin||']'||chr(13)||chr(10);
           else
                   vPar3 := vPar3||'Data Inserção de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParLogDateUpdIni != '' and pParLogDateUpdFin != ''then
                   vPar3 := vPar3||'Data Alteração de ['||pParLogDateUpdIni||'] até ['||pParLogDateUpdFin||']'||chr(13)||chr(10);
           else
                   vPar3 := vPar3||'Data Alteração de [] até []'||chr(13)||chr(10);
           end if;
           
           
           
           vSql = 'select
           '  || pVart01 ||'   as vart_01 '||
               ','''|| pVard01 ||''' as vard_01 ';
               
               if  pVart02 != ''  THEN
                vSql = vSql || ','  || pVart02 ||'   as vart_02 '||
                          ','''|| pVard02 ||''' as vard_02 ';
               else 
                  vSql = vSql || ',null as vart_02'||
                                      ',null as vard_02';
               end if;
           if  pVart03 != '' THEN
                vSql = vSql || ','  || pVart03 ||'   as vart_03 '||
                          ','''|| pVard03 ||''' as vard_03 ';
               else 
                  vSql = vSql || ',null as vart_03'||
                                      ',null as vard_03';
               end if;
           if  pVart04 != '' THEN
                vSql = vSql || ','  || pVart04 ||'   as vart_04 '||
                          ','''|| pVard04 ||''' as vard_04 ';
               else 
                  vSql = vSql || ',null as vart_04'||
                                      ',null as vard_04';
               end if;
           if  pVart05 != ''  THEN
                vSql = vSql || ','  || pVart05 ||'   as vart_05 '||
                          ','''|| pVard05 ||''' as vard_05 ';
               else 
                  vSql = vSql || ',null as vart_05'||
                                      ',null as vard_05';
               end if;
           
           
               vSql = vSql ||',
                       count(1) as valor_01
                       from vwope_centro2_pessoa t1 where 1=1';
               
               
               IF pParUnitId != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro1_unit_id' || ' in(''' ||pParUnitId||''')';
               END IF;
               
               IF pParPessoaPtoIdenfTipo != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro2_pessoa_pto_idenf_tipo' || ' like ''' ||pParPessoaPtoIdenfTipo||'''';
               END IF;
               
               IF pParPessoaPtoIdenf != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro2_pessoa_pto_idenf' || ' like ''' ||pParPessoaPtoIdenf||'''';
               END IF;
               
               IF pParCentro1Id != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro1_id' || ' in(''' ||pParCentro1Id||''')';
               END IF;
           
               IF pParCentro1Nome != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro1_nome' || ' like '|| '''%' || pParCentro1Nome || '%'' ';
               END IF;
               
               IF pParCentro1Ativo != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro1_ativo_desc' || ' like '|| '''%' || pParCentro1Ativo || '%'' ';
               END IF;
               
               IF pParCentroSubTipoId != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro_subtipo_id' || ' in(''' ||pParCentroSubTipoId||''')';
               END IF;
                   
               IF pParCentroSubTipoNome != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro_subtipo_nome' || ' like '|| '''%' || pParCentroSubTipoNome || '%'' ';
               END IF;
               
               IF pParCentro2Id != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro2_id' || ' in(''' ||pParCentro2Id||''')';
               END IF;
           
               IF pParCentro2Sigla != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro2_sigla' || ' like '|| '''%' ||pParCentro2Sigla|| '%'' ';
               END IF;
               
               IF pParCentro2Nome != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro2_nome' || ' like '|| '''%' ||pParCentro2Nome|| '%'' ';
               END IF;
               IF pParCentro2Ativo != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro2_ativo_desc' || ' like '|| '''%' ||pParCentro2Ativo|| '%'' ';
               END IF;
               
               IF pParFrenteTrabalhoId != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_frente_trabalho_id' || ' in(''' ||pParFrenteTrabalhoId||''')';
               END IF;
       
               IF pParFrenteTrabalhoNome != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_frente_trabalho_nome' || ' like '|| '''%' ||pParFrenteTrabalhoNome|| '%'' ';
               END IF;
       
               IF pParFrenteTrabalhoSigla != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_frente_trabalho_sigla' || ' like '|| '''%' ||pParFrenteTrabalhoSigla|| '%'' ';
               END IF;
       
               IF pParFrenteTrabalhoAtivo != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_frente_trabalho_ativo_desc' || ' like '|| '''%' ||pParFrenteTrabalhoAtivo|| '%'' ';
               END IF;
       
               IF pParLogUserIns != '' THEN
                   vSql = vSql || 'and ' || ' t1.log_user_ins' || ' like '|| '''%' ||pParLogUserIns|| '%'' ';
               END IF;
               
               IF pParLogDateInsIni != '' and pParLogDateInsFin != '' THEN
                 vSql = vSql || ' and ' || 'CAST(t1.log_date_ins AS DATE)' || ' >= ''' || pParLogDateInsIni|| '''' || ' and  CAST(t1.log_date_ins AS DATE)' || ' <= ''' || pParLogDateInsFin || '''';
               END IF;
               
               IF pParLogUserUpd != '' THEN
                   vSql = vSql || 'and ' || ' t1.log_user_upd' || ' like '|| '''%' ||pParLogUserUpd|| '%'' ';
               END IF;		
       
               IF pParLogDateUpdIni != '' and pParLogDateUpdFin != '' THEN
                 vSql = vSql || ' and ' || 'CAST(t1.log_date_upd AS DATE)' || ' >= ''' || pParLogDateUpdIni|| '''' || ' and  CAST(t1.log_date_upd AS DATE)' || ' <= ''' || pParLogDateUpdFin || '''';
               END IF;
       
            -- Group By
            -- ===================================
               vSql = vSql||' group by '|| pVart01;
       
               if  pVart02 != ''  THEN
                vSql = vSql||  ','|| pVart02;
               end if;
               
           if  pVart03 != ''  THEN
                vSql = vSql||  ','|| pVart03;
               end if;
               
           if  pVart04 != ''  THEN
                vSql = vSql||  ','|| pVart04;
               end if;
               
           if  pVart05 != ''  THEN
                vSql = vSql||  ','|| pVart05;
               end if;
               
            -- Order By
            -- ===================================
               vSql = vSql||' order by '|| pVart01;
       
               if  pVart02 != ''  THEN
                vSql = vSql||  ','|| pVart02;
               end if;
               
           if  pVart03 != ''  THEN
                vSql = vSql||  ','|| pVart03;
               end if;
               
           if  pVart04 != ''  THEN
                vSql = vSql||  ','|| pVart04;
               end if;
               
           if  pVart05 != ''  THEN
                vSql = vSql||  ','|| pVart05;
               end if;
           
           
           FOR r IN EXECUTE vSql loop
           
               ind_rel_id := pParIndRelId;
               ind_rel_par1 := vPar1;
               ind_rel_par2 := vPar2;
               ind_rel_par3 := vPar3;
               vart_01 := r.vart_01;
               vard_01 := r.vard_01;
               vart_02 := r.vart_02;
               vard_02 := r.vard_02;
               vart_03 := r.vart_03;
               vard_03 := r.vard_03;
               vart_04 := r.vart_04;
               vard_04 := r.vard_04;
               vart_05 := r.vart_05;
               vard_05 := r.vard_05;
               valor_01 := r.valor_01;
               
           RETURN NEXT;
           
       END loop;
       raise notice'vSql :%',vSql;
               
               
       end;
       $BODY$
         LANGUAGE plpgsql VOLATILE;;
           
       
       
       -----------
       
       

       Drop FUNCTION IF EXISTS  fnreport0018;;

       CREATE OR REPLACE FUNCTION fnreport0018(
       pParUnitId varchar, 
       pParIndRelId varchar, 
       pVart01 varchar, 
       pVard01 varchar, 
       pVart02 varchar default null,
       pVard02 varchar default null,
       pVart03 varchar default null,
       pVard03 varchar default null,
       pVart04 varchar default null,
       pVard04 varchar default null,
       pVart05 varchar default null,
       pVard05 varchar default null,
       pParEstoqId  varchar default null,
       pParEstoqTipo  varchar default null,
       pParCentro2Id  varchar default null,
       pParCentro2Nome  varchar default null,
       pParCentro2Ativo  varchar default null,
       pParCentro2Sigla  varchar default null,
       pParCentro2TipoDestinacao  varchar default null,
       pParCentro2TipoCtbComp  varchar default null,
       pParCentro2CtbCompId varchar default null,
       pParLogUserIns varchar default null,
       pParLogDateInsIni varchar default null,
       pParLogDateInsFin varchar default null,
       pParLogUserUpd varchar default null,
       pParLogDateUpdIni varchar default null,
       pParLogDateUpdFin varchar default null
       )
       RETURNS TABLE(
        ind_rel_id varchar,
        ind_rel_par1 varchar,
        ind_rel_par2 varchar,
        vart_01 varchar,
        vard_01 varchar,
        vart_02 varchar,
        vard_02 varchar,
        vart_03 varchar,
        vard_03 varchar,
        vart_04 varchar,
        vard_04 varchar,
        vart_05 varchar,
        vard_05 varchar,
        valor_01 numeric,
        valor_02 numeric,
        valor_03 numeric,
        valor_04 numeric,
        valor_05 numeric,
        valor_06 numeric,
        valor_07 numeric,
        valor_08 numeric,
        valor_09 numeric,
        valor_10 numeric) AS $BODY$
       declare
       vSql varchar;
       vPar1 varchar :='';
       vPar2 varchar :='';
       r record;
       
       begin
       
       
       if pParEstoqTipo != '' then
           vPar1 := vPar1||'Tipo Estoque ['||pParEstoqTipo||']'||chr(13)||chr(10);
       else
           vPar1 := vPar1||'Tipo Estoque []'||chr(13)||chr(10);
       end if;
       
       if pParCentro2Id != '' then
           vPar1 := vPar1||'Centro 2 ['||fnreport_sigla(pParUnitId,'ope_centro2','sigla_centro2','id',''''||pParCentro2Id||'''')||'] '||chr(13)||chr(10);
       else
       vPar1 := vPar1||'Centro 2 []'||chr(13)||chr(10);
       end if;
       
       if pParCentro2Nome != '' then
       vPar1 := vPar1||'Nome Centro 2 ['||pParCentro2Nome||']'||chr(13)||chr(10);
       else
       vPar1 := vPar1||'Nome Centro 2 []'||chr(13)||chr(10);
       end if;
       
       if pParCentro2Ativo != '' then
       vPar1 := vPar1||'Centro 2 Ativo ['||pParCentro2Ativo||']'||chr(13)||chr(10);
       else
       vPar1 := vPar1||'Centro 2 Ativo []'||chr(13)||chr(10);
       end if;
       
       if pParCentro2Sigla != '' then
       vPar1 := vPar1||'Centro 2 Sigla ['||pParCentro2Sigla||']'||chr(13)||chr(10);
       else
       vPar1 := vPar1||'Centro 2 Sigla []'||chr(13)||chr(10);
       end if;
       
       if pParCentro2TipoDestinacao != '' then
       vPar1 := vPar1||'Destinação ['||pParCentro2TipoDestinacao||']'||chr(13)||chr(10);
       else
       vPar1 := vPar1||'Destinação []'||chr(13)||chr(10);
       end if;
       
       if pParCentro2TipoCtbComp != '' then
       vPar2 := vPar2||'Centro 2 Tipo Contabil ['||pParCentro2TipoCtbComp||']'||chr(13)||chr(10);
       else
       vPar2 := vPar2||'Centro 2 Tipo Contabil []'||chr(13)||chr(10);
       end if;
       
       if pParCentro2CtbCompId != '' then
           vPar2 := vPar2||'Componente Contábil ['||fnreport_sigla(pParUnitId,'ctb_comp','sigla_comp','id',''''||pParCentro2CtbCompId||'''')||'] '||chr(13)||chr(10);
       else
       vPar2 := vPar2||'Componente Contábil []'||chr(13)||chr(10);
       end if;
       
       if pParLogUserIns != '' then
       vPar2 := vPar2||'Log Usuario Inserção ['||pParLogUserIns||']'||chr(13)||chr(10);
       else
       vPar2 := vPar2||'Log Usuario Inserção []'||chr(13)||chr(10);
       end if;
       
       if pParLogUserUpd != '' then
       vPar2 := vPar2||'Log Usuario Alteração ['||pParLogUserIns||']'||chr(13)||chr(10);
       else
       vPar2 := vPar2||'Log Usuario Alteração []'||chr(13)||chr(10);
       end if;
       
       if pParLogDateInsIni != '' and pParLogDateInsFin != '' then
           vPar2 := vPar2||'Data Inserção de ['||pParLogDateInsIni||'] até ['||pParLogDateInsFin||']'||chr(13)||chr(10);
       else
                   vPar2 := vPar2||'Data Inserção de [] até []'||chr(13)||chr(10);
       end if;
       
           if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then
               vPar2 := vPar2||'Data Alteração de ['||pParLogDateUpdIni||'] até ['||pParLogDateUpdFin||']'||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Data Alteração de [] até []'||chr(13)||chr(10);
           end if;
       
           vSql = 'select
           '  || pVart01 ||'   as vart_01 '||
               ','''|| pVard01 ||''' as vard_01 ';
               
               if  pVart02 != ''  THEN
                vSql = vSql || ','  || pVart02 ||'   as vart_02 '||
                          ','''|| pVard02 ||''' as vard_02 ';
               else 
                  vSql = vSql || ',null as vart_02'||
                                      ',null as vard_02';
               end if;
           if  pVart03 != '' THEN
                vSql = vSql || ','  || pVart03 ||'   as vart_03 '||
                          ','''|| pVard03 ||''' as vard_03 ';
               else 
                  vSql = vSql || ',null as vart_03'||
                                      ',null as vard_03';
               end if;
           if  pVart04 != '' THEN
                vSql = vSql || ','  || pVart04 ||'   as vart_04 '||
                          ','''|| pVard04 ||''' as vard_04 ';
               else 
                  vSql = vSql || ',null as vart_04'||
                                      ',null as vard_04';
               end if;
           if  pVart05 != ''  THEN
                vSql = vSql || ','  || pVart05 ||'   as vart_05 '||
                          ','''|| pVard05 ||''' as vard_05 ';
               else 
                  vSql = vSql || ',null as vart_05'||
                                      ',null as vard_05';
               end if;
               
               vSql = vSql ||',
                   count(1) as valor_01
                   from vwope_centro2_estoque t1 where 1=1';
       
       
               IF pParUnitId != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro2_estoque_unit_id' || ' in(''' ||pParUnitId||''')';
               END IF;
               
               IF pParEstoqId != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro2_estoque_id' || ' in(''' ||pParEstoqId||''')';
               END IF;
               
               IF pParEstoqTipo != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro2_estoque_tipo' || ' like '|| '''%' || pParEstoqTipo || '%'' ';			
               END IF;
               
               IF pParCentro2Id != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro2_id' || ' in(''' ||pParCentro2Id||''')';			
               END IF;
               
               IF pParCentro2Nome != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro2_nome' || ' like '|| '''%' || pParCentro2Nome || '%'' ';	
               END IF;
               
               IF pParCentro2Ativo != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro2_ativo_desc' || ' like '|| '''%' || pParCentro2Ativo || '%'' ';	
               END IF;
               
               IF pParCentro2Sigla != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro2_sigla_centro2' || ' like '|| '''%' || pParCentro2Sigla || '%'' ';	
               END IF;
               
               IF pParCentro2TipoDestinacao != '' THEN
                 vSql = vSql|| 'and ' || ' t1.ope_centro2_tipo_destinacao' || ' like '|| '''%' || pParCentro2TipoDestinacao|| '%'' ';	
               END IF;
               
               IF pParCentro2TipoCtbComp != '' THEN
                 vSql = vSql|| 'and ' || ' t1.ope_centro2_tipo_ctb_comp' || ' like '|| '''%' || pParCentro2TipoCtbComp|| '%'' ';	
               END IF;
               
               IF pParCentro2TipoCtbComp != '' THEN
                 vSql = vSql|| 'and ' || ' t1.ope_centro2_tipo_ctb_comp' || ' like '|| '''%' || pParCentro2TipoCtbComp|| '%'' ';	
               END IF;
       
               IF pParCentro2CtbCompId != '' THEN
                   vSql = vSql || 'and ' || ' t1.ope_centro2_ctb_comp_id' || ' in(''' ||pParCentro2CtbCompId||''')';			
               END IF;
               
               IF pParLogUserIns != '' THEN
                   vSql = vSql || 'and ' || ' t1.log_user_ins' || ' like '|| '''%' ||pParLogUserIns|| '%'' ';
               END IF;
               
               IF pParLogDateInsIni != '' and pParLogDateInsFin != '' THEN
                 vSql = vSql || ' and ' || 'CAST(t1.log_date_ins AS DATE)' || ' >= ''' || pParLogDateInsIni|| '''' || ' and  CAST(t1.log_date_ins AS DATE)' || ' <= ''' || pParLogDateInsFin || '''';
               END IF;
               
               IF pParLogUserUpd != '' THEN
                   vSql = vSql || 'and ' || ' t1.log_user_upd' || ' like '|| '''%' ||pParLogUserUpd|| '%'' ';
               END IF;		
       
               IF pParLogDateUpdIni != '' and pParLogDateUpdFin != '' THEN
                 vSql = vSql || ' and ' || 'CAST(t1.log_date_upd AS DATE)' || ' >= ''' || pParLogDateUpdIni|| '''' || ' and  CAST(t1.log_date_upd AS DATE)' || ' <= ''' || pParLogDateUpdFin || '''';
               END IF;
               
            -- Group By
            -- ===================================
               vSql = vSql||' group by '|| pVart01;
       
               if  pVart02 != ''  THEN
                vSql = vSql||  ','|| pVart02;
               end if;
               
           if  pVart03 != ''  THEN
                vSql = vSql||  ','|| pVart03;
               end if;
               
           if  pVart04 != ''  THEN
                vSql = vSql||  ','|| pVart04;
               end if;
               
           if  pVart05 != ''  THEN
                vSql = vSql||  ','|| pVart05;
               end if;
               
            -- Order By
            -- ===================================
               vSql = vSql||' order by '|| pVart01;
       
               if  pVart02 != ''  THEN
                vSql = vSql||  ','|| pVart02;
               end if;
               
           if  pVart03 != ''  THEN
                vSql = vSql||  ','|| pVart03;
               end if;
               
           if  pVart04 != ''  THEN
                vSql = vSql||  ','|| pVart04;
               end if;
               
           if  pVart05 != ''  THEN
                vSql = vSql||  ','|| pVart05;
               end if;
           
           
           FOR r IN EXECUTE vSql loop
               ind_rel_id := pParIndRelId;
               ind_rel_par1 := vPar1;
               ind_rel_par2 := vPar2;
               vart_01 := r.vart_01;
               vard_01 := r.vard_01;
               vart_02 := r.vart_02;
               vard_02 := r.vard_02;
               vart_03 := r.vart_03;
               vard_03 := r.vard_03;
               vart_04 := r.vart_04;
               vard_04 := r.vard_04;
               vart_05 := r.vart_05;
               vard_05 := r.vard_05;
               valor_01 := r.valor_01;
       
           RETURN NEXT;
           
       END loop;
       raise notice'vSql :%',vSql;
       
       end;
       $BODY$
         LANGUAGE plpgsql VOLATILE;;
       
       
       -----------
       
       

       drop function if EXISTS fnreport0019;;

       CREATE OR REPLACE FUNCTION fnreport0019(
       pParUnitId varchar,
       pParIndRelId varchar,
       pVart01 varchar, 
       pVard01 varchar, 
       pVart02 varchar default null,
       pVard02 varchar default null,
       pVart03 varchar default null,
       pVard03 varchar default null,
       pVart04 varchar default null,
       pVard04 varchar default null,
       pVart05 varchar default null,
       pVard05 varchar default null,
       pParOrdDestId varchar default null,
       pParOrdDestQntPrevObjIni varchar default null,
       pParOrdDestQntPrevObjFin varchar default null,
       pParOrdDestVrUnitPrevIni varchar default null,
       pParOrdDestVrUnitPrevFin varchar default null,
       pParOrdDestVrTotPrevIni varchar default null,
       pParOrdDestVrTotPrevFin varchar default null,
       pParOrdDestQntObjIni varchar default null,
       pParOrdDestQntObjFin varchar default null,
       pParOrdDestVrUnitIni varchar default null,
       pParOrdDestVrUnitFin varchar default null,
       pParOrdDestVrTotalIni varchar default null,
       pParOrdDestVrTotalFin varchar default null,
       pParOrdDataIniExecIni varchar default null,
       pParOrdDataIniExecFin varchar default null,
       pParOrdDataFinExecIni varchar default null,
       pParOrdDataFinExecFin varchar default null,
       pParOrdDataStatusIni varchar default null,
       pParOrdDataStatusFin varchar default null,
       pParOrdDataIniExecPrevIni varchar default null,
       pParOrdDataIniExecPrevFin varchar default null,
       pParOrdDataFinExecPrevIni varchar default null,
       pParOrdDataFinExecPrevFin varchar default null,
       pParCentro2Id varchar default null,
       pParCentro2Nome varchar default null,
       pParCentro2Ativo varchar default null,
       
       pParCtbId varchar default null,
       pParCtbNome varchar default null,
       pParCtbAtivo varchar default null,
       
       pParGerUmedidaId varchar default null,
       pParGerUmedidaNome varchar default null,
       pParGerUmedidaAtivo varchar default null,
       pParCentro1Id varchar default null,
       pParCentro1Nome varchar default null,
       pParCentro1Ativo varchar default null,
       pParSubGrupoId varchar default null,
       pParSubGrupoNome varchar default null,
       pParSubGrupoAtivo varchar default null,
       pParGrupoId varchar default null,
       pParGrupoNome varchar default null,
       pParGrupoAtivo varchar default null,
       pParSubTipoId varchar default null,
       pParSubTipoNome varchar default null,
       pParTipoId varchar default null,
       pParTipoNome varchar default null,
       pParGerEmpresaId varchar default null,
       pParGerEmpresaNome varchar default null,
       pParGerEmpresaAtivo varchar default null,
       pParGerEmpresaDocCnpj varchar default null,
       pParGerEmpresaDocCpf varchar default null,
       pParPeriodoId varchar default null,
       pParPeriodoNome varchar default null,
       pParPeriodoAtivo varchar default null,
       pParPeriodoDataIni varchar default null,
       pParPeriodoDataIniFin varchar default null,
       pParPeriodoDataFinIni varchar default null,
       pParPeriodoDataFin varchar default null,
       pParCentro2PessoaId varchar default null,
       pParCentro2PessoaNome varchar default null,
       pParGerPessoaEnderecoId varchar default null,
       pParGerPessoaEnderecoAtivo varchar default null,
       pParGerPessoaEnderecoTipo varchar default null,
       pParGerPessoaEnderecoPadrao varchar default null,
       pParGerPessoaEnderecoLograd varchar default null,
       pParGerPessoaEnderecoLogradNr varchar default null,
       pParGerPessoaEnderecoLogradBairro varchar default null,
       pParGerPessoaId varchar default null,
       pParGerPessoaNome varchar default null,
       pParGerPessoaAtivo varchar default null,
       pParGerPessoaDoc varchar default null,
       pParOrdTipoId varchar default null,
       pParOrdTipoNome varchar default null,
       
       pParOrdCentro2Id varchar default null,
       pParOrdCentro2Nome varchar default null,
       pParOrdCentro2Ativo varchar default null,
       pParFrenteTrabalhoId varchar default null,
       pParFrenteTrabalhoNome varchar default null,
       pParFrenteTrabalhoAtivo varchar default null,
       pParStatusId varchar default null,
       pParStatusNome varchar default null,
       pParStatusAtivo varchar default null,
       pParStatusTipo varchar default null,
       pParLogUserIns varchar default null,
       pParLogDateInsIni varchar default null,
       pParLogDateInsFin varchar default null,
       pParLogUserUpd varchar default null,
       pParLogDateUpdIni varchar default null,
       pParLogDateUpdFin varchar default null
       )
       
       RETURNS TABLE(
        ind_rel_id varchar,
        ind_rel_par1 varchar,
        ind_rel_par2 varchar,
        ind_rel_par3 varchar,
        ind_rel_par4 varchar,
        vart_01 varchar,
        vard_01 varchar,
        vart_02 varchar,
        vard_02 varchar,
        vart_03 varchar,
        vard_03 varchar,
        vart_04 varchar,
        vard_04 varchar,
        vart_05 varchar,
        vard_05 varchar,
        valor_01 numeric,
        valor_02 numeric,
        valor_03 numeric,
        valor_04 numeric,
        valor_05 numeric,
        valor_06 numeric,
        valor_07 numeric,
        valor_08 numeric,
        valor_09 numeric,
        valor_10 numeric) AS $BODY$
       declare
       vSql varchar;
       vPar1 varchar :='';
       vPar2 varchar :='';
       vPar3 varchar :='';
       vPar4 varchar :='';
       r record;
       
       begin
           if  pParOrdDestQntPrevObjIni != '' and pParOrdDestQntPrevObjFin != '' then
             vPar1 := vPar1||'Qntd - Prevista - Objeto de ['||pParOrdDestQntPrevObjIni||'] até ['||pParOrdDestQntPrevObjFin||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Qntd - Prevista - Objeto de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParOrdDestVrUnitPrevIni != '' and pParOrdDestVrUnitPrevFin != '' then
               vPar1 := vPar1 ||'Valor Unitário - Previsto de ['||pParOrdDestVrUnitPrevIni||'] até ['||pParOrdDestVrUnitPrevFin||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1 ||'Valor Unitário - Previsto de [] até []'||chr(13)||chr(10);
           end if;
           if pParOrdDestVrTotPrevIni != '' and pParOrdDestVrTotPrevFin != '' then
               vPar1 := vPar1 ||'Valor Total - Previsto de ['||pParOrdDestVrTotPrevIni||'] até ['||pParOrdDestVrTotPrevFin||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1 ||'Valor Total - Previsto de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParOrdDestQntObjIni != '' and pParOrdDestQntObjFin != '' then
               vPar1 := vPar1 ||'Qntd - Real - Objeto de ['||pParOrdDestQntObjIni||'] até ['||pParOrdDestQntObjFin||']'||chr(13)||chr(10);
           else 
               vPar1 := vPar1||'Qntd - Real - Objeto de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParOrdDestVrUnitIni != '' and pParOrdDestVrUnitFin != '' then
               vPar1 := vPar1||'Valor Unitário - Real de['||pParOrdDestVrUnitIni||'] até ['||pParOrdDestVrUnitFin||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Valor Unitário - Real de[] até []'||chr(13)||chr(10);
           end if;
           
           if pParOrdDestVrTotalIni != '' and pParOrdDestVrTotalFin != '' then
               vPar1 := vPar1||'Valor Total - Real de ['||pParOrdDestVrTotalIni||'] até ['||pParOrdDestVrTotalFin||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Valor Total - Real de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParOrdDataIniExecIni != '' and pParOrdDataIniExecFin != '' then
               vPar1 := vPar1||'Data Inicial Execução de ['||pParOrdDataIniExecIni||'] até ['||pParOrdDataIniExecFin||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Data Inicial Execução de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParOrdDataFinExecIni != '' and pParOrdDataFinExecFin != '' then
               vPar1 := vPar1||'Data Final Execução de ['||pParOrdDataFinExecIni||'] até ['||pParOrdDataFinExecFin||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Data Final Execução de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParOrdDataStatusIni != '' and pParOrdDataStatusFin != '' then
               vPar1 := vPar1||'Data Status de ['||pParOrdDataStatusIni||'] até ['||pParOrdDataStatusFin||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Data Status de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParOrdDataIniExecPrevIni != '' and pParOrdDataIniExecPrevFin != '' then
               vPar1 := vPar1||'Data Inicial Execução Prev de ['||pParOrdDataIniExecPrevIni||'] até ['||pParOrdDataIniExecPrevFin||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Data Inicial Execução Prev de [] até []'||chr(13)||chr(10);
           end if;
       
           if pParOrdDataFinExecPrevIni != '' and pParOrdDataFinExecPrevFin != '' then
               vPar1 := vPar1||'Data Final Execução Prev de ['||pParOrdDataFinExecPrevIni||'] até ['||pParOrdDataFinExecPrevFin||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Data Final Execução Prev de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParCentro2Id != '' then
                   vPar1 := vPar1||'Centro 2 ['||fnreport_sigla(pParUnitId,'ope_centro2','sigla_centro2','id',''''||pParCentro2Id||'''')||'] '||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Centro 2 []'||chr(13)||chr(10);
           end if;
           
           if pParCentro2Nome != '' then
               vPar1:= vPar1||'Nome Centro 2 ['||pParCentro2Nome||']'||chr(13)||chr(10);
           else
               vPar1:= vPar1||'Nome Centro 2 []'||chr(13)||chr(10);
           end if;
           
           if pParCentro2Ativo != '' then
               vPar1:= vPar1||'Centro 2 Ativo ['||pParCentro2Ativo||']'||chr(13)||chr(10);
           else 
               vPar1:= vPar1||'Centro 2 Ativo []'||chr(13)||chr(10);
           end if;
           
           if pParCtbId != '' then
                   vPar1 := vPar1||'Componente Contábil ['||fnreport_sigla(pParUnitId,'ctb_comp','sigla_comp','id',''''||pParCtbId||'''')||'] '||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Componente Contábil []'||chr(13)||chr(10);
           end if;
           
           if pParCtbNome != '' then
               vPar1 := vPar1||'Nome Componente Contábil ['||pParCtbNome||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Nome Componente Contábil []'||chr(13)||chr(10);
           end if;
           
           if pParCtbAtivo != '' then
               vPar1 := vPar1||'Componente Contábil Ativo ['||pParCtbAtivo||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Componente Contábil Ativo []'||chr(13)||chr(10);
           end if;
           
           if pParGerUmedidaId != '' then
                   vPar2 := vPar2||'Unidade Medida ['||fnreport_sigla(pParUnitId,'ger_umedida','sigla_umedida','id',''''||pParGerUmedidaId||'''')||'] '||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Unidade Medida []'||chr(13)||chr(10);
           end if;	
           
           if pParGerUmedidaNome != '' then
               vPar2 := vPar2||'Nome Unidade Medida ['||pParGerUmedidaNome||']'||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Nome Unidade Medida []'||chr(13)||chr(10);
           end if;
           
           if pParGerUmedidaAtivo != '' then
               vPar2 := vPar2||'Unidade Medida Ativo ['||pParGerUmedidaAtivo||']'||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Unidade Medida Ativo[]'||chr(13)||chr(10);
           end if;
           
           if pParCentro1Id != '' then
                   vPar2 := vPar2||'Centro 1 ['||fnreport_sigla(pParUnitId,'ope_centro1','sigla_centro1','id',''''||pParCentro1Id||'''')||'] '||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Centro 1 []'||chr(13)||chr(10);
           end if;
           
           if pParCentro1Nome != '' then
               vPar2 := vPar2||'Nome Centro 1 ['||pParCentro1Nome||']'||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Nome Centro 1 []'||chr(13)||chr(10);
           end if;
       
           if pParCentro1Ativo != '' then
               vPar2 := vPar2||'Centro 1 Ativo ['||pParCentro1Ativo||']'||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Centro 1 Ativo []'||chr(13)||chr(10);
           end if;
           
           if pParSubGrupoId != '' then
                   vPar2 := vPar2||'SubGrupo ['||fnreport_sigla(pParUnitId,'ope_centro_subgrupo','sigla_centro_subgrupo','id',''''||pParSubGrupoId||'''')||'] '||chr(13)||chr(10);
           else
                   vPar2 := vPar2||'SubGrupo []'||chr(13)||chr(10);
           end if;
           if pParSubGrupoNome != '' then
               vPar2 := vPar2||'Nome SubGrupo ['||pParSubGrupoNome||']'||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Nome SubGrupo []'||chr(13)||chr(10);
           end if;
           
           if pParSubGrupoAtivo != '' then
               vPar2 := vPar2||'SubGrupo Ativo ['||pParSubGrupoAtivo||']'||chr(13)||chr(10);
           else
               vPar2 := vPar2||'SubGrupo Ativo []'||chr(13)||chr(10);
           end if;
           
           if pParGrupoId != '' then
               vPar2 := vPar2||'Grupo ['||fnreport_sigla(pParUnitId,'ope_centro_grupo','sigla_centro_grupo','id',''''||pParGrupoId||'''')||'] '||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Grupo []'||chr(13)||chr(10);
           end if;
           
           if pParGrupoNome != '' then
               vPar2 := vPar2||'Nome Grupo ['||pParGrupoNome||']'||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Nome Grupo []'||chr(13)||chr(10);
           end if;
           
           if pParGrupoAtivo != '' then
               vPar2 := vPar2||'Grupo Ativo ['||pParGrupoAtivo||']'||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Grupo Ativo []'||chr(13)||chr(10);
           end if;
           
           if pParSubTipoId != '' then
               vPar2 := vPar2||'SubTipo ['||fnreport_sigla(pParUnitId,'ope_centro_subtipo','nome','id',''''||pParSubTipoId||'''')||'] '||chr(13)||chr(10);
           else
               vPar2 := vPar2||'SubTipo []'||chr(13)||chr(10);	
           end if;
           
           if pParSubTipoNome != '' then
               vPar2 := vPar2||'Nome SubTipo ['||pParSubTipoNome||']'||chr(13)||chr(10);	
           else
               vPar2 := vPar2||'Nome SubTipo []'||chr(13)||chr(10);	
           end if;
           
           if pParTipoId != '' then
               vPar2 := vPar2||'Tipo ['||fnreport_sigla(pParUnitId,'ope_centro_tipo','nome','id',''''||pParTipoId||'''')||'] '||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Tipo []'||chr(13)||chr(10);	
           end if;
           
           if pParTipoNome != '' then
               vPar2 := vPar2||'Nome Tipo ['||pParTipoNome||']'||chr(13)||chr(10);	
           else
               vPar2 := vPar2||'Nome Tipo []'||chr(13)||chr(10);	
           end if;
           
           if pParGerEmpresaId != '' then
               vPar2 := vPar2||'Empresa ['||fnreport_sigla(pParUnitId,'ger_empresa','sigla_empresa','id',''''||pParGerEmpresaId||'''')||'] '||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Empresa []'||chr(13)||chr(10);
           end if;
           
           if pParGerEmpresaNome != '' then
               vPar2 := vPar2||'Nome Empresa ['||pParGerEmpresaNome||']'||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Nome Empresa []'||chr(13)||chr(10);
           end if;
           
           if pParGerEmpresaAtivo != '' then
               vPar3 := vPar3||'Empresa Ativo['||pParGerEmpresaAtivo||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Empresa Ativo[]'||chr(13)||chr(10);
           end if;
           
           if pParGerEmpresaDocCnpj != '' then
               vPar3 := vPar3||'Empresa Doc Cnpj['||pParGerEmpresaDocCnpj||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Empresa Doc Cnpj[]'||chr(13)||chr(10);
           end if;
           
           if pParGerEmpresaDocCpf != '' then
               vPar3 := vPar3||'Empresa Doc Cpf['||pParGerEmpresaDocCpf||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Empresa Doc Cpf[]'||chr(13)||chr(10);
           end if;
           
           if pParPeriodoId != '' then
               vPar3 := vPar3||'Período ['||fnreport_sigla(pParUnitId,'ope_periodo','sigla_periodo','id',''''||pParPeriodoId||'''')||'] '||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Período []'||chr(13)||chr(10);
           end if;
           
           if pParPeriodoNome != '' then
               vPar3 := vPar3||'Nome Período ['||pParPeriodoNome||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Nome Período []'||chr(13)||chr(10);
           end if;
           
           if pParPeriodoAtivo != '' then
               vPar3 := vPar3||'Período Ativo['||pParPeriodoAtivo||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Período Ativo[]'||chr(13)||chr(10);
           end if;
           
           if pParPeriodoDataIni != '' and pParPeriodoDataIniFin != '' then
                vPar3 := vPar3||'Data Inicial Período de ['||pParPeriodoDataIni||'] até ['||pParPeriodoDataIniFin||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Data Inicial Período de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParPeriodoDataFinIni != '' and pParPeriodoDataFin !='' then
               vPar3 := vPar3||'Data Final Período de ['||pParPeriodoDataFinIni||'] até ['||pParPeriodoDataFin||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Data Final Período de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParCentro2PessoaId != '' then
               vPar3 := vPar3||'Centro 2 Pessoa ['||fnreport_sigla(pParUnitId,'ger_pessoa','sigla_pes','id',''''||pParCentro2PessoaId||'''')||'] '||chr(13)||chr(10);	
           else
               vPar3 := vPar3||'Centro 2 Pessoa []'||chr(13)||chr(10);
           end if;
           
           if pParCentro2PessoaNome != '' then
               vPar3 := vPar3||'Centro 2 Nome Pessoa ['||pParCentro2PessoaNome||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Centro 2 Nome Pessoa []'||chr(13)||chr(10);
           end if;
           
           if pParGerPessoaEnderecoAtivo != '' then
               vPar3 := vPar3||'Pessoa Endereco Ativo ['||pParGerPessoaEnderecoAtivo||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Pessoa Endereco Ativo []'||chr(13)||chr(10);
           end if;
           
           if pParGerPessoaEnderecoTipo != '' then
               vPar3 := vPar3||'Pessoa Endereco Tipo ['||pParGerPessoaEnderecoTipo||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Pessoa Endereco Tipo []'||chr(13)||chr(10);	
           end if;
           
           if pParGerPessoaEnderecoPadrao != '' then
               vPar3 := vPar3||'Pessoa Endereco Padrão ['||pParGerPessoaEnderecoPadrao||']'||chr(13)||chr(10);	
           else
               vPar3 := vPar3||'Pessoa Endereco Padrão []'||chr(13)||chr(10);	
           end if;
           
           if pParGerPessoaEnderecoLograd !='' then
               vPar3 := vPar3||'Pessoa Endereco Logradouro ['||pParGerPessoaEnderecoLograd||']'||chr(13)||chr(10);	
           else
               vPar3 := vPar3||'Pessoa Endereco Logradouro []'||chr(13)||chr(10);	
           end if;
           
           if pParGerPessoaEnderecoLogradNr !='' then
               vPar3 := vPar3||'Pessoa Nº Endereco ['||pParGerPessoaEnderecoLogradNr||']'||chr(13)||chr(10);			
           else
               vPar3 := vPar3||'Pessoa Nº Endereco []'||chr(13)||chr(10);	
           end if;
           
           if pParGerPessoaEnderecoLogradBairro != '' then
               vPar3 := vPar3||'Pessoa Bairro ['||pParGerPessoaEnderecoLogradBairro||']'||chr(13)||chr(10);	
           else
               vPar3 := vPar3||'Pessoa Bairro []'||chr(13)||chr(10);	
           end if;
           
           if pParGerPessoaId != '' then
               vPar3 := vPar3||'Pessoa ['||fnreport_sigla(pParUnitId,'ger_pessoa','sigla_pes','id',''''||pParCentro2PessoaId||'''')||'] '||chr(13)||chr(10);		
           else
               vPar3 := vPar3||'Pessoa []'||chr(13)||chr(10);		
           end if;
           
           if pParGerPessoaNome != '' then
               vPar3 := vPar3||'Nome Pessoa ['||pParGerPessoaNome||']'||chr(13)||chr(10);		
           else
               vPar3 := vPar3||'Nome Pessoa []'||chr(13)||chr(10);		
           end if;
           
           if pParGerPessoaAtivo != '' then
               vPar4 := vPar4||'Pessoa Ativo ['||pParGerPessoaAtivo||']'||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Pessoa Ativo []'||chr(13)||chr(10);		
           end if;
           
           if pParGerPessoaDoc != '' then
               vPar4 := vPar4||'Pessoa Doc ['||pParGerPessoaDoc||']'||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Pessoa Doc []'||chr(13)||chr(10);
           end if;
           
           if pParOrdTipoId != '' then
               vPar4 := vPar4||'Tipo ['||fnreport_sigla(pParUnitId,'ope_centro2_ord_tipo','sigla_ord_tipo','id',''''||pParOrdTipoId||'''')||'] '||chr(13)||chr(10);	
           else
               vPar4 := vPar4||'Tipo []'||chr(13)||chr(10);
           end if;
           
           if pParOrdTipoNome != '' then
               vPar4 := vPar4||'Nome Tipo ['||pParOrdTipoNome||']'||chr(13)||chr(10);	
           else
               vPar4 := vPar4||'Nome Tipo []'||chr(13)||chr(10);
           end if;
           
           
           if pParOrdCentro2Id != '' then
               vPar4 := vPar4||'Centro 2 Ord ['||fnreport_sigla(pParUnitId,'ope_centro2','sigla_centro2','id',''''||pParOrdCentro2Id||'''')||'] '||chr(13)||chr(10);				
           else
               vPar4 := vPar4||'Centro 2 Ord []'||chr(13)||chr(10);			
           end if;
           
           if pParOrdCentro2Nome != '' then
               vPar4 := vPar4||'Nome Centro 2 Ord ['||pParOrdCentro2Nome||']'||chr(13)||chr(10);				
           else
               vPar4 := vPar4||'Nome Centro 2 Ord []'||chr(13)||chr(10);			
           end if;
           
           
           if pParOrdCentro2Ativo != '' then
               vPar4 := vPar4||'Centro 2 Ord Ativo ['||pParOrdCentro2Ativo||']'||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Centro 2 Ord Ativo []'||chr(13)||chr(10);
           end if;
           
           if pParFrenteTrabalhoId != '' then
               vPar4 := vPar4||'Frente Trabalho ['||fnreport_sigla(pParUnitId,'ope_frente_trabalho','sigla_frente_trabalho','id',''''||pParFrenteTrabalhoId||'''')||'] '||chr(13)||chr(10);		
           else
               vPar4 := vPar4||'Frente Trabalho []'||chr(13)||chr(10);
           end if;
           
           if pParFrenteTrabalhoNome != '' then
               vPar4 := vPar4||'Nome Frente Trabalho ['||pParFrenteTrabalhoNome||']'||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Nome Frente Trabalho []'||chr(13)||chr(10);
           end if;
       
           if pParFrenteTrabalhoAtivo != '' then
               vPar4 := vPar4||'Frente Trabalho Ativo['||pParFrenteTrabalhoAtivo||']'||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Frente Trabalho Ativo[]'||chr(13)||chr(10);	
           end if;
           
           if pParStatusId != '' then
               vPar4 := vPar4||'Status ['||fnreport_sigla(pParUnitId,'ope_centro2_ord_status','sigla_ord_status','id',''''||pParStatusId||'''')||']'||chr(13)||chr(10);			
           else
               vPar4 := vPar4||'Status []'||chr(13)||chr(10);
           end if;
           
           if pParStatusNome != '' then
               vPar4 := vPar4||'Nome Status ['||pParStatusNome||']'||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Nome Status []'||chr(13)||chr(10);	
           end if;
       
           if pParStatusAtivo != '' then
               vPar4 := vPar4||'Status Ativo ['||pParStatusAtivo||']'||chr(13)||chr(10);	
           else
               vPar4 := vPar4||'Status Ativo []'||chr(13)||chr(10);		
           end if;
       
           if pParStatusTipo != '' then
               vPar4 := vPar4||'Status Tipo ['||pParStatusTipo||']'||chr(13)||chr(10);	
           else
               vPar4 := vPar4||'Status Tipo []'||chr(13)||chr(10);	
           end if;
           
           if pParLogUserIns != '' then
               vPar4 := vPar4||'Log Usuario Inserção ['||pParLogUserIns||']'||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Log Usuario Inserção []'||chr(13)||chr(10);
           end if;
       
           if pParLogUserUpd != '' then
               vPar4 := vPar4||'Log Usuario Alteração ['||pParLogUserUpd||']'||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Log Usuario Alteração []'||chr(13)||chr(10);
           end if;
       
           if pParLogDateInsIni != '' and pParLogDateInsFin != '' then
               vPar4 := vPar4||'Data Inserção de ['||pParLogDateInsIni||'] até ['||pParLogDateInsFin||']'||chr(13)||chr(10);
           else
                       vPar4 := vPar4||'Data Inserção de [] até []'||chr(13)||chr(10);
           end if;
       
           if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then
               vPar4 := vPar4||'Data Alteração de ['||pParLogDateUpdIni||'] até ['||pParLogDateUpdFin||']'||chr(13)||chr(10);
           else
                   vPar4 := vPar4||'Data Alteração de [] até []'||chr(13)||chr(10);
           end if;
           
           vSql = 'select
           '  || pVart01 ||'   as vart_01 '||
               ','''|| pVard01 ||''' as vard_01 ';
               
               if  pVart02 != ''  THEN
                vSql = vSql || ','  || pVart02 ||'   as vart_02 '||
                          ','''|| pVard02 ||''' as vard_02 ';
               else 
                  vSql = vSql || ',null as vart_02'||
                                      ',null as vard_02';
               end if;
               
           if  pVart03 != '' THEN
                vSql = vSql || ','  || pVart03 ||'   as vart_03 '||
                          ','''|| pVard03 ||''' as vard_03 ';
               else 
                  vSql = vSql || ',null as vart_03'||
                                      ',null as vard_03';
               end if;
               
           if  pVart04 != '' THEN
                vSql = vSql || ','  || pVart04 ||'   as vart_04 '||
                          ','''|| pVard04 ||''' as vard_04 ';
               else 
                  vSql = vSql || ',null as vart_04'||
                                      ',null as vard_04';
               end if;
           if  pVart05 != ''  THEN
                vSql = vSql || ','  || pVart05 ||'   as vart_05 '||
                          ','''|| pVard05 ||''' as vard_05 ';
               else 
                  vSql = vSql || ',null as vart_05'||
                                      ',null as vard_05';
               end if;
               
               vSql = vSql||' 
                   ,sum(t1.ope_centro2_ord_dest_qnt_prev_obj)  as valor_01
                   ,sum(t1.ope_centro2_ord_dest_valor_unit_prev) as valor_02
                   ,sum(t1.ope_centro2_ord_dest_valor_total_prev) as valor_03
                   ,sum(t1.ope_centro2_ord_dest_qnt_obj) as valor_04
                   ,sum(t1.ope_centro2_ord_dest_valor_unit) as valor_05
                   ,sum(t1.ope_centro2_ord_dest_valor_total) as valor_06
               from vwope_centro2_ord_dest t1 
               where 1=1 ';
               
       
               
               
           if pParUnitId != '' then
               vSql = vSql || 'and ' || ' t1.ope_centro2_ord_dest_unit_id' || ' in(''' ||pParUnitId||''')';
           end if;
           
           if pParOrdDestId != '' then
               vSql = vSql || 'and ' || ' t1.ope_centro2_ord_dest_id' || ' in(''' ||pParOrdDestId||''')';
           end if;
           
           if pParOrdDestQntPrevObjIni != '' and pParOrdDestQntPrevObjFin != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_ord_dest_qnt_prev_obj'||' >= '''||pParOrdDestQntPrevObjIni||''''||
            ' and t1.ope_centro2_ord_dest_qnt_prev_obj'||' <= '''||pParOrdDestQntPrevObjFin||''''; 
           end if;
           
           if pParOrdDestVrUnitPrevIni != '' and pParOrdDestVrUnitPrevFin != '' then
                   vSql = vSql ||' and '||'t1.ope_centro2_ord_dest_valor_unit_prev'||' >= '''||pParOrdDestVrUnitPrevIni||''''||
            ' and t1.ope_centro2_ord_dest_valor_unit_prev'||' <= '''||pParOrdDestVrUnitPrevFin||''''; 
           end if;
           
           if pParOrdDestVrTotPrevIni != '' and 	pParOrdDestVrTotPrevFin != '' then
                   vSql = vSql ||' and '||'t1.ope_centro2_ord_dest_valor_total_prev'||' >= '''||pParOrdDestVrTotPrevIni||''''||
            ' and t1.ope_centro2_ord_dest_valor_total_prev'||' <= '''||pParOrdDestVrTotPrevFin||''''; 		
           end if;
       
           if pParOrdDestVrTotPrevIni != '' and 	pParOrdDestVrTotPrevFin != '' then
                   vSql = vSql ||' and '||'t1.ope_centro2_ord_dest_valor_total_prev'||' >= '''||pParOrdDestVrTotPrevIni||''''||
            ' and t1.ope_centro2_ord_dest_valor_total_prev'||' <= '''||pParOrdDestVrTotPrevFin||''''; 		
           end if;
           
               
           if pParOrdDestQntObjIni != '' and 	pParOrdDestQntObjFin != '' then
                   vSql = vSql ||' and '||'t1.ope_centro2_ord_dest_qnt_obj'||' >= '''||pParOrdDestQntObjIni||''''||
            ' and t1.ope_centro2_ord_dest_qnt_obj'||' <= '''||pParOrdDestQntObjFin||''''; 		
           end if;
           
           if pParOrdDestVrUnitIni != '' and 	pParOrdDestVrUnitFin != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_ord_dest_valor_unit'||' >= '''||pParOrdDestVrUnitIni||''''||
            ' and t1.ope_centro2_ord_dest_valor_unit'||' <= '''||pParOrdDestVrUnitFin||''''; 		
           end if;
               
           if pParOrdDestVrTotalIni != '' and 	pParOrdDestVrTotalFin != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_ord_dest_valor_total'||' >= '''||pParOrdDestVrTotalIni||''''||
            ' and t1.ope_centro2_ord_dest_valor_total'||' <= '''||pParOrdDestVrTotalFin||''''; 		
           end if;
           
           if pParOrdDataIniExecIni != '' and 	pParOrdDataIniExecFin != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_ord_data_ini_exec'||' >= '''||pParOrdDataIniExecIni||''''||
            ' and t1.ope_centro2_ord_data_ini_exec'||' <= '''||pParOrdDataIniExecFin||''''; 		
           end if;
           
           if pParOrdDataFinExecIni != '' and 	pParOrdDataFinExecFin != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_ord_data_fin_exec'||' >= '''||pParOrdDataFinExecIni||''''||
            ' and t1.ope_centro2_ord_data_fin_exec'||' <= '''||pParOrdDataFinExecFin||''''; 		
           end if;
           
           if pParOrdDataStatusIni != '' and 	pParOrdDataStatusFin != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_ord_data_status'||' >= '''||pParOrdDataStatusIni||''''||
            ' and t1.ope_centro2_ord_data_status'||' <= '''||pParOrdDataStatusFin||''''; 		
           end if;
           
           if pParOrdDataIniExecPrevIni != '' and 	pParOrdDataIniExecPrevFin != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_ord_data_ini_exec_prev'||' >= '''||pParOrdDataIniExecPrevIni||''''||
            ' and t1.ope_centro2_ord_data_ini_exec_prev'||' <= '''||pParOrdDataIniExecPrevFin||''''; 		
           end if;
           
           if pParOrdDataFinExecPrevIni != '' and 	pParOrdDataFinExecPrevFin != '' then
                vSql = vSql ||' and '||'t1.ope_centro2_ord_data_fin_exec_prev'||' >= '''||pParOrdDataFinExecPrevIni||''''||
            ' and t1.ope_centro2_ord_data_fin_exec_prev'||' <= '''||pParOrdDataFinExecPrevFin||''''; 		
           end if;	
           
           if pParCentro2Id != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_id' || ' in(''' ||pParCentro2Id||''')';
           end if;
           
           if pParCentro2Nome != '' then
                   vSql = vSql ||' and '||'t1.ope_centro2_nome'||' like'||'''%'||pParCentro2Nome||'%'' ';
           end if;
       
           if pParCentro2Ativo != '' then
                   vSql = vSql ||' and '||'t1.ope_centro2_ativo_desc'||' like'||'''%'||pParCentro2Ativo||'%'' ';
           end if;
           
           if pParCtbId != '' then
                   vSql = vSql || 'and ' || ' t1.ctb_id' || ' in(''' ||pParCtbId||''')';
           end if;
           
           if pParCtbNome != '' then
                   vSql = vSql ||' and '||'t1.ctb_nome'||' like'||'''%'||pParCtbNome||'%'' ';
           end if;
           
           if pParCtbAtivo != '' then
                   vSql = vSql ||' and '||'t1.ctb_ativo_desc'||' like'||'''%'||pParCtbAtivo||'%'' ';
           end if;
           
       
           if pParGerUmedidaId != '' then
                   vSql = vSql || 'and ' || ' t1.ger_umedida_id' || ' in(''' ||pParGerUmedidaId||''')';
           end if;
       
           if pParGerUmedidaNome != '' then
                   vSql = vSql ||' and '||'t1.ger_umedida_nome'||' like'||'''%'||pParGerUmedidaNome||'%'' ';
           end if;
           
           if pParGerUmedidaAtivo != '' then
                   vSql = vSql ||' and '||'t1.ger_umedida_ativo_desc'||' like'||'''%'||pParGerUmedidaAtivo||'%'' ';
           end if;
           
           if pParCentro1Id != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro1_id' || ' in(''' ||pParCentro1Id||''')';
           end if;	
           
           if pParCentro1Nome != '' then
                   vSql = vSql ||' and '||'t1.ope_centro1_nome_dest'||' like'||'''%'||pParCentro1Nome||'%'' ';
           end if;
       
           if pParCentro1Ativo != '' then
                   vSql = vSql ||' and '||'t1.ope_centro1_ativo_desc'||' like'||'''%'||pParCentro1Ativo||'%'' ';
           end if;
       
           if pParSubGrupoId != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro_subgrupo_id' || ' in(''' ||pParSubGrupoId||''')';
           end if;	
           
           if pParSubGrupoNome != '' then
                   vSql = vSql ||' and '||'t1.ope_centro_subgrupo_nome'||' like'||'''%'||pParSubGrupoNome||'%'' ';
           end if;
           
           if pParSubGrupoAtivo != '' then
                   vSql = vSql ||' and '||'t1.ope_centro_subgrupo_ativo_desc'||' like'||'''%'||pParSubGrupoAtivo||'%'' ';
           end if;
       
           if pParGrupoId != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro_grupo_id' || ' in(''' ||pParGrupoId||''')';
           end if;	
           
           if pParGrupoNome != '' then
                   vSql = vSql ||' and '||'t1.ope_centro_grupo_nome'||' like'||'''%'||pParGrupoNome||'%'' ';
           end if;
       
           if pParGrupoAtivo != '' then
                   vSql = vSql ||' and '||'t1.ope_centro_grupo_ativo_desc'||' like'||'''%'||pParGrupoAtivo||'%'' ';
           end if;
           
           if pParSubTipoId != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro_subtipo_id' || ' in(''' ||pParSubTipoId||''')';
           end if;	
           
           if pParSubTipoNome != '' then
                   vSql = vSql ||' and '||'t1.ope_centro_subtipo_nome'||' like'||'''%'||pParSubTipoNome||'%'' ';
           end if;	
       
           if pParTipoId != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro_tipo_id' || ' in(''' ||pParTipoId||''')';
           end if;	
           
           if pParTipoNome != '' then
                   vSql = vSql ||' and '||'t1.ope_centro_tipo_nome'||' like'||'''%'||pParTipoNome||'%'' ';
           end if;	
           
           if pParGerEmpresaId != '' then
                   vSql = vSql || 'and ' || ' t1.ger_empresa_id_ord' || ' in(''' ||pParGerEmpresaId||''')';
           end if;		
           
           if pParGerEmpresaNome != '' then
               vSql = vSql ||' and '||'t1.ger_empresa_nome_ord'||' like'||'''%'||pParGerEmpresaNome||'%'' ';
           end if;
           
           if pParGerEmpresaAtivo != '' then
               vSql = vSql ||' and '||'t1.ger_empresa_ativo_ord_desc'||' like'||'''%'||pParGerEmpresaAtivo||'%'' ';
           end if;
       
           if pParGerEmpresaDocCnpj != '' then
               vSql = vSql ||' and '||'t1.ger_empresa_doc_cnpj_ord'||' like'||'''%'||pParGerEmpresaDocCnpj||'%'' ';
           end if;
       
           if pParGerEmpresaDocCpf != '' then
               vSql = vSql ||' and '||'t1.ger_empresa_doc_cpf_ord'||' like'||'''%'||pParGerEmpresaDocCpf||'%'' ';
           end if;	
       
           if pParPeriodoId != '' then
                   vSql = vSql || 'and ' || ' t1.ope_periodo_id_ord' || ' in(''' ||pParPeriodoId||''')';
           end if;
           
           if pParPeriodoNome != '' then
               vSql = vSql||' and '||'t1.ope_periodo_nome_ord'||' like'||'''%'||pParPeriodoNome||'%'' ';
           end if;
           
           if pParPeriodoAtivo != '' then
               vSql = vSql||' and '||'t1.ope_periodo_ativo_ord_desc'||' like'||'''%'||pParPeriodoAtivo||'%'' ';
           end if;	
           
           if pParPeriodoDataIni != '' and pParPeriodoDataIniFin != '' then
                   vSql = vSql ||' and '||'t1.ope_periodo_data_ini_ord'||' >= '''||pParPeriodoDataIni||''''||
            ' and t1.ope_periodo_data_ini_ord'||' <= '''||pParPeriodoDataIniFin||''''; 
           end if;	
           
           if pParPeriodoDataFinIni != '' and pParPeriodoDataFin != '' then
                   vSql = vSql ||' and '||'t1.ope_periodo_data_fin_ord'||' >= '''||pParPeriodoDataFinIni||''''||
            ' and t1.ope_periodo_data_fin_ord'||' <= '''||pParPeriodoDataFin||''''; 
           end if;	
           
           if pParCentro2PessoaId != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_pessoa_id_ord' || ' in(''' ||pParCentro2PessoaId||''')';
           end if;
           
           if pParCentro2PessoaNome != '' then
               vSql = vSql||' and '||'t1.ope_centro2_nome_pessoa_ord'||' like'||'''%'||pParCentro2PessoaNome||'%'' ';
           end if;	
       
           if pParGerPessoaEnderecoId != '' then
                   vSql = vSql || 'and ' || ' t1.ger_pessoa_endereco_id_ord' || ' in(''' ||pParGerPessoaEnderecoId||''')';
           end if;
           
           if pParGerPessoaEnderecoAtivo != '' then
               vSql = vSql||' and '||'t1.ger_pessoa_endereco_ativo_ord_desc'||' like'||'''%'||pParGerPessoaEnderecoAtivo||'%'' ';
           end if;	
           
           if pParGerPessoaEnderecoTipo != '' then
               vSql = vSql||' and '||'t1.ger_pessoa_endereco_tipo_ord'||' like'||'''%'||pParGerPessoaEnderecoTipo||'%'' ';
           end if;		
           
           if pParGerPessoaEnderecoPadrao != '' then
               vSql = vSql||' and '||'t1.ger_pessoa_endereco_padrao_ord'||' like'||'''%'||pParGerPessoaEnderecoPadrao||'%'' ';
           end if;	
           
       
           if pParGerPessoaEnderecoLograd != '' then
               vSql = vSql||' and '||'t1.ger_pessoa_endereco_end_logradouro_ord'||' like'||'''%'||pParGerPessoaEnderecoLograd||'%'' ';
           end if;
           
           if pParGerPessoaEnderecoLogradNr != '' then
               vSql = vSql||' and '||'t1.ger_pessoa_endereco_end_logradouro_nr_ord'||' like'||'''%'||pParGerPessoaEnderecoLogradNr||'%'' ';
           end if;
           
           if pParGerPessoaEnderecoLogradBairro != '' then
               vSql = vSql||' and '||'t1.ger_pessoa_endereco_end_bairro_ord'||' like'||'''%'||pParGerPessoaEnderecoLogradBairro||'%'' ';
           end if;	
           
           if pParGerPessoaId != '' then
                   vSql = vSql || 'and ' || ' t1.ger_pessoa_id_ord' || ' in(''' ||pParGerPessoaId||''')';
           end if;	
           
           if pParGerPessoaNome != '' then
               vSql = vSql||' and '||'t1.ger_pessoa_nome_ord'||' like'||'''%'||pParGerPessoaNome||'%'' ';
           end if;
           
           if pParGerPessoaAtivo != '' then
                   vSql = vSql||' and '||'t1.ger_pessoa_ativo_ord_desc'||' like'||'''%'||pParGerPessoaAtivo||'%'' ';
           end if;	
           
           if pParGerPessoaDoc != '' then
                   vSql = vSql||' and '||'t1.ger_pessoa_doc_cpf_cnpj_ord'||' like'||'''%'||pParGerPessoaDoc||'%'' ';
           end if;	
       
           if pParOrdTipoId != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_ord_tipo_id_ord' || ' in(''' ||pParOrdTipoId||''')';
           end if;
       
           if pParOrdTipoNome != '' then
                   vSql = vSql||' and '||'t1.ope_centro2_ord_tipo_nome_ord'||' like'||'''%'||pParOrdTipoNome||'%'' ';
           end if;	
           
           if pParOrdCentro2Id != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_id_ord' || ' in(''' ||pParOrdCentro2Id||''')';
           end if;
           
           if pParOrdCentro2Nome != '' then
                   vSql = vSql||' and '||'t1.ope_centro2_nome_ord'||' like'||'''%'||pParOrdCentro2Nome||'%'' ';
           end if;	
           
           if pParOrdCentro2Ativo != '' then
                   vSql = vSql||' and '||'t1.ope_centro2_ativo_desc_ord'||' like'||'''%'||pParOrdCentro2Ativo||'%'' ';
           end if;
           
           if pParFrenteTrabalhoId != '' then
                   vSql = vSql || 'and ' || ' t1.ope_frente_trabalho_id_ord' || ' in(''' ||pParFrenteTrabalhoId||''')';
           end if;
           
           if pParFrenteTrabalhoNome != '' then
                   vSql = vSql||' and '||'t1.ope_frente_trabalho_nome_ord'||' like'||'''%'||pParFrenteTrabalhoNome||'%'' ';
           end if;	
           
           if pParFrenteTrabalhoAtivo != '' then
                   vSql = vSql||' and '||'t1.ope_frente_trabalho_ativo_desc'||' like'||'''%'||pParFrenteTrabalhoAtivo||'%'' ';
           end if;	
       
           if pParStatusId != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_ord_status_id_ord' || ' in(''' ||pParStatusId||''')';
           end if;
           
           if pParStatusNome != '' then
                   vSql = vSql||' and '||'t1.ope_centro2_ord_status_nome_ord'||' like'||'''%'||pParStatusNome||'%'' ';
           end if;	
           
           if pParStatusAtivo != '' then
                   vSql = vSql||' and '||'t1.ope_centro2_ord_status_ativo_ord_desc'||' like'||'''%'||pParStatusAtivo||'%'' ';
           end if;	
           
           if pParStatusTipo != '' then
                   vSql = vSql||' and '||'t1.ope_centro2_tipo_status_ord'||' like'||'''%'||pParStatusTipo||'%'' ';
           end if;
           
           if pParLogUserIns != '' then
                   vSql = vSql || 'and ' || ' t1.log_user_ins' || ' like '|| '''%' ||pParLogUserIns|| '%'' ';
           end if;
               
               if pParLogDateInsIni != '' and pParLogDateInsFin != '' then
                 vSql = vSql || ' and ' || 'CAST(t1.log_date_ins AS DATE)' || ' >= ''' || pParLogDateInsIni|| '''' || ' and  CAST(t1.log_date_ins AS DATE)' || ' <= ''' || pParLogDateInsFin || '''';
               end if;
               
               if pParLogUserUpd != '' then
                   vSql = vSql || 'and ' || ' t1.log_user_upd' || ' like '|| '''%' ||pParLogUserUpd|| '%'' ';
               end if;		
       
               if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then
                 vSql = vSql || ' and ' || 'CAST(t1.log_date_upd AS DATE)' || ' >= ''' || pParLogDateUpdIni|| '''' || ' and  CAST(t1.log_date_upd AS DATE)' || ' <= ''' || pParLogDateUpdFin || '''';
               end if;
           
           
                -- Group By
            -- ===================================
               vSql = vSql||' group by '|| pVart01;
       
               if  pVart02 != ''  THEN
                vSql = vSql||  ','|| pVart02;
               end if;
               
           if  pVart03 != ''  THEN
                vSql = vSql||  ','|| pVart03;
               end if;
               
           if  pVart04 != ''  THEN
                vSql = vSql||  ','|| pVart04;
               end if;
               
           if  pVart05 != ''  THEN
                vSql = vSql||  ','|| pVart05;
               end if;
               
            -- Order By
            -- ===================================
               vSql = vSql||' order by '|| pVart01;
       
               if  pVart02 != ''  THEN
                vSql = vSql||  ','|| pVart02;
               end if;
               
           if  pVart03 != ''  THEN
                vSql = vSql||  ','|| pVart03;
               end if;
               
           if  pVart04 != ''  THEN
                vSql = vSql||  ','|| pVart04;
               end if;
               
           if  pVart05 != ''  THEN
                vSql = vSql||  ','|| pVart05;
               end if;
           
           
           FOR r IN EXECUTE vSql loop
               ind_rel_id := pParIndRelId;
               ind_rel_par1 := vPar1;
               ind_rel_par2 := vPar2;
               ind_rel_par3 := vPar3;
               ind_rel_par4 := vPar4;
               vart_01 := r.vart_01;
               vard_01 := r.vard_01;
               vart_02 := r.vart_02;
               vard_02 := r.vard_02;
               vart_03 := r.vart_03;
               vard_03 := r.vard_03;
               vart_04 := r.vart_04;
               vard_04 := r.vard_04;
               vart_05 := r.vart_05;
               vard_05 := r.vard_05;
               valor_01 := r.valor_01;
               valor_02 := r.valor_02;
               valor_03 := r.valor_03;
               valor_04 := r.valor_04;
               valor_05 := r.valor_05;
               valor_06 := r.valor_06;
       
           RETURN NEXT;
           
           END loop;
       raise notice 'SQl:% ',vSql; 
       end;
       $BODY$
         LANGUAGE plpgsql VOLATILE;;
       
       
       
       -----------
       
       

       Drop FUNCTION IF EXISTS  fnreport0020;;

       CREATE OR REPLACE FUNCTION fnreport0020(
       pParUnitId varchar,
       pParIndRelId varchar,
       pVart01 varchar, 
       pVard01 varchar, 
       pVart02 varchar default null,
       pVard02 varchar default null,
       pVart03 varchar default null,
       pVard03 varchar default null,
       pVart04 varchar default null,
       pVard04 varchar default null,
       pVart05 varchar default null,
       pVard05 varchar default null,
       pParItemServId varchar default null,
       pParQntRendIni varchar default null,
       pParQntRendFin varchar default null,
       pParPercUtilIni varchar default null,
       pParPercUtilFin varchar default null,
       pParQntTotUtilIni varchar default null,
       pParQntTotUtilFin varchar default null,
       pParVrUnitUtilIni varchar default null,
       pParVrUnitUtilFin varchar default null,
       pParVrTotUtilIni varchar default null,
       pParVrTotUtilFin varchar default null,
       pParAtivOrdExec varchar default null,
       pParAtivOrdTipoExec varchar default null,
       pParItemServNome varchar default null,
       pParItemServAtivo varchar default null,
       pParItemServTipo varchar default null,
       pParAtivId varchar default null,
       pParAtivNome varchar default null,
       pParAtivAtivo varchar default null,
       pParCentro2OrdId varchar default null,
       pParCentro2OrdDtIniExec varchar default null,
       pParCentro2OrdDtIniExecFin varchar default null,
       pParCentro2OrdDtFinExecIni varchar default null,
       pParCentro2OrdDtFinExec varchar default null,
       pParCentro2OrdDtIniExecPrev varchar default null,
       pParCentro2OrdDtIniExecPrevFin varchar default null,
       pParCentro2OrdDtFinExecPrevIni varchar default null,
       pParCentro2OrdDtFinExecPrev varchar default null,
       pParCentro2OrdNr varchar default null,
       pParEmpresaOrdId varchar default null,
       pParEmpresaOrdNome varchar default null,
       pParEmpresaOrdAtivo varchar default null,
       pParEmpresaOrdCpf varchar default null,
       pParEmpresaOrdCnpj varchar default null,
       pParPeriodoOrdId varchar default null,
       pParPeriodoOrdNome varchar default null,
       pParPeriodoOrdAtivo varchar default null,
       pParPeriodoOrdDataIni varchar default null,
       pParPeriodoOrdDataIniFin varchar default null,
       pParPeriodoOrdDataFinIni varchar default null,
       pParPeriodoOrdDataFin varchar default null,
       pParCtbId varchar default null,
       pParCtbNome varchar default null,
       pParCtbAtivo varchar default null,
       pParGerPessoaId varchar default null,
       pParGerPessoaNome varchar default null,
       pParGerPessoaAtivo varchar default null,
       pParGerPessoaDoc varchar default null,
       pParPessoaEnderecoId varchar default null,
       pParPessoaEnderecoAtivo varchar default null,
       pParPessoaEnderecoTipo varchar default null,
       pParPessoaEnderecoPadrao varchar default null,
       pParPessoaEnderecoLograd varchar default null,
       pParPessoaEnderecoNr varchar default null,
       pParCentro2OrdTipoId varchar default null,
       pParCentro2OrdTipoNome varchar default null,
       pParCentro2OrdTipoAtivo varchar default null,
       pParCentro2Id varchar default null,
       pParCentro2Nome varchar default null,
       pParCentro2Ativo varchar default null,
       pParCentro1Id varchar default null,
       pParCentro1Nome varchar default null,
       pParCentro1Ativo varchar default null,
       pParFrentTrabId varchar default null,
       pParFrentTrabNome varchar default null,
       pParFrentTrabAtivo varchar default null,
       pParStatusId varchar default null,
       pParStatusNome varchar default null,
       pParStatusAtivo varchar default null,
       pParStatusTipo varchar default null,
       pParSubGrupoId varchar default null,
       pParSubGrupoNome varchar default null,
       pParSubGrupoAtivo varchar default null,
       pParGrupoId varchar default null,
       pParGrupoNome varchar default null,
       pParGrupoAtivo varchar default null,
       pParSubTipoId varchar default null,
       pParSubTipoNome varchar default null,
       pParTipoId varchar default null,
       pParTipoNome varchar default null,
       pParLogUserIns varchar default null,
       pParLogDateInsIni varchar default null,
       pParLogDateInsFin varchar default null,
       pParLogUserUpd varchar default null,
       pParLogDateUpdIni varchar default null,
       pParLogDateUpdFin varchar default null
       
       )
       
       RETURNS TABLE(
        ind_rel_id varchar,
        ind_rel_par1 varchar,
        ind_rel_par2 varchar,
        ind_rel_par3 varchar,
        ind_rel_par4 varchar,
        vart_01 varchar,
        vard_01 varchar,
        vart_02 varchar,
        vard_02 varchar,
        vart_03 varchar,
        vard_03 varchar,
        vart_04 varchar,
        vard_04 varchar,
        vart_05 varchar,
        vard_05 varchar,
        valor_01 numeric,
        valor_02 numeric,
        valor_03 numeric,
        valor_04 numeric,
        valor_05 numeric,
        valor_06 numeric,
        valor_07 numeric,
        valor_08 numeric,
        valor_09 numeric,
        valor_10 numeric) AS $BODY$
       declare
       vSql varchar;
       vPar1 varchar :='';
       vPar2 varchar :='';
       vPar3 varchar :='';
       vPar4 varchar :='';
       r record;
       
       begin
           
           
           if pParItemServId != '' then
                vPar1 := vPar1||'Item/Serviço ['||fnreport_sigla(pParUnitId,'vwope_centro2_ord_itemserv','ger_itemserv_nome','ope_centro2_ord_itemserv_id',''''||pParItemServId||'''')||'] '||chr(13)||chr(10);
           else
                vPar1 := vPar1||'Item/Serviço []'||chr(13)||chr(10);
           end if;
           
           if pParQntRendIni != '' and pParQntRendFin != '' then
               vPar1 := vPar1||'Qnt Rendimento / Dosagem de ['||pParQntRendIni||'] até ['||pParQntRendFin||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Qnt Rendimento / Dosagem de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParPercUtilIni != '' and pParPercUtilFin != '' then
               vPar1 := vPar1||'Percentual Utilização de ['||pParPercUtilIni||'] até ['||pParPercUtilFin||']'||chr(13)||chr(10);	
           else
               vPar1 := vPar1||'Percentual Utilização de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParQntTotUtilIni != '' and pParQntTotUtilFin != '' then
               vPar1 := vPar1||'Quantidade Total de Utilização de ['||pParQntTotUtilIni||'] até ['||pParQntTotUtilFin||']'||chr(13)||chr(10);	
           else
               vPar1 := vPar1||'Quantidade Total de Utilização de [] até []'||chr(13)||chr(10);	
           end if;
           
           if pParVrUnitUtilIni != '' and pParVrUnitUtilFin != '' then
                vPar1 := vPar1||'Valor Unitário de Utilização de ['||pParVrUnitUtilIni||'] até ['||pParVrUnitUtilFin||']'||chr(13)||chr(10);	
           else
                vPar1 := vPar1||'Valor Unitário Utilização de [] até []'||chr(13)||chr(10);		
           end if;
           
           if pParVrTotUtilIni != '' and pParVrTotUtilFin != '' then
                vPar1 := vPar1||'Valor Total Utilização de ['||pParVrTotUtilIni||'] até ['||pParVrTotUtilFin||']'||chr(13)||chr(10);	
           else
                vPar1 := vPar1||'Valor Total Utilização de [] até []'||chr(13)||chr(10);	
           end if;
       
           
           if pParAtivOrdExec != '' then
               vPar1 := vPar1||'Ordem Execução ['||pParAtivOrdExec||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Ordem Execução []'||chr(13)||chr(10);
           end if;
           
           if pParAtivOrdTipoExec != '' then
               vPar1 := vPar1||'Tipo Executor ['||pParAtivOrdTipoExec||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Tipo Executor []'||chr(13)||chr(10);
           end if;
           
           if pParItemServNome != '' then
               vPar1 := vPar1||'Nome Item/Serviço ['||pParItemServNome||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Nome Item/Serviço []'||chr(13)||chr(10);
           end if;
           
           if pParItemServAtivo != '' then
               vPar1 := vPar1||'Item/Serviço Ativo ['||pParItemServAtivo||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Item/Serviço Ativo []'||chr(13)||chr(10);
           end if;
           
           if pParItemServTipo != '' then
               vPar1 := vPar1||'Tipo Item/Serviço ['||pParItemServTipo||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Tipo Item/Serviço []'||chr(13)||chr(10);
           end if;
           
           if pParAtivId != '' then
                   vPar1 := vPar1||'Atividade ['||fnreport_sigla(pParUnitId,'ope_atividade','sigla_atividade','id',''''||pParAtivId||'''')||'] '||chr(13)||chr(10);
           else
                vPar1 := vPar1||'Atividade [] '||chr(13)||chr(10);	
           end if;
           
           if pParAtivNome != '' then
               vPar1 := vPar1||'Nome Atividade ['||pParAtivNome||'] '||chr(13)||chr(10);	
           else
               vPar1 := vPar1||'Nome Atividade [] '||chr(13)||chr(10);	
           end if;
           
           if pParAtivAtivo != '' then
               vPar1 := vPar1||'Atividade Ativo ['||pParAtivAtivo||'] '||chr(13)||chr(10);	
           else
               vPar1 := vPar1||'Atividade Ativo [] '||chr(13)||chr(10);	
           end if;
           
           if pParCentro2OrdDtIniExec != '' and pParCentro2OrdDtIniExecFin != '' then
               vPar1 := vPar1||'Data Inicial Execução de ['||pParCentro2OrdDtIniExec||'] até ['|| pParCentro2OrdDtIniExecFin||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Data Inicial Execução de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParCentro2OrdDtFinExecIni != '' and pParCentro2OrdDtFinExec != '' then
               vPar1 := vPar1||'Data Final Execução de ['||pParCentro2OrdDtFinExecIni||'] até ['|| pParCentro2OrdDtFinExec||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Data Final Execução de [] até []'||chr(13)||chr(10);
           end if;	
       
           if pParCentro2OrdDtIniExecPrev!= '' and pParCentro2OrdDtIniExecPrevFin != '' then
               vPar1 := vPar1||'Data Inicial Execução Prévia de ['||pParCentro2OrdDtIniExecPrev||'] até ['|| pParCentro2OrdDtIniExecPrevFin||']'||chr(13)||chr(10);	
           else
               vPar1 := vPar1||'Data Inicial Execução Prévia de [] até []'||chr(13)||chr(10);		
           end if;
           
           if pParCentro2OrdDtFinExecPrevIni != '' and pParCentro2OrdDtFinExecPrev != '' then
               vPar1 := vPar1||'Data Final Execução Prévia de ['||pParCentro2OrdDtFinExecPrevIni||'] até ['|| pParCentro2OrdDtFinExecPrev||']'||chr(13)||chr(10);		
           else
               vPar1 := vPar1||'Data Final Execução Prévia de [] até []'||chr(13)||chr(10);		
           end if;
           
           if pParCentro2OrdNr != '' then
               vPar1 := vPar1||'Nº Ordem ['||pParCentro2OrdNr||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Nº Ordem []'||chr(13)||chr(10);
           end if;
       
        raise notice ': Params 1%', vPar1;
        
           if pParEmpresaOrdId != '' then
                   vPar2 := vPar2||'Empresa ['||fnreport_sigla(pParUnitId,'ger_empresa','sigla_empresa','id',''''||pParEmpresaOrdId||'''')||'] '||chr(13)||chr(10);	
           else
                   vPar2 := vPar2||'Empresa []'||chr(13)||chr(10);		
           end if;
           
           if pParEmpresaOrdNome != '' then
                   vPar2 := vPar2||'Nome Empresa ['||pParEmpresaOrdNome||']'||chr(13)||chr(10);			
           else
                   vPar2 := vPar2||'Nome Empresa []'||chr(13)||chr(10);			
           end if;
       
           if pParEmpresaOrdAtivo != '' then
                   vPar2 := vPar2||'Empresa Ativo ['||pParEmpresaOrdAtivo||']'||chr(13)||chr(10);			
           else
                   vPar2 := vPar2||'Empresa Ativo []'||chr(13)||chr(10);			
           end if;
           
           if pParEmpresaOrdCpf != '' then
                   vPar2 := vPar2||'Empresa Cpf ['||pParEmpresaOrdCpf||']'||chr(13)||chr(10);			
           else
                   vPar2 := vPar2||'Empresa Cpf []'||chr(13)||chr(10);			
           end if;
           
           if pParEmpresaOrdCnpj != '' then
                   vPar2 := vPar2||'Empresa CNPJ ['||pParEmpresaOrdCnpj||']'||chr(13)||chr(10);			
           else
                   vPar2 := vPar2||'Empresa CNPJ []'||chr(13)||chr(10);			
           end if;	
       
           if pParPeriodoOrdId != '' then
                vPar2 := vPar2||'Período  ['||fnreport_sigla(pParUnitId,'ope_periodo','sigla_periodo','id',''''||pParPeriodoOrdId||'''')||'] '||chr(13)||chr(10);				
           else
                   vPar2 := vPar2||'Período []'||chr(13)||chr(10);			
           end if;	
       
           if pParPeriodoOrdNome != '' then
                   vPar2 := vPar2||'Nome Período ['||pParPeriodoOrdNome||']'||chr(13)||chr(10);			
           else
                   vPar2 := vPar2||'Nome Período []'||chr(13)||chr(10);			
           end if;	
       
           if pParPeriodoOrdAtivo != '' then
                   vPar2 := vPar2||'Período Ativo ['||pParPeriodoOrdAtivo||']'||chr(13)||chr(10);			
           else
                   vPar2 := vPar2||'Período Ativo []'||chr(13)||chr(10);			
           end if;	
           
           if pParPeriodoOrdDataIni != '' and pParPeriodoOrdDataIniFin != '' then
               vPar2 := vPar2||'Data Inicial do Período de ['||pParPeriodoOrdDataIni||'] até ['|| pParPeriodoOrdDataIniFin||']'||chr(13)||chr(10);	
           else
               vPar2 := vPar2||'Data Inicial do Período de [] até []'||chr(13)||chr(10);		
           end if;
           
           if pParPeriodoOrdDataFinIni != '' and pParPeriodoOrdDataFin != '' then
               vPar2 := vPar2||'Data Final do Período de ['||pParPeriodoOrdDataFinIni||'] até ['|| pParPeriodoOrdDataFin||']'||chr(13)||chr(10);		
           else
               vPar2 := vPar2||'Data Final do Período de [] até []'||chr(13)||chr(10);		
           end if;
           
           if pParCtbId != '' then
                   vPar2 := vPar2||'Componente Contábil ['||fnreport_sigla(pParUnitId,'ctb_comp','sigla_comp','id',''''||pParCtbId||'''')||'] '||chr(13)||chr(10);	
           else
                   vPar2 := vPar2||'Componente Contábil [] '||chr(13)||chr(10);	
           end if;
           
           if pParCtbNome != '' then
               vPar2 := vPar2||'Nome Componente Contábil ['||pParCtbNome||'] '||chr(13)||chr(10);	
           else
               vPar2 := vPar2||'Nome Componente Contábil [] '||chr(13)||chr(10);	
           end if;
       
           if pParCtbAtivo != '' then
                   vPar2 := vPar2||'Componente Contábil Ativo ['||pParCtbAtivo||'] '||chr(13)||chr(10);	
           else
                   vPar2 := vPar2||'Componente Contábil Ativo [] '||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaId != '' then
               vPar2 := vPar2||'Pessoa ['||fnreport_sigla(pParUnitId,'ger_pessoa','nome','id',''''||pParGerPessoaId||'''')||'] '||chr(13)||chr(10);		
           else
               vPar2 := vPar2||'Pessoa [] '||chr(13)||chr(10);			
           end if;
       
           if pParGerPessoaNome != '' then
               vPar2 := vPar2||'Nome Pessoa ['||pParGerPessoaNome||'] '||chr(13)||chr(10);			
           else
               vPar2 := vPar2||'Nome Pessoa [] '||chr(13)||chr(10);	
           end if;
       
           if pParGerPessoaAtivo != '' then
               vPar2 := vPar2||'Pessoa Ativo ['||pParGerPessoaAtivo||'] '||chr(13)||chr(10);				
           else
               vPar2 := vPar2||'Pessoa Ativo [] '||chr(13)||chr(10);	
           end if;
       
           if pParGerPessoaDoc != '' then
               vPar2 := vPar2||'Doc Pessoa ['||pParGerPessoaDoc||'] '||chr(13)||chr(10);	
           else
               vPar2 := vPar2||'Doc Pessoa [] '||chr(13)||chr(10);	
           end if;
       
           if pParPessoaEnderecoAtivo != '' then
               vPar3 := vPar3||'Pessoa Endereco Ativo ['||pParPessoaEnderecoAtivo||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Pessoa Endereco Ativo []'||chr(13)||chr(10);
           end if;
           
       
           if pParPessoaEnderecoTipo != '' then
               vPar3 := vPar3||'Pessoa Endereco Tipo ['||pParPessoaEnderecoTipo||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Pessoa Endereco Tipo []'||chr(13)||chr(10);	
           end if;
           
           if pParPessoaEnderecoPadrao != '' then
               vPar3 := vPar3||'Pessoa Endereco Padrão ['||pParPessoaEnderecoPadrao||']'||chr(13)||chr(10);	
           else
               vPar3 := vPar3||'Pessoa Endereco Padrão []'||chr(13)||chr(10);	
           end if;
           
           if pParPessoaEnderecoLograd !='' then
               vPar3 := vPar3||'Pessoa Endereco Logradouro ['||pParPessoaEnderecoLograd||']'||chr(13)||chr(10);	
           else
               vPar3 := vPar3||'Pessoa Endereco Logradouro []'||chr(13)||chr(10);	
           end if;
           
           if pParPessoaEnderecoNr !='' then
               vPar3 := vPar3||'Pessoa Nº Endereco ['||pParPessoaEnderecoNr||']'||chr(13)||chr(10);			
           else
               vPar3 := vPar3||'Pessoa Nº Endereco []'||chr(13)||chr(10);	
           end if;
           
       
       
           if pParCentro2OrdTipoId != '' then
               vPar3 := vPar3||'Tipo ['||fnreport_sigla(pParUnitId,'ope_centro2_ord_tipo','sigla_ord_tipo','id',''''||pParCentro2OrdTipoId||'''')||'] '||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Tipo [] '||chr(13)||chr(10);
           end if;
           
           if pParCentro2OrdTipoNome != '' then
               vPar3 := vPar3||'Nome Tipo ['||pParCentro2OrdTipoNome||'] '||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Nome Tipo [] '||chr(13)||chr(10);	
           end if;
           
           if pParCentro2OrdTipoAtivo != '' then
               vPar3 := vPar3||'Tipo Ativo ['||pParCentro2OrdTipoAtivo||'] '||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Tipo Ativo [] '||chr(13)||chr(10);	
           end if;
       
           if pParCentro2Id != '' then
                vPar3 := vPar3||'Centro 2 ['||fnreport_sigla(pParUnitId,'ope_centro2','sigla_centro2','id',''''||pParCentro2Id||'''')||'] '||chr(13)||chr(10);
           else
                vPar3 := vPar3||'Centro 2 [] '||chr(13)||chr(10);
           end if;
           
           if pParCentro2Nome != '' then
                vPar3 := vPar3||'Nome Centro 2 ['||pParCentro2Nome||'] '||chr(13)||chr(10);
           else
                vPar3 := vPar3||'Nome Centro 2 [] '||chr(13)||chr(10);	
           end if;
           
           if pParCentro2Ativo != '' then
                vPar3 := vPar3||'Centro 2 Ativo ['||pParCentro2Ativo||'] '||chr(13)||chr(10);	
           else
                vPar3 := vPar3||'Centro 2 Ativo [] '||chr(13)||chr(10);
           end if;
           
           if pParCentro1Id != '' then
                vPar3 := vPar3||'Centro 1 ['||fnreport_sigla(pParUnitId,'ope_centro1','sigla_centro1','id',''''||pParCentro1Id||'''')||'] '||chr(13)||chr(10);	
           else
               vPar3 := vPar3||'Centro 1 [] '||chr(13)||chr(10);
           end if;
       
           if pParCentro1Nome != '' then
               vPar3 := vPar3||'Nome Centro 1 ['||pParCentro1Nome||'] '||chr(13)||chr(10);	
           else
               vPar3 := vPar3||'Nome Centro 1 [] '||chr(13)||chr(10);
           end if;
           
           if pParCentro1Ativo != '' then
               vPar3 := vPar3||'Centro 1 Ativo ['||pParCentro1Ativo||'] '||chr(13)||chr(10);		
           else
               vPar3 := vPar3||'Centro 1 Ativo [] '||chr(13)||chr(10);	
           end if;
           
           if pParFrentTrabId != '' then
                vPar3 := vPar3||'Frente Trabalho ['||fnreport_sigla(pParUnitId,'ope_frente_trabalho','sigla_frente_trabalho','id',''''||pParFrentTrabId||'''')||'] '||chr(13)||chr(10);
           else
                vPar3 := vPar3||'Frente Trabalho [] '||chr(13)||chr(10);	
           end if;
           
           if pParFrentTrabNome != '' then
                vPar3 := vPar3||'Nome Frente Trabalho ['||pParFrentTrabNome||'] '||chr(13)||chr(10);		
           else
                vPar3 := vPar3||'Nome Frente Trabalho [] '||chr(13)||chr(10);		
           end if;
           
           
           if pParFrentTrabAtivo != '' then
                vPar3 := vPar3||'Frente Trabalho Ativo ['||pParFrentTrabAtivo||'] '||chr(13)||chr(10);	
           else
                vPar3 := vPar3||'Frente Trabalho Ativo [] '||chr(13)||chr(10);		
           end if;
           
           if pParStatusId != '' then
                vPar4 := vPar4||'Status ['||fnreport_sigla(pParUnitId,'ope_centro2_ord_status','sigla_ord_status','id',''''||pParStatusId||'''')||'] '||chr(13)||chr(10);	
           else
                vPar4 := vPar4||'Status [] '||chr(13)||chr(10);	
           end if;
           
           if pParStatusNome != '' then
                vPar4 := vPar4||'Nome Status ['||pParStatusNome||'] '||chr(13)||chr(10);
                
           else
               vPar4 := vPar4||'Nome Status [] '||chr(13)||chr(10);
           end if;
           
           
           if pParStatusAtivo != '' then
               vPar4 := vPar4||'Status Ativo ['||pParStatusAtivo||'] '||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Status Ativo [] '||chr(13)||chr(10);
           end if;
           
           if pParStatusTipo != '' then
               vPar4 := vPar4||'Tipo Status ['||pParStatusTipo||'] '||chr(13)||chr(10);	
           else
               vPar4 := vPar4||'Tipo Status [] '||chr(13)||chr(10);		
           end if;
           
           if pParSubGrupoId != '' then
                vPar4 := vPar4||'SubGrupo ['||fnreport_sigla(pParUnitId,'ope_centro_subgrupo','sigla_centro_subgrupo','id',''''||pParSubGrupoId||'''')||'] '||chr(13)||chr(10);
           else
                vPar4 := vPar4||'SubGrupo [] '||chr(13)||chr(10);	
           end if;
           
           if pParSubGrupoNome != '' then
                vPar4 := vPar4||'Nome SubGrupo ['||pParSubGrupoNome||'] '||chr(13)||chr(10);		
           else
                vPar4 := vPar4||'Nome SubGrupo [] '||chr(13)||chr(10);		
           end if;
           
           if pParSubGrupoAtivo != '' then
                vPar4 := vPar4||'SubGrupo Ativo ['||pParSubGrupoAtivo||'] '||chr(13)||chr(10);			
           else
                vPar4 := vPar4||'SubGrupo Ativo [] '||chr(13)||chr(10);	
           end if;
           
           if pParGrupoId != '' then
               vPar4 := vPar4||'Grupo ['||fnreport_sigla(pParUnitId,'ope_centro_grupo','sigla_centro_grupo','id',''''||pParGrupoId||'''')||'] '||chr(13)||chr(10);		 
           else
               vPar4 := vPar4||'Grupo [] '||chr(13)||chr(10);
           end if;
           
           if pParGrupoNome != '' then
               vPar4 := vPar4||'Nome Grupo ['||pParGrupoNome||'] '||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Nome Grupo [] '||chr(13)||chr(10);
           end if;
           
           if pParGrupoAtivo != '' then
               vPar4 := vPar4||'Grupo Ativo ['||pParGrupoAtivo||'] '||chr(13)||chr(10);	
           else
               vPar4 := vPar4||'Grupo Ativo [] '||chr(13)||chr(10);	
           end if;
           
           if pParSubTipoId != '' then
               vPar4 := vPar4||'SubTipo ['||fnreport_sigla(pParUnitId,'ope_centro_subtipo','nome','id',''''||pParSubTipoId||'''')||'] '||chr(13)||chr(10);		 		
           else
               vPar4 := vPar4||'SubTipo [] '||chr(13)||chr(10);		 			
           end if;
           
           if pParSubTipoNome != '' then
               vPar4 := vPar4||'Nome SubTipo ['||pParSubTipoNome||'] '||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Nome SubTipo [] '||chr(13)||chr(10);	
           end if;
           
           if pParTipoId != '' then
               vPar4 := vPar4||'Tipo ['||fnreport_sigla(pParUnitId,'ope_centro_tipo','nome','id',''''||pParTipoId||'''')||'] '||chr(13)||chr(10);		 			
           else
               vPar4 := vPar4||'Tipo [] '||chr(13)||chr(10);
           end if;
           
           if pParTipoNome != '' then
               vPar4 := vPar4||'Nome Tipo ['||pParTipoNome||'] '||chr(13)||chr(10);	
           else
               vPar4 := vPar4||'Nome Tipo [] '||chr(13)||chr(10);	
           end if;
           
           if pParLogUserIns != '' then
               vPar4 := vPar4||'Log Usuario Inserção ['||pParLogUserIns||']'||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Log Usuario Inserção []'||chr(13)||chr(10);
           end if;
       
           if pParLogUserUpd != '' then
               vPar4 := vPar4||'Log Usuario Alteração ['||pParLogUserUpd||']'||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Log Usuario Alteração []'||chr(13)||chr(10);
           end if;
       
           if pParLogDateInsIni != '' and pParLogDateInsFin != '' then
               vPar4 := vPar4||'Data Inserção de ['||pParLogDateInsIni||'] até ['||pParLogDateInsFin||']'||chr(13)||chr(10);
           else
                       vPar4 := vPar4||'Data Inserção de [] até []'||chr(13)||chr(10);
           end if;
       
           if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then
               vPar4 := vPar4||'Data Alteração de ['||pParLogDateUpdIni||'] até ['||pParLogDateUpdFin||']'||chr(13)||chr(10);
           else
                   vPar4 := vPar4||'Data Alteração de [] até []'||chr(13)||chr(10);
           end if;
           
           
               vSql = 'select
           '  || pVart01 ||'   as vart_01 '||
               ','''|| pVard01 ||''' as vard_01 ';
               
               if  pVart02 != ''  THEN
                vSql = vSql || ','  || pVart02 ||'   as vart_02 '||
                          ','''|| pVard02 ||''' as vard_02 ';
               else 
                  vSql = vSql || ',null as vart_02'||
                                      ',null as vard_02';
               end if;
               
           if  pVart03 != '' THEN
                vSql = vSql || ','  || pVart03 ||'   as vart_03 '||
                          ','''|| pVard03 ||''' as vard_03 ';
               else 
                  vSql = vSql || ',null as vart_03'||
                                      ',null as vard_03';
               end if;
               
           if  pVart04 != '' THEN
                vSql = vSql || ','  || pVart04 ||'   as vart_04 '||
                          ','''|| pVard04 ||''' as vard_04 ';
               else 
                  vSql = vSql || ',null as vart_04'||
                                      ',null as vard_04';
               end if;
           if  pVart05 != ''  THEN
                vSql = vSql || ','  || pVart05 ||'   as vart_05 '||
                          ','''|| pVard05 ||''' as vard_05 ';
               else 
                  vSql = vSql || ',null as vart_05'||
                                      ',null as vard_05';
               end if;
               
               vSql = vSql||' 
               ,sum(t1.ope_centro2_ord_itemserv_qnt_rend) as valor_01
               ,sum(t1.ope_centro2_ord_itemserv_perc_util) as valor_02
               ,sum(t1.ope_centro2_ord_itemserv_qnt_total_util) as valor_03
               ,sum(t1.ope_centro2_ord_itemserv_valor_unit_util) as valor_04
               ,sum(t1.ope_centro2_ord_itemserv_valor_total_util) as valor_05
               from vwope_centro2_ord_itemserv t1 where 1=1 ';
               
               if pParUnitId != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_ord_itemserv_unit_id' || ' in(''' ||pParUnitId||''')';
               end if;
           
           
           if pParItemServId != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_ord_itemserv_id' || ' in(''' ||pParItemServId||''')';		
           end if;
           
           if pParQntRendIni != '' and pParQntRendFin != '' then
               vSql = vSql || ' and ' || 't1.ope_centro2_ord_itemserv_qnt_rend ' || ' >= ''' || pParQntRendIni|| '''' || ' and   t1.ope_centro2_ord_itemserv_qnt_rend ' || ' <= ''' || pParQntRendFin|| '''';	
           end if;
       
           if pParPercUtilIni != '' and pParPercUtilFin != '' then
               vSql = vSql || ' and ' || 't1.ope_centro2_ord_itemserv_perc_util ' || ' >= ''' || pParPercUtilIni|| '''' || ' and  t1.ope_centro2_ord_itemserv_perc_util ' || ' <= ''' || pParPercUtilFin|| '''';	
           end if;
       
           if pParQntTotUtilIni != '' and pParQntTotUtilFin != '' then
               vSql = vSql || ' and ' ||'t1.ope_centro2_ord_itemserv_qnt_total_util ' || ' >= ''' || pParQntTotUtilIni|| '''' || ' and  t1.ope_centro2_ord_itemserv_qnt_total_util ' || ' <= ''' || pParQntTotUtilFin|| '''';	
           end if;
           
           if pParVrUnitUtilIni != '' and pParVrUnitUtilFin != '' then
               vSql = vSql || ' and ' ||'t1.ope_centro2_ord_itemserv_valor_unit_util ' || ' >= ''' || pParVrUnitUtilIni|| '''' || ' and  t1.ope_centro2_ord_itemserv_valor_unit_util ' || ' <= ''' || pParVrUnitUtilFin|| '''';	
           end if;
       
           if pParVrTotUtilIni != '' and pParVrTotUtilFin != '' then
               vSql = vSql || ' and ' ||'t1.ope_centro2_ord_itemserv_valor_total_util ' || ' >= ''' || pParVrTotUtilIni|| '''' || ' and  t1.ope_centro2_ord_itemserv_valor_total_util ' || ' <= ''' || pParVrTotUtilFin|| '''';	
           end if;	
           
           if pParAtivOrdExec != '' then 
               vSql = vSql ||' and '||'t1.ope_centro2_ord_ativ_ordem_exec'||' like '||'''%'||pParAtivOrdExec||'%'' ';
           end if;
           
           if pParAtivOrdTipoExec != '' then 
               vSql = vSql ||' and '||'t1.ope_centro2_ord_tipo_executor'||' like '||'''%'||pParAtivOrdTipoExec||'%'' ';
           end if;
           
           
           if pParItemServNome != '' then
               vSql = vSql ||' and '||'t1.ger_itemserv_nome'||' like '||'''%'||pParItemServNome||'%'' ';
           end if;
           
           if pParItemServAtivo != '' then
               vSql = vSql ||' and '||'t1.ger_itemserv_ativo'||' like '||'''%'||pParItemServAtivo||'%'' ';
           end if;
           
           if pParItemServTipo != '' then
               vSql = vSql ||' and '||'t1.ger_itemserv_tipo_desc'||' like '||'''%'||pParItemServTipo||'%'' ';
           end if;
           
           if pParAtivId != '' then
                vSql = vSql || 'and ' || ' t1.ope_atividade_id' || ' in(''' ||pParAtivId||''')';	
           end if;
           
           if pParAtivNome != '' then
               vSql = vSql ||' and '||'t1.ope_atividade_nome'||' like '||'''%'||pParAtivNome||'%'' ';
           end if;
           
           if pParAtivAtivo != '' then
               vSql = vSql ||' and '||'t1.ope_atividade_ativo_desc'||' like '||'''%'||pParAtivAtivo||'%'' ';
           end if;	
           
           if pParCentro2OrdId != '' then
                vSql = vSql || 'and ' || ' t1.ope_centro2_ord_id' || ' in(''' ||pParCentro2OrdId||''')';
           end if;
           
           if pParCentro2OrdDtIniExec != '' and pParCentro2OrdDtIniExecFin != '' then
               vSql = vSql || ' and ' ||'CAST(t1.ope_centro2_ord_data_ini_exec AS DATE)' || ' >= ''' || pParCentro2OrdDtIniExec|| '''' || ' and  CAST(t1.ope_centro2_ord_data_ini_exec AS DATE)' || ' <= ''' || pParCentro2OrdDtIniExecFin|| '''';		
           end if;
       
           if pParCentro2OrdDtFinExecIni != '' and pParCentro2OrdDtFinExec != '' then
               vSql = vSql || ' and ' ||'CAST(t1.ope_centro2_ord_data_fin_exec AS DATE)' || ' >= ''' || pParCentro2OrdDtFinExecIni|| '''' || ' and  CAST(t1.ope_centro2_ord_data_fin_exec AS DATE)' || ' <= ''' || pParCentro2OrdDtFinExec|| '''';		
           end if;
       
           if pParCentro2OrdDtIniExecPrev != '' and pParCentro2OrdDtIniExecPrevFin != '' then
               vSql = vSql || ' and ' ||'CAST(t1.ope_centro2_ord_data_ini_exec_prev AS DATE)' || ' >= ''' || pParCentro2OrdDtIniExecPrev|| '''' || ' and  CAST(t1.ope_centro2_ord_data_ini_exec_prev AS DATE)' || ' <= ''' || pParCentro2OrdDtIniExecPrevFin|| '''';
           end if;
           
           if pParCentro2OrdDtFinExecPrevIni != '' and pParCentro2OrdDtFinExecPrev != '' then
               vSql = vSql || ' and ' ||'CAST(t1.ope_centro2_ord_data_fin_exec_prev AS DATE)' || ' >= ''' || pParCentro2OrdDtFinExecPrevIni|| '''' || ' and  CAST(t1.ope_centro2_ord_data_fin_exec_prev AS DATE)' || ' <= ''' || pParCentro2OrdDtFinExecPrev|| '''';	
           end if;
       
       
           if pParCentro2OrdNr != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_ord_numero_ord'||' like '||'''%'||pParCentro2OrdNr||'%'' ';	
           end if;
       
           if pParEmpresaOrdId != '' then
                vSql = vSql || 'and ' || ' t1.ger_empresa_id_ord' || ' in(''' ||pParEmpresaOrdId||''')';	
           end if;
           
           if pParEmpresaOrdNome != '' then
               vSql = vSql ||' and '||'t1.ger_empresa_nome_ord'||' like '||'''%'||pParEmpresaOrdNome||'%'' ';	
           end if;	
           
           if pParEmpresaOrdAtivo != '' then
               vSql = vSql ||' and '||'t1.ger_empresa_ativo_desc_ord'||' like '||'''%'||pParEmpresaOrdAtivo||'%'' ';	
           end if;		
           
           if pParEmpresaOrdCpf != '' then
               vSql = vSql ||' and '||'t1.ger_empresa_doc_cpf_ord'||' like '||'''%'||pParEmpresaOrdCpf||'%'' ';	
           end if;					
           
           if pParEmpresaOrdCnpj != '' then
               vSql = vSql ||' and '||'t1.ger_empresa_cnpj_ord'||' like '||'''%'||pParEmpresaOrdCnpj||'%'' ';	
           end if;
       
           if pParPeriodoOrdId != '' then
                vSql = vSql || 'and ' || ' t1.ope_periodo_id_ord' || ' in(''' ||pParPeriodoOrdId||''')';		
           end if;
       
           if pParPeriodoOrdNome != '' then
               vSql = vSql ||' and '||'t1.ope_periodo_nome_ord'||' like '||'''%'||pParPeriodoOrdNome||'%'' ';	
           end if;
       
           if pParPeriodoOrdAtivo != '' then
               vSql = vSql ||' and '||'t1.ope_periodo_ativo_ord_desc'||' like '||'''%'||pParPeriodoOrdAtivo||'%'' ';	
           end if;
       
           if pParPeriodoOrdDataIni != '' and pParPeriodoOrdDataIniFin != '' then
               vSql = vSql || ' and ' ||'CAST(t1.ope_periodo_data_ini_ord AS DATE)' || ' >= ''' || pParPeriodoOrdDataIni|| '''' || ' and CAST(t1.ope_periodo_data_ini_ord AS DATE)' || ' <= ''' || pParPeriodoOrdDataIniFin|| '''';	
           end if;
       
           if pParPeriodoOrdDataFinIni != '' and pParPeriodoOrdDataFin != '' then
               vSql = vSql || ' and ' ||'CAST(t1.ope_periodo_data_fin_ord AS DATE)' || ' >= ''' || pParPeriodoOrdDataFinIni|| '''' || ' and CAST(t1.ope_periodo_data_fin_ord AS DATE)' || ' <= ''' || pParPeriodoOrdDataFin|| '''';	
           end if;
           
           
           if pParCtbId != '' then
                vSql = vSql || 'and ' || ' t1.ctb_id' || ' in(''' ||pParCtbId||''')';
           end if;
       
           if pParCtbNome != '' then
               vSql = vSql ||' and '||'t1.ctb_nome'||' like '||'''%'||pParCtbNome||'%'' ';		
           end if;
       
           if pParCtbAtivo != '' then
               vSql = vSql ||' and '||'t1.ctb_ativo_desc'||' like '||'''%'||pParCtbAtivo||'%'' ';		
           end if;
           
           if pParGerPessoaId != '' then
                vSql = vSql || 'and ' || 't1.ger_pessoa_id_ord' || ' in(''' ||pParGerPessoaId||''')';
           end if;
       
           if pParGerPessoaNome != '' then
               vSql = vSql ||' and '||'t1.ger_pessoa_nome_ord'||' like '||'''%'||pParGerPessoaNome||'%'' ';		
           end if;
           
           if pParGerPessoaAtivo != '' then
               vSql = vSql ||' and '||'t1.ger_pessoa_ativo_desc_ord'||' like '||'''%'||pParGerPessoaAtivo||'%'' ';		
           end if;
       
           if pParGerPessoaDoc != '' then
               vSql = vSql ||' and '||'t1.ger_pessoa_doc_cpf_cnpj_ord'||' like '||'''%'||pParGerPessoaDoc||'%'' ';		
           end if;
           
           if pParPessoaEnderecoId != '' then
                vSql = vSql || 'and ' || ' t1.ger_pessoa_endereco_id_ord' || ' in(''' ||pParPessoaEnderecoId||''')';
           end if;
           
           if pParPessoaEnderecoAtivo != '' then
               vSql = vSql ||' and '||'t1.ger_pessoa_endereco_ativo_ord_desc'||' like '||'''%'||pParPessoaEnderecoAtivo||'%'' ';				
           end if;
           
           if pParPessoaEnderecoTipo != '' then
               vSql = vSql ||' and '||'t1.ger_pessoa_endereco_tipo_ord'||' like '||'''%'||pParPessoaEnderecoTipo||'%'' ';				
           end if;	
           
           if pParPessoaEnderecoPadrao != '' then
               vSql = vSql ||' and '||'t1.ger_pessoa_endereco_padrao_ord'||' like '||'''%'||pParPessoaEnderecoPadrao||'%'' ';				
           end if;		
           
       
           if pParPessoaEnderecoLograd != '' then
               vSql = vSql ||' and '||'t1.ger_pessoa_endereco_logradouro_ord'||' like '||'''%'||pParPessoaEnderecoLograd||'%'' ';				
           end if;		
           
           if pParPessoaEnderecoNr != '' then
               vSql = vSql ||' and '||'t1.ger_pessoa_endereco_logradouro_nr_ord'||' like '||'''%'||pParPessoaEnderecoNr||'%'' ';				
           end if;	
           
           
           if pParCentro2OrdTipoId != '' then
                vSql = vSql || 'and ' || ' t1.ope_centro2_ord_tipo_id' || ' in(''' ||pParCentro2OrdTipoId||''')';
           end if;
           
       
           if pParCentro2OrdTipoNome != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_ord_tipo_nome'||' like '||'''%'||pParCentro2OrdTipoNome||'%'' ';				
           end if;	
       
           if pParCentro2OrdTipoAtivo != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_ord_tipo_ativo_desc'||' like '||'''%'||pParCentro2OrdTipoAtivo||'%'' ';				
           end if;	
           
           if pParCentro2Id != '' then
                vSql = vSql || 'and ' || ' t1.ope_centro2_id_ord' || ' in(''' ||pParCentro2Id||''')';
           end if;
           if pParCentro2Nome != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_nome_ord'||' like '||'''%'||pParCentro2Nome||'%'' ';				
           end if;
       
           if pParCentro2Ativo != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_ativo_ord_desc'||' like '||'''%'||pParCentro2Ativo||'%'' ';				
           end if;
       
           if pParCentro1Id != '' then
                vSql = vSql || 'and ' || ' t1.ope_centro1_id_ord' || ' in(''' ||pParCentro1Id||''')';
           end if;
       
           if pParCentro1Nome != '' then
               vSql = vSql ||' and '||'t1.ope_centro1_nome_ord'||' like '||'''%'||pParCentro1Nome||'%'' ';				
           end if;
       
           if pParCentro1Ativo != '' then
               vSql = vSql ||' and '||'t1.ope_centro1_ativo_ord_desc'||' like '||'''%'||pParCentro1Ativo||'%'' ';				
           end if;
           
           if pParFrentTrabId != '' then
                vSql = vSql || 'and ' || ' t1.ope_frente_trabalho_id_ord' || ' in(''' ||pParFrentTrabId||''')';
           end if;	
           
           if pParFrentTrabNome != '' then
               vSql = vSql ||' and '||'t1.ope_frente_trabalho_nome_ord'||' like '||'''%'||pParFrentTrabNome||'%'' ';	
           end if;
           
           if pParFrentTrabAtivo != '' then
               vSql = vSql ||' and '||'t1.ope_frente_trabalho_ativo_desc_ord'||' like '||'''%'||pParFrentTrabAtivo||'%'' ';	
           end if;	
           
           if pParStatusId != '' then
                vSql = vSql || 'and ' || ' t1.ope_centro2_ord_status_id' || ' in(''' ||pParStatusId||''')';
           end if;
           
           if pParStatusNome != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_ord_status_nome'||' like '||'''%'||pParStatusNome||'%'' ';	
           end if;
       
           if pParStatusAtivo != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_ord_status_ativo_desc'||' like '||'''%'||pParStatusAtivo||'%'' ';	
           end if;
           
           if pParStatusTipo != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_ord_status_tipo_status'||' like '||'''%'||pParStatusTipo||'%'' ';	
           end if;	
           
           if pParSubGrupoId != '' then
                vSql = vSql || 'and ' || ' t1.ope_centro_subgrupo_id_ord' || ' in(''' ||pParSubGrupoId||''')';
           end if;	
           
           if pParSubGrupoNome != '' then
               vSql = vSql ||' and '||'t1.ope_centro_subgrupo_nome_ord'||' like '||'''%'||pParSubGrupoNome||'%'' ';	
           end if;	
       
           if pParSubGrupoAtivo != '' then
               vSql = vSql ||' and '||'t1.ope_centro_subgrupo_ativo_desc_ord'||' like '||'''%'||pParSubGrupoAtivo||'%'' ';	
           end if;
           
           if pParGrupoId != '' then
                vSql = vSql || 'and ' || ' t1.ope_centro_grupo_id_ord' || ' in(''' ||pParGrupoId||''')';
           end if;	
           
           if pParGrupoNome != '' then
               vSql = vSql ||' and '||'t1.ope_centro_grupo_nome_ord'||' like '||'''%'||pParGrupoNome||'%'' ';	
           end if;	
           
           if pParGrupoAtivo != '' then
               vSql = vSql ||' and '||'t1.ope_centro_grupo_ativo_desc_ord'||' like '||'''%'||pParGrupoAtivo||'%'' ';	
           end if;
       
           if pParSubTipoId != '' then
                vSql = vSql || 'and ' || ' t1.ope_centro_subtipo_id' || ' in(''' ||pParSubTipoId||''')';
           end if;
           
           if pParSubTipoNome != '' then
               vSql = vSql ||' and '||'t1.ope_centro_subtipo_nome'||' like '||'''%'||pParSubTipoNome||'%'' ';	
           end if;
           
           if pParTipoId != '' then
                vSql = vSql || 'and ' || ' t1.ope_centro_tipo_id' || ' in(''' ||pParTipoId||''')';
           end if;	
           
           if pParTipoNome != '' then
               vSql = vSql ||' and '||'t1.ope_centro_tipo_nome'||' like '||'''%'||pParTipoNome||'%'' ';	
           end if;
       
           if pParLogUserIns != '' then
                   vSql = vSql || 'and ' || ' t1.log_user_ins' || ' like '|| '''%' ||pParLogUserIns|| '%'' ';
           end if;
               
           if pParLogDateInsIni != '' and pParLogDateInsFin != '' then
             vSql = vSql || ' and ' || 'CAST(t1.log_date_ins AS DATE)' || ' >= ''' || pParLogDateInsIni|| '''' || ' and  CAST(t1.log_date_ins AS DATE)' || ' <= ''' || pParLogDateInsFin || '''';
           end if;
           
           if pParLogUserUpd != '' then
               vSql = vSql || 'and ' || ' t1.log_user_upd' || ' like '|| '''%' ||pParLogUserUpd|| '%'' ';
           end if;		
       
           if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then
             vSql = vSql || ' and ' || 'CAST(t1.log_date_upd AS DATE)' || ' >= ''' || pParLogDateUpdIni|| '''' || ' and  CAST(t1.log_date_upd AS DATE)' || ' <= ''' || pParLogDateUpdFin || '''';
           end if;
               
               
                    -- Group By
            -- ===================================
               vSql = vSql||' group by '|| pVart01;
       
               if  pVart02 != ''  THEN
                vSql = vSql||  ','|| pVart02;
               end if;
               
           if  pVart03 != ''  THEN
                vSql = vSql||  ','|| pVart03;
               end if;
               
           if  pVart04 != ''  THEN
                vSql = vSql||  ','|| pVart04;
               end if;
               
           if  pVart05 != ''  THEN
                vSql = vSql||  ','|| pVart05;
               end if;
               
            -- Order By
            -- ===================================
               vSql = vSql||' order by '|| pVart01;
       
               if  pVart02 != ''  THEN
                vSql = vSql||  ','|| pVart02;
               end if;
               
           if  pVart03 != ''  THEN
                vSql = vSql||  ','|| pVart03;
               end if;
               
           if  pVart04 != ''  THEN
                vSql = vSql||  ','|| pVart04;
               end if;
               
           if  pVart05 != ''  THEN
                vSql = vSql||  ','|| pVart05;
               end if;
               
           
           FOR r IN EXECUTE vSql loop
               ind_rel_id := pParIndRelId;
               ind_rel_par1 := vPar1;
               ind_rel_par2 := vPar2;
               ind_rel_par3 := vPar3;
               ind_rel_par4 := vPar4;
               vart_01 := r.vart_01;
               vard_01 := r.vard_01;
               vart_02 := r.vart_02;
               vard_02 := r.vard_02;
               vart_03 := r.vart_03;
               vard_03 := r.vard_03;
               vart_04 := r.vart_04;
               vard_04 := r.vard_04;
               vart_05 := r.vart_05;
               vard_05 := r.vard_05;
               valor_01 := r.valor_01;
               valor_02 := r.valor_02;
               valor_03 := r.valor_03;
               valor_04 := r.valor_04;
               valor_05 := r.valor_05;
       
           RETURN NEXT;
           
           END loop;
               
               
               
       end;
       $BODY$
         LANGUAGE plpgsql VOLATILE;;
       
       
       
       -----------
       
       

       DROP FUNCTION IF EXISTS fnreport0021;;

       CREATE OR REPLACE FUNCTION fnreport0021(
       pParUnitId varchar,
       pParIndRelId varchar,
       pVart01 varchar, 
       pVard01 varchar, 
       pVart02 varchar default null,
       pVard02 varchar default null,
       pVart03 varchar default null,
       pVard03 varchar default null,
       pVart04 varchar default null,
       pVard04 varchar default null,
       pVart05 varchar default null,
       pVard05 varchar default null,
       pParOrdRecIId varchar default null,
       pParOrdRecQntRendIni varchar default null,
       pParOrdRecQntRendFin varchar default null,
       pParOrdRecPercUtilIni varchar default null,
       pParOrdRecPercUtilFin varchar default null,
       pParOrdRecQntTotUtilIni varchar default null,
       pParOrdRecQntTotUtilFin varchar default null,
       pParOrdRecVrUnitUtilIni varchar default null,
       pParOrdRecVrUnitUtilFin varchar default null,
       pParOrdRecVrTotUtilIni varchar default null,
       pParOrdRecVrTotUtilFin varchar default null,
       pParCentro1Id varchar default null,
       pParCentro1Nome varchar default null,
       pParCentro1Ativo varchar default null,
       pParCentro2Id varchar default null,
       pParCentro2Nome varchar default null,
       pParCentro2Ativo varchar default null,
       pParCtbId varchar default null,
       pParCtbNome varchar default null,
       pParCtbAtivo varchar default null,
       pParPessoaEnderecoId varchar default null,
       pParPessoaEnderecoAtivo varchar default null,
       pParPessoaEnderecoTipo varchar default null,
       pParPessoaEnderecoPadrao varchar default null,
       pParPessoaEnderecoLograd varchar default null,
       pParPessoaEnderecoNr varchar default null,
       pParCentro1Imp01Id varchar default null,
       pParCentro1Imp01Nome varchar default null,
       pParCentro1Imp01Ativo varchar default null,
       pParCentro2Imp01Id varchar default null,
       pParCentro2Imp01Nome varchar default null,
       pParCentro2Imp01Ativo varchar default null,
       pParSubTipoId varchar default null,
       pParSubTipoNome varchar default null,
       pParTipoId varchar default null,
       pParTipoNome varchar default null,
       pParSubGrupoId varchar default null,
       pParSubGrupoNome varchar default null,
       pParSubGrupoAtivo varchar default null,
       pParGrupoId varchar default null,
       pParGrupoNome varchar default null,
       pParGrupoAtivo varchar default null,
       pParCentro2OrdId varchar default null,
       pParCentro2OrdDtIniExec varchar default null,
       pParCentro2OrdDtIniExecFin varchar default null,
       pParCentro2OrdDtFinExecIni varchar default null,
       pParCentro2OrdDtFinExec varchar default null,
       pParCentro2OrdDtIniExecPrev varchar default null,
       pParCentro2OrdDtIniExecPrevFin varchar default null,
       pParCentro2OrdDtFinExecPrevIni varchar default null,
       pParCentro2OrdDtFinExecPrev varchar default null,
       pParCentro2OrdNr varchar default null,
       pParEmpresaOrdId varchar default null,
       pParEmpresaOrdNome varchar default null,
       pParEmpresaOrdAtivo varchar default null,
       pParEmpresaOrdCpf varchar default null,
       pParEmpresaOrdCnpj varchar default null,
       pParPeriodoOrdId varchar default null,
       pParPeriodoOrdNome varchar default null,
       pParPeriodoOrdAtivo varchar default null,
       pParPeriodoOrdDataIni varchar default null,
       pParPeriodoOrdDataIniFin varchar default null,
       pParPeriodoOrdDataFinIni varchar default null,
       pParPeriodoOrdDataFin varchar default null,
       pParGerPessoaId varchar default null,
       pParGerPessoaNome varchar default null,
       pParGerPessoaAtivo varchar default null,
       pParGerPessoaDoc varchar default null,
       pParCentro2OrdTipoId varchar default null,
       pParCentro2OrdTipoNome varchar default null,
       pParCentro2OrdTipoAtivo varchar default null,
       pParFrentTrabId varchar default null,
       pParFrentTrabNome varchar default null,
       pParFrentTrabAtivo varchar default null,
       pParStatusId varchar default null,
       pParStatusNome varchar default null,
       pParStatusAtivo varchar default null,
       pParStatusTipo varchar default null,
       pParLogUserIns varchar default null,
       pParLogDateInsIni varchar default null,
       pParLogDateInsFin varchar default null,
       pParLogUserUpd varchar default null,
       pParLogDateUpdIni varchar default null,
       pParLogDateUpdFin varchar default null
       
       )
       RETURNS TABLE(
        ind_rel_id varchar,
        ind_rel_par1 varchar,
        ind_rel_par2 varchar,
        ind_rel_par3 varchar,
        ind_rel_par4 varchar,
        vart_01 varchar,
        vard_01 varchar,
        vart_02 varchar,
        vard_02 varchar,
        vart_03 varchar,
        vard_03 varchar,
        vart_04 varchar,
        vard_04 varchar,
        vart_05 varchar,
        vard_05 varchar,
        valor_01 numeric,
        valor_02 numeric,
        valor_03 numeric,
        valor_04 numeric,
        valor_05 numeric,
        valor_06 numeric,
        valor_07 numeric,
        valor_08 numeric,
        valor_09 numeric,
        valor_10 numeric) AS $BODY$
       declare
       vSql varchar;
       vPar1 varchar :='';
       vPar2 varchar :='';
       vPar3 varchar :='';
       vPar4 varchar :='';
       r record;
       
       begin
       
           
           if pParOrdRecQntRendIni != '' and pParOrdRecQntRendFin != '' then
            vPar1 := vPar1||'Rendimento / Dosagem de ['||pParOrdRecQntRendIni||'] até ['||pParOrdRecQntRendFin||']'||chr(13)||chr(10);
            
        else
               vPar1 := vPar1||'Rendimento / Dosagem de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParOrdRecPercUtilIni != '' and pParOrdRecPercUtilFin != '' then
            vPar1 := vPar1||'Percentual Utilização de ['||pParOrdRecPercUtilIni||'] até ['||pParOrdRecPercUtilFin||']'||chr(13)||chr(10);
            
        else
               vPar1 := vPar1||'Percentual Utilização de [] até []'||chr(13)||chr(10);
        end if;	
           
           if pParOrdRecQntTotUtilIni != '' and pParOrdRecQntTotUtilFin != '' then
            vPar1 := vPar1||'Quantidade Total Utilização de ['||pParOrdRecQntTotUtilIni||'] até ['||pParOrdRecQntTotUtilFin||']'||chr(13)||chr(10);
            
        else
               vPar1 := vPar1||'Quantidade Total Utilização de [] até []'||chr(13)||chr(10);
        end if;
       
           if pParOrdRecVrUnitUtilIni != '' and pParOrdRecVrUnitUtilFin != '' then
               vPar1 := vPar1||'Valor Unitário Utilização de ['||pParOrdRecVrUnitUtilIni||'] até ['||pParOrdRecVrUnitUtilFin||']'||chr(13)||chr(10);
        else
               vPar1 := vPar1||'Valor Unitário Utilização de [] até []'||chr(13)||chr(10);
        end if;
       
           if pParOrdRecVrTotUtilIni != '' and pParOrdRecVrTotUtilFin != '' then
               vPar1 := vPar1||'Valor Total Utilização de ['||pParOrdRecVrTotUtilIni||'] até ['||pParOrdRecVrTotUtilFin||']'||chr(13)||chr(10);
        else
               vPar1 := vPar1||'Valor Total Utilização  de [] até []'||chr(13)||chr(10);
        end if;	
           
        if pParCentro2Id != '' then
                vPar1 := vPar1||'Centro 2 ['||fnreport_sigla(pParUnitId,'ope_centro2','sigla_centro2','id',''''||pParCentro2Id||'''')||'] '||chr(13)||chr(10);
           else
                vPar1 := vPar1||'Centro 2 [] '||chr(13)||chr(10);
           end if;
           
           if pParCentro2Nome != '' then
                vPar1 := vPar1||'Nome Centro 2 ['||pParCentro2Nome||'] '||chr(13)||chr(10);
           else
                vPar1 := vPar1||'Nome Centro 2 [] '||chr(13)||chr(10);	
           end if;
           
           if pParCentro2Ativo != '' then
                vPar1 := vPar1||'Centro 2 Ativo ['||pParCentro2Ativo||'] '||chr(13)||chr(10);	
           else
                vPar1 := vPar1||'Centro 2 Ativo [] '||chr(13)||chr(10);
           end if;
           
           if pParCentro1Id != '' then
                vPar1 := vPar1||'Centro 1 ['||fnreport_sigla(pParUnitId,'ope_centro1','sigla_centro1','id',''''||pParCentro1Id||'''')||'] '||chr(13)||chr(10);	
           else
               vPar1 := vPar1||'Centro 1 [] '||chr(13)||chr(10);
           end if;
       
           if pParCentro1Nome != '' then
               vPar1 := vPar1||'Nome Centro 1 ['||pParCentro1Nome||'] '||chr(13)||chr(10);	
           else
               vPar1 := vPar1||'Nome Centro 1 [] '||chr(13)||chr(10);
           end if;
           
           if pParCentro1Ativo != '' then
               vPar1 := vPar1||'Centro 1 Ativo ['||pParCentro1Ativo||'] '||chr(13)||chr(10);		
           else
               vPar1 := vPar1||'Centro 1 Ativo [] '||chr(13)||chr(10);	
           end if;
           
               if pParCtbId != '' then
                   vPar1 := vPar1||'Componente Contábil ['||fnreport_sigla(pParUnitId,'ctb_comp','sigla_comp','id',''''||pParCtbId||'''')||'] '||chr(13)||chr(10);	
           else
                   vPar1 := vPar1||'Componente Contábil [] '||chr(13)||chr(10);	
           end if;
           
           if pParCtbNome != '' then
               vPar1 := vPar1||'Nome Componente Contábil ['||pParCtbNome||'] '||chr(13)||chr(10);	
           else
               vPar1 := vPar1||'Nome Componente Contábil [] '||chr(13)||chr(10);	
           end if;
       
           if pParCtbAtivo != '' then
                   vPar1 := vPar1||'Componente Contábil Ativo ['||pParCtbAtivo||'] '||chr(13)||chr(10);	
           else
                   vPar1 := vPar1||'Componente Contábil Ativo [] '||chr(13)||chr(10);
           end if;
       
           if pParPessoaEnderecoAtivo != '' then
               vPar1 := vPar1||'Pessoa Endereco Ativo ['||pParPessoaEnderecoAtivo||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Pessoa Endereco Ativo []'||chr(13)||chr(10);
           end if;
           
       
           if pParPessoaEnderecoTipo != '' then
               vPar1 := vPar1||'Pessoa Endereco Tipo ['||pParPessoaEnderecoTipo||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Pessoa Endereco Tipo []'||chr(13)||chr(10);	
           end if;
           
           if pParPessoaEnderecoPadrao != '' then
               vPar1 := vPar1||'Pessoa Endereco Padrão ['||pParPessoaEnderecoPadrao||']'||chr(13)||chr(10);	
           else
               vPar1 := vPar1||'Pessoa Endereco Padrão []'||chr(13)||chr(10);	
           end if;
           
           if pParPessoaEnderecoLograd !='' then
               vPar1 := vPar1||'Pessoa Endereco Logradouro ['||pParPessoaEnderecoLograd||']'||chr(13)||chr(10);	
           else
               vPar1 := vPar1||'Pessoa Endereco Logradouro []'||chr(13)||chr(10);	
           end if;
           
           if pParPessoaEnderecoNr !='' then
               vPar2 := vPar2||'Pessoa Nº Endereco ['||pParPessoaEnderecoNr||']'||chr(13)||chr(10);			
           else
               vPar2 := vPar2||'Pessoa Nº Endereco []'||chr(13)||chr(10);	
           end if;
           
           if pParCentro1Imp01Id != '' then
                vPar2 := vPar2||'Implemento Centro 1 ['||fnreport_sigla(pParUnitId,'ope_centro1','sigla_centro1','id',''''||pParCentro1Imp01Id||'''')||'] '||chr(13)||chr(10);		
           else
                vPar2 := vPar2||'Implemento Centro 1 [] '||chr(13)||chr(10);	
           end if;	
       
           if pParCentro1Imp01Nome != '' then
               vPar2 := vPar2||'Nome Implemento Centro 1 ['||pParCentro1Imp01Nome||'] '||chr(13)||chr(10);		
           else
               vPar2 := vPar2||'Nome Implemento Centro 1 [] '||chr(13)||chr(10);			
           end if;
           
           if pParCentro1Imp01Ativo != '' then
               vPar2 := vPar2||'Implemento Centro 1 Ativo ['||pParCentro1Imp01Ativo||'] '||chr(13)||chr(10);			
           else
               vPar2 := vPar2||'Implemento Centro 1 Ativo [] '||chr(13)||chr(10);				
           end if;	
           
           
           
           if pParCentro2Imp01Id != '' then
                vPar2 := vPar2||'Implemento Centro 2 ['||fnreport_sigla(pParUnitId,'ope_centro2','sigla_centro2','id',''''||pParCentro2Imp01Id||'''')||'] '||chr(13)||chr(10);	
           else
                vPar2 := vPar2||'Implemento Centro 2 [] '||chr(13)||chr(10);		
           end if;	
           
           if pParCentro2Imp01Nome != '' then
               vPar2 := vPar2||'Nome Implemento Centro 2 ['||pParCentro2Imp01Nome||'] '||chr(13)||chr(10);				
           else
               vPar2 := vPar2||'Nome Implemento Centro 2 [] '||chr(13)||chr(10);						
           end if;	
       
           if pParCentro2Imp01Ativo != '' then
               vPar2 := vPar2||'Implemento Centro 2 Ativo ['||pParCentro2Imp01Ativo||'] '||chr(13)||chr(10);			
           else
               vPar2 := vPar2||'Implemento Centro 2 Ativo [] '||chr(13)||chr(10);					
           end if;
       
           if pParSubTipoId != '' then
               vPar2 := vPar2||'SubTipo ['||fnreport_sigla(pParUnitId,'ope_centro_subtipo','nome','id',''''||pParSubTipoId||'''')||'] '||chr(13)||chr(10);		 		
           else
               vPar2 := vPar2||'SubTipo [] '||chr(13)||chr(10);		 			
           end if;
           
           if pParSubTipoNome != '' then
               vPar2 := vPar2||'Nome SubTipo ['||pParSubTipoNome||'] '||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Nome SubTipo [] '||chr(13)||chr(10);	
           end if;
           
           if pParTipoId != '' then
               vPar2 := vPar2||'Tipo ['||fnreport_sigla(pParUnitId,'ope_centro_tipo','nome','id',''''||pParTipoId||'''')||'] '||chr(13)||chr(10);		 			
           else
               vPar2 := vPar2||'Tipo [] '||chr(13)||chr(10);
           end if;
           
           if pParTipoNome != '' then
               vPar2 := vPar2||'Nome Tipo ['||pParTipoNome||'] '||chr(13)||chr(10);	
           else
               vPar2 := vPar2||'Nome Tipo [] '||chr(13)||chr(10);	
           end if;
       
           if pParSubGrupoId != '' then
                vPar2 := vPar2||'SubGrupo ['||fnreport_sigla(pParUnitId,'ope_centro_subgrupo','sigla_centro_subgrupo','id',''''||pParSubGrupoId||'''')||'] '||chr(13)||chr(10);
           else
                vPar2 := vPar2||'SubGrupo [] '||chr(13)||chr(10);	
           end if;
           
           if pParSubGrupoNome != '' then
                vPar2 := vPar2||'Nome SubGrupo ['||pParSubGrupoNome||'] '||chr(13)||chr(10);		
           else
                vPar2 := vPar2||'Nome SubGrupo [] '||chr(13)||chr(10);		
           end if;
           
           if pParSubGrupoAtivo != '' then
                vPar2 := vPar2||'SubGrupo Ativo ['||pParSubGrupoAtivo||'] '||chr(13)||chr(10);			
           else
                vPar2 := vPar2||'SubGrupo Ativo [] '||chr(13)||chr(10);	
           end if;
           
           if pParGrupoId != '' then
               vPar2 := vPar2||'Grupo ['||fnreport_sigla(pParUnitId,'ope_centro_grupo','sigla_centro_grupo','id',''''||pParGrupoId||'''')||'] '||chr(13)||chr(10);		 
           else
               vPar2 := vPar2||'Grupo [] '||chr(13)||chr(10);
           end if;
           
           if pParGrupoNome != '' then
               vPar2 := vPar2||'Nome Grupo ['||pParGrupoNome||'] '||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Nome Grupo [] '||chr(13)||chr(10);
           end if;
           
           if pParGrupoAtivo != '' then
               vPar3 := vPar3||'Grupo Ativo ['||pParGrupoAtivo||'] '||chr(13)||chr(10);	
           else
               vPar3 := vPar3||'Grupo Ativo [] '||chr(13)||chr(10);	
           end if;
           
           if pParCentro2OrdDtIniExec != '' and pParCentro2OrdDtIniExecFin != '' then
               vPar3 := vPar3||'Data Inicial Execução de ['||pParCentro2OrdDtIniExec||'] até ['|| pParCentro2OrdDtIniExecFin||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Data Inicial Execução de [] até []'||chr(13)||chr(10);
           end if;
           
        if pParCentro2OrdDtFinExecIni != '' and pParCentro2OrdDtFinExec != '' then
               vPar3 := vPar3||'Data Final Execução de ['||pParCentro2OrdDtFinExecIni||'] até ['|| pParCentro2OrdDtFinExec||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Data Final Execução de [] até []'||chr(13)||chr(10);
           end if;
       
           if pParCentro2OrdDtIniExecPrev!= '' and pParCentro2OrdDtIniExecPrevFin != '' then
               vPar3 := vPar3||'Data Inicial Execução Prévia de ['||pParCentro2OrdDtIniExecPrev||'] até ['|| pParCentro2OrdDtIniExecPrevFin||']'||chr(13)||chr(10);	
           else
               vPar3 := vPar3||'Data Inicial Execução Prévia de [] até []'||chr(13)||chr(10);		
           end if;
           
           if pParCentro2OrdDtFinExecPrevIni != '' and pParCentro2OrdDtFinExecPrev != '' then
               vPar3 := vPar3||'Data Final Execução Prévia de ['||pParCentro2OrdDtFinExecPrevIni||'] até ['|| pParCentro2OrdDtFinExecPrev||']'||chr(13)||chr(10);		
           else
               vPar3 := vPar3||'Data Final Execução Prévia de [] até []'||chr(13)||chr(10);		
           end if;
           
           if pParCentro2OrdNr != '' then
               vPar3 := vPar3||'Nº Ordem ['||pParCentro2OrdNr||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Nº Ordem []'||chr(13)||chr(10);
           end if;	
       
       
           if pParEmpresaOrdId != '' then
                   vPar3 := vPar3||'Empresa ['||fnreport_sigla(pParUnitId,'ger_empresa','sigla_empresa','id',''''||pParEmpresaOrdId||'''')||'] '||chr(13)||chr(10);	
           else
                   vPar3 := vPar3||'Empresa []'||chr(13)||chr(10);		
           end if;
           
           if pParEmpresaOrdNome != '' then
                   vPar3 := vPar3||'Nome Empresa ['||pParEmpresaOrdNome||']'||chr(13)||chr(10);			
           else
                   vPar3 := vPar3||'Nome Empresa []'||chr(13)||chr(10);			
           end if;
       
           if pParEmpresaOrdAtivo != '' then
                   vPar3 := vPar3||'Empresa Ativo ['||pParEmpresaOrdAtivo||']'||chr(13)||chr(10);			
           else
                   vPar3 := vPar3||'Empresa Ativo []'||chr(13)||chr(10);			
           end if;
           
           if pParEmpresaOrdCpf != '' then
                   vPar3 := vPar3||'Empresa Cpf ['||pParEmpresaOrdCpf||']'||chr(13)||chr(10);			
           else
                   vPar3 := vPar3||'Empresa Cpf []'||chr(13)||chr(10);			
           end if;
           
           if pParEmpresaOrdCnpj != '' then
                   vPar3 := vPar3||'Empresa CNPJ ['||pParEmpresaOrdCnpj||']'||chr(13)||chr(10);			
           else
                   vPar3 := vPar3||'Empresa CNPJ []'||chr(13)||chr(10);			
           end if;
           
           if pParPeriodoOrdId != '' then
                vPar3 := vPar3||'Período  ['||fnreport_sigla(pParUnitId,'ope_periodo','sigla_periodo','id',''''||pParPeriodoOrdId||'''')||'] '||chr(13)||chr(10);				
           else
                vPar3 := vPar3||'Período []'||chr(13)||chr(10);			
           end if;	
       
           if pParPeriodoOrdNome != '' then
                   vPar3 := vPar3||'Nome Período ['||pParPeriodoOrdNome||']'||chr(13)||chr(10);			
           else
                   vPar3 := vPar3||'Nome Período []'||chr(13)||chr(10);			
           end if;	
       
           if pParPeriodoOrdAtivo != '' then
                   vPar3 := vPar3||'Período Ativo ['||pParPeriodoOrdAtivo||']'||chr(13)||chr(10);			
           else
                   vPar3 := vPar3||'Período Ativo []'||chr(13)||chr(10);			
           end if;	
           
           if pParPeriodoOrdDataIni != '' and pParPeriodoOrdDataIniFin != '' then
               vPar3 := vPar3||'Data Inicial do Período de ['||pParPeriodoOrdDataIni||'] até ['|| pParPeriodoOrdDataIniFin||']'||chr(13)||chr(10);	
           else
               vPar3 := vPar3||'Data Inicial do Período de [] até []'||chr(13)||chr(10);		
           end if;
           
           if pParPeriodoOrdDataFinIni != '' and pParPeriodoOrdDataFin != '' then
               vPar3 := vPar3||'Data Final do Período de ['||pParPeriodoOrdDataFinIni||'] até ['|| pParPeriodoOrdDataFin||']'||chr(13)||chr(10);		
           else
               vPar3 := vPar3||'Data Final do Período de [] até []'||chr(13)||chr(10);		
           end if;
           
           if pParGerPessoaId != '' then
               vPar4 := vPar4||'Pessoa ['||fnreport_sigla(pParUnitId,'ger_pessoa','nome','id',''''||pParGerPessoaId||'''')||'] '||chr(13)||chr(10);		
           else
               vPar4 := vPar4||'Pessoa [] '||chr(13)||chr(10);			
           end if;
       
           if pParGerPessoaNome != '' then
               vPar4 := vPar4||'Nome Pessoa ['||pParGerPessoaNome||'] '||chr(13)||chr(10);			
           else
               vPar4 := vPar4||'Nome Pessoa [] '||chr(13)||chr(10);	
           end if;
       
           if pParGerPessoaAtivo != '' then
               vPar4 := vPar4||'Pessoa Ativo ['||pParGerPessoaAtivo||'] '||chr(13)||chr(10);				
           else
               vPar4 := vPar4||'Pessoa Ativo [] '||chr(13)||chr(10);	
           end if;
       
           if pParGerPessoaDoc != '' then
               vPar4 := vPar4||'Doc Pessoa ['||pParGerPessoaDoc||'] '||chr(13)||chr(10);	
           else
               vPar4 := vPar4||'Doc Pessoa [] '||chr(13)||chr(10);	
           end if;
       
           if pParCentro2OrdTipoId != '' then
               vPar4 := vPar4||'Tipo Ord ['||fnreport_sigla(pParUnitId,'ope_centro2_ord_tipo','sigla_ord_tipo','id',''''||pParCentro2OrdTipoId||'''')||'] '||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Tipo Ord [] '||chr(13)||chr(10);
           end if;
           
           if pParCentro2OrdTipoNome != '' then
               vPar4 := vPar4||'Nome Tipo Ord ['||pParCentro2OrdTipoNome||'] '||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Nome Tipo Ord [] '||chr(13)||chr(10);	
           end if;
           
           if pParCentro2OrdTipoAtivo != '' then
               vPar4 := vPar4||'Tipo Ativo Ord ['||pParCentro2OrdTipoAtivo||'] '||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Tipo Ativo Ord [] '||chr(13)||chr(10);	
           end if;
           
           if pParFrentTrabId != '' then
                vPar4 := vPar4||'Frente Trabalho ['||fnreport_sigla(pParUnitId,'ope_frente_trabalho','sigla_frente_trabalho','id',''''||pParFrentTrabId||'''')||'] '||chr(13)||chr(10);
           else
                vPar4 := vPar4||'Frente Trabalho [] '||chr(13)||chr(10);	
           end if;
           
           if pParFrentTrabNome != '' then
                vPar4 := vPar4||'Nome Frente Trabalho ['||pParFrentTrabNome||'] '||chr(13)||chr(10);		
           else
                vPar4 := vPar4||'Nome Frente Trabalho [] '||chr(13)||chr(10);		
           end if;
           
           
           if pParFrentTrabAtivo != '' then
                vPar4 := vPar4||'Frente Trabalho Ativo ['||pParFrentTrabAtivo||'] '||chr(13)||chr(10);	
           else
                vPar4 := vPar4||'Frente Trabalho Ativo [] '||chr(13)||chr(10);		
           end if;	
           
           if pParStatusId != '' then
                vPar4 := vPar4||'Status ['||fnreport_sigla(pParUnitId,'ope_centro2_ord_status','sigla_ord_status','id',''''||pParStatusId||'''')||'] '||chr(13)||chr(10);	
           else
                vPar4 := vPar4||'Status [] '||chr(13)||chr(10);	
           end if;
           
           if pParStatusNome != '' then
                vPar4 := vPar4||'Nome Status ['||pParStatusNome||'] '||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Nome Status [] '||chr(13)||chr(10);
           end if;
               
           if pParStatusAtivo != '' then
               vPar4 := vPar4||'Status Ativo ['||pParStatusAtivo||'] '||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Status Ativo [] '||chr(13)||chr(10);
           end if;
           
           if pParStatusTipo != '' then
               vPar4 := vPar4||'Tipo Status ['||pParStatusTipo||'] '||chr(13)||chr(10);	
           else
               vPar4 := vPar4||'Tipo Status [] '||chr(13)||chr(10);		
           end if;
           
               if pParLogUserIns != '' then
               vPar4 := vPar4||'Log Usuario Inserção ['||pParLogUserIns||']'||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Log Usuario Inserção []'||chr(13)||chr(10);
           end if;
       
           if pParLogUserUpd != '' then
               vPar4 := vPar4||'Log Usuario Alteração ['||pParLogUserUpd||']'||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Log Usuario Alteração []'||chr(13)||chr(10);
           end if;
       
           if pParLogDateInsIni != '' and pParLogDateInsFin != '' then
               vPar4 := vPar4||'Data Inserção de ['||pParLogDateInsIni||'] até ['||pParLogDateInsFin||']'||chr(13)||chr(10);
           else
                       vPar4 := vPar4||'Data Inserção de [] até []'||chr(13)||chr(10);
           end if;
       
           if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then
               vPar4 := vPar4||'Data Alteração de ['||pParLogDateUpdIni||'] até ['||pParLogDateUpdFin||']'||chr(13)||chr(10);
           else
                   vPar4 := vPar4||'Data Alteração de [] até []'||chr(13)||chr(10);
           end if;
       
       vSql = 'select
           '  || pVart01 ||'   as vart_01 '||
               ','''|| pVard01 ||''' as vard_01 ';
               
               if  pVart02 != ''  THEN
                vSql = vSql || ','  || pVart02 ||'   as vart_02 '||
                          ','''|| pVard02 ||''' as vard_02 ';
               else 
                  vSql = vSql || ',null as vart_02'||
                                      ',null as vard_02';
               end if;
               
           if  pVart03 != '' THEN
                vSql = vSql || ','  || pVart03 ||'   as vart_03 '||
                          ','''|| pVard03 ||''' as vard_03 ';
               else 
                  vSql = vSql || ',null as vart_03'||
                                      ',null as vard_03';
               end if;
               
           if  pVart04 != '' THEN
                vSql = vSql || ','  || pVart04 ||'   as vart_04 '||
                          ','''|| pVard04 ||''' as vard_04 ';
               else 
                  vSql = vSql || ',null as vart_04'||
                                      ',null as vard_04';
               end if;
           if  pVart05 != ''  THEN
                vSql = vSql || ','  || pVart05 ||'   as vart_05 '||
                          ','''|| pVard05 ||''' as vard_05 ';
               else 
                  vSql = vSql || ',null as vart_05'||
                                      ',null as vard_05';
               end if;
               
               vSql = vSql||'
               ,sum(t1.ope_centro2_ord_rec_qnt_rend) as valor_01
               ,sum(t1.ope_centro2_ord_rec_perc_util) as valor_02
               ,sum(t1.ope_centro2_ord_rec_qnt_total_util) as valor_03
               ,sum(t1.ope_centro2_ord_rec_valor_unit_util) as valor_04
               ,sum(t1.ope_centro2_ord_rec_valor_total_util) as valor_05
               from vwope_centro2_ord_rec t1 where 1=1
               ';
               
               if pParUnitId != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_ord_rec_unitid' || ' in(''' ||pParUnitId||''')';
               end if;
               
               if pParOrdRecIId != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_ord_rec_id' || ' in(''' ||pParOrdRecIId||''')';
               end if;
           
            if pParOrdRecQntRendIni != ''  and pParOrdRecQntRendFin != '' then
                   vSql = vSql || ' and ' || 't1.ope_centro2_ord_rec_qnt_rend' || ' >= ''' || pParOrdRecQntRendIni|| '''' || ' and t1.ope_centro2_ord_rec_qnt_rend' || ' <= ''' || pParOrdRecQntRendFin|| ''''; 
            end if;
           
            if pParOrdRecPercUtilIni != ''  and pParOrdRecPercUtilFin != '' then
                   vSql = vSql || ' and ' || 't1.ope_centro2_ord_rec_perc_util' || ' >= ''' || pParOrdRecPercUtilIni|| '''' || ' and  t1.ope_centro2_ord_rec_perc_util' || ' <= ''' || pParOrdRecPercUtilFin|| ''''; 
            end if;
            
            if pParOrdRecQntTotUtilIni != ''  and pParOrdRecQntTotUtilFin != '' then
                   vSql = vSql || ' and ' || 't1.ope_centro2_ord_rec_qnt_total_util ' || ' >= ''' || pParOrdRecQntTotUtilIni|| '''' || ' and  t1.ope_centro2_ord_rec_qnt_total_util' || ' <= ''' || pParOrdRecQntTotUtilFin|| ''''; 
            end if;
       
            if pParOrdRecVrUnitUtilIni != ''  and pParOrdRecVrUnitUtilFin != '' then
                   vSql = vSql || ' and ' || 't1.ope_centro2_ord_rec_valor_unit_util' || ' >= ''' || pParOrdRecVrUnitUtilIni|| '''' || ' and  t1.ope_centro2_ord_rec_valor_unit_util' || ' <= ''' || pParOrdRecVrUnitUtilFin|| ''''; 
            end if;
       
            if pParOrdRecVrTotUtilIni != ''  and pParOrdRecVrTotUtilFin != '' then
                   vSql = vSql || ' and ' || 't1.ope_centro2_ord_rec_valor_total_util' || ' >= ''' || pParOrdRecVrTotUtilIni|| '''' || ' and t1.ope_centro2_ord_rec_valor_total_util' || ' <= ''' || pParOrdRecVrTotUtilFin|| ''''; 
            end if;
            
            if pParCentro1Id != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro1_id' || ' in(''' ||pParCentro1Id||''')';	 
            end if;
            
           if pParCentro1Nome != '' then
               vSql = vSql ||' and '||'t1.ope_centro1_nome'||' like'||'''%'||pParCentro1Nome||'%'' ';
           end if;
           
           if pParCentro1Ativo != '' then
               vSql = vSql ||' and '||'t1.ope_centro1_ativo_desc'||' like'||'''%'||pParCentro1Ativo||'%'' ';	
           end if;
           
           
           if pParCentro2Id != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_id' || ' in(''' ||pParCentro2Id||''')';	 	
           end if;
           
           if pParCentro2Nome != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_nome'||' like'||'''%'||pParCentro2Nome||'%'' ';	
           end if;
           
           if pParCentro2Ativo != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_ativo_desc'||' like'||'''%'||pParCentro2Ativo||'%'' ';	
           end if;
           
           if pParCtbId != '' then
                vSql = vSql || 'and ' || ' t1.ctb_id' || ' in(''' ||pParCtbId||''')';
           end if;
       
           if pParCtbNome != '' then
               vSql = vSql ||' and '||'t1.ctb_nome'||' like'||'''%'||pParCtbNome||'%'' ';		
           end if;
       
           if pParCtbAtivo != '' then
               vSql = vSql ||' and '||'t1.ctb_ativo_desc'||' like'||'''%'||pParCtbAtivo||'%'' ';		
           end if;
           
           
           --
           if pParPessoaEnderecoId != '' then
                vSql = vSql || 'and ' || ' t1.ger_pessoa_endereco_id' || ' in(''' ||pParPessoaEnderecoId||''')';
           end if;
           
           if pParPessoaEnderecoAtivo != '' then
               vSql = vSql ||' and '||'t1.ger_pessoa_endereco_ativo_desc'||' like'||'''%'||pParPessoaEnderecoAtivo||'%'' ';				
           end if;
           
           if pParPessoaEnderecoTipo != '' then
               vSql = vSql ||' and '||'t1.ger_pessoa_endereco_tipo'||' like'||'''%'||pParPessoaEnderecoTipo||'%'' ';				
           end if;	
           
           if pParPessoaEnderecoPadrao != '' then
               vSql = vSql ||' and '||'t1.ger_pessoa_endereco_padrao'||' like'||'''%'||pParPessoaEnderecoPadrao||'%'' ';				
           end if;		
           
       
           if pParPessoaEnderecoLograd != '' then
               vSql = vSql ||' and '||'t1.ger_pessoa_endereco_logradouro'||' like'||'''%'||pParPessoaEnderecoLograd||'%'' ';				
           end if;		
           
           if pParPessoaEnderecoNr != '' then
               vSql = vSql ||' and '||'t1.ger_pessoa_endereco_loradouro_nr'||' like'||'''%'||pParPessoaEnderecoNr||'%'' ';				
           end if;	
           
           
           if pParCentro1Imp01Id != '' then
                vSql = vSql || 'and ' || ' t1.ope_centro1_imp01_id' || ' in(''' ||pParCentro1Imp01Id||''')';	
           end if;
           
           if pParCentro1Imp01Nome != '' then
               vSql = vSql ||' and '||'t1.ope_centro1_imp01_nome'||' like'||'''%'||pParCentro1Imp01Nome||'%'' ';	
           end if; 
           
           if pParCentro1Imp01Ativo != '' then
               vSql = vSql ||' and '||'t1.ope_centro1_imp01_ativo_desc'||' like'||'''%'||pParCentro1Imp01Ativo||'%'' ';		
           end if;
           
           
           if pParCentro2Imp01Id != '' then
                vSql = vSql || 'and ' || ' t1.ope_centro2_imp01_id' || ' in(''' ||pParCentro2Imp01Id||''')';	
           end if;
           
           if pParCentro2Imp01Nome != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_imp01_nome'||' like'||'''%'||pParCentro2Imp01Nome||'%'' ';	
           end if; 
           
           if pParCentro2Imp01Ativo != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_imp01_id_ativo_desc'||' like'||'''%'||pParCentro2Imp01Ativo||'%'' ';		
           end if;
           
           
           if pParSubTipoId != '' then
                vSql = vSql || 'and ' || ' t1.ope_centro_subtipo_id' || ' in(''' ||pParSubTipoId||''')';
           end if;
           
           if pParSubTipoNome != '' then
               vSql = vSql ||' and '||'t1.ope_centro_subtipo_nome'||' like'||'''%'||pParSubTipoNome||'%'' ';	
           end if;
           
           if pParTipoId != '' then
                vSql = vSql || 'and ' || ' t1.ope_centro_tipo_id' || ' in(''' ||pParTipoId||''')';
           end if;	
           
           if pParTipoNome != '' then
               vSql = vSql ||' and '||'t1.ope_centro_tipo_nome'||' like'||'''%'||pParTipoNome||'%'' ';	
           end if;
            
           if pParSubGrupoId != '' then
                vSql = vSql || 'and ' || ' t1.ope_centro_subgrupo_id' || ' in(''' ||pParSubGrupoId||''')';
           end if;	
           
           if pParSubGrupoNome != '' then
               vSql = vSql ||' and '||'t1.ope_centro_subgrupo_nome'||' like'||'''%'||pParSubGrupoNome||'%'' ';	
           end if;	
       
           if pParSubGrupoAtivo != '' then
               vSql = vSql ||' and '||'t1.ope_centro_subgrupo_ativo_desc'||' like'||'''%'||pParSubGrupoAtivo||'%'' ';	
           end if;
           
           if pParGrupoId != '' then
                vSql = vSql || 'and ' || ' t1.ope_centro_grupo_id' || ' in(''' ||pParGrupoId||''')';
           end if;	
           
           if pParGrupoNome != '' then
               vSql = vSql ||' and '||'t1.ope_centro_grupo_nome'||' like'||'''%'||pParGrupoNome||'%'' ';	
           end if;	
           
           if pParGrupoAtivo != '' then
               vSql = vSql ||' and '||'t1.ope_centro_grupo_ativo_desc'||' like'||'''%'||pParGrupoAtivo||'%'' ';	
           end if;
           
           
           if pParCentro2OrdId != '' then
                    vSql = vSql || 'and ' || ' t1.ope_centro2_ord_id' || ' in(''' ||pParCentro2OrdId||''')';
           end if;
           
           
           
           if pParCentro2OrdDtIniExec != '' and pParCentro2OrdDtIniExecFin != '' then
               vSql = vSql || ' and ' ||'CAST(t1.ope_centro2_ord_data_ini_exec AS DATE)' || ' >= ''' || pParCentro2OrdDtIniExec|| '''' || ' and  CAST(t1.ope_centro2_ord_data_ini_exec AS DATE)' || ' <= ''' || pParCentro2OrdDtIniExecFin|| '''';		
           end if;
       
           if pParCentro2OrdDtFinExecIni != '' and pParCentro2OrdDtFinExec != '' then
               vSql = vSql || ' and ' ||'CAST(t1.ope_centro2_ord_data_fin_exec AS DATE)' || ' >= ''' || pParCentro2OrdDtFinExecIni|| '''' || ' and  CAST(t1.ope_centro2_ord_data_fin_exec AS DATE)' || ' <= ''' || pParCentro2OrdDtFinExec|| '''';		
           end if;
       
           if pParCentro2OrdDtIniExecPrev != '' and pParCentro2OrdDtIniExecPrevFin != '' then
               vSql = vSql || ' and ' ||'CAST(t1.ope_centro2_ord_data_ini_exec_prev AS DATE)' || ' >= ''' || pParCentro2OrdDtIniExecPrev|| '''' || ' and  CAST(t1.ope_centro2_ord_data_ini_exec_prev AS DATE)' || ' <= ''' || pParCentro2OrdDtIniExecPrevFin|| '''';
           end if;
           
           if pParCentro2OrdDtFinExecPrevIni != '' and pParCentro2OrdDtFinExecPrev != '' then
               vSql = vSql || ' and ' ||'CAST(t1.ope_centro2_ord_data_fin_exec_prev AS DATE)' || ' >= ''' || pParCentro2OrdDtFinExecPrevIni|| '''' || ' and  CAST(t1.ope_centro2_ord_data_fin_exec_prev AS DATE)' || ' <= ''' || pParCentro2OrdDtFinExecPrev|| '''';	
           end if;
       
           if pParCentro2OrdNr != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_ord_numero_ord'||' like'||'''%'||pParCentro2OrdNr||'%'' ';	
           end if;
       
       
               if pParEmpresaOrdId != '' then
                vSql = vSql || 'and ' || ' t1.ger_empresa_id_ord' || ' in(''' ||pParEmpresaOrdId||''')';	
           end if;
           
           if pParEmpresaOrdNome != '' then
               vSql = vSql ||' and '||'t1.ger_empresa_nome_ord'||' like'||'''%'||pParEmpresaOrdNome||'%'' ';	
           end if;	
               
           if pParEmpresaOrdAtivo != '' then
               vSql = vSql ||' and '||'t1.ger_empresa_ativo_desc_ord'||' like'||'''%'||pParEmpresaOrdAtivo||'%'' ';	
           end if;		
           
           if pParEmpresaOrdCpf != '' then
               vSql = vSql ||' and '||'t1.ger_empresa_doc_cpf_ord'||' like'||'''%'||pParEmpresaOrdCpf||'%'' ';	
           end if;					
           
           if pParEmpresaOrdCnpj != '' then
               vSql = vSql ||' and '||'t1.ger_empresa_doc_cnpj_ord'||' like'||'''%'||pParEmpresaOrdCnpj||'%'' ';	
           end if;
           
           
           if pParPeriodoOrdId != '' then
                vSql = vSql || 'and ' || ' t1.ope_periodo_id_ord' || ' in(''' ||pParPeriodoOrdId||''')';		
           end if;
       
           if pParPeriodoOrdNome != '' then
               vSql = vSql ||' and '||'t1.ope_periodo_nome_ord'||' like'||'''%'||pParPeriodoOrdNome||'%'' ';	
           end if;
       
           if pParPeriodoOrdAtivo != '' then
               vSql = vSql ||' and '||'t1.ope_periodo_ativo_ord_desc'||' like'||'''%'||pParPeriodoOrdAtivo||'%'' ';	
           end if;
       
           if pParPeriodoOrdDataIni != '' and pParPeriodoOrdDataIniFin != '' then
               vSql = vSql || ' and ' ||'CAST(t1.ope_periodo_data_ini_ord AS DATE)' || ' >= ''' || pParPeriodoOrdDataIni|| '''' || ' and CAST(t1.ope_periodo_data_ini_ord AS DATE)' || ' <= ''' || pParPeriodoOrdDataIniFin|| '''';	
           end if;
       
           if pParPeriodoOrdDataFinIni != '' and pParPeriodoOrdDataFin != '' then
               vSql = vSql || ' and ' ||'CAST(t1.ope_periodo_data_fin_ord AS DATE)' || ' >= ''' || pParPeriodoOrdDataFinIni|| '''' || ' and CAST(t1.ope_periodo_data_fin_ord AS DATE)' || ' <= ''' || pParPeriodoOrdDataFin|| '''';	
           end if;
           
           
           if pParGerPessoaId != '' then
                vSql = vSql || 'and ' || ' t1.ger_pessoa_id_ord' || ' in(''' ||pParGerPessoaId||''')';
           end if;
       
           if pParGerPessoaNome != '' then
               vSql = vSql ||' and '||'t1.ger_pessoa_nome_ord'||' like'||'''%'||pParGerPessoaNome||'%'' ';		
           end if;
           
           if pParGerPessoaAtivo != '' then
               vSql = vSql ||' and '||'t1.ger_pessoa_ativo_desc_ord'||' like'||'''%'||pParGerPessoaAtivo||'%'' ';		
           end if;
       
           if pParGerPessoaDoc != '' then
               vSql = vSql ||' and '||'t1.ger_pessoa_doc_cpf_cnpj_ord'||' like'||'''%'||pParGerPessoaDoc||'%'' ';		
           end if;
           
           
           if pParCentro2OrdTipoId != '' then
                vSql = vSql || 'and ' || ' t1.ope_centro2_ord_tipo_id' || ' in(''' ||pParCentro2OrdTipoId||''')';
           end if;
           
       
           if pParCentro2OrdTipoNome != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_ord_tipo_nome'||' like'||'''%'||pParCentro2OrdTipoNome||'%'' ';				
           end if;	
       
           if pParCentro2OrdTipoAtivo != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_ord_tipo_ativo_desc'||' like'||'''%'||pParCentro2OrdTipoAtivo||'%'' ';				
           end if;	
           
           if pParFrentTrabId != '' then
                vSql = vSql || 'and ' || ' t1.ope_frente_trabalho_id_ord' || ' in(''' ||pParFrentTrabId||''')';
           end if;	
           
           if pParFrentTrabNome != '' then
               vSql = vSql ||' and '||'t1.ope_frente_trabalho_nome_ord'||' like'||'''%'||pParFrentTrabNome||'%'' ';	
           end if;
           
           if pParFrentTrabAtivo != '' then
               vSql = vSql ||' and '||'t1.ope_frente_trabalho_ativo_desc_ord'||' like'||'''%'||pParFrentTrabAtivo||'%'' ';	
           end if;	
           
           if pParStatusId != '' then
                vSql = vSql || 'and ' || ' t1.ope_centro2_ord_status_id' || ' in(''' ||pParStatusId||''')';
           end if;
           
           if pParStatusNome != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_ord_status_nome'||' like'||'''%'||pParStatusNome||'%'' ';	
           end if;
       
           if pParStatusAtivo != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_ord_status_ativo_desc'||' like'||'''%'||pParStatusAtivo||'%'' ';	
           end if;
           
           if pParStatusTipo != '' then
               vSql = vSql ||' and '||'t1.ope_centro2_ord_status_tipo_status'||' like'||'''%'||pParStatusTipo||'%'' ';	
           end if;	
           
           if pParLogUserIns != '' then
                   vSql = vSql || 'and ' || ' t1.log_user_ins' || ' like '|| '''%' ||pParLogUserIns|| '%'' ';
           end if;
               
               if pParLogDateInsIni != '' and pParLogDateInsFin != '' then
                 vSql = vSql || ' and ' || 'CAST(t1.log_date_ins AS DATE)' || ' >= ''' || pParLogDateInsIni|| '''' || ' and  CAST(t1.log_date_ins AS DATE)' || ' <= ''' || pParLogDateInsFin || '''';
               end if;
               
               if pParLogUserUpd != '' then
                   vSql = vSql || 'and ' || ' t1.log_user_upd' || ' like '|| '''%' ||pParLogUserUpd|| '%'' ';
               end if;		
       
               if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then
                 vSql = vSql || ' and ' || 'CAST(t1.log_date_upd AS DATE)' || ' >= ''' || pParLogDateUpdIni|| '''' || ' and  CAST(t1.log_date_upd AS DATE)' || ' <= ''' || pParLogDateUpdFin || '''';
               end if;
           
           
           
            -- Group By
            -- ===================================
               vSql = vSql||' group by '|| pVart01;
       
               if  pVart02 != ''  THEN
                vSql = vSql||  ','|| pVart02;
               end if;
               
           if  pVart03 != ''  THEN
                vSql = vSql||  ','|| pVart03;
               end if;
               
           if  pVart04 != ''  THEN
                vSql = vSql||  ','|| pVart04;
               end if;
               
           if  pVart05 != ''  THEN
                vSql = vSql||  ','|| pVart05;
               end if;
               
            -- Order By
            -- ===================================
               vSql = vSql||' order by '|| pVart01;
       
               if  pVart02 != ''  THEN
                vSql = vSql||  ','|| pVart02;
               end if;
               
           if  pVart03 != ''  THEN
                vSql = vSql||  ','|| pVart03;
               end if;
               
           if  pVart04 != ''  THEN
                vSql = vSql||  ','|| pVart04;
               end if;
               
           if  pVart05 != ''  THEN
                vSql = vSql||  ','|| pVart05;
               end if;
               
           
           FOR r IN EXECUTE vSql loop
               ind_rel_id := pParIndRelId;
               ind_rel_par1 := vPar1;
               ind_rel_par2 := vPar2;
               ind_rel_par3 := vPar3;
               ind_rel_par4 := vPar4;
               vart_01 := r.vart_01;
               vard_01 := r.vard_01;
               vart_02 := r.vart_02;
               vard_02 := r.vard_02;
               vart_03 := r.vart_03;
               vard_03 := r.vard_03;
               vart_04 := r.vart_04;
               vard_04 := r.vard_04;
               vart_05 := r.vart_05;
               vard_05 := r.vard_05;
               valor_01 := r.valor_01;
               valor_02 := r.valor_02;
               valor_03 := r.valor_03;
               valor_04 := r.valor_04;
               valor_05 := r.valor_05;
       
           RETURN NEXT;
           
           END loop;
       Raise notice 'Sql :%',vSql;
       end;
       $BODY$
         LANGUAGE plpgsql VOLATILE;;
       
       
       
       -----------
       
       

       Drop FUNCTION IF EXISTS fnreport0022;;

       CREATE OR REPLACE FUNCTION fnreport0022(
       pParUnitId varchar, 
       pParIndRelId varchar, 
       pVart01 varchar, 
       pVard01 varchar, 
       pVart02 varchar default null,
       pVard02 varchar default null,
       pVart03 varchar default null,
       pVard03 varchar default null,
       pVart04 varchar default null,
       pVard04 varchar default null,
       pVart05 varchar default null,
       pVard05 varchar default null,
       pParItemServId varchar default null,
       pParItemServNome varchar default null,
       pParItemServAtivo varchar default null,
       pParItemServTipo varchar default null,
       pParItemServOrigemFiscal varchar default null,
       pParItemServTipoComposi varchar default null,
       pParItemServTipoCtbComp varchar default null,
       pParItemServDocCnaeNfs varchar default null,
       pParItemServSubGrupoId varchar default null,
       pParItemServSubGrupoNome varchar default null,
       pParItemServSubGrupoAtivo varchar default null,
       
       pParItemServGrupoId varchar default null,
       pParItemServGrupoNome varchar default null,
       pParItemServGrupoAtivo varchar default null,
       pParFisNcmId varchar default null,
       pParFisNcmNome varchar default null,
       pParFisNcmAtivo varchar default null,
       pParFisNcmDataValidadeIni varchar default null,
       pParFisNcmDataValidadeFin varchar default null,
       pParFisNcmNumero varchar default null,
       pParUnidadeMedId varchar default null,
       pParUnidadeMedNome varchar default null,
       pParUnidadeMedAtivo varchar default null,
       
       pParFisCestId varchar default null,
       pParFisCestNome varchar default null,
       pParFisCestAtivo varchar default null,
       pParFisCestDataValidadeIni varchar default null,
       pParFisCestDataValidadeFin varchar default null,
       pParFisCestNumero varchar default null,
       pParFisNbsId varchar default null,
       pParFisNbsNome varchar default null,
       pParFisNbsAtivo varchar default null,
       pParFisNbsDataValidadeIni varchar default null,
       pParFisNbsDataValidadeFin varchar default null,
       pParFisNbsNumero varchar default null,
       pParCtbId varchar default null,
       pParCtbNome varchar default null,
       pParCtbAtivo varchar default null,
       pParLogUserIns varchar default null,
       pParLogDateInsIni varchar default null,
       pParLogDateInsFin varchar default null,
       pParLogUserUpd varchar default null,
       pParLogDateUpdIni varchar default null,
       pParLogDateUpdFin varchar default null
       )
       RETURNS TABLE(
        ind_rel_id varchar,
        ind_rel_par1 varchar,
        ind_rel_par2 varchar,
        ind_rel_par3 varchar,
        vart_01 varchar,
        vard_01 varchar,
        vart_02 varchar,
        vard_02 varchar,
        vart_03 varchar,
        vard_03 varchar,
        vart_04 varchar,
        vard_04 varchar,
        vart_05 varchar,
        vard_05 varchar,
        valor_01 numeric,
        valor_02 numeric,
        valor_03 numeric,
        valor_04 numeric,
        valor_05 numeric,
        valor_06 numeric,
        valor_07 numeric,
        valor_08 numeric,
        valor_09 numeric,
        valor_10 numeric) AS $BODY$
       declare
       vSql varchar;
       vPar1 varchar :='';
       vPar2 varchar :='';
       vPar3 varchar :='';
       r record;
       
       begin
       
           if pParItemServId != '' then
               vPar1 :=vPar1||'Item/Serviço ['||fnreport_sigla(pParUnitId,'ger_itemserv','sigla_itemserv','id',''''||pParItemServId||'''')||'] '||chr(13)||chr(10);
           else
               vPar1 :=vPar1||'Item/Serviço []'||chr(13)||chr(10);
           end if;
           
           if pParItemServNome != '' then
               vPar1 :=vPar1||'Nome Item/Serviço ['||pParItemServNome||']'||chr(13)||chr(10);	
           else
               vPar1 :=vPar1||'Nome Item/Serviço []'||chr(13)||chr(10);		
           end if;
           
           if pParItemServAtivo != '' then
               vPar1 :=vPar1||'Item/Serviço Ativo ['||pParItemServAtivo||']'||chr(13)||chr(10);		
           else
               vPar1 :=vPar1||'Item/Serviço Ativo []'||chr(13)||chr(10);			
           end if;
           
           if pParItemServTipo != '' then
               vPar1 :=vPar1||'Tipo Item/Serviço ['||pParItemServTipo||']'||chr(13)||chr(10);		
           else
               vPar1 :=vPar1||'Tipo Item/Serviço []'||chr(13)||chr(10);			
           end if;
           
           if pParItemServOrigemFiscal != '' then
               vPar1 :=vPar1||'Origem Fiscal Item/Serviço ['||pParItemServOrigemFiscal||']'||chr(13)||chr(10);			
           else
               vPar1 :=vPar1||'Origem Fiscal Item/Serviço []'||chr(13)||chr(10);				
           end if;
           
           if pParItemServTipoComposi != '' then
               vPar1 :=vPar1||'Tipo de Composição Item/Serviço ['||pParItemServTipoComposi||']'||chr(13)||chr(10);				
           else
               vPar1 :=vPar1||'Tipo de Composição Item/Serviço []'||chr(13)||chr(10);					
           end if;
       
           if pParItemServTipoCtbComp != '' then
               vPar1 :=vPar1||'Tipo Componente Contábil Item/Serviço ['||pParItemServTipoCtbComp||']'||chr(13)||chr(10);				
           else
               vPar1 :=vPar1||'Tipo Componente Contábil Item/Serviço []'||chr(13)||chr(10);					
           end if;
           
        if pParItemServDocCnaeNfs!= '' then
               vPar1 :=vPar1||'Documento Cnae da NFS Item/Serviço ['||pParItemServDocCnaeNfs||']'||chr(13)||chr(10);	 
        else
               vPar1 :=vPar1||'Documento Cnae da NFS Item/Serviço []'||chr(13)||chr(10);	  
        end if;
       
           if pParItemServSubGrupoId != '' then
               vPar1 :=vPar1||'SubGrupo Item/Serviço ['||fnreport_sigla(pParUnitId,'ger_itemserv_subgrupo','nome','id',''''||pParItemServSubGrupoId||'''')||'] '||chr(13)||chr(10);
           else
               vPar1 :=vPar1||'SubGrupo Item/Serviço []'||chr(13)||chr(10);
           end if;
       
        if pParItemServSubGrupoNome != '' then
               vPar1 :=vPar1||'Nome SubGrupo Item/Serviço ['||pParItemServSubGrupoNome||']'||chr(13)||chr(10);	 
        else
               vPar1 :=vPar1||'Nome SubGrupo Item/Serviço []'||chr(13)||chr(10);	  
        end if;
       
       
        if pParItemServSubGrupoAtivo != '' then
               vPar1 :=vPar1||'SubGrupo Item/Serviço Ativo ['||pParItemServSubGrupoAtivo||']'||chr(13)||chr(10);	 
        else
               vPar1 :=vPar1||'SubGrupo Item/Serviço Ativo []'||chr(13)||chr(10);	  
        end if;
       
           if pParItemServGrupoId != '' then
               vPar1 :=vPar1||'Grupo Item/Serviço ['||fnreport_sigla(pParUnitId,'ger_itemserv_grupo','nome','id',''''||pParItemServGrupoId||'''')||'] '||chr(13)||chr(10);
           else
               vPar1 :=vPar1||'Grupo Item/Serviço []'||chr(13)||chr(10);
           end if;
       
        if pParItemServGrupoNome != '' then
               vPar1 :=vPar1||'Nome Grupo Item/Serviço ['||pParItemServGrupoNome||']'||chr(13)||chr(10);	 
        else
               vPar1 :=vPar1||'Nome Grupo Item/Serviço []'||chr(13)||chr(10);	  
        end if;
       
        if pParItemServGrupoAtivo != '' then
               vPar2 :=vPar2||'Grupo Item/Serviço Ativo ['||pParItemServGrupoAtivo||']'||chr(13)||chr(10);	 
        else
               vPar2 :=vPar2||'Grupo Item/Serviço Ativo []'||chr(13)||chr(10);	  
        end if;
       
           if pParFisNcmId != '' then
               vPar2 :=vPar2||'NCM ['||fnreport_sigla(pParUnitId,'fis_ncm','nome','id',''''||pParFisNcmId||'''')||'] '||chr(13)||chr(10);
           else
               vPar2 :=vPar2||'NCM []'||chr(13)||chr(10);
           end if;
       
        if pParFisNcmNome != '' then
               vPar2 :=vPar2||'Nome NCM ['||pParFisNcmNome||']'||chr(13)||chr(10);	 
        else
               vPar2 :=vPar2||'Nome NCM []'||chr(13)||chr(10);	  
        end if;
       
        if pParFisNcmAtivo != '' then
               vPar2 :=vPar2||'NCM Ativo ['||pParFisNcmAtivo||']'||chr(13)||chr(10);	 
        else
               vPar2 :=vPar2||'NCM Ativo []'||chr(13)||chr(10);	  
        end if;
       
        if pParFisNcmDataValidadeIni != '' and pParFisNcmDataValidadeFin != '' then
               vPar2 :=vPar2||'Data Validade NCM de ['||pParFisNcmDataValidadeIni||'] até ['||pParFisNcmDataValidadeFin||']'||chr(13)||chr(10);	 
        else
               vPar2 :=vPar2||'Data Validade NCM de [] até []'||chr(13)||chr(10);	  
        end if;
       
        if pParFisNcmNumero != '' then
               vPar2 :=vPar2||'Nº NCM ['||pParFisNcmNumero||']'||chr(13)||chr(10);	 
        else
               vPar2 :=vPar2||'Nº NCM []'||chr(13)||chr(10);	  
        end if;
       
        if pParUnidadeMedId != '' then
               vPar2 :=vPar2||'Unidade de Medida ['||fnreport_sigla(pParUnitId,'ger_umedida','sigla_umedida','id',''''||pParUnidadeMedId||'''')||'] '||chr(13)||chr(10);
           else
               vPar2 :=vPar2||'Unidade de Medida []'||chr(13)||chr(10);
           end if;
       
        if pParUnidadeMedNome != '' then
               vPar2 :=vPar2||'Nome Unidade de Medida ['||pParUnidadeMedNome||']'||chr(13)||chr(10);	 
        else
               vPar2 :=vPar2||'Nome Unidade de Medida []'||chr(13)||chr(10);	  
        end if;
       
        if pParUnidadeMedAtivo != '' then
               vPar2 :=vPar2||'Unidade de Medida Ativo ['||pParUnidadeMedAtivo||']'||chr(13)||chr(10);	 
        else
               vPar2 :=vPar2||'Unidade de Medida Ativo []'||chr(13)||chr(10);	  
        end if;
       
        if pParFisCestId != '' then
               vPar2 :=vPar2||'CEST ['||fnreport_sigla(pParUnitId,'fis_cest','nome','id',''''||pParFisCestId||'''')||'] '||chr(13)||chr(10);
           else
               vPar2 :=vPar2||'CEST []'||chr(13)||chr(10);
           end if;
       
        if pParFisCestNome != '' then
               vPar2 :=vPar2||'Nome CEST ['||pParFisCestNome||']'||chr(13)||chr(10);	 
        else
               vPar2 :=vPar2||'Nome CEST []'||chr(13)||chr(10);	  
        end if;
        
        if pParFisCestAtivo != '' then
               vPar2 :=vPar2||'CEST Ativo ['||pParFisCestAtivo||']'||chr(13)||chr(10);	 
        else
               vPar2 :=vPar2||'CEST Ativo []'||chr(13)||chr(10);	  
        end if;
       
        if pParFisCestDataValidadeIni != '' and pParFisCestDataValidadeFin != '' then
               vPar2 :=vPar2||'Data Validade CEST de ['||pParFisCestDataValidadeIni||'] até ['||pParFisCestDataValidadeFin||']'||chr(13)||chr(10);	 
        else
               vPar2 :=vPar2||'Data Validade CEST de [] até []'||chr(13)||chr(10);	  
        end if;
       
        if pParFisCestNumero != '' then
               vPar3 :=vPar3||'Nº CEST ['||pParFisCestNumero||']'||chr(13)||chr(10);	 
        else
               vPar3 :=vPar3||'Nº CEST []'||chr(13)||chr(10);	  
        end if;
       
        if pParFisNbsId != '' then
               vPar3 :=vPar3||'NBS ['||fnreport_sigla(pParUnitId,'fis_nbs','nome','id',''''||pParFisNbsId||'''')||'] '||chr(13)||chr(10);
           else
               vPar3 :=vPar3||'NBS []'||chr(13)||chr(10);
           end if;
       
        if pParFisNbsNome != '' then
               vPar3 :=vPar3||'Nome NBS ['||pParFisNbsNome||']'||chr(13)||chr(10);	 
        else
               vPar3 :=vPar3||'Nome NBS []'||chr(13)||chr(10);	  
        end if;
       
        if pParFisNbsAtivo != '' then
               vPar3 :=vPar3||'NBS Ativo ['||pParFisNbsAtivo||']'||chr(13)||chr(10);	 
        else
               vPar3 :=vPar3||'NBS Ativo []'||chr(13)||chr(10);	  
        end if;
       
        if pParFisNbsDataValidadeIni != '' and pParFisNbsDataValidadeFin != '' then
               vPar3 :=vPar3||'Data Validade NBS de ['||pParFisNbsDataValidadeIni||'] até ['||pParFisNbsDataValidadeFin||']'||chr(13)||chr(10);	 
        else
               vPar3 :=vPar3||'Data Validade NBS de [] até []'||chr(13)||chr(10);	  
        end if;
       
        if pParFisNbsNumero != '' then
               vPar3 :=vPar3||'Nº NBS ['||pParFisNbsNumero||']'||chr(13)||chr(10);	 
        else
               vPar3 :=vPar3||'Nº NBS []'||chr(13)||chr(10);	  
        end if;
       
        if pParCtbId != '' then
               vPar3 :=vPar3||'Componente Contábil ['||fnreport_sigla(pParUnitId,'ctb_comp','sigla_comp','id',''''||pParCtbId||'''')||'] '||chr(13)||chr(10);
           else
               vPar3 :=vPar3||'Componente Contábil []'||chr(13)||chr(10);
           end if;
       
        if pParCtbNome != '' then
               vPar3 :=vPar3||'Nome Componente Contábil ['||pParCtbNome||']'||chr(13)||chr(10);	 
        else
               vPar3 :=vPar3||'Nome Componente Contábil []'||chr(13)||chr(10);	  
        end if;
       
        if pParCtbAtivo != '' then
               vPar3 :=vPar3||'Componente Contábil Ativo ['||pParCtbAtivo||']'||chr(13)||chr(10);	 
        else
               vPar3 :=vPar3||'Componente Contábil Ativo []'||chr(13)||chr(10);	  
        end if;
       
           if pParLogUserIns != '' then
               vPar3 :=vPar3||'Log Usuario Inserção ['||pParLogUserIns||']'||chr(13)||chr(10);
           else
               vPar3 :=vPar3||'Log Usuario Inserção []'||chr(13)||chr(10);
           end if;
       
           if pParLogUserUpd != '' then
               vPar3 :=vPar3||'Log Usuario Alteração ['||pParLogUserUpd||']'||chr(13)||chr(10);
           else
               vPar3 :=vPar3||'Log Usuario Alteração []'||chr(13)||chr(10);
           end if;
       
           if pParLogDateInsIni != '' and pParLogDateInsFin != '' then
               vPar3 :=vPar3||'Data Inserção de ['||pParLogDateInsIni||'] até ['||pParLogDateInsFin||']'||chr(13)||chr(10);
           else
               vPar3 :=vPar3||'Data Inserção de [] até []'||chr(13)||chr(10);
           end if;
       
           if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then
               vPar3 :=vPar3||'Data Alteração de ['||pParLogDateUpdIni||'] até ['||pParLogDateUpdFin||']'||chr(13)||chr(10);
           else
               vPar3 :=vPar3||'Data Alteração de [] até []'||chr(13)||chr(10);
           end if;
       
       
           vSql = 'select
           '  || pVart01 ||'   as vart_01 '||
               ','''|| pVard01 ||''' as vard_01 ';
               
               if  pVart02 != ''  THEN
                vSql = vSql || ','  || pVart02 ||'   as vart_02 '||
                          ','''|| pVard02 ||''' as vard_02 ';
               else 
                  vSql = vSql || ',null as vart_02'||
                                      ',null as vard_02';
               end if;
           if  pVart03 != '' THEN
                vSql = vSql || ','  || pVart03 ||'   as vart_03 '||
                          ','''|| pVard03 ||''' as vard_03 ';
               else 
                  vSql = vSql || ',null as vart_03'||
                                      ',null as vard_03';
               end if;
           if  pVart04 != '' THEN
                vSql = vSql || ','  || pVart04 ||'   as vart_04 '||
                          ','''|| pVard04 ||''' as vard_04 ';
               else 
                  vSql = vSql || ',null as vart_04'||
                                      ',null as vard_04';
               end if;
           if  pVart05 != ''  THEN
                vSql = vSql || ','  || pVart05 ||'   as vart_05 '||
                          ','''|| pVard05 ||''' as vard_05 ';
               else 
                  vSql = vSql || ',null as vart_05'||
                                      ',null as vard_05';
               end if;
               
               vSql = vSql ||',
                   count(1) as valor_01
                   from vwger_itemserv t1 where 1=1';
       
       
       
               IF pParUnitId != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_itemserv_unitid' || ' in(''' ||pParUnitId||''')';
               END IF;
               
               IF pParItemServId != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_itemserv_id' || ' in(''' ||pParItemServId||''')';
               END IF;
               
               IF pParItemServNome != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_itemserv_nome' || ' like '|| '''%' || pParItemServNome || '%'' ';	
               END IF;
               
               IF pParItemServAtivo != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_itemserv_ativo_desc' || ' like '|| '''%' || pParItemServAtivo || '%'' ';	
               END IF;
       
               IF pParItemServTipo != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_itemserv_tipo' || ' like '|| '''%' || pParItemServTipo || '%'' ';	
               END IF;
               
               IF pParItemServOrigemFiscal != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_itemserv_origem_fiscal' || ' = '|| '''' || pParItemServOrigemFiscal || ''' ';	
               END IF;		
               
               IF pParItemServTipoComposi != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_itemserv_tipo_composicao ' || ' like '|| '''%' || pParItemServTipoComposi || '%'' ';	
               END IF;			
       
               IF pParItemServTipoCtbComp != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_itemserv_tipo_ctb_comp' || ' like '|| '''%' || pParItemServTipoCtbComp || '%'' ';	
               END IF;	
               
               IF pParItemServDocCnaeNfs != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_itemserv_fis_doc_cnae_nfs' || ' like '|| '''%' || pParItemServDocCnaeNfs || '%'' ';	
               END IF;	
               
               IF pParItemServSubGrupoId != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_itemserv_subgrupo_id' || ' in(''' ||pParItemServSubGrupoId||''')';
               END IF;	
       
               IF pParItemServSubGrupoNome != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_itemserv_subgrupo_nome' || ' like '|| '''%' || pParItemServSubGrupoNome || '%'' ';	
               END IF;		
               
               IF pParItemServSubGrupoAtivo != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_itemserv_subgrupo_ativo_desc' || ' like '|| '''%' || pParItemServSubGrupoAtivo || '%'' ';	
               END IF;			
               
               IF pParItemServGrupoId != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_itemserv_grupo_id' || ' in(''' ||pParItemServGrupoId||''')';
               END IF;			
           
               IF pParItemServGrupoNome != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_itemserv_grupo_nome' || ' like '|| '''%' || pParItemServGrupoNome || '%'' ';	
               END IF;		
               
               IF pParItemServGrupoAtivo != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_itemserv_grupo_ativo_desc' || ' like '|| '''%' || pParItemServGrupoAtivo || '%'' ';	
               END IF;		
       
               IF pParFisNcmId != '' THEN
                   vSql = vSql || 'and ' || ' t1.fis_ncm_id' || ' in(''' ||pParFisNcmId||''')';
               END IF;		
       
               IF pParFisNcmNome != '' THEN
                   vSql = vSql || 'and ' || ' t1.fis_ncm_nome' || ' like '|| '''%' || pParFisNcmNome || '%'' ';	
               END IF;		
       
               IF pParFisNcmAtivo != '' THEN
                   vSql = vSql || 'and ' || ' t1.fis_ncm_ativo_desc' || ' like '|| '''%' || pParFisNcmAtivo || '%'' ';	
               END IF;	
       
               IF pParFisNcmDataValidadeIni != '' and pParFisNcmDataValidadeFin != '' THEN
                 vSql = vSql || ' and ' || 'CAST(t1.fis_ncm_dt_validade AS DATE)' || ' >= ''' || pParFisNcmDataValidadeIni|| '''' || ' and  CAST(t1.fis_ncm_dt_validade AS DATE)' || ' <= ''' || pParFisNcmDataValidadeFin || '''';
               END IF;
       
               IF pParFisNcmNumero != '' THEN
                   vSql = vSql || 'and ' || ' t1.fis_ncm_nr_ncm' || ' like '|| '''%' || pParFisNcmNumero || '%'' ';	
               END IF;	
       
               IF pParUnidadeMedId != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_umedida_id' || ' in(''' ||pParUnidadeMedId||''')';
               END IF;	
               
               IF pParUnidadeMedNome != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_umedida_nome' || ' like '|| '''%' || pParUnidadeMedNome || '%'' ';	
               END IF;	
           
             IF pParUnidadeMedAtivo != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_umedida_ativo_desc' || ' like '|| '''%' || pParUnidadeMedAtivo || '%'' ';	
               END IF;	
       
               IF pParFisCestId != '' THEN
                   vSql = vSql || 'and ' || ' t1.fis_cest_id' || ' in(''' ||pParFisCestId||''')';
               END IF;	
       
             IF pParFisCestNome != '' THEN
                   vSql = vSql || 'and ' || ' t1.fis_cest_nome' || ' like '|| '''%' || pParFisCestNome || '%'' ';	
               END IF;	
       
             IF pParFisCestAtivo != '' THEN
                   vSql = vSql || 'and ' || ' t1.fis_cest_ativo_desc' || ' like '|| '''%' || pParFisCestAtivo || '%'' ';	
               END IF;	
               
               IF pParFisCestDataValidadeIni != '' and pParFisCestDataValidadeFin != '' THEN
                 vSql = vSql || ' and ' || 'CAST(t1.fis_cest_dt_validade AS DATE)' || ' >= ''' || pParFisCestDataValidadeIni|| '''' || ' and  CAST(t1.fis_cest_dt_validade AS DATE)' || ' <= ''' || pParFisCestDataValidadeFin || '''';
               END IF;
       
       
             IF pParFisCestNumero != '' THEN
                   vSql = vSql || 'and ' || ' t1.fis_cest_nr_cest' || ' like '|| '''%' || pParFisCestNumero || '%'' ';	
               END IF;
       
               IF pParFisNbsId != '' THEN
                   vSql = vSql || 'and ' || ' t1.fis_nbs_id' || ' in(''' ||pParFisNbsId||''')';
               END IF;					
       
             IF pParFisNbsNome != '' THEN
                   vSql = vSql || 'and ' || ' t1.fis_nbs_nome' || ' like '|| '''%' || pParFisNbsNome || '%'' ';	
               END IF;
       
             IF pParFisNbsAtivo != '' THEN
                   vSql = vSql || 'and ' || ' t1.fis_nbs_ativo_desc' || ' like '|| '''%' || pParFisNbsAtivo || '%'' ';	
               END IF;
       
               IF pParFisNbsDataValidadeIni != '' and pParFisNbsDataValidadeFin != '' THEN
                 vSql = vSql || ' and ' || 'CAST(t1.fis_nbs_dt_validade AS DATE)' || ' >= ''' || pParFisNbsDataValidadeIni|| '''' || ' and  CAST(t1.fis_nbs_dt_validade AS DATE)' || ' <= ''' || pParFisNbsDataValidadeFin || '''';
               END IF;
               
             IF pParFisNbsNumero != '' THEN
                   vSql = vSql || 'and ' || ' t1.fis_nbs_nr_nbs' || ' like '|| '''%' || pParFisNbsNumero || '%'' ';	
               END IF;		
               
               IF pParCtbId != '' THEN
                   vSql = vSql || 'and ' || ' t1.ctb_comp_id' || ' in(''' ||pParCtbId||''')';
               END IF;			
               
             IF pParCtbNome != '' THEN
                   vSql = vSql || 'and ' || ' t1.ctb_comp_nome' || ' like '|| '''%' || pParCtbNome || '%'' ';	
               END IF;		
               
             IF pParCtbAtivo != '' THEN
                   vSql = vSql || 'and ' || ' t1.ctb_comp_ativo_desc' || ' like '|| '''%' || pParCtbAtivo || '%'' ';	
               END IF;	
       
               IF pParLogUserIns != '' THEN
                   vSql = vSql || 'and ' || ' t1.log_user_ins' || ' like '|| '''%' ||pParLogUserIns|| '%'' ';
               END IF;
               
               IF pParLogDateInsIni != '' and pParLogDateInsFin != '' THEN
                 vSql = vSql || ' and ' || 'CAST(t1.log_date_ins AS DATE)' || ' >= ''' || pParLogDateInsIni|| '''' || ' and  CAST(t1.log_date_ins AS DATE)' || ' <= ''' || pParLogDateInsFin || '''';
               END IF;
               
               IF pParLogUserUpd != '' THEN
                   vSql = vSql || 'and ' || ' t1.log_user_upd' || ' like '|| '''%' ||pParLogUserUpd|| '%'' ';
               END IF;		
       
               IF pParLogDateUpdIni != '' and pParLogDateUpdFin != '' THEN
                 vSql = vSql || ' and ' || 'CAST(t1.log_date_upd AS DATE)' || ' >= ''' || pParLogDateUpdIni|| '''' || ' and  CAST(t1.log_date_upd AS DATE)' || ' <= ''' || pParLogDateUpdFin || '''';
               END IF;
       
       
       
            -- Group By
            -- ===================================
               vSql = vSql||' group by '|| pVart01;
       
               if  pVart02 != ''  THEN
                vSql = vSql||  ','|| pVart02;
               end if;
               
           if  pVart03 != ''  THEN
                vSql = vSql||  ','|| pVart03;
               end if;
               
           if  pVart04 != ''  THEN
                vSql = vSql||  ','|| pVart04;
               end if;
               
           if  pVart05 != ''  THEN
                vSql = vSql||  ','|| pVart05;
               end if;
               
            -- Order By
            -- ===================================
               vSql = vSql||' order by '|| pVart01;
       
               if  pVart02 != ''  THEN
                vSql = vSql||  ','|| pVart02;
               end if;
               
           if  pVart03 != ''  THEN
                vSql = vSql||  ','|| pVart03;
               end if;
               
           if  pVart04 != ''  THEN
                vSql = vSql||  ','|| pVart04;
               end if;
               
           if  pVart05 != ''  THEN
                vSql = vSql||  ','|| pVart05;
               end if;
           
           
           FOR r IN EXECUTE vSql loop
               ind_rel_id := pParIndRelId;
               ind_rel_par1 := vPar1;
               ind_rel_par2 := vPar2;
               ind_rel_par3 := vPar3;		
               vart_01 := r.vart_01;
               vard_01 := r.vard_01;
               vart_02 := r.vart_02;
               vard_02 := r.vard_02;
               vart_03 := r.vart_03;
               vard_03 := r.vard_03;
               vart_04 := r.vart_04;
               vard_04 := r.vard_04;
               vart_05 := r.vart_05;
               vard_05 := r.vard_05;
               valor_01 := r.valor_01;
       
           RETURN NEXT;
           
       END loop;
       raise notice'vSql :%',vSql;
       
       
       
       end;
       $BODY$
         LANGUAGE plpgsql VOLATILE;;
           
       
       
       -----------
       
       

       Drop FUNCTION IF EXISTS fnreport0023;;

       CREATE OR REPLACE FUNCTION fnreport0023(
       pParUnitId varchar, 
       pParIndRelId varchar, 
       pVart01 VARCHAR,
       pVard01 VARCHAR,
       pVart02 VARCHAR DEFAULT NULL,
       pVard02 VARCHAR DEFAULT NULL,
       pVart03 VARCHAR DEFAULT NULL,
       pVard03 VARCHAR DEFAULT NULL,
       pVart04 VARCHAR DEFAULT NULL,
       pVard04 VARCHAR DEFAULT NULL,
       pVart05 VARCHAR DEFAULT NULL,
       pVard05 VARCHAR DEFAULT NULL,
       pVart06 VARCHAR DEFAULT NULL,
       pVard06 VARCHAR DEFAULT NULL,
       pVart07 VARCHAR DEFAULT NULL,
       pVard07 VARCHAR DEFAULT NULL,
       pVart08 VARCHAR DEFAULT NULL,
       pVard08 VARCHAR DEFAULT NULL,
       pVart09 VARCHAR DEFAULT NULL,
       pVard09 VARCHAR DEFAULT NULL, 
       pVart10 VARCHAR DEFAULT NULL,
       pVard10 VARCHAR DEFAULT NULL,	
       
       pParMovId VARCHAR DEFAULT NULL,	
       pParMovSerie VARCHAR DEFAULT NULL,
       pParDataMovIni VARCHAR DEFAULT NULL,
       pParDataMovFin VARCHAR DEFAULT NULL,
       pParNrMov VARCHAR DEFAULT NULL,
       pParDataEntregaMovIni VARCHAR DEFAULT NULL,
       pParDataEntregaMovFin VARCHAR DEFAULT NULL,
       
       pParMovOperacaoId VARCHAR DEFAULT NULL,
       pParMovOperacaoNome VARCHAR DEFAULT NULL,
       pParMovOperacaoAtivo VARCHAR DEFAULT NULL,
       pParMovOperacaoSigla VARCHAR DEFAULT NULL,
       pParMovOperacaoTipoES VARCHAR DEFAULT NULL,
       
       
       pParMovTipoId VARCHAR DEFAULT NULL,
       pParMovTipoNome VARCHAR DEFAULT NULL,
       pParMovTipoAtivo VARCHAR DEFAULT NULL,
       pParMovTipoSigla VARCHAR DEFAULT NULL,
       pParMovTipoMov VARCHAR DEFAULT NULL,
       
       pParGerNumeracaoId VARCHAR DEFAULT NULL,
       pParGerNumeracaoNome VARCHAR DEFAULT NULL,
       pParGerNumeracaoAtivo VARCHAR DEFAULT NULL,
       pParGerNumeracaoSerie VARCHAR DEFAULT NULL,
       
       pParMovStatusId VARCHAR DEFAULT NULL,
       pParMovStatusNome VARCHAR DEFAULT NULL,
       pParMovStatusAtivo VARCHAR DEFAULT NULL,
       pParMovStatusSigla VARCHAR DEFAULT NULL,
       pParMovStatusTipo VARCHAR DEFAULT NULL,
       
       pParGerEmpresaId VARCHAR DEFAULT NULL,
       pParGerEmpresaNome VARCHAR DEFAULT NULL,
       pParGerEmpresaAtivo VARCHAR DEFAULT NULL,
       pParGerEmpresaSigla VARCHAR DEFAULT NULL,
       
       pParGerPessoaId VARCHAR DEFAULT NULL,
       pParGerPessoaNome VARCHAR DEFAULT NULL,
       pParGerPessoaAtivo VARCHAR DEFAULT NULL,
       pParGerPessoaSigla VARCHAR DEFAULT NULL,
       
       pParGerPessoaEnderecoAtivo VARCHAR DEFAULT NULL,
       pParGerPessoaEnderecoLograd VARCHAR DEFAULT NULL,
       pParGerPessoaEnderecoLogradNr VARCHAR DEFAULT NULL,
       pParGerPessoaEnderecoLogradBairro VARCHAR DEFAULT NULL,
       
       pParGerPessoaEntregId VARCHAR DEFAULT NULL,
       pParGerPessoaEntregNome VARCHAR DEFAULT NULL,
       pParGerPessoaEntregAtivo VARCHAR DEFAULT NULL,
       
       pParGerPessoaEntregEnderecoAtivo VARCHAR DEFAULT NULL,
       pParGerPessoaEntregEnderecoLograd VARCHAR DEFAULT NULL,
       pParGerPessoaEntregEnderecoLogradNr VARCHAR DEFAULT NULL,
       pParGerPessoaEntregEnderecoLogradBairro VARCHAR DEFAULT NULL,
       
       pParMovItemServId VARCHAR DEFAULT NULL,
       
       pParItemServId VARCHAR DEFAULT NULL,
       pParItemServNome VARCHAR DEFAULT NULL,
       pParItemServAtivo VARCHAR DEFAULT NULL,
       pParItemServSigla VARCHAR DEFAULT NULL,
       pParItemServTipo VARCHAR DEFAULT NULL,
       
       pParItemServSubGrupoId VARCHAR DEFAULT NULL,
       pParItemServSubGrupoNome VARCHAR DEFAULT NULL,
       pParItemServSubGrupoAtivo VARCHAR DEFAULT NULL,
       
       pParItemServGrupoId VARCHAR DEFAULT NULL,
       pParItemServGrupoNome VARCHAR DEFAULT NULL,
       pParItemServGrupoAtivo VARCHAR DEFAULT NULL,
       
       pParGerUmedidaId VARCHAR DEFAULT NULL,
       pParGerUmedidaNome VARCHAR DEFAULT NULL,
       pParGerUmedidaAtivo VARCHAR DEFAULT NULL,
       pParGerUmedidaSigla VARCHAR DEFAULT NULL,
       
       
       pParFisCfopId VARCHAR DEFAULT NULL,
       pParFisCfopNR VARCHAR DEFAULT NULL,
       pParFisCfopNome VARCHAR DEFAULT NULL,
       pParFisCfopAtivo VARCHAR DEFAULT NULL,
       pParFisCfopDataValidIni VARCHAR DEFAULT NULL,
       pParFisCfopDataValidFin VARCHAR DEFAULT NULL,
       
       pParLogUserIns VARCHAR DEFAULT NULL,
       pParLogDateInsIni VARCHAR DEFAULT NULL, 
       pParLogDateInsFin VARCHAR DEFAULT NULL, 
       pParLogUserUpd VARCHAR DEFAULT NULL,
       pParLogDateUpdIni VARCHAR DEFAULT NULL,
       pParLogDateUpdFin VARCHAR DEFAULT NULL		
       
       )
       RETURNS TABLE(
               ind_rel_id VARCHAR,
               ind_rel_par1 VARCHAR,
               ind_rel_par2 VARCHAR,
               ind_rel_par3 VARCHAR,
               ind_rel_par4 VARCHAR,
               vart_01 VARCHAR,
               vard_01 VARCHAR,
               vart_02 VARCHAR,
               vard_02 VARCHAR,
               vart_03 VARCHAR,
               vard_03 VARCHAR,
               vart_04 VARCHAR,
               vard_04 VARCHAR,
               vart_05 VARCHAR,
               vard_05 VARCHAR,
               vart_06 VARCHAR,
               vard_06 VARCHAR,
               vart_07 VARCHAR,
               vard_07 VARCHAR,
               vart_08 VARCHAR,
               vard_08 VARCHAR,
               vart_09 VARCHAR,
               vard_09 VARCHAR,
               vart_10 VARCHAR,
               vard_10 VARCHAR,
               valor_01 NUMERIC,
               valor_02 NUMERIC,
               valor_03 NUMERIC,
               valor_04 NUMERIC,
               valor_05 NUMERIC,
               valor_06 NUMERIC,
               valor_07 NUMERIC,
               valor_08 NUMERIC,
               valor_09 NUMERIC,
               valor_10 NUMERIC,
               valor_11 NUMERIC,
               valor_12 NUMERIC,
               valor_13 NUMERIC,
               valor_14 NUMERIC,
               valor_15 NUMERIC,
               valor_16 NUMERIC,
               valor_17 NUMERIC,
               valor_18 NUMERIC
        ) AS $BODY$
       declare
       vSql varchar;
       vPar1 varchar :='';
       vPar2 varchar :='';
       vPar3 varchar :='';
       vPar4 varchar :='';
       r record;
       
       begin
       
       
       
           if pParMovSerie != '' then
               vPar1 = vPar1||'Serie do Movimento ['||pParMovSerie||'] '||chr(13)||chr(10);			
           else
               vPar1 = vPar1||'Serie do Movimento [] '||chr(13)||chr(10);
           end if;
       
       
           if pParDataMovIni != '' and pParDataMovFin != '' then
               vPar1 := vPar1 || 'Data do Movimento de ['||pParDataMovIni||'] até ['||pParDataMovFin||']'|| chr(13) || chr(10);
           else
               vPar1 := vPar1 || 'Data do Movimento de [] até []'|| chr(13) || chr(10);	
           end if;
       
       
           if pParNrMov != '' then
               vPar1 := vPar1 ||'Nº do Movimento ['||pParNrMov||']'|| chr(13) || chr(10);
           else
               vPar1 := vPar1 ||'Nº do Movimento []'|| chr(13) || chr(10);	
           end if;
       
       
           if pParDataEntregaMovIni != '' and  pParDataEntregaMovFin != '' then
               vPar1 := vPar1 || 'Data Entrega do Movimento de ['||pParDataEntregaMovIni||'] até ['||pParDataEntregaMovFin||']'|| chr(13) || chr(10);
           else
               vPar1 := vPar1 || 'Data Entrega do Movimento de [] até []'|| chr(13) || chr(10);
           end if;
       
       
           if pParMovOperacaoId != '' then
               vPar1 = vPar1||'Operação do Movimento ['||fnreport_sigla(pParUnitId,'mov_operacao','sigla_mov_operacao','id',''''||pParMovOperacaoId||'''' ) ||'] '||chr(13)||chr(10);			
           else
               vPar1 = vPar1||'Operação do Movimento []'||chr(13)||chr(10);				
           end if;
       
           if pParMovOperacaoNome != '' then
               vPar1 = vPar1||'Nome Operação do Movimento ['||pParMovOperacaoNome||'] '||chr(13)||chr(10);			
           else
               vPar1 = vPar1||'Nome Operação do Movimento [] '||chr(13)||chr(10);
           end if;
       
           if pParMovOperacaoAtivo != '' then
               vPar1 = vPar1||'Operação do Movimento Ativo ['||pParMovOperacaoAtivo||'] '||chr(13)||chr(10);			
           else
               vPar1 = vPar1||'Operação do Movimento Ativo [] '||chr(13)||chr(10);
           end if;
       
           if pParMovOperacaoSigla != '' then
               vPar1 = vPar1||'Sigla Operação do Movimento ['||pParMovOperacaoSigla||'] '||chr(13)||chr(10);			
           else
               vPar1 = vPar1||'Sigla Operação do Movimento [] '||chr(13)||chr(10);
           end if;
               
           if pParMovOperacaoTipoES != '' then
               vPar1 = vPar1||'Operação do Movimento Tipo E/S ['||pParMovOperacaoTipoES||'] '||chr(13)||chr(10);			
           else
               vPar1 = vPar1||'Operação do Movimento Tipo E/S [] '||chr(13)||chr(10);
           end if;	
       
       
           if pParMovTipoId != '' then
               vPar1 = vPar1||'Tipo de Movimento ['||fnreport_sigla(pParUnitId,'mov_tipo','sigla_mov_tipo','id',''''||pParMovTipoId||'''' ) ||'] '||chr(13)||chr(10);			
           else
               vPar1 = vPar1||'Tipo de Movimento []'||chr(13)||chr(10);	
           end if;
       
       
           if pParMovTipoNome != '' then
                   vPar1 = vPar1||'Nome Tipo de Movimento ['||pParMovTipoNome||'] '||chr(13)||chr(10);	
           else
                   vPar1 = vPar1||'Nome Tipo de Movimento [] '||chr(13)||chr(10);		
           end if;
       
           if pParMovTipoAtivo != '' then
                   vPar1 = vPar1||'Tipo de Movimento Ativo ['||pParMovTipoAtivo||'] '||chr(13)||chr(10);	
           else
                   vPar1 = vPar1||'Tipo de Movimento Ativo[] '||chr(13)||chr(10);	
           end if;
           
           if pParMovTipoSigla != '' then
                   vPar1 = vPar1||'Sigla Tipo de Movimento ['||pParMovTipoSigla||'] '||chr(13)||chr(10);	
           else
                   vPar1 = vPar1||'Sigla Tipo de Movimento [] '||chr(13)||chr(10);	
           end if;	
           
           if pParMovTipoMov != '' then
                   vPar1 = vPar1||'Tipo do Movimento ['||pParMovTipoMov||'] '||chr(13)||chr(10);	
           else
                   vPar1 = vPar1||'Tipo do Movimento [] '||chr(13)||chr(10);	
           end if;	
           
           if pParGerNumeracaoId != '' then
               vPar1 = vPar1||'Numeração ['||fnreport_sigla(pParUnitId,'ger_numeracao','nome','id',''''||pParGerNumeracaoId||'''' ) ||'] '||chr(13)||chr(10);			
           else
               vPar1 = vPar1||'Numeração []'||chr(13)||chr(10);
           end if;	
           
           if pParGerNumeracaoNome != '' then
               vPar1 = vPar1||'Nome da Numeração ['||pParGerNumeracaoNome||'] '||chr(13)||chr(10);			
           else
               vPar1 = vPar1||'Nome da Numeração []'||chr(13)||chr(10);
           end if;		
       
           if pParGerNumeracaoAtivo != '' then
               vPar1 = vPar1||'Numeração Ativo ['||pParGerNumeracaoAtivo||'] '||chr(13)||chr(10);			
           else
               vPar1 = vPar1||'Numeração Ativo[]'||chr(13)||chr(10);
           end if;	
       
           if pParGerNumeracaoSerie != '' then
               vPar2 = vPar2||'Série Numeração ['||pParGerNumeracaoSerie||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Série Numeração []'||chr(13)||chr(10);
           end if;	
       
           if pParMovStatusId != '' then
               vPar2 = vPar2||'Status da Movimentação ['||fnreport_sigla(pParUnitId,'mov_status','sigla_mov_status','id',''''||pParMovStatusId||'''' ) ||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Status da Movimentação []'||chr(13)||chr(10);
           end if;	
           
           if pParMovStatusNome != '' then
               vPar2 = vPar2||'Nome Status da Movimentação ['||pParMovStatusNome||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Nome Status da Movimentação []'||chr(13)||chr(10);
           end if;	
           
           if pParMovStatusAtivo != '' then
               vPar2 = vPar2||'Status da Movimentação Ativo ['||pParMovStatusAtivo||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Status da Movimentação Ativo []'||chr(13)||chr(10);
           end if;
       
           if pParMovStatusSigla != '' then
               vPar2 = vPar2||'Sigla Status da Movimentação ['||pParMovStatusSigla||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Sigla Status da Movimentação []'||chr(13)||chr(10);
           end if;
       
           if pParMovStatusTipo != '' then
               vPar2 = vPar2||'Tipo Status da Movimentação ['||pParMovStatusTipo||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Tipo Status da Movimentação []'||chr(13)||chr(10);
           end if;
       
           if pParGerEmpresaId != '' then
               vPar2 = vPar2||'Empresa ['||fnreport_sigla(pParUnitId,'ger_empresa','sigla_empresa','id',''''||pParGerEmpresaId||'''' ) ||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Empresa []'||chr(13)||chr(10);
           end if;	
       
           if pParGerEmpresaNome != '' then
               vPar2 = vPar2||'Nome Empresa ['||pParGerEmpresaNome||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Nome Empresa []'||chr(13)||chr(10);
           end if;
       
           if pParGerEmpresaAtivo != '' then
               vPar2 = vPar2||'Empresa Ativo ['||pParGerEmpresaAtivo||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Empresa Ativo []'||chr(13)||chr(10);
           end if;
       
           if pParGerEmpresaSigla != '' then
               vPar2 = vPar2||'Sigla Empresa ['||pParGerEmpresaSigla||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Sigla Empresa []'||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaId != '' then
               vPar2 = vPar2||'Pessoa ['||fnreport_sigla(pParUnitId,'ger_pessoa','sigla_pes','id',''''||pParGerPessoaId||'''' ) ||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Pessoa []'||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaNome != ''  then
               vPar2 = vPar2||'Nome Pessoa ['||pParGerPessoaNome||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Nome Pessoa []'||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaAtivo != ''  then
               vPar2 = vPar2||'Pessoa Ativo ['||pParGerPessoaAtivo||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Pessoa Ativo []'||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaSigla != ''  then
               vPar2 = vPar2||'Sigla Pessoa ['||pParGerPessoaSigla||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Sigla Pessoa []'||chr(13)||chr(10);
           end if;
           
               
           if pParGerPessoaEnderecoAtivo != ''  then
               vPar2 = vPar2||'Endereço Pessoa Ativo ['||pParGerPessoaEnderecoAtivo||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Endereço Pessoa Ativo []'||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaEnderecoLograd != ''  then
               vPar2 = vPar2||'Endereço Pessoa Logradouro ['||pParGerPessoaEnderecoLograd||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Endereço Pessoa Logradouro []'||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaEnderecoLogradNr != ''  then
               vPar3 = vPar3||'Nº Endereço Pessoa ['||pParGerPessoaEnderecoLogradNr||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Nº Endereço Pessoa []'||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaEnderecoLogradBairro != ''  then
               vPar3 = vPar3||'Bairro Endereço Pessoa ['||pParGerPessoaEnderecoLogradBairro||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Bairro Endereço Pessoa []'||chr(13)||chr(10);
           end if;	
           
           if pParGerPessoaEntregId != '' then
               vPar3 = vPar3||'Pessoa Entrega ['||fnreport_sigla(pParUnitId,'ger_pessoa','sigla_pes','id',''''||pParGerPessoaEntregId||'''' ) ||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Pessoa Entrega []'||chr(13)||chr(10);
           end if;		
       
           if pParGerPessoaEntregNome != ''  then
               vPar3 = vPar3||'Nome Pessoa Entrega ['||pParGerPessoaEntregNome||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Nome Pessoa Entrega []'||chr(13)||chr(10);
           end if;	
       
           if pParGerPessoaEntregAtivo != ''  then
               vPar3 = vPar3||'Pessoa Entrega Ativo ['||pParGerPessoaEntregAtivo||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Pessoa Entrega Ativo []'||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaEntregEnderecoAtivo != ''  then
               vPar3 = vPar3||'Endereço Pessoa Entrega Ativo ['||pParGerPessoaEntregEnderecoAtivo||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Endereço Pessoa Entrega Ativo []'||chr(13)||chr(10);
           end if;
           
           if pParGerPessoaEntregEnderecoLograd != ''  then
               vPar3 = vPar3||'Endereço Pessoa Entrega Logradouro ['||pParGerPessoaEntregEnderecoLograd||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Endereço Pessoa Entrega Logradouro []'||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaEntregEnderecoLogradNr != ''  then
               vPar3 = vPar3||'Nº Endereço Pessoa Entrega ['||pParGerPessoaEntregEnderecoLogradNr||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Nº Endereço Pessoa Entrega []'||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaEntregEnderecoLogradBairro != ''  then
               vPar3 = vPar3||'Bairro Endereço Pessoa Entrega ['||pParGerPessoaEntregEnderecoLogradBairro||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Bairro Endereço Pessoa Entrega []'||chr(13)||chr(10);
           end if;
       
           if pParItemServId != '' then
               vPar3 = vPar3||'Item/Serviço ['||fnreport_sigla(pParUnitId,'ger_itemserv','sigla_itemserv','id',''''||pParItemServId||'''' ) ||'] '||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Item/Serviço []'||chr(13)||chr(10);
           end if;	
       
           if pParItemServNome != ''  then
               vPar3 = vPar3||'Nome Item/Serviço ['||pParItemServNome||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Nome Item/Serviço []'||chr(13)||chr(10);
           end if;
       
           if pParItemServAtivo != ''  then
               vPar3 = vPar3||'Item/Serviço Ativo ['||pParItemServAtivo||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Item/Serviço Ativo []'||chr(13)||chr(10);
           end if;
       
           if pParItemServSigla != ''  then
               vPar3 = vPar3||'Sigla Item/Serviço ['||pParItemServSigla||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Sigla Item/Serviço []'||chr(13)||chr(10);
           end if;
       
           if pParItemServTipo != ''  then
               vPar3 = vPar3||'Tipo Item/Serviço ['||pParItemServTipo||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Tipo Item/Serviço []'||chr(13)||chr(10);
           end if;
           if pParItemServSubGrupoId != '' then
               vPar3 = vPar3||'SubGrupo Item/Serviço ['||fnreport_sigla(pParUnitId,'ger_itemserv_subgrupo','nome','id',''''||pParItemServSubGrupoId||'''' ) ||'] '||chr(13)||chr(10);
           else
               vPar3 = vPar3||'SubGrupo Item/Serviço []'||chr(13)||chr(10);
           end if;
       
           if pParItemServSubGrupoNome != ''  then
               vPar3 = vPar3||'Nome SubGrupo Item/Serviço ['||pParItemServSubGrupoNome||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Nome SubGrupo Item/Serviço []'||chr(13)||chr(10);
           end if;
       
           if pParItemServSubGrupoAtivo != ''  then
               vPar4 = vPar4||'SubGrupo Item/Serviço Ativo ['||pParItemServSubGrupoAtivo||'] '||chr(13)||chr(10);			
           else
               vPar4 = vPar4||'SubGrupo Item/Serviço Ativo []'||chr(13)||chr(10);
           end if;
       
       
           if pParItemServGrupoId != '' then
               vPar4 = vPar4||'Grupo Item/Serviço ['||fnreport_sigla(pParUnitId,'ger_itemserv_grupo','nome','id',''''||pParItemServGrupoId||'''' ) ||'] '||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Grupo Item/Serviço []'||chr(13)||chr(10);
           end if;
       
           if pParItemServGrupoNome != ''  then
               vPar4 = vPar4||'Nome Grupo Item/Serviço ['||pParItemServGrupoNome||'] '||chr(13)||chr(10);			
           else
               vPar4 = vPar4||'Nome Grupo Item/Serviço []'||chr(13)||chr(10);
           end if;
       
           if pParItemServGrupoAtivo != ''  then
               vPar4 = vPar4||'Grupo Item/Serviço Ativo ['||pParItemServGrupoAtivo||'] '||chr(13)||chr(10);			
           else
               vPar4 = vPar4||'Grupo Item/Serviço Ativo []'||chr(13)||chr(10);
           end if;
       
           if pParGerUmedidaId != '' then
               vPar4 = vPar4||'Unidade de Medida ['||fnreport_sigla(pParUnitId,'ger_umedida','sigla_umedida','id',''''||pParGerUmedidaId||'''' ) ||'] '||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Unidade de Medida []'||chr(13)||chr(10);
           end if;
           
           if pParGerUmedidaNome != '' then
               vPar4 = vPar4||'Nome Unidade de Medida ['||pParGerUmedidaNome||'] '||chr(13)||chr(10);			
           else
               vPar4 = vPar4||'Nome Unidade de Medida []'||chr(13)||chr(10);
           end if;	
       
           if pParGerUmedidaAtivo != '' then
               vPar4 = vPar4||'Unidade de Medida Ativo ['||pParGerUmedidaAtivo||'] '||chr(13)||chr(10);			
           else
               vPar4 = vPar4||'Unidade de Medida Ativo []'||chr(13)||chr(10);
           end if;	
       
           if pParGerUmedidaSigla != '' then
               vPar4 = vPar4||'Sigla Unidade de Medida ['||pParGerUmedidaSigla||'] '||chr(13)||chr(10);			
           else
               vPar4 = vPar4||'Sigla Unidade de Medida []'||chr(13)||chr(10);
           end if;
       
           if pParFisCfopId != '' then
               vPar4 = vPar4||'Cfop ['||fnreport_sigla(pParUnitId,'fis_cfop','nome','id',''''||pParFisCfopId||'''' ) ||'] '||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Cfop []'||chr(13)||chr(10);
           end if;
       
           if pParFisCfopNR != '' then
               vPar4 = vPar4||'Nº Cfop ['||pParFisCfopNR||'] '||chr(13)||chr(10);			
           else
               vPar4 = vPar4||'Nº Cfop []'||chr(13)||chr(10);
           end if;
       
           if pParFisCfopNome != '' then
               vPar4 = vPar4||'Nome Cfop ['||pParFisCfopNome||'] '||chr(13)||chr(10);			
           else
               vPar4 = vPar4||'Nome Cfop []'||chr(13)||chr(10);
           end if;
           
           if pParFisCfopAtivo != '' then
               vPar4 = vPar4||'Cfop Ativo ['||pParFisCfopAtivo||'] '||chr(13)||chr(10);			
           else
               vPar4 = vPar4||'Cfop Ativo []'||chr(13)||chr(10);
           end if;
       
       
           if pParFisCfopDataValidIni != '' and  pParFisCfopDataValidFin != '' then
               vPar4 = vPar4||'Data Validade Cfop de ['||pParFisCfopDataValidIni||'] até ['||pParFisCfopDataValidFin||']'||chr(13)||chr(10);			
           else
               vPar4 = vPar4||'Data Validade Cfop de [] até []'||chr(13)||chr(10);
           end if;
       
           if pParLogUserIns != '' then
               vPar4 := vPar4 || 'Log Usuario Inserção [' ||pParLogUserIns|| '] ' || chr(13) || chr(10);
           else 
               vPar4 := vPar4 || 'Log Usuario Inserção []' || chr(13) || chr(10);
           end if;
           
           if pParLogUserUpd != ''  then
               vPar4 := vPar4 || 'Log Usuario Alteração [' ||pParLogUserUpd|| '] ' || chr(13) || chr(10);
           else 
               vPar4 := vPar4 || 'Log Usuario Alteração [] ' || chr(13) || chr(10);
           end if;
           
           if pParLogDateInsIni != '' and pParLogDateInsFin != '' then
           vPar4 := vPar4 || 'Log Data Inserção de [' ||pParLogDateInsIni|| '] até ['||pParLogDateInsFin||']'|| chr(13) || chr(10);
           else
           vPar4 := vPar4 || 'Log Data Inserção de [] até []' || chr(13) || chr(10);
           end if;
           
           if pParLogDateUpdIni != '' and pParLogDateUpdIni != '' then
           vPar4 := vPar4 || 'Log Data Alteração de [' || pParLogDateUpdIni || '] até [' ||pParLogDateUpdFin||']'|| chr(13) || chr(10);
           else
           vPar4 := vPar4 || 'Log Data Alteração de [] até []' || chr(13) || chr(10);
           end if;
           
           
           vSql = 'select
           '  || pVart01 ||'   as vart_01 '||
               ','''|| pVard01 ||''' as vard_01 ';
               
               if  pVart02 != ''  THEN
                vSql = vSql || ','  || pVart02 ||'   as vart_02 '||
                          ','''|| pVard02 ||''' as vard_02 ';
               else 
                  vSql = vSql || ',null as vart_02'||
                                      ',null as vard_02';
               end if;
           if  pVart03 != '' THEN
                vSql = vSql || ','  || pVart03 ||'   as vart_03 '||
                          ','''|| pVard03 ||''' as vard_03 ';
               else 
                  vSql = vSql || ',null as vart_03'||
                                      ',null as vard_03';
               end if;
           if  pVart04 != '' THEN
                vSql = vSql || ','  || pVart04 ||'   as vart_04 '||
                          ','''|| pVard04 ||''' as vard_04 ';
               else 
                  vSql = vSql || ',null as vart_04'||
                                      ',null as vard_04';
               end if;
               
           if  pVart05 != ''  THEN
                vSql = vSql || ','  || pVart05 ||'   as vart_05 '||
                          ','''|| pVard05 ||''' as vard_05 ';
               else 
                  vSql = vSql || ',null as vart_05'||
                                      ',null as vard_05';
               end if;
               
               if  pVart06 != ''  THEN
                vSql = vSql || ','  || pVart06 ||'   as vart_06 '||
                          ','''|| pVard06 ||''' as vard_06 ';
               else 
                  vSql = vSql || ',null as vart_06'||
                                      ',null as vard_06';
               end if;
       
               if  pVart07 != ''  THEN
                vSql = vSql || ','  || pVart07 ||'   as vart_07 '||
                          ','''|| pVard07 ||''' as vard_07 ';
               else 
                  vSql = vSql || ',null as vart_07'||
                                      ',null as vard_07';
               end if;
               
               if  pVart08 != ''  THEN
                vSql = vSql || ','  || pVart08 ||'   as vart_08 '||
                          ','''|| pVard08 ||''' as vard_08 ';
               else 
                  vSql = vSql || ',null as vart_08'||
                                      ',null as vard_08';
               end if;
       
               if  pVart09 != ''  THEN
                vSql = vSql || ','  || pVart09 ||'   as vart_09 '||
                          ','''|| pVard09 ||''' as vard_09 ';
               else 
                  vSql = vSql || ',null as vart_09'||
                                      ',null as vard_09';
               end if;
       
       --- 
               if  pVart10 != ''  THEN
                vSql = vSql || ','  || pVart10 ||'   as vart_10 '||
                          ','''|| pVard10 ||''' as vard_10 ';
               else 
                  vSql = vSql || ',null as vart_10'||
                                      ',null as vard_10';
               end if;
       
               vSql = vSql ||',
                   sum(t1.mov_itemserv_qnt_devolvida) as valor_01,
                   sum(t1.mov_itemserv_qnt_orig) as valor_02,
                   t1.mov_itemserv_valor_unit_orig as valor_03,
                   sum(t1.mov_itemserv_valor_bruto) as valor_04,
                   sum(t1.mov_itemserv_valor_liquido) as valor_05,
                   sum(t1.mov_itemserv_qnt_conv) as valor_06,
                   t1.mov_itemserv_valor_unit_conv as valor_07,
                   sum(t1.mov_itemserv_valor_desconto) as valor_08,
                   sum(t1.mov_itemserv_valor_acrecimo) as valor_09,
                   sum(t1.mov_itemserv_valor_outros) as valor_10,
                   sum(t1.mov_itemserv_valor_frete) as valor_11,
                   sum(t1.mov_itemserv_valor_seguro) as valor_12,
                   sum(t1.mov_itemserv_valor_tributo_retido) as valor_13,
                   sum(t1.mov_itemserv_valor_tributo_total) as valor_14,
                   sum(t1.mov_itemserv_valor_outros_tributo_ret) as valor_15,
                   sum(t1.mov_itemserv_valor_desconto_cond) as valor_16,
                   sum(t1.mov_itemserv_valor_desconto_incond) as valor_17,
                   sum(t1.mov_itemserv_valor_deducao) as valor_18
                   from vwmov_mov_itemserv t1 
                   inner join vwmov_mov t2
                   on t1.mov_id = t2.mov_id
                   where 1=1 ';
                   
                   
                   
               IF pParUnitId != '' THEN
                   vSql = vSql || 'and ' || ' t1.mov_itemserv_unit_id' || ' in(''' ||pParUnitId||''')';
               END IF;
       
               IF pParMovId != '' THEN
                   vSql = vSql || 'and ' || ' t2.mov_id ' || ' in(''' ||pParMovId||''')';		
               END IF;
               
               IF pParMovSerie != '' THEN
                   vSql = vSql || 'and ' || ' t2.mov_serie_mov ' ||' like'||'''%'||pParMovSerie||'%'' ';
               END IF;
               
               IF pParDataMovIni != '' and pParDataMovFin != '' THEN
                 vSql = vSql || ' and ' || 'CAST(t2.mov_data_mov AS DATE)' || ' >= ''' || pParDataMovIni|| '''' || ' and  CAST(t2.mov_data_mov AS DATE)' || ' <= ''' || pParDataMovFin || '''';	
               END IF;
       
               IF pParNrMov != '' THEN
                   vSql = vSql || 'and ' || ' t2.mov_numero_mov ' ||' = '||''||pParNrMov||'';
               END IF;
       
               IF pParDataEntregaMovIni != '' and pParDataEntregaMovFin != '' THEN
                 vSql = vSql || ' and ' || 'CAST(t2.mov_data_entrega AS DATE)' || ' >= ''' || pParDataEntregaMovIni|| '''' || ' and  CAST(t2.mov_data_entrega AS DATE)' || ' <= ''' || pParDataEntregaMovFin || '''';
               END IF;
       
               IF pParMovOperacaoId != '' THEN
                   vSql = vSql || 'and ' || ' t2.mov_operacao_id ' || ' in(''' ||pParMovOperacaoId||''')';	
               END IF;
       
               IF pParMovOperacaoNome != '' THEN
                   vSql = vSql ||' and '||'t2.mov_operacao_nome'||' like'||'''%'||pParMovOperacaoNome||'%'' ';
               END IF;
       
               IF pParMovOperacaoAtivo != '' THEN
                   vSql = vSql ||' and '||'t2.mov_operacao_ativo'||' like'||'''%'||pParMovOperacaoAtivo||'%'' ';
               END IF;
       
               IF pParMovOperacaoSigla != '' THEN
                   vSql = vSql ||' and '||'t2.mov_operacao_sigla'||' like'||'''%'||pParMovOperacaoSigla||'%'' ';
               END IF;
       
               IF pParMovOperacaoTipoES != '' THEN
                   vSql = vSql ||' and '||'t2.mov_operacao_tipo_es'||' like'||'''%'||pParMovOperacaoTipoES||'%'' ';
               END IF;
               
               IF pParMovTipoId != '' THEN
                   vSql = vSql || 'and ' || ' t2.mov_tipo_id ' || ' in(''' ||pParMovTipoId||''')';
               END IF;		
               
               IF pParMovTipoNome != '' THEN
                   vSql = vSql ||' and '||'t2.mov_tipo_nome'||' like'||'''%'||pParMovTipoNome||'%'' ';
               END IF;		
           
               IF pParMovTipoAtivo != '' THEN
                   vSql = vSql ||' and '||'t2.mov_tipo_ativo'||' like'||'''%'||pParMovTipoAtivo||'%'' ';
               END IF;	
               
               IF pParMovTipoSigla != '' THEN
                   vSql = vSql ||' and '||'t2.mov_tipo_sigla'||' like'||'''%'||pParMovTipoSigla||'%'' ';
               END IF;
       
               IF pParMovTipoMov != '' THEN
                   vSql = vSql ||' and '||'t2.mov_tipo_tipo_mov'||' like'||'''%'||pParMovTipoMov||'%'' ';		
               END IF;
               
               IF pParGerNumeracaoId != '' THEN
                   vSql = vSql || 'and ' || ' t2.ger_numeracao_id ' || ' in(''' ||pParGerNumeracaoId||''')';
               END IF;		
       
               IF pParGerNumeracaoNome != '' THEN
                   vSql = vSql ||' and '||'t2.ger_numeracao_nome'||' like'||'''%'||pParGerNumeracaoNome||'%'' ';
               END IF;		
       
               IF pParGerNumeracaoAtivo != '' THEN
                   vSql = vSql ||' and '||'t2.ger_numeracao_ativo'||' like'||'''%'||pParGerNumeracaoAtivo||'%'' ';
               END IF;	
       
               IF pParGerNumeracaoSerie != '' THEN
                   vSql = vSql || 'and ' || ' t2.ger_numeracao_serie ' ||' like'||'''%'||pParGerNumeracaoSerie||'%'' ';
               END IF;	
       
               IF pParMovStatusId != '' THEN
                   vSql = vSql || 'and ' || ' t2.mov_status_id ' || ' in(''' ||pParMovStatusId||''')';		
               END IF;	
       
               IF pParMovStatusNome != '' THEN
                   vSql = vSql ||' and '||'t2.mov_status_nome'||' like'||'''%'||pParMovStatusNome||'%'' ';
               END IF;	
       
               IF pParMovStatusAtivo != '' THEN
                   vSql = vSql ||' and '||'t2.mov_status_ativo'||' like'||'''%'||pParMovStatusAtivo||'%'' ';
               END IF;	
       
               IF pParMovStatusSigla != '' THEN
                   vSql = vSql ||' and '||'t2.mov_status_sigla'||' like'||'''%'||pParMovStatusSigla||'%'' ';
               END IF;
       
               IF pParMovStatusTipo != '' THEN
                   vSql = vSql ||' and '||'t2.mov_status_tipo_status'||' like'||'''%'||pParMovStatusTipo||'%'' ';
               END IF;
               
               IF pParGerEmpresaId != '' THEN
                   vSql = vSql || 'and ' || ' t2.ger_empresa_id ' || ' in(''' ||pParGerEmpresaId||''')';
               END IF;
       
               IF pParGerEmpresaNome != '' THEN
                   vSql = vSql ||' and '||'t2.ger_empresa_nome'||' like'||'''%'||pParGerEmpresaNome||'%'' ';
               END IF;
       
               IF pParGerEmpresaAtivo != '' THEN
                   vSql = vSql ||' and '||'t2.ger_empresa_ativo'||' like'||'''%'||pParGerEmpresaAtivo||'%'' ';
               END IF;
       
               IF pParGerEmpresaSigla != '' THEN
                   vSql = vSql ||' and '||'t2.ger_empresa_sigla'||' like'||'''%'||pParGerEmpresaSigla||'%'' ';
               END IF;
       
               IF pParGerPessoaId != '' THEN
                   vSql = vSql || 'and ' || ' t2.ger_pessoa_id ' || ' in(''' ||pParGerPessoaId||''')';
               END IF;
       
               IF pParGerPessoaNome != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_nome'||' like'||'''%'||pParGerPessoaNome||'%'' ';
               END IF;
       
               IF pParGerPessoaAtivo != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_ativo'||' like'||'''%'||pParGerPessoaAtivo||'%'' ';
               END IF;
       
               IF pParGerPessoaSigla != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_sigla_pes'||' like'||'''%'||pParGerPessoaSigla||'%'' ';
               END IF;
       
               IF pParGerPessoaEnderecoAtivo != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_endereco_ativo'||' like'||'''%'||pParGerPessoaEnderecoAtivo||'%'' ';
               END IF;
       
               IF pParGerPessoaEnderecoLograd != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_endereco_end_lograd'||' like'||'''%'||pParGerPessoaEnderecoLograd||'%'' ';		
               END IF;
       
               IF pParGerPessoaEnderecoLogradNr != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_endereco_lograd_nr'||' like'||'''%'||pParGerPessoaEnderecoLogradNr||'%'' ';		
               END IF;
       
               IF pParGerPessoaEnderecoLogradBairro != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_endereco_end_bairro'||' like'||'''%'||pParGerPessoaEnderecoLogradBairro||'%'' ';			
               END IF;
               
               IF pParGerPessoaEntregId != '' THEN
                   vSql = vSql || 'and ' || ' t2.ger_pessoa_entrega_id ' || ' in(''' ||pParGerPessoaEntregId||''')';
               END IF;
       
               IF pParGerPessoaEntregNome != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_entrega_nome'||' like'||'''%'||pParGerPessoaEntregNome||'%'' ';
               END IF;
       
               IF pParGerPessoaEntregAtivo != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_entrega_ativo'||' like'||'''%'||pParGerPessoaEntregAtivo||'%'' ';
               END IF;
       
               IF pParGerPessoaEntregEnderecoAtivo != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_endereco_entrega_ativo'||' like'||'''%'||pParGerPessoaEntregEnderecoAtivo||'%'' ';		
               END IF;
       
               IF pParGerPessoaEntregEnderecoLograd != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_endereco_entrega_end_lograd'||' like'||'''%'||pParGerPessoaEntregEnderecoLograd||'%'' ';		
               END IF;
       
               IF pParGerPessoaEntregEnderecoLogradNr != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_endereco_entrega_end_lograd_nr'||' like'||'''%'||pParGerPessoaEntregEnderecoLogradNr||'%'' ';				
               END IF;
       
               IF pParGerPessoaEntregEnderecoLogradBairro != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_endereco_entrega_end_bairro'||' like'||'''%'||pParGerPessoaEntregEnderecoLogradBairro||'%'' ';		
               END IF;
       
               -- Analisar forma item/serv ou mov/item/serv
               
               IF pParMovItemServId != '' THEN
                   vSql = vSql || 'and ' || ' t1.mov_itemserv_id ' || ' in(''' ||pParMovItemServId||''')';
               END IF;
               
               IF pParItemServId != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_item_serv_id ' || ' in(''' ||pParItemServId||''')';
               END IF;
       
               IF pParItemServNome != '' THEN
                   vSql = vSql ||' and '||'t1.ger_item_serv_nome'||' like'||'''%'||pParItemServNome||'%'' ';
               END IF;
       
               IF pParItemServAtivo != '' THEN
                   vSql = vSql ||' and '||'t1.ger_item_serv_ativo'||' like'||'''%'||pParItemServAtivo||'%'' ';
               END IF;
       
               IF pParItemServSigla != '' THEN
                   vSql = vSql ||' and '||'t1.ger_item_serv_sigla'||' like'||'''%'||pParItemServSigla||'%'' ';
               END IF;
       
               IF pParItemServTipo != '' THEN
                   vSql = vSql ||' and '||'t1.ger_item_serv_tipo'||' like'||'''%'||pParItemServTipo||'%'' ';
               END IF;
       
               IF pParItemServSubGrupoId != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_itemserv_subgrupo_id ' || ' in(''' ||pParItemServSubGrupoId||''')';
               END IF;
       
               IF pParItemServSubGrupoNome != '' THEN
                   vSql = vSql ||' and '||'t1.ger_itemserv_subgrupo_nome'||' like'||'''%'||pParItemServSubGrupoNome||'%'' ';
               END IF;
       
               IF pParItemServSubGrupoAtivo != '' THEN
                   vSql = vSql ||' and '||'t1.ger_itemserv_subgrupo_ativo'||' like'||'''%'||pParItemServSubGrupoAtivo||'%'' ';
               END IF;
       
               IF pParItemServGrupoId != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_itemserv_grupo_id ' || ' in(''' ||pParItemServGrupoId||''')';
               END IF;
               
               IF pParItemServGrupoNome != '' THEN
                   vSql = vSql ||' and '||'t1.ger_itemserv_grupo_nome'||' like'||'''%'||pParItemServGrupoNome||'%'' ';		
               END IF;
       
               IF pParItemServGrupoAtivo != '' THEN
                   vSql = vSql ||' and '||'t1.ger_itemserv_grupo_ativo'||' like'||'''%'||pParItemServGrupoAtivo||'%'' ';
               END IF;
       
               IF pParGerUmedidaId != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_umedida_id ' || ' in(''' ||pParGerUmedidaId||''')';
               END IF;
       
               IF pParGerUmedidaNome != '' THEN
                   vSql = vSql ||' and '||'t1.ger_umedida_nome'||' like'||'''%'||pParGerUmedidaNome||'%'' ';
               END IF;
       
               IF pParGerUmedidaAtivo != '' THEN
                   vSql = vSql ||' and '||'t1.ger_umedida_ativo'||' like'||'''%'||pParGerUmedidaAtivo||'%'' ';
               END IF;
       
               IF pParGerUmedidaSigla != '' THEN
                   vSql = vSql ||' and '||'t1.ger_umedida_sigla'||' like'||'''%'||pParGerUmedidaSigla||'%'' ';
               END IF;
       
               IF pParFisCfopId != '' THEN
                   vSql = vSql || 'and ' || ' t1.fis_cfop_id ' || ' in(''' ||pParFisCfopId||''')';
               END IF;
       
               IF pParFisCfopNR != '' THEN
                   vSql = vSql || 'and ' || ' t1.fis_cfop_nr_cfop ' ||' like'||'''%'||pParFisCfopNR||'%'' ';
               END IF;
               
               IF pParFisCfopNome != '' THEN
                   vSql = vSql || 'and ' || ' t1.fis_cfop_nome ' ||' like'||'''%'||pParFisCfopNome||'%'' ';
               END IF;
       
               IF pParFisCfopAtivo != '' THEN
                   vSql = vSql || 'and ' || ' t1.fis_cfop_ativo ' ||' like'||'''%'||pParFisCfopAtivo||'%'' ';
               END IF;
               
               IF pParFisCfopDataValidIni != '' and pParFisCfopDataValidFin != '' THEN
                 vSql = vSql || ' and ' || 'CAST(t1.fis_cfop_data_validade AS DATE)' || ' >= ''' ||pParFisCfopDataValidIni|| '''' || ' and  CAST(t1.fis_cfop_data_validade AS DATE)' || ' <= ''' ||pParFisCfopDataValidFin || '''';		
               END IF;
       
               IF pParLogUserIns != '' THEN
                       vSql = vSql || 'and ' || ' t1.log_user_ins' || ' like '|| '''%' ||pParLogUserIns|| '%'' ';
               END IF;
                   
               IF pParLogDateInsIni != '' AND pParLogDateInsFin != '' THEN
                   vSql = vSql || ' and ' || 'CAST(t1.log_date_ins AS DATE)' || ' >= ''' || pParLogDateInsIni|| '''' || ' and  CAST(t1.log_date_ins AS DATE)' || ' <= ''' || pParLogDateInsFin || '''';
               END IF;
               
               IF pParLogUserUpd != '' THEN
                   vSql = vSql || 'and ' || ' t1.log_user_upd' || ' like '|| '''%' ||pParLogUserUpd|| '%'' ';
               END IF;		
       
               IF pParLogDateUpdIni != '' and pParLogDateUpdFin != '' THEN
                   vSql = vSql || ' and ' || 'CAST(t1.log_date_upd AS DATE)' || ' >= ''' || pParLogDateUpdIni|| '''' || ' and  CAST(t1.log_date_upd AS DATE)' || ' <= ''' || pParLogDateUpdFin || '''';
               END IF;
       
       
       
               -- Group By
            -- ===================================
               vSql = vSql||' group by valor_03, valor_07, '|| pVart01;
       
               if  pVart02 != ''  THEN
                vSql = vSql||  ','|| pVart02;
               end if;
               
           if  pVart03 != ''  THEN
                vSql = vSql||  ','|| pVart03;
               end if;
               
           if  pVart04 != ''  THEN
                vSql = vSql||  ','|| pVart04;
               end if;
               
           if  pVart05 != ''  THEN
                vSql = vSql||  ','|| pVart05;
               end if;
           
               if  pVart06 != ''  THEN
                vSql = vSql||  ','|| pVart06;
               end if;
       
               if  pVart07 != ''  THEN
                vSql = vSql||  ','|| pVart07;
               end if;
       
               if  pVart08 != ''  THEN
                vSql = vSql||  ','|| pVart08;
               end if;		
               
               if  pVart09 != ''  THEN
                vSql = vSql||  ','|| pVart09;
               end if;	
               
               if  pVart10 != ''  THEN
                vSql = vSql||  ','|| pVart10;
               end if;			
               
               
            -- Order By
            -- ===================================
               vSql = vSql||' order by '|| pVart01;
       
               if  pVart02 != ''  THEN
                vSql = vSql||  ','|| pVart02;
               end if;
               
           if  pVart03 != ''  THEN
                vSql = vSql||  ','|| pVart03;
               end if;
               
           if  pVart04 != ''  THEN
                vSql = vSql||  ','|| pVart04;
               end if;
               
           if  pVart05 != ''  THEN
                vSql = vSql||  ','|| pVart05;
               end if;
               
           if  pVart06 != ''  THEN
                vSql = vSql||  ','|| pVart06;
               end if;
       
           if  pVart07 != ''  THEN
                vSql = vSql||  ','|| pVart07;
               end if;
       
           if  pVart08 != ''  THEN
                vSql = vSql||  ','|| pVart08;
               end if;
       
           if  pVart09 != ''  THEN
                vSql = vSql||  ','|| pVart09;
               end if;
           
               if  pVart10 != ''  THEN
                vSql = vSql||  ','|| pVart10;
               end if;
       
       
               raise notice 'vSql :%', vSql;
       
       
       
               for r in EXECUTE vSql loop
                   ind_rel_id := pParIndRelId;
                   ind_rel_par1 := vPar1;
                   ind_rel_par2 := vPar2;
                   ind_rel_par3 := vPar3;
                   ind_rel_par4 := vPar4;
                    vart_01 := r.vart_01;
                    vard_01 := r.vard_01;
                    vart_02 := r.vart_02;
                    vard_02 := r.vard_02;
                    vart_03 := r.vart_03;
                    vard_03 := r.vard_03;
                    vart_04 := r.vart_04;
                    vard_04 := r.vard_04;
                    vart_05 := r.vart_05;
                    vard_05 := r.vard_05;
                    valor_01 := r.valor_01;
                    valor_02 := r.valor_02;
                    valor_03 := r.valor_03;
                    valor_04 := r.valor_04;
                    valor_05 := r.valor_05;
                    valor_06 := r.valor_06;
                    valor_07 := r.valor_07;
                    valor_08 := r.valor_08;
                    valor_09 := r.valor_09;
                    valor_10 := r.valor_10;
                    valor_11 := r.valor_11;
                    valor_12 := r.valor_12;
                    valor_13 := r.valor_13;
                    valor_14 := r.valor_14;
                    valor_15 := r.valor_15;
                    valor_16 := r.valor_16;
                    valor_17 := r.valor_17;
                    valor_18 := r.valor_18;
                    
                   return next;
                   raise notice 'vSql :%', vSql;
               end loop;
               return;
       
       
       
       end;
       $BODY$
         LANGUAGE plpgsql VOLATILE;;
       
       
       -----------
       
       

       Drop FUNCTION IF EXISTS fnreport0025;;

       CREATE OR REPLACE FUNCTION fnreport0025(
       pParUnitId varchar, 
       pParIndRelId varchar, 
       pVart01 varchar, 
       pVard01 varchar, 
       pVart02 varchar default null,
       pVard02 varchar default null,
       pVart03 varchar default null,
       pVard03 varchar default null,
       pVart04 varchar default null,
       pVard04 varchar default null,
       pVart05 varchar default null,
       pVard05 varchar default null,
       pParOcorMovDataMovIni varchar default null,
       pParOcorMovDataMovFin varchar default null,
       pParOcorMovNr varchar default null,
       pParGerEmpresaNome varchar default null,
       pParGerEmpresaAtivo varchar default null,
       pParGerEmpresaDocCnpj varchar default null,
       pParGerEmpresaDocCpf varchar default null,
       pParGerPessoaEnderecoLograd varchar default null,
       pParGerPessoaEnderecoLogradNr varchar default null,
       pParGerCidadeNome varchar default null,
       pParUfNome varchar default null,
       pParOcorTipoNome varchar default null,
       pParOcorTipoAtivo varchar default null,
       pParOcorTipoSigla varchar default null,
       pParOcorTipoObrigCompart varchar default null,
       pParOcorTipoTp varchar default null,
       pParOcorMovDetQntOcor varchar default null,
       pParOcorMovDetQntOcorCalc varchar default null,
       pParOcorMovDetDtStatusIni varchar default null,
       pParOcorMovDetDtStatusFin varchar default null,
       pParOcorNome varchar default null,
       pParOcorAtivo varchar default null,
       pParOcorSigla varchar default null,
       pParOcorTipo varchar default null,
       pParOcorTipoLanc varchar default null,
       pParOcorGrupoNome varchar default null,
       pParOcorGrupoAtivo varchar default null,
       pParOcorGrupoSigla varchar default null,
       pParGerUmedidaNome varchar default null,
       pParGerUmedidaAtivo varchar default null,
       pParGerUmedidaSigla varchar default null,
       pParOcorStatusNome varchar default null,
       pParOcorStatusAtivo varchar default null,
       pParOcorStatusSigla varchar default null,
       pParOcorStatusTipo varchar default null,
       pParOpeAreaQntAreaProd varchar default null,
       pParOpeAreaQntAreaImprod varchar default null,
       pParOpeAreaQntPlantEstand varchar default null,
       pParOpeAreaBlocoCol varchar default null,
       pParOpeAreaDtIniPlan varchar default null,
       pParOpeAreaDtIniPlanFin varchar default null,
       pParOpeAreaDtFinPlanIni varchar default null,
       pParOpeAreaDtFinPlan varchar default null,
       pParOpeAreaDtUltPlanIni varchar default null,
       pParOpeAreaDtUltPlanFin varchar default null,
       pParOpeAreaDtIniCol varchar default null,
       pParOpeAreaDtIniColFin varchar default null,
       pParOpeAreaDtFinColIni varchar default null,
       pParOpeAreaDtFinCol varchar default null,
       pParOpeAreaDtUltColIni varchar default null,
       pParOpeAreaDtUltColFin varchar default null,
       pParOpeAreaDtFlorada1Ini varchar default null,
       pParOpeAreaDtFlorada1Fin varchar default null,
       pParOpeAreaDtEmergIni varchar default null,
       pParOpeAreaDtEmergFin varchar default null,
       pParOpeAreaUmedidaNome varchar default null,
       pParOpeAreaUmedidaSigla varchar default null,
       pParCentro2Nome varchar default null,
       pParCentro2Sigla varchar default null,
       pParCentro2Ativo varchar default null,
       pParCentro2TipoDestinacao varchar default null,
       pParCentro2TipoProp varchar default null,
       pParCentro1Nome varchar default null,
       pParCentro1Ativo varchar default null,
       pParCentro1Sigla varchar default null,
       pParAreaSistemaCultNome varchar default null,
       pParAreaSistemaCultSigla varchar default null,
       pParLogUserIns varchar default null,
       pParLogDateInsIni varchar default null,
       pParLogDateInsFin varchar default null,
       pParLogUserUpd varchar default null,
       pParLogDateUpdIni varchar default null,
       pParLogDateUpdFin varchar default null
       
       )
       RETURNS TABLE(
        ind_rel_id varchar,
        ind_rel_par1 varchar,
        ind_rel_par2 varchar,
        ind_rel_par3 varchar,
        ind_rel_par4 varchar,
        vart_01 varchar,
        vard_01 varchar,
        vart_02 varchar,
        vard_02 varchar,
        vart_03 varchar,
        vard_03 varchar,
        vart_04 varchar,
        vard_04 varchar,
        vart_05 varchar,
        vard_05 varchar,
        valor_01 numeric,
        valor_02 numeric,
        valor_03 numeric,
        valor_04 numeric,
        valor_05 numeric,
        valor_06 numeric,
        valor_07 numeric,
        valor_08 numeric,
        valor_09 numeric,
        valor_10 numeric) AS $BODY$
       DECLARE
       vSql varchar;
       vPar1 varchar :='';
       vPar2 varchar :='';
       vPar3 varchar :='';
       vPar4 varchar :='';
       r record;
       
       begin
       
       
           if pParOcorMovNr != '' THEN
               vPar1 = vPar1||'Número do Movimento ['||pParOcorMovNr||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Número do Movimento [] '||chr(13)||chr(10);
           end if;
           
           if pParGerEmpresaNome != '' THEN
               vPar1 = vPar1||'Empresa ['||pParGerEmpresaNome||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Empresa []'||chr(13)||chr(10);
           end if;
       
           if pParGerEmpresaAtivo != '' THEN	
               vPar1 = vPar1||'Empresa Ativo ['||pParGerEmpresaAtivo||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Empresa Ativo []'||chr(13)||chr(10);
           end if;
           
           if pParGerEmpresaDocCnpj != '' THEN	
               vPar1 = vPar1||'CNPJ Empresa ['||pParGerEmpresaDocCnpj||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'CNPJ Empresa []'||chr(13)||chr(10);
           end if;
           
           if pParGerEmpresaDocCpf != '' THEN	
               vPar1 = vPar1||'CPF Empresa ['||pParGerEmpresaDocCpf||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'CPF Empresa []'||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaEnderecoLograd != '' THEN	
               vPar1 = vPar1||'Endereço ['||pParGerPessoaEnderecoLograd||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Endereço []'||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaEnderecoLogradNr != '' THEN	
               vPar1 = vPar1||'Nº Endereço ['||pParGerPessoaEnderecoLogradNr||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Nº Endereço []'||chr(13)||chr(10);
           end if;
           
           if pParGerCidadeNome != '' THEN	
               vPar1 = vPar1||'Cidade ['||pParGerCidadeNome||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Cidade []'||chr(13)||chr(10);
           end if;	
       
           if pParUfNome != '' THEN	
               vPar1 = vPar1||'Estado ['||pParUfNome||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Estado []'||chr(13)||chr(10);
           end if;	
       
           if pParOcorTipoNome != '' THEN	
               vPar1 = vPar1||'Nome Tipo Ocorrência ['||pParOcorTipoNome||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Nome Tipo Ocorrência []'||chr(13)||chr(10);
           end if;
       
           if pParOcorTipoAtivo != '' THEN	
               vPar1 = vPar1||'Tipo Ocorrência Ativo ['||pParOcorTipoAtivo||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Tipo Ocorrência Ativo []'||chr(13)||chr(10);
           end if;
           
           if pParOcorTipoSigla != '' THEN	
               vPar1 = vPar1||'Sigla Tipo Ocorrência ['||pParOcorTipoSigla||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Sigla Tipo Ocorrência []'||chr(13)||chr(10);
           end if;
           
           if pParOcorTipoObrigCompart != '' THEN	
               vPar1 = vPar1||'Tipo Ocorrência Obrigatorio ['||pParOcorTipoObrigCompart||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Tipo Ocorrência Obrigatorio []'||chr(13)||chr(10);
           end if;
       
           if pParOcorTipoTp != '' THEN	
               vPar1 = vPar1||'Tipo Ocorrência ['||pParOcorTipoTp||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Tipo Ocorrência []'||chr(13)||chr(10);
           end if;
           
           if pParOcorMovDetQntOcor != '' THEN	
               vPar1 = vPar1||'Quantidade da Ocorrência ['||pParOcorMovDetQntOcor||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Quantidade da Ocorrência []'||chr(13)||chr(10);
           end if;
       
           if pParOcorMovDetQntOcorCalc != '' THEN	
               vPar2 = vPar2||'Quantidade Cálculada da Ocorrência ['||pParOcorMovDetQntOcorCalc||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Quantidade Cálculada da Ocorrência []'||chr(13)||chr(10);
           end if;
       
           if pParOcorNome != '' THEN	
               vPar2 = vPar2||'Ocorrência ['||pParOcorNome||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Ocorrência []'||chr(13)||chr(10);
           end if;
       
           if pParOcorAtivo != '' THEN	
               vPar2 = vPar2||'Ocorrência Ativa ['||pParOcorAtivo||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Ocorrência Ativa []'||chr(13)||chr(10);
           end if;
           
           if pParOcorSigla != '' THEN	
               vPar2 = vPar2||'Sigla Ocorrência ['||pParOcorSigla||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Sigla Ocorrência []'||chr(13)||chr(10);
           end if;
       
           if pParOcorTipo != '' THEN	
               vPar2 = vPar2||'Tipo Ocorrência ['||pParOcorTipo||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Tipo Ocorrência []'||chr(13)||chr(10);
           end if;
           
           if pParOcorTipoLanc != '' THEN	
               vPar2 = vPar2||'Tipo Lancamento Ocorrência ['||pParOcorTipoLanc||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Tipo Lancamento Ocorrência []'||chr(13)||chr(10);
           end if;
           
           if pParOcorGrupoNome != '' THEN	
               vPar2 = vPar2||'Grupo de Ocorrência ['||pParOcorGrupoNome||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Grupo de Ocorrência []'||chr(13)||chr(10);
           end if;
           
           if pParOcorGrupoAtivo != '' THEN	
               vPar2 = vPar2||'Grupo de Ocorrência Ativo ['||pParOcorGrupoAtivo||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Grupo de Ocorrência Ativo []'||chr(13)||chr(10);
           end if;
       
           if pParOcorGrupoSigla != '' THEN	
               vPar2 = vPar2||'Sigla Grupo de Ocorrência ['||pParOcorGrupoSigla||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Sigla Grupo de Ocorrência []'||chr(13)||chr(10);
           end if;
       
           if pParGerUmedidaNome != '' THEN	
               vPar2 = vPar2||'U. Medida Ocorrência ['||pParGerUmedidaNome||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'U. Medida Ocorrência []'||chr(13)||chr(10);
           end if;
       
           if pParGerUmedidaAtivo != '' THEN	
               vPar2 = vPar2||'U. Medida Ocorrência Ativo ['||pParGerUmedidaAtivo||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'U. Medida Ocorrência Ativo []'||chr(13)||chr(10);
           end if;
           
           if pParGerUmedidaSigla != '' THEN	
               vPar2 = vPar2||'Sigla U. Medida Ocorrência ['||pParGerUmedidaSigla||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Sigla U. Medida Ocorrência []'||chr(13)||chr(10);
           end if;	
       
           if pParOcorStatusNome != '' THEN	
               vPar2 = vPar2||'Status da Ocorrência ['||pParOcorStatusNome||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Status da Ocorrência []'||chr(13)||chr(10);
           end if;	
       
           if pParOcorStatusAtivo != '' THEN	
               vPar2 = vPar2||'Status da Ocorrência Ativo ['||pParOcorStatusAtivo||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Status da Ocorrência Ativo []'||chr(13)||chr(10);
           end if;	
       
           if pParOcorStatusSigla != '' THEN	
               vPar2 = vPar2||'Sigla Status da Ocorrência ['||pParOcorStatusSigla||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Sigla Status da Ocorrência []'||chr(13)||chr(10);
           end if;	
       
           if pParOcorStatusTipo != '' THEN	
               vPar3 = vPar3||'Tipo Status da Ocorrência ['||pParOcorStatusTipo||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Tipo Status da Ocorrência []'||chr(13)||chr(10);
           end if;	
       
           if pParOpeAreaQntAreaProd != '' THEN
               vPar3 = vPar3||'Qnt Area Produtiva ['||pParOpeAreaQntAreaProd||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Qnt Area Produtiva []'||chr(13)||chr(10);
           end if;
       
           if pParOpeAreaQntAreaImprod != '' THEN
               vPar3 = vPar3||'Qntd. Area Improdutiva ['||pParOpeAreaQntAreaImprod||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Qntd. Area Improdutiva []'||chr(13)||chr(10);
           end if;		
       
           if pParOpeAreaQntPlantEstand != '' THEN
               vPar3 = vPar3||'Qntd. de Plantas Estande ['||pParOpeAreaQntPlantEstand||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Qntd. de Plantas Estande []'||chr(13)||chr(10);
           end if;
       
           if pParOpeAreaBlocoCol != '' THEN
               vPar3 = vPar3||'Bloco de Colheita ['||pParOpeAreaBlocoCol||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Bloco de Colheita []'||chr(13)||chr(10);
           end if;
       
           if pParOpeAreaUmedidaNome != '' THEN
               vPar3 = vPar3||'U. Medida Área ['||pParOpeAreaUmedidaNome||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'U. Medida Área []'||chr(13)||chr(10);
           end if;
           
           if pParOpeAreaUmedidaSigla != '' THEN
               vPar3 = vPar3||'Sigla U. Medida Área ['||pParOpeAreaUmedidaSigla||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Sigla U. Medida Área []'||chr(13)||chr(10);
           end if;
       
           if pParCentro2Nome != '' THEN
               vPar3 = vPar3||'Nome Centro 2 ['||pParCentro2Nome||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Nome Centro 2 []'||chr(13)||chr(10);
           end if;
       
           if pParCentro2Sigla != '' THEN
               vPar3 = vPar3||'Sigla Centro 2 ['||pParCentro2Sigla||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Sigla Centro 2 []'||chr(13)||chr(10);
           end if;
       
           if pParCentro2Ativo != '' THEN
               vPar3 = vPar3||'Centro 2 Ativo ['||pParCentro2Ativo||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Centro 2 Ativo []'||chr(13)||chr(10);
           end if;
       
           if pParCentro2TipoDestinacao != '' THEN
               vPar3 = vPar3||'Tipo Destinação Centro 2 ['||pParCentro2TipoDestinacao||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Tipo Destinação Centro 2 []'||chr(13)||chr(10);
           end if;
       
           if pParCentro2TipoProp != '' THEN
               vPar3 = vPar3||'Tipo Proprietário ['||pParCentro2TipoProp||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Tipo Proprietário []'||chr(13)||chr(10);
           end if;
       
           if pParCentro1Nome != '' THEN
               vPar3 = vPar3||'Nome Centro 1 ['||pParCentro1Nome||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Nome Centro 1 []'||chr(13)||chr(10);
           end if;
       
           if pParCentro1Ativo != '' THEN
               vPar3 = vPar3||'Centro 1 Ativo ['||pParCentro1Ativo||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Centro 1 Ativo []'||chr(13)||chr(10);
           end if;
       
           if pParCentro1Sigla != '' THEN
               vPar3 = vPar3||'Sigla Centro 1 ['||pParCentro1Sigla||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Sigla Centro 1 []'||chr(13)||chr(10);
           end if;
       
           if pParAreaSistemaCultNome != '' THEN
               vPar4 = vPar4||'Sistema Atividade Cultivo ['||pParAreaSistemaCultNome||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Sistema Atividade Cultivo []'||chr(13)||chr(10);
           end if;
       
           if pParAreaSistemaCultSigla != '' THEN
               vPar4 = vPar4||'Sigla Sistema Atividade Cultivo ['||pParAreaSistemaCultSigla||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Sigla Sistema Atividade Cultivo []'||chr(13)||chr(10);
           end if;
       
       
           if pParLogUserIns != '' then
               vPar4 = vPar4||'Log Usuario Inserção ['||pParLogUserIns||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Log Usuario Inserção []'||chr(13)||chr(10);
           end if;
       
           if pParLogUserUpd != '' then
               vPar4 = vPar4||'Log Usuario Alteração ['||pParLogUserUpd||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Log Usuario Alteração []'||chr(13)||chr(10);
           end if;
       
       -- Datas
           if pParLogDateInsIni != '' and pParLogDateInsFin != '' then
               vPar4 = vPar4||'Data Inserção de ['||pParLogDateInsIni||'] até ['||pParLogDateInsFin||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Data Inserção de [] até []'||chr(13)||chr(10);
           end if;
       
           if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then
               vPar4 = vPar4||'Data Alteração de ['||pParLogDateUpdIni||'] até ['||pParLogDateUpdFin||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Data Alteração de [] até []'||chr(13)||chr(10);
           end if;
       
           if pParOcorMovDataMovIni != '' and pParOcorMovDataMovFin != '' THEN	
               vPar4 = vPar4||'Data do Movimento de ['||pParOcorMovDataMovIni||'] até ['||pParOcorMovDataMovFin||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Data do Movimento de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParOcorMovDetDtStatusIni != '' and pParOcorMovDetDtStatusFin != '' THEN
               vPar4 = vPar4||'Data Status Ocorrência de ['||pParOcorMovDetDtStatusIni||'] até ['||pParOcorMovDetDtStatusFin||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Data Status Ocorrência de [] até []'||chr(13)||chr(10);
           end if;
       
       
           if pParOpeAreaDtIniPlan != '' and pParOpeAreaDtIniPlanFin != '' THEN
               vPar4 = vPar4||'Data Inicial Plantio de ['||pParOpeAreaDtIniPlan||'] até ['||pParOpeAreaDtIniPlanFin||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Data Inicial Plantio de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParOpeAreaDtFinPlanIni != '' and pParOpeAreaDtFinPlan != '' THEN
               vPar4 = vPar4||'Data Final Plantio de ['||pParOpeAreaDtFinPlanIni||'] até ['||pParOpeAreaDtFinPlan||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Data Final Plantio de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParOpeAreaDtUltPlanIni != '' and pParOpeAreaDtUltPlanFin != '' THEN
               vPar4 = vPar4||'Data Último Plantio de ['||pParOpeAreaDtUltPlanIni||'] até ['||pParOpeAreaDtUltPlanFin||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Data Último Plantio de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParOpeAreaDtIniCol != '' and pParOpeAreaDtIniColFin != '' THEN
               vPar4 = vPar4||'Data Inicial Colheita de ['||pParOpeAreaDtIniCol||'] até ['||pParOpeAreaDtIniColFin||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Data Inicial Colheita de [] até []'||chr(13)||chr(10);
           end if;
           
       
           if pParOpeAreaDtFinColIni != '' and pParOpeAreaDtFinCol != '' THEN
               vPar4 = vPar4||'Data Final Colheita de ['||pParOpeAreaDtFinColIni||'] até ['||pParOpeAreaDtFinCol||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Data Final Colheita de [] até []'||chr(13)||chr(10);
           end if;
       
       
           if pParOpeAreaDtUltColIni != '' and pParOpeAreaDtUltColFin != '' THEN
               vPar4 = vPar4||'Data Última Colheita de ['||pParOpeAreaDtUltColIni||'] até ['||pParOpeAreaDtUltColFin||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Data Última Colheita de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParOpeAreaDtFlorada1Ini != '' and pParOpeAreaDtFlorada1Fin != '' THEN
               vPar4 = vPar4||'Data 1º Florada de ['||pParOpeAreaDtFlorada1Ini||'] até ['||pParOpeAreaDtFlorada1Fin||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Data 1º Florada de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParOpeAreaDtEmergIni != '' and pParOpeAreaDtEmergFin != '' THEN
               vPar4 = vPar4||'Data Emergência de ['||pParOpeAreaDtEmergIni||'] até ['||pParOpeAreaDtEmergFin||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Data Emergência de [] até []'||chr(13)||chr(10);
           end if;
       
       
       
       vSql = 'select
           '  || pVart01 ||'   as vart_01 '||
               ','''|| pVard01 ||''' as vard_01 ';
               
               if  pVart02 != ''  THEN
                vSql = vSql || ','  || pVart02 ||'   as vart_02 '||
                          ','''|| pVard02 ||''' as vard_02 ';
               else 
                  vSql = vSql || ',null as vart_02'||
                                      ',null as vard_02';
               end if;
               
           if  pVart03 != '' THEN
                vSql = vSql || ','  || pVart03 ||'   as vart_03 '||
                          ','''|| pVard03 ||''' as vard_03 ';
               else 
                  vSql = vSql || ',null as vart_03'||
                                      ',null as vard_03';
               end if;
               
           if  pVart04 != '' THEN
                vSql = vSql || ','  || pVart04 ||'   as vart_04 '||
                          ','''|| pVard04 ||''' as vard_04 ';
               else 
                  vSql = vSql || ',null as vart_04'||
                                      ',null as vard_04';
               end if;
               
           if  pVart05 != ''  THEN
                vSql = vSql || ','  || pVart05 ||'   as vart_05 '||
                          ','''|| pVard05 ||''' as vard_05 ';
               else 
                  vSql = vSql || ',null as vart_05'||
                                      ',null as vard_05';
               end if;
       
       
               vSql = vSql||' 
               ,count(1) as valor_01
               from vwope_ocor_mov_dest_area t1 where 1=1 ';
               
               if pParUnitId != '' then
                   vSql = vSql || 'and ' || ' t1.unit_id' || ' in(''' ||pParUnitId||''')';
               end if;
               
               if pParOcorMovNr != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_mov_numero' || ' like '||'''' ||pParOcorMovNr||'''';
               end if;
       
               if pParGerEmpresaNome != '' then
                   vSql = vSql || 'and ' || ' t1.ger_empresa_nome' || ' like ' ||'''' ||pParGerEmpresaNome||'''';
               end if;
       
               if pParGerEmpresaAtivo != '' then
                   vSql = vSql || 'and ' || ' t1.ger_empresa_ativo' || ' like '||'''' ||pParGerEmpresaAtivo||'''';
               end if;
       
               if pParGerEmpresaDocCnpj != '' then
                   vSql = vSql || 'and ' || ' t1.ger_empresa_doc_cnpj' || ' like ' ||'''' ||pParGerEmpresaDocCnpj||'''';
               end if;
               
               if pParGerEmpresaDocCpf != '' then
                   vSql = vSql || 'and ' || ' t1.ger_empresa_doc_cpf' || ' like ' ||'''' ||pParGerEmpresaDocCpf||'''';
               end if;
       
               if pParGerPessoaEnderecoLograd != '' then
                   vSql = vSql || 'and ' || ' t1.ger_pessoa_endereco' || ' like ' ||'''' ||pParGerPessoaEnderecoLograd||'''';
               end if;
               
               if pParGerPessoaEnderecoLogradNr != '' then
                   vSql = vSql || 'and ' || ' t1.ger_pessoa_endereco_nr' || ' like ' ||'''' ||pParGerPessoaEnderecoLogradNr||'''';
               end if;
       
               if pParGerCidadeNome != '' then
                   vSql = vSql || 'and ' || ' t1.ger_pessoa_endereco_nome_cidade' || ' like ' ||'''' ||pParGerCidadeNome||'''';
               end if;
               
               if pParUfNome != '' then
                   vSql = vSql || 'and ' || ' t1.ger_pessoa_endereco_uf' || ' like ' ||'''' ||pParUfNome||'''';
               end if;
       
               if pParOcorTipoNome != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_tipo_nome' || ' like ' ||'''' ||pParOcorTipoNome||'''';
               end if;
       
               if pParOcorTipoAtivo != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_tipo_ativo' || ' like ' ||'''' ||pParOcorTipoAtivo||'''';
               end if;
               
               if pParOcorTipoSigla != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_tipo_sigla' || ' like ' ||'''' ||pParOcorTipoSigla||'''';
               end if;		
       
               if pParOcorTipoTp != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_tipo_tp' || ' like ' ||'''' ||pParOcorTipoTp||'''';
               end if;
       
               if pParOcorTipoObrigCompart != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_tipo_obrig' || ' like '||'''' ||pParOcorTipoObrigCompart||'''';
               end if;
       
               if pParOcorMovDetQntOcor != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_mov_det_qnt_ocor::text' || ' like ' ||'''' ||pParOcorMovDetQntOcor||'''';
               end if;
       
               if pParOcorMovDetQntOcorCalc != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_mov_det_qnt_ocor_calc::text' || ' like ' ||'''' ||pParOcorMovDetQntOcorCalc||'''';
               end if;
               
               if pParOcorNome != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_nome' || ' like ' ||'''' ||pParOcorNome||'''';
               end if;		
       
               if pParOcorAtivo != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_ativo' || ' like ' ||'''' ||pParOcorAtivo||'''';
               end if;
       
               if pParOcorSigla != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_sigla' || ' like ' ||'''' ||pParOcorSigla||'''';
               end if;
       
               if pParOcorTipo != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_tipo' || ' like ' ||'''' ||pParOcorTipo||'''';
               end if;
       
               if pParOcorTipoLanc != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_tipo_lanc' || ' like ' ||'''' ||pParOcorTipoLanc||'''';
               end if;
       
               if pParOcorGrupoNome != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_grupo_nome' || ' like ' ||'''' ||pParOcorGrupoNome||'''';
               end if;
       
               if pParOcorGrupoAtivo != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_grupo_ativo' || ' like ' ||'''' ||pParOcorGrupoAtivo||'''';
               end if;	
       
               if pParOcorGrupoSigla != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_grupo_sigla' || ' like '||'''' ||pParOcorGrupoSigla||'''';
               end if;
               
               if pParGerUmedidaNome != '' then
                   vSql = vSql || 'and ' || ' t1.ger_umedida_nome' || ' like '||'''' ||pParGerUmedidaNome||'''';
               end if;
       
               if pParGerUmedidaAtivo != '' then
                   vSql = vSql || 'and ' || ' t1.ger_umedida_ativo' || ' like ' ||'''' ||pParGerUmedidaAtivo||'''';
               end if;
       
               if pParGerUmedidaSigla != '' then
                   vSql = vSql || 'and ' || ' t1.ger_umedida_sigla' || ' like '||'''' ||pParGerUmedidaSigla||'''';
               end if;
       
               if pParOcorStatusNome != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_status_nome' || ' like ' ||'''' ||pParOcorStatusNome||'''';
               end if;
       
               if pParOcorStatusAtivo != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_status_ativo' || ' like ' ||'''' ||pParOcorStatusAtivo||'''';
               end if;
               
               if pParOcorStatusSigla != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_status_sigla' || ' like ' ||'''' ||pParOcorStatusSigla||'''';
               end if;
       
               if pParOcorStatusTipo != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_status_tipo_status' || ' like '||'''' ||pParOcorStatusTipo||'''';
               end if;
       
               if pParOpeAreaQntAreaProd != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_area_qnt_area_prod::text' || ' like '||'''' ||pParOpeAreaQntAreaProd||'''';
               end if;
       
               if pParOpeAreaQntAreaImprod != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_area_qnt_area_improd::text' || ' like '||'''' ||pParOpeAreaQntAreaImprod||'''';
               end if;
               
               if pParOpeAreaQntPlantEstand != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_area_qnt_plantas_estande::text' || ' like '||'''' ||pParOpeAreaQntPlantEstand||'''';
               end if;
       
               if pParOpeAreaBlocoCol != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_area_bloco_col' || ' like ' ||'''' ||pParOpeAreaBlocoCol||'''';
               end if;
       
               if pParOpeAreaUmedidaNome != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_area_umedida_nome' || ' like ' ||'''' ||pParOpeAreaUmedidaNome||'''';
               end if;
       
               if pParOpeAreaUmedidaSigla != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_area_umedida_sigla' || ' like '||'''' ||pParOpeAreaUmedidaSigla||'''';
               end if;
       
               if pParCentro2Nome != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_nome' || ' like '||'''' ||pParCentro2Nome||'''';
               end if;
       
               if pParCentro2Sigla != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_sigla' || ' like '||'''' ||pParCentro2Sigla||'''';
               end if;
       
               if pParCentro2Ativo != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_ativo' || ' like '||'''' ||pParCentro2Ativo||'''';
               end if;
       
               if pParCentro2TipoDestinacao != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_tipo_destinacao' || ' like '||'''' ||pParCentro2TipoDestinacao||'''';
               end if;
       
               if pParCentro2TipoProp != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_tipo_prop' || ' like '||'''' ||pParCentro2TipoProp||'''';
               end if;
       
               if pParCentro1Nome != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro1_nome' || ' like '||'''' ||pParCentro1Nome||'''';
               end if;
       
               if pParCentro1Ativo != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro1_ativo' || ' like '||'''' ||pParCentro1Ativo||'''';
               end if;
               
               if pParCentro1Sigla != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro1_sigla' || ' like '||'''' ||pParCentro1Sigla||'''';
               end if;
       
               if pParLogUserIns != '' then 
                   vSql = vSql ||' and '||'t1.log_user_ins'||' in(''' ||pParLogUserIns||''')';
               end if; 
                
               if pParLogUserUpd != '' then 
                   vSql = vSql ||' and '||'t1.log_user_upd'||' in(''' ||pParLogUserUpd||''')';
               end if;
            
            
               --data
               if pParLogDateInsIni != '' and pParLogDateInsFin != '' then 
                   vSql = vSql ||' and '||' CAST(t1.log_date_ins AS DATE)'||' >= '''||pParLogDateInsIni||''''||'and CAST(t1.log_date_ins AS DATE)'||' <= '''||pParLogDateInsFin||'''';
               end if;		 
               
               if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then 
                   vSql = vSql ||' and '||'CAST(t1.log_date_upd AS DATE)'||' >= '''||pParLogDateUpdIni||''''||' and  CAST(t1.log_date_upd AS DATE)'||' <= '''||pParLogDateUpdFin||'''';
               end if;	
                
               if pParOcorMovDataMovIni != '' and pParOcorMovDataMovFin != '' then
                   vSql = vSql || ' and ' || 'CAST(t1.ope_ocor_mov_data_mov AS DATE)' || ' >= ''' || pParOcorMovDataMovIni|| '''' || ' and  CAST(t1.ope_ocor_mov_data_mov AS DATE)' || ' <= ''' || pParOcorMovDataMovFin || '''';
               end if;
               
               if pParOcorMovDetDtStatusIni != '' and pParOcorMovDetDtStatusFin != '' then
                   vSql = vSql || ' and ' || 'CAST(t1.ope_ocor_mov_det_data_status AS DATE)' || ' >= ''' || pParOcorMovDetDtStatusIni|| '''' || ' and  CAST(t1.ope_ocor_mov_det_data_status AS DATE)' || ' <= ''' || pParOcorMovDetDtStatusFin || '''';
               end if;
       
               if pParOpeAreaDtIniPlan != '' and pParOpeAreaDtIniPlanFin != '' then
                   vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_ini_plan AS DATE)' || ' >= ''' || pParOpeAreaDtIniPlan|| '''' || ' and  CAST(t1.ope_centro2_area_data_ini_plan AS DATE)' || ' <= ''' || pParOpeAreaDtIniPlanFin || '''';
               end if;
       
               if pParOpeAreaDtFinPlanIni != '' and pParOpeAreaDtFinPlan != '' then
                   vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_fin_plan AS DATE)' || ' >= ''' || pParOpeAreaDtFinPlanIni|| '''' || ' and  CAST(t1.ope_centro2_area_data_fin_plan AS DATE)' || ' <= ''' || pParOpeAreaDtFinPlan || '''';
               end if;
               
               if pParOpeAreaDtUltPlanIni != '' and pParOpeAreaDtUltPlanFin != '' then
                   vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_ult_plan AS DATE)' || ' >= ''' || pParOpeAreaDtUltPlanIni|| '''' || ' and  CAST(t1.ope_centro2_area_data_ult_plan AS DATE)' || ' <= ''' || pParOpeAreaDtUltPlanFin || '''';
               end if;
       
               if pParOpeAreaDtIniCol != '' and pParOpeAreaDtIniColFin != '' then
                   vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_ini_col AS DATE)' || ' >= ''' || pParOpeAreaDtIniCol|| '''' || ' and  CAST(t1.ope_centro2_area_data_ini_col AS DATE)' || ' <= ''' || pParOpeAreaDtIniColFin || '''';
               end if;
       
               if pParOpeAreaDtFinColIni != '' and pParOpeAreaDtFinCol != '' then
                   vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_fin_col AS DATE)' || ' >= ''' || pParOpeAreaDtFinColIni|| '''' || ' and  CAST(t1.ope_centro2_area_data_fin_col AS DATE)' || ' <= ''' || pParOpeAreaDtFinCol || '''';
               end if;
       
               if pParOpeAreaDtUltColIni != '' and pParOpeAreaDtUltColFin != '' then
                   vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_ult_col AS DATE)' || ' >= ''' || pParOpeAreaDtUltColIni|| '''' || ' and  CAST(t1.ope_centro2_area_data_ult_col AS DATE)' || ' <= ''' || pParOpeAreaDtUltColFin || '''';
               end if;
               
               if pParOpeAreaDtFlorada1Ini != '' and pParOpeAreaDtFlorada1Fin != '' then
                   vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_florada_1 AS DATE)' || ' >= ''' || pParOpeAreaDtFlorada1Ini|| '''' || ' and  CAST(t1.ope_centro2_area_data_florada_1 AS DATE)' || ' <= ''' || pParOpeAreaDtFlorada1Fin || '''';
               end if;
       
               if pParOpeAreaDtEmergIni != '' and pParOpeAreaDtEmergFin != '' then
                   vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_emerg AS DATE)' || ' >= ''' || pParOpeAreaDtEmergIni|| '''' || ' and  CAST(t1.ope_centro2_area_data_emerg AS DATE)' || ' <= ''' ||pParOpeAreaDtEmergFin|| '''';
               end if;
       
       
                    -- Group By
            -- ===================================
               vSql = vSql||' group by '|| pVart01;
       
               if  pVart02 != ''  THEN
                vSql = vSql||  ','|| pVart02;
               end if;
               
           if  pVart03 != ''  THEN
                vSql = vSql||  ','|| pVart03;
               end if;
               
           if  pVart04 != ''  THEN
                vSql = vSql||  ','|| pVart04;
               end if;
               
           if  pVart05 != ''  THEN
                vSql = vSql||  ','|| pVart05;
               end if;
               
            -- Order By
            -- ===================================
               vSql = vSql||' order by '|| pVart01;
       
               if  pVart02 != ''  THEN
                vSql = vSql||  ','|| pVart02;
               end if;
               
           if  pVart03 != ''  THEN
                vSql = vSql||  ','|| pVart03;
               end if;
               
           if  pVart04 != ''  THEN
                vSql = vSql||  ','|| pVart04;
               end if;
               
           if  pVart05 != ''  THEN
                vSql = vSql||  ','|| pVart05;
               end if;
               
           
           FOR r IN EXECUTE vSql loop
               ind_rel_id := pParIndRelId;
               ind_rel_par1 := vPar1;
               ind_rel_par2 := vPar2;
               ind_rel_par3 := vPar3;
               ind_rel_par4 := vPar4;
               vart_01 := r.vart_01;
               vard_01 := r.vard_01;
               vart_02 := r.vart_02;
               vard_02 := r.vard_02;
               vart_03 := r.vart_03;
               vard_03 := r.vard_03;
               vart_04 := r.vart_04;
               vard_04 := r.vard_04;
               vart_05 := r.vart_05;
               vard_05 := r.vard_05;
               valor_01 := r.valor_01;
           
           RETURN NEXT;
           
           END loop;
       
       end;
       $BODY$
       LANGUAGE plpgsql VOLATILE;;
       
       
       -----------
       
       

       Drop FUNCTION IF EXISTS fnreport0026;;

       CREATE OR REPLACE FUNCTION fnreport0026(
       pParUnitId varchar, 
       pParIndRelId varchar, 
       pVart01 varchar, 
       pVard01 varchar, 
       pVart02 varchar default null,
       pVard02 varchar default null,
       pVart03 varchar default null,
       pVard03 varchar default null,
       pVart04 varchar default null,
       pVard04 varchar default null,
       pVart05 varchar default null,
       pVard05 varchar default null,
       pParCentro1Nome varchar default null,
       pParCentro1Sigla varchar default null,
       pParCentro1Ativo varchar default null,
       pParCentro2Nome varchar default null,
       pParCentro2Ativo varchar default null,
       pParCentro2Sigla varchar default null,
       pParCentro2EquipTipoRodad varchar default null,
       pParCentro2EquipTipoCarroc varchar default null,
       pParCentro2EquipCid varchar default null,
       pParCentro2EquipUf varchar default null,
       pParCentro2EquipPlaca varchar default null,
       pParCentro2EquipRenavam varchar default null,
       pParCentro2EquipTara varchar default null,
       pParCentro2EquipCapacidKg varchar default null,
       pParCentro2EquipCapacidM3 varchar default null,
       pParCentro2EquipPotenc varchar default null,
       pParCentro2EquipNrChassi varchar default null,
       pParCentro2EquipNrSerie varchar default null,
       pParCentro2EquipLiberadoAbastec varchar default null,
       pParCentro2EquipNrRegisEstadual varchar default null,
       pParCentro2EquipTipoTracao varchar default null,
       pParCentro2EquipTranspAutoCarg varchar default null,
       pParCompartNome varchar default null,
       pParCompartAtivo varchar default null,
       pParCompartSigla varchar default null,
       pParCompartCapacid varchar default null,
       pParCompartValidItemServ varchar default null,
       pParCompartDtAquisicaoIni varchar default null,
       pParCompartDtAquisicaoFin varchar default null,
       pParCompartVrAquisicao varchar default null,
       pParCompartNrSerie varchar default null,
       pParOcorMovDataMovIni varchar default null,
       pParOcorMovDataMovFin varchar default null,
       pParOcorMovNr varchar default null,
       pParGerEmpresaNome varchar default null,
       pParGerEmpresaAtivo varchar default null,
       pParGerEmpresaDocCnpj varchar default null,
       pParGerEmpresaDocCpf varchar default null,
       pParGerPessoaEnderecoLograd varchar default null,
       pParGerPessoaEnderecoLogradNr varchar default null,
       pParGerCidadeNome varchar default null,
       pParUfNome varchar default null,
       pParOcorTipoNome varchar default null,
       pParOcorTipoAtivo varchar default null,
       pParOcorTipoSigla varchar default null,
       pParOcorTipoObrigCompart varchar default null,
       pParOcorTipoTp varchar default null,
       pParOcorMovDetQntOcor varchar default null,
       pParOcorMovDetQntOcorCalc varchar default null,
       pParOcorMovDetDtStatusIni varchar default null,
       pParOcorMovDetDtStatusFin varchar default null,
       pParOcorNome varchar default null,
       pParOcorAtivo varchar default null,
       pParOcorSigla varchar default null,
       pParOcorTipo varchar default null,
       pParOcorTipoLanc varchar default null,
       pParOcorGrupoNome varchar default null,
       pParOcorGrupoAtivo varchar default null,
       pParOcorGrupoSigla varchar default null,
       pParGerUmedidaNome varchar default null,
       pParGerUmedidaAtivo varchar default null,
       pParGerUmedidaSigla varchar default null,
       pParOcorStatusNome varchar default null,
       pParOcorStatusAtivo varchar default null,
       pParOcorStatusSigla varchar default null,
       pParOcorStatusTipo varchar default null,
       pParLogUserIns varchar default null,
       pParLogDateInsIni varchar default null,
       pParLogDateInsFin varchar default null,
       pParLogUserUpd varchar default null,
       pParLogDateUpdIni varchar default null,
       pParLogDateUpdFin varchar default null
       )
       RETURNS TABLE(
        ind_rel_id varchar,
        ind_rel_par1 varchar,
        ind_rel_par2 varchar,
        ind_rel_par3 varchar,
        ind_rel_par4 varchar,
        vart_01 varchar,
        vard_01 varchar,
        vart_02 varchar,
        vard_02 varchar,
        vart_03 varchar,
        vard_03 varchar,
        vart_04 varchar,
        vard_04 varchar,
        vart_05 varchar,
        vard_05 varchar,
        valor_01 numeric,
        valor_02 numeric,
        valor_03 numeric,
        valor_04 numeric,
        valor_05 numeric,
        valor_06 numeric,
        valor_07 numeric,
        valor_08 numeric,
        valor_09 numeric,
        valor_10 numeric) AS $BODY$
       DECLARE
       vSql varchar;
       vPar1 varchar :='';
       vPar2 varchar :='';
       vPar3 varchar :='';
       vPar4 varchar :='';
       r record;
       begin
           
           if pParCentro1Nome != '' THEN
               vPar1 = vPar1||'Nome Centro 1 ['||pParCentro1Nome||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Nome Centro 1 [] '||chr(13)||chr(10);
           end if;
       
           if pParCentro1Ativo != '' THEN
               vPar1 = vPar1||'Centro 1 Ativo ['||pParCentro1Ativo||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Centro 1 Ativo [] '||chr(13)||chr(10);
           end if;
       
           if pParCentro1Sigla != '' THEN
               vPar1 = vPar1||'Sigla Centro 1 ['||pParCentro1Sigla||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Sigla Centro 1 [] '||chr(13)||chr(10);
           end if;
       
           if pParCentro2Nome != '' THEN
               vPar1 = vPar1||'Equipamento ['||pParCentro2Nome||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Equipamento [] '||chr(13)||chr(10);
           end if;
       
           if pParCentro2Ativo != '' THEN
               vPar1 = vPar1||'Equipamento Ativo ['||pParCentro2Ativo||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Equipamento Ativo [] '||chr(13)||chr(10);
           end if;
       
           if pParCentro2Sigla != '' THEN
               vPar1 = vPar1||'Sigla Equipamento ['||pParCentro2Sigla||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Sigla Equipamento [] '||chr(13)||chr(10);
           end if;
       
           if pParCentro2EquipTipoRodad != '' THEN
               vPar1 = vPar1||'Tipo Rodado Equipamento ['||pParCentro2EquipTipoRodad||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Tipo Rodado Equipamento [] '||chr(13)||chr(10);
           end if;
       
           if pParCentro2EquipTipoCarroc != '' THEN
               vPar1 = vPar1||'Tipo Carroceria Equipamento ['||pParCentro2EquipTipoCarroc||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Tipo Carroceria Equipamento [] '||chr(13)||chr(10);
           end if;
       
           if pParCentro2EquipCid != '' THEN
               vPar1 = vPar1||'Equipamento Cidade ['||pParCentro2EquipCid||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Equipamento Cidade [] '||chr(13)||chr(10);
           end if;
       
           if pParCentro2EquipUf != '' THEN
               vPar1 = vPar1||'Estado Equipamento ['||pParCentro2EquipUf||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Estado Equipamento [] '||chr(13)||chr(10);
           end if;
       
           if pParCentro2EquipPlaca != '' THEN
               vPar1 = vPar1||'Placa Equipamento ['||pParCentro2EquipPlaca||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Placa Equipamento [] '||chr(13)||chr(10);
           end if;
       
           if pParCentro2EquipRenavam != '' THEN
               vPar1 = vPar1||'Renavam Equipamento ['||pParCentro2EquipRenavam||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Renavam Equipamento [] '||chr(13)||chr(10);
           end if;
       
           if pParCentro2EquipTara != '' THEN
               vPar1 = vPar1||'Tara Equipamento ['||pParCentro2EquipTara||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Tara Equipamento [] '||chr(13)||chr(10);
           end if;
       
           if pParCentro2EquipCapacidM3 != '' THEN
               vPar1 = vPar1||'Capacidade M³ Equipamento ['||pParCentro2EquipCapacidM3||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Capacidade M³ Equipamento [] '||chr(13)||chr(10);
           end if;
       
           if pParCentro2EquipPotenc != '' THEN
               vPar1 = vPar1||'Potência Equipamento ['||pParCentro2EquipPotenc||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Potência Equipamento [] '||chr(13)||chr(10);
           end if;
           
           if pParCentro2EquipNrChassi != '' THEN
               vPar1 = vPar1||'Nº Chassi Equipamento ['||pParCentro2EquipNrChassi||']'||chr(13)||chr(10);
           else
               vPar1 = vPar1||'Nº Chassi Equipamento [] '||chr(13)||chr(10);
           end if;
       
           if pParCentro2EquipNrSerie != '' THEN
               vPar2 = vPar2||'Nº Serie Equipamento ['||pParCentro2EquipNrSerie||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Nº Serie Equipamento [] '||chr(13)||chr(10);
           end if;
       
           if pParCentro2EquipLiberadoAbastec != '' THEN
               vPar2 = vPar2||'Equipamento Liberado Abastecimento ['||pParCentro2EquipLiberadoAbastec||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Equipamento Liberado Abastecimento [] '||chr(13)||chr(10);
           end if;
       
           if pParCentro2EquipNrRegisEstadual != '' THEN
               vPar2 = vPar2||'Nº Registro Estadual Equipamento ['||pParCentro2EquipNrRegisEstadual||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Nº Registro Estadual Equipamento [] '||chr(13)||chr(10);
           end if;
       
           if pParCentro2EquipTipoTracao != '' THEN
               vPar2 = vPar2||'Tipo Tração Equipamento ['||pParCentro2EquipTipoTracao||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Tipo Tração Equipamento [] '||chr(13)||chr(10);
           end if;
       
           if pParCentro2EquipTranspAutoCarg != '' THEN
               vPar2 = vPar2||'Tipo Transp. Automo Carga  ['||pParCentro2EquipTranspAutoCarg||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Tipo Transp. Automo Carga  [] '||chr(13)||chr(10);
           end if;
       
           if pParCompartNome != '' THEN
               vPar2 = vPar2||'Nome Compartimento ['||pParCompartNome||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Nome Compartimento [] '||chr(13)||chr(10);
           end if;
       
           if pParCompartAtivo != '' THEN
               vPar2 = vPar2||'Compartimento Ativo ['||pParCompartAtivo||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Compartimento Ativo [] '||chr(13)||chr(10);
           end if;
       
           if pParCompartSigla != '' THEN
               vPar2 = vPar2||'Sigla Compartimento ['||pParCompartSigla||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Sigla Compartimento [] '||chr(13)||chr(10);
           end if;
           
           if pParCompartCapacid != '' THEN
               vPar2 = vPar2||'Capacidade Compartimento ['||pParCompartCapacid||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Capacidade Compartimento [] '||chr(13)||chr(10);
           end if;	
       
           if pParCompartValidItemServ != '' THEN
               vPar2 = vPar2||'Valida Item/Serviço ['||pParCompartValidItemServ||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Valida Item/Serviço [] '||chr(13)||chr(10);
           end if;
       
           if pParCompartVrAquisicao != '' THEN
               vPar2 = vPar2||'Valor Aquisição Compartimento ['||pParCompartVrAquisicao||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Valor Aquisição Compartimento [] '||chr(13)||chr(10);
           end if;
       
           if pParCompartNrSerie != '' THEN
               vPar2 = vPar2||'Nº Serie Compartimento ['||pParCompartNrSerie||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Nº Serie Compartimento [] '||chr(13)||chr(10);
           end if;
           
           if pParOcorMovNr != '' THEN
               vPar2 = vPar2||'Número do Movimento ['||pParOcorMovNr||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Número do Movimento [] '||chr(13)||chr(10);
           end if;
       
           if pParGerEmpresaNome != '' THEN
               vPar2 = vPar2||'Empresa ['||pParGerEmpresaNome||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Empresa []'||chr(13)||chr(10);
           end if;
       
           if pParGerEmpresaAtivo != '' THEN	
               vPar2 = vPar2||'Empresa Ativo ['||pParGerEmpresaAtivo||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'Empresa Ativo []'||chr(13)||chr(10);
           end if;
           
           if pParGerEmpresaDocCnpj != '' THEN	
               vPar2 = vPar2||'CNPJ Empresa ['||pParGerEmpresaDocCnpj||']'||chr(13)||chr(10);
           else
               vPar2 = vPar2||'CNPJ Empresa []'||chr(13)||chr(10);
           end if;
           
           if pParGerEmpresaDocCpf != '' THEN	
               vPar3 = vPar3||'CPF Empresa ['||pParGerEmpresaDocCpf||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'CPF Empresa []'||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaEnderecoLograd != '' THEN	
               vPar3 = vPar3||'Endereço ['||pParGerPessoaEnderecoLograd||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Endereço []'||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaEnderecoLogradNr != '' THEN	
               vPar3 = vPar3||'Nº Endereço ['||pParGerPessoaEnderecoLogradNr||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Nº Endereço []'||chr(13)||chr(10);
           end if;
           
           if pParGerCidadeNome != '' THEN	
               vPar3 = vPar3||'Cidade ['||pParGerCidadeNome||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Cidade []'||chr(13)||chr(10);
           end if;	
       
           if pParUfNome != '' THEN	
               vPar3 = vPar3||'Estado ['||pParUfNome||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Estado []'||chr(13)||chr(10);
           end if;		
           
           if pParOcorTipoNome != '' THEN	
               vPar3 = vPar3||'Nome Tipo Ocorrência ['||pParOcorTipoNome||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Nome Tipo Ocorrência []'||chr(13)||chr(10);
           end if;
       
           if pParOcorTipoAtivo != '' THEN	
               vPar3 = vPar3||'Tipo Ocorrência Ativo ['||pParOcorTipoAtivo||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Tipo Ocorrência Ativo []'||chr(13)||chr(10);
           end if;
           
           if pParOcorTipoSigla != '' THEN	
               vPar3 = vPar3||'Sigla Tipo Ocorrência ['||pParOcorTipoSigla||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Sigla Tipo Ocorrência []'||chr(13)||chr(10);
           end if;
           
           if pParOcorTipoObrigCompart != '' THEN	
               vPar3 = vPar3||'Tipo Ocorrência Obrigatorio ['||pParOcorTipoObrigCompart||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Tipo Ocorrência Obrigatorio []'||chr(13)||chr(10);
           end if;
       
           if pParOcorTipoTp != '' THEN	
               vPar3 = vPar3||'Tipo Ocorrência ['||pParOcorTipoTp||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Tipo Ocorrência []'||chr(13)||chr(10);
           end if;
           
           if pParOcorMovDetQntOcor != '' THEN	
               vPar3 = vPar3||'Quantidade da Ocorrência ['||pParOcorMovDetQntOcor||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Quantidade da Ocorrência []'||chr(13)||chr(10);
           end if;
       
           if pParOcorMovDetQntOcorCalc != '' THEN	
               vPar3 = vPar3||'Quantidade Cálculada da Ocorrência ['||pParOcorMovDetQntOcorCalc||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Quantidade Cálculada da Ocorrência []'||chr(13)||chr(10);
           end if;
           
           if pParOcorNome != '' THEN	
               vPar3 = vPar3||'Ocorrência ['||pParOcorNome||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Ocorrência []'||chr(13)||chr(10);
           end if;
       
           if pParOcorAtivo != '' THEN	
               vPar3 = vPar3||'Ocorrência Ativa ['||pParOcorAtivo||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Ocorrência Ativa []'||chr(13)||chr(10);
           end if;
           
           if pParOcorSigla != '' THEN	
               vPar3 = vPar3||'Sigla Ocorrência ['||pParOcorSigla||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Sigla Ocorrência []'||chr(13)||chr(10);
           end if;
       
           if pParOcorTipo != '' THEN	
               vPar3 = vPar3||'Tipo Ocorrência ['||pParOcorTipo||']'||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Tipo Ocorrência []'||chr(13)||chr(10);
           end if;
           
           if pParOcorTipoLanc != '' THEN	
               vPar4 = vPar4||'Tipo Lancamento Ocorrência ['||pParOcorTipoLanc||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Tipo Lancamento Ocorrência []'||chr(13)||chr(10);
           end if;
           
           if pParOcorGrupoNome != '' THEN	
               vPar4 = vPar4||'Grupo de Ocorrência ['||pParOcorGrupoNome||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Grupo de Ocorrência []'||chr(13)||chr(10);
           end if;
           
           if pParOcorGrupoAtivo != '' THEN	
               vPar4 = vPar4||'Grupo de Ocorrência Ativo ['||pParOcorGrupoAtivo||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Grupo de Ocorrência Ativo []'||chr(13)||chr(10);
           end if;
       
           if pParOcorGrupoSigla != '' THEN	
               vPar4 = vPar4||'Sigla Grupo de Ocorrência ['||pParOcorGrupoSigla||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Sigla Grupo de Ocorrência []'||chr(13)||chr(10);
           end if;
       
           if pParGerUmedidaNome != '' THEN	
               vPar4 = vPar4||'U. Medida Ocorrência ['||pParGerUmedidaNome||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'U. Medida Ocorrência []'||chr(13)||chr(10);
           end if;
       
           if pParGerUmedidaAtivo != '' THEN	
               vPar4 = vPar4||'U. Medida Ocorrência Ativo ['||pParGerUmedidaAtivo||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'U. Medida Ocorrência Ativo []'||chr(13)||chr(10);
           end if;
           
           if pParGerUmedidaSigla != '' THEN	
               vPar4 = vPar4||'Sigla U. Medida Ocorrência ['||pParGerUmedidaSigla||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Sigla U. Medida Ocorrência []'||chr(13)||chr(10);
           end if;	
       
           if pParOcorStatusNome != '' THEN	
               vPar4 = vPar4||'Status da Ocorrência ['||pParOcorStatusNome||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Status da Ocorrência []'||chr(13)||chr(10);
           end if;	
       
           if pParOcorStatusAtivo != '' THEN	
               vPar4 = vPar4||'Status da Ocorrência Ativo ['||pParOcorStatusAtivo||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Status da Ocorrência Ativo []'||chr(13)||chr(10);
           end if;	
       
           if pParOcorStatusSigla != '' THEN	
               vPar4 = vPar4||'Sigla Status da Ocorrência ['||pParOcorStatusSigla||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Sigla Status da Ocorrência []'||chr(13)||chr(10);
           end if;	
       
           if pParOcorStatusTipo != '' THEN	
               vPar4 = vPar4||'Tipo Status da Ocorrência ['||pParOcorStatusTipo||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Tipo Status da Ocorrência []'||chr(13)||chr(10);
           end if;	
           
           if pParLogUserIns != '' then
               vPar4 = vPar4||'Log Usuario Inserção ['||pParLogUserIns||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Log Usuario Inserção []'||chr(13)||chr(10);
           end if;
       
           if pParLogUserUpd != '' then
               vPar4 = vPar4||'Log Usuario Alteração ['||pParLogUserUpd||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Log Usuario Alteração []'||chr(13)||chr(10);
           end if;
       
       -- Datas
           if pParLogDateInsIni != '' and pParLogDateInsFin != '' then
               vPar4 = vPar4||'Data Inserção de ['||pParLogDateInsIni||'] até ['||pParLogDateInsFin||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Data Inserção de [] até []'||chr(13)||chr(10);
           end if;
       
           if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then
               vPar4 = vPar4||'Data Alteração de ['||pParLogDateUpdIni||'] até ['||pParLogDateUpdFin||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Data Alteração de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParCompartDtAquisicaoIni != '' and pParCompartDtAquisicaoFin != '' THEN
               vPar4 = vPar4||'Data de Aquisição Compartimento de ['||pParCompartDtAquisicaoIni||'] até ['||pParCompartDtAquisicaoFin||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Data de Aquisição Compartimento de [] até []'||chr(13)||chr(10);
           end if;
       
           if pParOcorMovDataMovIni != '' and pParOcorMovDataMovFin != '' THEN
               vPar4 = vPar4||'Data do Movimento de ['||pParOcorMovDataMovIni||'] até ['||pParOcorMovDataMovFin||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Data do Movimento de [] até []'||chr(13)||chr(10);
           end if;
       
           if pParOcorMovDetDtStatusIni != '' and pParOcorMovDetDtStatusFin != '' THEN
               vPar4 = vPar4||'Data Status Ocorrência de ['||pParOcorMovDetDtStatusIni||'] até ['||pParOcorMovDetDtStatusFin||']'||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Data Status Ocorrência de [] até []'||chr(13)||chr(10);
           end if;
           
           
                   vSql = 'select
           '  || pVart01 ||'   as vart_01 '||
               ','''|| pVard01 ||''' as vard_01 ';
               
               if  pVart02 != ''  THEN
                vSql = vSql || ','  || pVart02 ||'   as vart_02 '||
                          ','''|| pVard02 ||''' as vard_02 ';
               else 
                  vSql = vSql || ',null as vart_02'||
                                      ',null as vard_02';
               end if;
               
           if  pVart03 != '' THEN
                vSql = vSql || ','  || pVart03 ||'   as vart_03 '||
                          ','''|| pVard03 ||''' as vard_03 ';
               else 
                  vSql = vSql || ',null as vart_03'||
                                      ',null as vard_03';
               end if;
               
           if  pVart04 != '' THEN
                vSql = vSql || ','  || pVart04 ||'   as vart_04 '||
                          ','''|| pVard04 ||''' as vard_04 ';
               else 
                  vSql = vSql || ',null as vart_04'||
                                      ',null as vard_04';
               end if;
           if  pVart05 != ''  THEN
                vSql = vSql || ','  || pVart05 ||'   as vart_05 '||
                          ','''|| pVard05 ||''' as vard_05 ';
               else 
                  vSql = vSql || ',null as vart_05'||
                                      ',null as vard_05';
               end if;
               
               vSql = vSql||' 
               ,count(1) as valor_01
               from vwope_ocor_mov_dest_equip t1 where 1=1 ';
               
               if pParUnitId != '' then
                   vSql = vSql || 'and ' || ' t1.unit_id' || ' in(''' ||pParUnitId||''')';
               end if;
               
               if pParCentro1Nome != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro1_nome' || ' like '||'''' ||pParCentro1Nome||'''';
               end if;
           
               if pParCentro1Sigla != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro1_sigla' || ' like '||'''' ||pParCentro1Sigla||'''';
               end if;
       
               if pParCentro1Ativo != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro1_ativo' || ' like '||'''' ||pParCentro1Ativo||'''';
               end if;
       
               if pParCentro2Nome != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_nome' || ' like '||'''' ||pParCentro2Nome||'''';
               end if;
               
               if pParCentro2Ativo != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_ativo' || ' like '||'''' ||pParCentro2Ativo||'''';
               end if;
       
               if pParCentro2Sigla != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_sigla' || ' like '||'''' ||pParCentro2Sigla||'''';
               end if;
       
               if pParCentro2EquipTipoRodad != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_equip_tipo_rodado' || ' like '||'''' ||pParCentro2EquipTipoRodad||'''';
               end if;
       
               if pParCentro2EquipTipoCarroc != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_equip_tipo_carroceria' || ' like '||'''' ||pParCentro2EquipTipoCarroc||'''';
               end if;
       
               if pParCentro2EquipCid != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_equip_cidade_nome' || ' like '||'''' ||pParCentro2EquipCid||'''';
               end if;
       
               if pParCentro2EquipUf != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_uf_sigla' || ' like '||'''' ||pParCentro2EquipUf||'''';
               end if;
       
               if pParCentro2EquipPlaca != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_equip_placa' || ' like '||'''' ||pParCentro2EquipPlaca||'''';
               end if;
       
               if pParCentro2EquipRenavam != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_equip_renavam' || ' like '||'''' ||pParCentro2EquipRenavam||'''';
               end if;
       
               if pParCentro2EquipTara != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_equip_tara' || ' like '||'''' ||pParCentro2EquipTara||'''';
               end if;
       
               if pParCentro2EquipCapacidKg != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_equip_capacidade_kg::text' || ' like '||'''' ||pParCentro2EquipCapacidKg||'''';
               end if;
       
               if pParCentro2EquipCapacidM3 != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_equip_capacidade_m3::text' || ' like '||'''' ||pParCentro2EquipCapacidM3||'''';
               end if;
       
               if pParCentro2EquipPotenc != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_equip_potencia' || ' like '||'''' ||pParCentro2EquipPotenc||'''';
               end if;
       
               if pParCentro2EquipNrChassi != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_equip_nr_chassi' || ' like '||'''' ||pParCentro2EquipNrChassi||'''';
               end if;
       
               if pParCentro2EquipNrSerie != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_equip_nr_serie' || ' like '||'''' ||pParCentro2EquipNrSerie||'''';
               end if;
       
               if pParCentro2EquipLiberadoAbastec != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_equip_liberado_abastec' || ' like '||''''||pParCentro2EquipLiberadoAbastec||'''';
               end if;
       
               if pParCentro2EquipNrRegisEstadual != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_equip_nr_registro_estadual' || ' like '||'''' ||pParCentro2EquipNrRegisEstadual||'''';
               end if;
       
               if pParCentro2EquipTipoTracao != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_equip_tipo_tracao::text' || ' like '||'''' ||pParCentro2EquipTipoTracao||'''';
               end if;
       
               if pParCentro2EquipTranspAutoCarg != '' then
                   vSql = vSql || 'and ' || ' t1.ope_centro2_equip_tipo_transp_auto_carga::text' || ' like ' ||'''' ||pParCentro2EquipTranspAutoCarg||'''';
               end if;
       
               if pParCompartNome != '' then
                   vSql = vSql || 'and ' || ' t1.ope_compart_nome' || ' like '||'''' ||pParCompartNome||'''';
               end if;
       
               if pParCompartAtivo != '' then
                   vSql = vSql || 'and ' || ' t1.ope_compart_ativo' || ' like '||'''' ||pParCompartAtivo||'''';
               end if;
       
               if pParCompartSigla != '' then
                   vSql = vSql || 'and ' || ' t1.ope_compart_sigla' || ' like '||'''' ||pParCompartSigla||'''';
               end if;
       
               if pParCompartCapacid != '' then
                   vSql = vSql || 'and ' || ' t1.ope_compart_capacidade' || ' like ' ||'''' ||pParCompartCapacid||'''';
               end if;
       
               if pParCompartValidItemServ != '' then
                   vSql = vSql || 'and ' || ' t1.ope_compart_validade_itemserv' || ' like '||'''' ||pParCompartValidItemServ||'''';
               end if;
       
               if pParCompartValidItemServ != '' then
                   vSql = vSql || 'and ' || ' t1.ope_compart_validade_itemserv' || ' like '||'''' ||pParCompartValidItemServ||'''';
               end if;
       
               if pParCompartVrAquisicao != '' then
                   vSql = vSql || 'and ' || ' t1.ope_compart_vr_aquisicao' || ' like '||'''' ||pParCompartVrAquisicao||'''';
               end if;
       
               if pParCompartNrSerie != '' then
                   vSql = vSql || 'and ' || ' t1.ope_compart_nr_serie' || ' like '||'''' ||pParCompartNrSerie||'''';
               end if;
       
               if pParOcorMovNr != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_mov_numero' || ' like '||'''' ||pParOcorMovNr||'''';
               end if;
       
       ---
               if pParGerEmpresaNome != '' then
                   vSql = vSql || 'and ' || ' t1.ger_empresa_nome' || ' like '||'''' ||pParGerEmpresaNome||'''';
               end if;
       
               if pParGerEmpresaAtivo != '' then
                   vSql = vSql || 'and ' || ' t1.ger_empresa_ativo' || ' like ' ||'''' ||pParGerEmpresaAtivo||'''';
               end if;
       
               if pParGerEmpresaDocCnpj != '' then
                   vSql = vSql || 'and ' || ' t1.ger_empresa_doc_cnpj' || ' like '||'''' ||pParGerEmpresaDocCnpj||'''';
               end if;
               
               if pParGerEmpresaDocCpf != '' then
                   vSql = vSql || 'and ' || ' t1.ger_empresa_doc_cpf' || ' like '||'''' ||pParGerEmpresaDocCpf||'''';
               end if;
       
               if pParGerPessoaEnderecoLograd != '' then
                   vSql = vSql || 'and ' || ' t1.ger_pessoa_endereco' || ' like '||'''' ||pParGerPessoaEnderecoLograd||'''';
               end if;
               
               if pParGerPessoaEnderecoLogradNr != '' then
                   vSql = vSql || 'and ' || ' t1.ger_pessoa_endereco_nr' || ' like '||'''' ||pParGerPessoaEnderecoLogradNr||'''';
               end if;
       
               if pParGerCidadeNome != '' then
                   vSql = vSql || 'and ' || ' t1.ger_pessoa_endereco_nome_cidade' || ' like '||'''' ||pParGerCidadeNome||'''';
               end if;
               
               if pParUfNome != '' then
                   vSql = vSql || 'and ' || ' t1.ger_pessoa_endereco_uf' || ' like '||'''' ||pParUfNome||'''';
               end if;
       
               if pParOcorTipoNome != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_tipo_nome' || ' like '||'''' ||pParOcorTipoNome||'''';
               end if;
       
               if pParOcorTipoAtivo != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_tipo_ativo' || ' like '||'''' ||pParOcorTipoAtivo||'''';
               end if;
               
               if pParOcorTipoSigla != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_tipo_sigla' || ' like '||'''' ||pParOcorTipoSigla||'''';
               end if;		
       
               if pParOcorTipoTp != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_tipo_tp' || ' like '||'''' ||pParOcorTipoTp||'''';
               end if;
       
               if pParOcorTipoObrigCompart != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_tipo_obrig' || ' like '||'''' ||pParOcorTipoObrigCompart||'''';
               end if;
       
               if pParOcorMovDetQntOcor != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_mov_det_qnt_ocor::text' || ' like '||'''' ||pParOcorMovDetQntOcor||'''';
               end if;
       
               if pParOcorMovDetQntOcorCalc != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_mov_det_qnt_ocor_calc::text' || ' like '||'''' ||pParOcorMovDetQntOcorCalc||'''';
               end if;
               
               if pParOcorNome != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_nome' || ' like '||'''' ||pParOcorNome||'''';
               end if;		
       
               if pParOcorAtivo != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_ativo' || ' like '||'''' ||pParOcorAtivo||'''';
               end if;
       
               if pParOcorSigla != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_sigla' || ' like '||'''' ||pParOcorSigla||'''';
               end if;
       
               if pParOcorTipo != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_tipo' || ' like '||'''' ||pParOcorTipo||'''';
               end if;
       
               if pParOcorTipoLanc != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_tipo_lanc' || ' like '||'''' ||pParOcorTipoLanc||'''';
               end if;
       
               if pParOcorGrupoNome != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_grupo_nome' || ' like '||'''' ||pParOcorGrupoNome||'''';
               end if;
       
               if pParOcorGrupoAtivo != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_grupo_ativo' || ' like '||'''' ||pParOcorGrupoAtivo||'''';
               end if;	
       
               if pParOcorGrupoSigla != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_grupo_sigla' || ' like '||'''' ||pParOcorGrupoSigla||'''';
               end if;
               
               if pParGerUmedidaNome != '' then
                   vSql = vSql || 'and ' || ' t1.ger_umedida_nome' || ' like '||'''' ||pParGerUmedidaNome||'''';
               end if;
       
               if pParGerUmedidaAtivo != '' then
                   vSql = vSql || 'and ' || ' t1.ger_umedida_ativo' || ' like '||'''' ||pParGerUmedidaAtivo||'''';
               end if;
       
               if pParGerUmedidaSigla != '' then
                   vSql = vSql || 'and ' || ' t1.ger_umedida_sigla' || ' like '||'''' ||pParGerUmedidaSigla||'''';
               end if;
       
               if pParOcorStatusNome != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_status_nome' || ' like '||'''' ||pParOcorStatusNome||'''';
               end if;
       
               if pParOcorStatusAtivo != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_status_ativo' || ' like '||'''' ||pParOcorStatusAtivo||'''';
               end if;
               
               if pParOcorStatusSigla != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_status_sigla' || ' like '||'''' ||pParOcorStatusSigla||'''';
               end if;
       
               if pParOcorStatusTipo != '' then
                   vSql = vSql || 'and ' || ' t1.ope_ocor_status_tipo_status' || ' like '||'''' ||pParOcorStatusTipo||'''';
               end if;
       
               if pParLogUserIns != '' then 
                   vSql = vSql ||' and '||'t1.log_user_ins'||' in(''' ||pParLogUserIns||''')';
               end if; 
                
               if pParLogUserUpd != '' then 
                   vSql = vSql ||' and '||'t1.log_user_upd'||' in(''' ||pParLogUserUpd||''')';
               end if;
               
       
               --data
               if pParLogDateInsIni != '' and pParLogDateInsFin != '' then 
                   vSql = vSql ||' and '||' CAST(t1.log_date_ins AS DATE)'||' >= '''||pParLogDateInsIni||''''||'and CAST(t1.log_date_ins AS DATE)'||' <= '''||pParLogDateInsFin||'''';
               end if;		 
               
               if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then 
                   vSql = vSql ||' and '||'CAST(t1.log_date_upd AS DATE)'||' >= '''||pParLogDateUpdIni||''''||' and  CAST(t1.log_date_upd AS DATE)'||' <= '''||pParLogDateUpdFin||'''';
               end if;	
                
               if pParCompartDtAquisicaoIni != '' and pParCompartDtAquisicaoFin != '' then
                   vSql = vSql || ' and ' || 'CAST(t1.ope_compart_data_aquisicao AS DATE)' || ' >= ''' || pParCompartDtAquisicaoIni|| '''' || ' and  CAST(t1.ope_compart_data_aquisicao AS DATE)' || ' <= ''' || pParCompartDtAquisicaoFin || '''';
               end if;
               
               if pParOcorMovDataMovIni != '' and pParOcorMovDataMovFin != '' then
                   vSql = vSql || ' and ' || 'CAST(t1.ope_ocor_mov_data_mov AS DATE)' || ' >= ''' || pParOcorMovDataMovIni|| '''' || ' and  CAST(t1.ope_ocor_mov_data_mov AS DATE)' || ' <= ''' || pParOcorMovDataMovFin || '''';
               end if;
       
               if pParOcorMovDetDtStatusIni != '' and pParOcorMovDetDtStatusFin != '' then
                   vSql = vSql || ' and ' || 'CAST(t1.ope_ocor_mov_det_data_status AS DATE)' || ' >= ''' || pParOcorMovDetDtStatusIni|| '''' || ' and  CAST(t1.ope_ocor_mov_det_data_status AS DATE)' || ' <= ''' || pParOcorMovDetDtStatusFin || '''';
               end if;
       
       
                    -- Group By
            -- ===================================
               vSql = vSql||' group by '|| pVart01;
       
               if  pVart02 != ''  THEN
                vSql = vSql||  ','|| pVart02;
               end if;
               
           if  pVart03 != ''  THEN
                vSql = vSql||  ','|| pVart03;
               end if;
               
           if  pVart04 != ''  THEN
                vSql = vSql||  ','|| pVart04;
               end if;
               
           if  pVart05 != ''  THEN
                vSql = vSql||  ','|| pVart05;
               end if;
               
            -- Order By
            -- ===================================
               vSql = vSql||' order by '|| pVart01;
       
               if  pVart02 != ''  THEN
                vSql = vSql||  ','|| pVart02;
               end if;
               
           if  pVart03 != ''  THEN
                vSql = vSql||  ','|| pVart03;
               end if;
               
           if  pVart04 != ''  THEN
                vSql = vSql||  ','|| pVart04;
               end if;
               
           if  pVart05 != ''  THEN
                vSql = vSql||  ','|| pVart05;
               end if;
               
           
           FOR r IN EXECUTE vSql loop
               ind_rel_id := pParIndRelId;
               ind_rel_par1 := vPar1;
               ind_rel_par2 := vPar2;
               ind_rel_par3 := vPar3;
               ind_rel_par4 := vPar4;
               vart_01 := r.vart_01;
               vard_01 := r.vard_01;
               vart_02 := r.vart_02;
               vard_02 := r.vard_02;
               vart_03 := r.vart_03;
               vard_03 := r.vard_03;
               vart_04 := r.vart_04;
               vard_04 := r.vard_04;
               vart_05 := r.vart_05;
               vard_05 := r.vard_05;
               valor_01 := r.valor_01;
           
           RETURN NEXT;
           
           END loop;
       
       
       
       end;
       $BODY$
       LANGUAGE plpgsql VOLATILE;;
       
       
       -----------
       
       

       Drop FUNCTION IF EXISTS fnutil_ExtraiValorArrayJson;;

       CREATE OR REPLACE FUNCTION fnutil_ExtraiValorArrayJson(pJson varchar, pValorExtraido varchar)
         RETURNS varchar AS $BODY$
       declare 
           vMsg varchar := '';
           vAuxiliar varchar;
           vJson json;
           vRetornoJson varchar;	
       BEGIN
       
           vAuxiliar := pJson;
           
           SELECT REPLACE(vAuxiliar,'data:','') into vAuxiliar;
           raise notice 'Json 1: %', vAuxiliar;
           
           SELECT REPLACE(vAuxiliar,'(','') into vAuxiliar;
           raise notice 'Json 2: %', vAuxiliar;
           
           SELECT REPLACE(vAuxiliar,')','') into vAuxiliar;
           raise notice 'Json 3: %', vAuxiliar;
           
           SELECT REPLACE(vAuxiliar,'[','') into vAuxiliar;
           raise notice 'Json 4: %', vAuxiliar;
           
           SELECT REPLACE(vAuxiliar,']','') into vAuxiliar;
           raise notice 'Json 5: %', vAuxiliar;
           
           vJson := vAuxiliar;
           
           select json_extract_path_text(vJson, pValorExtraido) into vAuxiliar;
           raise notice '%', vAuxiliar;
        
           return vAuxiliar;	
           
       EXCEPTION WHEN others THEN
               SELECT json_build_object('status','error', 'data','', 'message', sqlerrm) into vRetornoJson;
           return vRetornoJson;
       END;
       
       $BODY$
         LANGUAGE plpgsql VOLATILE
         COST 100;;
       
       
       -----------
       
       

       Drop FUNCTION IF EXISTS fnutil_FormatDate;;

       CREATE OR REPLACE FUNCTION fnutil_FormatDate(pDate DATE, pFormato integer)
         RETURNS varchar AS $BODY$ DECLARE
           vDia varchar;
           vMes varchar;
           vAno varchar;
           vDataFormat VARCHAR;
       BEGIN
           
           SELECT EXTRACT(DAY FROM	((pDate) :: DATE)) INTO vDia;
           SELECT EXTRACT(MONTH FROM	((pDate) :: DATE)) INTO vMes;
           SELECT EXTRACT(YEAR FROM	((pDate) :: DATE)) INTO vAno;
           
           if CHAR_LENGTH(vDia) < 2 then
               vDia := '0'||vDia;
           end if;
           
           if CHAR_LENGTH(vMes) < 2 then
               vMes := '0'||vMes;
           end if;
           
           if pFormato = 1 then
               vDataFormat := vDia ||'/' || vMes || '/' || vAno;
           elsif pformato = 2 then
               vDataFormat := vMes || '/' || vAno;
           elsif pFormato = 3 then
               vDataFormat := vAno ||'/' || vMes || '/' || vDia;
           end if;
           
           RETURN vDataFormat;
       
       END; $BODY$
         LANGUAGE plpgsql VOLATILE
         COST 100;;
       
       
       -----------
       
       

       drop function if EXISTS fnutil_nvl_sdt;;

       create or replace FUNCTION fnutil_nvl_sdt(
       pParCampo varchar,
       pParTypeOperation varchar,
       pParEntrada varchar)
       returns TIMESTAMP as 
       $function$
       declare
       begin
       
           IF pParCampo = pParTypeOperation then		
                   return fnutil_sdt(pParEntrada);
           else
                   return pParCampo;
           end if;
       
       end;
       $function$
       LANGUAGE plpgsql VOLATILE;;
       
     
       
       
       -----------
       
       

       Drop FUNCTION IF EXISTS fnutil_primeiro_dia;;

       CREATE OR REPLACE FUNCTION "public"."fnutil_primeiro_dia"("pperiodo" date, "pformato" int4)
         RETURNS "pg_catalog"."varchar" AS $BODY$ DECLARE
           vPrimeiroDiaMes varchar;
           vMes varchar;
           vAno varchar;
       BEGIN
       
           SELECT EXTRACT(MONTH FROM	((pPeriodo) :: DATE)) INTO vMes;
           
           if LENGTH(vMes) < 2 then
               vMes := '0' || vMes;
           end if;
           
           SELECT EXTRACT(YEAR FROM	((pPeriodo) :: DATE)) INTO vAno;
           vPrimeiroDiaMes := '01';
           
           if pFormato = 1 then
               vPrimeiroDiaMes := vPrimeiroDiaMes ||'/' || vMes || '/' || vAno;
           elsif pFormato = 2 then
               vPrimeiroDiaMes := vAno ||'/' || vMes || '/' || vPrimeiroDiaMes;
           end if;
           
           RETURN vPrimeiroDiaMes;
       
       END; $BODY$
         LANGUAGE plpgsql VOLATILE
         COST 100;;
       
       
       -----------
       
       

       Drop FUNCTION IF EXISTS fnutil_ProximoMes;;

       CREATE OR REPLACE FUNCTION fnutil_ProximoMes(pData varchar, pFormato integer)
         RETURNS varchar AS $BODY$ DECLARE
           vPrimeiroDia varchar;
           vUltimoDia varchar;
           vAno integer;
           vMes integer;	
       BEGIN
           
           vPrimeiroDia := '01';
           SELECT EXTRACT(MONTH FROM	(pData) :: DATE) INTO vMes;
           SELECT EXTRACT(YEAR FROM	(pData) :: DATE) INTO vAno;
           
    /*1 - Próximo mês com ultimo dia*/
           if pFormato = 1 then
               vUltimoDia := fnutil_ultimo_dia(vMes, vAno, 2);		
               SELECT EXTRACT(MONTH FROM vUltimoDia :: date) into vMes;		
               vUltimoDia := fnutil_ultimo_dia(vMes + 1, vAno, 1);	
                   RETURN vUltimoDia;
    /*2 - Próximo mês com Primeiro dia*/
           elsif pFormato = 2 then
               vPrimeiroDia := fnutil_primeiro_dia(pData::date,2);
               SELECT EXTRACT(MONTH FROM vPrimeiroDia :: date) into vMes;
               vPrimeiroDia := concat(vAno,'/',vMes+1,'/01');
               vPrimeiroDia := fnutil_primeiro_dia(vPrimeiroDia :: date, 1);
                   RETURN vPrimeiroDia;
           end if;	
           
           RETURN '01/01/1900';
       
       END; $BODY$
         LANGUAGE plpgsql VOLATILE
         COST 100;;
       
       
       -----------
       
       

       Drop FUNCTION IF EXISTS fnutil_result_Json;;

       CREATE OR REPLACE FUNCTION fnutil_result_Json(pJson json)
         RETURNS table(status varchar, data varchar, message varchar) AS $BODY$
       BEGIN
         RETURN QUERY
               SELECT * from json_to_record($1) as x(status varchar, data varchar, message varchar);
       END;
       $BODY$
         LANGUAGE plpgsql VOLATILE
         COST 100;;
       
       
       -----------
       
       

       Drop FUNCTION IF EXISTS fnutil_sdt;;

       CREATE OR REPLACE FUNCTION public.fnutil_sdt(pTp varchar)
         RETURNs TIMESTAMP AS $BODY$
       DECLARE
           vResult TIMESTAMP;	
       BEGIN
        
        if pTp = 'I' then
          SELECT TO_TIMESTAMP('1900-01-01 12:00:00', 'YYYY-MM-DD HH24:MI:SS') into vResult;
            
        end if;
        
        if pTp = 'F' then
            SELECT TO_TIMESTAMP('2999-12-31 12:00:00', 'YYYY-MM-DD HH24:MI:SS') into vResult;
            
        end if;
        
       
       RETURN vResult;
               
       END;
       $BODY$
         LANGUAGE plpgsql volatile;;
         
       
       
       -----------
       
       

       drop function if exists fnutil_table_id;;
       

       CREATE OR REPLACE FUNCTION fnutil_table_id(pids varchar, pidnull varchar)
       RETURNS TABLE("id" varchar) AS $BODY$
       declare
       vSql varchar;
       vIdNull varchar;
       r record;
       begin
       
           if pids != ''  or pids != null then
               vSql = 'select unnest(string_to_array('''|| pids ||''', '','')) as idaux ';
           else
               vSql = 'select unnest(string_to_array('''|| pidnull ||''', '','')) as idaux ';
           end if;
           
         for r in execute vSql
            loop
               id = r.idaux;
               return next;
               raise notice 'teste :%', 1;
            
            end loop;	
       return;
       end;
       $BODY$
         LANGUAGE plpgsql VOLATILE
         COST 100
         ROWS 1000;;
       
       
       -----------
       
       

       Drop FUNCTION IF EXISTS fnutil_ultimo_dia;;

       CREATE OR REPLACE FUNCTION "public"."fnutil_ultimo_dia"("mes" int4, "ano" int4, "formato" int4)
         RETURNS "pg_catalog"."varchar" AS $BODY$ DECLARE
           UltimoDiaMes varchar;
           vMes integer;
       BEGIN
           
           if (Mes + 1) > 12 then
               vMes := 0;
           else 
               vMes := Mes;
           end if;
           
           SELECT EXTRACT(DAY FROM	(( Ano || '/' ||( vMes + 1 ) || '/01' ) :: DATE - 1 )) INTO UltimoDiaMes;
       
           if vMes = 0 then
             vMes := 12;			
           end if;
       
           if Formato = 1 then
               if CHAR_LENGTH(vMes::text) < 2 then			
                   UltimoDiaMes := UltimoDiaMes ||'/0' || vMes || '/' || Ano;	
               else
                   UltimoDiaMes := UltimoDiaMes ||'/' || vMes || '/' || Ano;	
               end if;		
               
           elsif Formato = 2 then
               
               if CHAR_LENGTH(vMes::text) < 2 then			
                   UltimoDiaMes := Ano ||'/0' || vMes || '/' || UltimoDiaMes;
               else
                   UltimoDiaMes := Ano ||'/' || vMes || '/' || UltimoDiaMes;
               end if;
               
           elsif Formato = 3 then
               return UltimoDiaMes;
           end if;
           
           RETURN UltimoDiaMes;
       
       END; $BODY$
         LANGUAGE plpgsql VOLATILE
         COST 100;;
       
       
       -----------
       
       
       
       DROP VIEW IF EXISTS vwbor_mov_atual;;

       CREATE OR replace VIEW public.vwbor_mov_atual
       AS SELECT a.ope_centro2_equip_id as id,
           b.unit_id,
           a.ope_centro2_equip_id,
           b.sigla_centro2 AS ope_centro2_equip_sigla,
           b.nome AS ope_centro2_equip_nome,
               b.sigla_centro2||' - '||b.nome AS ope_centro2_equip_sigla_desc,
           a.id_tipo,
           a.numero_serie,
           a.ibutton_rfid,
           a.dthr_track,
           a.gps_altitude,
           a.gps_altitude_status,
           a.gps_lat,
           a.gps_long,
           a.gps_angulo_norte,
           a.gps_posicao_status,
           a.gps_velocidade,
           a.gps_velocidade_media,
           a.equipamento_ignicao,
           a.equipamento_bateria,
           a.equipamento_odometro,
           a.equipamento_rpm,
           a.equipamento_veloc,
           a.equipamento_veloc_odom,
           a.equipamento_veloc_odom_media,
           a.ope_centro2_pessoa_id,
           c.sigla_centro2 AS ope_centro2_pessoa_sigla,
           c.nome AS ope_centro2_pessoa_nome,
           a.ger_empresa_id,
           f.nome AS ger_empresa_nome,
           a.ope_centro2_area_id,
           d.sigla_centro2 AS ope_centro2_area_sigla,
           d.nome AS ope_centro2_area_nome,
           d.sigla_centro2||' - '||d.nome AS ope_centro2_area_sigla_desc,		
           d.ope_centro1_id as ope_centro1_area_id,
           e.sigla_centro1 AS ope_centro1_area_sigla,
           e.nome AS ope_centro1_area_nome,
               e.sigla_centro1||' - '||e.nome AS ope_centro1_area_sigla_desc,
           a.geom,
           '01' as icone_equipamento		
          FROM bor_mov_atual              a
            LEFT JOIN ope_centro2         b ON b.id = a.ope_centro2_equip_id
            LEFT JOIN ope_centro2         c ON c.id = a.ope_centro2_pessoa_id
            LEFT JOIN ope_centro2         d ON d.id = a.ope_centro2_area_id
            LEFT JOIN ope_centro1         e ON e.id = d.ope_centro1_id
            LEFT JOIN ger_empresa         f ON f.id = a.ger_empresa_id
            LEFT JOIN ope_centro_subgrupo g on g.id = b.ope_centro_subgrupo_id;;
       
       
       -----------
       
       
       
       DROP VIEW IF EXISTS vwbor_bor_mov_line;;

       CREATE OR replace VIEW public.vwbor_bor_mov_line
       AS select a.id,
           a.id_tipo,
           a.numero_serie,
           a.ibutton_rfid,
           a.dthr_track,
           a.gps_altitude,
           a.gps_altitude_status,
           a.gps_lat,
           a.gps_long,
           a.gps_angulo_norte,
           a.gps_posicao_status,
           a.gps_velocidade,
           a.gps_velocidade_media,
           a.equipamento_ignicao,
           a.equipamento_bateria,
           a.equipamento_odometro,
           a.equipamento_rpm,
           a.equipamento_veloc,
           a.equipamento_veloc_odom,
           a.equipamento_veloc_odom_media,
           a.log_user_ins,
           a.log_date_ins,
           a.log_user_upd,
           a.log_date_upd,
           a.ope_centro2_equip_id_1,
           a.ope_centro2_equip_id_2,
           a.ope_centro2_pessoa_id,
           a.ger_empresa_id,
           a.ope_centro2_area_id,
           a.buzzer,
           a.unit_id,
               st_setsrid(st_makeline(st_geomfromtext(((('POINT('::text || a.gps_lat::text) || ' '::text) || a.gps_long::text) || ')'::text), lag(st_geomfromtext(((('POINT('::text || a.gps_lat::text) || ' '::text) || a.gps_long::text) || ')'::text)) OVER (ORDER BY a.numero_serie, a.dthr_track)), 4326) AS line
            FROM bor_mov a
           GROUP BY a.id,
           a.id_tipo,
           a.numero_serie,
           a.ibutton_rfid,
           a.dthr_track,
           a.gps_altitude,
           a.gps_altitude_status,
           a.gps_lat,
           a.gps_long,
           a.gps_angulo_norte,
           a.gps_posicao_status,
           a.gps_velocidade,
           a.gps_velocidade_media,
           a.equipamento_ignicao,
           a.equipamento_bateria,
           a.equipamento_odometro,
           a.equipamento_rpm,
           a.equipamento_veloc,
           a.equipamento_veloc_odom,
           a.equipamento_veloc_odom_media,
           a.log_user_ins,
           a.log_date_ins,
           a.log_user_upd,
           a.log_date_upd,
           a.ope_centro2_equip_id_1,
           a.ope_centro2_equip_id_2,
           a.ope_centro2_pessoa_id,
           a.ger_empresa_id,
           a.ope_centro2_area_id,
           a.buzzer,
           a.unit_id;;
       
       
       -----------
       
       
       
       DROP VIEW IF EXISTS vwind_rel;;

       CREATE OR replace VIEW vwind_rel
       AS
       select 
        t1.id as ind_rel_id,
        t1.nome as ind_rel_nome,
        t1.ativo as ind_rel_ativo,
        t1.nome_tecnico as ind_rel_nome_tecnico,
        t1.tipo as ind_rel_tipo,
        
        t3.id as ind_prm_id, 
        t3.nome as ind_prm_nome,
        t3.ativo as ind_prm_ativo,
        t3.nome_tecnico as ind_prm_nome_tecnico,
        t3.tipo_dado as ind_prm_tipo_dado,
        t3.tipo_entrada as ind_prm_tipo_entrada,
        t3.internal as ind_prm_internal,
        t3.busca_tabela as ind_prm_busca_tabela,
        t3.busca_campo_nome as ind_prm_busca_campo_nome,
        t3.busca_campo_id as ind_prm_busca_campo_id, 
        t3.busca_valores as ind_prm_busca_valores, 
        t3.obrigatorio as ind_prm_obrigatorio,
        t3.valor_padrao as ind_prm_valor_padrao, 
        t3.visivel as ind_prm_visivel, 
        t3.busca_tabela_classe as ind_prm_busca_tabela_classe,
        t3.busca_campo_nome_classe as ind_prm_busca_campo_nome_classe,
        t3.busca_campo_id_classe as ind_prm_busca_campo_id_classe,
        
        
        t4.id as ind_ftd_id,
        t4.nome as ind_ftd_nome,
        t4.ativo as ind_ftd_ativo,
        t4.nome_tecnico as ind_ftd_nome_tecnico,
        t4.config_ftd as ind_ftd_config_ftd,
        
        t5.id as ind_cjd_id,
        t5.nome as ind_cjd_nome,
        t5.ativo as ind_cjd_ativo,
        t5.nome_tecnico as ind_cjd_nome_tecnico,
        t2.ordem_exib
        
       from ind_rel t1
           inner join ind_rel_relac_prm t2
           on t1.id = t2.ind_rel_id
           inner join ind_prm t3
           on t3.id = t2.ind_prm_id
           left join ind_ftd t4
           on t1.ind_ftd_id = t4.id
           left join ind_cjd t5
           on t1.ind_cjd_id = t5.id
           order by t1.id asc;;
       
       
       -----------
       
       
       
       Drop VIEW IF EXISTS public.vwope_centro2_mapa_coord;;

       CREATE OR REPLACE VIEW public.vwope_centro2_mapa_coord
       AS SELECT a.id,
           a.unit_id,
           b.ope_centro1_id ,
           a.ope_centro2_id_area,
           a.lat_x,
           a.long_y,
           a.ordem,
           a.log_user_ins,
           a.log_date_ins,
           a.log_user_upd,
           a.log_date_upd,
           CASE
               WHEN b.sigla_centro2::text = 'T4'::text THEN '#ffff4d'::text
               ELSE '#A9D0F5'::text
           END AS color
          FROM public.ope_centro2_mapa_coord a
          JOIN public.ope_centro2 b on (b.id = a.ope_centro2_id_area);;
       
       
       -----------
       
       
       
       Drop VIEW IF EXISTS public.vwope_centro2_mapa_geometria;;

       CREATE OR REPLACE VIEW public.vwope_centro2_mapa_geometria
       AS SELECT a.unit_id,
           a.ope_centro2_id_area,
           b.ope_centro1_id AS ope_centro1_id_area,
           b.nome as centro2_nome,
           b.sigla_centro2,
           a.geom,
           a.log_user_ins,
           a.log_date_ins,
           a.log_user_upd,
           a.log_date_upd,
           a.id,
           CASE
               WHEN b.sigla_centro2::text = 'T4'::text THEN '#ffff4d'::text
               ELSE '#A9D0F5'::text
           END AS color
          FROM ope_centro2_mapa_geometria a
            JOIN ope_centro2 b ON b.id::text = a.ope_centro2_id_area::text;;
       
       
       -----------
       
       
       
       Drop View If Exists vwope_ocor_mov_dest_area;;
       Drop View If Exists vwope_ocor_mov_dest_equip;;
       Drop View If Exists vwope_ocor_mov_dest;;
       

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
       on t5.ope_ocor_status_id = t9.id;;
       
       
       
       
       -----------
       
       
       
       DROP VIEW
       IF
           EXISTS vwope_ocor_mov_dest_area;
       CREATE 
           OR REPLACE VIEW vwope_ocor_mov_dest_area AS SELECT
           t1.unit_id,
           t1.ID AS ope_ocor_mov_dest_id,
           t1.observacao AS ope_ocor_mov_dest_obs,
           t1.ope_centro2_id AS ope_ocor_mov_dest_centro2_id,
       ---------------------------------------------------
           t2.ope_ocor_mov_id,
           t2.ope_ocor_mov_obs,
           t2.ope_ocor_mov_data_mov,
           t2.ope_ocor_mov_numero,
           t2.ope_ocor_mov_ger_empresa_id,
           t2.ope_ocor_mov_pes_endereco_id_exec,
           t2.ope_ocor_mov_ocor_tipo_id,
           t2.ger_empresa_id,
           t2.ger_empresa_nome,
           t2.ger_empresa_razao_social,
           t2.ger_empresa_ativo,
           t2.ger_empresa_ativo_desc,
           t2.ger_empresa_sigla,
           t2.ger_empresa_doc_cnpj,
           t2.ger_empresa_doc_cpf,
           t2.ger_pessoa_endereco_id,
           t2.ger_pessoa_endereco,
           t2.ger_pessoa_endereco_nr,
           t2.ger_pessoa_endereco_cep,
           t2.ger_pessoa_endereco_id_cidade,
           t2.ger_pessoa_endereco_nome_cidade,
           t2.ger_pessoa_endereco_uf,
           t2.ger_pessoa_endereco_id_pes,
           t2.ger_pessoa_endereco_nome_pes,
           t2.ger_pessoa_endereco_doc_pes,
           t2.ope_ocor_tipo_id,
           t2.ope_ocor_tipo_nome,
           t2.ope_ocor_tipo_ativo,
           t2.ope_ocor_tipo_ativo_desc,
           t2.ope_ocor_tipo_sigla,
           t2.ope_ocor_tipo_tp,
           t2.ope_ocor_tipo_tp_desc,
           t2.ope_ocor_tipo_obrig,
           t2.ope_ocor_tipo_obrig_desc,
           t2.ope_ocor_mov_det_id,
           t2.ope_ocor_mov_det_obs,
           t2.ope_ocor_mov_det_qnt_ocor,
           t2.ope_ocor_mov_det_qnt_ocor_calc,
           t2.ope_ocor_mov_det_data_status,
           t2.ope_ocor_mov_det_qnt_ocor_long_y,
           t2.ope_ocor_mov_det_qnt_ocor_lat_x,
           t2.ope_ocor_mov_det_ocor_ponto,
           t2.ope_ocor_id,
           t2.ope_ocor_nome,
           t2.ope_ocor_ativo,
           t2.ope_ocor_ativo_desc,
           t2.ope_ocor_sigla,
           t2.ope_ocor_icon,
           t2.ope_ocor_tipo,
           t2.ope_ocor_tipo_desc,
           t2.ope_ocor_tipo_lanc,
           t2.ope_ocor_tipo_lanc_desc,
           t2.ope_ocor_grupo_id,
           t2.ope_ocor_grupo_nome,
           t2.ope_ocor_grupo_ativo,
           t2.ope_ocor_grupo_ativo_desc,
           t2.ope_ocor_grupo_sigla,
           t2.ger_umedida_id,
           t2.ger_umedida_nome,
           t2.ger_umedida_ativo,
           t2.ger_umedida_ativo_desc,
           t2.ger_umedida_sigla,
           t2.ope_ocor_status_id,
           t2.ope_ocor_status_nome,
           t2.ope_ocor_status_ativo,
           t2.ope_ocor_status_sigla,
           t2.ope_ocor_status_tipo_status,
           t2.ope_ocor_status_tipo_status_desc,
           t2.ger_empresa_sigla_desc,
           t2.ope_ocor_tipo_sigla_desc,
           t2.ope_ocor_sigla_desc,
           t2.ope_ocor_grupo_sigla_desc,
           t2.ger_umedida_sigla_desc,
           t2.ope_ocor_status_sigla_desc,
       ------------------------------------------------------
           t3.ope_centro2_area_id,
           t3.ope_centro2_area_qnt_area_prod,
           t3.ope_centro2_area_qnt_area_improd,
           t3.ope_centro2_area_qnt_plantas_estande,
           t3.ope_centro2_area_bloco_col,
           ope_centro2_area_lat_x,
           ope_centro2_area_long_y,
           t3.ope_centro2_area_data_ini_plan,
           t3.ope_centro2_area_data_fin_plan,
           t3.ope_centro2_area_data_ult_plan,
           t3.ope_centro2_area_data_ini_col,
           t3.ope_centro2_area_data_fin_col,
           t3.ope_centro2_area_data_ult_col,
           t3.ope_centro2_area_data_florada_1,
           t3.ope_centro2_area_data_emerg,
           t3.ope_centro2_area_umedida_id,
           t3.ope_centro2_area_umedida_nome,
           t3.ope_centro2_area_umedida_sigla,
           t3.ope_centro2_id,
           t3.ope_centro2_nome,
           t3.ope_centro2_sigla,
           t3.ope_centro2_sigla_desc,
           t3.ope_centro2_ativo,
           t3.ope_centro2_ativo_desc,
           t3.ope_centro2_tipo_destinacao,
           t3.ope_centro2_tipo_destinacao_desc,
           t3.ope_centro2_tipo_prop,
           t3.ope_centro2_tipo_prop_desc,
           t3.ope_centro1_id,
           t3.ope_centro1_nome,
           t3.ope_centro1_sigla,
           t3.ope_centro1_sigla_desc,
           t3.ope_centro1_observacao,
           t3.ope_centro1_ativo,
           t3.ope_centro1_ativo_desc,
           t3.ope_centro2_area_atividade_sistema_cult_id,
           t3.ope_centro2_area_atividade_sistema_cult_nome,
           t3.ope_centro2_area_atividade_sistema_cult_sigla,
       ------------------------------------------------------
           t1.log_user_ins,
           t1.log_date_ins,
           t1.log_user_upd,
           t1.log_date_upd 
       FROM
           ope_ocor_mov_dest t1
           
           INNER JOIN vwope_ocor_mov t2 
           ON t1.ope_ocor_mov_id = t2.ope_ocor_mov_id
           
           INNER JOIN vwope_centro2_area t3 
           ON t1.ope_centro2_id = t3.ope_centro2_id;;
       
       
       -----------
       
       
       
       DROP VIEW
       IF
           EXISTS vwope_ocor_mov_dest_area;;
       CREATE 
           OR REPLACE VIEW vwope_ocor_mov_dest_area AS SELECT
           t1.unit_id,
           t1.ID AS ope_ocor_mov_dest_id,
           t1.observacao AS ope_ocor_mov_dest_obs,
           t1.ope_centro2_id AS ope_ocor_mov_dest_centro2_id,
       ---------------------------------------------------
           t2.ope_ocor_mov_id,
           t2.ope_ocor_mov_obs,
           t2.ope_ocor_mov_data_mov,
           t2.ope_ocor_mov_numero,
           t2.ope_ocor_mov_ger_empresa_id,
           t2.ope_ocor_mov_pes_endereco_id_exec,
           t2.ope_ocor_mov_ocor_tipo_id,
           t2.ger_empresa_id,
           t2.ger_empresa_nome,
           t2.ger_empresa_razao_social,
           t2.ger_empresa_ativo,
           t2.ger_empresa_ativo_desc,
           t2.ger_empresa_sigla,
           t2.ger_empresa_doc_cnpj,
           t2.ger_empresa_doc_cpf,
           t2.ger_pessoa_endereco_id,
           t2.ger_pessoa_endereco,
           t2.ger_pessoa_endereco_nr,
           t2.ger_pessoa_endereco_cep,
           t2.ger_pessoa_endereco_id_cidade,
           t2.ger_pessoa_endereco_nome_cidade,
           t2.ger_pessoa_endereco_uf,
           t2.ger_pessoa_endereco_id_pes,
           t2.ger_pessoa_endereco_nome_pes,
           t2.ger_pessoa_endereco_doc_pes,
           t2.ope_ocor_tipo_id,
           t2.ope_ocor_tipo_nome,
           t2.ope_ocor_tipo_ativo,
           t2.ope_ocor_tipo_ativo_desc,
           t2.ope_ocor_tipo_sigla,
           t2.ope_ocor_tipo_tp,
           t2.ope_ocor_tipo_tp_desc,
           t2.ope_ocor_tipo_obrig,
           t2.ope_ocor_tipo_obrig_desc,
           t2.ope_ocor_mov_det_id,
           t2.ope_ocor_mov_det_obs,
           t2.ope_ocor_mov_det_qnt_ocor,
           t2.ope_ocor_mov_det_qnt_ocor_calc,
           t2.ope_ocor_mov_det_data_status,
           t2.ope_ocor_mov_det_qnt_ocor_long_y,
           t2.ope_ocor_mov_det_qnt_ocor_lat_x,
           t2.ope_ocor_mov_det_ocor_ponto,
           t2.ope_ocor_id,
           t2.ope_ocor_nome,
           t2.ope_ocor_ativo,
           t2.ope_ocor_ativo_desc,
           t2.ope_ocor_sigla,
           t2.ope_ocor_icon,
           t2.ope_ocor_tipo,
           t2.ope_ocor_tipo_desc,
           t2.ope_ocor_tipo_lanc,
           t2.ope_ocor_tipo_lanc_desc,
           t2.ope_ocor_grupo_id,
           t2.ope_ocor_grupo_nome,
           t2.ope_ocor_grupo_ativo,
           t2.ope_ocor_grupo_ativo_desc,
           t2.ope_ocor_grupo_sigla,
           t2.ger_umedida_id,
           t2.ger_umedida_nome,
           t2.ger_umedida_ativo,
           t2.ger_umedida_ativo_desc,
           t2.ger_umedida_sigla,
           t2.ope_ocor_status_id,
           t2.ope_ocor_status_nome,
           t2.ope_ocor_status_ativo,
           t2.ope_ocor_status_sigla,
           t2.ope_ocor_status_tipo_status,
           t2.ope_ocor_status_tipo_status_desc,
           t2.ger_empresa_sigla_desc,
           t2.ope_ocor_tipo_sigla_desc,
           t2.ope_ocor_sigla_desc,
           t2.ope_ocor_grupo_sigla_desc,
           t2.ger_umedida_sigla_desc,
           t2.ope_ocor_status_sigla_desc,
       ------------------------------------------------------
           t3.ope_centro2_area_id,
           t3.ope_centro2_area_qnt_area_prod,
           t3.ope_centro2_area_qnt_area_improd,
           t3.ope_centro2_area_qnt_plantas_estande,
           t3.ope_centro2_area_bloco_col,
           ope_centro2_area_lat_x,
           ope_centro2_area_long_y,
           t3.ope_centro2_area_data_ini_plan,
           t3.ope_centro2_area_data_fin_plan,
           t3.ope_centro2_area_data_ult_plan,
           t3.ope_centro2_area_data_ini_col,
           t3.ope_centro2_area_data_fin_col,
           t3.ope_centro2_area_data_ult_col,
           t3.ope_centro2_area_data_florada_1,
           t3.ope_centro2_area_data_emerg,
           t3.ope_centro2_area_umedida_id,
           t3.ope_centro2_area_umedida_nome,
           t3.ope_centro2_area_umedida_sigla,
           t3.ope_centro2_id,
           t3.ope_centro2_nome,
           t3.ope_centro2_sigla,
           t3.ope_centro2_sigla_desc,
           t3.ope_centro2_ativo,
           t3.ope_centro2_ativo_desc,
           t3.ope_centro2_tipo_destinacao,
           t3.ope_centro2_tipo_destinacao_desc,
           t3.ope_centro2_tipo_prop,
           t3.ope_centro2_tipo_prop_desc,
           t3.ope_centro1_id,
           t3.ope_centro1_nome,
           t3.ope_centro1_sigla,
           t3.ope_centro1_sigla_desc,
           t3.ope_centro1_observacao,
           t3.ope_centro1_ativo,
           t3.ope_centro1_ativo_desc,
           t3.ope_centro2_area_atividade_sistema_cult_id,
           t3.ope_centro2_area_atividade_sistema_cult_nome,
           t3.ope_centro2_area_atividade_sistema_cult_sigla,
       ------------------------------------------------------
           t1.log_user_ins,
           t1.log_date_ins,
           t1.log_user_upd,
           t1.log_date_upd 
       FROM
           ope_ocor_mov_dest t1
           
           INNER JOIN vwope_ocor_mov t2 
           ON t1.ope_ocor_mov_id = t2.ope_ocor_mov_id
           
           INNER JOIN vwope_centro2_area t3 
           ON t1.ope_centro2_id = t3.ope_centro2_id;;
       
       
       -----------
       
       
       
       Drop View If Exists vwope_ocor_mov_dest_area;;

       CREATE OR REPLACE VIEW vwope_ocor_mov_dest_area  AS
        SELECT t1.unit_id,
           t1.id AS ope_ocor_mov_dest_id,
           t1.observacao AS ope_ocor_mov_dest_obs,
           t1.ope_centro2_id AS ope_ocor_mov_dest_centro2_id,
           t2.ope_ocor_mov_id,
           t2.ope_ocor_mov_obs,
           t2.ope_ocor_mov_data_mov,
           t2.ope_ocor_mov_numero,
           t2.ope_ocor_mov_ger_empresa_id,
           t2.ope_ocor_mov_pes_endereco_id_exec,
           t2.ope_ocor_mov_ocor_tipo_id,
           t2.ger_empresa_id,
           t2.ger_empresa_nome,
           t2.ger_empresa_razao_social,
           t2.ger_empresa_ativo,
           t2.ger_empresa_ativo_desc,
           t2.ger_empresa_sigla,
           t2.ger_empresa_doc_cnpj,
           t2.ger_empresa_doc_cpf,
           t2.ger_pessoa_endereco_id,
           t2.ger_pessoa_endereco,
           t2.ger_pessoa_endereco_nr,
           t2.ger_pessoa_endereco_cep,
           t2.ger_pessoa_endereco_id_cidade,
           t2.ger_pessoa_endereco_nome_cidade,
           t2.ger_pessoa_endereco_uf,
           t2.ger_pessoa_endereco_id_pes,
           t2.ger_pessoa_endereco_nome_pes,
           t2.ger_pessoa_endereco_doc_pes,
           t2.ope_ocor_tipo_id,
           t2.ope_ocor_tipo_nome,
           t2.ope_ocor_tipo_ativo,
           t2.ope_ocor_tipo_ativo_desc,
           t2.ope_ocor_tipo_sigla,
           t2.ope_ocor_tipo_tp,
           t2.ope_ocor_tipo_tp_desc,
           t2.ope_ocor_tipo_obrig,
           t2.ope_ocor_tipo_obrig_desc,
           t2.ope_ocor_mov_det_id,
           t2.ope_ocor_mov_det_obs,
           t2.ope_ocor_mov_det_qnt_ocor,
           t2.ope_ocor_mov_det_qnt_ocor_calc,
           t2.ope_ocor_mov_det_data_status,
           t2.ope_ocor_mov_det_qnt_ocor_long_y,
           t2.ope_ocor_mov_det_qnt_ocor_lat_x,
           t2.ope_ocor_mov_det_ocor_ponto,
           t2.ope_ocor_id,
           t2.ope_ocor_nome,
           t2.ope_ocor_ativo,
           t2.ope_ocor_ativo_desc,
           t2.ope_ocor_sigla,
           t2.ope_ocor_icon,
           t2.ope_ocor_tipo,
           t2.ope_ocor_tipo_desc,
           t2.ope_ocor_tipo_lanc,
           t2.ope_ocor_tipo_lanc_desc,
           t2.ope_ocor_grupo_id,
           t2.ope_ocor_grupo_nome,
           t2.ope_ocor_grupo_ativo,
           t2.ope_ocor_grupo_ativo_desc,
           t2.ope_ocor_grupo_sigla,
           t2.ger_umedida_id,
           t2.ger_umedida_nome,
           t2.ger_umedida_ativo,
           t2.ger_umedida_ativo_desc,
           t2.ger_umedida_sigla,
           t2.ope_ocor_status_id,
           t2.ope_ocor_status_nome,
           t2.ope_ocor_status_ativo,
           t2.ope_ocor_status_sigla,
           t2.ope_ocor_status_tipo_status,
           t2.ope_ocor_status_tipo_status_desc,
           t2.ger_empresa_sigla_desc,
           t2.ope_ocor_tipo_sigla_desc,
           t2.ope_ocor_sigla_desc,
           t2.ope_ocor_grupo_sigla_desc,
           t2.ger_umedida_sigla_desc,
           t2.ope_ocor_status_sigla_desc,
           t3.ope_centro2_area_id,
           t3.ope_centro2_area_qnt_area_prod,
           t3.ope_centro2_area_qnt_area_improd,
           t3.ope_centro2_area_qnt_plantas_estande,
           t3.ope_centro2_area_bloco_col,
           t3.ope_centro2_area_lat_x,
           t3.ope_centro2_area_long_y,
           t3.ope_centro2_area_data_ini_plan,
           t3.ope_centro2_area_data_fin_plan,
           t3.ope_centro2_area_data_ult_plan,
           t3.ope_centro2_area_data_ini_col,
           t3.ope_centro2_area_data_fin_col,
           t3.ope_centro2_area_data_ult_col,
           t3.ope_centro2_area_data_florada_1,
           t3.ope_centro2_area_data_emerg,
           t3.ope_centro2_area_umedida_id,
           t3.ope_centro2_area_umedida_nome,
           t3.ope_centro2_area_umedida_sigla,
           t3.ope_centro2_id,
           t3.ope_centro2_nome,
           t3.ope_centro2_sigla,
           t3.ope_centro2_sigla_desc,
           t3.ope_centro2_ativo,
           t3.ope_centro2_ativo_desc,
           t3.ope_centro2_tipo_destinacao,
           t3.ope_centro2_tipo_destinacao_desc,
           t3.ope_centro2_tipo_prop,
           t3.ope_centro2_tipo_prop_desc,
           t3.ope_centro1_id,
           t3.ope_centro1_nome,
           t3.ope_centro1_sigla,
           t3.ope_centro1_sigla_desc,
           t3.ope_centro1_observacao,
           t3.ope_centro1_ativo,
           t3.ope_centro1_ativo_desc,
           t3.ope_centro2_area_atividade_sistema_cult_id,
           t3.ope_centro2_area_atividade_sistema_cult_nome,
           t3.ope_centro2_area_atividade_sistema_cult_sigla,
           t1.log_user_ins,
           t1.log_date_ins,
           t1.log_user_upd,
           t1.log_date_upd
          FROM ope_ocor_mov_dest t1
            INNER JOIN vwope_ocor_mov t2 
                ON t1.ope_ocor_mov_id = t2.ope_ocor_mov_id
            INNER JOIN vwope_centro2_area t3 
                ON t1.ope_centro2_id = t3.ope_centro2_id;;
       
       
       
       -----------
       
       
       
       DROP VIEW IF EXISTS vwope_ocor_mov_dest_equip;;

       CREATE OR REPLACE VIEW vwope_ocor_mov_dest_equip AS 
       SELECT
           t1.unit_id,
           t1.ID AS ope_ocor_mov_dest_id,
           t1.observacao AS ope_ocor_mov_dest_obs,
           t1.ope_centro2_id AS ope_ocor_mov_dest_centro2_id,
       ---------------------------------------------------
           t2.ope_ocor_mov_id,
           t2.ope_ocor_mov_obs,
           t2.ope_ocor_mov_data_mov,
           t2.ope_ocor_mov_numero,
           t2.ope_ocor_mov_ger_empresa_id,
           t2.ope_ocor_mov_pes_endereco_id_exec,
           t2.ope_ocor_mov_ocor_tipo_id,
           t2.ger_empresa_id,
           t2.ger_empresa_nome,
           t2.ger_empresa_razao_social,
           t2.ger_empresa_ativo,
           t2.ger_empresa_ativo_desc,
           t2.ger_empresa_sigla,
           t2.ger_empresa_doc_cnpj,
           t2.ger_empresa_doc_cpf,
           t2.ger_pessoa_endereco_id,
           t2.ger_pessoa_endereco,
           t2.ger_pessoa_endereco_nr,
           t2.ger_pessoa_endereco_cep,
           t2.ger_pessoa_endereco_id_cidade,
           t2.ger_pessoa_endereco_nome_cidade,
           t2.ger_pessoa_endereco_uf,
           t2.ger_pessoa_endereco_id_pes,
           t2.ger_pessoa_endereco_nome_pes,
           t2.ger_pessoa_endereco_doc_pes,
           t2.ope_ocor_tipo_id,
           t2.ope_ocor_tipo_nome,
           t2.ope_ocor_tipo_ativo,
           t2.ope_ocor_tipo_ativo_desc,
           t2.ope_ocor_tipo_sigla,
           t2.ope_ocor_tipo_tp,
           t2.ope_ocor_tipo_tp_desc,
           t2.ope_ocor_tipo_obrig,
           t2.ope_ocor_tipo_obrig_desc,
           t2.ope_ocor_mov_det_id,
           t2.ope_ocor_mov_det_obs,
           t2.ope_ocor_mov_det_qnt_ocor,
           t2.ope_ocor_mov_det_qnt_ocor_calc,
           t2.ope_ocor_mov_det_data_status,
           t2.ope_ocor_mov_det_qnt_ocor_long_y,
           t2.ope_ocor_mov_det_qnt_ocor_lat_x,
           t2.ope_ocor_mov_det_ocor_ponto,
           t2.ope_ocor_id,
           t2.ope_ocor_nome,
           t2.ope_ocor_ativo,
           t2.ope_ocor_ativo_desc,
           t2.ope_ocor_sigla,
           t2.ope_ocor_icon,
           t2.ope_ocor_tipo,
           t2.ope_ocor_tipo_desc,
           t2.ope_ocor_tipo_lanc,
           t2.ope_ocor_tipo_lanc_desc,
           t2.ope_ocor_grupo_id,
           t2.ope_ocor_grupo_nome,
           t2.ope_ocor_grupo_ativo,
           t2.ope_ocor_grupo_ativo_desc,
           t2.ope_ocor_grupo_sigla,
           t2.ger_umedida_id,
           t2.ger_umedida_nome,
           t2.ger_umedida_ativo,
           t2.ger_umedida_ativo_desc,
           t2.ger_umedida_sigla,
           t2.ope_ocor_status_id,
           t2.ope_ocor_status_nome,
           t2.ope_ocor_status_ativo,
           t2.ope_ocor_status_sigla,
           t2.ope_ocor_status_tipo_status,
           t2.ope_ocor_status_tipo_status_desc,
           t2.ger_empresa_sigla_desc,
           t2.ope_ocor_tipo_sigla_desc,
           t2.ope_ocor_sigla_desc,
           t2.ope_ocor_grupo_sigla_desc,
           t2.ger_umedida_sigla_desc,
           t2.ope_ocor_status_sigla_desc,
       ------------------------------------------------------
           t3.ID AS ope_compart_id,
           t3.nome AS ope_compart_nome,
           t3.ativo AS ope_compart_ativo,
           t3.sigla_compart AS ope_compart_sigla,
           t3.capacidade AS ope_compart_capacidade,
           t3.valida_itemserv AS ope_compart_validade_itemserv,
           t3.medicao_trab_centro AS ope_compart_medicao_trab_centro,
           t3.data_aquisicao AS ope_compart_data_aquisicao,
           t3.data_baixa AS ope_compart_data_baixa,
           data_status AS ope_compart_data_status,
           t3.observacao AS ope_compart_obs,
           t3.valor_aquisicao AS ope_compart_vr_aquisicao,
           t3.numero_serie AS ope_compart_nr_serie,
       --------------------------------------------------------
           t4.ope_centro1_id,
           t4.ope_centro1_sigla,
           t4.ope_centro1_nome,
           t4.ope_centro1_ativo,
           t4.ope_centro1_ativo_desc,
           t4.ope_centro2_id,
           t4.ope_centro2_nome,
           t4.ope_centro2_ativo,
           t4.ope_centro2_ativo_desc,
           t4.ope_centro2_sigla,
           t4.ope_centro2_equip_id,
           t4.ope_centro2_equip_tipo_rodado,
           t4.ope_centro2_equip_tipo_rodado_desc,
           t4.ope_centro2_equip_tipo_carroceria,
           t4.ope_centro2_equip_tipo_carroceria_desc,
           t4.ope_centro2_equip_cidade_id,
           t4.ope_centro2_equip_cidade_nome,
           t4.ope_centro2_equip_cidade_ativo,
           t4.ope_centro2_equip_cidade_ativo_desc,
           t4.ope_centro2_uf_id,
           t4.ope_centro2_uf_nome,
           t4.ope_centro2_uf_sigla,
           t4.ope_centro2_equip_placa,
           t4.ope_centro2_equip_renavam,
           t4.ope_centro2_equip_tara,
           t4.ope_centro2_equip_capacidade_kg,
           t4.ope_centro2_equip_capacidade_m3,
           t4.ope_centro2_equip_potencia,
           t4.ope_centro2_equip_nr_chassi,
           t4.ope_centro2_equip_nr_serie,
           t4.ope_centro2_equip_liberado_abastec,
           t4.ope_centro2_equip_liberado_abastec_desc,
           t4.ope_centro2_equip_largura,
           t4.ope_centro2_equip_altura,
           t4.ope_centro2_equip_nr_registro_estadual,
           t4.ope_centro2_equip_tipo_tracao,
           t4.ope_centro2_equip_tipo_tracao_desc,
           t4.ope_centro2_equip_tipo_transp_auto_carga,
           t4.ope_centro2_equip_tipo_transp_auto_carga_desc,
       --------------------------------------------------------
           t1.log_user_ins,
           t1.log_date_ins,
           t1.log_user_upd,
           t1.log_date_upd 
       FROM
           ope_ocor_mov_dest t1
           INNER JOIN vwope_ocor_mov t2 
           ON t1.ope_ocor_mov_id = t2.ope_ocor_mov_id
           LEFT JOIN ope_compart t3 
           ON t1.ope_compart_id = t3.id 
           INNER JOIN vwope_centro2_equip t4 
           ON t1.ope_centro2_id = t4.ope_centro2_id;;
           
       
       
       -----------
       
       
       
       Drop  VIEW IF EXISTS vwmov_mov_itemserv;;

       CREATE OR REPLACE VIEW vwmov_mov_itemserv AS
           select 
               -- Mov ItemServ 
               t1.unit_id as mov_itemserv_unit_id,
               t1.id as mov_itemserv_id,
               t1.mov_id as mov_itemserv_mov_id,
               t1.ger_itemserv_id as mov_itemserv_ger_itemserv_id,
               t1.qnt_orig as mov_itemserv_qnt_orig,
               t1.valor_unit_orig as mov_itemserv_valor_unit_orig,
               t1.ger_umedida_id_conv as mov_itemserv_ger_umedida_id_conv,
               t1.qnt_conv as mov_itemserv_qnt_conv,
               t1.valor_unit_conv as mov_itemserv_valor_unit_conv,
               t1.valor_bruto as mov_itemserv_valor_bruto,  
               t1.valor_desconto as mov_itemserv_valor_desconto,
               t1.valor_acrecimo as mov_itemserv_valor_acrecimo,
               t1.valor_outros as mov_itemserv_valor_outros,
               t1.valor_liquido as mov_itemserv_valor_liquido,
               t1.qnt_devolvida as mov_itemserv_qnt_devolvida,
               t1.valor_frete as mov_itemserv_valor_frete,
               t1.valor_seguro as mov_itemserv_valor_seguro,
               t1.observacao as mov_itemserv_observacao,
               t1.valor_tributo_retido as mov_itemserv_valor_tributo_retido,
               t1.fis_cfop_id as mov_itemserv_fis_cfop_id,
               t1.valor_tributo_total as mov_itemserv_valor_tributo_total,
               t1.qnt_altura as mov_itemserv_qnt_altura,
               t1.qnt_largura as mov_itemserv_qnt_largura,
               t1.qnt_comprimento as mov_itemserv_qnt_comprimento,
               t1.nome_itemserv as mov_itemserv_nome_itemserv,
               t1.ger_itemserv_var_id as mov_itemserv_ger_itemserv_var_id,
               t1.ger_itemserv_lote_id as mov_itemserv_ger_itemserv_lote_id,
               t1.fis_obra_art as mov_itemserv_fis_obra_art,
               t1.fis_obra_cei as mov_itemserv_fis_obra_cei,
               t1.fis_numero_proc_susp_nfs as mov_itemserv_fis_numero_proc_susp_nfs,
               t1.fis_doc_cnae_nfs as mov_itemserv_fis_doc_cnae_nfs,
               t1.valor_outros_tributo_ret as mov_itemserv_valor_outros_tributo_ret,
               t1.valor_desconto_cond as mov_itemserv_valor_desconto_cond,
               t1.valor_desconto_incond as mov_itemserv_valor_desconto_incond,
               t1.valor_deducao as mov_itemserv_valor_deducao,
               t1.qnt_min_pessoa_cot as mov_itemserv_qnt_min_pessoa_cot,
       
               -- Mov
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
               
               -- Ger Item/Serv
               t3.id as ger_item_serv_id,
               t3.nome as ger_item_serv_nome,
               t3.ativo as ger_item_serv_ativo,
               fnstd('SN','default',t3.ativo) as ger_item_serv_ativo_desc,
               t3.tipo as ger_item_serv_tipo,
               fnstd('ger_itemserv','tipo',t3.tipo) as ger_item_serv_tipo_desc,
               t3.sigla_itemserv as ger_item_serv_sigla,
               
               -- Ger Umedida
               t4.id as ger_umedida_id,
               t4.nome as ger_umedida_nome,
               t4.ativo as ger_umedida_ativo,
               fnstd('SN','default',t4.ativo) as ger_umedida_ativo_desc,
               t4.sigla_umedida as ger_umedida_sigla,
               t4.nr_umedida as ger_umedida_nr_umedida,
               
               -- Fis Cfop
               t5.id as fis_cfop_id,
               t5.nr_cfop as fis_cfop_nr_cfop,
               t5.nome as fis_cfop_nome,
               t5.ativo as fis_cfop_ativo,		
               fnstd('SN','default',t5.ativo) as fis_cfop_ativo_desc,
               t5.data_validade as fis_cfop_data_validade,
       
               --Lote Item/Serv
               t6.id as ger_itemserv_lote_id,
               t6.nome as ger_itemserv_lote_nome,
               t6.ativo as ger_itemserv_lote_ativo,
               fnstd('SN','default',t6.ativo) as ger_itemserv_lote_ativo_desc,
               t6.data_ini as ger_itemserv_lote_data_ini,
               t6.data_fin as ger_itemserv_lote_data_fin,
               t6.observacao as ger_itemserv_lote_obs,
               t6.data_validade as ger_itemserv_lote_data_validade,
               
               t7.id as ger_itemserv_subgrupo_id,
               t7.nome as ger_itemserv_subgrupo_nome,
               t7.ativo as ger_itemserv_subgrupo_ativo,
               fnstd('SN','default',t7.ativo) as ger_itemserv_subgrupo_ativo_desc,
       
               t8.id as ger_itemserv_grupo_id,
               t8.nome as ger_itemserv_grupo_nome,
               t8.ativo as ger_itemserv_grupo_ativo,
               fnstd('SN','default',t8.ativo) as ger_itemserv_grupo_ativo_desc,		
               
               t1.log_user_ins,
               t1.log_date_ins,
               t1.log_user_upd,
               t1.log_date_upd,
       
               -- Sigla Desc
               t3.sigla_itemserv||' - '||t3.nome as ger_item_serv_sigla_desc,
               t4.sigla_umedida||' - '||t4.nome as ger_umedida_sigla_desc
       
           from mov_itemserv t1
               inner join mov t2
               on t1.mov_id = t2.id
               inner join ger_itemserv t3
               on  t1.ger_itemserv_id = t3.id
               inner join ger_umedida t4
               on t1.ger_umedida_id_conv = t4.id
               left join fis_cfop t5
               on t1.fis_cfop_id = t5.id
               left join ger_itemserv_lote t6
               on t1.ger_itemserv_lote_id = t6.id
               inner join ger_itemserv_subgrupo t7
               on t3.ger_itemserv_subgrupo_id = t7.id
               inner join ger_itemserv_grupo t8
               on t7.ger_grupo_id =  t8.id;;
       
       
       
       -----------
       
       
       
       DROP VIEW IF EXISTS vwope_centro2_ord_rec;;
       

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
               on t1.ope_compart_id = t26.id;
       
