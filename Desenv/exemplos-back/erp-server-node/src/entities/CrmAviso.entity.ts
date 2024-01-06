import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { CrmAvisoOrg } from './CrmAvisoOrg.entity';
import { BaseEntity } from '../shared/bases/base.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';

@Index('pk_crm_aviso', ['id'], { unique: true })
@Entity('crm_aviso', { schema: 'public' })
export class CrmAviso extends BaseEntity {
  @Column('text', { name: 'descritivo' })
  descritivo: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_aviso', length: 50 })
  siglaAviso: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(() => CrmAvisoOrg, (crmAvisoOrg) => crmAvisoOrg.crmAviso)
  crmAvisoOrgs: CrmAvisoOrg[];
}
