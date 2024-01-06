import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { IndPrm } from './IndPrm.entity';
import { IndRel } from './IndRel.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ind_rel_relac_prm', ['id'], { unique: true })
@Entity('ind_rel_relac_prm', { schema: 'public' })
export class IndRelRelacPrm extends BaseEntity {
  @Column('integer', { name: 'ordem_exib' })
  ordemExib: number;

  @Column('json', { name: 'valor_padrao', nullable: true })
  valorPadrao: object | null;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => IndPrm, (indPrm) => indPrm.indRelRelacPrms)
  @JoinColumn([{ name: 'ind_prm_id', referencedColumnName: 'id' }])
  indPrm: IndPrm;

  @ManyToOne(() => IndRel, (indRel) => indRel.indRelRelacPrms)
  @JoinColumn([{ name: 'ind_rel_id', referencedColumnName: 'id' }])
  indRel: IndRel;
}
