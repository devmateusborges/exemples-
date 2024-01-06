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

@Index('pk_crm_chat_msg', ['id'], { unique: true })
@Entity('crm_chat_msg', { schema: 'public' })
export class CrmChatMsg extends BaseEntity {
  @Column('text', { name: 'corpo', nullable: true })
  corpo: string;

  @Column('date', { name: 'data_msg', nullable: true })
  dataMsg: string;

  @Column('varchar', { name: 'ativo', nullable: true, length: 1 })
  ativo: string;

  @Column('varchar', {
    name: 'origem_sistema',
    length: 1,
    default: () => "'N'",
  })
  origemSistema: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUser)
  @JoinColumn([{ name: 'system_user_id_orig', referencedColumnName: 'id' }])
  systemUserIdOrig: SystemUser;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => CrmChatGrupo, (crmChatGrupo) => crmChatGrupo.crmChatMsgs)
  @JoinColumn([{ name: 'crm_chat_grupo_id', referencedColumnName: 'id' }])
  crmChatGrupo: CrmChatGrupo;
}
