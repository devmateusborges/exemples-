import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { FisTributacao } from './FisTributacao.entity';
import { GerCidade } from './GerCidade.entity';
import { SystemUnit } from './SystemUnit.entity';
import { GerPessoa } from './GerPessoa.entity';
import { Mov } from './Mov.entity';
import { MovCotacao } from './MovCotacao.entity';
import { MovCotacaoAnal } from './MovCotacaoAnal.entity';
import { MovFrete } from './MovFrete.entity';
import { OpeCentro2 } from './OpeCentro2.entity';
import { OpeCentro2Ord } from './OpeCentro2Ord.entity';
import { OpeCentro2OrdRec } from './OpeCentro2OrdRec.entity';
import { OpeOcorCompartMov } from './OpeOcorCompartMov.entity';
import { OpeOcorMov } from './OpeOcorMov.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_pessoa_endereco', ['id'], { unique: true })
@Entity('ger_pessoa_endereco', { schema: 'public' })
export class GerPessoaEndereco extends BaseEntity {
  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'tipo', length: 1 })
  tipo: string;

  @Column('varchar', { name: 'padrao', length: 1 })
  padrao: string;

  @Column('varchar', {
    name: 'end_logradouro',
    nullable: true,
    length: 100,
  })
  endLogradouro: string;

  @Column('varchar', {
    name: 'end_logradouro_nr',
    nullable: true,
    length: 10,
  })
  endLogradouroNr: string;

  @Column('varchar', {
    name: 'end_bairro',
    nullable: true,
    length: 100,
  })
  endBairro: string;

  @Column('varchar', {
    name: 'end_complemento',
    nullable: true,
    length: 100,
  })
  endComplemento: string;

  @Column('varchar', { name: 'end_cep', nullable: true, length: 100 })
  endCep: string;

  @Column('varchar', { name: 'fone', nullable: true, length: 100 })
  fone: string;

  @Column('varchar', { name: 'email', nullable: true, length: 100 })
  email: string;

  @Column('varchar', { name: 'contato', nullable: true, length: 100 })
  contato: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => FisTributacao,
    (fisTributacao) => fisTributacao.gerPessoaEndereco,
  )
  fisTributacaos: FisTributacao[];

  @ManyToOne(() => GerCidade, (gerCidade) => gerCidade.gerPessoaEnderecos)
  @JoinColumn([{ name: 'end_ger_cidade_id', referencedColumnName: 'id' }])
  endGerCidade: GerCidade;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.gerPessoaEnderecos)
  @JoinColumn([{ name: 'ger_pessoa_id', referencedColumnName: 'id' }])
  gerPessoa: GerPessoa;

  @OneToMany(() => Mov, (mov) => mov.gerPessoaEnderecoIdDest)
  movs: Mov[];

  @OneToMany(() => Mov, (mov) => mov.gerPessoaEnderecoIdEntrega)
  movs2: Mov[];

  @OneToMany(() => Mov, (mov) => mov.gerPessoaEnderecoIdExpe)
  movs3: Mov[];

  @OneToMany(() => Mov, (mov) => mov.gerPessoaEnderecoIdFiscal)
  movs4: Mov[];

  @OneToMany(() => Mov, (mov) => mov.gerPessoaEnderecoIdInter)
  movs5: Mov[];

  @OneToMany(() => Mov, (mov) => mov.gerPessoaEnderecoIdRece)
  movs6: Mov[];

  @OneToMany(() => Mov, (mov) => mov.gerPessoaEnderecoIdReme)
  movs7: Mov[];

  @OneToMany(() => MovCotacao, (movCotacao) => movCotacao.gerPessoaEndereco)
  movCotacaos: MovCotacao[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c01GerPessoaEndereco,
  )
  movCotacaoAnals: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c02GerPessoaEndereco,
  )
  movCotacaoAnals2: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c03GerPessoaEndereco,
  )
  movCotacaoAnals3: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c04GerPessoaEndereco,
  )
  movCotacaoAnals4: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c05GerPessoaEndereco,
  )
  movCotacaoAnals5: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c06GerPessoaEndereco,
  )
  movCotacaoAnals6: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c07GerPessoaEndereco,
  )
  movCotacaoAnals7: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c08GerPessoaEndereco,
  )
  movCotacaoAnals8: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c09GerPessoaEndereco,
  )
  movCotacaoAnals9: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c10GerPessoaEndereco,
  )
  movCotacaoAnas: MovCotacaoAnal[];

  @OneToMany(() => MovFrete, (movFrete) => movFrete.gerPessoaEnderecoIdCondutor)
  movFretes: MovFrete[];

  @OneToMany(() => MovFrete, (movFrete) => movFrete.gerPessoaEnderecoIdTransp)
  movFretes2: MovFrete[];

  @OneToMany(() => OpeCentro2, (opeCentro2) => opeCentro2.gerPessoaEndereco)
  opeCentros: OpeCentro2[];

  @OneToMany(
    () => OpeCentro2Ord,
    (opeCentro2Ord) => opeCentro2Ord.gerPessoaEnderecoIdExec,
  )
  opeCentro2Ords: OpeCentro2Ord[];

  @OneToMany(
    () => OpeCentro2OrdRec,
    (opeCentro2OrdRec) => opeCentro2OrdRec.gerPessoaEnderecoIdExec,
  )
  opeCentro2OrdRecs: OpeCentro2OrdRec[];

  @OneToMany(
    () => OpeOcorCompartMov,
    (opeOcorCompartMov) => opeOcorCompartMov.gerPessoaEnderecoIdExec,
  )
  opeOcorCompartMovs: OpeOcorCompartMov[];

  @OneToMany(
    () => OpeOcorMov,
    (opeOcorMov) => opeOcorMov.gerPessoaEnderecoIdExec,
  )
  opeOcorMovs: OpeOcorMov[];
}
