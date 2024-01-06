import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { CrmMov } from './CrmMov.entity';
import { BaseEntity } from '../shared/bases/base.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';

@Index('pk_crm_mov_tag', ['id'], { unique: true })
@Entity('crm_mov_tag', { schema: 'public' })
export class CrmMovTag extends BaseEntity {
  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => CrmMov, (crmMov) => crmMov.crmMovTags)
  @JoinColumn([{ name: 'crm_mov_id', referencedColumnName: 'id' }])
  crmMov: CrmMov;
}
