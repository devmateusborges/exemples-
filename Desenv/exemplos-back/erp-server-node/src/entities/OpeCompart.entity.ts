import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { OpeCentro2MovMedia } from './OpeCentro2MovMedia.entity';
import { OpeCentro2OrdRec } from './OpeCentro2OrdRec.entity';
import { OpeCentroConfig } from './OpeCentroConfig.entity';
import { OpeCentroDest } from './OpeCentroDest.entity';
import { SystemUnit } from './SystemUnit.entity';
import { OpeCompartStatus } from './OpeCompartStatus.entity';
import { OpeCompartSubgrupo } from './OpeCompartSubgrupo.entity';
import { OpeCompartItemserv } from './OpeCompartItemserv.entity';
import { OpeOcorCompartMovDet } from './OpeOcorCompartMovDet.entity';
import { OpeOcorMovDest } from './OpeOcorMovDest.entity';
import { OpeOcorPrev } from './OpeOcorPrev.entity';
import { SystemDocument } from './SystemDocument.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_compart', ['id'], { unique: true })
@Entity('ope_compart', { schema: 'public' })
export class OpeCompart extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_compart', length: 50 })
  siglaCompart: string;

  @Column('numeric', {
    name: 'capacidade',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  capacidade: string;

  @Column('varchar', { name: 'valida_itemserv', length: 1 })
  validaItemserv: string;

  @Column('varchar', {
    name: 'medicao_trab_centro',
    length: 1,
    default: () => "'N'",
  })
  medicaoTrabCentro: string;

  @Column('varchar', {
    name: 'data_aquisicao',
    nullable: true,
    length: 255,
  })
  dataAquisicao: string;

  @Column('varchar', {
    name: 'data_baixa',
    nullable: true,
    length: 255,
  })
  dataBaixa: string;

  @Column('date', { name: 'data_status', nullable: true })
  dataStatus: string;

  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column('numeric', {
    name: 'valor_aquisicao',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valorAquisicao: string;

  @Column('varchar', {
    name: 'numero_serie',
    nullable: true,
    length: 100,
  })
  numeroSerie: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => OpeCentro2MovMedia,
    (opeCentro2MovMedia) => opeCentro2MovMedia.opeCompart,
  )
  opeCentro2MovMedias: OpeCentro2MovMedia[];

  @OneToMany(
    () => OpeCentro2OrdRec,
    (opeCentro2OrdRec) => opeCentro2OrdRec.opeCompart,
  )
  opeCentro2OrdRecs: OpeCentro2OrdRec[];

  @OneToMany(
    () => OpeCentroConfig,
    (opeCentroConfig) => opeCentroConfig.opeCompart,
  )
  opeCentroConfigs: OpeCentroConfig[];

  @OneToMany(() => OpeCentroDest, (opeCentroDest) => opeCentroDest.opeCompart)
  opeCentroDests: OpeCentroDest[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => OpeCompartStatus,
    (opeCompartStatus) => opeCompartStatus.opeComparts,
  )
  @JoinColumn([{ name: 'ope_compart_status_id', referencedColumnName: 'id' }])
  opeCompartStatus: OpeCompartStatus;

  @ManyToOne(
    () => OpeCompartSubgrupo,
    (opeCompartSubgrupo) => opeCompartSubgrupo.opeComparts,
  )
  @JoinColumn([{ name: 'ope_compart_subgrupo_id', referencedColumnName: 'id' }])
  opeCompartSubgrupo: OpeCompartSubgrupo;

  @OneToMany(
    () => OpeCompartItemserv,
    (opeCompartItemserv) => opeCompartItemserv.opeCompart,
  )
  opeCompartItemservs: OpeCompartItemserv[];

  @OneToMany(
    () => OpeOcorCompartMovDet,
    (opeOcorCompartMovDet) => opeOcorCompartMovDet.opeCompart,
  )
  opeOcorCompartMovDets: OpeOcorCompartMovDet[];

  @OneToMany(
    () => OpeOcorMovDest,
    (opeOcorMovDest) => opeOcorMovDest.opeCompart,
  )
  opeOcorMovDests: OpeOcorMovDest[];

  @OneToMany(() => OpeOcorPrev, (opeOcorPrev) => opeOcorPrev.opeCompart)
  opeOcorPrevs: OpeOcorPrev[];

  @OneToMany(
    () => SystemDocument,
    (systemDocument) => systemDocument.opeCompart,
  )
  systemDocuments: SystemDocument[];
}
