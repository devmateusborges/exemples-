import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { OpeCentro2Equip } from './OpeCentro2Equip.entity';
import { OpeCentro2Pessoa } from './OpeCentro2Pessoa.entity';
import { BaseEntity } from '../shared/bases/base.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';

@Index('pk_bor_dispositivo', ['id'], { unique: true })
@Index('idx_bor_dispositivo_01', ['numeroSerie'], { unique: true })
@Entity('bor_dispositivo', { schema: 'public' })
export class BorDispositivo extends BaseEntity {
  @Column('varchar', { name: 'nome', nullable: true, length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', nullable: true, length: 1 })
  ativo: string;

  @Column('varchar', { name: 'numero_serie', length: 50 })
  numeroSerie: string;

  @Column('varchar', { name: 'tipo', nullable: true, length: 1 })
  tipo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => OpeCentro2Equip,
    (opeCentro2Equip) => opeCentro2Equip.borDispositivos,
  )
  @JoinColumn([{ name: 'ope_centro2_equip_id', referencedColumnName: 'id' }])
  opeCentro2Equip: OpeCentro2Equip;

  @ManyToOne(
    () => OpeCentro2Pessoa,
    (opeCentro2Pessoa) => opeCentro2Pessoa.borDispositivos,
  )
  @JoinColumn([{ name: 'ope_centro2_pessoa_id', referencedColumnName: 'id' }])
  opeCentro2Pessoa: OpeCentro2Pessoa;
}
