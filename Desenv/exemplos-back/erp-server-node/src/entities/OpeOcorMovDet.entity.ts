import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { OpeOcor } from './OpeOcor.entity';
import { OpeOcorMovDest } from './OpeOcorMovDest.entity';
import { OpeOcorMov } from './OpeOcorMov.entity';
import { OpeOcorStatus } from './OpeOcorStatus.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_ocor_mov_det', ['id'], { unique: true })
@Entity('ope_ocor_mov_det', { schema: 'public' })
export class OpeOcorMovDet extends BaseEntity {
  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column('numeric', {
    name: 'qnt_ocor',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  qntOcor: string;

  @Column('numeric', {
    name: 'qnt_ocor_calc',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  qntOcorCalc: string;

  @Column('date', { name: 'data_status' })
  dataStatus: string;

  @Column('varchar', { name: 'lat_x', nullable: true, length: 50 })
  latX: string;

  @Column('varchar', { name: 'long_y', nullable: true, length: 50 })
  longY: string;

  @Column('varchar', { name: 'ponto', nullable: true, length: 50 })
  ponto: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => OpeOcor, (opeOcor) => opeOcor.opeOcorMovDets)
  @JoinColumn([{ name: 'ope_ocor_id', referencedColumnName: 'id' }])
  opeOcor: OpeOcor;

  @ManyToOne(
    () => OpeOcorMovDest,
    (opeOcorMovDest) => opeOcorMovDest.opeOcorMovDets,
  )
  @JoinColumn([{ name: 'ope_ocor_mov_dest_id', referencedColumnName: 'id' }])
  opeOcorMovDest: OpeOcorMovDest;

  @ManyToOne(() => OpeOcorMov, (opeOcorMov) => opeOcorMov.opeOcorMovDets, {
    onDelete: 'CASCADE',
    onUpdate: 'CASCADE',
  })
  @JoinColumn([{ name: 'ope_ocor_mov_id', referencedColumnName: 'id' }])
  opeOcorMov: OpeOcorMov;

  @ManyToOne(
    () => OpeOcorStatus,
    (opeOcorStatus) => opeOcorStatus.opeOcorMovDets,
  )
  @JoinColumn([{ name: 'ope_ocor_status_id', referencedColumnName: 'id' }])
  opeOcorStatus: OpeOcorStatus;
}
