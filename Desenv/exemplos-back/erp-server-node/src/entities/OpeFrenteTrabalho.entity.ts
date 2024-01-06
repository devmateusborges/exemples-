import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { OpeCentro2Equip } from './OpeCentro2Equip.entity';
import { OpeCentro2Ord } from './OpeCentro2Ord.entity';
import { OpeCentro2OrdAtiv } from './OpeCentro2OrdAtiv.entity';
import { OpeCentro2ParamPer } from './OpeCentro2ParamPer.entity';
import { OpeCentro2Pessoa } from './OpeCentro2Pessoa.entity';
import { SystemUnit } from './SystemUnit.entity';
import { GerEmpresa } from './GerEmpresa.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_frente_trabalho', ['id'], { unique: true })
@Entity('ope_frente_trabalho', { schema: 'public' })
export class OpeFrenteTrabalho extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', {
    name: 'sigla_frente_trabalho',
    nullable: true,
    length: 50,
  })
  siglaFrenteTrabalho: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => OpeCentro2Equip,
    (opeCentro2Equip) => opeCentro2Equip.opeFrenteTrabalho,
  )
  opeCentro2Equips: OpeCentro2Equip[];

  @OneToMany(
    () => OpeCentro2Ord,
    (opeCentro2Ord) => opeCentro2Ord.opeFrenteTrabalho,
  )
  opeCentro2Ords: OpeCentro2Ord[];

  @OneToMany(
    () => OpeCentro2OrdAtiv,
    (opeCentro2OrdAtiv) => opeCentro2OrdAtiv.opeFrenteTrabalho,
  )
  opeCentro2OrdAtivs: OpeCentro2OrdAtiv[];

  @OneToMany(
    () => OpeCentro2ParamPer,
    (opeCentro2ParamPer) => opeCentro2ParamPer.opeFrenteTrabalho,
  )
  opeCentro2ParamPers: OpeCentro2ParamPer[];

  @OneToMany(
    () => OpeCentro2Pessoa,
    (opeCentro2Pessoa) => opeCentro2Pessoa.opeFrenteTrabalho,
  )
  opeCentro2Pessoas: OpeCentro2Pessoa[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerEmpresa, (gerEmpresa) => gerEmpresa.opeFrenteTrabalhos)
  @JoinColumn([{ name: 'ger_empresa_id', referencedColumnName: 'id' }])
  gerEmpresa: GerEmpresa;
}
