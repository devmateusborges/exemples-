import { Column, Entity, Index, OneToMany } from 'typeorm';
import { SystemLicence } from './SystemLicence.entity';
import { SystemModule } from './SystemModule.entity';
import { SystemParam } from './SystemParam.entity';
import { SystemPlan } from './SystemPlan.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system', ['id'], { unique: true })
@Entity('system', { schema: 'public' })
export class System extends BaseEntity {
  @Column('varchar', { name: 'name', nullable: true, length: 100 })
  name: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => SystemLicence, (systemLicence) => systemLicence.system)
  systemLicences: SystemLicence[];

  @OneToMany(() => SystemModule, (systemModule) => systemModule.system)
  systemModules: SystemModule[];

  @OneToMany(() => SystemParam, (systemParam) => systemParam.system)
  systemParams: SystemParam[];

  @OneToMany(() => SystemPlan, (systemPlan) => systemPlan.system)
  systemPlans: SystemPlan[];
}
