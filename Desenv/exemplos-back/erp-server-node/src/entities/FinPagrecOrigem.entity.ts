import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { FinPagrecBancoExtrato } from './FinPagrecBancoExtrato.entity';
import { FinPagrecBaixa } from './FinPagrecBaixa.entity';
import { FinPagrecBanco } from './FinPagrecBanco.entity';
import { FinPagrec } from './FinPagrec.entity';
import { FinPagrecParc } from './FinPagrecParc.entity';
import { FinRecibo } from './FinRecibo.entity';
import { Mov } from './Mov.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_pagrec_origem', ['id'], { unique: true })
@Entity('fin_pagrec_origem', { schema: 'public' })
export class FinPagrecOrigem extends BaseEntity {
  @Column('varchar', { name: 'tipo', nullable: true, length: 50 })
  tipo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => FinPagrecBancoExtrato,
    (finPagrecBancoExtrato) => finPagrecBancoExtrato.finPagrecOrigems,
  )
  @JoinColumn([{ name: 'fin_extrato_id', referencedColumnName: 'id' }])
  finExtrato: FinPagrecBancoExtrato;

  @ManyToOne(
    () => FinPagrecBaixa,
    (finPagrecBaixa) => finPagrecBaixa.finPagrecOrigems,
  )
  @JoinColumn([{ name: 'fin_pagrec_baixa_id', referencedColumnName: 'id' }])
  finPagrecBaixa: FinPagrecBaixa;

  @ManyToOne(
    () => FinPagrecBanco,
    (finPagrecBanco) => finPagrecBanco.finPagrecOrigems,
  )
  @JoinColumn([{ name: 'fin_pagrec_banco_id', referencedColumnName: 'id' }])
  finPagrecBanco: FinPagrecBanco;

  @ManyToOne(() => FinPagrec, (finPagrec) => finPagrec.finPagrecOrigems)
  @JoinColumn([{ name: 'fin_pagrec_id', referencedColumnName: 'id' }])
  finPagrec: FinPagrec;

  @ManyToOne(() => FinPagrec, (finPagrec) => finPagrec.finPagrecOrigems2)
  @JoinColumn([{ name: 'fin_pagrec_id_origem', referencedColumnName: 'id' }])
  finPagrecIdOrigem: FinPagrec;

  @ManyToOne(
    () => FinPagrecParc,
    (finPagrecParc) => finPagrecParc.finPagrecOrigems,
  )
  @JoinColumn([{ name: 'fin_pagrec_parc_id', referencedColumnName: 'id' }])
  finPagrecParc: FinPagrecParc;

  @ManyToOne(
    () => FinPagrecParc,
    (finPagrecParc) => finPagrecParc.finPagrecOrigems2,
  )
  @JoinColumn([
    { name: 'fin_pagrec_parc_id_origem', referencedColumnName: 'id' },
  ])
  finPagrecParcIdOrigem: FinPagrecParc;

  @ManyToOne(() => FinRecibo, (finRecibo) => finRecibo.finPagrecOrigems)
  @JoinColumn([{ name: 'fin_recibo_id', referencedColumnName: 'id' }])
  finRecibo: FinRecibo;

  @ManyToOne(() => Mov, (mov) => mov.finPagrecOrigems)
  @JoinColumn([{ name: 'mov_id', referencedColumnName: 'id' }])
  mov: Mov;
}
