import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { Mov } from './Mov.entity';
import { MovTipo } from './MovTipo.entity';
import { SystemUnit } from './SystemUnit.entity';
import { GerNumeracao } from './GerNumeracao.entity';
import { MovOperacaoStatus } from './MovOperacaoStatus.entity';
import { OpeCentroConfig } from './OpeCentroConfig.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_mov_operacao', ['id'], { unique: true })
@Entity('mov_operacao', { schema: 'public' })
export class MovOperacao extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_mov_operacao', length: 50 })
  siglaMovOperacao: string;

  @Column('integer', { name: 'finalidade_doc' })
  finalidadeDoc: number;

  @Column('varchar', { name: 'tipo_es', nullable: true, length: 1 })
  tipoEs: string;

  @Column('text', { name: 'configuracao', nullable: true })
  configuracao: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => Mov, (mov) => mov.movOperacao)
  movs: Mov[];

  @ManyToOne(() => MovTipo, (movTipo) => movTipo.movOperacaos)
  @JoinColumn([{ name: 'mov_tipo_id', referencedColumnName: 'id' }])
  movTipo: MovTipo;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerNumeracao, (gerNumeracao) => gerNumeracao.movOperacaos)
  @JoinColumn([{ name: 'ger_numeracao_id', referencedColumnName: 'id' }])
  gerNumeracao: GerNumeracao;

  @OneToMany(
    () => MovOperacaoStatus,
    (movOperacaoStatus) => movOperacaoStatus.movOperacao,
  )
  movOperacaoStatuses: MovOperacaoStatus[];

  @OneToMany(
    () => MovOperacaoStatus,
    (movOperacaoStatus) => movOperacaoStatus.movOperacaoIdProx,
  )
  movOperacaoStatuses2: MovOperacaoStatus[];

  @OneToMany(
    () => OpeCentroConfig,
    (opeCentroConfig) => opeCentroConfig.movOperacao,
  )
  opeCentroConfigs: OpeCentroConfig[];
}
