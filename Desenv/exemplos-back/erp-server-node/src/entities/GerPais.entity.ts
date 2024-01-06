import { Column, Entity, Index, OneToMany } from 'typeorm';
import { GerUf } from './GerUf.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_pais', ['id'], { unique: true })
@Entity('ger_pais', { schema: 'public' })
export class GerPais extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'nr_pais', length: 50 })
  nrPais: string;

  @Column('varchar', {
    name: 'sigla_pais',
    nullable: true,
    length: 50,
  })
  siglaPais: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => GerUf, (gerUf) => gerUf.gerPais)
  gerUfs: GerUf[];
}
