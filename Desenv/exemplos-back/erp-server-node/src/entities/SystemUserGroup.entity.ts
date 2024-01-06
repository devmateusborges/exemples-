import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemGroup } from './SystemGroup.entity';
import { SystemUser } from './SystemUser.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_user_group', ['id'], { unique: true })
@Index('idx_system_user_group_group', ['systemGroupId'], {})
@Index('idx_system_user_group_user', ['systemUserId'], {})
@Entity('system_user_group', { schema: 'public' })
export class SystemUserGroup extends BaseEntity {
  @Column('varchar', {
    name: 'system_user_id',
    nullable: true,
    length: 36,
  })
  systemUserId: string;

  @Column('varchar', {
    name: 'system_group_id',
    nullable: true,
    length: 36,
  })
  systemGroupId: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => SystemGroup, (systemGroup) => systemGroup.systemUserGroups)
  @JoinColumn([{ name: 'system_group_id', referencedColumnName: 'id' }])
  systemGroup: SystemGroup;

  @OneToOne(() => SystemUser)
  @JoinColumn([{ name: 'system_user_id', referencedColumnName: 'id' }])
  systemUser: SystemUser;
}
