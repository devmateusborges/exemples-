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
import { OpeCompartTipo } from './OpeCompartTipo.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_compart_medida', ['id'], { unique: true })
@Entity('ope_compart_medida', { schema: 'public' })
export class OpeCompartMedida extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_compart_medida', length: 50 })
  siglaCompartMedida: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(
    () => OpeCompartTipo,
    (opeCompartTipo) => opeCompartTipo.opeCompartMedida,
  )
  opeCompartTipos: OpeCompartTipo[];
}
