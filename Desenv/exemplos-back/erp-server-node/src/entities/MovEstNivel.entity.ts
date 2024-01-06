import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { GerEstNivel } from './GerEstNivel.entity';
import { GerItemserv } from './GerItemserv.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_mov_est_nivel', ['id'], { unique: true })
@Entity('mov_est_nivel', { schema: 'public' })
export class MovEstNivel extends BaseEntity {
  @Column('numeric', { name: 'qnt_min', precision: 18, scale: 6 })
  qntMin: string;

  @Column('numeric', { name: 'qnt_max', precision: 18, scale: 6 })
  qntMax: string;

  @Column('numeric', { name: 'qnt_nesc', precision: 18, scale: 6 })
  qntNesc: string;

  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerEstNivel, (gerEstNivel) => gerEstNivel.movEstNivels)
  @JoinColumn([{ name: 'ger_est_nivel_id', referencedColumnName: 'id' }])
  gerEstNivel: GerEstNivel;

  @ManyToOne(() => GerItemserv, (gerItemserv) => gerItemserv.movEstNivels)
  @JoinColumn([{ name: 'ger_itemserv_id', referencedColumnName: 'id' }])
  gerItemserv: GerItemserv;
}
