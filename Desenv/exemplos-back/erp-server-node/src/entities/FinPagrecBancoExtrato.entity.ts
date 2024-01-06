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
import { FinConta } from './FinConta.entity';
import { FinPagrecOrigem } from './FinPagrecOrigem.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_pagrec_banco_extrato', ['id'], { unique: true })
@Entity('fin_pagrec_banco_extrato', { schema: 'public' })
export class FinPagrecBancoExtrato extends BaseEntity {
  @Column('date', { name: 'data_extrato' })
  dataExtrato: string;

  @Column('varchar', { name: 'numero_doc', length: 50 })
  numeroDoc: string;

  @Column('varchar', {
    name: 'descricao',
    nullable: true,
    length: 250,
  })
  descricao: string;

  @Column('numeric', {
    name: 'valor',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor: string;

  @Column('varchar', {
    name: 'status',
    length: 2,
    default: () => "'PD'",
  })
  status: string;

  @Column('varchar', {
    name: 'status_observacao',
    nullable: true,
    length: 250,
  })
  statusObservacao: string;

  @Column('varchar', {
    name: 'process_id',
    nullable: true,
    length: 36,
  })
  processId: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => FinConta, (finConta) => finConta.finPagrecBancoExtratoes)
  @JoinColumn([{ name: 'fin_conta_id', referencedColumnName: 'id' }])
  finConta: FinConta;

  @OneToMany(
    () => FinPagrecOrigem,
    (finPagrecOrigem) => finPagrecOrigem.finExtrato,
  )
  finPagrecOrigems: FinPagrecOrigem[];
}
