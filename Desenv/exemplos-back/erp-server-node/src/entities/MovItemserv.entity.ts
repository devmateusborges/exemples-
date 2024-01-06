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
import { FisCfop } from './FisCfop.entity';
import { GerUmedida } from './GerUmedida.entity';
import { SystemUnit } from './SystemUnit.entity';
import { GerItemserv } from './GerItemserv.entity';
import { GerItemservLote } from './GerItemservLote.entity';
import { GerItemservVar } from './GerItemservVar.entity';
import { Mov } from './Mov.entity';
import { MovOrigem } from './MovOrigem.entity';
import { OpeCentroDest } from './OpeCentroDest.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_mov_itemserv', ['id'], { unique: true })
@Entity('mov_itemserv', { schema: 'public' })
export class MovItemserv extends BaseEntity {
  @Column('numeric', {
    name: 'qnt_orig',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  qntOrig: string;

  @Column('numeric', {
    name: 'valor_unit_orig',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorUnitOrig: string;

  @Column('numeric', {
    name: 'qnt_conv',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  qntConv: string;

  @Column('numeric', {
    name: 'valor_unit_conv',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorUnitConv: string;

  @Column('numeric', {
    name: 'valor_bruto',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorBruto: string;

  @Column('numeric', {
    name: 'valor_desconto',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorDesconto: string;

  @Column('numeric', {
    name: 'valor_acrecimo',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorAcrecimo: string;

  @Column('numeric', {
    name: 'valor_outros',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorOutros: string;

  @Column('numeric', {
    name: 'valor_liquido',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorLiquido: string;

  @Column('numeric', {
    name: 'qnt_devolvida',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  qntDevolvida: string;

  @Column('numeric', { name: 'valor_frete', precision: 18, scale: 6 })
  valorFrete: string;

  @Column('numeric', { name: 'valor_seguro', precision: 18, scale: 6 })
  valorSeguro: string;

  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column('numeric', {
    name: 'valor_tributo_retido',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorTributoRetido: string;

  @Column('numeric', {
    name: 'valor_tributo_total',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorTributoTotal: string;

  @Column('numeric', {
    name: 'qnt_altura',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  qntAltura: string;

  @Column('numeric', {
    name: 'qnt_largura',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  qntLargura: string;

  @Column('numeric', {
    name: 'qnt_comprimento',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  qntComprimento: string;

  @Column('varchar', {
    name: 'nome_itemserv',
    nullable: true,
    length: 250,
  })
  nomeItemserv: string;

  @Column('varchar', {
    name: 'fis_obra_art',
    nullable: true,
    length: 50,
  })
  fisObraArt: string;

  @Column('varchar', {
    name: 'fis_obra_cei',
    nullable: true,
    length: 50,
  })
  fisObraCei: string;

  @Column('varchar', {
    name: 'fis_numero_proc_susp_nfs',
    nullable: true,
    length: 50,
  })
  fisNumeroProcSuspNfs: string;

  @Column('varchar', {
    name: 'fis_doc_cnae_nfs',
    nullable: true,
    length: 50,
  })
  fisDocCnaeNfs: string;

  @Column('numeric', {
    name: 'valor_outros_tributo_ret',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorOutrosTributoRet: string;

  @Column('numeric', {
    name: 'valor_desconto_cond',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorDescontoCond: string;

  @Column('numeric', {
    name: 'valor_desconto_incond',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorDescontoIncond: string;

  @Column('numeric', {
    name: 'valor_deducao',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorDeducao: string;

  @Column('integer', {
    name: 'qnt_min_pessoa_cot',
    nullable: true,
    default: () => '0',
  })
  qntMinPessoaCot: number | null;

  @Column('date', { name: 'data_valid', nullable: true })
  dataValid: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => FisTributacao, (fisTributacao) => fisTributacao.movItemserv)
  fisTributacaos: FisTributacao[];

  @ManyToOne(() => FisCfop, (fisCfop) => fisCfop.movItemservs)
  @JoinColumn([{ name: 'fis_cfop_id', referencedColumnName: 'id' }])
  fisCfop: FisCfop;

  @ManyToOne(() => GerUmedida, (gerUmedida) => gerUmedida.movItemservs)
  @JoinColumn([{ name: 'ger_umedida_id_conv', referencedColumnName: 'id' }])
  gerUmedidaIdConv: GerUmedida;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerItemserv, (gerItemserv) => gerItemserv.movItemservs)
  @JoinColumn([{ name: 'ger_itemserv_id', referencedColumnName: 'id' }])
  gerItemserv: GerItemserv;

  @ManyToOne(
    () => GerItemservLote,
    (gerItemservLote) => gerItemservLote.movItemservs,
  )
  @JoinColumn([{ name: 'ger_itemserv_lote_id', referencedColumnName: 'id' }])
  gerItemservLote: GerItemservLote;

  @ManyToOne(
    () => GerItemservVar,
    (gerItemservVar) => gerItemservVar.movItemservs,
  )
  @JoinColumn([{ name: 'ger_itemserv_var_id', referencedColumnName: 'id' }])
  gerItemservVar: GerItemservVar;

  @ManyToOne(() => Mov, (mov) => mov.movItemservs)
  @JoinColumn([{ name: 'mov_id', referencedColumnName: 'id' }])
  mov: Mov;

  @OneToMany(() => MovOrigem, (movOrigem) => movOrigem.movItemserv)
  movOrigems: MovOrigem[];

  @OneToMany(() => MovOrigem, (movOrigem) => movOrigem.movItemservIdOrigem)
  movOrigems2: MovOrigem[];

  @OneToMany(() => OpeCentroDest, (opeCentroDest) => opeCentroDest.movItemserv)
  opeCentroDests: OpeCentroDest[];
}
