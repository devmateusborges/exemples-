import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { BaseEntity } from '../shared/bases/base.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';

@Index('pk_bov_unit_param', ['id'], { unique: true })
@Entity('bov_unit_param', { schema: 'public' })
export class BovUnitParam extends BaseEntity {
  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'system_unit_id', referencedColumnName: 'id' }])
  systemUnit: SystemUnit;
}
