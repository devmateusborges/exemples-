import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemPlan } from './SystemPlan.entity';
import { SystemRestriction } from './SystemRestriction.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_plan_restriction', ['id'], { unique: true })
@Entity('system_plan_restriction', { schema: 'public' })
export class SystemPlanRestriction extends BaseEntity {
  @Column('integer', { name: 'value_restriction', default: () => '1' })
  valueRestriction: number;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(
    () => SystemPlan,
    (systemPlan) => systemPlan.systemPlanRestrictions,
  )
  @JoinColumn([{ name: 'system_plan_id', referencedColumnName: 'id' }])
  systemPlan: SystemPlan;

  @ManyToOne(
    () => SystemRestriction,
    (systemRestriction) => systemRestriction.systemPlanRestrictions,
  )
  @JoinColumn([{ name: 'system_restriction_id', referencedColumnName: 'id' }])
  systemRestriction: SystemRestriction;
}
