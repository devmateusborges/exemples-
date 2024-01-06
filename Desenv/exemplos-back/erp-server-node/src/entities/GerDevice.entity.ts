import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { GerDeviceParam } from './GerDeviceParam.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_device', ['id'], { unique: true })
@Entity('ger_device', { schema: 'public' })
export class GerDevice extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_device', length: 50 })
  siglaDevice: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(() => GerDeviceParam, (gerDeviceParam) => gerDeviceParam.gerDevice)
  gerDeviceParams: GerDeviceParam[];
}
