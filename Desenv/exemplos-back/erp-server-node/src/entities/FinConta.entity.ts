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
import { FinBanco } from './FinBanco.entity';
import { GerEmpresa } from './GerEmpresa.entity';
import { FinPagrecBaixa } from './FinPagrecBaixa.entity';
import { FinPagrecBanco } from './FinPagrecBanco.entity';
import { FinPagrecBancoExtrato } from './FinPagrecBancoExtrato.entity';
import { FinPagrecBancoTransf } from './FinPagrecBancoTransf.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_conta', ['id'], { unique: true })
@Entity('fin_conta', { schema: 'public' })
export class FinConta extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'nr_agencia', length: 50 })
  nrAgencia: string;

  @Column('varchar', { name: 'nr_conta', length: 50 })
  nrConta: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => FinBanco, (finBanco) => finBanco.finContas)
  @JoinColumn([{ name: 'fin_banco_id', referencedColumnName: 'id' }])
  finBanco: FinBanco;

  @ManyToOne(() => GerEmpresa, (gerEmpresa) => gerEmpresa.finContas)
  @JoinColumn([{ name: 'ger_empresa_id', referencedColumnName: 'id' }])
  gerEmpresa: GerEmpresa;

  @OneToMany(() => FinPagrecBaixa, (finPagrecBaixa) => finPagrecBaixa.finConta)
  finPagrecBaixas: FinPagrecBaixa[];

  @OneToMany(() => FinPagrecBanco, (finPagrecBanco) => finPagrecBanco.finConta)
  finPagrecBancos: FinPagrecBanco[];

  @OneToMany(
    () => FinPagrecBancoExtrato,
    (finPagrecBancoExtrato) => finPagrecBancoExtrato.finConta,
  )
  finPagrecBancoExtratoes: FinPagrecBancoExtrato[];

  @OneToMany(
    () => FinPagrecBancoTransf,
    (finPagrecBancoTransf) => finPagrecBancoTransf.finContaIdDestino,
  )
  finPagrecBancoTransfs: FinPagrecBancoTransf[];

  @OneToMany(
    () => FinPagrecBancoTransf,
    (finPagrecBancoTransf) => finPagrecBancoTransf.finContaIdOrigem,
  )
  finPagrecBancoTransfs2: FinPagrecBancoTransf[];
}
