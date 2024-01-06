import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { FinPagrecPrev } from './FinPagrecPrev.entity';
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_pagrec_versao', ['id'], { unique: true })
@Entity('fin_pagrec_versao', { schema: 'public' })
export class FinPagrecVersao extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_versao', length: 50 })
  siglaVersao: string;

  @Column('date', { name: 'data_per_ini' })
  dataPerIni: string;

  @Column('date', { name: 'data_per_fin' })
  dataPerFin: string;

  @Column('varchar', {
    name: 'versao_atual',
    length: 1,
    default: () => "'N'",
  })
  versaoAtual: string;

  @Column('varchar', {
    name: 'tipo_per',
    length: 1,
    default: () => "'M'",
  })
  tipoPer: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => FinPagrecPrev,
    (finPagrecPrev) => finPagrecPrev.finPagrecVersao,
  )
  finPagrecPrevs: FinPagrecPrev[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
