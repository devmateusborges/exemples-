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
import { GerEmpresa } from './GerEmpresa.entity';
import { GerProcessoBloqUser } from './GerProcessoBloqUser.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_processo_bloq', ['id'], { unique: true })
@Entity('ger_processo_bloq', { schema: 'public' })
export class GerProcessoBloq extends BaseEntity {
  @Column('varchar', { name: 'tipo_processo', length: 50 })
  tipoProcesso: string;

  @Column('date', { name: 'data_lib_inicial', nullable: true })
  dataLibInicial: string;

  @Column('date', { name: 'data_lib_final', nullable: true })
  dataLibFinal: string;

  @Column('varchar', { name: 'observacao', length: 250 })
  observacao: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerEmpresa, (gerEmpresa) => gerEmpresa.gerProcessoBloqs)
  @JoinColumn([{ name: 'ger_empresa_id', referencedColumnName: 'id' }])
  gerEmpresa: GerEmpresa;

  @OneToMany(
    () => GerProcessoBloqUser,
    (gerProcessoBloqUser) => gerProcessoBloqUser.gerProcessoBloq,
  )
  gerProcessoBloqUsers: GerProcessoBloqUser[];
}
