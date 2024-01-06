import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { CrmStatus } from './CrmStatus.entity';
import { BaseEntity } from '../shared/bases/base.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';

@Index('pk_crm_status_prox', ['id'], { unique: true })
@Entity('crm_status_prox', { schema: 'public' })
export class CrmStatusProx extends BaseEntity {
  @Column('smallint', { name: 'ordem', default: () => '0' })
  ordem: number;

  @Column('varchar', {
    name: 'tipo_status_ant',
    nullable: true,
    length: 2,
  })
  tipoStatusAnt: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => CrmStatus, (crmStatus) => crmStatus.crmStatusProxes)
  @JoinColumn([{ name: 'crm_status_id', referencedColumnName: 'id' }])
  crmStatus: CrmStatus;

  @ManyToOne(() => CrmStatus, (crmStatus) => crmStatus.crmStatusProxes2)
  @JoinColumn([{ name: 'crm_status_id_prox', referencedColumnName: 'id' }])
  crmStatusIdProx: CrmStatus;
}
