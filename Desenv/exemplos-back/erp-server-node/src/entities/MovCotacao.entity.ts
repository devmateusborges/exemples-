import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUser } from './SystemUser.entity';
import { SystemUnit } from './SystemUnit.entity';
import { FinCondPagrec } from './FinCondPagrec.entity';
import { GerItemserv } from './GerItemserv.entity';
import { GerPessoaEndereco } from './GerPessoaEndereco.entity';
import { GerPessoa } from './GerPessoa.entity';
import { Mov } from './Mov.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_mov_cotacao', ['id'], { unique: true })
@Entity('mov_cotacao', { schema: 'public' })
export class MovCotacao extends BaseEntity {
  @Column('varchar', {
    name: 'observacao1',
    nullable: true,
    length: 250,
  })
  observacao1: string;

  @Column('varchar', {
    name: 'observacao2',
    nullable: true,
    length: 250,
  })
  observacao2: string;

  @Column('numeric', {
    name: 'qnt_cot',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  qntCot: string;

  @Column('numeric', {
    name: 'valor_unit_cot',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorUnitCot: string;

  @Column('numeric', {
    name: 'valor_total_cot',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorTotalCot: string;

  @Column('numeric', {
    name: 'valor_desc_cot',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorDescCot: string;

  @Column('numeric', {
    name: 'valor_frete_cot',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorFreteCot: string;

  @Column('numeric', { name: 'valor_outro_cot', precision: 18, scale: 6 })
  valorOutroCot: string;

  @Column('numeric', {
    name: 'valor_total_trib_cot',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorTotalTribCot: string;

  @Column('varchar', {
    name: 'status',
    length: 1,
    default: () => "'P'",
  })
  status: string;

  @Column('timestamp without time zone', {
    name: 'data_status',
    nullable: true,
  })
  dataStatus: Date | null;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUser)
  @JoinColumn([{ name: 'system_user_id_aprov', referencedColumnName: 'id' }])
  systemUserIdAprov: SystemUser;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => FinCondPagrec, (finCondPagrec) => finCondPagrec.movCotacaos)
  @JoinColumn([{ name: 'fin_cond_pagrec_id', referencedColumnName: 'id' }])
  finCondPagrec: FinCondPagrec;

  @ManyToOne(() => GerItemserv, (gerItemserv) => gerItemserv.movCotacaos)
  @JoinColumn([{ name: 'ger_itemserv_id', referencedColumnName: 'id' }])
  gerItemserv: GerItemserv;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.movCotacaos,
  )
  @JoinColumn([{ name: 'ger_pessoa_endereco_id', referencedColumnName: 'id' }])
  gerPessoaEndereco: GerPessoaEndereco;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.movCotacaos)
  @JoinColumn([{ name: 'ger_pessoa_id', referencedColumnName: 'id' }])
  gerPessoa: GerPessoa;

  @ManyToOne(() => Mov, (mov) => mov.movCotacaos)
  @JoinColumn([{ name: 'mov_id', referencedColumnName: 'id' }])
  mov: Mov;
}
