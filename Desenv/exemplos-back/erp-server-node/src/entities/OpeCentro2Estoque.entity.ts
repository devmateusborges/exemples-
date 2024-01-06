import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { OpeCentro2 } from './OpeCentro2.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro2_estoque', ['id'], { unique: true })
@Entity('ope_centro2_estoque', { schema: 'public' })
export class OpeCentro2Estoque extends BaseEntity {
  @Column('varchar', { name: 'tipo', nullable: true, length: 1 })
  tipo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => OpeCentro2, (opeCentro2) => opeCentro2.opeCentro2Estoques, {
    onDelete: 'CASCADE',
  })
  @JoinColumn([{ name: 'ope_centro2_id', referencedColumnName: 'id' }])
  opeCentro2: OpeCentro2;
}
