import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { CrmMov } from './CrmMov.entity';
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_crm_prioridade', ['id'], { unique: true })
@Entity('crm_prioridade', { schema: 'public' })
export class CrmPrioridade extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_prioridade', length: 50 })
  siglaPrioridade: string;

  @Column('varchar', { name: 'padrao', nullable: true, length: 1 })
  padrao: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => CrmMov, (crmMov) => crmMov.crmPrioridade)
  crmMovs: CrmMov[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
