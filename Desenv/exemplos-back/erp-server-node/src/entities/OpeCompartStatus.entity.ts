import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { OpeCompart } from './OpeCompart.entity';
import { OpeCompartOcor } from './OpeCompartOcor.entity';
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_compart_status', ['id'], { unique: true })
@Entity('ope_compart_status', { schema: 'public' })
export class OpeCompartStatus extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_compart_status', length: 50 })
  siglaCompartStatus: string;

  @Column('varchar', { name: 'tipo_status', length: 1 })
  tipoStatus: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => OpeCompart, (opeCompart) => opeCompart.opeCompartStatus)
  opeComparts: OpeCompart[];

  @OneToMany(
    () => OpeCompartOcor,
    (opeCompartOcor) => opeCompartOcor.opeCompartStatus,
  )
  opeCompartOcors: OpeCompartOcor[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
