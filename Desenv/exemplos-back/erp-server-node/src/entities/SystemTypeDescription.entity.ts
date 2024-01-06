import { Column, Entity, Index } from 'typeorm';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('idx_system_type_description', ['fieldName', 'tableName', 'valueType'], {
  unique: true,
})
@Index('pk_system_type_description', ['id'], { unique: true })
@Entity('system_type_description', { schema: 'public' })
export class SystemTypeDescription extends BaseEntity {
  @Column('varchar', { name: 'table_name', length: 100 })
  tableName: string;

  @Column('varchar', { name: 'field_name', length: 100 })
  fieldName: string;

  @Column('varchar', { name: 'value_type', length: 50 })
  valueType: string;

  @Column('varchar', { name: 'description_type', length: 100 })
  descriptionType: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;
}
