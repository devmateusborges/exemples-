import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUser } from './SystemUser.entity';
import { SystemUnit } from './SystemUnit.entity';
import { CrmMov } from './CrmMov.entity';
import { BaseEntity } from '../shared/bases/base.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';

@Index('pk_crm_mov_hist', ['id'], { unique: true })
@Entity('crm_mov_hist', { schema: 'public' })
export class CrmMovHist extends BaseEntity {
  @Column('timestamp without time zone', { name: 'data_hist' })
  dataHist: Date;

  @Column('text', { name: 'descritivo' })
  descritivo: string;

  @Column('varchar', {
    name: 'visual_ext',
    length: 1,
    default: () => "'N'",
  })
  visualExt: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUser)
  @JoinColumn([{ name: 'system_user_id_hist', referencedColumnName: 'id' }])
  systemUserIdHist: SystemUser;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => CrmMov, (crmMov) => crmMov.crmMovHists)
  @JoinColumn([{ name: 'crm_mov_id', referencedColumnName: 'id' }])
  crmMov: CrmMov;
}
