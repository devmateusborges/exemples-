import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { OpeCentro2Area } from './OpeCentro2Area.entity';
import { OpeCentroConfig } from './OpeCentroConfig.entity';
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_estagio', ['id'], { unique: true })
@Entity('ope_estagio', { schema: 'public' })
export class OpeEstagio extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_estagio', length: 50 })
  siglaEstagio: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => OpeCentro2Area,
    (opeCentro2Area) => opeCentro2Area.opeEstagio,
  )
  opeCentro2Areas: OpeCentro2Area[];

  @OneToMany(
    () => OpeCentroConfig,
    (opeCentroConfig) => opeCentroConfig.opeEstagio,
  )
  opeCentroConfigs: OpeCentroConfig[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
