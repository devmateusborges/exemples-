import { Column, Entity, Index } from 'typeorm';
import { BaseEntity } from '../shared/bases/base.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';

@Index('idx_bor_mov_04', ['dthrTrack'], {})
@Index('idx_bor_mov_geom', ['geom'], {})
@Index('idx_bor_mov_geom_circle', ['geomCircle'], {})
@Index('idx_bor_mov_03', ['ibuttonRfid'], {})
@Index('pk_bor_mov', ['id'], { unique: true })
@Index('idx_bor_mov_01', ['idTipo'], {})
@Index('idx_bor_mov_02', ['numeroSerie'], {})
@Entity('bor_mov', { schema: 'public' })
export class BorMov extends BaseEntity {
  @Column('varchar', { name: 'id_tipo', length: 36 })
  idTipo: string;

  @Column('varchar', { name: 'numero_serie', length: 50 })
  numeroSerie: string;

  @Column('varchar', {
    name: 'ibutton_rfid',
    nullable: true,
    length: 50,
  })
  ibuttonRfid: string;

  @Column('timestamp without time zone', { name: 'dthr_track' })
  dthrTrack: Date;

  @Column('varchar', {
    name: 'gps_altitude',
    nullable: true,
    length: 50,
  })
  gpsAltitude: string;

  @Column('varchar', {
    name: 'gps_altitude_status',
    nullable: true,
    length: 50,
  })
  gpsAltitudeStatus: string;

  @Column('varchar', { name: 'gps_lat', nullable: true, length: 50 })
  gpsLat: string;

  @Column('varchar', { name: 'gps_long', nullable: true, length: 50 })
  gpsLong: string;

  @Column('varchar', {
    name: 'gps_angulo_norte',
    nullable: true,
    length: 50,
  })
  gpsAnguloNorte: string;

  @Column('varchar', {
    name: 'gps_posicao_status',
    nullable: true,
    length: 50,
  })
  gpsPosicaoStatus: string;

  @Column('varchar', {
    name: 'gps_velocidade',
    nullable: true,
    length: 50,
  })
  gpsVelocidade: string;

  @Column('varchar', {
    name: 'gps_velocidade_media',
    nullable: true,
    length: 50,
  })
  gpsVelocidadeMedia: string;

  @Column('varchar', {
    name: 'equipamento_ignicao',
    nullable: true,
    length: 50,
  })
  equipamentoIgnicao: string;

  @Column('varchar', {
    name: 'equipamento_bateria',
    nullable: true,
    length: 50,
  })
  equipamentoBateria: string;

  @Column('varchar', {
    name: 'equipamento_odometro',
    nullable: true,
    length: 50,
  })
  equipamentoOdometro: string;

  @Column('varchar', {
    name: 'equipamento_rpm',
    nullable: true,
    length: 50,
  })
  equipamentoRpm: string;

  @Column('varchar', {
    name: 'equipamento_veloc',
    nullable: true,
    length: 50,
  })
  equipamentoVeloc: string;

  @Column('varchar', {
    name: 'equipamento_veloc_odom',
    nullable: true,
    length: 50,
  })
  equipamentoVelocOdom: string;

  @Column('varchar', {
    name: 'equipamento_veloc_odom_media',
    nullable: true,
    length: 50,
  })
  equipamentoVelocOdomMedia: string;

  @Column('geometry', { name: 'geom', nullable: true })
  geom: string;

  @Column('varchar', {
    name: 'ope_centro2_equip_id_1',
    nullable: true,
    length: 36,
  })
  opeCentro2EquipId_1: string;

  @Column('varchar', {
    name: 'ope_centro2_equip_id_2',
    nullable: true,
    length: 36,
  })
  opeCentro2EquipId_2: string;

  @Column('varchar', {
    name: 'ope_centro2_pessoa_id',
    nullable: true,
    length: 36,
  })
  opeCentro2PessoaId: string;

  @Column('varchar', {
    name: 'ger_empresa_id',
    nullable: true,
    length: 36,
  })
  gerEmpresaId: string;

  @Column('varchar', {
    name: 'ope_centro2_area_id',
    nullable: true,
    length: 36,
  })
  opeCentro2AreaId: string;

  @Column('geometry', { name: 'geom_circle', nullable: true })
  geomCircle: string;

  @Column('varchar', { name: 'buzzer', nullable: true, length: 4 })
  buzzer: string;

  @Column('varchar', { name: 'unit_id', length: 36 })
  unitId: string;

  @Column('varchar', { name: 'status', nullable: true, length: 2 })
  status: string;

  @Column('timestamp without time zone', {
    name: 'dthr_status',
    nullable: true,
  })
  dthrStatus: Date | null;

  @Column('varchar', {
    name: 'ope_atividade_id',
    nullable: true,
    length: 36,
  })
  opeAtividadeId: string;

  @Column('numeric', {
    name: 'qnt_ha_trab',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  qntHaTrab: string;

  @Column('geometry', { name: 'geom_line', nullable: true })
  geomLine: string;

  @Column('numeric', {
    name: 'duracao',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  duracao: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;
}
