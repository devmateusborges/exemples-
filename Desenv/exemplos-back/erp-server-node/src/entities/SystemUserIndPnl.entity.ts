import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { IndPnl } from './IndPnl.entity';
import { SystemUser } from './SystemUser.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_user_ind_pnl', ['id'], { unique: true })
@Index('idx_system_user_ind_pnl_pnl', ['indPnlId'], {})
@Index('idx_system_user_ind_pnl_user', ['systemUserId'], {})
@Entity('system_user_ind_pnl', { schema: 'public' })
export class SystemUserIndPnl extends BaseEntity {
  @Column('varchar', {
    name: 'system_user_id',
    nullable: true,
    length: 36,
  })
  systemUserId: string;

  @Column('varchar', {
    name: 'ind_pnl_id',
    nullable: true,
    length: 36,
  })
  indPnlId: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => IndPnl, (indPnl) => indPnl.systemUserIndPnls)
  @JoinColumn([{ name: 'ind_pnl_id', referencedColumnName: 'id' }])
  indPnl: IndPnl;

  @OneToOne(() => SystemUser, {
    onDelete: 'CASCADE',
  })
  @JoinColumn([{ name: 'system_user_id', referencedColumnName: 'id' }])
  systemUser: SystemUser;
}
