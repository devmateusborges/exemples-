import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { GerItemserv } from './GerItemserv.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_itemserv_localizacao', ['id'], { unique: true })
@Entity('ger_itemserv_local', { schema: 'public' })
export class GerItemservLocal extends BaseEntity {
  @Column('varchar', { name: 'desc_local1', length: 50 })
  descLocal1: string;

  @Column('varchar', {
    name: 'desc_local2',
    nullable: true,
    length: 100,
  })
  descLocal2: string;

  @Column('varchar', {
    name: 'desc_local3',
    nullable: true,
    length: 100,
  })
  descLocal3: string;

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

  @ManyToOne(() => GerItemserv, (gerItemserv) => gerItemserv.gerItemservLocals)
  @JoinColumn([{ name: 'ger_itemserv_id', referencedColumnName: 'id' }])
  gerItemserv: GerItemserv;
}
