import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { FinClassAgrupGrupo } from './FinClassAgrupGrupo.entity';
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_class_grupo', ['id'], { unique: true })
@Entity('fin_class_grupo', { schema: 'public' })
export class FinClassGrupo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'estrutura', length: 50 })
  estrutura: string;

  @Column('varchar', {
    name: 'sigla_class_grupo',
    nullable: true,
    length: 255,
  })
  siglaClassGrupo: string;

  @Column('smallint', { name: 'nivel', nullable: true })
  nivel: number | null;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => FinClassAgrupGrupo,
    (finClassAgrupGrupo) => finClassAgrupGrupo.finClassGrupo,
  )
  finClassAgrupGrupos: FinClassAgrupGrupo[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
