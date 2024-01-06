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
import { CtbCentroGrupo } from './CtbCentroGrupo.entity';
import { OpeCentroRatFator } from './OpeCentroRatFator.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ctb_centro', ['id'], { unique: true })
@Entity('ctb_centro', { schema: 'public' })
export class CtbCentro extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_centro', length: 50 })
  siglaCentro: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => CtbCentroGrupo,
    (ctbCentroGrupo) => ctbCentroGrupo.ctbCentros,
  )
  @JoinColumn([{ name: 'ctb_centro_grupo_id', referencedColumnName: 'id' }])
  ctbCentroGrupo: CtbCentroGrupo;

  @OneToMany(
    () => OpeCentroRatFator,
    (opeCentroRatFator) => opeCentroRatFator.ctbCentro,
  )
  opeCentroRatFators: OpeCentroRatFator[];
}
