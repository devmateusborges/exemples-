import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { FisCest } from './FisCest.entity';
import { FisNcm } from './FisNcm.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fis_cest_ncm', ['id'], { unique: true })
@Entity('fis_cest_ncm', { schema: 'public' })
export class FisCestNcm extends BaseEntity {
  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => FisCest, (fisCest) => fisCest.fisCestNcms)
  @JoinColumn([{ name: 'fis_cest_id', referencedColumnName: 'id' }])
  fisCest: FisCest;

  @ManyToOne(() => FisNcm, (fisNcm) => fisNcm.fisCestNcms)
  @JoinColumn([{ name: 'fis_ncm_id', referencedColumnName: 'id' }])
  fisNcm: FisNcm;
}
