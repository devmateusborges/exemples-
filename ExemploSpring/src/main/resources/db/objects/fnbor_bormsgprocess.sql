Drop FUNCTION IF EXISTS fnbor_bormsgprocess;
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
$function$
;
