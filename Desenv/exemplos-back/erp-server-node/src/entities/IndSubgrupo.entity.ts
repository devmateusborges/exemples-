import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { IndGrupoRelacSub } from './IndGrupoRelacSub.entity';
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ind_subgrupo', ['id'], { unique: true })
@Entity('ind_subgrupo', { schema: 'public' })
export class IndSubgrupo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('integer', { name: 'ordem_exibicao' })
  ordemExibicao: number;

  @Column('varchar', { name: 'sigla_subgrupo', length: 50 })
  siglaSubgrupo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => IndGrupoRelacSub,
    (indGrupoRelacSub) => indGrupoRelacSub.indSubgrupo,
  )
  indGrupoRelacSubs: IndGrupoRelacSub[];

  @OneToMany(
    () => IndGrupoRelacSub,
    (indGrupoRelacSub) => indGrupoRelacSub.indSubgrupo_2,
  )
  indGrupoRelacSubs2: IndGrupoRelacSub[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
