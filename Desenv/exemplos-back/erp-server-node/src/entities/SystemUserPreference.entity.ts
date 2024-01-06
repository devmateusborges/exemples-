import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUser } from './SystemUser.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_user_preference', ['id'], { unique: true })
@Entity('system_user_preference', { schema: 'public' })
export class SystemUserPreference extends BaseEntity {
  @Column('text', { name: 'value', nullable: true })
  value: string;

  @Column('varchar', { name: 'object_type', length: 36 })
  objectType: string;

  @Column('varchar', { name: 'object_id', length: 36 })
  objectId: string;

  @Column('varchar', { name: 'preference_description', length: 150 })
  preferenceDescription: string;

  @Column('varchar', { name: 'defaultd', nullable: true, length: 1 })
  defaultd: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUser)
  @JoinColumn([{ name: 'system_user_id', referencedColumnName: 'id' }])
  systemUser: SystemUser;
}
