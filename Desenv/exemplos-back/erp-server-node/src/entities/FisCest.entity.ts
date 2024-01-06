import { Column, Entity, Index, OneToMany } from 'typeorm';
import { FisCestNcm } from './FisCestNcm.entity';
import { GerItemserv } from './GerItemserv.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fis_cest', ['id'], { unique: true })
@Entity('fis_cest', { schema: 'public' })
export class FisCest extends BaseEntity {
  @Column('varchar', { name: 'nr_cest', length: 50 })
  nrCest: string;

  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('date', { name: 'data_validade' })
  dataValidade: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => FisCestNcm, (fisCestNcm) => fisCestNcm.fisCest)
  fisCestNcms: FisCestNcm[];

  @OneToMany(() => GerItemserv, (gerItemserv) => gerItemserv.fisCest)
  gerItemservs: GerItemserv[];
}
