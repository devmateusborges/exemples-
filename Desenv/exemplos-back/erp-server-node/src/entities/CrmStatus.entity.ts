import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { CrmEtapaProx } from './CrmEtapaProx.entity';
import { CrmMov } from './CrmMov.entity';
import { SystemUnit } from './SystemUnit.entity';
import { CrmStatusProx } from './CrmStatusProx.entity';
import { BaseEntity } from '../shared/bases/base.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';

@Index('pk_crm_status', ['id'], { unique: true })
@Entity('crm_status', { schema: 'public' })
export class CrmStatus extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_status', length: 50 })
  siglaStatus: string;

  @Column('varchar', { name: 'tipo_status', length: 2 })
  tipoStatus: string;

  @Column('varchar', { name: 'obrig_motivo', length: 1 })
  obrigMotivo: string;

  @Column('varchar', { name: 'cor', nullable: true, length: 50 })
  cor: string;

  @Column('varchar', {
    name: 'padrao',
    nullable: true,
    length: 1,
    default: () => "'N'",
  })
  padrao: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => CrmEtapaProx, (crmEtapaProx) => crmEtapaProx.crmStatus)
  crmEtapaProxes: CrmEtapaProx[];

  @OneToMany(() => CrmMov, (crmMov) => crmMov.crmStatus)
  crmMovs: CrmMov[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(() => CrmStatusProx, (crmStatusProx) => crmStatusProx.crmStatus)
  crmStatusProxes: CrmStatusProx[];

  @OneToMany(
    () => CrmStatusProx,
    (crmStatusProx) => crmStatusProx.crmStatusIdProx,
  )
  crmStatusProxes2: CrmStatusProx[];
}
