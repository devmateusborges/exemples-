import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemProgram } from './SystemProgram.entity';
import { SystemUser } from './SystemUser.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('system_user_program_feature_pkey', ['id'], { unique: true })
@Entity('system_user_program_feature', { schema: 'public' })
export class SystemUserProgramFeature extends BaseEntity {
  @Column('varchar', { name: 'feature_code', length: 200 })
  featureCode: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(
    () => SystemProgram,
    (systemProgram) => systemProgram.systemUserProgramFeatures,
  )
  @JoinColumn([{ name: 'system_program_id', referencedColumnName: 'id' }])
  systemProgram: SystemProgram;

  @OneToOne(() => SystemUser)
  @JoinColumn([{ name: 'system_user_id', referencedColumnName: 'id' }])
  systemUser: SystemUser;
}
