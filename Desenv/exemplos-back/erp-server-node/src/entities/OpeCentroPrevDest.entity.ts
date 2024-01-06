import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { CtbComp } from './CtbComp.entity';
import { GerItemserv } from './GerItemserv.entity';
import { OpeCentro1 } from './OpeCentro1.entity';
import { OpeCentro2 } from './OpeCentro2.entity';
import { OpeCentroPrev } from './OpeCentroPrev.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro_prev_dest', ['id'], { unique: true })
@Entity('ope_centro_prev_dest', { schema: 'public' })
export class OpeCentroPrevDest extends BaseEntity {
  @Column('varchar', { name: 'tipo_prev', length: 1 })
  tipoPrev: string;

  @Column('numeric', {
    name: 'qnt01',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt01: string;

  @Column('numeric', {
    name: 'qnt02',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt02: string;

  @Column('numeric', {
    name: 'qnt03',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt03: string;

  @Column('numeric', {
    name: 'qnt04',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt04: string;

  @Column('numeric', {
    name: 'qnt05',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt05: string;

  @Column('numeric', {
    name: 'qnt06',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt06: string;

  @Column('numeric', {
    name: 'qnt07',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt07: string;

  @Column('numeric', {
    name: 'qnt08',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt08: string;

  @Column('numeric', {
    name: 'qnt09',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt09: string;

  @Column('numeric', {
    name: 'qnt10',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt10: string;

  @Column('numeric', {
    name: 'qnt11',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt11: string;

  @Column('numeric', {
    name: 'qnt12',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt12: string;

  @Column('numeric', {
    name: 'qnt13',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt13: string;

  @Column('numeric', {
    name: 'qnt14',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt14: string;

  @Column('numeric', {
    name: 'qnt15',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt15: string;

  @Column('numeric', {
    name: 'qnt16',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt16: string;

  @Column('numeric', {
    name: 'qnt17',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt17: string;

  @Column('numeric', {
    name: 'qnt18',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt18: string;

  @Column('numeric', {
    name: 'qnt19',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt19: string;

  @Column('numeric', {
    name: 'qnt20',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt20: string;

  @Column('numeric', {
    name: 'qnt21',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt21: string;

  @Column('numeric', {
    name: 'qnt22',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt22: string;

  @Column('numeric', {
    name: 'qnt23',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt23: string;

  @Column('numeric', {
    name: 'qnt24',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt24: string;

  @Column('numeric', {
    name: 'qnt25',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt25: string;

  @Column('numeric', {
    name: 'qnt26',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt26: string;

  @Column('numeric', {
    name: 'qnt27',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt27: string;

  @Column('numeric', {
    name: 'qnt28',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt28: string;

  @Column('numeric', {
    name: 'qnt29',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt29: string;

  @Column('numeric', {
    name: 'qnt30',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt30: string;

  @Column('numeric', {
    name: 'qnt31',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  qnt31: string;

  @Column('varchar', {
    name: 'process_id',
    nullable: true,
    length: 36,
  })
  processId: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => CtbComp, (ctbComp) => ctbComp.opeCentroPrevDests)
  @JoinColumn([{ name: 'ctb_comp_id', referencedColumnName: 'id' }])
  ctbComp: CtbComp;

  @ManyToOne(() => GerItemserv, (gerItemserv) => gerItemserv.opeCentroPrevDests)
  @JoinColumn([{ name: 'ger_itemserv_id', referencedColumnName: 'id' }])
  gerItemserv: GerItemserv;

  @ManyToOne(() => OpeCentro1, (opeCentro1) => opeCentro1.opeCentroPrevDests)
  @JoinColumn([{ name: 'ope_centro1_id', referencedColumnName: 'id' }])
  opeCentro1: OpeCentro1;

  @ManyToOne(() => OpeCentro2, (opeCentro2) => opeCentro2.opeCentroPrevDests)
  @JoinColumn([{ name: 'ope_centro2_id', referencedColumnName: 'id' }])
  opeCentro2: OpeCentro2;

  @ManyToOne(
    () => OpeCentroPrev,
    (opeCentroPrev) => opeCentroPrev.opeCentroPrevDests,
    { onDelete: 'CASCADE' },
  )
  @JoinColumn([{ name: 'ope_centro_prev_id', referencedColumnName: 'id' }])
  opeCentroPrev: OpeCentroPrev;
}
