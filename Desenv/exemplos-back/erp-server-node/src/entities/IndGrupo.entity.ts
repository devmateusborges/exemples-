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
import { IndGrupoRelacSub } from './IndGrupoRelacSub.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ind_grupo', ['id'], { unique: true })
@Entity('ind_grupo', { schema: 'public' })
export class IndGrupo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('integer', { name: 'ordem_exibicao' })
  ordemExibicao: number;

  @Column('varchar', { name: 'sigla_grupo', length: 50 })
  siglaGrupo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(
    () => IndGrupoRelacSub,
    (indGrupoRelacSub) => indGrupoRelacSub.indGrupo,
  )
  indGrupoRelacSubs: IndGrupoRelacSub[];

  @OneToMany(
    () => IndGrupoRelacSub,
    (indGrupoRelacSub) => indGrupoRelacSub.indGrupo_2,
  )
  indGrupoRelacSubs2: IndGrupoRelacSub[];
}
