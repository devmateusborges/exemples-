import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ctb_tipo_saldo', ['id'], { unique: true })
@Entity('ctb_tipo_saldo', { schema: 'public' })
export class CtbTipoSaldo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_tipo_saldo', length: 50 })
  siglaTipoSaldo: string;

  @Column('smallint', { name: 'mes_ini_fechamento', default: () => '0' })
  mesIniFechamento: number;

  @Column('smallint', { name: 'mes_fin_fechamento', default: () => '12' })
  mesFinFechamento: number;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
