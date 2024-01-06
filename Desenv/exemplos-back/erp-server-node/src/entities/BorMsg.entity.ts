import { Column, Entity, Index } from 'typeorm';
import { BaseEntity } from '../shared/bases/base.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';

@Index('pk_bor_msg', ['id'], { unique: true })
@Entity('bor_msg', { schema: 'public' })
export class BorMsg extends BaseEntity {
  @Column('varchar', { name: 'id_tipo', length: 50 })
  idTipo: string;

  @Column('varchar', { name: 'numero_serie', length: 50 })
  numeroSerie: string;

  @Column('timestamp without time zone', { name: 'dthr_trans_msg_rast' })
  dthrTransMsgRast: Date;

  @Column('timestamp without time zone', { name: 'dthr_msg_gerada' })
  dthrMsgGerada: Date;

  @Column('varchar', { name: 'grupo_msg', length: 30 })
  grupoMsg: string;

  @Column('varchar', { name: 'index_msg', length: 30 })
  indexMsg: string;

  @Column('timestamp without time zone', { name: 'dthr_posicao' })
  dthrPosicao: Date;

  @Column('varchar', { name: 'latitude', length: 50 })
  latitude: string;

  @Column('varchar', { name: 'longitude', length: 50 })
  longitude: string;

  @Column('varchar', { name: 'qualidade_posi', length: 10 })
  qualidadePosi: string;

  @Column('varchar', { name: 'valor_msg', length: 100 })
  valorMsg: string;

  @Column('varchar', {
    name: 'status_msg',
    nullable: true,
    length: 50,
    default: () => "'NP'",
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
    name: 'ope_centro2_equip_id_1',
    nullable: true,
    length: 50,
  })
  opeCentro2EquipId_1: string;

  @Column('varchar', { name: 'unit_id', length: 36 })
  unitId: string;

  @Column('varchar', {
    name: 'corpo_msg',
    nullable: true,
    length: 250,
  })
  corpoMsg: string;

  @Column('varchar', {
    name: 'ope_atividade_id',
    nullable: true,
    length: 36,
  })
  opeAtividadeId: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;
}
