import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { Ind } from './Ind.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ind_relac', ['id'], { unique: true })
@Entity('ind_relac', { schema: 'public' })
export class IndRelac extends BaseEntity {
  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => Ind, (ind) => ind.indRelacs)
  @JoinColumn([{ name: 'ind_id', referencedColumnName: 'id' }])
  ind: Ind;

  @ManyToOne(() => Ind, (ind) => ind.indRelacs2)
  @JoinColumn([{ name: 'ind_id_relac', referencedColumnName: 'id' }])
  indIdRelac: Ind;
}
