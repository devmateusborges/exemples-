import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_unit_param', ['id'], { unique: true })
@Entity('ger_unit_param', { schema: 'public' })
export class GerUnitParam extends BaseEntity {
  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'system_unit_id', referencedColumnName: 'id' }])
  systemUnit: SystemUnit;
}
