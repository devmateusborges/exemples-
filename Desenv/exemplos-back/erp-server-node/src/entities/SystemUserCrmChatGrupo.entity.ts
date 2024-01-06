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
import { CrmChatGrupo } from './CrmChatGrupo.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_user_crm_chat_grupo', ['id'], { unique: true })
@Entity('system_user_crm_chat_grupo', { schema: 'public' })
export class SystemUserCrmChatGrupo extends BaseEntity {
  @Column('varchar', {
    name: 'admin',
    length: 36,
    default: () => "'N'",
  })
  admin: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUser)
  @JoinColumn([{ name: 'system_user_id', referencedColumnName: 'id' }])
  systemUser: SystemUser;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => CrmChatGrupo,
    (crmChatGrupo) => crmChatGrupo.systemUserCrmChatGrupos,
  )
  @JoinColumn([{ name: 'crm_chat_grupo_id', referencedColumnName: 'id' }])
  crmChatGrupo: CrmChatGrupo;
}
