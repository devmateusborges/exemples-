import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { SystemUser } from './SystemUser.entity';
import { SystemUnit } from './SystemUnit.entity';
import { CrmChatMsg } from './CrmChatMsg.entity';
import { SystemUserCrmChatGrupo } from './SystemUserCrmChatGrupo.entity';
import { BaseEntity } from '../shared/bases/base.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';

@Index('pk_crm_chat_grupo', ['id'], { unique: true })
@Entity('crm_chat_grupo', { schema: 'public' })
export class CrmChatGrupo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_chat_grupo', length: 50 })
  siglaChatGrupo: string;

  @Column('varchar', {
    name: 'tipo',
    length: 1,
    default: () => "'G'",
  })
  tipo: string;

  @Column('varchar', { name: 'senha', nullable: true, length: 100 })
  senha: string;

  @Column('varchar', {
    name: 'acesso_privado',
    length: 1,
    default: () => "'N'",
  })
  acessoPrivado: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUser)
  @JoinColumn([{ name: 'system_user_id_dest', referencedColumnName: 'id' }])
  systemUserIdDest: SystemUser;

  @OneToOne(() => SystemUser)
  @JoinColumn([{ name: 'system_user_id_orig', referencedColumnName: 'id' }])
  systemUserIdOrig: SystemUser;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(() => CrmChatMsg, (crmChatMsg) => crmChatMsg.crmChatGrupo)
  crmChatMsgs: CrmChatMsg[];

  @OneToMany(
    () => SystemUserCrmChatGrupo,
    (systemUserCrmChatGrupo) => systemUserCrmChatGrupo.crmChatGrupo,
  )
  systemUserCrmChatGrupos: SystemUserCrmChatGrupo[];
}
