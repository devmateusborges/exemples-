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
import { FinConta } from './FinConta.entity';
import { GerPessoaContaBanco } from './GerPessoaContaBanco.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_banco', ['id'], { unique: true })
@Entity('fin_banco', { schema: 'public' })
export class FinBanco extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'nr_banco', length: 50 })
  nrBanco: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(() => FinConta, (finConta) => finConta.finBanco)
  finContas: FinConta[];

  @OneToMany(
    () => GerPessoaContaBanco,
    (gerPessoaContaBanco) => gerPessoaContaBanco.finBanco,
  )
  gerPessoaContaBancos: GerPessoaContaBanco[];
}
