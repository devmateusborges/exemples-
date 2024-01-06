import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { OpeAtividade } from './OpeAtividade.entity';
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_atividade_grupo', ['id'], { unique: true })
@Entity('ope_atividade_grupo', { schema: 'public' })
export class OpeAtividadeGrupo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_atividade_grupo', length: 50 })
  siglaAtividadeGrupo: string;

  @Column('varchar', { name: 'ordem', length: 3 })
  ordem: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => OpeAtividade,
    (opeAtividade) => opeAtividade.opeAtividadeGrupo,
  )
  opeAtividades: OpeAtividade[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
