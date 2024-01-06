import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { FinConta } from './FinConta.entity';
import { GerEmpresa } from './GerEmpresa.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_pagrec_banco_transf', ['id'], { unique: true })
@Entity('fin_pagrec_banco_transf', { schema: 'public' })
export class FinPagrecBancoTransf extends BaseEntity {
  @Column('date', { name: 'data_mov' })
  dataMov: string;

  @Column('numeric', {
    name: 'valor',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor: string;

  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column('varchar', {
    name: 'process_id',
    nullable: true,
    length: 36,
  })
  processId: string;

  @Column('date', { name: 'data_valid', nullable: true })
  dataValid: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => FinConta, (finConta) => finConta.finPagrecBancoTransfs)
  @JoinColumn([{ name: 'fin_conta_id_destino', referencedColumnName: 'id' }])
  finContaIdDestino: FinConta;

  @ManyToOne(() => FinConta, (finConta) => finConta.finPagrecBancoTransfs2)
  @JoinColumn([{ name: 'fin_conta_id_origem', referencedColumnName: 'id' }])
  finContaIdOrigem: FinConta;

  @ManyToOne(() => GerEmpresa, (gerEmpresa) => gerEmpresa.finPagrecBancoTransfs)
  @JoinColumn([{ name: 'ger_empresa_id', referencedColumnName: 'id' }])
  gerEmpresa: GerEmpresa;
}
