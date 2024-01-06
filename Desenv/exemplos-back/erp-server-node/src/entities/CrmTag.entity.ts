import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { BaseEntity } from '../shared/bases/base.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';

@Index('pk_crm_tag', ['id'], { unique: true })
@Entity('crm_tag', { schema: 'public' })
export class CrmTag extends BaseEntity {
  @Column('text', { name: 'descritivo' })
  descritivo: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_tag', length: 50 })
  siglaTag: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
