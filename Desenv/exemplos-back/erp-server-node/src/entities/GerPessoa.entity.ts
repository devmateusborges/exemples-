import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { FinPagrec } from './FinPagrec.entity';
import { FinPagrecPrev } from './FinPagrecPrev.entity';
import { FinUnitParam } from './FinUnitParam.entity';
import { GerEmpresaPessoa } from './GerEmpresaPessoa.entity';
import { GerItemservPessoa } from './GerItemservPessoa.entity';
import { GerMarcaPessoa } from './GerMarcaPessoa.entity';
import { SystemUnit } from './SystemUnit.entity';
import { GerPessoaContaBanco } from './GerPessoaContaBanco.entity';
import { GerPessoaEndereco } from './GerPessoaEndereco.entity';
import { Mov } from './Mov.entity';
import { MovCiot } from './MovCiot.entity';
import { MovCondutor } from './MovCondutor.entity';
import { MovCotacao } from './MovCotacao.entity';
import { MovCotacaoAnal } from './MovCotacaoAnal.entity';
import { MovPedagio } from './MovPedagio.entity';
import { MovSeguradora } from './MovSeguradora.entity';
import { MovTomador } from './MovTomador.entity';
import { OpeCentro1 } from './OpeCentro1.entity';
import { SystemDocument } from './SystemDocument.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_pessoa', ['id'], { unique: true })
@Entity('ger_pessoa', { schema: 'public' })
export class GerPessoa extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'razao_social', length: 100 })
  razaoSocial: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'doc_cnpj', nullable: true, length: 50 })
  docCnpj: string;

  @Column('varchar', { name: 'doc_cpf', nullable: true, length: 50 })
  docCpf: string;

  @Column('varchar', { name: 'doc_ie', nullable: true, length: 50 })
  docIe: string;

  @Column('varchar', { name: 'doc_im', nullable: true, length: 50 })
  docIm: string;

  @Column('varchar', { name: 'doc_cnae', nullable: true, length: 50 })
  docCnae: string;

  @Column('varchar', {
    name: 'data_abertura',
    nullable: true,
    length: 50,
  })
  dataAbertura: string;

  @Column('varchar', {
    name: 'doc_junta',
    nullable: true,
    length: 50,
  })
  docJunta: string;

  @Column('varchar', {
    name: 'fis_regime',
    nullable: true,
    length: 50,
  })
  fisRegime: string;

  @Column('varchar', { name: 'fone_1', nullable: true, length: 100 })
  fone_1: string;

  @Column('varchar', { name: 'fone_2', nullable: true, length: 100 })
  fone_2: string;

  @Column('varchar', { name: 'fone_3', nullable: true, length: 100 })
  fone_3: string;

  @Column('varchar', {
    name: 'contato_1',
    nullable: true,
    length: 100,
  })
  contato_1: string;

  @Column('varchar', {
    name: 'contato_2',
    nullable: true,
    length: 100,
  })
  contato_2: string;

  @Column('varchar', {
    name: 'contato_3',
    nullable: true,
    length: 100,
  })
  contato_3: string;

  @Column('integer', { name: 'contrib_icms' })
  contribIcms: number;

  @Column('varchar', { name: 'nr_rntrc', nullable: true, length: 8 })
  nrRntrc: string;

  @Column('varchar', { name: 'doc_rg', nullable: true, length: 50 })
  docRg: string;

  @Column('varchar', {
    name: 'doc_rg_org_exp',
    nullable: true,
    length: 50,
  })
  docRgOrgExp: string;

  @Column('varchar', { name: 'doc_crc', nullable: true, length: 50 })
  docCrc: string;

  @Column('varchar', {
    name: 'doc_crc_seq',
    nullable: true,
    length: 50,
  })
  docCrcSeq: string;

  @Column('varchar', {
    name: 'doc_crc_org_exp',
    nullable: true,
    length: 50,
  })
  docCrcOrgExp: string;

  @Column('varchar', {
    name: 'sigla_pes',
    nullable: true,
    length: 50,
  })
  siglaPes: string;

  @Column('varchar', {
    name: 'nr_registro_est_cte',
    nullable: true,
    length: 50,
  })
  nrRegistroEstCte: string;

  @Column('varchar', { name: 'doc_taf', nullable: true, length: 50 })
  docTaf: string;

  @Column('date', { name: 'data_valid', nullable: true })
  dataValid: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => FinPagrec, (finPagrec) => finPagrec.gerPessoa)
  finPagrecs: FinPagrec[];

  @OneToMany(() => FinPagrec, (finPagrec) => finPagrec.gerPessoaIdPagrec)
  finPagrecs2: FinPagrec[];

  @OneToMany(() => FinPagrecPrev, (finPagrecPrev) => finPagrecPrev.gerPessoa)
  finPagrecPrevs: FinPagrecPrev[];

  @OneToMany(() => FinUnitParam, (finUnitParam) => finUnitParam.gerPessoa)
  finUnitParams: FinUnitParam[];

  @OneToMany(
    () => GerEmpresaPessoa,
    (gerEmpresaPessoa) => gerEmpresaPessoa.gerPessoa,
  )
  gerEmpresaPessoas: GerEmpresaPessoa[];

  @OneToMany(
    () => GerItemservPessoa,
    (gerItemservPessoa) => gerItemservPessoa.gerPessoa,
  )
  gerItemservPessoas: GerItemservPessoa[];

  @OneToMany(() => GerMarcaPessoa, (gerMarcaPessoa) => gerMarcaPessoa.gerPessoa)
  gerMarcaPessoas: GerMarcaPessoa[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(
    () => GerPessoaContaBanco,
    (gerPessoaContaBanco) => gerPessoaContaBanco.gerPessoa,
  )
  gerPessoaContaBancos: GerPessoaContaBanco[];

  @OneToMany(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.gerPessoa,
  )
  gerPessoaEnderecos: GerPessoaEndereco[];

  @OneToMany(() => Mov, (mov) => mov.gerPessoa)
  movs: Mov[];

  @OneToMany(() => MovCiot, (movCiot) => movCiot.gerPessoaIdResponsavel)
  movCiots: MovCiot[];

  @OneToMany(
    () => MovCondutor,
    (movCondutor) => movCondutor.gerPessoaIdCondutor,
  )
  movCondutors: MovCondutor[];

  @OneToMany(() => MovCotacao, (movCotacao) => movCotacao.gerPessoa)
  movCotacaos: MovCotacao[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c01GerPessoa,
  )
  movCotacaoAnals: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c02GerPessoa,
  )
  movCotacaoAnals2: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c03GerPessoa,
  )
  movCotacaoAnals3: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c04GerPessoa,
  )
  movCotacaoAnals4: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c05GerPessoa,
  )
  movCotacaoAnals5: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c06GerPessoa,
  )
  movCotacaoAnals6: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c07GerPessoa,
  )
  movCotacaoAnals7: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c08GerPessoa,
  )
  movCotacaoAnals8: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c09GerPessoa,
  )
  movCotacaoAnals9: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c10GerPessoa,
  )
  movCotacaoAnas: MovCotacaoAnal[];

  @OneToMany(() => MovPedagio, (movPedagio) => movPedagio.gerPessoaIdEmpPedagio)
  movPedagios: MovPedagio[];

  @OneToMany(
    () => MovPedagio,
    (movPedagio) => movPedagio.gerPessoaIdResponsavel,
  )
  movPedagios2: MovPedagio[];

  @OneToMany(
    () => MovSeguradora,
    (movSeguradora) => movSeguradora.gerPessoaIdResponsavel,
  )
  movSeguradoras: MovSeguradora[];

  @OneToMany(
    () => MovSeguradora,
    (movSeguradora) => movSeguradora.gerPessoaIdSeguradora,
  )
  movSeguradoras2: MovSeguradora[];

  @OneToMany(
    () => MovTomador,
    (movTomador) => movTomador.gerPessoaIdResponsavel,
  )
  movTomadors: MovTomador[];

  @OneToMany(() => OpeCentro1, (opeCentro1) => opeCentro1.gerPessoa)
  opeCentros: OpeCentro1[];

  @OneToMany(() => SystemDocument, (systemDocument) => systemDocument.gerPessoa)
  systemDocuments: SystemDocument[];
}
