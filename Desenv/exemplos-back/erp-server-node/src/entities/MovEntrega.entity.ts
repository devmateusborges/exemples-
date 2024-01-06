import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { GerCidade } from './GerCidade.entity';
import { SystemUnit } from './SystemUnit.entity';
import { Mov } from './Mov.entity';
import { MovEntregaDoc } from './MovEntregaDoc.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_mov_entrega', ['id'], { unique: true })
@Entity('mov_entrega', { schema: 'public' })
export class MovEntrega extends BaseEntity {
  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => GerCidade, (gerCidade) => gerCidade.movEntregas)
  @JoinColumn([{ name: 'ger_cidade_id', referencedColumnName: 'id' }])
  gerCidade: GerCidade;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => Mov, (mov) => mov.movEntregas)
  @JoinColumn([{ name: 'mov_id', referencedColumnName: 'id' }])
  mov: Mov;

  @OneToMany(() => MovEntregaDoc, (movEntregaDoc) => movEntregaDoc.movEntrega)
  movEntregaDocs: MovEntregaDoc[];
}
