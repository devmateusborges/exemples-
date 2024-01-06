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
import { OpeCentro2OrdAtiv } from './OpeCentro2OrdAtiv.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro2_ord_itemserv', ['id'], { unique: true })
@Entity('ope_centro2_ord_itemserv', { schema: 'public' })
export class OpeCentro2OrdItemserv extends BaseEntity {
  @Column('varchar', {
    name: 'observacao_interna',
    nullable: true,
    length: 250,
  })
  observacaoInterna: string;

  @Column('varchar', {
    name: 'observacao_externa',
    nullable: true,
    length: 250,
  })
  observacaoExterna: string;

  @Column('numeric', {
    name: 'qnt_rend',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  qntRend: string;

  @Column('numeric', {
    name: 'perc_util',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  percUtil: string;

  @Column('numeric', {
    name: 'qnt_total_util',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  qntTotalUtil: string;

  @Column('numeric', {
    name: 'valor_unit_util',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorUnitUtil: string;

  @Column('numeric', {
    name: 'valor_total_util',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorTotalUtil: string;

  @Column('date', { name: 'data_valid', nullable: true })
  dataValid: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => CtbComp, (ctbComp) => ctbComp.opeCentro2OrdItemservs)
  @JoinColumn([{ name: 'ctb_comp_id', referencedColumnName: 'id' }])
  ctbComp: CtbComp;

  @ManyToOne(
    () => GerItemserv,
    (gerItemserv) => gerItemserv.opeCentro2OrdItemservs,
  )
  @JoinColumn([{ name: 'ger_itemserv_id', referencedColumnName: 'id' }])
  gerItemserv: GerItemserv;

  @ManyToOne(
    () => OpeCentro2OrdAtiv,
    (opeCentro2OrdAtiv) => opeCentro2OrdAtiv.opeCentro2OrdItemservs,
  )
  @JoinColumn([{ name: 'ope_centro2_ord_ativ_id', referencedColumnName: 'id' }])
  opeCentro2OrdAtiv: OpeCentro2OrdAtiv;
}
