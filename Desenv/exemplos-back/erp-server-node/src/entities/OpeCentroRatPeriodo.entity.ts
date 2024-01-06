import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { OpeCentroRatFator } from './OpeCentroRatFator.entity';
import { SystemUnit } from './SystemUnit.entity';
import { OpeCentroRatTipo } from './OpeCentroRatTipo.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro_rat_periodo', ['id'], { unique: true })
@Entity('ope_centro_rat_periodo', { schema: 'public' })
export class OpeCentroRatPeriodo extends BaseEntity {
  @Column('date', { name: 'data_ini' })
  dataIni: string;

  @Column('varchar', { name: 'tipo_rp', nullable: true, length: 1 })
  tipoRp: string;

  @Column('varchar', {
    name: 'atual',
    nullable: true,
    length: 1,
    default: () => "'N'",
  })
  atual: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => OpeCentroRatFator,
    (opeCentroRatFator) => opeCentroRatFator.opeCentroRatPeriodo,
  )
  opeCentroRatFators: OpeCentroRatFator[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => OpeCentroRatTipo,
    (opeCentroRatTipo) => opeCentroRatTipo.opeCentroRatPeriodos,
  )
  @JoinColumn([{ name: 'ope_centro_rat_tipo_id', referencedColumnName: 'id' }])
  opeCentroRatTipo: OpeCentroRatTipo;
}
