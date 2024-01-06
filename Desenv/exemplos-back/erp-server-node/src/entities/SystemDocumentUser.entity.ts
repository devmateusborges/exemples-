import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemDocument } from './SystemDocument.entity';
import { SystemUser } from './SystemUser.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_document_user', ['id'], { unique: true })
@Entity('system_document_user', { schema: 'public' })
export class SystemDocumentUser extends BaseEntity {
  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(
    () => SystemDocument,
    (systemDocument) => systemDocument.systemDocumentUsers,
  )
  @JoinColumn([{ name: 'document_id', referencedColumnName: 'id' }])
  document: SystemDocument;

  @OneToOne(() => SystemUser)
  @JoinColumn([{ name: 'system_user_id', referencedColumnName: 'id' }])
  systemUser: SystemUser;
}
