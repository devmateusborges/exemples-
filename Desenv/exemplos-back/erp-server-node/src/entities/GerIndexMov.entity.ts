import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { GerIndex } from './GerIndex.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_index_mov', ['id'], { unique: true })
@Entity('ger_index_mov', { schema: 'public' })
export class GerIndexMov extends BaseEntity {
  @Column('date', { name: 'data_mov' })
  dataMov: string;

  @Column('numeric', {
    name: 'valor1',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valor1: string;

  @Column('numeric', {
    name: 'valor2',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valor2: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerIndex, (gerIndex) => gerIndex.gerIndexMovs)
  @JoinColumn([{ name: 'ger_index_id', referencedColumnName: 'id' }])
  gerIndex: GerIndex;
}
