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
import { SystemUnit } from './SystemUnit.entity';
import { OpeCompartSubgrupo } from './OpeCompartSubgrupo.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_compart_grupo', ['id'], { unique: true })
@Entity('ope_compart_grupo', { schema: 'public' })
export class OpeCompartGrupo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_compart_grupo', length: 50 })
  siglaCompartGrupo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => OpeCentroConfig,
    (opeCentroConfig) => opeCentroConfig.opeCompartGrupo,
  )
  opeCentroConfigs: OpeCentroConfig[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(
    () => OpeCompartSubgrupo,
    (opeCompartSubgrupo) => opeCompartSubgrupo.opeCompartGrupo,
  )
  opeCompartSubgrupos: OpeCompartSubgrupo[];
}
