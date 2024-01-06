import { Column, Entity, Index, OneToMany } from 'typeorm';
import { CtbComp } from './CtbComp.entity';
import { GerItemserv } from './GerItemserv.entity';
import { GerUmedidaConv } from './GerUmedidaConv.entity';
import { Ind } from './Ind.entity';
import { MovItemserv } from './MovItemserv.entity';
import { MovMedida } from './MovMedida.entity';
import { OpeAtividade } from './OpeAtividade.entity';
import { OpeCentro2 } from './OpeCentro2.entity';
import { OpeCentro2Area } from './OpeCentro2Area.entity';
import { OpeCentro2OrdDest } from './OpeCentro2OrdDest.entity';
import { OpeOcor } from './OpeOcor.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_umedida', ['id'], { unique: true })
@Entity('ger_umedida', { schema: 'public' })
export class GerUmedida extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_umedida', length: 50 })
  siglaUmedida: string;

  @Column('varchar', {
    name: 'nr_umedida',
    nullable: true,
    length: 50,
  })
  nrUmedida: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => CtbComp, (ctbComp) => ctbComp.gerUmedida)
  ctbComps: CtbComp[];

  @OneToMany(() => GerItemserv, (gerItemserv) => gerItemserv.gerUmedida)
  gerItemservs: GerItemserv[];

  @OneToMany(
    () => GerUmedidaConv,
    (gerUmedidaConv) => gerUmedidaConv.gerUmedidaIdDe,
  )
  gerUmedidaConvs: GerUmedidaConv[];

  @OneToMany(
    () => GerUmedidaConv,
    (gerUmedidaConv) => gerUmedidaConv.gerUmedidaIdPara,
  )
  gerUmedidaConvs2: GerUmedidaConv[];

  @OneToMany(() => Ind, (ind) => ind.gerUmedida)
  inds: Ind[];

  @OneToMany(() => MovItemserv, (movItemserv) => movItemserv.gerUmedidaIdConv)
  movItemservs: MovItemserv[];

  @OneToMany(() => MovMedida, (movMedida) => movMedida.gerUmedida)
  movMedidas: MovMedida[];

  @OneToMany(() => OpeAtividade, (opeAtividade) => opeAtividade.gerUmedida)
  opeAtividades: OpeAtividade[];

  @OneToMany(() => OpeCentro2, (opeCentro2) => opeCentro2.gerUmedida)
  opeCentros: OpeCentro2[];

  @OneToMany(
    () => OpeCentro2Area,
    (opeCentro2Area) => opeCentro2Area.gerUmedida,
  )
  opeCentro2Areas: OpeCentro2Area[];

  @OneToMany(
    () => OpeCentro2OrdDest,
    (opeCentro2OrdDest) => opeCentro2OrdDest.gerUmedidaIdDest,
  )
  opeCentro2OrdDests: OpeCentro2OrdDest[];

  @OneToMany(() => OpeOcor, (opeOcor) => opeOcor.gerUmedida)
  opeOcors: OpeOcor[];
}
