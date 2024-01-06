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
import { OpeCentro2Area } from './OpeCentro2Area.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_atividade_sistema', ['id'], { unique: true })
@Entity('ope_atividade_sistema', { schema: 'public' })
export class OpeAtividadeSistema extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', {
    name: 'sigla_atividade_grupo',
    nullable: true,
    length: 50,
  })
  siglaAtividadeGrupo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(
    () => OpeCentro2Area,
    (opeCentro2Area) => opeCentro2Area.opeAtividadeSistemaIdCol,
  )
  opeCentro2Areas: OpeCentro2Area[];

  @OneToMany(
    () => OpeCentro2Area,
    (opeCentro2Area) => opeCentro2Area.opeAtividadeSistemaIdCult,
  )
  opeCentro2Areas2: OpeCentro2Area[];

  @OneToMany(
    () => OpeCentro2Area,
    (opeCentro2Area) => opeCentro2Area.opeAtividadeSistemaIdPlan,
  )
  opeCentro2Areas3: OpeCentro2Area[];
}
