import { Column, Entity, Index, OneToMany } from 'typeorm';
import { SystemPlanRestriction } from './SystemPlanRestriction.entity';
import { SystemRestrictionLicence } from './SystemRestrictionLicence.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_restriction', ['id'], { unique: true })
@Entity('system_restriction', { schema: 'public' })
export class SystemRestriction extends BaseEntity {
  @Column('varchar', { name: 'name', nullable: true, length: 100 })
  name: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => SystemPlanRestriction,
    (systemPlanRestriction) => systemPlanRestriction.systemRestriction,
  )
  systemPlanRestrictions: SystemPlanRestriction[];

  @OneToMany(
    () => SystemRestrictionLicence,
    (systemRestrictionLicence) => systemRestrictionLicence.systemRestriction,
  )
  systemRestrictionLicences: SystemRestrictionLicence[];
}
