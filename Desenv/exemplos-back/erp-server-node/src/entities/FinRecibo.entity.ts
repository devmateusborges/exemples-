import { Column, Entity, Index, OneToMany } from 'typeorm';
import { FinPagrecOrigem } from './FinPagrecOrigem.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_recibo', ['id'], { unique: true })
@Entity('fin_recibo', { schema: 'public' })
export class FinRecibo extends BaseEntity {
  @Column('varchar', { name: 'unit_id', length: 36 })
  unitId: string;

  @Column('date', { name: 'data_recibo', nullable: true })
  dataRecibo: string;

  @Column('text', { name: 'conteudo' })
  conteudo: string;

  @Column('numeric', { name: 'valor', precision: 18, scale: 2 })
  valor: string;

  @Column('varchar', {
    name: 'ger_pessoa_endereco_id',
    nullable: true,
    length: 36,
  })
  gerPessoaEnderecoId: string;

  @Column('varchar', {
    name: 'nome_pessoa',
    nullable: true,
    length: 100,
  })
  nomePessoa: string;

  @Column('varchar', {
    name: 'nr_doc_pessoa',
    nullable: true,
    length: 50,
  })
  nrDocPessoa: string;

  @Column('varchar', {
    name: 'tipo_doc_pessoa',
    nullable: true,
    length: 50,
  })
  tipoDocPessoa: string;

  @Column('varchar', { name: 'status', length: 2 })
  status: string;

  @Column('varchar', {
    name: 'status_observacao',
    nullable: true,
    length: 250,
  })
  statusObservacao: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => FinPagrecOrigem,
    (finPagrecOrigem) => finPagrecOrigem.finRecibo,
  )
  finPagrecOrigems: FinPagrecOrigem[];
}
