import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { OpeCentroSubtipo } from './OpeCentroSubtipo.entity';
import { SystemUnit } from './SystemUnit.entity';
import { CtbCentro } from './CtbCentro.entity';
import { GerEmpresa } from './GerEmpresa.entity';
import { OpeAtividade } from './OpeAtividade.entity';
import { OpeCentro1 } from './OpeCentro1.entity';
import { OpeCentro2 } from './OpeCentro2.entity';
import { OpeCentroRatPeriodo } from './OpeCentroRatPeriodo.entity';
import { OpePeriodo } from './OpePeriodo.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro2_rat_fator', ['id'], { unique: true })
@Entity('ope_centro_rat_fator', { schema: 'public' })
export class OpeCentroRatFator extends BaseEntity {
  @Column('numeric', {
    name: 'fator_rat',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  fatorRat: string;

  @Column('numeric', {
    name: 'perc_rat',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  percRat: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(
    () => OpeCentroSubtipo,
    (opeCentroSubtipo) => opeCentroSubtipo.opeCentroRatFators,
  )
  @JoinColumn([{ name: 'ope_centro_subtipo_id', referencedColumnName: 'id' }])
  opeCentroSubtipo: OpeCentroSubtipo;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => CtbCentro, (ctbCentro) => ctbCentro.opeCentroRatFators)
  @JoinColumn([{ name: 'ctb_centro_id', referencedColumnName: 'id' }])
  ctbCentro: CtbCentro;

  @ManyToOne(() => GerEmpresa, (gerEmpresa) => gerEmpresa.opeCentroRatFators)
  @JoinColumn([{ name: 'ger_empresa_id', referencedColumnName: 'id' }])
  gerEmpresa: GerEmpresa;

  @ManyToOne(
    () => OpeAtividade,
    (opeAtividade) => opeAtividade.opeCentroRatFators,
  )
  @JoinColumn([{ name: 'ope_atividade_id', referencedColumnName: 'id' }])
  opeAtividade: OpeAtividade;

  @ManyToOne(() => OpeCentro1, (opeCentro1) => opeCentro1.opeCentroRatFators)
  @JoinColumn([{ name: 'ope_centro1_id', referencedColumnName: 'id' }])
  opeCentro1: OpeCentro1;

  @ManyToOne(() => OpeCentro2, (opeCentro2) => opeCentro2.opeCentroRatFators)
  @JoinColumn([{ name: 'ope_centro2_id', referencedColumnName: 'id' }])
  opeCentro2: OpeCentro2;

  @ManyToOne(
    () => OpeCentroRatPeriodo,
    (opeCentroRatPeriodo) => opeCentroRatPeriodo.opeCentroRatFators,
  )
  @JoinColumn([
    { name: 'ope_centro_rat_periodo_id', referencedColumnName: 'id' },
  ])
  opeCentroRatPeriodo: OpeCentroRatPeriodo;

  @ManyToOne(() => OpePeriodo, (opePeriodo) => opePeriodo.opeCentroRatFators)
  @JoinColumn([{ name: 'ope_periodo_id', referencedColumnName: 'id' }])
  opePeriodo: OpePeriodo;
}
