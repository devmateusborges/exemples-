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
import { MovItemserv } from './MovItemserv.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_mov_origem', ['id'], { unique: true })
@Entity('mov_origem', { schema: 'public' })
export class MovOrigem extends BaseEntity {
  @Column('varchar', { name: 'tipo', nullable: true, length: 50 })
  tipo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => Mov, (mov) => mov.movOrigems)
  @JoinColumn([{ name: 'mov_id', referencedColumnName: 'id' }])
  mov: Mov;

  @ManyToOne(() => Mov, (mov) => mov.movOrigems2)
  @JoinColumn([{ name: 'mov_id_origem', referencedColumnName: 'id' }])
  movIdOrigem: Mov;

  @ManyToOne(() => MovItemserv, (movItemserv) => movItemserv.movOrigems)
  @JoinColumn([{ name: 'mov_itemserv_id', referencedColumnName: 'id' }])
  movItemserv: MovItemserv;

  @ManyToOne(() => MovItemserv, (movItemserv) => movItemserv.movOrigems2)
  @JoinColumn([{ name: 'mov_itemserv_id_origem', referencedColumnName: 'id' }])
  movItemservIdOrigem: MovItemserv;
}
