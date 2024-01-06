import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { System } from './System.entity';
import { SystemProgram } from './SystemProgram.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_module', ['id'], { unique: true })
@Entity('system_module', { schema: 'public' })
export class SystemModule extends BaseEntity {
  @Column('varchar', { name: 'name', length: 100 })
  name: string;

  @Column('varchar', { name: 'sigla_module', length: 50 })
  siglaModule: string;

  @Column('varchar', { name: 'icon', length: 50 })
  icon: string;

  @Column('varchar', { name: 'color', length: 50 })
  color: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => System, (system) => system.systemModules)
  @JoinColumn([{ name: 'system_id', referencedColumnName: 'id' }])
  system: System;

  @OneToMany(() => SystemProgram, (systemProgram) => systemProgram.module)
  systemPrograms: SystemProgram[];
}
