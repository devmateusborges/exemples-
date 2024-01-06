import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { SystemDocumentCategory } from './SystemDocumentCategory.entity';
import { SystemUser } from './SystemUser.entity';
import { TestPai } from './TestPai.entity';
import { FinPagrec } from './FinPagrec.entity';
import { GerPessoa } from './GerPessoa.entity';
import { Mov } from './Mov.entity';
import { OpeCentro1 } from './OpeCentro1.entity';
import { OpeCentro2 } from './OpeCentro2.entity';
import { OpeCentro2Ord } from './OpeCentro2Ord.entity';
import { OpeCompart } from './OpeCompart.entity';
import { OpeCompartOcor } from './OpeCompartOcor.entity';
import { OpeOcor } from './OpeOcor.entity';
import { SystemDocumentGroup } from './SystemDocumentGroup.entity';
import { SystemDocumentUser } from './SystemDocumentUser.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_document', ['id'], { unique: true })
@Entity('system_document', { schema: 'public' })
export class SystemDocument extends BaseEntity {
  @Column('text', { name: 'title', nullable: true })
  title: string;

  @Column('text', { name: 'description', nullable: true })
  description: string;

  @Column('date', { name: 'submission_date', nullable: true })
  submissionDate: string;

  @Column('date', { name: 'archive_date', nullable: true })
  archiveDate: string;

  @Column('text', { name: 'filename', nullable: true })
  filename: string;

  @Column('varchar', {
    name: 'storage_type',
    nullable: true,
    length: 50,
    default: () => "'L'",
  })
  storageType: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(
    () => SystemDocumentCategory,
    (systemDocumentCategory) => systemDocumentCategory.systemDocuments,
  )
  @JoinColumn([{ name: 'category_id', referencedColumnName: 'id' }])
  category: SystemDocumentCategory;

  @OneToOne(() => SystemUser)
  @JoinColumn([{ name: 'system_user_id', referencedColumnName: 'id' }])
  systemUser: SystemUser;

  @ManyToOne(() => TestPai, (testPai) => testPai.systemDocuments)
  @JoinColumn([{ name: 'test_pai_id', referencedColumnName: 'id' }])
  testPai: TestPai;

  @ManyToOne(() => FinPagrec, (finPagrec) => finPagrec.systemDocuments)
  @JoinColumn([{ name: 'fin_pagrec_id', referencedColumnName: 'id' }])
  finPagrec: FinPagrec;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.systemDocuments)
  @JoinColumn([{ name: 'ger_pessoa_id', referencedColumnName: 'id' }])
  gerPessoa: GerPessoa;

  @ManyToOne(() => Mov, (mov) => mov.systemDocuments)
  @JoinColumn([{ name: 'mov_id', referencedColumnName: 'id' }])
  mov: Mov;

  @ManyToOne(() => OpeCentro1, (opeCentro1) => opeCentro1.systemDocuments)
  @JoinColumn([{ name: 'ope_centro1_id', referencedColumnName: 'id' }])
  opeCentro1: OpeCentro1;

  @ManyToOne(() => OpeCentro2, (opeCentro2) => opeCentro2.systemDocuments)
  @JoinColumn([{ name: 'ope_centro2_id', referencedColumnName: 'id' }])
  opeCentro2: OpeCentro2;

  @ManyToOne(
    () => OpeCentro2Ord,
    (opeCentro2Ord) => opeCentro2Ord.systemDocuments,
  )
  @JoinColumn([{ name: 'ope_centro2_ord_id', referencedColumnName: 'id' }])
  opeCentro2Ord: OpeCentro2Ord;

  @ManyToOne(() => OpeCompart, (opeCompart) => opeCompart.systemDocuments)
  @JoinColumn([{ name: 'ope_compart_id', referencedColumnName: 'id' }])
  opeCompart: OpeCompart;

  @ManyToOne(
    () => OpeCompartOcor,
    (opeCompartOcor) => opeCompartOcor.systemDocuments,
  )
  @JoinColumn([{ name: 'ope_compart_ocor_id', referencedColumnName: 'id' }])
  opeCompartOcor: OpeCompartOcor;

  @ManyToOne(() => OpeOcor, (opeOcor) => opeOcor.systemDocuments)
  @JoinColumn([{ name: 'ope_ocor_id', referencedColumnName: 'id' }])
  opeOcor: OpeOcor;

  @OneToMany(
    () => SystemDocumentGroup,
    (systemDocumentGroup) => systemDocumentGroup.document,
  )
  systemDocumentGroups: SystemDocumentGroup[];

  @OneToMany(
    () => SystemDocumentUser,
    (systemDocumentUser) => systemDocumentUser.document,
  )
  systemDocumentUsers: SystemDocumentUser[];
}
