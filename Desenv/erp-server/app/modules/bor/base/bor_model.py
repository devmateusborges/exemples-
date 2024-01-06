import app
from app.generics.generic_model import generic_model


# ==========================================================


class BorDispositivo(generic_model, app.db.Model):
    __tablename__ = "bor_dispositivo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    numero_serie = app.db.Column(app.db.String(50), unique=True)
    tipo = app.db.Column(app.db.String(1))

    ope_centro2_equip_id = app.db.Column(app.db.ForeignKey("ope_centro2_equip.id"))
    ope_centro2_equip_id_obj = app.db.relationship("OpeCentro2Equip")
    ope_centro2_pessoa_id = app.db.Column(app.db.ForeignKey("ope_centro2_pessoa.id"))
    ope_centro2_pessoa_id_obj = app.db.relationship("OpeCentro2Pessoa")


class BorMov(generic_model, app.db.Model):
    __tablename__ = "bor_mov"

    id_tipo = app.db.Column(app.db.String(36))
    numero_serie = app.db.Column(app.db.String(50))
    ibutton_rfid = app.db.Column(app.db.String(50))
    dthr_track = app.db.Column(app.db.TIMESTAMP())
    gps_altitude = app.db.Column(app.db.String(50))
    gps_altitude_status = app.db.Column(app.db.String(50))
    gps_lat = app.db.Column(app.db.String(50))
    gps_long = app.db.Column(app.db.String(50))
    gps_angulo_norte = app.db.Column(app.db.String(50))
    gps_posicao_status = app.db.Column(app.db.String(50))
    gps_velocidade = app.db.Column(app.db.String(50))
    gps_velocidade_media = app.db.Column(app.db.String(50))
    equipamento_ignicao = app.db.Column(app.db.String(50))
    equipamento_bateria = app.db.Column(app.db.String(50))
    equipamento_odometro = app.db.Column(app.db.String(50))
    equipamento_rpm = app.db.Column(app.db.String(50))
    equipamento_veloc = app.db.Column(app.db.String(50))
    equipamento_veloc_odom = app.db.Column(app.db.String(50))
    equipamento_veloc_odom_media = app.db.Column(app.db.String(50))
    geom = app.db.Column(index=True)
    ope_centro2_equip_id_1 = app.db.Column(app.db.String(36))
    ope_centro2_equip_id_2 = app.db.Column(app.db.String(36))
    ope_centro2_pessoa_id = app.db.Column(app.db.String(36))
    ger_empresa_id = app.db.Column(app.db.String(36))
    ope_centro2_area_id = app.db.Column(app.db.String(36))
    geom_circle = app.db.Column(index=True)
    id_realtime = app.db.Column(app.db.String(100))
    buzzer = app.db.Column(app.db.String(4))
    unit_id = app.db.Column(
        app.db.String(36),
    )
    status = app.db.Column(app.db.String(2))
    dthr_status = app.db.Column(app.db.TIMESTAMP())
    ope_atividade_id = app.db.Column(app.db.String(36))
    qnt_ha_trab = app.db.Column(
        app.db.Numeric(18, 6),
    )
    geom_line = app.db.Column()
    duracao = app.db.Column(app.db.Numeric(18, 6))


# ==========================================================


class BorMovAtual(generic_model, app.db.Model):
    __tablename__ = "bor_mov_atual"

    ope_centro2_equip_id = app.db.Column(
        app.db.String(36),
    )
    id_tipo = app.db.Column(app.db.String(50))
    numero_serie = app.db.Column(app.db.String(50))
    ibutton_rfid = app.db.Column(app.db.String(50))
    dthr_track = app.db.Column(app.db.TIMESTAMP())
    gps_altitude = app.db.Column(app.db.String(50))
    gps_altitude_status = app.db.Column(app.db.String(50))
    gps_lat = app.db.Column(app.db.String(50))
    gps_long = app.db.Column(app.db.String(50))
    gps_angulo_norte = app.db.Column(app.db.String(50))
    gps_posicao_status = app.db.Column(app.db.String(50))
    gps_velocidade = app.db.Column(app.db.String(50))
    gps_velocidade_media = app.db.Column(app.db.String(50))
    equipamento_ignicao = app.db.Column(app.db.String(50))
    equipamento_bateria = app.db.Column(app.db.String(50))
    equipamento_odometro = app.db.Column(app.db.String(50))
    equipamento_rpm = app.db.Column(app.db.String(50))
    equipamento_veloc = app.db.Column(app.db.String(50))
    equipamento_veloc_odom = app.db.Column(app.db.String(50))
    equipamento_veloc_odom_media = app.db.Column(app.db.String(50))
    geom = app.db.Column(index=True)
    ope_centro2_pessoa_id = app.db.Column(app.db.String(36))
    ger_empresa_id = app.db.Column(app.db.String(36))
    ope_centro2_area_id = app.db.Column(app.db.String(36))
    unit_id = app.db.Column(app.db.String(36))
    dthr_ignicao_last_off = app.db.Column(app.db.TIMESTAMP())


# ==========================================================


class BorMsg(generic_model, app.db.Model):
    __tablename__ = "bor_msg"

    id_tipo = app.db.Column(app.db.String(50))
    numero_serie = app.db.Column(app.db.String(50))
    dthr_trans_msg_rast = app.db.Column(app.db.TIMESTAMP())
    dthr_msg_gerada = app.db.Column(app.db.TIMESTAMP())
    grupo_msg = app.db.Column(app.db.String(30))
    index_msg = app.db.Column(app.db.String(30))
    dthr_posicao = app.db.Column(app.db.TIMESTAMP())
    latitude = app.db.Column(app.db.String(50))
    longitude = app.db.Column(app.db.String(50))
    qualidade_posi = app.db.Column(app.db.String(10))
    valor_msg = app.db.Column(app.db.String(100))
    status_msg = app.db.Column(app.db.String(50))
    dthr_status = app.db.Column(app.db.TIMESTAMP())
    ger_empresa_id = app.db.Column(app.db.String(36))
    ope_centro2_equip_id_1 = app.db.Column(app.db.String(50))
    unit_id = app.db.Column(app.db.String(36))
    corpo_msg = app.db.Column(app.db.String(250))
    ope_atividade_id = app.db.Column(app.db.String(36))


# ==========================================================


class BorTel(generic_model, app.db.Model):
    __tablename__ = "bor_tel"

    id_tipo = app.db.Column(
        app.db.String(50),
    )
    numero_serie = app.db.Column(app.db.String(50))
    dthr_msg = app.db.Column(app.db.String(50))
    dthr_fim = app.db.Column(app.db.String(50))
    dthr_inicio = app.db.Column(app.db.String(50))
    acel_viagem_m_s2 = app.db.Column(app.db.String(50))
    freadas_bruscas_acum = app.db.Column(app.db.String(50))
    freadas_bruscas_viagem = app.db.Column(app.db.String(50))
    gps_qual_acel_max_viagem = app.db.Column(app.db.String(50))
    gps_qual_desacel_max_viagem = app.db.Column(app.db.String(50))
    gps_qual_rot_motor_max_viagem = app.db.Column(app.db.String(50))
    gps_qual_vel_max_viagem_tac = app.db.Column(app.db.String(50))
    id_ibutton = app.db.Column(app.db.String(50))
    lat_acel_max_viagem = app.db.Column(app.db.String(50))
    lat_desacel_max_viagem = app.db.Column(app.db.String(50))
    lat_max_tempo_marcha_lenta_viagem = app.db.Column(app.db.String(50))
    lat_rot_motor_max_viagem = app.db.Column(app.db.String(50))
    lat_vel_max_banguela = app.db.Column(app.db.String(50))
    lat_vel_max_viagem_gps = app.db.Column(app.db.String(50))
    lat_vel_max_viagem_tac = app.db.Column(app.db.String(50))
    long_acel_max_viagem = app.db.Column(app.db.String(50))
    long_desacel_max_viagem = app.db.Column(app.db.String(50))
    long_max_tempo_marcha_lenta_viagem = app.db.Column(app.db.String(50))
    long_rot_motor_max_viagem = app.db.Column(app.db.String(50))
    long_vel_max_banguela = app.db.Column(app.db.String(50))
    long_vel_max_viagem_gps = app.db.Column(app.db.String(50))
    long_vel_max_viagem_tac = app.db.Column(app.db.String(50))
    maior_tempo_banguela_viagem = app.db.Column(app.db.String(50))
    maior_vel_banguela = app.db.Column(app.db.String(50))
    media_acel_brusca_m_s2_acum = app.db.Column(app.db.String(50))
    media_acel_brusca_viage_m_s2 = app.db.Column(app.db.String(50))
    media_freadas_m_s2_acum = app.db.Column(app.db.String(50))
    media_freadas_viagem_m_s2 = app.db.Column(app.db.String(50))
    nm_marcha_lenta_acum = app.db.Column(app.db.String(50))
    nm_marcha_lenta_viagem = app.db.Column(app.db.String(50))
    num_arranc_bruscas_acum = app.db.Column(app.db.String(50))
    num_arranc_bruscas_viagem = app.db.Column(app.db.String(50))
    num_banguela_acum = app.db.Column(app.db.String(50))
    num_banguela_viagem = app.db.Column(app.db.String(50))
    num_freio_motor_acum = app.db.Column(app.db.String(50))
    num_rpm_acima_acum = app.db.Column(app.db.String(50))
    num_rpm_acima_parcial = app.db.Column(app.db.String(50))
    num_vezes_banguela_viagem = app.db.Column(app.db.String(50))
    num_vezes_vel_acima_acum = app.db.Column(app.db.String(50))
    num_vezes_vel_acima_parcial = app.db.Column(app.db.String(50))
    odo_acum_gps_dec_km = app.db.Column(app.db.String(50))
    odo_acum_tac_dec_km = app.db.Column(app.db.String(50))
    odo_viagem_gps_dec_km = app.db.Column(app.db.String(50))
    odo_viagem_tac_dec_km = app.db.Column(app.db.String(50))
    rot_motor_max_viagem = app.db.Column(app.db.String(50))
    rot_motor_med_viagem = app.db.Column(app.db.String(50))
    tensao_batt_bkp_med_dec_volts = app.db.Column(app.db.String(50))
    tensao_batt_veic_med_dec_volts = app.db.Column(app.db.String(50))
    dthr_acel_max_viagem = app.db.Column(app.db.String(50))
    dthr_desacel_max_viagem = app.db.Column(app.db.String(50))
    dthr_max_tempo_marcha_lenta_viagem = app.db.Column(app.db.String(50))
    dthr_rot_motor_max_viagem = app.db.Column(app.db.String(50))
    dthr_vel_max_banguela = app.db.Column(app.db.String(50))
    dthr_vel_max_viagem_gps = app.db.Column(app.db.String(50))
    dthr_vel_max_viagem_tac = app.db.Column(app.db.String(50))
    tempo_faixa_amarela_acum = app.db.Column(app.db.String(50))
    tempo_faixa_amarela_parcial = app.db.Column(app.db.String(50))
    tempo_faixa_azul_acum = app.db.Column(app.db.String(50))
    tempo_faixa_azul_parcial = app.db.Column(app.db.String(50))
    tempo_faixa_verde_acum = app.db.Column(app.db.String(50))
    tempo_faixa_verde_parcial = app.db.Column(app.db.String(50))
    tempo_faixa_vermelha_acum = app.db.Column(app.db.String(50))
    tempo_faixa_vermelha_parcial = app.db.Column(app.db.String(50))
    tempo_freio_motor_acum = app.db.Column(app.db.String(50))
    tempo_marcha_lenta_acum = app.db.Column(app.db.String(50))
    tempo_marcha_lenta_viagem = app.db.Column(app.db.String(50))
    tempo_max_marcha_lenta_viagem = app.db.Column(app.db.String(50))
    tempo_medio_marcha_lenta_viagem = app.db.Column(app.db.String(50))
    tempo_pedal_freio_acionado_viagem = app.db.Column(app.db.String(50))
    tempo_perm_bang_acum_secs = app.db.Column(app.db.String(50))
    tempo_perm_bang_viagem_secs = app.db.Column(app.db.String(50))
    tempo_rpm_acima_acum = app.db.Column(app.db.String(50))
    tempo_rpm_acima_parcial = app.db.Column(app.db.String(50))
    tempo_uso_acum_em_movimento_secs = app.db.Column(
        app.db.String(50),
    )
    tempo_uso_acum_parado_secs = app.db.Column(app.db.String(50))
    tempo_uso_acum_total_secs = app.db.Column(app.db.String(50))
    tempo_uso_viagem_em_movto_secs = app.db.Column(app.db.String(50))
    tempo_uso_viagem_parado_secs = app.db.Column(app.db.String(50))
    tempo_uso_viagem_total_secs = app.db.Column(app.db.String(50))
    tempo_veic_deslig_acum_secs = app.db.Column(app.db.String(50))
    tempo_veic_desl_entre_viagens_secs = app.db.Column(app.db.String(50))
    tempo_vel_acima_acum = app.db.Column(app.db.String(50))
    tempo_vel_acima_parcial = app.db.Column(app.db.String(50))
    vel_final_frenagem_brusca = app.db.Column(app.db.String(50))
    vel_final_max_acel_brusca = app.db.Column(app.db.String(50))
    vel_inicial_frenagem_brusca = app.db.Column(app.db.String(50))
    vel_inicial_max_acel_brusca = app.db.Column(app.db.String(50))
    vel_max_viagem_gps = app.db.Column(app.db.String(50))
    vel_max_viagem_tac = app.db.Column(app.db.String(50))
    vel_media_gps_acum = app.db.Column(app.db.String(50))
    vel_media_tac_acum = app.db.Column(app.db.String(50))
    vel_med_viagem_gps = app.db.Column(app.db.String(50))
    vel_med_viagem_tac = app.db.Column(app.db.String(50))
    id_reatime = app.db.Column(app.db.String(100))
    status_msg = app.db.Column(app.db.String(50))
    dthr_status = app.db.Column(app.db.TIMESTAMP())
    ger_empresa_id = app.db.Column(app.db.String(36))
    ope_centro2_pessoa_id = app.db.Column(app.db.String(36))
    ope_centro2_equip_id_1 = app.db.Column(app.db.String(50))
    unit_id = app.db.Column(
        app.db.String(36),
    )


# ==========================================================


class BorUnitParam(generic_model, app.db.Model):
    __tablename__ = "bor_unit_param"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    data_valid_ini = app.db.Column(app.db.Date)


# ==========================================================
