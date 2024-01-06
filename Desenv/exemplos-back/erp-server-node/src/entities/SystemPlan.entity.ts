import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToMany,
} from 'typeorm';
import { SystemLicence } from './SystemLicence.entity';
import { System } from './System.entity';
import { SystemPlanRestriction } from './SystemPlanRestriction.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_plan', ['id'], { unique: true })
@Entity('system_plan', { schema: 'public' })
export class SystemPlan extends BaseEntity {
  @Column('varchar', { name: 'name', nullable: true, length: 100 })
  name: string;

  @Column('varchar', { name: 'type_plan', length: 2 })
  typePlan: string;

  @Column('text', { name: 'description' })
  description: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => SystemLicence, (systemLicence) => systemLicence.systemPlan)
  systemLicences: SystemLicence[];

  @ManyToOne(() => System, (system) => system.systemPlans)
  @JoinColumn([{ name: 'system_id', referencedColumnName: 'id' }])
  system: System;

  @OneToMany(
    () => SystemPlanRestriction,
    (systemPlanRestriction) => systemPlanRestriction.systemPlan,
  )
  systemPlanRestrictions: SystemPlanRestriction[];
}
