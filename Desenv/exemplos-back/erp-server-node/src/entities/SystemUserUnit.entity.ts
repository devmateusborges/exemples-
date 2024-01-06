import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { SystemUser } from './SystemUser.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_user_unit', ['id'], { unique: true })
@Entity('system_user_unit', { schema: 'public' })
export class SystemUserUnit extends BaseEntity {
  @Column('varchar', {
    name: 'owner',
    nullable: true,
    length: 1,
    default: () => "'N'",
  })
  owner: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit, {
    onDelete: 'CASCADE',
  })
  @JoinColumn([{ name: 'system_unit_id', referencedColumnName: 'id' }])
  systemUnit: SystemUnit;

  @OneToOne(() => SystemUser, {
    onDelete: 'CASCADE',
  })
  @JoinColumn([{ name: 'system_user_id', referencedColumnName: 'id' }])
  systemUser: SystemUser;
}
