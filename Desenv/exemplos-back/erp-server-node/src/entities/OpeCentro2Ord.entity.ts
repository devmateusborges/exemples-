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
import { GerEmpresa } from './GerEmpresa.entity';
import { GerPessoaEndereco } from './GerPessoaEndereco.entity';
import { OpeCentro2 } from './OpeCentro2.entity';
import { OpeCentro2OrdStatus } from './OpeCentro2OrdStatus.entity';
import { OpeCentro2OrdTipo } from './OpeCentro2OrdTipo.entity';
import { OpeCentro2Pessoa } from './OpeCentro2Pessoa.entity';
import { OpeCentroVersao } from './OpeCentroVersao.entity';
import { OpeFrenteTrabalho } from './OpeFrenteTrabalho.entity';
import { OpePeriodo } from './OpePeriodo.entity';
import { OpeCentro2OrdAtiv } from './OpeCentro2OrdAtiv.entity';
import { OpeCentro2OrdDest } from './OpeCentro2OrdDest.entity';
import { SystemDocument } from './SystemDocument.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro2_ord', ['id'], { unique: true })
@Entity('ope_centro2_ord', { schema: 'public' })
export class OpeCentro2Ord extends BaseEntity {
  @Column('date', { name: 'data_ini_exec' })
  dataIniExec: string;

  @Column('date', { name: 'data_fin_exec' })
  dataFinExec: string;

  @Column('date', { name: 'data_status' })
  dataStatus: string;

  @Column('varchar', {
    name: 'observacao_interna',
    nullable: true,
    length: 250,
  })
  observacaoInterna: string;

  @Column('varchar', {
    name: 'observacao_externa',
    nullable: true,
    length: 250,
  })
  observacaoExterna: string;

  @Column('date', { name: 'data_ini_exec_prev', nullable: true })
  dataIniExecPrev: string;

  @Column('date', { name: 'data_fin_exec_prev', nullable: true })
  dataFinExecPrev: string;

  @Column('varchar', {
    name: 'process_id',
    nullable: true,
    length: 36,
  })
  processId: string;

  @Column('varchar', {
    name: 'numero_ord',
    nullable: true,
    length: 50,
  })
  numeroOrd: string;

  @Column('date', { name: 'data_valid', nullable: true })
  dataValid: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerEmpresa, (gerEmpresa) => gerEmpresa.opeCentro2Ords)
  @JoinColumn([{ name: 'ger_empresa_id', referencedColumnName: 'id' }])
  gerEmpresa: GerEmpresa;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.opeCentro2Ords,
  )
  @JoinColumn([
    { name: 'ger_pessoa_endereco_id_exec', referencedColumnName: 'id' },
  ])
  gerPessoaEnderecoIdExec: GerPessoaEndereco;

  @ManyToOne(() => OpeCentro2, (opeCentro2) => opeCentro2.opeCentro2Ords)
  @JoinColumn([{ name: 'ope_centro2_id', referencedColumnName: 'id' }])
  opeCentro2: OpeCentro2;

  @ManyToOne(
    () => OpeCentro2OrdStatus,
    (opeCentro2OrdStatus) => opeCentro2OrdStatus.opeCentro2Ords,
  )
  @JoinColumn([
    { name: 'ope_centro2_ord_status_id', referencedColumnName: 'id' },
  ])
  opeCentro2OrdStatus: OpeCentro2OrdStatus;

  @ManyToOne(
    () => OpeCentro2OrdTipo,
    (opeCentro2OrdTipo) => opeCentro2OrdTipo.opeCentro2Ords,
  )
  @JoinColumn([{ name: 'ope_centro2_ord_tipo_id', referencedColumnName: 'id' }])
  opeCentro2OrdTipo: OpeCentro2OrdTipo;

  @ManyToOne(
    () => OpeCentro2Pessoa,
    (opeCentro2Pessoa) => opeCentro2Pessoa.opeCentro2Ords,
  )
  @JoinColumn([
    { name: 'ope_centro2_pessoa_id_solic', referencedColumnName: 'id' },
  ])
  opeCentro2PessoaIdSolic: OpeCentro2Pessoa;

  @ManyToOne(
    () => OpeCentroVersao,
    (opeCentroVersao) => opeCentroVersao.opeCentro2Ords,
  )
  @JoinColumn([{ name: 'ope_centro_versao_id', referencedColumnName: 'id' }])
  opeCentroVersao: OpeCentroVersao;

  @ManyToOne(
    () => OpeFrenteTrabalho,
    (opeFrenteTrabalho) => opeFrenteTrabalho.opeCentro2Ords,
  )
  @JoinColumn([{ name: 'ope_frente_trabalho_id', referencedColumnName: 'id' }])
  opeFrenteTrabalho: OpeFrenteTrabalho;

  @ManyToOne(() => OpePeriodo, (opePeriodo) => opePeriodo.opeCentro2Ords)
  @JoinColumn([{ name: 'ope_periodo_id', referencedColumnName: 'id' }])
  opePeriodo: OpePeriodo;

  @OneToMany(
    () => OpeCentro2OrdAtiv,
    (opeCentro2OrdAtiv) => opeCentro2OrdAtiv.opeCentro2Ord,
  )
  opeCentro2OrdAtivs: OpeCentro2OrdAtiv[];

  @OneToMany(
    () => OpeCentro2OrdDest,
    (opeCentro2OrdDest) => opeCentro2OrdDest.opeCentro2Ord,
  )
  opeCentro2OrdDests: OpeCentro2OrdDest[];

  @OneToMany(
    () => SystemDocument,
    (systemDocument) => systemDocument.opeCentro2Ord,
  )
  systemDocuments: SystemDocument[];
}
