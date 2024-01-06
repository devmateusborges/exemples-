import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_unit_preference', ['id'], { unique: true })
@Entity('system_unit_preference', { schema: 'public' })
export class SystemUnitPreference extends BaseEntity {
  @Column('text', { name: 'value', nullable: true })
  value: string;

  @Column('varchar', { name: 'object_type', length: 36 })
  objectType: string;

  @Column('varchar', { name: 'object_id', length: 36 })
  objectId: string;

  @Column('varchar', { name: 'preference_description', length: 150 })
  preferenceDescription: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'system_unit_id', referencedColumnName: 'id' }])
  systemUnit: SystemUnit;
}
