import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { OpeCentro2Area } from './OpeCentro2Area.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro_mapa_coord', ['id'], { unique: true })
@Entity('ope_centro2_mapa_coord', { schema: 'public' })
export class OpeCentro2MapaCoord extends BaseEntity {
  @Column('varchar', { name: 'lat_x', length: 100 })
  latX: string;

  @Column('varchar', { name: 'long_y', length: 100 })
  longY: string;

  @Column('integer', { name: 'ordem' })
  ordem: number;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => OpeCentro2Area,
    (opeCentro2Area) => opeCentro2Area.opeCentro2MapaCoords,
    { onDelete: 'CASCADE' },
  )
  @JoinColumn([{ name: 'ope_centro2_id_area', referencedColumnName: 'id' }])
  opeCentro2IdArea: OpeCentro2Area;
}
