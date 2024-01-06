import { Column, Entity, Index, OneToMany } from 'typeorm';
import { OpeCentroConfig } from './OpeCentroConfig.entity';
import { OpeCentroSubtipo } from './OpeCentroSubtipo.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro_tipo', ['id'], { unique: true })
@Entity('ope_centro_tipo', { schema: 'public' })
export class OpeCentroTipo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'tipo_es', length: 1 })
  tipoEs: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => OpeCentroConfig,
    (opeCentroConfig) => opeCentroConfig.opeCentroTipo,
  )
  opeCentroConfigs: OpeCentroConfig[];

  @OneToMany(
    () => OpeCentroSubtipo,
    (opeCentroSubtipo) => opeCentroSubtipo.opeCentroTipo,
  )
  opeCentroSubtipos: OpeCentroSubtipo[];
}
