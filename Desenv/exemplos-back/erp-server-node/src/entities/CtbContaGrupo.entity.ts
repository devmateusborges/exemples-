import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { CtbConta } from './CtbConta.entity';
import { SystemUnit } from './SystemUnit.entity';
import { CtbContaVersao } from './CtbContaVersao.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ctb_conta_grupo', ['id'], { unique: true })
@Entity('ctb_conta_grupo', { schema: 'public' })
export class CtbContaGrupo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_conta_grupo', length: 50 })
  siglaContaGrupo: string;

  @Column('varchar', { name: 'estrutura', length: 50 })
  estrutura: string;

  @Column('smallint', { name: 'nivel', nullable: true })
  nivel: number | null;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => CtbConta, (ctbConta) => ctbConta.ctbContaGrupo)
  ctbContas: CtbConta[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => CtbContaVersao,
    (ctbContaVersao) => ctbContaVersao.ctbContaGrupos,
  )
  @JoinColumn([{ name: 'ctb_conta_versao_id', referencedColumnName: 'id' }])
  ctbContaVersao: CtbContaVersao;
}
