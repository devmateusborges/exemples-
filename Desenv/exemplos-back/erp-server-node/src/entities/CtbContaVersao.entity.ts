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
import { CtbContaGrupo } from './CtbContaGrupo.entity';
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ctb_conta_versao', ['id'], { unique: true })
@Entity('ctb_conta_versao', { schema: 'public' })
export class CtbContaVersao extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_versao', length: 50 })
  siglaVersao: string;

  @Column('varchar', { name: 'versao_atual', default: () => "'N'" })
  versaoAtual: string;

  @Column('date', { name: 'data_valid_ini' })
  dataValidIni: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => CtbConta, (ctbConta) => ctbConta.ctbContaVersao)
  ctbContas: CtbConta[];

  @OneToMany(
    () => CtbContaGrupo,
    (ctbContaGrupo) => ctbContaGrupo.ctbContaVersao,
  )
  ctbContaGrupos: CtbContaGrupo[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
