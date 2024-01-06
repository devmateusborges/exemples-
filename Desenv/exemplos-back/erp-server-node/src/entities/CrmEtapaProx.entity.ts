import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { CrmEtapa } from './CrmEtapa.entity';
import { CrmStatus } from './CrmStatus.entity';
import { BaseEntity } from '../shared/bases/base.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';

@Index('pk_crm_etapa_prox', ['id'], { unique: true })
@Entity('crm_etapa_prox', { schema: 'public' })
export class CrmEtapaProx extends BaseEntity {
  @Column('smallint', { name: 'ordem', default: () => '0' })
  ordem: number;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => CrmEtapa, (crmEtapa) => crmEtapa.crmEtapaProxes)
  @JoinColumn([{ name: 'crm_etapa_id', referencedColumnName: 'id' }])
  crmEtapa: CrmEtapa;

  @ManyToOne(() => CrmEtapa, (crmEtapa) => crmEtapa.crmEtapaProxes2)
  @JoinColumn([{ name: 'crm_etapa_id_prox', referencedColumnName: 'id' }])
  crmEtapaIdProx: CrmEtapa;

  @ManyToOne(() => CrmStatus, (crmStatus) => crmStatus.crmEtapaProxes)
  @JoinColumn([{ name: 'crm_status_id', referencedColumnName: 'id' }])
  crmStatus: CrmStatus;
}
