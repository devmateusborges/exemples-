import { Entity, Column, PrimaryGeneratedColumn, JoinColumn } from 'typeorm';
import { LogColumn } from './log-column';
import { BaseEntity } from '@shared/base.entity';

@Entity({ name: 'tenant' })
export class Tenant extends BaseEntity {
  @PrimaryGeneratedColumn('uuid', { name: 'id', comment: 'ID Tenant' })
  id: string;

  @Column('varchar', { name: 'name', length: 50, comment: 'Name' })
  name: string;

  @Column('varchar', { name: 'active', length: 1, comment: 'Active' })
  active: string;

  @Column(type => LogColumn)
  log: LogColumn;
}
