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
import { FinUnitParam } from './FinUnitParam.entity';
import { OpeCentro2 } from './OpeCentro2.entity';
import { OpeCentroDest } from './OpeCentroDest.entity';
import { OpeCentroRatPeriodo } from './OpeCentroRatPeriodo.entity';
import { SystemUnit } from './SystemUnit.entity';
import { OpeCentroVersao } from './OpeCentroVersao.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro_rat_tipo', ['id'], { unique: true })
@Entity('ope_centro_rat_tipo', { schema: 'public' })
export class OpeCentroRatTipo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', {
    name: 'tipo_ps',
    length: 1,
    default: () => "'P'",
  })
  tipoPs: string;

  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column('varchar', {
    name: 'tipo_apur',
    length: 1,
    default: () => "'P'",
  })
  tipoApur: string;

  @Column('varchar', {
    name: 'sigla_centro_rat_tipo',
    nullable: true,
    length: 50,
  })
  siglaCentroRatTipo: string;

  @Column('varchar', {
    name: 'tipo_fator',
    length: 1,
    default: () => "'1'",
  })
  tipoFator: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => FinPagrec, (finPagrec) => finPagrec.opeCentroRatTipo)
  finPagrecs: FinPagrec[];

  @OneToMany(
    () => FinUnitParam,
    (finUnitParam) => finUnitParam.opeCentroRatTipo,
  )
  finUnitParams: FinUnitParam[];

  @OneToMany(() => OpeCentro2, (opeCentro2) => opeCentro2.opeCentroRatTipo)
  opeCentros: OpeCentro2[];

  @OneToMany(
    () => OpeCentroDest,
    (opeCentroDest) => opeCentroDest.opeCentroRatTipo,
  )
  opeCentroDests: OpeCentroDest[];

  @OneToMany(
    () => OpeCentroRatPeriodo,
    (opeCentroRatPeriodo) => opeCentroRatPeriodo.opeCentroRatTipo,
  )
  opeCentroRatPeriodos: OpeCentroRatPeriodo[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => OpeCentroVersao,
    (opeCentroVersao) => opeCentroVersao.opeCentroRatTipos,
  )
  @JoinColumn([{ name: 'ope_centro_versao_id', referencedColumnName: 'id' }])
  opeCentroVersao: OpeCentroVersao;
}
