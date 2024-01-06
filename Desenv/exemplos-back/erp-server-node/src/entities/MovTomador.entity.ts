import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { GerPessoa } from './GerPessoa.entity';
import { Mov } from './Mov.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_mov_tomador', ['id'], { unique: true })
@Entity('mov_tomador', { schema: 'public' })
export class MovTomador extends BaseEntity {
  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.movTomadors)
  @JoinColumn([
    { name: 'ger_pessoa_id_responsavel', referencedColumnName: 'id' },
  ])
  gerPessoaIdResponsavel: GerPessoa;

  @ManyToOne(() => Mov, (mov) => mov.movTomadors)
  @JoinColumn([{ name: 'mov_id', referencedColumnName: 'id' }])
  mov: Mov;
}
