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
import { OpeCompartStatus } from './OpeCompartStatus.entity';
import { OpeOcorCompartMovDet } from './OpeOcorCompartMovDet.entity';
import { SystemDocument } from './SystemDocument.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_compart_ocor', ['id'], { unique: true })
@Entity('ope_compart_ocor', { schema: 'public' })
export class OpeCompartOcor extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_compart_ocor', length: 50 })
  siglaCompartOcor: string;

  @Column('varchar', { name: 'tipo_ocor', length: 1 })
  tipoOcor: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => OpeCompartStatus,
    (opeCompartStatus) => opeCompartStatus.opeCompartOcors,
  )
  @JoinColumn([{ name: 'ope_compart_status_id', referencedColumnName: 'id' }])
  opeCompartStatus: OpeCompartStatus;

  @OneToMany(
    () => OpeOcorCompartMovDet,
    (opeOcorCompartMovDet) => opeOcorCompartMovDet.opeCompartOcor,
  )
  opeOcorCompartMovDets: OpeOcorCompartMovDet[];

  @OneToMany(
    () => SystemDocument,
    (systemDocument) => systemDocument.opeCompartOcor,
  )
  systemDocuments: SystemDocument[];
}
