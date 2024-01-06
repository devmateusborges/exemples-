import { Column, Entity, Index } from 'typeorm';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_process_log', ['id'], { unique: true })
@Entity('system_process_log', { schema: 'public' })
export class SystemProcessLog extends BaseEntity {
  @Column('varchar', {
    name: 'type_process',
    nullable: false,
    length: 50,
  })
  typeProcess: string;

  @Column('varchar', {
    name: 'unit_id',
    nullable: true,
    length: 36,
  })
  unitId: string;

  @Column('timestamp without time zone', {
    name: 'date_ini_process',
    nullable: false,
  })
  dateIniProcess: Date;

  @Column('timestamp without time zone', {
    name: 'date_fin_process',
    nullable: true,
  })
  dateFinProcess: Date;

  @Column('text', { name: 'param_process', nullable: false })
  paramProcess: string;

  @Column('varchar', {
    name: 'system_user_id',
    nullable: false,
    length: 36,
  })
  systemUserId: string;

  @Column('varchar', {
    name: 'reversed',
    nullable: false,
    length: 1,
    default: () => 'N',
  })
  reversed: string;
}
