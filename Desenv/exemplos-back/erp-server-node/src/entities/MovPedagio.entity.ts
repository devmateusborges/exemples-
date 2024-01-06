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

@Index('pk_mov_pedagio', ['id'], { unique: true })
@Entity('mov_pedagio', { schema: 'public' })
export class MovPedagio extends BaseEntity {
  @Column('numeric', { name: 'valor_pedagio', precision: 18, scale: 6 })
  valorPedagio: string;

  @Column('varchar', {
    name: 'nr_comprovante',
    nullable: true,
    length: 50,
  })
  nrComprovante: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.movPedagios)
  @JoinColumn([
    { name: 'ger_pessoa_id_emp_pedagio', referencedColumnName: 'id' },
  ])
  gerPessoaIdEmpPedagio: GerPessoa;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.movPedagios2)
  @JoinColumn([
    { name: 'ger_pessoa_id_responsavel', referencedColumnName: 'id' },
  ])
  gerPessoaIdResponsavel: GerPessoa;

  @ManyToOne(() => Mov, (mov) => mov.movPedagios)
  @JoinColumn([{ name: 'mov_id', referencedColumnName: 'id' }])
  mov: Mov;
}
