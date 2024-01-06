import { Column, Entity, Index, OneToMany } from 'typeorm';
import { IndCjdRelacFtd } from './IndCjdRelacFtd.entity';
import { IndRel } from './IndRel.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ind_cjd', ['id'], { unique: true })
@Entity('ind_cjd', { schema: 'public' })
export class IndCjd extends BaseEntity {
  @Column('varchar', { name: 'nome', nullable: true, length: 250 })
  nome: string;

  @Column('varchar', { name: 'ativo', nullable: true, length: 1 })
  ativo: string;

  @Column('varchar', {
    name: 'nome_tecnico',
    nullable: true,
    length: 50,
  })
  nomeTecnico: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => IndCjdRelacFtd, (indCjdRelacFtd) => indCjdRelacFtd.indCjd)
  indCjdRelacFtds: IndCjdRelacFtd[];

  @OneToMany(() => IndRel, (indRel) => indRel.indCjd)
  indRels: IndRel[];
}
