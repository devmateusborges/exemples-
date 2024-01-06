import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { OpeCentro2 } from './OpeCentro2.entity';
import { OpeCentroConfig } from './OpeCentroConfig.entity';
import { SystemUnit } from './SystemUnit.entity';
import { CtbComp } from './CtbComp.entity';
import { OpeCentroGrupo } from './OpeCentroGrupo.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro_subgrupo', ['id'], { unique: true })
@Entity('ope_centro_subgrupo', { schema: 'public' })
export class OpeCentroSubgrupo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_centro_subgrupo', length: 50 })
  siglaCentroSubgrupo: string;

  @Column('varchar', { name: 'icon', nullable: true, length: 50 })
  icon: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => OpeCentro2, (opeCentro2) => opeCentro2.opeCentroSubgrupo)
  opeCentros: OpeCentro2[];

  @OneToMany(
    () => OpeCentroConfig,
    (opeCentroConfig) => opeCentroConfig.opeCentroSubgrupo,
  )
  opeCentroConfigs: OpeCentroConfig[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => CtbComp, (ctbComp) => ctbComp.opeCentroSubgrupos)
  @JoinColumn([{ name: 'ctb_comp_id', referencedColumnName: 'id' }])
  ctbComp: CtbComp;

  @ManyToOne(
    () => OpeCentroGrupo,
    (opeCentroGrupo) => opeCentroGrupo.opeCentroSubgrupos,
  )
  @JoinColumn([{ name: 'ope_centro_grupo_id', referencedColumnName: 'id' }])
  opeCentroGrupo: OpeCentroGrupo;
}
