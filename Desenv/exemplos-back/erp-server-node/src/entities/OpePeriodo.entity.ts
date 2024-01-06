import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { OpeCentro2Area } from './OpeCentro2Area.entity';
import { OpeCentro2Ord } from './OpeCentro2Ord.entity';
import { OpeCentroDest } from './OpeCentroDest.entity';
import { OpeCentroPrev } from './OpeCentroPrev.entity';
import { OpeCentroRatFator } from './OpeCentroRatFator.entity';
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_periodo', ['id'], { unique: true })
@Entity('ope_periodo', { schema: 'public' })
export class OpePeriodo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_periodo', length: 50 })
  siglaPeriodo: string;

  @Column('date', { name: 'data_ini' })
  dataIni: string;

  @Column('date', { name: 'data_fin' })
  dataFin: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => OpeCentro2Area,
    (opeCentro2Area) => opeCentro2Area.opePeriodo,
  )
  opeCentro2Areas: OpeCentro2Area[];

  @OneToMany(() => OpeCentro2Ord, (opeCentro2Ord) => opeCentro2Ord.opePeriodo)
  opeCentro2Ords: OpeCentro2Ord[];

  @OneToMany(
    () => OpeCentroDest,
    (opeCentroDest) => opeCentroDest.opePeriodoIdDest,
  )
  opeCentroDests: OpeCentroDest[];

  @OneToMany(() => OpeCentroPrev, (opeCentroPrev) => opeCentroPrev.opePeriodo)
  opeCentroPrevs: OpeCentroPrev[];

  @OneToMany(
    () => OpeCentroRatFator,
    (opeCentroRatFator) => opeCentroRatFator.opePeriodo,
  )
  opeCentroRatFators: OpeCentroRatFator[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
