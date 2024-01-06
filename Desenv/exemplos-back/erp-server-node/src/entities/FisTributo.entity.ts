import { Column, Entity, Index, OneToMany } from 'typeorm';
import { FisTributacao } from './FisTributacao.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fis_tributo', ['id'], { unique: true })
@Entity('fis_tributo', { schema: 'public' })
export class FisTributo extends BaseEntity {
  @Column('varchar', { name: 'nr_tributo', length: 50 })
  nrTributo: string;

  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => FisTributacao, (fisTributacao) => fisTributacao.fisTributo)
  fisTributacaos: FisTributacao[];
}
