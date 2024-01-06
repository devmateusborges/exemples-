import { Column, CreateDateColumn, UpdateDateColumn } from 'typeorm';

export class LogColumn {
  @Column('varchar', { name: '_user_ins', nullable: true, comment: 'Log User Insert' })
  userins: string;

  @CreateDateColumn({
    type: 'timestamp',
    name: '_date_ins',
    default: () => 'current_timestamp',
    comment: 'Log Date Insert',
  })
  dateins: Date;

  @Column('varchar', { name: '_user_upd', nullable: true, comment: 'Log User Update' })
  userupd: string;

  @UpdateDateColumn({
    type: 'timestamp',
    name: '_date_upd',
    default: () => 'current_timestamp',
    comment: 'Log Date Update',
  })
  dateupd: Date;
}
