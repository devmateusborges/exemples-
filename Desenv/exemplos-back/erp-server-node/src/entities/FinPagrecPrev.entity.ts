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
import { FinClass } from './FinClass.entity';
import { FinPagrecVersao } from './FinPagrecVersao.entity';
import { GerEmpresa } from './GerEmpresa.entity';
import { GerPessoa } from './GerPessoa.entity';
import { FinPagrecPrevDest } from './FinPagrecPrevDest.entity';
import { FinPagrecPrevVar } from './FinPagrecPrevVar.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_pagrec_prev', ['id'], { unique: true })
@Entity('fin_pagrec_prev', { schema: 'public' })
export class FinPagrecPrev extends BaseEntity {
  @Column('date', { name: 'data_per' })
  dataPer: string;

  @Column('numeric', {
    name: 'valor01',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor01: string;

  @Column('numeric', {
    name: 'valor02',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor02: string;

  @Column('numeric', {
    name: 'valor03',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor03: string;

  @Column('numeric', {
    name: 'valor04',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor04: string;

  @Column('numeric', {
    name: 'valor05',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor05: string;

  @Column('numeric', {
    name: 'valor06',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor06: string;

  @Column('numeric', {
    name: 'valor07',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor07: string;

  @Column('numeric', {
    name: 'valor08',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor08: string;

  @Column('numeric', {
    name: 'valor09',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor09: string;

  @Column('numeric', {
    name: 'valor10',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor10: string;

  @Column('numeric', {
    name: 'valor11',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor11: string;

  @Column('numeric', {
    name: 'valor12',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor12: string;

  @Column('numeric', {
    name: 'valor13',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor13: string;

  @Column('numeric', {
    name: 'valor14',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor14: string;

  @Column('numeric', {
    name: 'valor15',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor15: string;

  @Column('numeric', {
    name: 'valor16',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor16: string;

  @Column('numeric', {
    name: 'valor17',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor17: string;

  @Column('numeric', {
    name: 'valor18',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor18: string;

  @Column('numeric', {
    name: 'valor19',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor19: string;

  @Column('numeric', {
    name: 'valor20',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor20: string;

  @Column('numeric', {
    name: 'valor21',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor21: string;

  @Column('numeric', {
    name: 'valor22',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor22: string;

  @Column('numeric', {
    name: 'valor23',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor23: string;

  @Column('numeric', {
    name: 'valor24',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor24: string;

  @Column('numeric', {
    name: 'valor25',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor25: string;

  @Column('numeric', {
    name: 'valor26',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor26: string;

  @Column('numeric', {
    name: 'valor27',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor27: string;

  @Column('numeric', {
    name: 'valor28',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor28: string;

  @Column('numeric', {
    name: 'valor29',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor29: string;

  @Column('numeric', {
    name: 'valor30',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor30: string;

  @Column('numeric', {
    name: 'valor31',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor31: string;

  @Column('varchar', { name: 'tipo_es', nullable: true, length: 1 })
  tipoEs: string;

  @Column('varchar', {
    name: 'process_id',
    nullable: true,
    length: 36,
  })
  processId: string;

  @Column('date', { name: 'data_valid', nullable: true })
  dataValid: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => FinClass, (finClass) => finClass.finPagrecPrevs)
  @JoinColumn([{ name: 'fin_class_id', referencedColumnName: 'id' }])
  finClass: FinClass;

  @ManyToOne(
    () => FinPagrecVersao,
    (finPagrecVersao) => finPagrecVersao.finPagrecPrevs,
  )
  @JoinColumn([{ name: 'fin_pagrec_versao_id', referencedColumnName: 'id' }])
  finPagrecVersao: FinPagrecVersao;

  @ManyToOne(() => GerEmpresa, (gerEmpresa) => gerEmpresa.finPagrecPrevs)
  @JoinColumn([{ name: 'ger_empresa_id', referencedColumnName: 'id' }])
  gerEmpresa: GerEmpresa;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.finPagrecPrevs)
  @JoinColumn([{ name: 'ger_pessoa_id', referencedColumnName: 'id' }])
  gerPessoa: GerPessoa;

  @OneToMany(
    () => FinPagrecPrevDest,
    (finPagrecPrevDest) => finPagrecPrevDest.finPagrecPrev,
  )
  finPagrecPrevDests: FinPagrecPrevDest[];

  @OneToMany(
    () => FinPagrecPrevVar,
    (finPagrecPrevVar) => finPagrecPrevVar.finPagrecPrev,
  )
  finPagrecPrevVars: FinPagrecPrevVar[];
}
