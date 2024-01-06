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
import { CtbComp } from './CtbComp.entity';
import { GerMarcaModelo } from './GerMarcaModelo.entity';
import { GerPessoaEndereco } from './GerPessoaEndereco.entity';
import { OpeCentro1 } from './OpeCentro1.entity';
import { OpeCentroRatTipo } from './OpeCentroRatTipo.entity';
import { OpeCentroSubgrupo } from './OpeCentroSubgrupo.entity';
import { OpeRegiao } from './OpeRegiao.entity';
import { OpeCentro2Area } from './OpeCentro2Area.entity';
import { OpeCentro2Equip } from './OpeCentro2Equip.entity';
import { OpeCentro2Estoque } from './OpeCentro2Estoque.entity';
import { OpeCentro2MovMedia } from './OpeCentro2MovMedia.entity';
import { OpeCentro2Ord } from './OpeCentro2Ord.entity';
import { OpeCentro2OrdDest } from './OpeCentro2OrdDest.entity';
import { OpeCentro2OrdRec } from './OpeCentro2OrdRec.entity';
import { OpeCentro2ParamPer } from './OpeCentro2ParamPer.entity';
import { OpeCentro2Pessoa } from './OpeCentro2Pessoa.entity';
import { OpeCentroConfig } from './OpeCentroConfig.entity';
import { OpeCentroDest } from './OpeCentroDest.entity';
import { OpeCentroPrev } from './OpeCentroPrev.entity';
import { OpeCentroPrevDest } from './OpeCentroPrevDest.entity';
import { OpeCentroRatFator } from './OpeCentroRatFator.entity';
import { OpeCentroRendFator } from './OpeCentroRendFator.entity';
import { OpeOcorMovDest } from './OpeOcorMovDest.entity';
import { OpeOcorPrev } from './OpeOcorPrev.entity';
import { SystemDocument } from './SystemDocument.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro2', ['id'], { unique: true })
@Entity('ope_centro2', { schema: 'public' })
export class OpeCentro2 extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_centro2', length: 50 })
  siglaCentro2: string;

  @Column('varchar', { name: 'utiliza_compart', length: 1 })
  utilizaCompart: string;

  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column('varchar', { name: 'tipo_prop', nullable: true, length: 1 })
  tipoProp: string;

  @Column('varchar', {
    name: 'tipo_destinacao',
    nullable: true,
    length: 1,
  })
  tipoDestinacao: string;

  @Column('varchar', {
    name: 'tipo_ctb_comp',
    nullable: true,
    length: 1,
  })
  tipoCtbComp: string;

  @Column('varchar', {
    name: 'medicao_trab_centro',
    nullable: true,
    length: 1,
    default: () => "'S'",
  })
  medicaoTrabCentro: string;

  @Column('varchar', {
    name: 'valida_seq_medicao_trab_centro',
    nullable: true,
    length: 1,
    default: () => "'S'",
  })
  validaSeqMedicaoTrabCentro: string;

  @Column('date', { name: 'data_valid', nullable: true })
  dataValid: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => CtbLancDet, (ctbLancDet) => ctbLancDet.opeCentro2)
  ctbLancDets: CtbLancDet[];

  @OneToMany(
    () => FinPagrecPrevDest,
    (finPagrecPrevDest) => finPagrecPrevDest.opeCentro2IdDest,
  )
  finPagrecPrevDests: FinPagrecPrevDest[];

  @ManyToOne(() => GerUmedida, (gerUmedida) => gerUmedida.opeCentros)
  @JoinColumn([{ name: 'ger_umedida_id', referencedColumnName: 'id' }])
  gerUmedida: GerUmedida;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => CtbComp, (ctbComp) => ctbComp.opeCentros2)
  @JoinColumn([{ name: 'ctb_comp_id', referencedColumnName: 'id' }])
  ctbComp: CtbComp;

  @ManyToOne(
    () => GerMarcaModelo,
    (gerMarcaModelo) => gerMarcaModelo.opeCentros,
  )
  @JoinColumn([{ name: 'ger_marca_modelo_id', referencedColumnName: 'id' }])
  gerMarcaModelo: GerMarcaModelo;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.opeCentros,
  )
  @JoinColumn([{ name: 'ger_pessoa_endereco_id', referencedColumnName: 'id' }])
  gerPessoaEndereco: GerPessoaEndereco;

  @ManyToOne(() => OpeCentro1, (opeCentro1) => opeCentro1.opeCentros)
  @JoinColumn([{ name: 'ope_centro1_id', referencedColumnName: 'id' }])
  opeCentro1: OpeCentro1;

  @ManyToOne(
    () => OpeCentroRatTipo,
    (opeCentroRatTipo) => opeCentroRatTipo.opeCentros,
  )
  @JoinColumn([{ name: 'ope_centro_rat_tipo_id', referencedColumnName: 'id' }])
  opeCentroRatTipo: OpeCentroRatTipo;

  @ManyToOne(
    () => OpeCentroSubgrupo,
    (opeCentroSubgrupo) => opeCentroSubgrupo.opeCentros,
  )
  @JoinColumn([{ name: 'ope_centro_subgrupo_id', referencedColumnName: 'id' }])
  opeCentroSubgrupo: OpeCentroSubgrupo;

  @ManyToOne(() => OpeRegiao, (opeRegiao) => opeRegiao.opeCentros)
  @JoinColumn([{ name: 'ope_regiao_id', referencedColumnName: 'id' }])
  opeRegiao: OpeRegiao;

  @OneToMany(
    () => OpeCentro2Area,
    (opeCentro2Area) => opeCentro2Area.opeCentro2,
  )
  opeCentro2Areas: OpeCentro2Area[];

  @OneToMany(
    () => OpeCentro2Equip,
    (opeCentro2Equip) => opeCentro2Equip.opeCentro2,
  )
  opeCentro2Equips: OpeCentro2Equip[];

  @OneToMany(
    () => OpeCentro2Estoque,
    (opeCentro2Estoque) => opeCentro2Estoque.opeCentro2,
  )
  opeCentro2Estoques: OpeCentro2Estoque[];

  @OneToMany(
    () => OpeCentro2MovMedia,
    (opeCentro2MovMedia) => opeCentro2MovMedia.opeCentro2,
  )
  opeCentro2MovMedias: OpeCentro2MovMedia[];

  @OneToMany(() => OpeCentro2Ord, (opeCentro2Ord) => opeCentro2Ord.opeCentro2)
  opeCentro2Ords: OpeCentro2Ord[];

  @OneToMany(
    () => OpeCentro2OrdDest,
    (opeCentro2OrdDest) => opeCentro2OrdDest.opeCentro2IdDest,
  )
  opeCentro2OrdDests: OpeCentro2OrdDest[];

  @OneToMany(
    () => OpeCentro2OrdRec,
    (opeCentro2OrdRec) => opeCentro2OrdRec.opeCentro2,
  )
  opeCentro2OrdRecs: OpeCentro2OrdRec[];

  @OneToMany(
    () => OpeCentro2OrdRec,
    (opeCentro2OrdRec) => opeCentro2OrdRec.opeCentro2IdImp,
  )
  opeCentro2OrdRecs2: OpeCentro2OrdRec[];

  @OneToMany(
    () => OpeCentro2ParamPer,
    (opeCentro2ParamPer) => opeCentro2ParamPer.opeCentro2,
  )
  opeCentro2ParamPers: OpeCentro2ParamPer[];

  @OneToMany(
    () => OpeCentro2Pessoa,
    (opeCentro2Pessoa) => opeCentro2Pessoa.opeCentro2,
  )
  opeCentro2Pessoas: OpeCentro2Pessoa[];

  @OneToMany(
    () => OpeCentroConfig,
    (opeCentroConfig) => opeCentroConfig.opeCentro2,
  )
  opeCentroConfigs: OpeCentroConfig[];

  @OneToMany(() => OpeCentroDest, (opeCentroDest) => opeCentroDest.opeCentro2)
  opeCentroDests: OpeCentroDest[];

  @OneToMany(
    () => OpeCentroDest,
    (opeCentroDest) => opeCentroDest.opeCentro2IdDest,
  )
  opeCentroDests2: OpeCentroDest[];

  @OneToMany(() => OpeCentroPrev, (opeCentroPrev) => opeCentroPrev.opeCentro2)
  opeCentroPrevs: OpeCentroPrev[];

  @OneToMany(
    () => OpeCentroPrevDest,
    (opeCentroPrevDest) => opeCentroPrevDest.opeCentro2,
  )
  opeCentroPrevDests: OpeCentroPrevDest[];

  @OneToMany(
    () => OpeCentroRatFator,
    (opeCentroRatFator) => opeCentroRatFator.opeCentro2,
  )
  opeCentroRatFators: OpeCentroRatFator[];

  @OneToMany(
    () => OpeCentroRendFator,
    (opeCentroRendFator) => opeCentroRendFator.opeCentro2,
  )
  opeCentroRendFators: OpeCentroRendFator[];

  @OneToMany(
    () => OpeOcorMovDest,
    (opeOcorMovDest) => opeOcorMovDest.opeCentro2,
  )
  opeOcorMovDests: OpeOcorMovDest[];

  @OneToMany(() => OpeOcorPrev, (opeOcorPrev) => opeOcorPrev.opeCentro2)
  opeOcorPrevs: OpeOcorPrev[];

  @OneToMany(
    () => SystemDocument,
    (systemDocument) => systemDocument.opeCentro2,
  )
  systemDocuments: SystemDocument[];
}
