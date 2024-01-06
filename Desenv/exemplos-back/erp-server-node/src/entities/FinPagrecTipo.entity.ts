import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { FinPagrec } from './FinPagrec.entity';
import { SystemUnit } from './SystemUnit.entity';
import { FinUnitParam } from './FinUnitParam.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_tipo_pagrec', ['id'], { unique: true })
@Entity('fin_pagrec_tipo', { schema: 'public' })
export class FinPagrecTipo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'aceita_entrada', length: 1 })
  aceitaEntrada: string;

  @Column('varchar', { name: 'aceita_saida', length: 1 })
  aceitaSaida: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => FinPagrec, (finPagrec) => finPagrec.finPagrecTipo)
  finPagrecs: FinPagrec[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(() => FinUnitParam, (finUnitParam) => finUnitParam.finPagrecTipo)
  finUnitParams: FinUnitParam[];
}
