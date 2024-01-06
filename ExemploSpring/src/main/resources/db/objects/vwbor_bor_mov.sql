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
a.ope_atividade_id, a.qnt_ha_trab, a.duracao, b.nome, c.nome, d.nome, e.sigla_centro2;

-- Permissions

ALTER TABLE public.vwbor_bor_mov OWNER TO rf;
GRANT ALL ON TABLE public.vwbor_bor_mov TO rf;
