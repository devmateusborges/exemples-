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
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_espac', ['id'], { unique: true })
@Entity('ope_espac', { schema: 'public' })
export class OpeEspac extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', {
    name: 'sigla_espac',
    nullable: true,
    length: 50,
  })
  siglaEspac: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => OpeCentro2Area, (opeCentro2Area) => opeCentro2Area.opeEspac)
  opeCentro2Areas: OpeCentro2Area[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
