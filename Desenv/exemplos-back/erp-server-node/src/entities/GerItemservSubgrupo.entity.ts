import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { GerItemserv } from './GerItemserv.entity';
import { GerItemservGrupo } from './GerItemservGrupo.entity';
import { OpeCentroConfig } from './OpeCentroConfig.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_itemserv_subgrupo', ['id'], { unique: true })
@Entity('ger_itemserv_subgrupo', { schema: 'public' })
export class GerItemservSubgrupo extends BaseEntity {
  @Column('varchar', { name: 'unit_id', length: 36 })
  unitId: string;

  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', {
    name: 'ctb_comp_id',
    nullable: true,
    length: 36,
  })
  ctbCompId: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => GerItemserv,
    (gerItemserv) => gerItemserv.gerItemservSubgrupo,
  )
  gerItemservs: GerItemserv[];

  @ManyToOne(
    () => GerItemservGrupo,
    (gerItemservGrupo) => gerItemservGrupo.gerItemservSubgrupos,
  )
  @JoinColumn([{ name: 'ger_grupo_id', referencedColumnName: 'id' }])
  gerGrupo: GerItemservGrupo;

  @OneToMany(
    () => OpeCentroConfig,
    (opeCentroConfig) => opeCentroConfig.gerItemservSubgrupo,
  )
  opeCentroConfigs: OpeCentroConfig[];
}
