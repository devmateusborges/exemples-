Drop FUNCTION IF EXISTS fnbor_bormovdatagenerationprocess;
CREATE OR REPLACE FUNCTION public.fnbor_bormovdatagenerationprocess(pUnitId varchar, pdataini timestamp with time zone, hours integer, qtddispositivos integer)
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
              where unit_id = pUnitId ) w
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
       trunc(random() * (1100-600) + 600),                   'VALID',                                             vLat,                                                           vLng,
	   trunc(random() * (359)),                               true,                                                trunc(random() * (45-20) + 20),                                 trunc(random() * (45-20) + 20), 
   	   case when round(random()) = 0 then '' else 'ON' end,   case when round(random()) = 0 then '' else 'ON' end, vHodometroInicial + trunc(random() * (7-2) + 2),                trunc(random() * (3700-1500) + 1500), 
   	   trunc(random() * (45-20) + 20),                        trunc(random() * (45-20) + 20),                      trunc(random() * (45-20) + 20),                                 'admin',
       now(),                                                 case when round(random()) = 0 then '' else 'ON' end, pUnitId ,                                                       'NP',
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
$function$
;
