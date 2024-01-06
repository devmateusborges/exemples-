import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { BorDispositivo } from './BorDispositivo.entity';
import { MovFrete } from './MovFrete.entity';
import { MovReboque } from './MovReboque.entity';
import { GerCidade } from './GerCidade.entity';
import { SystemUnit } from './SystemUnit.entity';
import { OpeCentro2 } from './OpeCentro2.entity';
import { OpeFrenteTrabalho } from './OpeFrenteTrabalho.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro_equip', ['id'], { unique: true })
@Entity('ope_centro2_equip', { schema: 'public' })
export class OpeCentro2Equip extends BaseEntity {
  @Column('varchar', { name: 'tipo_rodado', length: 100 })
  tipoRodado: string;

  @Column('varchar', { name: 'tipo_carroceria', length: 100 })
  tipoCarroceria: string;

  @Column('varchar', { name: 'placa', nullable: true, length: 100 })
  placa: string;

  @Column('varchar', { name: 'renavam', nullable: true, length: 100 })
  renavam: string;

  @Column('numeric', { name: 'tara', nullable: true, precision: 18, scale: 6 })
  tara: string;

  @Column('numeric', {
    name: 'capacidade_kg',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  capacidadeKg: string;

  @Column('numeric', {
    name: 'capacidade_m3',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  capacidadeM3: string;

  @Column('varchar', {
    name: 'potencia',
    nullable: true,
    length: 100,
  })
  potencia: string;

  @Column('varchar', {
    name: 'nr_chassi',
    nullable: true,
    length: 100,
  })
  nrChassi: string;

  @Column('varchar', {
    name: 'nr_serie',
    nullable: true,
    length: 100,
  })
  nrSerie: string;

  @Column('varchar', { name: 'liberado_abastec', length: 1 })
  liberadoAbastec: string;

  @Column('numeric', {
    name: 'largura',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  largura: string;

  @Column('numeric', {
    name: 'altura',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  altura: string;

  @Column('varchar', {
    name: 'nr_registro_estadual',
    nullable: true,
    length: 50,
  })
  nrRegistroEstadual: string;

  @Column('integer', { name: 'tipo_tracao', nullable: true })
  tipoTracao: number | null;

  @Column('integer', { name: 'tipo_transp_auto_carga', nullable: true })
  tipoTranspAutoCarga: number | null;

  @Column('date', { name: 'data_venc_licenciamento', nullable: true })
  dataVencLicenciamento: string;

  @Column('date', { name: 'data_venc_imposto', nullable: true })
  dataVencImposto: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => BorDispositivo,
    (borDispositivo) => borDispositivo.opeCentro2Equip,
  )
  borDispositivos: BorDispositivo[];

  @OneToMany(() => MovFrete, (movFrete) => movFrete.opeCentro2IdEquip)
  movFretes: MovFrete[];

  @OneToMany(() => MovReboque, (movReboque) => movReboque.opeCentro2IdEquip)
  movReboques: MovReboque[];

  @ManyToOne(() => GerCidade, (gerCidade) => gerCidade.opeCentro2Equips)
  @JoinColumn([{ name: 'ger_cidade_id', referencedColumnName: 'id' }])
  gerCidade: GerCidade;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => OpeCentro2, (opeCentro2) => opeCentro2.opeCentro2Equips, {
    onDelete: 'CASCADE',
  })
  @JoinColumn([{ name: 'ope_centro2_id', referencedColumnName: 'id' }])
  opeCentro2: OpeCentro2;

  @ManyToOne(
    () => OpeFrenteTrabalho,
    (opeFrenteTrabalho) => opeFrenteTrabalho.opeCentro2Equips,
  )
  @JoinColumn([{ name: 'ope_frente_trabalho_id', referencedColumnName: 'id' }])
  opeFrenteTrabalho: OpeFrenteTrabalho;
}
