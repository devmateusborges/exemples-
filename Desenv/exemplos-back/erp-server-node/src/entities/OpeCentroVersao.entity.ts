import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { OpeCentro2Ord } from './OpeCentro2Ord.entity';
import { OpeCentroPrev } from './OpeCentroPrev.entity';
import { OpeCentroRatTipo } from './OpeCentroRatTipo.entity';
import { OpeCentroRend } from './OpeCentroRend.entity';
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro_versao', ['id'], { unique: true })
@Entity('ope_centro_versao', { schema: 'public' })
export class OpeCentroVersao extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_versao', length: 50 })
  siglaVersao: string;

  @Column('varchar', { name: 'versao_atual', length: 1 })
  versaoAtual: string;

  @Column('date', { name: 'data_per_ini' })
  dataPerIni: string;

  @Column('date', { name: 'data_per_fin' })
  dataPerFin: string;

  @Column('varchar', { name: 'tipo_per', length: 1 })
  tipoPer: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => OpeCentro2Ord,
    (opeCentro2Ord) => opeCentro2Ord.opeCentroVersao,
  )
  opeCentro2Ords: OpeCentro2Ord[];

  @OneToMany(
    () => OpeCentroPrev,
    (opeCentroPrev) => opeCentroPrev.opeCentroVersao,
  )
  opeCentroPrevs: OpeCentroPrev[];

  @OneToMany(
    () => OpeCentroRatTipo,
    (opeCentroRatTipo) => opeCentroRatTipo.opeCentroVersao,
  )
  opeCentroRatTipos: OpeCentroRatTipo[];

  @OneToMany(
    () => OpeCentroRend,
    (opeCentroRend) => opeCentroRend.opeCentroVersao,
  )
  opeCentroRends: OpeCentroRend[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
