import { Column, Entity, Index, OneToMany } from 'typeorm';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_unit', ['id'], { unique: true })
@Entity('system_unit', { schema: 'public' })
export class SystemUnit extends BaseEntity {
  @Column('varchar', { name: 'name', length: 100 })
  name: string;

  @Column('varchar', { name: 'sigla_unit', length: 100 })
  siglaUnit: string;

  @Column('varchar', {
    name: 'img_logo',
    nullable: true,
    length: 100,
  })
  imgLogo: string;

  @Column('varchar', {
    name: 'connection_name',
    nullable: true,
    length: 50,
  })
  connectionName: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;
}
