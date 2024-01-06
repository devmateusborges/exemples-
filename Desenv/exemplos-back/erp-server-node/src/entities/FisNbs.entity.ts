import { Column, Entity, Index, OneToMany } from 'typeorm';
import { FisIbpt } from './FisIbpt.entity';
import { GerItemserv } from './GerItemserv.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fis_nbs', ['id'], { unique: true })
@Entity('fis_nbs', { schema: 'public' })
export class FisNbs extends BaseEntity {
  @Column('varchar', { name: 'nr_nbs', length: 50 })
  nrNbs: string;

  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('date', { name: 'data_validade' })
  dataValidade: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => FisIbpt, (fisIbpt) => fisIbpt.fisNbs)
  fisIbpts: FisIbpt[];

  @OneToMany(() => GerItemserv, (gerItemserv) => gerItemserv.fisNbs)
  gerItemservs: GerItemserv[];
}
