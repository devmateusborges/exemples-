import { Column, Entity, Index } from 'typeorm';
import { BaseEntity } from '../shared/bases/base.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';

@Index('idx_bor_mov_atual_04', ['dthrTrack'], {})
@Index('idx_bor_mov_atual_geom', ['geom'], {})
@Index('idx_bor_mov_atual_03', ['ibuttonRfid'], {})
@Index('pk_bor_mov_atual', ['id'], { unique: true })
@Index('idx_bor_mov_atual_01', ['idTipo'], {})
@Index('idx_bor_mov_atual_02', ['numeroSerie'], {})
@Entity('bor_mov_atual', { schema: 'public' })
export class BorMovAtual extends BaseEntity {
  @Column('varchar', { name: 'ope_centro2_equip_id', length: 36 })
  opeCentro2EquipId: string;

  @Column('varchar', { name: 'id_tipo', length: 50 })
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

  @Column('varchar', { name: 'unit_id', nullable: true, length: 36 })
  unitId: string;

  @Column('timestamp without time zone', {
    name: 'dthr_ignicao_last_off',
    nullable: true,
  })
  dthrIgnicaoLastOff: Date | null;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;
}
