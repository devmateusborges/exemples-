import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { FisCest } from './FisCest.entity';
import { FisNbs } from './FisNbs.entity';
import { FisNcm } from './FisNcm.entity';
import { GerUmedida } from './GerUmedida.entity';
import { SystemUnit } from './SystemUnit.entity';
import { CtbComp } from './CtbComp.entity';
import { GerItemservSubgrupo } from './GerItemservSubgrupo.entity';
import { GerItemservBarra } from './GerItemservBarra.entity';
import { GerItemservCompos } from './GerItemservCompos.entity';
import { GerItemservLocal } from './GerItemservLocal.entity';
import { GerItemservPessoa } from './GerItemservPessoa.entity';
import { MovCotacao } from './MovCotacao.entity';
import { MovCotacaoAnal } from './MovCotacaoAnal.entity';
import { MovEstNivel } from './MovEstNivel.entity';
import { MovItemserv } from './MovItemserv.entity';
import { OpeCentro2Area } from './OpeCentro2Area.entity';
import { OpeCentro2MovMedia } from './OpeCentro2MovMedia.entity';
import { OpeCentro2OrdItemserv } from './OpeCentro2OrdItemserv.entity';
import { OpeCentroConfig } from './OpeCentroConfig.entity';
import { OpeCentroPrevDest } from './OpeCentroPrevDest.entity';
import { OpeCentroRendFator } from './OpeCentroRendFator.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_itemserv', ['id'], { unique: true })
@Entity('ger_itemserv', { schema: 'public' })
export class GerItemserv extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', {
    name: 'referencia1',
    nullable: true,
    length: 50,
  })
  referencia1: string;

  @Column('varchar', {
    name: 'referencia2',
    nullable: true,
    length: 50,
  })
  referencia2: string;

  @Column('varchar', {
    name: 'referencia3',
    nullable: true,
    length: 50,
  })
  referencia3: string;

  @Column('varchar', { name: 'tipo', length: 1 })
  tipo: string;

  @Column('varchar', { name: 'tipo_ctb_comp', length: 1 })
  tipoCtbComp: string;

  @Column('integer', { name: 'origem_fiscal' })
  origemFiscal: number;

  @Column('varchar', {
    name: 'nome_alternativo',
    nullable: true,
    length: 100,
  })
  nomeAlternativo: string;

  @Column('varchar', {
    name: 'tipo_composicao',
    nullable: true,
    length: 1,
    default: () => "'N'",
  })
  tipoComposicao: string;

  @Column('varchar', {
    name: 'fis_sigla_servico',
    nullable: true,
    length: 50,
  })
  fisSiglaServico: string;

  @Column('varchar', {
    name: 'fis_doc_cnae_nfs',
    nullable: true,
    length: 50,
  })
  fisDocCnaeNfs: string;

  @Column('varchar', {
    name: 'fis_sigla_servico_municipio',
    nullable: true,
    length: 50,
  })
  fisSiglaServicoMunicipio: string;

  @Column('varchar', {
    name: 'sigla_itemserv',
    nullable: true,
    length: 15,
  })
  siglaItemserv: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => FisCest, (fisCest) => fisCest.gerItemservs)
  @JoinColumn([{ name: 'fis_cest_id', referencedColumnName: 'id' }])
  fisCest: FisCest;

  @ManyToOne(() => FisNbs, (fisNbs) => fisNbs.gerItemservs)
  @JoinColumn([{ name: 'fis_nbs_id', referencedColumnName: 'id' }])
  fisNbs: FisNbs;

  @ManyToOne(() => FisNcm, (fisNcm) => fisNcm.gerItemservs)
  @JoinColumn([{ name: 'fis_ncm_id', referencedColumnName: 'id' }])
  fisNcm: FisNcm;

  @ManyToOne(() => GerUmedida, (gerUmedida) => gerUmedida.gerItemservs)
  @JoinColumn([{ name: 'ger_umedida_id', referencedColumnName: 'id' }])
  gerUmedida: GerUmedida;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => CtbComp, (ctbComp) => ctbComp.gerItemservs)
  @JoinColumn([{ name: 'ctb_comp_id', referencedColumnName: 'id' }])
  ctbComp: CtbComp;

  @ManyToOne(
    () => GerItemservSubgrupo,
    (gerItemservSubgrupo) => gerItemservSubgrupo.gerItemservs,
  )
  @JoinColumn([
    { name: 'ger_itemserv_subgrupo_id', referencedColumnName: 'id' },
  ])
  gerItemservSubgrupo: GerItemservSubgrupo;

  @OneToMany(
    () => GerItemservBarra,
    (gerItemservBarra) => gerItemservBarra.gerItemserv,
  )
  gerItemservBarras: GerItemservBarra[];

  @OneToMany(
    () => GerItemservCompos,
    (gerItemservCompos) => gerItemservCompos.gerItemservIdDe,
  )
  gerItemservCompos: GerItemservCompos[];

  @OneToMany(
    () => GerItemservCompos,
    (gerItemservCompos) => gerItemservCompos.gerItemservIdPara,
  )
  gerItemservCompos2: GerItemservCompos[];

  @OneToMany(
    () => GerItemservLocal,
    (gerItemservLocal) => gerItemservLocal.gerItemserv,
  )
  gerItemservLocals: GerItemservLocal[];

  @OneToMany(
    () => GerItemservPessoa,
    (gerItemservPessoa) => gerItemservPessoa.gerItemserv,
  )
  gerItemservPessoas: GerItemservPessoa[];

  @OneToMany(() => MovCotacao, (movCotacao) => movCotacao.gerItemserv)
  movCotacaos: MovCotacao[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.gerItemserv,
  )
  movCotacaoAnals: MovCotacaoAnal[];

  @OneToMany(() => MovEstNivel, (movEstNivel) => movEstNivel.gerItemserv)
  movEstNivels: MovEstNivel[];

  @OneToMany(() => MovItemserv, (movItemserv) => movItemserv.gerItemserv)
  movItemservs: MovItemserv[];

  @OneToMany(
    () => OpeCentro2Area,
    (opeCentro2Area) => opeCentro2Area.gerItemserv,
  )
  opeCentro2Areas: OpeCentro2Area[];

  @OneToMany(
    () => OpeCentro2Area,
    (opeCentro2Area) => opeCentro2Area.gerItemservIdUlt,
  )
  opeCentro2Areas2: OpeCentro2Area[];

  @OneToMany(
    () => OpeCentro2MovMedia,
    (opeCentro2MovMedia) => opeCentro2MovMedia.gerItemserv,
  )
  opeCentro2MovMedias: OpeCentro2MovMedia[];

  @OneToMany(
    () => OpeCentro2OrdItemserv,
    (opeCentro2OrdItemserv) => opeCentro2OrdItemserv.gerItemserv,
  )
  opeCentro2OrdItemservs: OpeCentro2OrdItemserv[];

  @OneToMany(
    () => OpeCentroConfig,
    (opeCentroConfig) => opeCentroConfig.gerItemserv,
  )
  opeCentroConfigs: OpeCentroConfig[];

  @OneToMany(
    () => OpeCentroPrevDest,
    (opeCentroPrevDest) => opeCentroPrevDest.gerItemserv,
  )
  opeCentroPrevDests: OpeCentroPrevDest[];

  @OneToMany(
    () => OpeCentroRendFator,
    (opeCentroRendFator) => opeCentroRendFator.gerItemserv,
  )
  opeCentroRendFators: OpeCentroRendFator[];
}
