import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUser } from './SystemUser.entity';
import { SystemUnit } from './SystemUnit.entity';
import { GerProcessoBloq } from './GerProcessoBloq.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_processo_bloq_user', ['id'], { unique: true })
@Entity('ger_processo_bloq_user', { schema: 'public' })
export class GerProcessoBloqUser extends BaseEntity {
  @Column('varchar', {
    name: 'tipo_bloq',
    nullable: true,
    length: 255,
  })
  tipoBloq: string;

  @OneToOne(() => SystemUser)
  @JoinColumn([{ name: 'system_user_id', referencedColumnName: 'id' }])
  systemUser: SystemUser;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(
    () => GerProcessoBloq,
    (gerProcessoBloq) => gerProcessoBloq.gerProcessoBloqUsers,
  )
  @JoinColumn([{ name: 'ger_processo_bloq_id', referencedColumnName: 'id' }])
  gerProcessoBloq: GerProcessoBloq;
}
