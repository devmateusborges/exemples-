import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { Mov } from './Mov.entity';
import { OpeCentro2Equip } from './OpeCentro2Equip.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_mov_reboque', ['id'], { unique: true })
@Entity('mov_reboque', { schema: 'public' })
export class MovReboque extends BaseEntity {
  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => Mov, (mov) => mov.movReboques)
  @JoinColumn([{ name: 'mov_id', referencedColumnName: 'id' }])
  mov: Mov;

  @ManyToOne(
    () => OpeCentro2Equip,
    (opeCentro2Equip) => opeCentro2Equip.movReboques,
  )
  @JoinColumn([{ name: 'ope_centro2_id_equip', referencedColumnName: 'id' }])
  opeCentro2IdEquip: OpeCentro2Equip;
}
