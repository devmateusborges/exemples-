import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { SystemGroupProgram } from './SystemGroupProgram.entity';
import { SystemGroupProgramFeature } from './SystemGroupProgramFeature.entity';
import { SystemModule } from './SystemModule.entity';
import { SystemProgramFavorite } from './SystemProgramFavorite.entity';
import { SystemProgramFeature } from './SystemProgramFeature.entity';
import { SystemUserProgram } from './SystemUserProgram.entity';
import { SystemUserProgramFeature } from './SystemUserProgramFeature.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('unq_system_param', ['controller'], { unique: true })
@Index('pk_system_program', ['id'], { unique: true })
@Entity('system_program', { schema: 'public' })
export class SystemProgram extends BaseEntity {
  @Column('varchar', { name: 'name', length: 100 })
  name: string;

  @Column('varchar', {
    name: 'controller',
    unique: true,
    length: 100,
  })
  controller: string;

  @Column('varchar', { name: 'menu', length: 1 })
  menu: string;

  @Column('varchar', { name: 'type_program', length: 1 })
  typeProgram: string;

  @Column('varchar', { name: 'icon', nullable: true, length: 50 })
  icon: string;

  @Column('varchar', { name: 'admin', length: 1 })
  admin: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => SystemGroupProgram,
    (systemGroupProgram) => systemGroupProgram.systemProgram,
  )
  systemGroupPrograms: SystemGroupProgram[];

  @OneToMany(
    () => SystemGroupProgramFeature,
    (systemGroupProgramFeature) => systemGroupProgramFeature.systemProgram,
  )
  systemGroupProgramFeatures: SystemGroupProgramFeature[];

  @ManyToOne(() => SystemModule, (systemModule) => systemModule.systemPrograms)
  @JoinColumn([{ name: 'module_id', referencedColumnName: 'id' }])
  module: SystemModule;

  @OneToMany(
    () => SystemProgramFavorite,
    (systemProgramFavorite) => systemProgramFavorite.systemProgram,
  )
  systemProgramFavorites: SystemProgramFavorite[];

  @OneToMany(
    () => SystemProgramFeature,
    (systemProgramFeature) => systemProgramFeature.systemProgram,
  )
  systemProgramFeatures: SystemProgramFeature[];

  @OneToMany(
    () => SystemUserProgram,
    (systemUserProgram) => systemUserProgram.systemProgram,
  )
  systemUserPrograms: SystemUserProgram[];

  @OneToMany(
    () => SystemUserProgramFeature,
    (systemUserProgramFeature) => systemUserProgramFeature.systemProgram,
  )
  systemUserProgramFeatures: SystemUserProgramFeature[];
}
