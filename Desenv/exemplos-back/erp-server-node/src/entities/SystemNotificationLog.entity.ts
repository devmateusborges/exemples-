import { Column, Entity, Index } from 'typeorm';

import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_notification_log', ['id'], { unique: true })
@Entity('system_notification_log', { schema: 'public' })
export class SystemNotificationLog extends BaseEntity {
  @Column('varchar', {
    name: 'system_user_id',
    nullable: false,
    length: 36,
  })
  systemUserId: string;

  @Column('varchar', {
    name: 'system_user_to_id',
    nullable: false,
    length: 36,
  })
  systemUserToId: string;

  @Column('varchar', {
    name: 'email_to',
    nullable: true,
    length: 100,
  })
  email_to: string;

  @Column('text', {
    name: 'email_to',
    nullable: false,
  })
  subject: string;

  @Column('text', {
    name: 'message',
    nullable: false,
  })
  message: string;

  @Column('text', {
    name: 'message',
    nullable: false,
  })
  dt_message: string;

  @Column('varchar', {
    name: 'type_notification',
    nullable: true,
    length: 50,
  })
  typeNotification: string;

  @Column('text', {
    name: 'icon',
    nullable: true,
  })
  icon: string;

  @Column('char', {
    name: 'type_notification',
    length: 1,
    default: () => "'N'",
  })
  checked: string;
  @Column('text', {
    name: 'action_url1',
    nullable: true,
  })
  actionUrl1: string;

  @Column('text', {
    name: 'action_label1',
    nullable: true,
  })
  actionLabel1: string;

  @Column('text', {
    name: 'action_body1',
    nullable: true,
  })
  actionBody1: string;

  @Column('text', {
    name: 'action_header1',
    nullable: true,
  })
  actionHeader1: string;

  @Column('text', {
    name: 'action_type1',
    nullable: true,
  })
  actionType1: string;

  @Column('text', {
    name: 'action_url2',
    nullable: true,
  })
  actionUrl2: string;

  @Column('text', {
    name: 'action_label2',
    nullable: true,
  })
  actionLabel2: string;

  @Column('text', {
    name: 'action_body2',
    nullable: true,
  })
  actionBody2: string;

  @Column('text', {
    name: 'action_header2',
    nullable: true,
  })
  actionHeader2: string;

  @Column('text', {
    name: 'action_type2',
    nullable: true,
  })
  actionType2: string;

  @Column('text', {
    name: 'action_url3',
    nullable: true,
  })
  actionUrl3: string;

  @Column('text', {
    name: 'action_label3',
    nullable: true,
  })
  actionLabel3: string;

  @Column('text', {
    name: 'action_body3',
    nullable: true,
  })
  actionBody3: string;

  @Column('text', {
    name: 'action_header3',
    nullable: true,
  })
  actionHeader3: string;

  @Column('text', {
    name: 'action_type3',
    nullable: true,
  })
  actionType3: string;
}
