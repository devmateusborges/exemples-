import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { FinBanco } from './FinBanco.entity';
import { GerPessoa } from './GerPessoa.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_pessoa_conta_banco', ['id'], { unique: true })
@Entity('ger_pessoa_conta_banco', { schema: 'public' })
export class GerPessoaContaBanco extends BaseEntity {
  @Column('varchar', { name: 'unit_id', length: 36 })
  unitId: string;

  @Column('varchar', { name: 'agencia', length: 100 })
  agencia: string;

  @Column('varchar', { name: 'conta', length: 100 })
  conta: string;

  @Column('varchar', { name: 'observacao', length: 250 })
  observacao: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => FinBanco, (finBanco) => finBanco.gerPessoaContaBancos)
  @JoinColumn([{ name: 'fin_banco_id', referencedColumnName: 'id' }])
  finBanco: FinBanco;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.gerPessoaContaBancos)
  @JoinColumn([{ name: 'ger_pessoa_id', referencedColumnName: 'id' }])
  gerPessoa: GerPessoa;
}
