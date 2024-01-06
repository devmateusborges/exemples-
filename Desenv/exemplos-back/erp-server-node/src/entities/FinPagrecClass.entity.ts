import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { FinClass } from './FinClass.entity';
import { FinPagrecBanco } from './FinPagrecBanco.entity';
import { FinPagrec } from './FinPagrec.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_pagrec_class', ['id'], { unique: true })
@Entity('fin_pagrec_class', { schema: 'public' })
export class FinPagrecClass extends BaseEntity {
  @Column('numeric', {
    name: 'valor',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor: string;

  @Column('numeric', {
    name: 'fator_rat',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  fatorRat: string;

  @Column('numeric', {
    name: 'perc_rat',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  percRat: string;

  @Column('date', { name: 'data_valid', nullable: true })
  dataValid: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => FinClass, (finClass) => finClass.finPagrecClasses)
  @JoinColumn([{ name: 'fin_class_id', referencedColumnName: 'id' }])
  finClass: FinClass;

  @ManyToOne(
    () => FinPagrecBanco,
    (finPagrecBanco) => finPagrecBanco.finPagrecClasses,
  )
  @JoinColumn([{ name: 'fin_pagrec_banco_id', referencedColumnName: 'id' }])
  finPagrecBanco: FinPagrecBanco;

  @ManyToOne(() => FinPagrec, (finPagrec) => finPagrec.finPagrecClasses)
  @JoinColumn([{ name: 'fin_pagrec_id', referencedColumnName: 'id' }])
  finPagrec: FinPagrec;
}
