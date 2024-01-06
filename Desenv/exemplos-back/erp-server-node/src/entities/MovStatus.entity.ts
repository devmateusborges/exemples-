import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { Mov } from './Mov.entity';
import { MovOperacaoStatus } from './MovOperacaoStatus.entity';
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_mov_status', ['id'], { unique: true })
@Entity('mov_status', { schema: 'public' })
export class MovStatus extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_mov_status', length: 50 })
  siglaMovStatus: string;

  @Column('varchar', { name: 'tipo_status', length: 1 })
  tipoStatus: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => Mov, (mov) => mov.movStatus)
  movs: Mov[];

  @OneToMany(
    () => MovOperacaoStatus,
    (movOperacaoStatus) => movOperacaoStatus.movStatus,
  )
  movOperacaoStatuses: MovOperacaoStatus[];

  @OneToMany(
    () => MovOperacaoStatus,
    (movOperacaoStatus) => movOperacaoStatus.movStatusIdProx,
  )
  movOperacaoStatuses2: MovOperacaoStatus[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
