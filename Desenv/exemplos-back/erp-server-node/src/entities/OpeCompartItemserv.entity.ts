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
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_compart_itemserv', ['id'], { unique: true })
@Entity('ope_compart_itemserv', { schema: 'public' })
export class OpeCompartItemserv extends BaseEntity {
  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'ger_itemserv_id', length: 36 })
  gerItemservId: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => OpeCompart, (opeCompart) => opeCompart.opeCompartItemservs)
  @JoinColumn([{ name: 'ope_compart_id', referencedColumnName: 'id' }])
  opeCompart: OpeCompart;
}
