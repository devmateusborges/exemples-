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
import { FinClassAgrupGrupo } from './FinClassAgrupGrupo.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_class_agrup', ['id'], { unique: true })
@Entity('fin_class_agrup', { schema: 'public' })
export class FinClassAgrup extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'padrao', length: 1 })
  padrao: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(
    () => FinClassAgrupGrupo,
    (finClassAgrupGrupo) => finClassAgrupGrupo.finClassAgrup,
  )
  finClassAgrupGrupos: FinClassAgrupGrupo[];
}
