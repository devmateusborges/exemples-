import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { PtoMarcacao } from './PtoMarcacao.entity';
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_pto_medidor', ['id'], { unique: true })
@Entity('pto_medidor', { schema: 'public' })
export class PtoMedidor extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', {
    name: 'sigla_medidor',
    nullable: true,
    length: 50,
  })
  siglaMedidor: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => PtoMarcacao, (ptoMarcacao) => ptoMarcacao.ptoMedidor)
  ptoMarcacaos: PtoMarcacao[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
