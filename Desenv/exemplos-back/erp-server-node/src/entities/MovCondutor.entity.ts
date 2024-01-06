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

@Index('pk_mov_condutor', ['id'], { unique: true })
@Entity('mov_condutor', { schema: 'public' })
export class MovCondutor extends BaseEntity {
  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.movCondutors)
  @JoinColumn([{ name: 'ger_pessoa_id_condutor', referencedColumnName: 'id' }])
  gerPessoaIdCondutor: GerPessoa;

  @ManyToOne(() => Mov, (mov) => mov.movCondutors)
  @JoinColumn([{ name: 'mov_id', referencedColumnName: 'id' }])
  mov: Mov;
}
