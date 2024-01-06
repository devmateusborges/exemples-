import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { OpeCentro2Ord } from './OpeCentro2Ord.entity';
import { SystemUnit } from './SystemUnit.entity';
import { OpeCentroConfig } from './OpeCentroConfig.entity';
import { OpeCentroPrev } from './OpeCentroPrev.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro2_ord_tipo', ['id'], { unique: true })
@Entity('ope_centro2_ord_tipo', { schema: 'public' })
export class OpeCentro2OrdTipo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_ord_tipo', length: 50 })
  siglaOrdTipo: string;

  @Column('varchar', {
    name: 'valida_saldo_area_aberta',
    nullable: true,
    length: 1,
    default: () => "'S'",
  })
  validaSaldoAreaAberta: string;

  @Column('varchar', {
    name: 'valida_prev_itemserv',
    nullable: true,
    length: 1,
    default: () => "'S'",
  })
  validaPrevItemserv: string;

  @Column('varchar', {
    name: 'valida_prev_rec',
    nullable: true,
    length: 1,
    default: () => "'S'",
  })
  validaPrevRec: string;

  @Column('varchar', {
    name: 'valida_regra_config',
    nullable: true,
    length: 1,
    default: () => "'S'",
  })
  validaRegraConfig: string;

  @Column('varchar', {
    name: 'valida_tipo_executor',
    nullable: true,
    length: 2,
    default: () => "'S'",
  })
  validaTipoExecutor: string;

  @Column('varchar', {
    name: 'valida_rec_equip',
    nullable: true,
    length: 1,
    default: () => "'S'",
  })
  validaRecEquip: string;

  @Column('varchar', {
    name: 'valida_rec_pessoa',
    nullable: true,
    length: 1,
    default: () => "'S'",
  })
  validaRecPessoa: string;

  @Column('varchar', {
    name: 'valida_itemserv_i',
    nullable: true,
    length: 1,
    default: () => "'S'",
  })
  validaItemservI: string;

  @Column('varchar', {
    name: 'valida_itemserv_s',
    nullable: true,
    length: 1,
    default: () => "'S'",
  })
  validaItemservS: string;

  @Column('varchar', {
    name: 'valida_tipo_prop_rec_equip',
    nullable: true,
    length: 2,
    default: () => "'S'",
  })
  validaTipoPropRecEquip: string;

  @Column('varchar', {
    name: 'valida_tipo_prop_rec_pessoa',
    nullable: true,
    length: 2,
    default: () => "'S'",
  })
  validaTipoPropRecPessoa: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => OpeCentro2Ord,
    (opeCentro2Ord) => opeCentro2Ord.opeCentro2OrdTipo,
  )
  opeCentro2Ords: OpeCentro2Ord[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(
    () => OpeCentroConfig,
    (opeCentroConfig) => opeCentroConfig.opeCentro2OrdTipo,
  )
  opeCentroConfigs: OpeCentroConfig[];

  @OneToMany(
    () => OpeCentroPrev,
    (opeCentroPrev) => opeCentroPrev.opeCentro2OrdTipo,
  )
  opeCentroPrevs: OpeCentroPrev[];
}
