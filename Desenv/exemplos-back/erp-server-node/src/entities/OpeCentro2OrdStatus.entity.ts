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
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro2_ord_status', ['id'], { unique: true })
@Entity('ope_centro2_ord_status', { schema: 'public' })
export class OpeCentro2OrdStatus extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_ord_status', length: 50 })
  siglaOrdStatus: string;

  @Column('varchar', { name: 'tipo_status', length: 1 })
  tipoStatus: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => OpeCentro2Ord,
    (opeCentro2Ord) => opeCentro2Ord.opeCentro2OrdStatus,
  )
  opeCentro2Ords: OpeCentro2Ord[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
