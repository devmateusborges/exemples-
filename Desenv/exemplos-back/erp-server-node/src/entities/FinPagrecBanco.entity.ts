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
import { GerEmpresa } from './GerEmpresa.entity';
import { FinPagrecClass } from './FinPagrecClass.entity';
import { FinPagrecOrigem } from './FinPagrecOrigem.entity';
import { OpeCentroDest } from './OpeCentroDest.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_pagrec_banco', ['id'], { unique: true })
@Entity('fin_pagrec_banco', { schema: 'public' })
export class FinPagrecBanco extends BaseEntity {
  @Column('date', { name: 'data_mov' })
  dataMov: string;

  @Column('varchar', { name: 'numero_doc_pagrec', length: 50 })
  numeroDocPagrec: string;

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

  @Column('date', { name: 'data_valid', nullable: true })
  dataValid: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => FinConta, (finConta) => finConta.finPagrecBancos)
  @JoinColumn([{ name: 'fin_conta_id', referencedColumnName: 'id' }])
  finConta: FinConta;

  @ManyToOne(() => GerEmpresa, (gerEmpresa) => gerEmpresa.finPagrecBancos)
  @JoinColumn([{ name: 'ger_empresa_id', referencedColumnName: 'id' }])
  gerEmpresa: GerEmpresa;

  @OneToMany(
    () => FinPagrecClass,
    (finPagrecClass) => finPagrecClass.finPagrecBanco,
  )
  finPagrecClasses: FinPagrecClass[];

  @OneToMany(
    () => FinPagrecOrigem,
    (finPagrecOrigem) => finPagrecOrigem.finPagrecBanco,
  )
  finPagrecOrigems: FinPagrecOrigem[];

  @OneToMany(
    () => OpeCentroDest,
    (opeCentroDest) => opeCentroDest.finPagrecBanco,
  )
  opeCentroDests: OpeCentroDest[];
}
