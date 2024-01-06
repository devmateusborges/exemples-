import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { FinCondPagrec } from './FinCondPagrec.entity';
import { FinDocTipo } from './FinDocTipo.entity';
import { FinPagrecTipo } from './FinPagrecTipo.entity';
import { GerEmpresa } from './GerEmpresa.entity';
import { GerPessoa } from './GerPessoa.entity';
import { OpeCentroRatTipo } from './OpeCentroRatTipo.entity';
import { FinPagrecClass } from './FinPagrecClass.entity';
import { FinPagrecOrigem } from './FinPagrecOrigem.entity';
import { FinPagrecParc } from './FinPagrecParc.entity';
import { FisTributacao } from './FisTributacao.entity';
import { OpeCentroDest } from './OpeCentroDest.entity';
import { SystemDocument } from './SystemDocument.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_pagrec', ['id'], { unique: true })
@Entity('fin_pagrec', { schema: 'public' })
export class FinPagrec extends BaseEntity {
  @Column('integer', { name: 'numero_parc_total', default: () => '1' })
  numeroParcTotal: number;

  @Column('varchar', { name: 'tipo_es', length: 1 })
  tipoEs: string;

  @Column('varchar', { name: 'numero_doc_pagrec', length: 50 })
  numeroDocPagrec: string;

  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column('date', { name: 'data_mov' })
  dataMov: string;

  @Column('numeric', {
    name: 'valor_pagrec',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valorPagrec: string;

  @Column('varchar', {
    name: 'process_id',
    nullable: true,
    length: 36,
  })
  processId: string;

  @Column('date', { name: 'data_valid', nullable: true })
  dataValid: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => FinCondPagrec, (finCondPagrec) => finCondPagrec.finPagrecs)
  @JoinColumn([{ name: 'fin_cond_pagrec_id', referencedColumnName: 'id' }])
  finCondPagrec: FinCondPagrec;

  @ManyToOne(() => FinDocTipo, (finDocTipo) => finDocTipo.finPagrecs)
  @JoinColumn([{ name: 'fin_doc_tipo_id', referencedColumnName: 'id' }])
  finDocTipo: FinDocTipo;

  @ManyToOne(() => FinPagrecTipo, (finPagrecTipo) => finPagrecTipo.finPagrecs)
  @JoinColumn([{ name: 'fin_pagrec_tipo_id', referencedColumnName: 'id' }])
  finPagrecTipo: FinPagrecTipo;

  @ManyToOne(() => GerEmpresa, (gerEmpresa) => gerEmpresa.finPagrecs)
  @JoinColumn([{ name: 'ger_empresa_id', referencedColumnName: 'id' }])
  gerEmpresa: GerEmpresa;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.finPagrecs)
  @JoinColumn([{ name: 'ger_pessoa_id', referencedColumnName: 'id' }])
  gerPessoa: GerPessoa;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.finPagrecs2)
  @JoinColumn([{ name: 'ger_pessoa_id_pagrec', referencedColumnName: 'id' }])
  gerPessoaIdPagrec: GerPessoa;

  @ManyToOne(
    () => OpeCentroRatTipo,
    (opeCentroRatTipo) => opeCentroRatTipo.finPagrecs,
  )
  @JoinColumn([{ name: 'ope_centro_rat_tipo_id', referencedColumnName: 'id' }])
  opeCentroRatTipo: OpeCentroRatTipo;

  @OneToMany(() => FinPagrecClass, (finPagrecClass) => finPagrecClass.finPagrec)
  finPagrecClasses: FinPagrecClass[];

  @OneToMany(
    () => FinPagrecOrigem,
    (finPagrecOrigem) => finPagrecOrigem.finPagrec,
  )
  finPagrecOrigems: FinPagrecOrigem[];

  @OneToMany(
    () => FinPagrecOrigem,
    (finPagrecOrigem) => finPagrecOrigem.finPagrecIdOrigem,
  )
  finPagrecOrigems2: FinPagrecOrigem[];

  @OneToMany(() => FinPagrecParc, (finPagrecParc) => finPagrecParc.finPagrec)
  finPagrecParcs: FinPagrecParc[];

  @OneToMany(() => FisTributacao, (fisTributacao) => fisTributacao.finPagrec)
  fisTributacaos: FisTributacao[];

  @OneToMany(() => OpeCentroDest, (opeCentroDest) => opeCentroDest.finPagrec)
  opeCentroDests: OpeCentroDest[];

  @OneToMany(() => SystemDocument, (systemDocument) => systemDocument.finPagrec)
  systemDocuments: SystemDocument[];
}
