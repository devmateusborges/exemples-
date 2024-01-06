import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { MovOperacao } from './MovOperacao.entity';
import { MovStatus } from './MovStatus.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_mov_operacao_status', ['id'], { unique: true })
@Entity('mov_operacao_status', { schema: 'public' })
export class MovOperacaoStatus extends BaseEntity {
  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => MovOperacao,
    (movOperacao) => movOperacao.movOperacaoStatuses,
  )
  @JoinColumn([{ name: 'mov_operacao_id', referencedColumnName: 'id' }])
  movOperacao: MovOperacao;

  @ManyToOne(
    () => MovOperacao,
    (movOperacao) => movOperacao.movOperacaoStatuses2,
  )
  @JoinColumn([{ name: 'mov_operacao_id_prox', referencedColumnName: 'id' }])
  movOperacaoIdProx: MovOperacao;

  @ManyToOne(() => MovStatus, (movStatus) => movStatus.movOperacaoStatuses)
  @JoinColumn([{ name: 'mov_status_id', referencedColumnName: 'id' }])
  movStatus: MovStatus;

  @ManyToOne(() => MovStatus, (movStatus) => movStatus.movOperacaoStatuses2)
  @JoinColumn([{ name: 'mov_status_id_prox', referencedColumnName: 'id' }])
  movStatusIdProx: MovStatus;
}
