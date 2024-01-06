import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { IndGrupo } from './IndGrupo.entity';
import { IndSubgrupo } from './IndSubgrupo.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ind_grupo_relac_sub', ['id'], { unique: true })
@Entity('ind_grupo_relac_sub', { schema: 'public' })
export class IndGrupoRelacSub extends BaseEntity {
  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => IndGrupo, (indGrupo) => indGrupo.indGrupoRelacSubs)
  @JoinColumn([{ name: 'ind_grupo_id', referencedColumnName: 'id' }])
  indGrupo: IndGrupo;

  @ManyToOne(() => IndGrupo, (indGrupo) => indGrupo.indGrupoRelacSubs2)
  @JoinColumn([{ name: 'ind_grupo_id', referencedColumnName: 'id' }])
  indGrupo_2: IndGrupo;

  @ManyToOne(() => IndSubgrupo, (indSubgrupo) => indSubgrupo.indGrupoRelacSubs)
  @JoinColumn([{ name: 'ind_subgrupo_id', referencedColumnName: 'id' }])
  indSubgrupo: IndSubgrupo;

  @ManyToOne(() => IndSubgrupo, (indSubgrupo) => indSubgrupo.indGrupoRelacSubs2)
  @JoinColumn([{ name: 'ind_subgrupo_id', referencedColumnName: 'id' }])
  indSubgrupo_2: IndSubgrupo;
}
