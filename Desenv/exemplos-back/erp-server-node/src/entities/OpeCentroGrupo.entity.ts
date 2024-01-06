import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { OpeCentroConfig } from './OpeCentroConfig.entity';
import { OpeCentroSubtipo } from './OpeCentroSubtipo.entity';
import { SystemUnit } from './SystemUnit.entity';
import { OpeCentroSubgrupo } from './OpeCentroSubgrupo.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro_grupo', ['id'], { unique: true })
@Entity('ope_centro_grupo', { schema: 'public' })
export class OpeCentroGrupo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_centro_grupo', length: 50 })
  siglaCentroGrupo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => OpeCentroConfig,
    (opeCentroConfig) => opeCentroConfig.opeCentroGrupo,
  )
  opeCentroConfigs: OpeCentroConfig[];

  @ManyToOne(
    () => OpeCentroSubtipo,
    (opeCentroSubtipo) => opeCentroSubtipo.opeCentroGrupos,
  )
  @JoinColumn([{ name: 'ope_centro_subtipo_id', referencedColumnName: 'id' }])
  opeCentroSubtipo: OpeCentroSubtipo;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(
    () => OpeCentroSubgrupo,
    (opeCentroSubgrupo) => opeCentroSubgrupo.opeCentroGrupo,
  )
  opeCentroSubgrupos: OpeCentroSubgrupo[];
}
