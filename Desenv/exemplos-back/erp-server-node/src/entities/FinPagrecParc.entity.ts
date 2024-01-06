import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { FinPagrecBaixa } from './FinPagrecBaixa.entity';
import { FinPagrecOrigem } from './FinPagrecOrigem.entity';
import { SystemUnit } from './SystemUnit.entity';
import { FinDocTipo } from './FinDocTipo.entity';
import { FinPagrec } from './FinPagrec.entity';
import { FinPagrecParcVar } from './FinPagrecParcVar.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_pagrec_parc', ['id'], { unique: true })
@Entity('fin_pagrec_parc', { schema: 'public' })
export class FinPagrecParc extends BaseEntity {
  @Column('integer', { name: 'numero_parc' })
  numeroParc: number;

  @Column('numeric', {
    name: 'valor_pagrec',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valorPagrec: string;

  @Column('numeric', {
    name: 'valor_juro',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valorJuro: string;

  @Column('numeric', {
    name: 'valor_desconto',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valorDesconto: string;

  @Column('numeric', {
    name: 'valor_multa',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valorMulta: string;

  @Column('date', { name: 'data_venc', nullable: true })
  dataVenc: string;

  @Column('date', { name: 'data_valid', nullable: true })
  dataValid: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => FinPagrecBaixa,
    (finPagrecBaixa) => finPagrecBaixa.finPagrecParc,
  )
  finPagrecBaixas: FinPagrecBaixa[];

  @OneToMany(
    () => FinPagrecOrigem,
    (finPagrecOrigem) => finPagrecOrigem.finPagrecParc,
  )
  finPagrecOrigems: FinPagrecOrigem[];

  @OneToMany(
    () => FinPagrecOrigem,
    (finPagrecOrigem) => finPagrecOrigem.finPagrecParcIdOrigem,
  )
  finPagrecOrigems2: FinPagrecOrigem[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => FinDocTipo, (finDocTipo) => finDocTipo.finPagrecParcs)
  @JoinColumn([{ name: 'fin_doc_tipo_id', referencedColumnName: 'id' }])
  finDocTipo: FinDocTipo;

  @ManyToOne(() => FinPagrec, (finPagrec) => finPagrec.finPagrecParcs)
  @JoinColumn([{ name: 'fin_pagrec_id', referencedColumnName: 'id' }])
  finPagrec: FinPagrec;

  @OneToMany(
    () => FinPagrecParcVar,
    (finPagrecParcVar) => finPagrecParcVar.finPagrecParc,
  )
  finPagrecParcVars: FinPagrecParcVar[];
}
