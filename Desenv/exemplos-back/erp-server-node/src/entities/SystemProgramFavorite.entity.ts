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

@Index('pk_system_program_favorite', ['id'], { unique: true })
@Index('idx_sys_program_favorite_program', ['systemProgramId'], {})
@Index('idx_sys_program_favorite_user', ['systemUserId'], {})
@Entity('system_program_favorite', { schema: 'public' })
export class SystemProgramFavorite extends BaseEntity {
  @Column('varchar', {
    name: 'system_user_id',
    nullable: true,
    length: 36,
  })
  systemUserId: string;

  @Column('varchar', {
    name: 'system_program_id',
    nullable: true,
    length: 36,
  })
  systemProgramId: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(
    () => SystemProgram,
    (systemProgram) => systemProgram.systemProgramFavorites,
  )
  @JoinColumn([{ name: 'system_program_id', referencedColumnName: 'id' }])
  systemProgram: SystemProgram;

  @OneToOne(() => SystemUser)
  @JoinColumn([{ name: 'system_user_id', referencedColumnName: 'id' }])
  systemUser: SystemUser;
}
