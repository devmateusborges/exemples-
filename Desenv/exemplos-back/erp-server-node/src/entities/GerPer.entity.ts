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
import { IndVrAno } from './IndVrAno.entity';
import { IndVrBimestre } from './IndVrBimestre.entity';
import { IndVrDia } from './IndVrDia.entity';
import { IndVrMes } from './IndVrMes.entity';
import { IndVrMeta } from './IndVrMeta.entity';
import { IndVrQuadrimestre } from './IndVrQuadrimestre.entity';
import { IndVrQuinzena } from './IndVrQuinzena.entity';
import { IndVrSemana } from './IndVrSemana.entity';
import { IndVrSemestre } from './IndVrSemestre.entity';
import { IndVrTrimestre } from './IndVrTrimestre.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_per', ['id'], { unique: true })
@Entity('ger_per', { schema: 'public' })
export class GerPer extends BaseEntity {
  @Column('date', { name: 'data_dia_inicial', nullable: true })
  dataDiaInicial: string;

  @Column('varchar', { name: 'dia_nome', nullable: true, length: 50 })
  diaNome: string;

  @Column('date', { name: 'data_semana_inicial', nullable: true })
  dataSemanaInicial: string;

  @Column('varchar', {
    name: 'semana_nome',
    nullable: true,
    length: 50,
  })
  semanaNome: string;

  @Column('date', { name: 'data_quinzena_inicial', nullable: true })
  dataQuinzenaInicial: string;

  @Column('varchar', {
    name: 'quinzena_nome',
    nullable: true,
    length: 50,
  })
  quinzenaNome: string;

  @Column('date', { name: 'data_mes_inicial', nullable: true })
  dataMesInicial: string;

  @Column('varchar', { name: 'mes_nome', nullable: true, length: 50 })
  mesNome: string;

  @Column('date', { name: 'data_bimestre_inicial', nullable: true })
  dataBimestreInicial: string;

  @Column('varchar', {
    name: 'bimestre_nome',
    nullable: true,
    length: 50,
  })
  bimestreNome: string;

  @Column('date', { name: 'data_trimestre_inicial', nullable: true })
  dataTrimestreInicial: string;

  @Column('varchar', {
    name: 'trimestre_nome',
    nullable: true,
    length: 50,
  })
  trimestreNome: string;

  @Column('date', { name: 'data_quadrimestre_inicial', nullable: true })
  dataQuadrimestreInicial: string;

  @Column('varchar', {
    name: 'quadrimestre_nome',
    nullable: true,
    length: 50,
  })
  quadrimestreNome: string;

  @Column('date', { name: 'data_semestre_inicial', nullable: true })
  dataSemestreInicial: string;

  @Column('varchar', {
    name: 'semestre_nome',
    nullable: true,
    length: 50,
  })
  semestreNome: string;

  @Column('date', { name: 'data_ano_inicial', nullable: true })
  dataAnoInicial: string;

  @Column('varchar', { name: 'ano_nome', nullable: true, length: 50 })
  anoNome: string;

  @Column('varchar', {
    name: 'tipo_calend',
    nullable: true,
    length: 3,
  })
  tipoCalend: string;

  @Column('date', { name: 'data_dia_final', nullable: true })
  dataDiaFinal: string;

  @Column('integer', { name: 'dia_numero', nullable: true })
  diaNumero: number | null;

  @Column('date', { name: 'data_semana_final', nullable: true })
  dataSemanaFinal: string;

  @Column('integer', { name: 'semana_numero', nullable: true })
  semanaNumero: number | null;

  @Column('date', { name: 'data_quinzena_final', nullable: true })
  dataQuinzenaFinal: string;

  @Column('integer', { name: 'quinzena_numero', nullable: true })
  quinzenaNumero: number | null;

  @Column('date', { name: 'data_mes_final', nullable: true })
  dataMesFinal: string;

  @Column('integer', { name: 'mes_numero', nullable: true })
  mesNumero: number | null;

  @Column('date', { name: 'data_bimestre_final', nullable: true })
  dataBimestreFinal: string;

  @Column('integer', { name: 'bimestre_numero', nullable: true })
  bimestreNumero: number | null;

  @Column('date', { name: 'data_trimestre_final', nullable: true })
  dataTrimestreFinal: string;

  @Column('integer', { name: 'trimestre_numero', nullable: true })
  trimestreNumero: number | null;

  @Column('date', { name: 'data_quadrimestre_final', nullable: true })
  dataQuadrimestreFinal: string;

  @Column('integer', { name: 'quadrimestre_numero', nullable: true })
  quadrimestreNumero: number | null;

  @Column('date', { name: 'data_semestre_final', nullable: true })
  dataSemestreFinal: string;

  @Column('integer', { name: 'semestre_numero', nullable: true })
  semestreNumero: number | null;

  @Column('date', { name: 'data_ano_final', nullable: true })
  dataAnoFinal: string;

  @Column('integer', { name: 'ano_numero', nullable: true })
  anoNumero: number | null;

  @Column('varchar', { name: 'dia_tipo', nullable: true, length: 1 })
  diaTipo: string;

  @Column('varchar', {
    name: 'semana_tipo',
    nullable: true,
    length: 1,
  })
  semanaTipo: string;

  @Column('varchar', {
    name: 'quinzena_tipo',
    nullable: true,
    length: 1,
  })
  quinzenaTipo: string;

  @Column('varchar', { name: 'mes_tipo', nullable: true, length: 1 })
  mesTipo: string;

  @Column('varchar', {
    name: 'bimestre_tipo',
    nullable: true,
    length: 1,
  })
  bimestreTipo: string;

  @Column('varchar', {
    name: 'trimestre_tipo',
    nullable: true,
    length: 1,
  })
  trimestreTipo: string;

  @Column('varchar', {
    name: 'quadrimestre_tipo',
    nullable: true,
    length: 1,
  })
  quadrimestreTipo: string;

  @Column('varchar', {
    name: 'semestre_tipo',
    nullable: true,
    length: 1,
  })
  semestreTipo: string;

  @Column('varchar', { name: 'ano_tipo', nullable: true, length: 1 })
  anoTipo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerEmpresa, (gerEmpresa) => gerEmpresa.gerPers)
  @JoinColumn([{ name: 'ger_empresa_id', referencedColumnName: 'id' }])
  gerEmpresa: GerEmpresa;

  @OneToMany(() => IndVrAno, (indVrAno) => indVrAno.gerPer)
  indVrAnos: IndVrAno[];

  @OneToMany(() => IndVrBimestre, (indVrBimestre) => indVrBimestre.gerPer)
  indVrBimestres: IndVrBimestre[];

  @OneToMany(() => IndVrDia, (indVrDia) => indVrDia.gerPer)
  indVrDias: IndVrDia[];

  @OneToMany(() => IndVrMes, (indVrMes) => indVrMes.gerPer)
  indVrMes: IndVrMes[];

  @OneToMany(() => IndVrMeta, (indVrMeta) => indVrMeta.gerPer)
  indVrMetas: IndVrMeta[];

  @OneToMany(
    () => IndVrQuadrimestre,
    (indVrQuadrimestre) => indVrQuadrimestre.gerPer,
  )
  indVrQuadrimestres: IndVrQuadrimestre[];

  @OneToMany(() => IndVrQuinzena, (indVrQuinzena) => indVrQuinzena.gerPer)
  indVrQuinzenas: IndVrQuinzena[];

  @OneToMany(() => IndVrSemana, (indVrSemana) => indVrSemana.gerPer)
  indVrSemanas: IndVrSemana[];

  @OneToMany(() => IndVrSemestre, (indVrSemestre) => indVrSemestre.gerPer)
  indVrSemestres: IndVrSemestre[];

  @OneToMany(() => IndVrTrimestre, (indVrTrimestre) => indVrTrimestre.gerPer)
  indVrTrimestres: IndVrTrimestre[];
}
