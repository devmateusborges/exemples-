import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { MovEstNivel } from './MovEstNivel.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_est_nivel', ['id'], { unique: true })
@Entity('ger_est_nivel', { schema: 'public' })
export class GerEstNivel extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column('varchar', {
    name: 'bloq_mov_solic',
    nullable: true,
    length: 1,
    default: () => "'N'",
  })
  bloqMovSolic: string;

  @Column('varchar', {
    name: 'bloq_mov_pedido',
    nullable: true,
    length: 1,
    default: () => "'N'",
  })
  bloqMovPedido: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(() => MovEstNivel, (movEstNivel) => movEstNivel.gerEstNivel)
  movEstNivels: MovEstNivel[];
}
