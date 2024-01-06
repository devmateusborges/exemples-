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
import { FinPagrecClass } from './FinPagrecClass.entity';
import { FinPagrecPrev } from './FinPagrecPrev.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_class', ['id'], { unique: true })
@Entity('fin_class', { schema: 'public' })
export class FinClass extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'tipo_es', length: 1 })
  tipoEs: string;

  @Column('varchar', { name: 'tipo_fluxo', length: 2 })
  tipoFluxo: string;

  @Column('varchar', { name: 'fixo_variavel', length: 1 })
  fixoVariavel: string;

  @Column('varchar', {
    name: 'sigla_class',
    nullable: true,
    length: 15,
  })
  siglaClass: string;

  @Column('varchar', { name: 'tipo_prev', nullable: true, length: 1 })
  tipoPrev: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(
    () => FinClassAgrupGrupo,
    (finClassAgrupGrupo) => finClassAgrupGrupo.finClass,
  )
  finClassAgrupGrupos: FinClassAgrupGrupo[];

  @OneToMany(() => FinPagrecClass, (finPagrecClass) => finPagrecClass.finClass)
  finPagrecClasses: FinPagrecClass[];

  @OneToMany(() => FinPagrecPrev, (finPagrecPrev) => finPagrecPrev.finClass)
  finPagrecPrevs: FinPagrecPrev[];
}
