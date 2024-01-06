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
import { GerEmpresa } from './GerEmpresa.entity';
import { FinPagrecBaixa } from './FinPagrecBaixa.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_lote', ['id'], { unique: true })
@Entity('fin_lote', { schema: 'public' })
export class FinLote extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('date', { name: 'data_lote' })
  dataLote: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerEmpresa, (gerEmpresa) => gerEmpresa.finLotes)
  @JoinColumn([{ name: 'ger_empresa_id', referencedColumnName: 'id' }])
  gerEmpresa: GerEmpresa;

  @OneToMany(() => FinPagrecBaixa, (finPagrecBaixa) => finPagrecBaixa.finLote)
  finPagrecBaixas: FinPagrecBaixa[];
}
