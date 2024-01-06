import { Column, Entity, Index, OneToMany } from 'typeorm';
import { IndFtd } from './IndFtd.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ind_cnd', ['id'], { unique: true })
@Entity('ind_cnd', { schema: 'public' })
export class IndCnd extends BaseEntity {
  @Column('varchar', { name: 'nome', nullable: true, length: 250 })
  nome: string;

  @Column('varchar', { name: 'ativo', nullable: true, length: 1 })
  ativo: string;

  @Column('varchar', { name: 'tipo', nullable: true, length: 2 })
  tipo: string;

  @Column('text', { name: 'config_cnd', nullable: true })
  configCnd: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => IndFtd, (indFtd) => indFtd.indCnd)
  indFtds: IndFtd[];
}
