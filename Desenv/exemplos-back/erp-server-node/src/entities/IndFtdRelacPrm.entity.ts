import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { IndFtd } from './IndFtd.entity';
import { IndPrm } from './IndPrm.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ind_ftd_relac_prm', ['id'], { unique: true })
@Entity('ind_ftd_relac_prm', { schema: 'public' })
export class IndFtdRelacPrm extends BaseEntity {
  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => IndFtd, (indFtd) => indFtd.indFtdRelacPrms)
  @JoinColumn([{ name: 'ind_ftd_id', referencedColumnName: 'id' }])
  indFtd: IndFtd;

  @ManyToOne(() => IndPrm, (indPrm) => indPrm.indFtdRelacPrms)
  @JoinColumn([{ name: 'ind_prm_id', referencedColumnName: 'id' }])
  indPrm: IndPrm;
}
