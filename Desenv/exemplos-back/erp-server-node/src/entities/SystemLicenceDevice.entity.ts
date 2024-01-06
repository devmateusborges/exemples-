import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemLicence } from './SystemLicence.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_licence_device', ['id'], { unique: true })
@Entity('system_licence_device', { schema: 'public' })
export class SystemLicenceDevice extends BaseEntity {
  @Column('varchar', { name: 'sigla_device', length: 100 })
  siglaDevice: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(
    () => SystemLicence,
    (systemLicence) => systemLicence.systemLicenceDevices,
  )
  @JoinColumn([{ name: 'system_licence_id', referencedColumnName: 'id' }])
  systemLicence: SystemLicence;
}
