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
import { Mov } from './Mov.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_mov_medida', ['id'], { unique: true })
@Entity('mov_medida', { schema: 'public' })
export class MovMedida extends BaseEntity {
  @Column('varchar', { name: 'tipo_medida', length: 50 })
  tipoMedida: string;

  @Column('numeric', { name: 'qnt_medida', precision: 18, scale: 6 })
  qntMedida: string;

  @Column('varchar', { name: 'marca', nullable: true, length: 50 })
  marca: string;

  @Column('numeric', {
    name: 'nr_volume',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  nrVolume: string;

  @Column('numeric', {
    name: 'peso_liquido',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  pesoLiquido: string;

  @Column('numeric', {
    name: 'peso_bruto',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  pesoBruto: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => GerUmedida, (gerUmedida) => gerUmedida.movMedidas)
  @JoinColumn([{ name: 'ger_umedida_id', referencedColumnName: 'id' }])
  gerUmedida: GerUmedida;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => Mov, (mov) => mov.movMedidas)
  @JoinColumn([{ name: 'mov_id', referencedColumnName: 'id' }])
  mov: Mov;
}
