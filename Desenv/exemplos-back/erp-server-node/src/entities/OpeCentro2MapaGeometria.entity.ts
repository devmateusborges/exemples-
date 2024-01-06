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

@Index('idx_ope_centro2_mapa_geometria_geom', ['geom'], {})
@Index('pk_ope_centro_mapa_geometria', ['id'], { unique: true })
@Index(
  'idx_ope_centro2_mapa_geometria_centro2_id_area',
  ['opeCentro2IdArea'],
  {},
)
@Entity('ope_centro2_mapa_geometria', { schema: 'public' })
export class OpeCentro2MapaGeometria extends BaseEntity {
  @Column('varchar', { name: 'ope_centro2_id_area', length: 36 })
  opeCentro2IdArea: string;

  @Column('geometry', { name: 'geom', nullable: true })
  geom: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => OpeCentro2Area,
    (opeCentro2Area) => opeCentro2Area.opeCentro2MapaGeometrias,
    { onDelete: 'CASCADE' },
  )
  @JoinColumn([{ name: 'ope_centro2_id_area', referencedColumnName: 'id' }])
  opeCentro2IdArea2: OpeCentro2Area;
}
