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
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_umedida_conv', ['id'], { unique: true })
@Entity('ger_umedida_conv', { schema: 'public' })
export class GerUmedidaConv extends BaseEntity {
  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('numeric', { name: 'fator_mult', precision: 18, scale: 6 })
  fatorMult: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => GerUmedida, (gerUmedida) => gerUmedida.gerUmedidaConvs)
  @JoinColumn([{ name: 'ger_umedida_id_de', referencedColumnName: 'id' }])
  gerUmedidaIdDe: GerUmedida;

  @ManyToOne(() => GerUmedida, (gerUmedida) => gerUmedida.gerUmedidaConvs2)
  @JoinColumn([{ name: 'ger_umedida_id_para', referencedColumnName: 'id' }])
  gerUmedidaIdPara: GerUmedida;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
