import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { FisTributo } from './FisTributo.entity';
import { SystemUnit } from './SystemUnit.entity';
import { FinPagrec } from './FinPagrec.entity';
import { GerPessoaEndereco } from './GerPessoaEndereco.entity';
import { Mov } from './Mov.entity';
import { MovItemserv } from './MovItemserv.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fis_tributacao', ['id'], { unique: true })
@Entity('fis_tributacao', { schema: 'public' })
export class FisTributacao extends BaseEntity {
  @Column('varchar', { name: 'cst', length: 4 })
  cst: string;

  @Column('integer', { name: 'modalidade_base_calc' })
  modalidadeBaseCalc: number;

  @Column('numeric', {
    name: 'valor_base_calc',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorBaseCalc: string;

  @Column('numeric', {
    name: 'perc_aliquota',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  percAliquota: string;

  @Column('numeric', {
    name: 'valor_imposto',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorImposto: string;

  @Column('numeric', {
    name: 'valor_base_calc_isento',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorBaseCalcIsento: string;

  @Column('numeric', {
    name: 'perc_aliquota_isento',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  percAliquotaIsento: string;

  @Column('numeric', {
    name: 'valor_imposto_isento',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorImpostoIsento: string;

  @Column('numeric', {
    name: 'valor_base_calc_st',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorBaseCalcSt: string;

  @Column('numeric', {
    name: 'margem_agregada_st',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  margemAgregadaSt: string;

  @Column('numeric', {
    name: 'perc_aliquota_st',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  percAliquotaSt: string;

  @Column('numeric', {
    name: 'valor_imposto_st',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorImpostoSt: string;

  @Column('numeric', {
    name: 'perc_reducao_base_calc',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  percReducaoBaseCalc: string;

  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column('numeric', {
    name: 'valor_imposto_operacao',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorImpostoOperacao: string;

  @Column('numeric', {
    name: 'valor_imposto_diferido',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorImpostoDiferido: string;

  @Column('numeric', {
    name: 'perc_credito_sn',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  percCreditoSn: string;

  @Column('numeric', {
    name: 'valor_credito_sn',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorCreditoSn: string;

  @Column('numeric', {
    name: 'valor_base_calc_fcp',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorBaseCalcFcp: string;

  @Column('numeric', {
    name: 'perc_aliquota_fcp',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  percAliquotaFcp: string;

  @Column('numeric', {
    name: 'valor_imposto_fcp',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorImpostoFcp: string;

  @Column('numeric', {
    name: 'valor_base_calc_fcp_st',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorBaseCalcFcpSt: string;

  @Column('numeric', {
    name: 'perc_aliquota_fcp_st',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  percAliquotaFcpSt: string;

  @Column('numeric', {
    name: 'valor_imposto_fcp_st',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorImpostoFcpSt: string;

  @Column('numeric', {
    name: 'perc_uf_fim_fcp',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  percUfFimFcp: string;

  @Column('numeric', {
    name: 'valor_total_uf_fim_fcp',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorTotalUfFimFcp: string;

  @Column('numeric', {
    name: 'valor_imposto_fcp_st_ret',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorImpostoFcpStRet: string;

  @Column('numeric', {
    name: 'valor_base_calc_fcp_st_ret',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorBaseCalcFcpStRet: string;

  @Column('numeric', {
    name: 'perc_aliquota_fcp_st_ret',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  percAliquotaFcpStRet: string;

  @Column('numeric', {
    name: 'valor_imposto_desonerado',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorImpostoDesonerado: string;

  @Column('integer', { name: 'motivo_imposto_desonerado', nullable: true })
  motivoImpostoDesonerado: number | null;

  @Column('integer', { name: 'modalidade_base_calc_st', nullable: true })
  modalidadeBaseCalcSt: number | null;

  @Column('numeric', {
    name: 'valor_base_calc_st_ret',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorBaseCalcStRet: string;

  @Column('numeric', {
    name: 'valor_imposto_st_ret',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorImpostoStRet: string;

  @Column('numeric', {
    name: 'perc_aliquota_red_base_calc_efetiva',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  percAliquotaRedBaseCalcEfetiva: string;

  @Column('numeric', {
    name: 'valor_base_calc_efetiva',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorBaseCalcEfetiva: string;

  @Column('numeric', {
    name: 'perc_aliquota_efetiva',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  percAliquotaEfetiva: string;

  @Column('numeric', {
    name: 'valor_imposto_efetiva',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorImpostoEfetiva: string;

  @Column('numeric', {
    name: 'perc_aliquota_credito',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  percAliquotaCredito: string;

  @Column('numeric', {
    name: 'valor_imposto_credito',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorImpostoCredito: string;

  @Column('numeric', {
    name: 'valor_base_calc_uf_fim',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorBaseCalcUfFim: string;

  @Column('numeric', {
    name: 'perc_interna_uf_fim',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  percInternaUfFim: string;

  @Column('numeric', {
    name: 'perc_interestadual_uf_fim',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  percInterestadualUfFim: string;

  @Column('numeric', {
    name: 'perc_partilha_uf_fim',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  percPartilhaUfFim: string;

  @Column('numeric', {
    name: 'valor_partilha_uf_fim',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorPartilhaUfFim: string;

  @Column('numeric', {
    name: 'valor_partilha_uf_inicio',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorPartilhaUfInicio: string;

  @Column('numeric', {
    name: 'valor_imposto_substituto',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  valorImpostoSubstituto: string;

  @Column('date', { name: 'data_valid', nullable: true })
  dataValid: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => FisTributo, (fisTributo) => fisTributo.fisTributacaos)
  @JoinColumn([{ name: 'fis_tributo_id', referencedColumnName: 'id' }])
  fisTributo: FisTributo;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => FinPagrec, (finPagrec) => finPagrec.fisTributacaos)
  @JoinColumn([{ name: 'fin_pagrec_id', referencedColumnName: 'id' }])
  finPagrec: FinPagrec;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.fisTributacaos,
  )
  @JoinColumn([{ name: 'ger_pessoa_endereco_id', referencedColumnName: 'id' }])
  gerPessoaEndereco: GerPessoaEndereco;

  @ManyToOne(() => Mov, (mov) => mov.fisTributacaos)
  @JoinColumn([{ name: 'mov_id', referencedColumnName: 'id' }])
  mov: Mov;

  @ManyToOne(() => MovItemserv, (movItemserv) => movItemserv.fisTributacaos)
  @JoinColumn([{ name: 'mov_itemserv_id', referencedColumnName: 'id' }])
  movItemserv: MovItemserv;
}
