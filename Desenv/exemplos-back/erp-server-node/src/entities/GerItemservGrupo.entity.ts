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
import { GerItemservSubgrupo } from './GerItemservSubgrupo.entity';
import { OpeCentroConfig } from './OpeCentroConfig.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_itemserv_grupo', ['id'], { unique: true })
@Entity('ger_itemserv_grupo', { schema: 'public' })
export class GerItemservGrupo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(
    () => GerItemservSubgrupo,
    (gerItemservSubgrupo) => gerItemservSubgrupo.gerGrupo,
  )
  gerItemservSubgrupos: GerItemservSubgrupo[];

  @OneToMany(
    () => OpeCentroConfig,
    (opeCentroConfig) => opeCentroConfig.gerItemservGrupo,
  )
  opeCentroConfigs: OpeCentroConfig[];
}
