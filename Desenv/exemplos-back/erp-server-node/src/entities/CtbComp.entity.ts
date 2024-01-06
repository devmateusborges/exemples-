import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { GerUmedida } from './GerUmedida.entity';
import { SystemUnit } from './SystemUnit.entity';
import { CtbCompGrupo } from './CtbCompGrupo.entity';
import { CtbLancDet } from './CtbLancDet.entity';
import { GerItemserv } from './GerItemserv.entity';
import { OpeCentro1 } from './OpeCentro1.entity';
import { OpeCentro2 } from './OpeCentro2.entity';
import { OpeCentro2OrdItemserv } from './OpeCentro2OrdItemserv.entity';
import { OpeCentro2OrdRec } from './OpeCentro2OrdRec.entity';
import { OpeCentroPrevDest } from './OpeCentroPrevDest.entity';
import { OpeCentroRendFator } from './OpeCentroRendFator.entity';
import { OpeCentroSubgrupo } from './OpeCentroSubgrupo.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ctb_comp', ['id'], { unique: true })
@Entity('ctb_comp', { schema: 'public' })
export class CtbComp extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_comp', length: 50 })
  siglaComp: string;

  @Column('varchar', {
    name: 'ctb_comp_id_calc_orig',
    nullable: true,
    length: 36,
  })
  ctbCompIdCalcOrig: string;

  @Column('numeric', {
    name: 'fator_calc_origem',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  fatorCalcOrigem: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => GerUmedida, (gerUmedida) => gerUmedida.ctbComps)
  @JoinColumn([{ name: 'ger_umedida_id', referencedColumnName: 'id' }])
  gerUmedida: GerUmedida;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => CtbCompGrupo, (ctbCompGrupo) => ctbCompGrupo.ctbComps)
  @JoinColumn([{ name: 'ctb_comp_grupo_id', referencedColumnName: 'id' }])
  ctbCompGrupo: CtbCompGrupo;

  @OneToMany(() => CtbLancDet, (ctbLancDet) => ctbLancDet.ctbComp)
  ctbLancDets: CtbLancDet[];

  @OneToMany(() => GerItemserv, (gerItemserv) => gerItemserv.ctbComp)
  gerItemservs: GerItemserv[];

  @OneToMany(() => OpeCentro1, (opeCentro1) => opeCentro1.ctbComp)
  opeCentros: OpeCentro1[];

  @OneToMany(() => OpeCentro2, (opeCentro2) => opeCentro2.ctbComp)
  opeCentros2: OpeCentro2[];

  @OneToMany(
    () => OpeCentro2OrdItemserv,
    (opeCentro2OrdItemserv) => opeCentro2OrdItemserv.ctbComp,
  )
  opeCentro2OrdItemservs: OpeCentro2OrdItemserv[];

  @OneToMany(
    () => OpeCentro2OrdRec,
    (opeCentro2OrdRec) => opeCentro2OrdRec.ctbComp,
  )
  opeCentro2OrdRecs: OpeCentro2OrdRec[];

  @OneToMany(
    () => OpeCentro2OrdRec,
    (opeCentro2OrdRec) => opeCentro2OrdRec.ctbCompIdImp,
  )
  opeCentro2OrdRecs2: OpeCentro2OrdRec[];

  @OneToMany(
    () => OpeCentroPrevDest,
    (opeCentroPrevDest) => opeCentroPrevDest.ctbComp,
  )
  opeCentroPrevDests: OpeCentroPrevDest[];

  @OneToMany(
    () => OpeCentroRendFator,
    (opeCentroRendFator) => opeCentroRendFator.ctbComp,
  )
  opeCentroRendFators: OpeCentroRendFator[];

  @OneToMany(
    () => OpeCentroSubgrupo,
    (opeCentroSubgrupo) => opeCentroSubgrupo.ctbComp,
  )
  opeCentroSubgrupos: OpeCentroSubgrupo[];
}
