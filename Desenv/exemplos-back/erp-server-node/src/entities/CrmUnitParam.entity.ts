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

@Index('pk_crm_unit_param', ['id'], { unique: true })
@Entity('crm_unit_param', { schema: 'public' })
export class CrmUnitParam extends BaseEntity {
  @Column('varchar', {
    name: 'abre_crm_mov_email',
    length: 1,
    default: () => "'N'",
  })
  abreCrmMovEmail: string;

  @Column('varchar', {
    name: 'endereco_email',
    nullable: true,
    length: 100,
  })
  enderecoEmail: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'system_unit_id', referencedColumnName: 'id' }])
  systemUnit: SystemUnit;
}
