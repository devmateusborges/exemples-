import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { OpeOcorMovDet } from './OpeOcorMovDet.entity';
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_ocor_status', ['id'], { unique: true })
@Entity('ope_ocor_status', { schema: 'public' })
export class OpeOcorStatus extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_ocor_status', length: 50 })
  siglaOcorStatus: string;

  @Column('varchar', { name: 'tipo_status', length: 1 })
  tipoStatus: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => OpeOcorMovDet,
    (opeOcorMovDet) => opeOcorMovDet.opeOcorStatus,
  )
  opeOcorMovDets: OpeOcorMovDet[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
