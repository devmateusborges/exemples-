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
import { CtbContaGrupo } from './CtbContaGrupo.entity';
import { CtbContaVersao } from './CtbContaVersao.entity';
import { CtbLancDet } from './CtbLancDet.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ctb_conta', ['id'], { unique: true })
@Entity('ctb_conta', { schema: 'public' })
export class CtbConta extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_conta', length: 50 })
  siglaConta: string;

  @Column('varchar', { name: 'tipo_variacao', length: 1 })
  tipoVariacao: string;

  @Column('varchar', { name: 'tipo_dc', length: 1 })
  tipoDc: string;

  @Column('varchar', { name: 'tipo_conta', length: 2 })
  tipoConta: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => CtbContaGrupo, (ctbContaGrupo) => ctbContaGrupo.ctbContas)
  @JoinColumn([{ name: 'ctb_conta_grupo_id', referencedColumnName: 'id' }])
  ctbContaGrupo: CtbContaGrupo;

  @ManyToOne(() => CtbContaVersao, (ctbContaVersao) => ctbContaVersao.ctbContas)
  @JoinColumn([{ name: 'ctb_conta_versao_id', referencedColumnName: 'id' }])
  ctbContaVersao: CtbContaVersao;

  @OneToMany(() => CtbLancDet, (ctbLancDet) => ctbLancDet.ctbConta)
  ctbLancDets: CtbLancDet[];
}
