import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { GerUmedida } from './GerUmedida.entity';
import { SystemUnit } from './SystemUnit.entity';
import { OpeCentro2 } from './OpeCentro2.entity';
import { OpeCentro2Ord } from './OpeCentro2Ord.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro2_ord_dest', ['id'], { unique: true })
@Entity('ope_centro2_ord_dest', { schema: 'public' })
export class OpeCentro2OrdDest extends BaseEntity {
  @Column('numeric', {
    name: 'qnt_obj',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  qntObj: string;

  @Column('numeric', {
    name: 'qnt_prev_obj',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  qntPrevObj: string;

  @Column('numeric', {
    name: 'valor_unit_prev',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  valorUnitPrev: string;

  @Column('numeric', {
    name: 'valor_total_prev',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  valorTotalPrev: string;

  @Column('varchar', {
    name: 'observacao_interna',
    nullable: true,
    length: 250,
  })
  observacaoInterna: string;

  @Column('varchar', {
    name: 'observacao_externa',
    nullable: true,
    length: 250,
  })
  observacaoExterna: string;

  @Column('numeric', {
    name: 'valor_unit',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  valorUnit: string;

  @Column('numeric', {
    name: 'valor_total',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  valorTotal: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @Column('date', { name: 'data_valid', nullable: true })
  dataValid: string;

  @ManyToOne(() => GerUmedida, (gerUmedida) => gerUmedida.opeCentro2OrdDests)
  @JoinColumn([{ name: 'ger_umedida_id_dest', referencedColumnName: 'id' }])
  gerUmedidaIdDest: GerUmedida;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => OpeCentro2, (opeCentro2) => opeCentro2.opeCentro2OrdDests)
  @JoinColumn([{ name: 'ope_centro2_id_dest', referencedColumnName: 'id' }])
  opeCentro2IdDest: OpeCentro2;

  @ManyToOne(
    () => OpeCentro2Ord,
    (opeCentro2Ord) => opeCentro2Ord.opeCentro2OrdDests,
  )
  @JoinColumn([{ name: 'ope_centro2_ord_id', referencedColumnName: 'id' }])
  opeCentro2Ord: OpeCentro2Ord;
}
