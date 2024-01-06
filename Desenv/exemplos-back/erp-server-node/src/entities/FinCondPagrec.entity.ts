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
import { FinCondPagrecConfig } from './FinCondPagrecConfig.entity';
import { FinPagrec } from './FinPagrec.entity';
import { FinUnitParam } from './FinUnitParam.entity';
import { Mov } from './Mov.entity';
import { MovCotacao } from './MovCotacao.entity';
import { MovCotacaoAnal } from './MovCotacaoAnal.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_cond_pagrec', ['id'], { unique: true })
@Entity('fin_cond_pagrec', { schema: 'public' })
export class FinCondPagrec extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_cond_pagamento', length: 50 })
  siglaCondPagamento: string;

  @Column('varchar', { name: 'considera_feriado', length: 1 })
  consideraFeriado: string;

  @Column('varchar', { name: 'considera_final_sem', length: 1 })
  consideraFinalSem: string;

  @Column('integer', { name: 'qnt_dia_ini' })
  qntDiaIni: number;

  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column('varchar', {
    name: 'tipo_prazo',
    nullable: true,
    length: 1,
  })
  tipoPrazo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(
    () => FinCondPagrecConfig,
    (finCondPagrecConfig) => finCondPagrecConfig.finCondPagRec,
  )
  finCondPagrecConfigs: FinCondPagrecConfig[];

  @OneToMany(() => FinPagrec, (finPagrec) => finPagrec.finCondPagrec)
  finPagrecs: FinPagrec[];

  @OneToMany(() => FinUnitParam, (finUnitParam) => finUnitParam.finCondPagrec)
  finUnitParams: FinUnitParam[];

  @OneToMany(() => Mov, (mov) => mov.finCondPagrec)
  movs: Mov[];

  @OneToMany(() => MovCotacao, (movCotacao) => movCotacao.finCondPagrec)
  movCotacaos: MovCotacao[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c01FinCondPagrec,
  )
  movCotacaoAnals: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c02FinCondPagrec,
  )
  movCotacaoAnals2: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c03FinCondPagrec,
  )
  movCotacaoAnals3: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c04FinCondPagrec,
  )
  movCotacaoAnals4: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c05FinCondPagrec,
  )
  movCotacaoAnals5: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c06FinCondPagrec,
  )
  movCotacaoAnals6: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c07FinCondPagrec,
  )
  movCotacaoAnals7: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c08FinCondPagrec,
  )
  movCotacaoAnals8: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c09FinCondPagrec,
  )
  movCotacaoAnals9: MovCotacaoAnal[];

  @OneToMany(
    () => MovCotacaoAnal,
    (movCotacaoAnal) => movCotacaoAnal.c10FinCondPagrec,
  )
  movCotacaoAnas: MovCotacaoAnal[];
}
