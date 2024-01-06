import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { IndCjdRelacFtd } from './IndCjdRelacFtd.entity';
import { IndCnd } from './IndCnd.entity';
import { IndFtdRelacPrm } from './IndFtdRelacPrm.entity';
import { IndRel } from './IndRel.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ind_ftd', ['id'], { unique: true })
@Entity('ind_ftd', { schema: 'public' })
export class IndFtd extends BaseEntity {
  @Column('varchar', { name: 'nome', nullable: true, length: 250 })
  nome: string;

  @Column('varchar', { name: 'ativo', nullable: true, length: 1 })
  ativo: string;

  @Column('text', { name: 'config_ftd', nullable: true })
  configFtd: string;

  @Column('varchar', {
    name: 'nome_tecnico',
    nullable: true,
    length: 50,
  })
  nomeTecnico: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => IndCjdRelacFtd, (indCjdRelacFtd) => indCjdRelacFtd.indFtd)
  indCjdRelacFtds: IndCjdRelacFtd[];

  @ManyToOne(() => IndCnd, (indCnd) => indCnd.indFtds)
  @JoinColumn([{ name: 'ind_cnd_id', referencedColumnName: 'id' }])
  indCnd: IndCnd;

  @OneToMany(() => IndFtdRelacPrm, (indFtdRelacPrm) => indFtdRelacPrm.indFtd)
  indFtdRelacPrms: IndFtdRelacPrm[];

  @OneToMany(() => IndRel, (indRel) => indRel.indFtd)
  indRels: IndRel[];
}
