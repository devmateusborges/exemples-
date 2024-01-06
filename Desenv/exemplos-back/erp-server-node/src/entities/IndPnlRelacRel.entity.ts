import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { IndPnl } from './IndPnl.entity';
import { IndRel } from './IndRel.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ind_pnl_relac_rel', ['id'], { unique: true })
@Entity('ind_pnl_relac_rel', { schema: 'public' })
export class IndPnlRelacRel extends BaseEntity {
  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => IndPnl, (indPnl) => indPnl.indPnlRelacRels)
  @JoinColumn([{ name: 'ind_pnl_id', referencedColumnName: 'id' }])
  indPnl: IndPnl;

  @ManyToOne(() => IndRel, (indRel) => indRel.indPnlRelacRels)
  @JoinColumn([{ name: 'ind_rel_id', referencedColumnName: 'id' }])
  indRel: IndRel;
}
