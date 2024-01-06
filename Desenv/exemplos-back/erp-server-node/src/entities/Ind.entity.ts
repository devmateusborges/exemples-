import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { GerUmedida } from './GerUmedida.entity';
import { SystemUnit } from './SystemUnit.entity';
import { IndRelac } from './IndRelac.entity';
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
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ind', ['id'], { unique: true })
@Entity('ind', { schema: 'public' })
export class Ind extends BaseEntity {
  @Column('varchar', {
    name: 'sigla_ind',
    nullable: true,
    length: 50,
  })
  siglaInd: string;

  @Column('varchar', { name: 'nome', nullable: true, length: 100 })
  nome: string;

  @Column('integer', { name: 'casas_dec', nullable: true })
  casasDec: number | null;

  @Column('varchar', {
    name: 'campo_ordenacao',
    nullable: true,
    length: 50,
  })
  campoOrdenacao: string;

  @Column('integer', { name: 'metodo_ordenacao', nullable: true })
  metodoOrdenacao: number | null;

  @Column('integer', { name: 'totalizador_atributo', nullable: true })
  totalizadorAtributo: number | null;

  @Column('varchar', {
    name: 'exibir_media_real',
    nullable: true,
    length: 1,
  })
  exibirMediaReal: string;

  @Column('varchar', {
    name: 'exibir_media_meta',
    nullable: true,
    length: 1,
  })
  exibirMediaMeta: string;

  @Column('varchar', {
    name: 'exibir_dia',
    nullable: true,
    length: 1,
  })
  exibirDia: string;

  @Column('varchar', {
    name: 'exibir_semana',
    nullable: true,
    length: 1,
  })
  exibirSemana: string;

  @Column('varchar', {
    name: 'exibir_quinzena',
    nullable: true,
    length: 1,
  })
  exibirQuinzena: string;

  @Column('varchar', {
    name: 'exibir_mes',
    nullable: true,
    length: 1,
  })
  exibirMes: string;

  @Column('varchar', {
    name: 'exibir_bimestre',
    nullable: true,
    length: 1,
  })
  exibirBimestre: string;

  @Column('varchar', {
    name: 'exibir_trimestre',
    nullable: true,
    length: 1,
  })
  exibirTrimestre: string;

  @Column('varchar', {
    name: 'exibir_quadrimestre',
    nullable: true,
    length: 1,
  })
  exibirQuadrimestre: string;

  @Column('varchar', {
    name: 'exibir_semestre',
    nullable: true,
    length: 1,
  })
  exibirSemestre: string;

  @Column('varchar', {
    name: 'exibir_ano',
    nullable: true,
    length: 1,
  })
  exibirAno: string;

  @Column('varchar', {
    name: 'acumular_semana',
    nullable: true,
    length: 1,
  })
  acumularSemana: string;

  @Column('varchar', {
    name: 'acumular_quinzena',
    nullable: true,
    length: 1,
  })
  acumularQuinzena: string;

  @Column('varchar', {
    name: 'acumular_mes',
    nullable: true,
    length: 1,
  })
  acumularMes: string;

  @Column('varchar', {
    name: 'acumular_bimestre',
    nullable: true,
    length: 1,
  })
  acumularBimestre: string;

  @Column('varchar', {
    name: 'acumular_trimestre',
    nullable: true,
    length: 1,
  })
  acumularTrimestre: string;

  @Column('varchar', {
    name: 'acumular_quadrimestre',
    nullable: true,
    length: 1,
  })
  acumularQuadrimestre: string;

  @Column('varchar', {
    name: 'acumular_semestre',
    nullable: true,
    length: 1,
  })
  acumularSemestre: string;

  @Column('varchar', {
    name: 'acumular_ano',
    nullable: true,
    length: 1,
  })
  acumularAno: string;

  @Column('integer', { name: 'tipo_acumulo', nullable: true })
  tipoAcumulo: number | null;

  @Column('integer', { name: 'grafico_tipo_atributo', nullable: true })
  graficoTipoAtributo: number | null;

  @Column('varchar', {
    name: 'grafico_valor_vazio_zero',
    nullable: true,
    length: 1,
  })
  graficoValorVazioZero: string;

  @Column('integer', { name: 'grafico_tipo_ind', nullable: true })
  graficoTipoInd: number | null;

  @Column('integer', { name: 'tipo_meta', nullable: true, default: () => '1' })
  tipoMeta: number | null;

  @Column('double precision', {
    name: 'faixa_meta_vr_01',
    nullable: true,
    precision: 53,
    default: () => '0',
  })
  faixaMetaVr_01: number | null;

  @Column('double precision', {
    name: 'faixa_meta_vr_02',
    nullable: true,
    precision: 53,
    default: () => '0',
  })
  faixaMetaVr_02: number | null;

  @Column('double precision', {
    name: 'faixa_meta_vr_03',
    nullable: true,
    precision: 53,
    default: () => '0',
  })
  faixaMetaVr_03: number | null;

  @Column('double precision', {
    name: 'faixa_meta_vr_04',
    nullable: true,
    precision: 53,
    default: () => '0',
  })
  faixaMetaVr_04: number | null;

  @Column('double precision', {
    name: 'faixa_meta_vr_05',
    nullable: true,
    precision: 53,
    default: () => '0',
  })
  faixaMetaVr_05: number | null;

  @Column('varchar', {
    name: 'faixa_meta_cor_01',
    nullable: true,
    length: 50,
    default: () => "'#ffffff'",
  })
  faixaMetaCor_01: string;

  @Column('varchar', {
    name: 'faixa_meta_cor_02',
    nullable: true,
    length: 50,
    default: () => "'#ffffff'",
  })
  faixaMetaCor_02: string;

  @Column('varchar', {
    name: 'faixa_meta_cor_03',
    nullable: true,
    length: 50,
    default: () => "'#ffffff'",
  })
  faixaMetaCor_03: string;

  @Column('varchar', {
    name: 'faixa_meta_cor_04',
    nullable: true,
    length: 50,
    default: () => "'#ffffff'",
  })
  faixaMetaCor_04: string;

  @Column('varchar', {
    name: 'faixa_meta_cor_05',
    nullable: true,
    length: 50,
    default: () => "'#ffffff'",
  })
  faixaMetaCor_05: string;

  @Column('varchar', {
    name: 'ativo',
    nullable: true,
    length: 1,
    default: () => "'S'",
  })
  ativo: string;

  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column('double precision', {
    name: 'qnt_dia_hist_ant',
    nullable: true,
    precision: 53,
    default: () => '30',
  })
  qntDiaHistAnt: number | null;

  @Column('double precision', {
    name: 'qnt_dia_hist_prox',
    nullable: true,
    precision: 53,
    default: () => '2',
  })
  qntDiaHistProx: number | null;

  @Column('double precision', {
    name: 'qnt_semana_hist_ant',
    nullable: true,
    precision: 53,
    default: () => '8',
  })
  qntSemanaHistAnt: number | null;

  @Column('double precision', {
    name: 'qnt_semana_hist_prox',
    nullable: true,
    precision: 53,
    default: () => '2',
  })
  qntSemanaHistProx: number | null;

  @Column('double precision', {
    name: 'qnt_quinzena_hist_ant',
    nullable: true,
    precision: 53,
    default: () => '6',
  })
  qntQuinzenaHistAnt: number | null;

  @Column('double precision', {
    name: 'qnt_quinzena_hist_prox',
    nullable: true,
    precision: 53,
    default: () => '2',
  })
  qntQuinzenaHistProx: number | null;

  @Column('double precision', {
    name: 'qnt_mes_hist_ant',
    nullable: true,
    precision: 53,
    default: () => '12',
  })
  qntMesHistAnt: number | null;

  @Column('double precision', {
    name: 'qnt_mes_hist_prox',
    nullable: true,
    precision: 53,
    default: () => '2',
  })
  qntMesHistProx: number | null;

  @Column('double precision', {
    name: 'qnt_bimestre_hist_ant',
    nullable: true,
    precision: 53,
    default: () => '6',
  })
  qntBimestreHistAnt: number | null;

  @Column('double precision', {
    name: 'qnt_bimestre_hist_prox',
    nullable: true,
    precision: 53,
    default: () => '2',
  })
  qntBimestreHistProx: number | null;

  @Column('double precision', {
    name: 'qnt_trimestre_hist_ant',
    nullable: true,
    precision: 53,
    default: () => '4',
  })
  qntTrimestreHistAnt: number | null;

  @Column('double precision', {
    name: 'qnt_trimestre_hist_prox',
    nullable: true,
    precision: 53,
    default: () => '2',
  })
  qntTrimestreHistProx: number | null;

  @Column('double precision', {
    name: 'qnt_quadrimestre_hist_ant',
    nullable: true,
    precision: 53,
    default: () => '4',
  })
  qntQuadrimestreHistAnt: number | null;

  @Column('double precision', {
    name: 'qnt_quadrimestre_hist_prox',
    nullable: true,
    precision: 53,
    default: () => '2',
  })
  qntQuadrimestreHistProx: number | null;

  @Column('double precision', {
    name: 'qnt_semestre_hist_ant',
    nullable: true,
    precision: 53,
    default: () => '6',
  })
  qntSemestreHistAnt: number | null;

  @Column('double precision', {
    name: 'qnt_semestre_hist_prox',
    nullable: true,
    precision: 53,
    default: () => '2',
  })
  qntSemestreHistProx: number | null;

  @Column('double precision', {
    name: 'qnt_ano_hist_ant',
    nullable: true,
    precision: 53,
    default: () => '6',
  })
  qntAnoHistAnt: number | null;

  @Column('double precision', {
    name: 'qnt_ano_hist_prox',
    nullable: true,
    precision: 53,
    default: () => '2',
  })
  qntAnoHistProx: number | null;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => GerUmedida, (gerUmedida) => gerUmedida.inds)
  @JoinColumn([{ name: 'ger_umedida_id', referencedColumnName: 'id' }])
  gerUmedida: GerUmedida;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => Ind, (ind) => ind.inds)
  @JoinColumn([{ name: 'ind_id_ponderacao', referencedColumnName: 'id' }])
  indIdPonderacao: Ind;

  @OneToMany(() => Ind, (ind) => ind.indIdPonderacao)
  inds: Ind[];

  @OneToMany(() => IndRelac, (indRelac) => indRelac.ind)
  indRelacs: IndRelac[];

  @OneToMany(() => IndRelac, (indRelac) => indRelac.indIdRelac)
  indRelacs2: IndRelac[];

  @OneToMany(() => IndVrAno, (indVrAno) => indVrAno.ind)
  indVrAnos: IndVrAno[];

  @OneToMany(() => IndVrBimestre, (indVrBimestre) => indVrBimestre.ind)
  indVrBimestres: IndVrBimestre[];

  @OneToMany(() => IndVrDia, (indVrDia) => indVrDia.ind)
  indVrDias: IndVrDia[];

  @OneToMany(() => IndVrMes, (indVrMes) => indVrMes.ind)
  indVrMes: IndVrMes[];

  @OneToMany(() => IndVrMeta, (indVrMeta) => indVrMeta.ind)
  indVrMetas: IndVrMeta[];

  @OneToMany(
    () => IndVrQuadrimestre,
    (indVrQuadrimestre) => indVrQuadrimestre.ind,
  )
  indVrQuadrimestres: IndVrQuadrimestre[];

  @OneToMany(() => IndVrQuinzena, (indVrQuinzena) => indVrQuinzena.ind)
  indVrQuinzenas: IndVrQuinzena[];

  @OneToMany(() => IndVrSemana, (indVrSemana) => indVrSemana.ind)
  indVrSemanas: IndVrSemana[];

  @OneToMany(() => IndVrSemestre, (indVrSemestre) => indVrSemestre.ind)
  indVrSemestres: IndVrSemestre[];

  @OneToMany(() => IndVrTrimestre, (indVrTrimestre) => indVrTrimestre.ind)
  indVrTrimestres: IndVrTrimestre[];
}
