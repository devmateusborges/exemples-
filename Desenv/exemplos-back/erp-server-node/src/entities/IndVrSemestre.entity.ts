import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { GerEmpresa } from './GerEmpresa.entity';
import { GerPer } from './GerPer.entity';
import { Ind } from './Ind.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ind_vr_semestre', ['id'], { unique: true })
@Entity('ind_vr_semestre', { schema: 'public' })
export class IndVrSemestre extends BaseEntity {
  @Column('varchar', { name: 'atributo', length: 100 })
  atributo: string;

  @Column('numeric', {
    name: 'valor_real',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorReal: string;

  @Column('numeric', {
    name: 'valor_meta',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorMeta: string;

  @Column('varchar', { name: 'aprovado_exibicao', length: 1 })
  aprovadoExibicao: string;

  @Column('integer', { name: 'ordem', nullable: true, default: () => '0' })
  ordem: number | null;

  @Column('varchar', { name: 'lote', nullable: true, length: 50 })
  lote: string;

  @Column('varchar', {
    name: 'lote_arquivo',
    nullable: true,
    length: 100,
  })
  loteArquivo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerEmpresa, (gerEmpresa) => gerEmpresa.indVrSemestres)
  @JoinColumn([{ name: 'ger_empresa_id', referencedColumnName: 'id' }])
  gerEmpresa: GerEmpresa;

  @ManyToOne(() => GerPer, (gerPer) => gerPer.indVrSemestres)
  @JoinColumn([{ name: 'ger_per_id', referencedColumnName: 'id' }])
  gerPer: GerPer;

  @ManyToOne(() => Ind, (ind) => ind.indVrSemestres)
  @JoinColumn([{ name: 'ind_id', referencedColumnName: 'id' }])
  ind: Ind;
}
