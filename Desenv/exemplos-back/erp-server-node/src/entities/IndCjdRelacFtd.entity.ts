import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { IndCjd } from './IndCjd.entity';
import { IndFtd } from './IndFtd.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ind_cjd_relac_ftd', ['id'], { unique: true })
@Entity('ind_cjd_relac_ftd', { schema: 'public' })
export class IndCjdRelacFtd extends BaseEntity {
  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => IndCjd, (indCjd) => indCjd.indCjdRelacFtds)
  @JoinColumn([{ name: 'ind_cjd_id', referencedColumnName: 'id' }])
  indCjd: IndCjd;

  @ManyToOne(() => IndFtd, (indFtd) => indFtd.indCjdRelacFtds)
  @JoinColumn([{ name: 'ind_ftd_id', referencedColumnName: 'id' }])
  indFtd: IndFtd;
}
