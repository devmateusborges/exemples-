import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { FinPagrecParc } from './FinPagrecParc.entity';
import { FinTipoVariacao } from './FinTipoVariacao.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_pagrec_parc_var', ['id'], { unique: true })
@Entity('fin_pagrec_parc_var', { schema: 'public' })
export class FinPagrecParcVar extends BaseEntity {
  @Column('numeric', {
    name: 'valor',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor: string;

  @Column('date', { name: 'data_valid', nullable: true })
  dataValid: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => FinPagrecParc,
    (finPagrecParc) => finPagrecParc.finPagrecParcVars,
  )
  @JoinColumn([{ name: 'fin_pagrec_parc_id', referencedColumnName: 'id' }])
  finPagrecParc: FinPagrecParc;

  @ManyToOne(
    () => FinTipoVariacao,
    (finTipoVariacao) => finTipoVariacao.finPagrecParcVars,
  )
  @JoinColumn([{ name: 'fin_tipo_variacao_id', referencedColumnName: 'id' }])
  finTipoVariacao: FinTipoVariacao;
}
