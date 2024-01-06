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

@Index('pk_mov_seguradora', ['id'], { unique: true })
@Entity('mov_seguradora', { schema: 'public' })
export class MovSeguradora extends BaseEntity {
  @Column('varchar', {
    name: 'nr_apolice',
    nullable: true,
    length: 50,
  })
  nrApolice: string;

  @Column('varchar', {
    name: 'nr_averbacao',
    nullable: true,
    length: 50,
  })
  nrAverbacao: string;

  @Column('numeric', { name: 'valor', nullable: true, precision: 18, scale: 6 })
  valor: string;

  @Column('integer', { name: 'tipo_responsavel', nullable: true })
  tipoResponsavel: number | null;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.movSeguradoras)
  @JoinColumn([
    { name: 'ger_pessoa_id_responsavel', referencedColumnName: 'id' },
  ])
  gerPessoaIdResponsavel: GerPessoa;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.movSeguradoras2)
  @JoinColumn([
    { name: 'ger_pessoa_id_seguradora', referencedColumnName: 'id' },
  ])
  gerPessoaIdSeguradora: GerPessoa;

  @ManyToOne(() => Mov, (mov) => mov.movSeguradoras)
  @JoinColumn([{ name: 'mov_id', referencedColumnName: 'id' }])
  mov: Mov;
}
