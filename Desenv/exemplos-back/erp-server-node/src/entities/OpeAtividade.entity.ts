import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { CtbLancDet } from './CtbLancDet.entity';
import { FinPagrecPrevDest } from './FinPagrecPrevDest.entity';
import { GerUmedida } from './GerUmedida.entity';
import { SystemUnit } from './SystemUnit.entity';
import { OpeAtividadeGrupo } from './OpeAtividadeGrupo.entity';
import { OpeAtividadeRelacProd } from './OpeAtividadeRelacProd.entity';
import { OpeCentro2OrdAtiv } from './OpeCentro2OrdAtiv.entity';
import { OpeCentroConfig } from './OpeCentroConfig.entity';
import { OpeCentroDest } from './OpeCentroDest.entity';
import { OpeCentroPrev } from './OpeCentroPrev.entity';
import { OpeCentroRatFator } from './OpeCentroRatFator.entity';
import { OpeCentroRend } from './OpeCentroRend.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_atividade', ['id'], { unique: true })
@Entity('ope_atividade', { schema: 'public' })
export class OpeAtividade extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_atividade', length: 50 })
  siglaAtividade: string;

  @Column('varchar', { name: 'parada', length: 1 })
  parada: string;

  @Column('varchar', {
    name: 'index_bor',
    nullable: true,
    length: 50,
  })
  indexBor: string;

  @Column('numeric', {
    name: 'largura',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  largura: string;

  @Column('varchar', {
    name: 'valida_seq_medicao_trab_centro',
    nullable: true,
    length: 1,
    default: () => "'S'",
  })
  validaSeqMedicaoTrabCentro: string;

  @Column('varchar', {
    name: 'valida_saldo_area_aberta',
    nullable: true,
    length: 1,
    default: () => "'S'",
  })
  validaSaldoAreaAberta: string;

  @Column('varchar', {
    name: 'valida_prev_itemserv',
    nullable: true,
    length: 1,
    default: () => "'S'",
  })
  validaPrevItemserv: string;

  @Column('varchar', {
    name: 'valida_prev_rec',
    nullable: true,
    length: 1,
    default: () => "'S'",
  })
  validaPrevRec: string;

  @Column('varchar', {
    name: 'valida_regra_config',
    nullable: true,
    length: 1,
    default: () => "'S'",
  })
  validaRegraConfig: string;

  @Column('varchar', {
    name: 'valida_tipo_executor',
    nullable: true,
    length: 2,
    default: () => "'SP'",
  })
  validaTipoExecutor: string;

  @Column('varchar', {
    name: 'valida_rec_equip',
    nullable: true,
    length: 1,
    default: () => "'S'",
  })
  validaRecEquip: string;

  @Column('varchar', {
    name: 'valida_rec_pessoa',
    nullable: true,
    length: 1,
    default: () => "'S'",
  })
  validaRecPessoa: string;

  @Column('varchar', {
    name: 'valida_itemserv_i',
    nullable: true,
    length: 1,
    default: () => "'S'",
  })
  validaItemservI: string;

  @Column('varchar', {
    name: 'valida_itemserv_s',
    nullable: true,
    length: 1,
    default: () => "'S'",
  })
  validaItemservS: string;

  @Column('varchar', {
    name: 'valida_tipo_prop_rec_equip',
    nullable: true,
    length: 2,
    default: () => "'SP'",
  })
  validaTipoPropRecEquip: string;

  @Column('varchar', {
    name: 'valida_tipo_prop_rec_pessoa',
    nullable: true,
    length: 2,
    default: () => "'SP'",
  })
  validaTipoPropRecPessoa: string;

  @Column('varchar', {
    name: 'valida_tot_area_acum_per_centro_plan',
    nullable: true,
    length: 1,
    default: () => "'S'",
  })
  validaTotAreaAcumPerCentroPlan: string;

  @Column('varchar', {
    name: 'valida_tot_area_acum_per_centro_exec',
    nullable: true,
    length: 1,
    default: () => "'S'",
  })
  validaTotAreaAcumPerCentroExec: string;

  @Column('varchar', {
    name: 'valida_tot_area_ord_exec',
    nullable: true,
    length: 1,
    default: () => "'S'",
  })
  validaTotAreaOrdExec: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => CtbLancDet, (ctbLancDet) => ctbLancDet.opeAtividade)
  ctbLancDets: CtbLancDet[];

  @OneToMany(
    () => FinPagrecPrevDest,
    (finPagrecPrevDest) => finPagrecPrevDest.opeAtividade,
  )
  finPagrecPrevDests: FinPagrecPrevDest[];

  @ManyToOne(() => GerUmedida, (gerUmedida) => gerUmedida.opeAtividades)
  @JoinColumn([{ name: 'ger_umedida_id', referencedColumnName: 'id' }])
  gerUmedida: GerUmedida;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => OpeAtividadeGrupo,
    (opeAtividadeGrupo) => opeAtividadeGrupo.opeAtividades,
  )
  @JoinColumn([{ name: 'ope_atividade_grupo_id', referencedColumnName: 'id' }])
  opeAtividadeGrupo: OpeAtividadeGrupo;

  @OneToMany(
    () => OpeAtividadeRelacProd,
    (opeAtividadeRelacProd) => opeAtividadeRelacProd.opeAtividade,
  )
  opeAtividadeRelacProds: OpeAtividadeRelacProd[];

  @OneToMany(
    () => OpeAtividadeRelacProd,
    (opeAtividadeRelacProd) => opeAtividadeRelacProd.opeAtividadeIdProd,
  )
  opeAtividadeRelacProds2: OpeAtividadeRelacProd[];

  @OneToMany(
    () => OpeCentro2OrdAtiv,
    (opeCentro2OrdAtiv) => opeCentro2OrdAtiv.opeAtividade,
  )
  opeCentro2OrdAtivs: OpeCentro2OrdAtiv[];

  @OneToMany(
    () => OpeCentroConfig,
    (opeCentroConfig) => opeCentroConfig.opeAtividade,
  )
  opeCentroConfigs: OpeCentroConfig[];

  @OneToMany(() => OpeCentroDest, (opeCentroDest) => opeCentroDest.opeAtividade)
  opeCentroDests: OpeCentroDest[];

  @OneToMany(() => OpeCentroPrev, (opeCentroPrev) => opeCentroPrev.opeAtividade)
  opeCentroPrevs: OpeCentroPrev[];

  @OneToMany(
    () => OpeCentroRatFator,
    (opeCentroRatFator) => opeCentroRatFator.opeAtividade,
  )
  opeCentroRatFators: OpeCentroRatFator[];

  @OneToMany(() => OpeCentroRend, (opeCentroRend) => opeCentroRend.opeAtividade)
  opeCentroRends: OpeCentroRend[];
}
