import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { CtbComp } from './CtbComp.entity';
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ctb_comp_grupo', ['id'], { unique: true })
@Entity('ctb_comp_grupo', { schema: 'public' })
export class CtbCompGrupo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_comp_grupo', length: 50 })
  siglaCompGrupo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => CtbComp, (ctbComp) => ctbComp.ctbCompGrupo)
  ctbComps: CtbComp[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
