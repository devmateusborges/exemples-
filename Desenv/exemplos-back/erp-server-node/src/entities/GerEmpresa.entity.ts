import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { CtbLanc } from './CtbLanc.entity';
import { FinConta } from './FinConta.entity';
import { FinLote } from './FinLote.entity';
import { FinPagrec } from './FinPagrec.entity';
import { FinPagrecBanco } from './FinPagrecBanco.entity';
import { FinPagrecBancoTransf } from './FinPagrecBancoTransf.entity';
import { FinPagrecPrev } from './FinPagrecPrev.entity';
import { FisDoc } from './FisDoc.entity';
import { GerCidade } from './GerCidade.entity';
import { SystemUnit } from './SystemUnit.entity';
import { FisCertificado } from './FisCertificado.entity';
import { GerEmpresaGrupo } from './GerEmpresaGrupo.entity';
import { GerEmpresaPessoa } from './GerEmpresaPessoa.entity';
import { GerPer } from './GerPer.entity';
import { GerProcessoBloq } from './GerProcessoBloq.entity';
import { IndVrAno } from './IndVrAno.entity';
import { IndVrBimestre } from './IndVrBimestre.entity';
import { IndVrDia } from './IndVrDia.entity';
import { IndVrMes } from './IndVrMes.entity';
import { IndVrMeta } from './IndVrMeta.entity';
import { IndVrQuadrimestre } from './IndVrQuadrimestre.entity';
import { IndVrQuinzena } from './IndVrQuinzena.entity';
import { IndVrSemana } from './IndVrSemana.entity';
import { IndVrSemestre } from './IndVrSemestre.entity';
import { IndVrTrimestre } from './IndVrTrimestre.entity';
import { Mov } from './Mov.entity';
import { OpeCentro2Ord } from './OpeCentro2Ord.entity';
import { OpeCentro2ParamPer } from './OpeCentro2ParamPer.entity';
import { OpeCentroConfig } from './OpeCentroConfig.entity';
import { OpeCentroPrev } from './OpeCentroPrev.entity';
import { OpeCentroRatFator } from './OpeCentroRatFator.entity';
import { OpeFrenteTrabalho } from './OpeFrenteTrabalho.entity';
import { OpeOcorCompartMov } from './OpeOcorCompartMov.entity';
import { OpeOcorMov } from './OpeOcorMov.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_empresa', ['id'], { unique: true })
@Entity('ger_empresa', { schema: 'public' })
export class GerEmpresa extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'razao_social', length: 100 })
  razaoSocial: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_empresa', length: 50 })
  siglaEmpresa: string;

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

  @Column('date', { name: 'data_abertura', nullable: true })
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

  @Column('date', { name: 'data_validade_a3', nullable: true })
  dataValidadeA3: string;

  @Column('date', { name: 'data_validade_a1', nullable: true })
  dataValidadeA1: string;

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

  @Column('varchar', { name: 'email_1', nullable: true, length: 255 })
  email_1: string;

  @Column('varchar', {
    name: 'doc_rntrc',
    nullable: true,
    length: 100,
  })
  docRntrc: string;

  @Column('varchar', {
    name: 'fis_dfe_ambiente',
    nullable: true,
    length: 1,
  })
  fisDfeAmbiente: string;

  @Column('text', { name: 'fis_dfe_api_token', nullable: true })
  fisDfeApiToken: string;

  @Column('varchar', {
    name: 'fis_regime_trib_nfs',
    nullable: true,
    length: 1,
  })
  fisRegimeTribNfs: string;

  @Column('varchar', {
    name: 'fis_provedor_nfs',
    nullable: true,
    length: 1,
  })
  fisProvedorNfs: string;

  @Column('varchar', {
    name: 'fis_incent_cultura',
    nullable: true,
    length: 1,
  })
  fisIncentCultura: string;

  @Column('varchar', {
    name: 'fis_incent_fiscal_nfs',
    nullable: true,
    length: 1,
  })
  fisIncentFiscalNfs: string;

  @Column('integer', { name: 'ini_semana', nullable: true, default: () => '0' })
  iniSemana: number | null;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => CtbLanc, (ctbLanc) => ctbLanc.gerEmpresa)
  ctbLancs: CtbLanc[];

  @OneToMany(() => FinConta, (finConta) => finConta.gerEmpresa)
  finContas: FinConta[];

  @OneToMany(() => FinLote, (finLote) => finLote.gerEmpresa)
  finLotes: FinLote[];

  @OneToMany(() => FinPagrec, (finPagrec) => finPagrec.gerEmpresa)
  finPagrecs: FinPagrec[];

  @OneToMany(
    () => FinPagrecBanco,
    (finPagrecBanco) => finPagrecBanco.gerEmpresa,
  )
  finPagrecBancos: FinPagrecBanco[];

  @OneToMany(
    () => FinPagrecBancoTransf,
    (finPagrecBancoTransf) => finPagrecBancoTransf.gerEmpresa,
  )
  finPagrecBancoTransfs: FinPagrecBancoTransf[];

  @OneToMany(() => FinPagrecPrev, (finPagrecPrev) => finPagrecPrev.gerEmpresa)
  finPagrecPrevs: FinPagrecPrev[];

  @OneToMany(() => FisDoc, (fisDoc) => fisDoc.gerEmpresa)
  fisDocs: FisDoc[];

  @ManyToOne(() => GerCidade, (gerCidade) => gerCidade.gerEmpresas)
  @JoinColumn([{ name: 'end_ger_cidade_id', referencedColumnName: 'id' }])
  endGerCidade: GerCidade;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => FisCertificado,
    (fisCertificado) => fisCertificado.gerEmpresas,
  )
  @JoinColumn([{ name: 'fis_certificado_id', referencedColumnName: 'id' }])
  fisCertificado: FisCertificado;

  @ManyToOne(
    () => GerEmpresaGrupo,
    (gerEmpresaGrupo) => gerEmpresaGrupo.gerEmpresas,
  )
  @JoinColumn([{ name: 'ger_empresa_grupo_id', referencedColumnName: 'id' }])
  gerEmpresaGrupo: GerEmpresaGrupo;

  @OneToMany(
    () => GerEmpresaPessoa,
    (gerEmpresaPessoa) => gerEmpresaPessoa.gerEmpresa,
  )
  gerEmpresaPessoas: GerEmpresaPessoa[];

  @OneToMany(() => GerPer, (gerPer) => gerPer.gerEmpresa)
  gerPers: GerPer[];

  @OneToMany(
    () => GerProcessoBloq,
    (gerProcessoBloq) => gerProcessoBloq.gerEmpresa,
  )
  gerProcessoBloqs: GerProcessoBloq[];

  @OneToMany(() => IndVrAno, (indVrAno) => indVrAno.gerEmpresa)
  indVrAnos: IndVrAno[];

  @OneToMany(() => IndVrBimestre, (indVrBimestre) => indVrBimestre.gerEmpresa)
  indVrBimestres: IndVrBimestre[];

  @OneToMany(() => IndVrDia, (indVrDia) => indVrDia.gerEmpresa)
  indVrDias: IndVrDia[];

  @OneToMany(() => IndVrMes, (indVrMes) => indVrMes.gerEmpresa)
  indVrMes: IndVrMes[];

  @OneToMany(() => IndVrMeta, (indVrMeta) => indVrMeta.gerEmpresa)
  indVrMetas: IndVrMeta[];

  @OneToMany(
    () => IndVrQuadrimestre,
    (indVrQuadrimestre) => indVrQuadrimestre.gerEmpresa,
  )
  indVrQuadrimestres: IndVrQuadrimestre[];

  @OneToMany(() => IndVrQuinzena, (indVrQuinzena) => indVrQuinzena.gerEmpresa)
  indVrQuinzenas: IndVrQuinzena[];

  @OneToMany(() => IndVrSemana, (indVrSemana) => indVrSemana.gerEmpresa)
  indVrSemanas: IndVrSemana[];

  @OneToMany(() => IndVrSemestre, (indVrSemestre) => indVrSemestre.gerEmpresa)
  indVrSemestres: IndVrSemestre[];

  @OneToMany(
    () => IndVrTrimestre,
    (indVrTrimestre) => indVrTrimestre.gerEmpresa,
  )
  indVrTrimestres: IndVrTrimestre[];

  @OneToMany(() => Mov, (mov) => mov.gerEmpresa)
  movs: Mov[];

  @OneToMany(() => OpeCentro2Ord, (opeCentro2Ord) => opeCentro2Ord.gerEmpresa)
  opeCentro2Ords: OpeCentro2Ord[];

  @OneToMany(
    () => OpeCentro2ParamPer,
    (opeCentro2ParamPer) => opeCentro2ParamPer.gerEmpresa,
  )
  opeCentro2ParamPers: OpeCentro2ParamPer[];

  @OneToMany(
    () => OpeCentroConfig,
    (opeCentroConfig) => opeCentroConfig.gerEmpresa,
  )
  opeCentroConfigs: OpeCentroConfig[];

  @OneToMany(() => OpeCentroPrev, (opeCentroPrev) => opeCentroPrev.gerEmpresa)
  opeCentroPrevs: OpeCentroPrev[];

  @OneToMany(
    () => OpeCentroRatFator,
    (opeCentroRatFator) => opeCentroRatFator.gerEmpresa,
  )
  opeCentroRatFators: OpeCentroRatFator[];

  @OneToMany(
    () => OpeFrenteTrabalho,
    (opeFrenteTrabalho) => opeFrenteTrabalho.gerEmpresa,
  )
  opeFrenteTrabalhos: OpeFrenteTrabalho[];

  @OneToMany(
    () => OpeOcorCompartMov,
    (opeOcorCompartMov) => opeOcorCompartMov.gerEmpresa,
  )
  opeOcorCompartMovs: OpeOcorCompartMov[];

  @OneToMany(() => OpeOcorMov, (opeOcorMov) => opeOcorMov.gerEmpresa)
  opeOcorMovs: OpeOcorMov[];
}
