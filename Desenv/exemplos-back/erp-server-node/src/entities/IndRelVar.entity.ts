import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { IndRel } from './IndRel.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ind_rel_var', ['id'], { unique: true })
@Entity('ind_rel_var', { schema: 'public' })
export class IndRelVar extends BaseEntity {
  @Column('varchar', { name: 'var_nome_tecnico', length: 50 })
  varNomeTecnico: string;

  @Column('varchar', { name: 'var_nome_descritivo', length: 50 })
  varNomeDescritivo: string;

  @Column('varchar', { name: 'var_agrupavel', length: 1 })
  varAgrupavel: string;

  @Column('integer', { name: 'ordem_padrao', default: () => '0' })
  ordemPadrao: number;

  @Column('numeric', {
    name: 'largura',
    nullable: true,
    precision: 18,
    scale: 2,
  })
  largura: string;

  @Column('varchar', { name: 'visivel', nullable: true, length: 1 })
  visivel: string;

  @Column('varchar', {
    name: 'var_nome_tecnico_prefixo',
    nullable: true,
    length: 50,
  })
  varNomeTecnicoPrefixo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => IndRel, (indRel) => indRel.indRelVars)
  @JoinColumn([{ name: 'ind_rel_id', referencedColumnName: 'id' }])
  indRel: IndRel;
}
