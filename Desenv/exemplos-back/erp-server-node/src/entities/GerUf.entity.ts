import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { FisIbpt } from './FisIbpt.entity';
import { GerCidade } from './GerCidade.entity';
import { GerPais } from './GerPais.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_uf', ['id'], { unique: true })
@Entity('ger_uf', { schema: 'public' })
export class GerUf extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'nr_uf', length: 50 })
  nrUf: string;

  @Column('varchar', { name: 'sigla_uf', length: 50 })
  siglaUf: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => FisIbpt, (fisIbpt) => fisIbpt.gerUf)
  fisIbpts: FisIbpt[];

  @OneToMany(() => GerCidade, (gerCidade) => gerCidade.gerUf)
  gerCidades: GerCidade[];

  @ManyToOne(() => GerPais, (gerPais) => gerPais.gerUfs)
  @JoinColumn([{ name: 'ger_pais_id', referencedColumnName: 'id' }])
  gerPais: GerPais;
}
