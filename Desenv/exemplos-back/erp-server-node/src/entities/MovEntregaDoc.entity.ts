import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { MovEntrega } from './MovEntrega.entity';
import { Mov } from './Mov.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_mov_entrega_doc', ['id'], { unique: true })
@Entity('mov_entrega_doc', { schema: 'public' })
export class MovEntregaDoc extends BaseEntity {
  @Column('numeric', {
    name: 'valor_total',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorTotal: string;

  @Column('varchar', {
    name: 'chave_documento',
    nullable: true,
    length: 50,
  })
  chaveDocumento: string;

  @Column('varchar', {
    name: 'modelo_documento',
    nullable: true,
    length: 2,
  })
  modeloDocumento: string;

  @Column('varchar', {
    name: 'serie_documento',
    nullable: true,
    length: 3,
  })
  serieDocumento: string;

  @Column('varchar', {
    name: 'nr_documento',
    nullable: true,
    length: 50,
  })
  nrDocumento: string;

  @Column('varchar', {
    name: 'subserie_documento',
    nullable: true,
    length: 2,
  })
  subserieDocumento: string;

  @Column('date', { name: 'data_emissao', nullable: true })
  dataEmissao: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => MovEntrega, (movEntrega) => movEntrega.movEntregaDocs)
  @JoinColumn([{ name: 'mov_entrega_id', referencedColumnName: 'id' }])
  movEntrega: MovEntrega;

  @ManyToOne(() => Mov, (mov) => mov.movEntregaDocs)
  @JoinColumn([{ name: 'mov_id', referencedColumnName: 'id' }])
  mov: Mov;

  @ManyToOne(() => Mov, (mov) => mov.movEntregaDocs2)
  @JoinColumn([{ name: 'mov_id_interno', referencedColumnName: 'id' }])
  movIdInterno: Mov;
}
