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
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_mov_comp', ['id'], { unique: true })
@Entity('mov_comp', { schema: 'public' })
export class MovComp extends BaseEntity {
  @Column('varchar', { name: 'nome_comp', length: 50 })
  nomeComp: string;

  @Column('numeric', { name: 'qnt_comp', precision: 18, scale: 6 })
  qntComp: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => Mov, (mov) => mov.movComps)
  @JoinColumn([{ name: 'mov_id', referencedColumnName: 'id' }])
  mov: Mov;
}
