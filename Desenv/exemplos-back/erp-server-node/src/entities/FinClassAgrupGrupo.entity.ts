import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { FinClassAgrup } from './FinClassAgrup.entity';
import { FinClassGrupo } from './FinClassGrupo.entity';
import { FinClass } from './FinClass.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_class_agrup_grupo', ['id'], { unique: true })
@Entity('fin_class_agrup_grupo', { schema: 'public' })
export class FinClassAgrupGrupo extends BaseEntity {
  @Column('smallint', { name: 'nivel', nullable: true })
  nivel: number | null;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => FinClassAgrup,
    (finClassAgrup) => finClassAgrup.finClassAgrupGrupos,
  )
  @JoinColumn([{ name: 'fin_class_agrup_id', referencedColumnName: 'id' }])
  finClassAgrup: FinClassAgrup;

  @ManyToOne(
    () => FinClassGrupo,
    (finClassGrupo) => finClassGrupo.finClassAgrupGrupos,
  )
  @JoinColumn([{ name: 'fin_class_grupo_id', referencedColumnName: 'id' }])
  finClassGrupo: FinClassGrupo;

  @ManyToOne(() => FinClass, (finClass) => finClass.finClassAgrupGrupos)
  @JoinColumn([{ name: 'fin_class_id', referencedColumnName: 'id' }])
  finClass: FinClass;
}
