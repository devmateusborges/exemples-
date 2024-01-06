import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { IndPnlRelacRel } from './IndPnlRelacRel.entity';
import { IndCjd } from './IndCjd.entity';
import { IndFtd } from './IndFtd.entity';
import { IndRelRelacPrm } from './IndRelRelacPrm.entity';
import { IndRelVar } from './IndRelVar.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ind_rel', ['id'], { unique: true })
@Entity('ind_rel', { schema: 'public' })
export class IndRel extends BaseEntity {
  @Column('varchar', { name: 'nome', nullable: true, length: 250 })
  nome: string;

  @Column('varchar', { name: 'ativo', nullable: true, length: 1 })
  ativo: string;

  @Column('varchar', {
    name: 'nome_tecnico',
    nullable: true,
    length: 100,
  })
  nomeTecnico: string;

  @Column('varchar', {
    name: 'tipo',
    nullable: true,
    length: 1,
    default: () => "'R'",
  })
  tipo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => IndPnlRelacRel, (indPnlRelacRel) => indPnlRelacRel.indRel)
  indPnlRelacRels: IndPnlRelacRel[];

  @ManyToOne(() => IndCjd, (indCjd) => indCjd.indRels)
  @JoinColumn([{ name: 'ind_cjd_id', referencedColumnName: 'id' }])
  indCjd: IndCjd;

  @ManyToOne(() => IndFtd, (indFtd) => indFtd.indRels)
  @JoinColumn([{ name: 'ind_ftd_id', referencedColumnName: 'id' }])
  indFtd: IndFtd;

  @OneToMany(() => IndRelRelacPrm, (indRelRelacPrm) => indRelRelacPrm.indRel)
  indRelRelacPrms: IndRelRelacPrm[];

  @OneToMany(() => IndRelVar, (indRelVar) => indRelVar.indRel)
  indRelVars: IndRelVar[];
}
