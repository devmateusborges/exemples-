import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { FinPagrecPrevDest } from './FinPagrecPrevDest.entity';
import { OpeCentroSubtipo } from './OpeCentroSubtipo.entity';
import { SystemUnit } from './SystemUnit.entity';
import { CtbComp } from './CtbComp.entity';
import { GerPessoa } from './GerPessoa.entity';
import { OpeCentro2 } from './OpeCentro2.entity';
import { OpeCentro2OrdRec } from './OpeCentro2OrdRec.entity';
import { OpeCentroConfig } from './OpeCentroConfig.entity';
import { OpeCentroDest } from './OpeCentroDest.entity';
import { OpeCentroPrevDest } from './OpeCentroPrevDest.entity';
import { OpeCentroRatFator } from './OpeCentroRatFator.entity';
import { SystemDocument } from './SystemDocument.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro1', ['id'], { unique: true })
@Entity('ope_centro1', { schema: 'public' })
export class OpeCentro1 extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_centro1', length: 50 })
  siglaCentro1: string;

  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column('date', { name: 'data_valid', nullable: true })
  dataValid: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => FinPagrecPrevDest,
    (finPagrecPrevDest) => finPagrecPrevDest.opeCentro1IdDest,
  )
  finPagrecPrevDests: FinPagrecPrevDest[];

  @ManyToOne(
    () => OpeCentroSubtipo,
    (opeCentroSubtipo) => opeCentroSubtipo.opeCentros,
  )
  @JoinColumn([{ name: 'ope_centro_subtipo_id', referencedColumnName: 'id' }])
  opeCentroSubtipo: OpeCentroSubtipo;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => CtbComp, (ctbComp) => ctbComp.opeCentros)
  @JoinColumn([{ name: 'ctb_comp_id', referencedColumnName: 'id' }])
  ctbComp: CtbComp;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.opeCentros)
  @JoinColumn([{ name: 'ger_pessoa_id', referencedColumnName: 'id' }])
  gerPessoa: GerPessoa;

  @OneToMany(() => OpeCentro2, (opeCentro2) => opeCentro2.opeCentro1)
  opeCentros: OpeCentro2[];

  @OneToMany(
    () => OpeCentro2OrdRec,
    (opeCentro2OrdRec) => opeCentro2OrdRec.opeCentro1,
  )
  opeCentro2OrdRecs: OpeCentro2OrdRec[];

  @OneToMany(
    () => OpeCentro2OrdRec,
    (opeCentro2OrdRec) => opeCentro2OrdRec.opeCentro1IdImp,
  )
  opeCentro2OrdRecs2: OpeCentro2OrdRec[];

  @OneToMany(
    () => OpeCentroConfig,
    (opeCentroConfig) => opeCentroConfig.opeCentro1,
  )
  opeCentroConfigs: OpeCentroConfig[];

  @OneToMany(() => OpeCentroDest, (opeCentroDest) => opeCentroDest.opeCentro1)
  opeCentroDests: OpeCentroDest[];

  @OneToMany(
    () => OpeCentroDest,
    (opeCentroDest) => opeCentroDest.opeCentro1IdDest,
  )
  opeCentroDests2: OpeCentroDest[];

  @OneToMany(
    () => OpeCentroPrevDest,
    (opeCentroPrevDest) => opeCentroPrevDest.opeCentro1,
  )
  opeCentroPrevDests: OpeCentroPrevDest[];

  @OneToMany(
    () => OpeCentroRatFator,
    (opeCentroRatFator) => opeCentroRatFator.opeCentro1,
  )
  opeCentroRatFators: OpeCentroRatFator[];

  @OneToMany(
    () => SystemDocument,
    (systemDocument) => systemDocument.opeCentro1,
  )
  systemDocuments: SystemDocument[];
}
