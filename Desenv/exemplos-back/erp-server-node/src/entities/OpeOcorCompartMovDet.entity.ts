import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { OpeCompart } from './OpeCompart.entity';
import { OpeOcorCompartMov } from './OpeOcorCompartMov.entity';
import { OpeCompartOcor } from './OpeCompartOcor.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_compart_mov_det', ['id'], { unique: true })
@Entity('ope_ocor_compart_mov_det', { schema: 'public' })
export class OpeOcorCompartMovDet extends BaseEntity {
  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column('numeric', {
    name: 'qnt_medicao',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  qntMedicao: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => OpeCompart, (opeCompart) => opeCompart.opeOcorCompartMovDets)
  @JoinColumn([{ name: 'ope_compart_id', referencedColumnName: 'id' }])
  opeCompart: OpeCompart;

  @ManyToOne(
    () => OpeOcorCompartMov,
    (opeOcorCompartMov) => opeOcorCompartMov.opeOcorCompartMovDets,
  )
  @JoinColumn([{ name: 'ope_compart_mov_id', referencedColumnName: 'id' }])
  opeCompartMov: OpeOcorCompartMov;

  @ManyToOne(
    () => OpeCompartOcor,
    (opeCompartOcor) => opeCompartOcor.opeOcorCompartMovDets,
  )
  @JoinColumn([{ name: 'ope_compart_ocor_id', referencedColumnName: 'id' }])
  opeCompartOcor: OpeCompartOcor;
}
