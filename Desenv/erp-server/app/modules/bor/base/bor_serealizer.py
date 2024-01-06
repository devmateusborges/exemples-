import app
from app.modules.bor.base.bor_model import (
    BorDispositivo,
    BorMov,
    BorMovAtual,
    BorMsg,
    BorTel,
    BorUnitParam,
)
from app.generics.generic_schema import generic_schema
from marshmallow import fields, EXCLUDE
from app.generics.generic_schema_field import fields_Type_Obj_Sql
from app.utils.validator_util import valid_type_choice_sql


# ==========================================================
class BorDispositivoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = BorDispositivo
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    numero_serie = fields.Str(required=True)
    tipo = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="bor_dispositivo", field_name="tipo", session=app.db.session
        ),
    )
    tipo_obj = fields_Type_Obj_Sql(
        field_choice="tipo",
        table_name="bor_dispositivo",
        field_name="tipo",
        session=app.db.session,
    )

    ope_centro2_equip_id = fields.Str(required=True)
    ope_centro2_equip_id_obj = fields.Nested("OpeCentro2EquipSchema", dump_only=True)
    ope_centro2_pessoa_id = fields.Str(required=True)
    ope_centro2_pessoa_id_obj = fields.Nested("OpeCentro2PessoaSchema", dump_only=True)


# ==========================================================


class BorMovSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = BorMov
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    id_tipo = fields.Str(required=True)
    numero_serie = fields.Str(required=True)
    ibutton_rfid = fields.Str(required=True)
    dthr_track = fields.Str(required=True)
    gps_altitude = fields.Str(required=True)
    gps_altitude_status = fields.Str(required=True)
    gps_lat = fields.Str(required=True)
    gps_long = fields.Str(required=True)
    gps_angulo_norte = fields.Str(required=True)
    gps_posicao_status = fields.Str(required=True)
    gps_velocidade = fields.Str(required=True)
    gps_velocidade_media = fields.Str(required=True)
    equipamento_ignicao = fields.Str(required=True)
    equipamento_bateria = fields.Str(required=True)
    equipamento_odometro = fields.Str(required=True)
    equipamento_rpm = fields.Str(required=True)
    equipamento_veloc = fields.Str(required=True)
    equipamento_veloc_odom = fields.Str(required=True)
    equipamento_veloc_odom_media = fields.Str(required=True)
    geom = app.db.Column(index=True)
    ope_centro2_equip_id_1 = fields.Str(required=True)
    ope_centro2_equip_id_2 = fields.Str(required=True)
    ope_centro2_pessoa_id = fields.Str(required=True)
    ger_empresa_id = fields.Str(required=True)
    ope_centro2_area_id = fields.Str(required=True)
    geom_circle = app.db.Column(index=True)
    id_realtime = fields.Str(required=True)
    buzzer = fields.Str(required=True)
    unit_id = fields.Str(required=True)
    status = fields.Str(required=True)
    dthr_status = fields.Str(required=True)
    ope_atividade_id = fields.Str(required=True)
    qnt_ha_trab = fields.Str(required=True)
    geom_line = app.db.Column()
    duracao = fields.Str(required=True)


# ==========================================================


class BorMovAtualSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = BorMovAtual
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    ope_centro2_equip_id = fields.Str(required=True)
    id_tipo = fields.Str(required=True)
    numero_serie = fields.Str(required=True)
    ibutton_rfid = fields.Str(required=True)
    dthr_track = fields.Str(required=True)
    gps_altitude = fields.Str(required=True)
    gps_altitude_status = fields.Str(required=True)
    gps_lat = fields.Str(required=True)
    gps_long = fields.Str(required=True)
    gps_angulo_norte = fields.Str(required=True)
    gps_posicao_status = fields.Str(required=True)
    gps_velocidade = fields.Str(required=True)
    gps_velocidade_media = fields.Str(required=True)
    equipamento_ignicao = fields.Str(required=True)
    equipamento_bateria = fields.Str(required=True)
    equipamento_odometro = fields.Str(required=True)
    equipamento_rpm = fields.Str(required=True)
    equipamento_veloc = fields.Str(required=True)
    equipamento_veloc_odom = fields.Str(required=True)
    equipamento_veloc_odom_media = fields.Str(required=True)
    geom = app.db.Column(index=True)
    ope_centro2_pessoa_id = fields.Str(required=True)
    ger_empresa_id = fields.Str(required=True)
    ope_centro2_area_id = fields.Str(required=True)
    unit_id = fields.Str(required=True)
    dthr_ignicao_last_off = fields.Str(required=True)


# ==========================================================


class BorMsgSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = BorMsg
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    id_tipo = fields.Str(required=True)
    numero_serie = fields.Str(required=True)
    dthr_trans_msg_rast = fields.Str(required=True)
    dthr_msg_gerada = fields.Str(required=True)
    grupo_msg = fields.Str(required=True)
    index_msg = fields.Str(required=True)
    dthr_posicao = fields.Str(required=True)
    latitude = fields.Str(required=True)
    longitude = fields.Str(required=True)
    qualidade_posi = fields.Str(required=True)
    valor_msg = fields.Str(required=True)
    status_msg = fields.Str(required=True)
    dthr_status = fields.Str(required=True)
    ger_empresa_id = fields.Str(required=True)
    ope_centro2_equip_id_1 = fields.Str(required=True)
    unit_id = fields.Str(required=True)
    corpo_msg = fields.Str(required=True)
    ope_atividade_id = fields.Str(required=True)


# ==========================================================


class BorTelSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = BorTel
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    id_tipo = fields.Str(required=True)
    numero_serie = fields.Str(required=True)
    dthr_msg = fields.Str(required=True)
    dthr_fim = fields.Str(required=True)
    dthr_inicio = fields.Str(required=True)
    acel_viagem_m_s2 = fields.Str(required=True)
    freadas_bruscas_acum = fields.Str(required=True)
    freadas_bruscas_viagem = fields.Str(required=True)
    gps_qual_acel_max_viagem = fields.Str(required=True)
    gps_qual_desacel_max_viagem = fields.Str(required=True)
    gps_qual_rot_motor_max_viagem = fields.Str(required=True)
    gps_qual_vel_max_viagem_tac = fields.Str(required=True)
    id_ibutton = fields.Str(required=True)
    lat_acel_max_viagem = fields.Str(required=True)
    lat_desacel_max_viagem = fields.Str(required=True)
    lat_max_tempo_marcha_lenta_viagem = fields.Str(required=True)
    lat_rot_motor_max_viagem = fields.Str(required=True)
    lat_vel_max_banguela = fields.Str(required=True)
    lat_vel_max_viagem_gps = fields.Str(required=True)
    lat_vel_max_viagem_tac = fields.Str(required=True)
    long_acel_max_viagem = fields.Str(required=True)
    long_desacel_max_viagem = fields.Str(required=True)
    long_max_tempo_marcha_lenta_viagem = fields.Str(required=True)
    long_rot_motor_max_viagem = fields.Str(required=True)
    long_vel_max_banguela = fields.Str(required=True)
    long_vel_max_viagem_gps = fields.Str(required=True)
    long_vel_max_viagem_tac = fields.Str(required=True)
    maior_tempo_banguela_viagem = fields.Str(required=True)
    maior_vel_banguela = fields.Str(required=True)
    media_acel_brusca_m_s2_acum = fields.Str(required=True)
    media_acel_brusca_viage_m_s2 = fields.Str(required=True)
    media_freadas_m_s2_acum = fields.Str(required=True)
    media_freadas_viagem_m_s2 = fields.Str(required=True)
    nm_marcha_lenta_acum = fields.Str(required=True)
    nm_marcha_lenta_viagem = fields.Str(required=True)
    num_arranc_bruscas_acum = fields.Str(required=True)
    num_arranc_bruscas_viagem = fields.Str(required=True)
    num_banguela_acum = fields.Str(required=True)
    num_banguela_viagem = fields.Str(required=True)
    num_freio_motor_acum = fields.Str(required=True)
    num_rpm_acima_acum = fields.Str(required=True)
    num_rpm_acima_parcial = fields.Str(required=True)
    num_vezes_banguela_viagem = fields.Str(required=True)
    num_vezes_vel_acima_acum = fields.Str(required=True)
    num_vezes_vel_acima_parcial = fields.Str(required=True)
    odo_acum_gps_dec_km = fields.Str(required=True)
    odo_acum_tac_dec_km = fields.Str(required=True)
    odo_viagem_gps_dec_km = fields.Str(required=True)
    odo_viagem_tac_dec_km = fields.Str(required=True)
    rot_motor_max_viagem = fields.Str(required=True)
    rot_motor_med_viagem = fields.Str(required=True)
    tensao_batt_bkp_med_dec_volts = fields.Str(required=True)
    tensao_batt_veic_med_dec_volts = fields.Str(required=True)
    dthr_acel_max_viagem = fields.Str(required=True)
    dthr_desacel_max_viagem = fields.Str(required=True)
    dthr_max_tempo_marcha_lenta_viagem = fields.Str(required=True)
    dthr_rot_motor_max_viagem = fields.Str(required=True)
    dthr_vel_max_banguela = fields.Str(required=True)
    dthr_vel_max_viagem_gps = fields.Str(required=True)
    dthr_vel_max_viagem_tac = fields.Str(required=True)
    tempo_faixa_amarela_acum = fields.Str(required=True)
    tempo_faixa_amarela_parcial = fields.Str(required=True)
    tempo_faixa_azul_acum = fields.Str(required=True)
    tempo_faixa_azul_parcial = fields.Str(required=True)
    tempo_faixa_verde_acum = fields.Str(required=True)
    tempo_faixa_verde_parcial = fields.Str(required=True)
    tempo_faixa_vermelha_acum = fields.Str(required=True)
    tempo_faixa_vermelha_parcial = fields.Str(required=True)
    tempo_freio_motor_acum = fields.Str(required=True)
    tempo_marcha_lenta_acum = fields.Str(required=True)
    tempo_marcha_lenta_viagem = fields.Str(required=True)
    tempo_max_marcha_lenta_viagem = fields.Str(required=True)
    tempo_medio_marcha_lenta_viagem = fields.Str(required=True)
    tempo_pedal_freio_acionado_viagem = fields.Str(required=True)
    tempo_perm_bang_acum_secs = fields.Str(required=True)
    tempo_perm_bang_viagem_secs = fields.Str(required=True)
    tempo_rpm_acima_acum = fields.Str(required=True)
    tempo_rpm_acima_parcial = fields.Str(required=True)
    tempo_uso_acum_em_movimento_secs = fields.Str(required=True)
    tempo_uso_acum_parado_secs = fields.Str(required=True)
    tempo_uso_acum_total_secs = fields.Str(required=True)
    tempo_uso_viagem_em_movto_secs = fields.Str(required=True)
    tempo_uso_viagem_parado_secs = fields.Str(required=True)
    tempo_uso_viagem_total_secs = fields.Str(required=True)
    tempo_veic_deslig_acum_secs = fields.Str(required=True)
    tempo_veic_desl_entre_viagens_secs = fields.Str(required=True)
    tempo_vel_acima_acum = fields.Str(required=True)
    tempo_vel_acima_parcial = fields.Str(required=True)
    vel_final_frenagem_brusca = fields.Str(required=True)
    vel_final_max_acel_brusca = fields.Str(required=True)
    vel_inicial_frenagem_brusca = fields.Str(required=True)
    vel_inicial_max_acel_brusca = fields.Str(required=True)
    vel_max_viagem_gps = fields.Str(required=True)
    vel_max_viagem_tac = fields.Str(required=True)
    vel_media_gps_acum = fields.Str(required=True)
    vel_media_tac_acum = fields.Str(required=True)
    vel_med_viagem_gps = fields.Str(required=True)
    vel_med_viagem_tac = fields.Str(required=True)
    id_reatime = fields.Str(required=True)
    status_msg = fields.Str(required=True)
    dthr_status = fields.Str(required=True)
    ger_empresa_id = fields.Str(required=True)
    ope_centro2_pessoa_id = fields.Str(required=True)
    ope_centro2_equip_id_1 = fields.Str(required=True)
    unit_id = fields.Str(required=True)


# ==========================================================


class BorUnitParamSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = BorUnitParam
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=False, allow_none=True)
    data_valid_ini = fields.Str(required=True)
