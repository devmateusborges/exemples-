import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { OpeCentro1 } from './OpeCentro1.entity';
import { OpeCentroConfig } from './OpeCentroConfig.entity';
import { OpeCentroGrupo } from './OpeCentroGrupo.entity';
import { OpeCentroRatFator } from './OpeCentroRatFator.entity';
import { OpeCentroTipo } from './OpeCentroTipo.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro_subtipo', ['id'], { unique: true })
@Entity('ope_centro_subtipo', { schema: 'public' })
export class OpeCentroSubtipo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', {
    name: 'tipo_destinacao',
    nullable: true,
    length: 1,
  })
  tipoDestinacao: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => OpeCentro1, (opeCentro1) => opeCentro1.opeCentroSubtipo)
  opeCentros: OpeCentro1[];

  @OneToMany(
    () => OpeCentroConfig,
    (opeCentroConfig) => opeCentroConfig.opeCentroSubtipo,
  )
  opeCentroConfigs: OpeCentroConfig[];

  @OneToMany(
    () => OpeCentroGrupo,
    (opeCentroGrupo) => opeCentroGrupo.opeCentroSubtipo,
  )
  opeCentroGrupos: OpeCentroGrupo[];

  @OneToMany(
    () => OpeCentroRatFator,
    (opeCentroRatFator) => opeCentroRatFator.opeCentroSubtipo,
  )
  opeCentroRatFators: OpeCentroRatFator[];

  @ManyToOne(
    () => OpeCentroTipo,
    (opeCentroTipo) => opeCentroTipo.opeCentroSubtipos,
  )
  @JoinColumn([{ name: 'ope_centro_tipo_id', referencedColumnName: 'id' }])
  opeCentroTipo: OpeCentroTipo;
}
