DROP VIEW IF EXISTS vwbor_mov_atual;
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
    '01' as icone_equipamento,
    a.log_user_ins,
	a.log_date_ins,
	a.log_user_upd,
	a.log_date_upd
   FROM bor_mov_atual              a
     LEFT JOIN ope_centro2         b ON b.id = a.ope_centro2_equip_id
     LEFT JOIN ope_centro2         c ON c.id = a.ope_centro2_pessoa_id
     LEFT JOIN ope_centro2         d ON d.id = a.ope_centro2_area_id
     LEFT JOIN ope_centro1         e ON e.id = d.ope_centro1_id
     LEFT JOIN ger_empresa         f ON f.id = a.ger_empresa_id
	 LEFT JOIN ope_centro_subgrupo g on g.id = b.ope_centro_subgrupo_id;