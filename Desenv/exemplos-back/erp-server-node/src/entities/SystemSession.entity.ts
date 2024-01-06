import { Column, Entity, Index } from 'typeorm';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('system_session_pkey', ['id'], { unique: true })
@Index('system_session_notification_id_key', ['notificationId'], {
  unique: true,
})
@Entity('system_session', { schema: 'public' })
export class SystemSession extends BaseEntity {
  @Column('varchar', {
    name: 'notification_id',
    unique: true,
    length: 256,
  })
  notificationId: string;

  @Column('varchar', {
    name: 'system_user_id',
    nullable: true,
    length: 36,
  })
  systemUserId: string;

  @Column('varchar', {
    name: 'system_id',
    nullable: true,
    length: 36,
  })
  systemId: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;
}
