import { Column, Entity, Index } from 'typeorm';
import { BaseEntity } from '../shared/bases/base.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';

@Index('pk_bor_tel', ['id'], { unique: true })
@Entity('bor_tel', { schema: 'public' })
export class BorTel extends BaseEntity {
  @Column('varchar', { name: 'id_tipo', length: 50 })
  idTipo: string;

  @Column('varchar', { name: 'numero_serie', length: 50 })
  numeroSerie: string;

  @Column('varchar', { name: 'dthr_msg', nullable: true, length: 50 })
  dthrMsg: string;

  @Column('varchar', { name: 'dthr_fim', nullable: true, length: 50 })
  dthrFim: string;

  @Column('varchar', {
    name: 'dthr_inicio',
    nullable: true,
    length: 50,
  })
  dthrInicio: string;

  @Column('varchar', {
    name: 'acel_viagem_m_s2',
    nullable: true,
    length: 50,
  })
  acelViagemMS2: string;

  @Column('varchar', {
    name: 'freadas_bruscas_acum',
    nullable: true,
    length: 50,
  })
  freadasBruscasAcum: string;

  @Column('varchar', {
    name: 'freadas_bruscas_viagem',
    nullable: true,
    length: 50,
  })
  freadasBruscasViagem: string;

  @Column('varchar', {
    name: 'gps_qual_acel_max_viagem',
    nullable: true,
    length: 50,
  })
  gpsQualAcelMaxViagem: string;

  @Column('varchar', {
    name: 'gps_qual_desacel_max_viagem',
    nullable: true,
    length: 50,
  })
  gpsQualDesacelMaxViagem: string;

  @Column('varchar', {
    name: 'gps_qual_rot_motor_max_viagem',
    nullable: true,
    length: 50,
  })
  gpsQualRotMotorMaxViagem: string;

  @Column('varchar', {
    name: 'gps_qual_vel_max_viagem_tac',
    nullable: true,
    length: 50,
  })
  gpsQualVelMaxViagemTac: string;

  @Column('varchar', {
    name: 'id_ibutton',
    nullable: true,
    length: 50,
  })
  idIbutton: string;

  @Column('varchar', {
    name: 'lat_acel_max_viagem',
    nullable: true,
    length: 50,
  })
  latAcelMaxViagem: string;

  @Column('varchar', {
    name: 'lat_desacel_max_viagem',
    nullable: true,
    length: 50,
  })
  latDesacelMaxViagem: string;

  @Column('varchar', {
    name: 'lat_max_tempo_marcha_lenta_viagem',
    nullable: true,
    length: 50,
  })
  latMaxTempoMarchaLentaViagem: string;

  @Column('varchar', {
    name: 'lat_rot_motor_max_viagem',
    nullable: true,
    length: 50,
  })
  latRotMotorMaxViagem: string;

  @Column('varchar', {
    name: 'lat_vel_max_banguela',
    nullable: true,
    length: 50,
  })
  latVelMaxBanguela: string;

  @Column('varchar', {
    name: 'lat_vel_max_viagem_gps',
    nullable: true,
    length: 50,
  })
  latVelMaxViagemGps: string;

  @Column('varchar', {
    name: 'lat_vel_max_viagem_tac',
    nullable: true,
    length: 50,
  })
  latVelMaxViagemTac: string;

  @Column('varchar', {
    name: 'long_acel_max_viagem',
    nullable: true,
    length: 50,
  })
  longAcelMaxViagem: string;

  @Column('varchar', {
    name: 'long_desacel_max_viagem',
    nullable: true,
    length: 50,
  })
  longDesacelMaxViagem: string;

  @Column('varchar', {
    name: 'long_max_tempo_marcha_lenta_viagem',
    nullable: true,
    length: 50,
  })
  longMaxTempoMarchaLentaViagem: string;

  @Column('varchar', {
    name: 'long_rot_motor_max_viagem',
    nullable: true,
    length: 50,
  })
  longRotMotorMaxViagem: string;

  @Column('varchar', {
    name: 'long_vel_max_banguela',
    nullable: true,
    length: 50,
  })
  longVelMaxBanguela: string;

  @Column('varchar', {
    name: 'long_vel_max_viagem_gps',
    nullable: true,
    length: 50,
  })
  longVelMaxViagemGps: string;

  @Column('varchar', {
    name: 'long_vel_max_viagem_tac',
    nullable: true,
    length: 50,
  })
  longVelMaxViagemTac: string;

  @Column('varchar', {
    name: 'maior_tempo_banguela_viagem',
    nullable: true,
    length: 50,
  })
  maiorTempoBanguelaViagem: string;

  @Column('varchar', {
    name: 'maior_vel_banguela',
    nullable: true,
    length: 50,
  })
  maiorVelBanguela: string;

  @Column('varchar', {
    name: 'media_acel_brusca_m_s2_acum',
    nullable: true,
    length: 50,
  })
  mediaAcelBruscaMS2Acum: string;

  @Column('varchar', {
    name: 'media_acel_brusca_viage_m_s2',
    nullable: true,
    length: 50,
  })
  mediaAcelBruscaViageMS2: string;

  @Column('varchar', {
    name: 'media_freadas_m_s2_acum',
    nullable: true,
    length: 50,
  })
  mediaFreadasMS2Acum: string;

  @Column('varchar', {
    name: 'media_freadas_viagem_m_s2',
    nullable: true,
    length: 50,
  })
  mediaFreadasViagemMS2: string;

  @Column('varchar', {
    name: 'nm_marcha_lenta_acum',
    nullable: true,
    length: 50,
  })
  nmMarchaLentaAcum: string;

  @Column('varchar', {
    name: 'nm_marcha_lenta_viagem',
    nullable: true,
    length: 50,
  })
  nmMarchaLentaViagem: string;

  @Column('varchar', {
    name: 'num_arranc_bruscas_acum',
    nullable: true,
    length: 50,
  })
  numArrancBruscasAcum: string;

  @Column('varchar', {
    name: 'num_arranc_bruscas_viagem',
    nullable: true,
    length: 50,
  })
  numArrancBruscasViagem: string;

  @Column('varchar', {
    name: 'num_banguela_acum',
    nullable: true,
    length: 50,
  })
  numBanguelaAcum: string;

  @Column('varchar', {
    name: 'num_banguela_viagem',
    nullable: true,
    length: 50,
  })
  numBanguelaViagem: string;

  @Column('varchar', {
    name: 'num_freio_motor_acum',
    nullable: true,
    length: 50,
  })
  numFreioMotorAcum: string;

  @Column('varchar', {
    name: 'num_rpm_acima_acum',
    nullable: true,
    length: 50,
  })
  numRpmAcimaAcum: string;

  @Column('varchar', {
    name: 'num_rpm_acima_parcial',
    nullable: true,
    length: 50,
  })
  numRpmAcimaParcial: string;

  @Column('varchar', {
    name: 'num_vezes_banguela_viagem',
    nullable: true,
    length: 50,
  })
  numVezesBanguelaViagem: string;

  @Column('varchar', {
    name: 'num_vezes_vel_acima_acum',
    nullable: true,
    length: 50,
  })
  numVezesVelAcimaAcum: string;

  @Column('varchar', {
    name: 'num_vezes_vel_acima_parcial',
    nullable: true,
    length: 50,
  })
  numVezesVelAcimaParcial: string;

  @Column('varchar', {
    name: 'odo_acum_gps_dec_km',
    nullable: true,
    length: 50,
  })
  odoAcumGpsDecKm: string;

  @Column('varchar', {
    name: 'odo_acum_tac_dec_km',
    nullable: true,
    length: 50,
  })
  odoAcumTacDecKm: string;

  @Column('varchar', {
    name: 'odo_viagem_gps_dec_km',
    nullable: true,
    length: 50,
  })
  odoViagemGpsDecKm: string;

  @Column('varchar', {
    name: 'odo_viagem_tac_dec_km',
    nullable: true,
    length: 50,
  })
  odoViagemTacDecKm: string;

  @Column('varchar', {
    name: 'rot_motor_max_viagem',
    nullable: true,
    length: 50,
  })
  rotMotorMaxViagem: string;

  @Column('varchar', {
    name: 'rot_motor_med_viagem',
    nullable: true,
    length: 50,
  })
  rotMotorMedViagem: string;

  @Column('varchar', {
    name: 'tensao_batt_bkp_med_dec_volts',
    nullable: true,
    length: 50,
  })
  tensaoBattBkpMedDecVolts: string;

  @Column('varchar', {
    name: 'tensao_batt_veic_med_dec_volts',
    nullable: true,
    length: 50,
  })
  tensaoBattVeicMedDecVolts: string;

  @Column('varchar', {
    name: 'dthr_acel_max_viagem',
    nullable: true,
    length: 50,
  })
  dthrAcelMaxViagem: string;

  @Column('varchar', {
    name: 'dthr_desacel_max_viagem',
    nullable: true,
    length: 50,
  })
  dthrDesacelMaxViagem: string;

  @Column('varchar', {
    name: 'dthr_max_tempo_marcha_lenta_viagem',
    nullable: true,
    length: 50,
  })
  dthrMaxTempoMarchaLentaViagem: string;

  @Column('varchar', {
    name: 'dthr_rot_motor_max_viagem',
    nullable: true,
    length: 50,
  })
  dthrRotMotorMaxViagem: string;

  @Column('varchar', {
    name: 'dthr_vel_max_banguela',
    nullable: true,
    length: 50,
  })
  dthrVelMaxBanguela: string;

  @Column('varchar', {
    name: 'dthr_vel_max_viagem_gps',
    nullable: true,
    length: 50,
  })
  dthrVelMaxViagemGps: string;

  @Column('varchar', {
    name: 'dthr_vel_max_viagem_tac',
    nullable: true,
    length: 50,
  })
  dthrVelMaxViagemTac: string;

  @Column('varchar', {
    name: 'tempo_faixa_amarela_acum',
    nullable: true,
    length: 50,
  })
  tempoFaixaAmarelaAcum: string;

  @Column('varchar', {
    name: 'tempo_faixa_amarela_parcial',
    nullable: true,
    length: 50,
  })
  tempoFaixaAmarelaParcial: string;

  @Column('varchar', {
    name: 'tempo_faixa_azul_acum',
    nullable: true,
    length: 50,
  })
  tempoFaixaAzulAcum: string;

  @Column('varchar', {
    name: 'tempo_faixa_azul_parcial',
    nullable: true,
    length: 50,
  })
  tempoFaixaAzulParcial: string;

  @Column('varchar', {
    name: 'tempo_faixa_verde_acum',
    nullable: true,
    length: 50,
  })
  tempoFaixaVerdeAcum: string;

  @Column('varchar', {
    name: 'tempo_faixa_verde_parcial',
    nullable: true,
    length: 50,
  })
  tempoFaixaVerdeParcial: string;

  @Column('varchar', {
    name: 'tempo_faixa_vermelha_acum',
    nullable: true,
    length: 50,
  })
  tempoFaixaVermelhaAcum: string;

  @Column('varchar', {
    name: 'tempo_faixa_vermelha_parcial',
    nullable: true,
    length: 50,
  })
  tempoFaixaVermelhaParcial: string;

  @Column('varchar', {
    name: 'tempo_freio_motor_acum',
    nullable: true,
    length: 50,
  })
  tempoFreioMotorAcum: string;

  @Column('varchar', {
    name: 'tempo_marcha_lenta_acum',
    nullable: true,
    length: 50,
  })
  tempoMarchaLentaAcum: string;

  @Column('varchar', {
    name: 'tempo_marcha_lenta_viagem',
    nullable: true,
    length: 50,
  })
  tempoMarchaLentaViagem: string;

  @Column('varchar', {
    name: 'tempo_max_marcha_lenta_viagem',
    nullable: true,
    length: 50,
  })
  tempoMaxMarchaLentaViagem: string;

  @Column('varchar', {
    name: 'tempo_medio_marcha_lenta_viagem',
    nullable: true,
    length: 50,
  })
  tempoMedioMarchaLentaViagem: string;

  @Column('varchar', {
    name: 'tempo_pedal_freio_acionado_viagem',
    nullable: true,
    length: 50,
  })
  tempoPedalFreioAcionadoViagem: string;

  @Column('varchar', {
    name: 'tempo_perm_bang_acum_secs',
    nullable: true,
    length: 50,
  })
  tempoPermBangAcumSecs: string;

  @Column('varchar', {
    name: 'tempo_perm_bang_viagem_secs',
    nullable: true,
    length: 50,
  })
  tempoPermBangViagemSecs: string;

  @Column('varchar', {
    name: 'tempo_rpm_acima_acum',
    nullable: true,
    length: 50,
  })
  tempoRpmAcimaAcum: string;

  @Column('varchar', {
    name: 'tempo_rpm_acima_parcial',
    nullable: true,
    length: 50,
  })
  tempoRpmAcimaParcial: string;

  @Column('varchar', {
    name: 'tempo_uso_acum_em_movimento_secs',
    length: 50,
  })
  tempoUsoAcumEmMovimentoSecs: string;

  @Column('varchar', {
    name: 'tempo_uso_acum_parado_secs',
    nullable: true,
    length: 50,
  })
  tempoUsoAcumParadoSecs: string;

  @Column('varchar', {
    name: 'tempo_uso_acum_total_secs',
    nullable: true,
    length: 50,
  })
  tempoUsoAcumTotalSecs: string;

  @Column('varchar', {
    name: 'tempo_uso_viagem_em_movto_secs',
    nullable: true,
    length: 50,
  })
  tempoUsoViagemEmMovtoSecs: string;

  @Column('varchar', {
    name: 'tempo_uso_viagem_parado_secs',
    nullable: true,
    length: 50,
  })
  tempoUsoViagemParadoSecs: string;

  @Column('varchar', {
    name: 'tempo_uso_viagem_total_secs',
    nullable: true,
    length: 50,
  })
  tempoUsoViagemTotalSecs: string;

  @Column('varchar', {
    name: 'tempo_veic_deslig_acum_secs',
    nullable: true,
    length: 50,
  })
  tempoVeicDesligAcumSecs: string;

  @Column('varchar', {
    name: 'tempo_veic_desl_entre_viagens_secs',
    nullable: true,
    length: 50,
  })
  tempoVeicDeslEntreViagensSecs: string;

  @Column('varchar', {
    name: 'tempo_vel_acima_acum',
    nullable: true,
    length: 50,
  })
  tempoVelAcimaAcum: string;

  @Column('varchar', {
    name: 'tempo_vel_acima_parcial',
    nullable: true,
    length: 50,
  })
  tempoVelAcimaParcial: string;

  @Column('varchar', {
    name: 'vel_final_frenagem_brusca',
    nullable: true,
    length: 50,
  })
  velFinalFrenagemBrusca: string;

  @Column('varchar', {
    name: 'vel_final_max_acel_brusca',
    nullable: true,
    length: 50,
  })
  velFinalMaxAcelBrusca: string;

  @Column('varchar', {
    name: 'vel_inicial_frenagem_brusca',
    nullable: true,
    length: 50,
  })
  velInicialFrenagemBrusca: string;

  @Column('varchar', {
    name: 'vel_inicial_max_acel_brusca',
    nullable: true,
    length: 50,
  })
  velInicialMaxAcelBrusca: string;

  @Column('varchar', {
    name: 'vel_max_viagem_gps',
    nullable: true,
    length: 50,
  })
  velMaxViagemGps: string;

  @Column('varchar', {
    name: 'vel_max_viagem_tac',
    nullable: true,
    length: 50,
  })
  velMaxViagemTac: string;

  @Column('varchar', {
    name: 'vel_media_gps_acum',
    nullable: true,
    length: 50,
  })
  velMediaGpsAcum: string;

  @Column('varchar', {
    name: 'vel_media_tac_acum',
    nullable: true,
    length: 50,
  })
  velMediaTacAcum: string;

  @Column('varchar', {
    name: 'vel_med_viagem_gps',
    nullable: true,
    length: 50,
  })
  velMedViagemGps: string;

  @Column('varchar', {
    name: 'vel_med_viagem_tac',
    nullable: true,
    length: 50,
  })
  velMedViagemTac: string;

  @Column('varchar', {
    name: 'id_reatime',
    nullable: true,
    length: 100,
  })
  idReatime: string;

  @Column('varchar', {
    name: 'status_msg',
    nullable: true,
    length: 50,
  })
  statusMsg: string;

  @Column('timestamp without time zone', {
    name: 'dthr_status',
    nullable: true,
  })
  dthrStatus: Date | null;

  @Column('varchar', {
    name: 'ger_empresa_id',
    nullable: true,
    length: 36,
  })
  gerEmpresaId: string;

  @Column('varchar', {
    name: 'ope_centro2_pessoa_id',
    nullable: true,
    length: 36,
  })
  opeCentro2PessoaId: string;

  @Column('varchar', {
    name: 'ope_centro2_equip_id_1',
    nullable: true,
    length: 50,
  })
  opeCentro2EquipId_1: string;

  @Column('varchar', { name: 'unit_id', length: 36 })
  unitId: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;
}
