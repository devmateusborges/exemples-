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
import { OpeCentro2 } from './OpeCentro2.entity';
import { OpeCompart } from './OpeCompart.entity';
import { OpeOcorMov } from './OpeOcorMov.entity';
import { OpeOcorMovDet } from './OpeOcorMovDet.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_ocor_mov_dest', ['id'], { unique: true })
@Entity('ope_ocor_mov_dest', { schema: 'public' })
export class OpeOcorMovDest extends BaseEntity {
  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => OpeCentro2, (opeCentro2) => opeCentro2.opeOcorMovDests)
  @JoinColumn([{ name: 'ope_centro2_id', referencedColumnName: 'id' }])
  opeCentro2: OpeCentro2;

  @ManyToOne(() => OpeCompart, (opeCompart) => opeCompart.opeOcorMovDests)
  @JoinColumn([{ name: 'ope_compart_id', referencedColumnName: 'id' }])
  opeCompart: OpeCompart;

  @ManyToOne(() => OpeOcorMov, (opeOcorMov) => opeOcorMov.opeOcorMovDests, {
    onDelete: 'CASCADE',
    onUpdate: 'CASCADE',
  })
  @JoinColumn([{ name: 'ope_ocor_mov_id', referencedColumnName: 'id' }])
  opeOcorMov: OpeOcorMov;

  @OneToMany(
    () => OpeOcorMovDet,
    (opeOcorMovDet) => opeOcorMovDet.opeOcorMovDest,
  )
  opeOcorMovDets: OpeOcorMovDet[];
}
