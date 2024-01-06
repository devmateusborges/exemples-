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

@Index('pk_mov_lacre', ['id'], { unique: true })
@Entity('mov_lacre', { schema: 'public' })
export class MovLacre extends BaseEntity {
  @Column('varchar', { name: 'lacres', nullable: true, length: 250 })
  lacres: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => Mov, (mov) => mov.movLacres)
  @JoinColumn([{ name: 'mov_id', referencedColumnName: 'id' }])
  mov: Mov;
}
