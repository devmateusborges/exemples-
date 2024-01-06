import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { GerDevice } from './GerDevice.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_device_param', ['id'], { unique: true })
@Entity('ger_device_param', { schema: 'public' })
export class GerDeviceParam extends BaseEntity {
  @Column('varchar', { name: 'sigla_param', length: 50 })
  siglaParam: string;

  @Column('varchar', {
    name: 'valor_tx',
    nullable: true,
    length: 250,
  })
  valorTx: string;

  @Column('date', { name: 'valor_dt', nullable: true })
  valorDt: string;

  @Column('numeric', {
    name: 'valor_nm',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  valorNm: string;

  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerDevice, (gerDevice) => gerDevice.gerDeviceParams, {
    onDelete: 'CASCADE',
  })
  @JoinColumn([{ name: 'ger_device_id', referencedColumnName: 'id' }])
  gerDevice: GerDevice;
}
