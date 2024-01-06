import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { CrmAviso } from './CrmAviso.entity';
import { CrmOrg } from './CrmOrg.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_crm_aviso_org', ['id'], { unique: true })
@Entity('crm_aviso_org', { schema: 'public' })
export class CrmAvisoOrg extends BaseEntity {
  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => CrmAviso, (crmAviso) => crmAviso.crmAvisoOrgs)
  @JoinColumn([{ name: 'crm_aviso_id', referencedColumnName: 'id' }])
  crmAviso: CrmAviso;

  @ManyToOne(() => CrmOrg, (crmOrg) => crmOrg.crmAvisoOrgs)
  @JoinColumn([{ name: 'crm_org_id', referencedColumnName: 'id' }])
  crmOrg: CrmOrg;
}
