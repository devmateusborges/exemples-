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

@Index('system_group_program_pkey', ['id'], { unique: true })
@Index('idx_system_group_program_group', ['systemGroupId'], {})
@Index('idx_system_group_program_program', ['systemProgramId'], {})
@Entity('system_group_program', { schema: 'public' })
export class SystemGroupProgram extends BaseEntity {
  @Column('varchar', {
    name: 'system_group_id',
    nullable: true,
    length: 36,
  })
  systemGroupId: string;

  @Column('varchar', {
    name: 'system_program_id',
    nullable: true,
    length: 36,
  })
  systemProgramId: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(
    () => SystemGroup,
    (systemGroup) => systemGroup.systemGroupPrograms,
  )
  @JoinColumn([{ name: 'system_group_id', referencedColumnName: 'id' }])
  systemGroup: SystemGroup;

  @ManyToOne(
    () => SystemProgram,
    (systemProgram) => systemProgram.systemGroupPrograms,
    { onDelete: 'CASCADE' },
  )
  @JoinColumn([{ name: 'system_program_id', referencedColumnName: 'id' }])
  systemProgram: SystemProgram;
}
