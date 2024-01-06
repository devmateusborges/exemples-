import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { OpeOcorMov } from './OpeOcorMov.entity';
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_ocor_tipo', ['id'], { unique: true })
@Entity('ope_ocor_tipo', { schema: 'public' })
export class OpeOcorTipo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_ocor_tipo', length: 50 })
  siglaOcorTipo: string;

  @Column('varchar', { name: 'tipo', length: 1 })
  tipo: string;

  @Column('varchar', { name: 'obrig_ope_compart', length: 1 })
  obrigOpeCompart: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => OpeOcorMov, (opeOcorMov) => opeOcorMov.opeOcorTipo)
  opeOcorMovs: OpeOcorMov[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
