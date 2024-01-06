import { Column, Entity, Index, OneToMany } from 'typeorm';
import { SystemDocument } from './SystemDocument.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_document_category', ['id'], { unique: true })
@Entity('system_document_category', { schema: 'public' })
export class SystemDocumentCategory extends BaseEntity {
  @Column('text', { name: 'name', nullable: true })
  name: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => SystemDocument, (systemDocument) => systemDocument.category)
  systemDocuments: SystemDocument[];
}
