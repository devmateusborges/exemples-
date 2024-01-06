import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { CrmClass } from './CrmClass.entity';
import { SystemUnit } from './SystemUnit.entity';
import { CrmClassGrupo } from './CrmClassGrupo.entity';
import { BaseEntity } from '../shared/bases/base.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';

@Index('pk_crm_class_subgupo', ['id'], { unique: true })
@Entity('crm_class_subgrupo', { schema: 'public' })
export class CrmClassSubgrupo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_class_subgrupo', length: 50 })
  siglaClassSubgrupo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => CrmClass, (crmClass) => crmClass.crmClassSubgrupo)
  crmClasses: CrmClass[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => CrmClassGrupo,
    (crmClassGrupo) => crmClassGrupo.crmClassSubgrupos,
  )
  @JoinColumn([{ name: 'crm_class_grupo_id', referencedColumnName: 'id' }])
  crmClassGrupo: CrmClassGrupo;
}
