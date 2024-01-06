import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { CrmAvisoOrg } from './CrmAvisoOrg.entity';
import { CrmMov } from './CrmMov.entity';
import { SystemUnit } from './SystemUnit.entity';
import { SystemUserCrmOrg } from './SystemUserCrmOrg.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_crm_org', ['id'], { unique: true })
@Entity('crm_org', { schema: 'public' })
export class CrmOrg extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_org', length: 50 })
  siglaOrg: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => CrmAvisoOrg, (crmAvisoOrg) => crmAvisoOrg.crmOrg)
  crmAvisoOrgs: CrmAvisoOrg[];

  @OneToMany(() => CrmMov, (crmMov) => crmMov.crmOrg)
  crmMovs: CrmMov[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(
    () => SystemUserCrmOrg,
    (systemUserCrmOrg) => systemUserCrmOrg.crmOrg,
  )
  systemUserCrmOrgs: SystemUserCrmOrg[];
}
