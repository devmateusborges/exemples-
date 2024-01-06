import { Column, Entity, Index, OneToMany } from 'typeorm';
import { SystemDocumentGroup } from './SystemDocumentGroup.entity';
import { SystemGroupProgram } from './SystemGroupProgram.entity';
import { SystemGroupProgramFeature } from './SystemGroupProgramFeature.entity';
import { SystemUserGroup } from './SystemUserGroup.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_group', ['id'], { unique: true })
@Entity('system_group', { schema: 'public' })
export class SystemGroup extends BaseEntity {
  @Column('varchar', { name: 'name', nullable: true, length: 100 })
  name: string;

  @Column('varchar', { name: 'admin', nullable: true, length: 1 })
  admin: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => SystemDocumentGroup,
    (systemDocumentGroup) => systemDocumentGroup.systemGroup,
  )
  systemDocumentGroups: SystemDocumentGroup[];

  @OneToMany(
    () => SystemGroupProgram,
    (systemGroupProgram) => systemGroupProgram.systemGroup,
  )
  systemGroupPrograms: SystemGroupProgram[];

  @OneToMany(
    () => SystemGroupProgramFeature,
    (systemGroupProgramFeature) => systemGroupProgramFeature.systemGroup,
  )
  systemGroupProgramFeatures: SystemGroupProgramFeature[];

  @OneToMany(
    () => SystemUserGroup,
    (systemUserGroup) => systemUserGroup.systemGroup,
  )
  systemUserGroups: SystemUserGroup[];
}
