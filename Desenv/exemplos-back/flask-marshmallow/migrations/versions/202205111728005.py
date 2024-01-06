from alembic import op
import sqlalchemy as sa

revision = '202205111728005'
down_revision = '202205111728004'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
  Drop FUNCTION IF EXISTS fnbor_bormovprocess;
CREATE OR REPLACE FUNCTION public.fnbor_bormovprocess(pdataini timestamp with time zone, pdatafim timestamp with time zone)
RETURNS boolean
LANGUAGE plpgsql
AS $function$
declare 
row Record;
equipamento Record;
--
vOpeCentro2PessoaId varchar;
vOpeCentro2AreaId varchar;
vOpeCentro2EquipId1 varchar;
vOpeAtividadeId varchar;
vGerEmpresaId varchar;
vOpeCentro2EquipId2 varchar;
vDtTrackBovMovAnt timestamp;
vLineGeometry geometry;
vDeslocInMeters numeric;
vLargura numeric;
--
vNumeroSerieAnt varchar;
vIbuttonFfidAnt varchar;
vNumeroSerieAtual varchar;
vIbuttonRfidAtual varchar;
vEquipamentoIgnicaoAnt varchar;
vGpsLatAnt varchar;
vGpsLngAnt varchar;
--
vDuração numeric;
begin
-- pega todos os equipamentos, o primeiro e o último apontamento no período executado
-- isso vai facilitar o processo e principalmente ajudar na performance
for equipamento in SELECT a.numero_serie,
                  max(a.dthr_track) as max_apont,
                  min(a.dthr_track) as min_apont
              FROM public.bor_mov a 
            WHERE a.dthr_track between pdataini and pdatafim
            GROUP BY a.numero_serie
            ORDER BY a.numero_serie 
loop
  -- buscar o apontamento do equipamento imediatamente anterior ao primeiro apontamento do bloco
  select a.numero_serie, a.ibutton_rfid, a.equipamento_ignicao, a.gps_lat, a.gps_long, a.dthr_track
    into vNumeroSerieAnt, vIbuttonFfidAnt, vEquipamentoIgnicaoAnt, vGpsLatAnt, vGpsLngAnt, vDtTrackBovMovAnt
    from public.bor_mov a
    where a.numero_serie = equipamento.numero_serie
      and a.dthr_track < equipamento.min_apont
    order by a.dthr_track desc
    limit 1;
  raise notice '% -> vNumeroSerieAnt = %, vIbuttonFfidAnt = %, vEquipamentoIgnicaoAnt = %, vGpsLng = %, vGpsLat = %, vDtTrackBovMovAnt = %', equipamento.numero_serie, vNumeroSerieAnt, vIbuttonFfidAnt, vEquipamentoIgnicaoAnt, vGpsLngAnt, vGpsLatAnt, vDtTrackBovMovAnt;

  -- insere um polígono para cada centro2 na ope_centro2_mapa_geometria
  for row in SELECT a.id,
                    a.numero_serie,
                    a.ibutton_rfid,
                    a.dthr_track,
                    a.gps_lat,
                    a.gps_long,
                    a.equipamento_ignicao,
                    coalesce(lag(a.gps_long::text) OVER (ORDER BY a.numero_serie, a.dthr_track), vGpsLngAnt) as gps_long_ant,
                    coalesce(lag(a.gps_lat::text) OVER (ORDER BY a.numero_serie, a.dthr_track), vGpsLatAnt) as gps_lat_ant
                FROM public.bor_mov a 
              WHERE a.numero_serie = equipamento.numero_serie
                AND a.dthr_track BETWEEN equipamento.min_apont 
                                      AND equipamento.min_apont
              ORDER BY a.dthr_track 
  loop
    -- atualiza numero_serie e rfid 
    if row.equipamento_ignicao = 'ON' then
      vNumeroSerieAtual = vNumeroSerieAnt;
      vIbuttonRfidAtual = vIbuttonFfidAnt;
    else
      vNumeroSerieAnt = row.numero_serie;
      vIbuttonFfidAnt = row.ibutton_rfid;
      --
      vNumeroSerieAtual = row.numero_serie;
      vIbuttonRfidAtual = row.ibutton_rfid;
    end if;
    
    raise notice 'vNumeroSerieAtual = % e vIbuttonRfidAtual = %', vNumeroSerieAtual, vIbuttonRfidAtual;
  
    -- busca pessoa na bor_dispositivo
    select a.ope_centro2_pessoa_id
      into vOpeCentro2PessoaId
      from public.bor_dispositivo a
      where a.numero_serie = vIbuttonRfidAtual
        and a.tipo = '2'; -- IBUTTON
    raise notice 'vOpeCentro2PessoaId = %', vOpeCentro2PessoaId;
  
    -- busca equipamento na bor_dispositivo
    select a.ope_centro2_equip_id
        into vOpeCentro2EquipId1
        from public.bor_dispositivo a
      where a.numero_serie = vNumeroSerieAtual
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
  
    -- busca a geometria na public.ope_centro2_mapa_geometria pela lat/lng
    select a.ope_centro2_id_area
      into vOpeCentro2AreaId
      from public.ope_centro2_mapa_geometria a
      where ST_Contains(ST_SetSRID(a.geom,4326), ST_GeomFromText('POINT(' || row.gps_lat|| ' ' || row.gps_long  || ')', 4326));
    raise notice 'vOpeCentro2AreaId = %', vOpeCentro2AreaId;
  
    -- busca ope_atividade na bor_msg e ope_atividade
    select c.id
      into vOpeAtividadeId
      from public.bor_msg a
      join public.bor_mov_atual b on (b.numero_serie = a.numero_serie)
  join public.ope_atividade c on (a.grupo_msg||'-'||a.index_msg = c.index_bor)
      where a.numero_serie = vNumeroSerieAtual
        and a.dthr_trans_msg_rast between b.dthr_ignicao_last_off
                                  and row.dthr_track
      order by a.dthr_trans_msg_rast desc
    limit 1;
    raise notice 'vOpeAtividadeId = %', vOpeAtividadeId;
    
    -- busca implemento 1 e salva na ope_centro2_equip_id_2
    select a.ope_centro1_id_imp01
      into vOpeCentro2EquipId2
      from public.ope_centro2_ord_rec a
      where a.ope_centro2_id = vOpeCentro2EquipId1;
    raise notice 'vOpeCentro2EquipId2 = %', vOpeCentro2EquipId2;   
    
    -- gera linha entre o registro da bor_mov e o registro anterior
    raise notice 'Lng = % - Lat = %', row.gps_long, row.gps_lat;
    vLineGeometry = st_setsrid(st_makeline(st_geomfromtext('POINT(' || row.gps_lat || ' ' || row.gps_long || ')'), st_geomfromtext('POINT(' || row.gps_lat_ant  || ' ' || row.gps_long_ant|| ')')), 4326);
    raise notice 'Geometria = %', vLineGeometry;
    
    -- pega a largura do equipamento e calcula a área trabalhada
    select st_length(ST_Transform(vLineGeometry, 26915)), a.largura
      into vDeslocInMeters, vLargura
      from public.ope_centro2_equip a
      where a.id = vOpeCentro2EquipId1;
    raise notice 'vDeslocInMeters = %   -  vLargura = % -> área trabalhada = %', vDeslocInMeters, vLargura, (vLargura * vDeslocInMeters) * 0.0001;
  
    -- atualiza public.bor_mov
    update public.bor_mov
        set numero_serie           = vNumeroSerieAtual,
            ibutton_rfid           = vIbuttonRfidAtual, 
            ope_centro2_pessoa_id  = vOpeCentro2PessoaId,
            ope_centro2_equip_id_1 = vOpeCentro2EquipId1,
            ope_centro2_equip_id_2 = vOpeCentro2EquipId2,
            ope_centro2_area_id    = vOpeCentro2AreaId,
            ope_atividade_id       = vOpeAtividadeId,
            geom_line              = case when vLineGeometry is not null then vLineGeometry else geom_line end,
            qnt_ha_trab            = (vLargura * vDeslocInMeters) * 0.0001,
            status                 = 'OK',
            dthr_status            = now(),
            duracao                = extract (EPOCH from (row.dthr_track - vDtTrackBovMovAnt)) / 60
      where id = row.id;
    raise notice 'ID = %', row.id;
    raise notice '********************************************************************';
  
  vDtTrackBovMovAnt = row.dthr_track;
  
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
               """)
 

def downgrade():
    pass