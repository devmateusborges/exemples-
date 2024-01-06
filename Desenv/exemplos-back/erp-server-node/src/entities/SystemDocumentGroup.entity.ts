import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemDocument } from './SystemDocument.entity';
import { SystemGroup } from './SystemGroup.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_document_group', ['id'], { unique: true })
@Entity('system_document_group', { schema: 'public' })
export class SystemDocumentGroup extends BaseEntity {
  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(
    () => SystemDocument,
    (systemDocument) => systemDocument.systemDocumentGroups,
  )
  @JoinColumn([{ name: 'document_id', referencedColumnName: 'id' }])
  document: SystemDocument;

  @ManyToOne(
    () => SystemGroup,
    (systemGroup) => systemGroup.systemDocumentGroups,
  )
  @JoinColumn([{ name: 'system_group_id', referencedColumnName: 'id' }])
  systemGroup: SystemGroup;
}
