import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_compart_posicao', ['id'], { unique: true })
@Entity('ope_compart_posicao', { schema: 'public' })
export class OpeCompartPosicao extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_compart_posicao', length: 50 })
  siglaCompartPosicao: string;

  @Column('smallint', { name: 'numero_eixo', default: () => '0' })
  numeroEixo: number;

  @Column('varchar', { name: 'posicao', length: 1 })
  posicao: string;

  @Column('varchar', { name: 'banda_montagem', length: 1 })
  bandaMontagem: string;

  @Column('varchar', { name: 'lado_montagem', length: 1 })
  ladoMontagem: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
