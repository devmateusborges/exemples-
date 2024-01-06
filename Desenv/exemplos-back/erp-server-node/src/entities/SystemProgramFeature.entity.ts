import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemProgram } from './SystemProgram.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('system_program_feature_pkey', ['id'], { unique: true })
@Entity('system_program_feature', { schema: 'public' })
export class SystemProgramFeature extends BaseEntity {
  @Column('varchar', { name: 'feature_code', length: 200 })
  featureCode: string;

  @Column('text', { name: 'feature_description', nullable: true })
  featureDescription: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(
    () => SystemProgram,
    (systemProgram) => systemProgram.systemProgramFeatures,
    { onDelete: 'CASCADE' },
  )
  @JoinColumn([{ name: 'system_program_id', referencedColumnName: 'id' }])
  systemProgram: SystemProgram;
}
