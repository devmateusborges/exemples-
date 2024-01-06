import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { FinPagrecBaixa } from './FinPagrecBaixa.entity';
import { FinTipoVariacao } from './FinTipoVariacao.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_pagrec_baixa_var', ['id'], { unique: true })
@Entity('fin_pagrec_baixa_var', { schema: 'public' })
export class FinPagrecBaixaVar extends BaseEntity {
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

  @ManyToOne(
    () => FinPagrecBaixa,
    (finPagrecBaixa) => finPagrecBaixa.finPagrecBaixaVars,
  )
  @JoinColumn([{ name: 'fin_pagrec_baixa_id', referencedColumnName: 'id' }])
  finPagrecBaixa: FinPagrecBaixa;

  @ManyToOne(
    () => FinTipoVariacao,
    (finTipoVariacao) => finTipoVariacao.finPagrecBaixaVars,
  )
  @JoinColumn([{ name: 'fin_tipo_variacao_id', referencedColumnName: 'id' }])
  finTipoVariacao: FinTipoVariacao;
}
