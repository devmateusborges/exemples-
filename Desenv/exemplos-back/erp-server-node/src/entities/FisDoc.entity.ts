import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { FisDocTipo } from './FisDocTipo.entity';
import { SystemUnit } from './SystemUnit.entity';
import { GerEmpresa } from './GerEmpresa.entity';
import { Mov } from './Mov.entity';
import { FisDocEvento } from './FisDocEvento.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fis_doc', ['id'], { unique: true })
@Entity('fis_doc', { schema: 'public' })
export class FisDoc extends BaseEntity {
  @Column('timestamp without time zone', { name: 'data_emissao' })
  dataEmissao: Date;

  @Column('varchar', { name: 'chave', nullable: true, length: 50 })
  chave: string;

  @Column('integer', { name: 'numero' })
  numero: number;

  @Column('varchar', { name: 'serie', length: 3 })
  serie: string;

  @Column('integer', { name: 'numero_ini', nullable: true })
  numeroIni: number | null;

  @Column('integer', { name: 'numero_fin', nullable: true })
  numeroFin: number | null;

  @Column('timestamp without time zone', {
    name: 'data_autorizado',
    nullable: true,
  })
  dataAutorizado: Date | null;

  @Column('timestamp without time zone', {
    name: 'data_cancelado',
    nullable: true,
  })
  dataCancelado: Date | null;

  @Column('timestamp without time zone', {
    name: 'data_encerrado',
    nullable: true,
  })
  dataEncerrado: Date | null;

  @Column('text', { name: 'xml_assinado', nullable: true })
  xmlAssinado: string;

  @Column('integer', { name: 'ambiente' })
  ambiente: number;

  @Column('integer', { name: 'tipo_emissao' })
  tipoEmissao: number;

  @Column('integer', { name: 'status_sefaz', nullable: true })
  statusSefaz: number | null;

  @Column('text', { name: 'xml_protocolado', nullable: true })
  xmlProtocolado: string;

  @Column('text', { name: 'pdf_emitido', nullable: true })
  pdfEmitido: string;

  @Column('integer', { name: 'numero_pre', nullable: true })
  numeroPre: number | null;

  @Column('varchar', { name: 'serie_pre', nullable: true, length: 3 })
  seriePre: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => FisDocTipo, (fisDocTipo) => fisDocTipo.fisDocs)
  @JoinColumn([{ name: 'fis_doc_tipo_id', referencedColumnName: 'id' }])
  fisDocTipo: FisDocTipo;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerEmpresa, (gerEmpresa) => gerEmpresa.fisDocs)
  @JoinColumn([{ name: 'ger_empresa_id', referencedColumnName: 'id' }])
  gerEmpresa: GerEmpresa;

  @ManyToOne(() => Mov, (mov) => mov.fisDocs)
  @JoinColumn([{ name: 'mov_id', referencedColumnName: 'id' }])
  mov: Mov;

  @OneToMany(() => FisDocEvento, (fisDocEvento) => fisDocEvento.fisDoc)
  fisDocEventos: FisDocEvento[];
}
