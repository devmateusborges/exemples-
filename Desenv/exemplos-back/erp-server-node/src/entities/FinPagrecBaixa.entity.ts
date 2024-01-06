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
import { FinDocTipo } from './FinDocTipo.entity';
import { FinLote } from './FinLote.entity';
import { FinPagrecParc } from './FinPagrecParc.entity';
import { FinPagrecBaixaVar } from './FinPagrecBaixaVar.entity';
import { FinPagrecOrigem } from './FinPagrecOrigem.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_pagrec_baixa', ['id'], { unique: true })
@Entity('fin_pagrec_baixa', { schema: 'public' })
export class FinPagrecBaixa extends BaseEntity {
  @Column('varchar', { name: 'tipo', length: 1 })
  tipo: string;

  @Column('varchar', { name: 'numero_doc_pagrec', length: 50 })
  numeroDocPagrec: string;

  @Column('numeric', {
    name: 'valor_pagrec',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valorPagrec: string;

  @Column('date', { name: 'data_baixa', nullable: true })
  dataBaixa: string;

  @Column('date', { name: 'data_valid', nullable: true })
  dataValid: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => FinConta, (finConta) => finConta.finPagrecBaixas)
  @JoinColumn([{ name: 'fin_conta_id', referencedColumnName: 'id' }])
  finConta: FinConta;

  @ManyToOne(() => FinDocTipo, (finDocTipo) => finDocTipo.finPagrecBaixas)
  @JoinColumn([{ name: 'fin_doc_tipo_id', referencedColumnName: 'id' }])
  finDocTipo: FinDocTipo;

  @ManyToOne(() => FinLote, (finLote) => finLote.finPagrecBaixas)
  @JoinColumn([{ name: 'fin_lote_id', referencedColumnName: 'id' }])
  finLote: FinLote;

  @ManyToOne(
    () => FinPagrecParc,
    (finPagrecParc) => finPagrecParc.finPagrecBaixas,
  )
  @JoinColumn([{ name: 'fin_pagrec_parc_id', referencedColumnName: 'id' }])
  finPagrecParc: FinPagrecParc;

  @OneToMany(
    () => FinPagrecBaixaVar,
    (finPagrecBaixaVar) => finPagrecBaixaVar.finPagrecBaixa,
  )
  finPagrecBaixaVars: FinPagrecBaixaVar[];

  @OneToMany(
    () => FinPagrecOrigem,
    (finPagrecOrigem) => finPagrecOrigem.finPagrecBaixa,
  )
  finPagrecOrigems: FinPagrecOrigem[];
}
