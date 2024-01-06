import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { OpeCompartMedida } from './OpeCompartMedida.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_compart_tipo', ['id'], { unique: true })
@Entity('ope_compart_tipo', { schema: 'public' })
export class OpeCompartTipo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_compart_tipo', length: 50 })
  siglaCompartTipo: string;

  @Column('varchar', { name: 'tipo_compart', length: 1 })
  tipoCompart: string;

  @Column('numeric', {
    name: 'qnt_lonas',
    precision: 18,
    scale: 3,
    default: () => '1',
  })
  qntLonas: string;

  @Column('numeric', {
    name: 'qnt_sulco_min',
    precision: 18,
    scale: 3,
    default: () => '0',
  })
  qntSulcoMin: string;

  @Column('numeric', {
    name: 'qnt_sulco_max',
    nullable: true,
    precision: 18,
    scale: 3,
    default: () => '0',
  })
  qntSulcoMax: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => OpeCompartMedida,
    (opeCompartMedida) => opeCompartMedida.opeCompartTipos,
  )
  @JoinColumn([{ name: 'ope_compart_medida_id', referencedColumnName: 'id' }])
  opeCompartMedida: OpeCompartMedida;
}
