import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemGroup } from './SystemGroup.entity';
import { SystemProgram } from './SystemProgram.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('system_group_program_feature_pkey', ['id'], { unique: true })
@Entity('system_group_program_feature', { schema: 'public' })
export class SystemGroupProgramFeature extends BaseEntity {
  @Column('varchar', { name: 'feature_code', length: 200 })
  featureCode: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(
    () => SystemGroup,
    (systemGroup) => systemGroup.systemGroupProgramFeatures,
  )
  @JoinColumn([{ name: 'system_group_id', referencedColumnName: 'id' }])
  systemGroup: SystemGroup;

  @ManyToOne(
    () => SystemProgram,
    (systemProgram) => systemProgram.systemGroupProgramFeatures,
    { onDelete: 'CASCADE' },
  )
  @JoinColumn([{ name: 'system_program_id', referencedColumnName: 'id' }])
  systemProgram: SystemProgram;
}
