import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { FinPagrecOrigem } from './FinPagrecOrigem.entity';
import { FisDoc } from './FisDoc.entity';
import { FisTributacao } from './FisTributacao.entity';
import { FisDocTipo } from './FisDocTipo.entity';
import { GerCidade } from './GerCidade.entity';
import { SystemUser } from './SystemUser.entity';
import { SystemUnit } from './SystemUnit.entity';
import { FinCondPagrec } from './FinCondPagrec.entity';
import { GerEmpresa } from './GerEmpresa.entity';
import { GerPessoaEndereco } from './GerPessoaEndereco.entity';
import { GerPessoa } from './GerPessoa.entity';
import { MovOperacao } from './MovOperacao.entity';
import { MovStatus } from './MovStatus.entity';
import { MovCiot } from './MovCiot.entity';
import { MovComp } from './MovComp.entity';
import { MovCondutor } from './MovCondutor.entity';
import { MovCotacao } from './MovCotacao.entity';
import { MovCotacaoAnal } from './MovCotacaoAnal.entity';
import { MovEntrega } from './MovEntrega.entity';
import { MovEntregaDoc } from './MovEntregaDoc.entity';
import { MovFrete } from './MovFrete.entity';
import { MovItemserv } from './MovItemserv.entity';
import { MovLacre } from './MovLacre.entity';
import { MovMedida } from './MovMedida.entity';
import { MovOrigem } from './MovOrigem.entity';
import { MovPedagio } from './MovPedagio.entity';
import { MovPercurso } from './MovPercurso.entity';
import { MovReboque } from './MovReboque.entity';
import { MovSeguradora } from './MovSeguradora.entity';
import { MovTomador } from './MovTomador.entity';
import { SystemDocument } from './SystemDocument.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_mov', ['id'], { unique: true })
@Entity('mov', { schema: 'public' })
export class Mov extends BaseEntity {
  @Column('varchar', {
    name: 'nr_externo',
    nullable: true,
    length: 50,
  })
  nrExterno: string;

  @Column('timestamp without time zone', { name: 'data_mov', nullable: true })
  dataMov: Date | null;

  @Column('integer', { name: 'numero_mov', nullable: true })
  numeroMov: number | null;

  @Column('timestamp without time zone', {
    name: 'data_emissao',
    nullable: true,
  })
  dataEmissao: Date | null;

  @Column('varchar', { name: 'serie_mov', nullable: true, length: 3 })
  serieMov: string;

  @Column('numeric', { name: 'valor_total', precision: 18, scale: 6 })
  valorTotal: string;

  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column('integer', { name: 'tipo_frete' })
  tipoFrete: number;

  @Column('date', { name: 'data_entrega', nullable: true })
  dataEntrega: string;

  @Column('date', { name: 'data_entrada_saida', nullable: true })
  dataEntradaSaida: string;

  @Column('integer', { name: 'tipo_emissao_carga', nullable: true })
  tipoEmissaoCarga: number | null;

  @Column('varchar', {
    name: 'tipo_modal_carga',
    nullable: true,
    length: 2,
  })
  tipoModalCarga: string;

  @Column('integer', { name: 'tipo_transportador_carga', nullable: true })
  tipoTransportadorCarga: number | null;

  @Column('numeric', {
    name: 'valor_carga',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  valorCarga: string;

  @Column('varchar', {
    name: 'tipo_umedida_carga',
    nullable: true,
    length: 2,
  })
  tipoUmedidaCarga: string;

  @Column('numeric', {
    name: 'qnt_carga',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  qntCarga: string;

  @Column('varchar', {
    name: 'observacao_transp',
    nullable: true,
    length: 250,
  })
  observacaoTransp: string;

  @Column('varchar', {
    name: 'observacao_serv',
    nullable: true,
    length: 250,
  })
  observacaoServ: string;

  @Column('integer', { name: 'tipo_fretamento', nullable: true })
  tipoFretamento: number | null;

  @Column('integer', { name: 'tipo_serv_frete', nullable: true })
  tipoServFrete: number | null;

  @Column('integer', { name: 'tipo_tomador_serv_frete', nullable: true })
  tipoTomadorServFrete: number | null;

  @Column('varchar', { name: 'taf', nullable: true, length: 50 })
  taf: string;

  @Column('date', { name: 'data_anulacao', nullable: true })
  dataAnulacao: string;

  @Column('varchar', {
    name: 'observacao_item',
    nullable: true,
    length: 250,
  })
  observacaoItem: string;

  @Column('numeric', {
    name: 'valor_financeiro_total',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  valorFinanceiroTotal: string;

  @Column('numeric', {
    name: 'valor_item_frete_total',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  valorItemFreteTotal: string;

  @Column('varchar', {
    name: 'observacao_fiscal',
    nullable: true,
    length: 250,
  })
  observacaoFiscal: string;

  @Column('varchar', {
    name: 'fis_tipo_resp_reten',
    nullable: true,
    length: 1,
  })
  fisTipoRespReten: string;

  @Column('varchar', {
    name: 'fis_exig_iss_nfs',
    nullable: true,
    length: 1,
  })
  fisExigIssNfs: string;

  @Column('varchar', {
    name: 'fis_iss_retido_nfs',
    nullable: true,
    length: 1,
  })
  fisIssRetidoNfs: string;

  @Column('varchar', {
    name: 'fis_nat_ope_nfs',
    nullable: true,
    length: 1,
  })
  fisNatOpeNfs: string;

  @Column('integer', { name: 'numero_mov_pre', nullable: true })
  numeroMovPre: number | null;

  @Column('varchar', {
    name: 'serio_mov_pre',
    nullable: true,
    length: 3,
  })
  serioMovPre: string;

  @Column('varchar', {
    name: 'cep_carreg',
    nullable: true,
    length: 50,
  })
  cepCarreg: string;

  @Column('varchar', {
    name: 'cep_descarreg',
    nullable: true,
    length: 50,
  })
  cepDescarreg: string;

  @Column('varchar', {
    name: 'tipo_carga',
    nullable: true,
    length: 2,
  })
  tipoCarga: string;

  @Column('date', { name: 'data_valid', nullable: true })
  dataValid: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => FinPagrecOrigem, (finPagrecOrigem) => finPagrecOrigem.mov)
  finPagrecOrigems: FinPagrecOrigem[];

  @OneToMany(() => FisDoc, (fisDoc) => fisDoc.mov)
  fisDocs: FisDoc[];

  @OneToMany(() => FisTributacao, (fisTributacao) => fisTributacao.mov)
  fisTributacaos: FisTributacao[];

  @ManyToOne(() => FisDocTipo, (fisDocTipo) => fisDocTipo.movs)
  @JoinColumn([{ name: 'fis_doc_tipo_id', referencedColumnName: 'id' }])
  fisDocTipo: FisDocTipo;

  @ManyToOne(() => GerCidade, (gerCidade) => gerCidade.movs)
  @JoinColumn([{ name: 'ger_cidade_id_carreg', referencedColumnName: 'id' }])
  gerCidadeIdCarreg: GerCidade;

  @ManyToOne(() => GerCidade, (gerCidade) => gerCidade.movs2)
  @JoinColumn([{ name: 'ger_cidade_id_descarreg', referencedColumnName: 'id' }])
  gerCidadeIdDescarreg: GerCidade;

  @OneToOne(() => SystemUser)
  @JoinColumn([{ name: 'system_user_id_resp', referencedColumnName: 'id' }])
  systemUserIdResp: SystemUser;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => FinCondPagrec, (finCondPagrec) => finCondPagrec.movs)
  @JoinColumn([{ name: 'fin_cond_pagrec_id', referencedColumnName: 'id' }])
  finCondPagrec: FinCondPagrec;

  @ManyToOne(() => GerEmpresa, (gerEmpresa) => gerEmpresa.movs)
  @JoinColumn([{ name: 'ger_empresa_id', referencedColumnName: 'id' }])
  gerEmpresa: GerEmpresa;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.movs,
  )
  @JoinColumn([
    { name: 'ger_pessoa_endereco_id_dest', referencedColumnName: 'id' },
  ])
  gerPessoaEnderecoIdDest: GerPessoaEndereco;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.movs2,
  )
  @JoinColumn([
    { name: 'ger_pessoa_endereco_id_entrega', referencedColumnName: 'id' },
  ])
  gerPessoaEnderecoIdEntrega: GerPessoaEndereco;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.movs3,
  )
  @JoinColumn([
    { name: 'ger_pessoa_endereco_id_expe', referencedColumnName: 'id' },
  ])
  gerPessoaEnderecoIdExpe: GerPessoaEndereco;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.movs4,
  )
  @JoinColumn([
    { name: 'ger_pessoa_endereco_id_fiscal', referencedColumnName: 'id' },
  ])
  gerPessoaEnderecoIdFiscal: GerPessoaEndereco;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.movs5,
  )
  @JoinColumn([
    { name: 'ger_pessoa_endereco_id_inter', referencedColumnName: 'id' },
  ])
  gerPessoaEnderecoIdInter: GerPessoaEndereco;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.movs6,
  )
  @JoinColumn([
    { name: 'ger_pessoa_endereco_id_rece', referencedColumnName: 'id' },
  ])
  gerPessoaEnderecoIdRece: GerPessoaEndereco;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.movs7,
  )
  @JoinColumn([
    { name: 'ger_pessoa_endereco_id_reme', referencedColumnName: 'id' },
  ])
  gerPessoaEnderecoIdReme: GerPessoaEndereco;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.movs)
  @JoinColumn([{ name: 'ger_pessoa_id', referencedColumnName: 'id' }])
  gerPessoa: GerPessoa;

  @ManyToOne(() => MovOperacao, (movOperacao) => movOperacao.movs)
  @JoinColumn([{ name: 'mov_operacao_id', referencedColumnName: 'id' }])
  movOperacao: MovOperacao;

  @ManyToOne(() => MovStatus, (movStatus) => movStatus.movs)
  @JoinColumn([{ name: 'mov_status_id', referencedColumnName: 'id' }])
  movStatus: MovStatus;

  @OneToMany(() => MovCiot, (movCiot) => movCiot.mov)
  movCiots: MovCiot[];

  @OneToMany(() => MovComp, (movComp) => movComp.mov)
  movComps: MovComp[];

  @OneToMany(() => MovCondutor, (movCondutor) => movCondutor.mov)
  movCondutors: MovCondutor[];

  @OneToMany(() => MovCotacao, (movCotacao) => movCotacao.mov)
  movCotacaos: MovCotacao[];

  @OneToMany(() => MovCotacaoAnal, (movCotacaoAnal) => movCotacaoAnal.mov)
  movCotacaoAnals: MovCotacaoAnal[];

  @OneToMany(() => MovEntrega, (movEntrega) => movEntrega.mov)
  movEntregas: MovEntrega[];

  @OneToMany(() => MovEntregaDoc, (movEntregaDoc) => movEntregaDoc.mov)
  movEntregaDocs: MovEntregaDoc[];

  @OneToMany(() => MovEntregaDoc, (movEntregaDoc) => movEntregaDoc.movIdInterno)
  movEntregaDocs2: MovEntregaDoc[];

  @OneToMany(() => MovFrete, (movFrete) => movFrete.mov)
  movFretes: MovFrete[];

  @OneToMany(() => MovItemserv, (movItemserv) => movItemserv.mov)
  movItemservs: MovItemserv[];

  @OneToMany(() => MovLacre, (movLacre) => movLacre.mov)
  movLacres: MovLacre[];

  @OneToMany(() => MovMedida, (movMedida) => movMedida.mov)
  movMedidas: MovMedida[];

  @OneToMany(() => MovOrigem, (movOrigem) => movOrigem.mov)
  movOrigems: MovOrigem[];

  @OneToMany(() => MovOrigem, (movOrigem) => movOrigem.movIdOrigem)
  movOrigems2: MovOrigem[];

  @OneToMany(() => MovPedagio, (movPedagio) => movPedagio.mov)
  movPedagios: MovPedagio[];

  @OneToMany(() => MovPercurso, (movPercurso) => movPercurso.mov)
  movPercursos: MovPercurso[];

  @OneToMany(() => MovReboque, (movReboque) => movReboque.mov)
  movReboques: MovReboque[];

  @OneToMany(() => MovSeguradora, (movSeguradora) => movSeguradora.mov)
  movSeguradoras: MovSeguradora[];

  @OneToMany(() => MovTomador, (movTomador) => movTomador.mov)
  movTomadors: MovTomador[];

  @OneToMany(() => SystemDocument, (systemDocument) => systemDocument.mov)
  systemDocuments: SystemDocument[];
}
