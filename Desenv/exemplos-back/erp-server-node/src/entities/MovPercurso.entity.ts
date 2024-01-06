import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { GerCidade } from './GerCidade.entity';
import { SystemUnit } from './SystemUnit.entity';
import { Mov } from './Mov.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_mov_percurso', ['id'], { unique: true })
@Entity('mov_percurso', { schema: 'public' })
export class MovPercurso extends BaseEntity {
  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => GerCidade, (gerCidade) => gerCidade.movPercursos)
  @JoinColumn([{ name: 'ger_cidade_id', referencedColumnName: 'id' }])
  gerCidade: GerCidade;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => Mov, (mov) => mov.movPercursos)
  @JoinColumn([{ name: 'mov_id', referencedColumnName: 'id' }])
  mov: Mov;
}
