import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemLicence } from './SystemLicence.entity';
import { SystemRestriction } from './SystemRestriction.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_restriction_licence', ['id'], { unique: true })
@Entity('system_restriction_licence', { schema: 'public' })
export class SystemRestrictionLicence extends BaseEntity {
  @Column('integer', { name: 'value_restriction' })
  valueRestriction: number;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(
    () => SystemLicence,
    (systemLicence) => systemLicence.systemRestrictionLicences,
    { onDelete: 'CASCADE' },
  )
  @JoinColumn([{ name: 'system_licence_id', referencedColumnName: 'id' }])
  systemLicence: SystemLicence;

  @ManyToOne(
    () => SystemRestriction,
    (systemRestriction) => systemRestriction.systemRestrictionLicences,
  )
  @JoinColumn([{ name: 'system_restriction_id', referencedColumnName: 'id' }])
  systemRestriction: SystemRestriction;
}
