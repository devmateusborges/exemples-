import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { FisDoc } from './FisDoc.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fis_doc_evento', ['id'], { unique: true })
@Entity('fis_doc_evento', { schema: 'public' })
export class FisDocEvento extends BaseEntity {
  @Column('text', { name: 'xml_retorno' })
  xmlRetorno: string;

  @Column('integer', { name: 'tipo_evento' })
  tipoEvento: number;

  @Column('varchar', { name: 'nr_protocolo', length: 50 })
  nrProtocolo: string;

  @Column('integer', { name: 'qnt_evento', nullable: true })
  qntEvento: number | null;

  @Column('text', { name: 'descricao_evento', nullable: true })
  descricaoEvento: string;

  @Column('text', { name: 'pdf_retorno', nullable: true })
  pdfRetorno: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => FisDoc, (fisDoc) => fisDoc.fisDocEventos)
  @JoinColumn([{ name: 'fis_doc_id', referencedColumnName: 'id' }])
  fisDoc: FisDoc;
}
