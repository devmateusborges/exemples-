import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { GerUmedida } from './GerUmedida.entity';
import { SystemUnit } from './SystemUnit.entity';
import { GerItemserv } from './GerItemserv.entity';
import { GerItemservVar } from './GerItemservVar.entity';
import { OpeAtividadeSistema } from './OpeAtividadeSistema.entity';
import { OpeCentro2 } from './OpeCentro2.entity';
import { OpeEspac } from './OpeEspac.entity';
import { OpeEstagio } from './OpeEstagio.entity';
import { OpePeriodo } from './OpePeriodo.entity';
import { OpeTipoSolo } from './OpeTipoSolo.entity';
import { OpeCentro2MapaCoord } from './OpeCentro2MapaCoord.entity';
import { OpeCentro2MapaGeometria } from './OpeCentro2MapaGeometria.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro2_area', ['id'], { unique: true })
@Entity('ope_centro2_area', { schema: 'public' })
export class OpeCentro2Area extends BaseEntity {
  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('numeric', {
    name: 'qnt_area_prod',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  qntAreaProd: string;

  @Column('numeric', {
    name: 'qnt_area_improd',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  qntAreaImprod: string;

  @Column('numeric', {
    name: 'qnt_plantas_estande',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  qntPlantasEstande: string;

  @Column('varchar', {
    name: 'bloco_col',
    nullable: true,
    length: 100,
  })
  blocoCol: string;

  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column('varchar', { name: 'lat_x', nullable: true, length: 100 })
  latX: string;

  @Column('varchar', { name: 'long_y', nullable: true, length: 100 })
  longY: string;

  @Column('varchar', { name: 'alt_z', nullable: true, length: 100 })
  altZ: string;

  @Column('date', { name: 'data_ini_plan', nullable: true })
  dataIniPlan: string;

  @Column('date', { name: 'data_fin_plan', nullable: true })
  dataFinPlan: string;

  @Column('date', { name: 'data_ult_plan', nullable: true })
  dataUltPlan: string;

  @Column('date', { name: 'data_ini_col', nullable: true })
  dataIniCol: string;

  @Column('date', { name: 'data_fin_col', nullable: true })
  dataFinCol: string;

  @Column('date', { name: 'data_ult_col', nullable: true })
  dataUltCol: string;

  @Column('date', { name: 'data_emerg', nullable: true })
  dataEmerg: string;

  @Column('date', { name: 'data_florada_1', nullable: true })
  dataFlorada_1: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => GerUmedida, (gerUmedida) => gerUmedida.opeCentro2Areas)
  @JoinColumn([{ name: 'ger_umedida_id', referencedColumnName: 'id' }])
  gerUmedida: GerUmedida;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerItemserv, (gerItemserv) => gerItemserv.opeCentro2Areas)
  @JoinColumn([{ name: 'ger_itemserv_id', referencedColumnName: 'id' }])
  gerItemserv: GerItemserv;

  @ManyToOne(() => GerItemserv, (gerItemserv) => gerItemserv.opeCentro2Areas2)
  @JoinColumn([{ name: 'ger_itemserv_id_ult', referencedColumnName: 'id' }])
  gerItemservIdUlt: GerItemserv;

  @ManyToOne(
    () => GerItemservVar,
    (gerItemservVar) => gerItemservVar.opeCentro2Areas,
  )
  @JoinColumn([{ name: 'ger_itemserv_var_id', referencedColumnName: 'id' }])
  gerItemservVar: GerItemservVar;

  @ManyToOne(
    () => GerItemservVar,
    (gerItemservVar) => gerItemservVar.opeCentro2Areas2,
  )
  @JoinColumn([{ name: 'ger_itemserv_var_id_ult', referencedColumnName: 'id' }])
  gerItemservVarIdUlt: GerItemservVar;

  @ManyToOne(
    () => OpeAtividadeSistema,
    (opeAtividadeSistema) => opeAtividadeSistema.opeCentro2Areas,
  )
  @JoinColumn([
    { name: 'ope_atividade_sistema_id_col', referencedColumnName: 'id' },
  ])
  opeAtividadeSistemaIdCol: OpeAtividadeSistema;

  @ManyToOne(
    () => OpeAtividadeSistema,
    (opeAtividadeSistema) => opeAtividadeSistema.opeCentro2Areas2,
  )
  @JoinColumn([
    { name: 'ope_atividade_sistema_id_cult', referencedColumnName: 'id' },
  ])
  opeAtividadeSistemaIdCult: OpeAtividadeSistema;

  @ManyToOne(
    () => OpeAtividadeSistema,
    (opeAtividadeSistema) => opeAtividadeSistema.opeCentro2Areas3,
  )
  @JoinColumn([
    { name: 'ope_atividade_sistema_id_plan', referencedColumnName: 'id' },
  ])
  opeAtividadeSistemaIdPlan: OpeAtividadeSistema;

  @ManyToOne(() => OpeCentro2, (opeCentro2) => opeCentro2.opeCentro2Areas, {
    onDelete: 'CASCADE',
  })
  @JoinColumn([{ name: 'ope_centro2_id', referencedColumnName: 'id' }])
  opeCentro2: OpeCentro2;

  @ManyToOne(() => OpeEspac, (opeEspac) => opeEspac.opeCentro2Areas)
  @JoinColumn([{ name: 'ope_espac_id', referencedColumnName: 'id' }])
  opeEspac: OpeEspac;

  @ManyToOne(() => OpeEstagio, (opeEstagio) => opeEstagio.opeCentro2Areas)
  @JoinColumn([{ name: 'ope_estagio_id', referencedColumnName: 'id' }])
  opeEstagio: OpeEstagio;

  @ManyToOne(() => OpePeriodo, (opePeriodo) => opePeriodo.opeCentro2Areas)
  @JoinColumn([{ name: 'ope_periodo_id', referencedColumnName: 'id' }])
  opePeriodo: OpePeriodo;

  @ManyToOne(() => OpeTipoSolo, (opeTipoSolo) => opeTipoSolo.opeCentro2Areas)
  @JoinColumn([{ name: 'ope_tipo_solo_id', referencedColumnName: 'id' }])
  opeTipoSolo: OpeTipoSolo;

  @OneToMany(
    () => OpeCentro2MapaCoord,
    (opeCentro2MapaCoord) => opeCentro2MapaCoord.opeCentro2IdArea,
  )
  opeCentro2MapaCoords: OpeCentro2MapaCoord[];

  @OneToMany(
    () => OpeCentro2MapaGeometria,
    (opeCentro2MapaGeometria) => opeCentro2MapaGeometria.opeCentro2IdArea2,
  )
  opeCentro2MapaGeometrias: OpeCentro2MapaGeometria[];
}
