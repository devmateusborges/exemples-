import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { GerItemservVar } from './GerItemservVar.entity';
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_ciclo_var', ['id'], { unique: true })
@Entity('ope_ciclo_var', { schema: 'public' })
export class OpeCicloVar extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', {
    name: 'sigla_ope_ciclo_var',
    nullable: true,
    length: 50,
  })
  siglaOpeCicloVar: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => GerItemservVar,
    (gerItemservVar) => gerItemservVar.opeCicloVar,
  )
  gerItemservVars: GerItemservVar[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
