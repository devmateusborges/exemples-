import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { System } from './System.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_param', ['id'], { unique: true })
@Index('idx_system_param', ['paramkey', 'systemId'], {})
@Entity('system_param', { schema: 'public' })
export class SystemParam extends BaseEntity {
  @Column('varchar', { name: 'type', length: 250 })
  type: string;

  @Column('varchar', { name: 'system_id', length: 36 })
  systemId: string;

  @Column('varchar', { name: 'paramkey', length: 255 })
  paramkey: string;

  @Column('text', { name: 'paramvalue' })
  paramvalue: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => System, (system) => system.systemParams)
  @JoinColumn([{ name: 'system_id', referencedColumnName: 'id' }])
  system: System;
}
