import { Column, Entity, Index, OneToMany } from 'typeorm';
import { MovOperacao } from './MovOperacao.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_mov_tipo', ['id'], { unique: true })
@Entity('mov_tipo', { schema: 'public' })
export class MovTipo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_mov_tipo', length: 50 })
  siglaMovTipo: string;

  @Column('varchar', { name: 'tipo_mov', length: 10 })
  tipoMov: string;

  @Column('text', { name: 'configuracao', nullable: true })
  configuracao: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => MovOperacao, (movOperacao) => movOperacao.movTipo)
  movOperacaos: MovOperacao[];
}
