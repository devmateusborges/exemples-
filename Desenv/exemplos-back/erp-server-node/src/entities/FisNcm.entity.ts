import { Column, Entity, Index, OneToMany } from 'typeorm';
import { FisCestNcm } from './FisCestNcm.entity';
import { FisIbpt } from './FisIbpt.entity';
import { GerItemserv } from './GerItemserv.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fis_ncm', ['id'], { unique: true })
@Entity('fis_ncm', { schema: 'public' })
export class FisNcm extends BaseEntity {
  @Column('varchar', { name: 'nr_ncm', length: 50 })
  nrNcm: string;

  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('date', { name: 'data_validade' })
  dataValidade: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => FisCestNcm, (fisCestNcm) => fisCestNcm.fisNcm)
  fisCestNcms: FisCestNcm[];

  @OneToMany(() => FisIbpt, (fisIbpt) => fisIbpt.fisNcm)
  fisIbpts: FisIbpt[];

  @OneToMany(() => GerItemserv, (gerItemserv) => gerItemserv.fisNcm)
  gerItemservs: GerItemserv[];
}
