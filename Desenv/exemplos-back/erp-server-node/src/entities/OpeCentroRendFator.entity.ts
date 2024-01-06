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
import { OpeCentro2 } from './OpeCentro2.entity';
import { OpeCentroRend } from './OpeCentroRend.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro_rend_fator', ['id'], { unique: true })
@Entity('ope_centro_rend_fator', { schema: 'public' })
export class OpeCentroRendFator extends BaseEntity {
  @Column('numeric', {
    name: 'fator_rend',
    precision: 18,
    scale: 4,
    default: () => '0',
  })
  fatorRend: string;

  @Column('numeric', {
    name: 'fator_util',
    precision: 18,
    scale: 4,
    default: () => '100',
  })
  fatorUtil: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => CtbComp, (ctbComp) => ctbComp.opeCentroRendFators)
  @JoinColumn([{ name: 'ctb_comp_id', referencedColumnName: 'id' }])
  ctbComp: CtbComp;

  @ManyToOne(
    () => GerItemserv,
    (gerItemserv) => gerItemserv.opeCentroRendFators,
  )
  @JoinColumn([{ name: 'ger_itemserv_id', referencedColumnName: 'id' }])
  gerItemserv: GerItemserv;

  @ManyToOne(() => OpeCentro2, (opeCentro2) => opeCentro2.opeCentroRendFators)
  @JoinColumn([{ name: 'ope_centro2_id', referencedColumnName: 'id' }])
  opeCentro2: OpeCentro2;

  @ManyToOne(
    () => OpeCentroRend,
    (opeCentroRend) => opeCentroRend.opeCentroRendFators,
    { onDelete: 'CASCADE', onUpdate: 'CASCADE' },
  )
  @JoinColumn([{ name: 'ope_centro_rend_id', referencedColumnName: 'id' }])
  opeCentroRend: OpeCentroRend;
}
