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
import { CrmClassSubgrupo } from './CrmClassSubgrupo.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';
@Index('pk_crm_class_gupo', ['id'], { unique: true })
@Entity('crm_class_grupo', { schema: 'public' })
export class CrmClassGrupo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_class_grupo', length: 50 })
  siglaClassGrupo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(
    () => CrmClassSubgrupo,
    (crmClassSubgrupo) => crmClassSubgrupo.crmClassGrupo,
  )
  crmClassSubgrupos: CrmClassSubgrupo[];
}
