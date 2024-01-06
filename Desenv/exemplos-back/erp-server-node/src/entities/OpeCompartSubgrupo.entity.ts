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
import { OpeCompart } from './OpeCompart.entity';
import { SystemUnit } from './SystemUnit.entity';
import { OpeCompartGrupo } from './OpeCompartGrupo.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_compart_subgrupo', ['id'], { unique: true })
@Entity('ope_compart_subgrupo', { schema: 'public' })
export class OpeCompartSubgrupo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_compart_subgrupo', length: 50 })
  siglaCompartSubgrupo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => OpeCentroConfig,
    (opeCentroConfig) => opeCentroConfig.opeCompartSubgrupo,
  )
  opeCentroConfigs: OpeCentroConfig[];

  @OneToMany(() => OpeCompart, (opeCompart) => opeCompart.opeCompartSubgrupo)
  opeComparts: OpeCompart[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => OpeCompartGrupo,
    (opeCompartGrupo) => opeCompartGrupo.opeCompartSubgrupos,
  )
  @JoinColumn([{ name: 'ope_compart_grupo_id', referencedColumnName: 'id' }])
  opeCompartGrupo: OpeCompartGrupo;
}
