import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUser } from './SystemUser.entity';
import { SystemUnit } from './SystemUnit.entity';
import { CrmOrg } from './CrmOrg.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('system_user_crm_org_pkey', ['id'], { unique: true })
@Entity('system_user_crm_org', { schema: 'public' })
export class SystemUserCrmOrg extends BaseEntity {
  @Column('varchar', { name: 'padrao', nullable: true, length: 1 })
  padrao: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUser)
  @JoinColumn([{ name: 'system_user_id', referencedColumnName: 'id' }])
  systemUser: SystemUser;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => CrmOrg, (crmOrg) => crmOrg.systemUserCrmOrgs)
  @JoinColumn([{ name: 'crm_org_id', referencedColumnName: 'id' }])
  crmOrg: CrmOrg;
}
