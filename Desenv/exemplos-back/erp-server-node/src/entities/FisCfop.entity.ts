import { Column, Entity, Index, OneToMany } from 'typeorm';
import { MovItemserv } from './MovItemserv.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fis_cfop', ['id'], { unique: true })
@Entity('fis_cfop', { schema: 'public' })
export class FisCfop extends BaseEntity {
  @Column('varchar', { name: 'nr_cfop', length: 50 })
  nrCfop: string;

  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('date', { name: 'data_validade' })
  dataValidade: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => MovItemserv, (movItemserv) => movItemserv.fisCfop)
  movItemservs: MovItemserv[];
}
