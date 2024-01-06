import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { FisNbs } from './FisNbs.entity';
import { FisNcm } from './FisNcm.entity';
import { GerUf } from './GerUf.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fis_ibpt', ['id'], { unique: true })
@Entity('fis_ibpt', { schema: 'public' })
export class FisIbpt extends BaseEntity {
  @Column('date', { name: 'data_validade_ini' })
  dataValidadeIni: string;

  @Column('date', { name: 'data_validade_fin' })
  dataValidadeFin: string;

  @Column('numeric', {
    name: 'perc_nacional',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  percNacional: string;

  @Column('numeric', {
    name: 'perc_importado',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  percImportado: string;

  @Column('numeric', {
    name: 'perc_municipal',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  percMunicipal: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => FisNbs, (fisNbs) => fisNbs.fisIbpts)
  @JoinColumn([{ name: 'fis_nbs_id', referencedColumnName: 'id' }])
  fisNbs: FisNbs;

  @ManyToOne(() => FisNcm, (fisNcm) => fisNcm.fisIbpts)
  @JoinColumn([{ name: 'fis_ncm_id', referencedColumnName: 'id' }])
  fisNcm: FisNcm;

  @ManyToOne(() => GerUf, (gerUf) => gerUf.fisIbpts)
  @JoinColumn([{ name: 'ger_uf_id', referencedColumnName: 'id' }])
  gerUf: GerUf;
}
