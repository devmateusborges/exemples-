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
import { CrmMov } from './CrmMov.entity';
import { SystemUserCrmClass } from './SystemUserCrmClass.entity';
import { BaseEntity } from '../shared/bases/base.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';

@Index('pk_crm_class', ['id'], { unique: true })
@Entity('crm_class', { schema: 'public' })
export class CrmClass extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_class', length: 50 })
  siglaClass: string;

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

  @ManyToOne(
    () => CrmClassSubgrupo,
    (crmClassSubgrupo) => crmClassSubgrupo.crmClasses,
  )
  @JoinColumn([{ name: 'crm_class_subgrupo_id', referencedColumnName: 'id' }])
  crmClassSubgrupo: CrmClassSubgrupo;

  @OneToMany(() => CrmMov, (crmMov) => crmMov.crmClass)
  crmMovs: CrmMov[];

  @OneToMany(
    () => SystemUserCrmClass,
    (systemUserCrmClass) => systemUserCrmClass.crmClass,
  )
  systemUserCrmClasses: SystemUserCrmClass[];
}
