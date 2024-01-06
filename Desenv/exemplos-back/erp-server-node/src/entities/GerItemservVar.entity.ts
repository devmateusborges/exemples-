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
import { OpeCicloVar } from './OpeCicloVar.entity';
import { MovItemserv } from './MovItemserv.entity';
import { OpeCentro2Area } from './OpeCentro2Area.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_itemserv_var', ['id'], { unique: true })
@Entity('ger_itemserv_var', { schema: 'public' })
export class GerItemservVar extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', {
    name: 'sigla_itemserv_var',
    nullable: true,
    length: 50,
  })
  siglaItemservVar: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => OpeCicloVar, (opeCicloVar) => opeCicloVar.gerItemservVars)
  @JoinColumn([{ name: 'ope_ciclo_var_id', referencedColumnName: 'id' }])
  opeCicloVar: OpeCicloVar;

  @OneToMany(() => MovItemserv, (movItemserv) => movItemserv.gerItemservVar)
  movItemservs: MovItemserv[];

  @OneToMany(
    () => OpeCentro2Area,
    (opeCentro2Area) => opeCentro2Area.gerItemservVar,
  )
  opeCentro2Areas: OpeCentro2Area[];

  @OneToMany(
    () => OpeCentro2Area,
    (opeCentro2Area) => opeCentro2Area.gerItemservVarIdUlt,
  )
  opeCentro2Areas2: OpeCentro2Area[];
}
