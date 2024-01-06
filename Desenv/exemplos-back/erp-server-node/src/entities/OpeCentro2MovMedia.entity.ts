import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { GerItemserv } from './GerItemserv.entity';
import { GerMarcaModelo } from './GerMarcaModelo.entity';
import { OpeCentro2 } from './OpeCentro2.entity';
import { OpeCompart } from './OpeCompart.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro2_compart', ['id'], { unique: true })
@Entity('ope_centro2_mov_media', { schema: 'public' })
export class OpeCentro2MovMedia extends BaseEntity {
  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column('numeric', {
    name: 'qnt_media_min',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  qntMediaMin: string;

  @Column('numeric', {
    name: 'qnt_media_max',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  qntMediaMax: string;

  @Column('numeric', {
    name: 'capacidade',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  capacidade: string;

  @Column('date', { name: 'dt_valid_ini' })
  dtValidIni: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => GerItemserv,
    (gerItemserv) => gerItemserv.opeCentro2MovMedias,
  )
  @JoinColumn([{ name: 'ger_itemserv_id', referencedColumnName: 'id' }])
  gerItemserv: GerItemserv;

  @ManyToOne(
    () => GerMarcaModelo,
    (gerMarcaModelo) => gerMarcaModelo.opeCentro2MovMedias,
  )
  @JoinColumn([{ name: 'ger_marca_modelo_id', referencedColumnName: 'id' }])
  gerMarcaModelo: GerMarcaModelo;

  @ManyToOne(() => OpeCentro2, (opeCentro2) => opeCentro2.opeCentro2MovMedias, {
    onDelete: 'CASCADE',
  })
  @JoinColumn([{ name: 'ope_centro2_id', referencedColumnName: 'id' }])
  opeCentro2: OpeCentro2;

  @ManyToOne(() => OpeCompart, (opeCompart) => opeCompart.opeCentro2MovMedias)
  @JoinColumn([{ name: 'ope_compart_id', referencedColumnName: 'id' }])
  opeCompart: OpeCompart;
}
