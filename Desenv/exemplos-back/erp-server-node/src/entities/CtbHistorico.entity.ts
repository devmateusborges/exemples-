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
import { CtbLanc } from './CtbLanc.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ctb_historico', ['id'], { unique: true })
@Entity('ctb_historico', { schema: 'public' })
export class CtbHistorico extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_historico', length: 50 })
  siglaHistorico: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(() => CtbLanc, (ctbLanc) => ctbLanc.ctbHistorico)
  ctbLancs: CtbLanc[];
}
