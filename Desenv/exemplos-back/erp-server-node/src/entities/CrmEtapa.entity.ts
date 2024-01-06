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
import { CrmEtapaProx } from './CrmEtapaProx.entity';
import { CrmMov } from './CrmMov.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_crm_etapa', ['id'], { unique: true })
@Entity('crm_etapa', { schema: 'public' })
export class CrmEtapa extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_etapa', length: 50 })
  siglaEtapa: string;

  @Column('varchar', {
    name: 'padrao',
    nullable: true,
    length: 1,
    default: () => "'N'",
  })
  padrao: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(() => CrmEtapaProx, (crmEtapaProx) => crmEtapaProx.crmEtapa)
  crmEtapaProxes: CrmEtapaProx[];

  @OneToMany(() => CrmEtapaProx, (crmEtapaProx) => crmEtapaProx.crmEtapaIdProx)
  crmEtapaProxes2: CrmEtapaProx[];

  @OneToMany(() => CrmMov, (crmMov) => crmMov.crmEtapa)
  crmMovs: CrmMov[];
}
