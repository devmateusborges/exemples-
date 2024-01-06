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
import { GerPessoaEndereco } from './GerPessoaEndereco.entity';
import { GerPessoa } from './GerPessoa.entity';
import { GerItemserv } from './GerItemserv.entity';
import { Mov } from './Mov.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_mov_cotacao_anal', ['id'], { unique: true })
@Entity('mov_cotacao_anal', { schema: 'public' })
export class MovCotacaoAnal extends BaseEntity {
  @Column('varchar', {
    name: 'c01_observacao1',
    nullable: true,
    length: 250,
  })
  c01Observacao1: string;

  @Column('varchar', {
    name: 'c01_observacao2',
    nullable: true,
    length: 250,
  })
  c01Observacao2: string;

  @Column('numeric', {
    name: 'c01_qnt_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c01QntCot: string;

  @Column('numeric', {
    name: 'c01_valor_unit_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c01ValorUnitCot: string;

  @Column('numeric', {
    name: 'c01_valor_total_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c01ValorTotalCot: string;

  @Column('numeric', {
    name: 'c01_valor_desc_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c01ValorDescCot: string;

  @Column('numeric', {
    name: 'c01_valor_frete_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c01ValorFreteCot: string;

  @Column('numeric', {
    name: 'c01_valor_outro_cot',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  c01ValorOutroCot: string;

  @Column('numeric', {
    name: 'c01_valor_total_trib_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c01ValorTotalTribCot: string;

  @Column('varchar', {
    name: 'c01_status',
    nullable: true,
    length: 1,
    default: () => "'P'",
  })
  c01Status: string;

  @Column('timestamp without time zone', {
    name: 'c01_data_status',
    nullable: true,
  })
  c01DataStatus: Date | null;

  @Column('varchar', {
    name: 'c02_observacao1',
    nullable: true,
    length: 250,
  })
  c02Observacao1: string;

  @Column('varchar', {
    name: 'c02_observacao2',
    nullable: true,
    length: 250,
  })
  c02Observacao2: string;

  @Column('numeric', {
    name: 'c02_qnt_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c02QntCot: string;

  @Column('numeric', {
    name: 'c02_valor_unit_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c02ValorUnitCot: string;

  @Column('numeric', {
    name: 'c02_valor_total_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c02ValorTotalCot: string;

  @Column('numeric', {
    name: 'c02_valor_desc_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c02ValorDescCot: string;

  @Column('numeric', {
    name: 'c02_valor_frete_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c02ValorFreteCot: string;

  @Column('numeric', {
    name: 'c02_valor_outro_cot',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  c02ValorOutroCot: string;

  @Column('numeric', {
    name: 'c02_valor_total_trib_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c02ValorTotalTribCot: string;

  @Column('varchar', {
    name: 'c02_status',
    nullable: true,
    length: 1,
    default: () => "'P'",
  })
  c02Status: string;

  @Column('timestamp without time zone', {
    name: 'c02_data_status',
    nullable: true,
  })
  c02DataStatus: Date | null;

  @Column('varchar', {
    name: 'c03_observacao1',
    nullable: true,
    length: 250,
  })
  c03Observacao1: string;

  @Column('varchar', {
    name: 'c03_observacao2',
    nullable: true,
    length: 250,
  })
  c03Observacao2: string;

  @Column('numeric', {
    name: 'c03_qnt_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c03QntCot: string;

  @Column('numeric', {
    name: 'c03_valor_unit_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c03ValorUnitCot: string;

  @Column('numeric', {
    name: 'c03_valor_total_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c03ValorTotalCot: string;

  @Column('numeric', {
    name: 'c03_valor_desc_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c03ValorDescCot: string;

  @Column('numeric', {
    name: 'c03_valor_frete_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c03ValorFreteCot: string;

  @Column('numeric', {
    name: 'c03_valor_outro_cot',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  c03ValorOutroCot: string;

  @Column('numeric', {
    name: 'c03_valor_total_trib_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c03ValorTotalTribCot: string;

  @Column('varchar', {
    name: 'c03_status',
    nullable: true,
    length: 1,
    default: () => "'P'",
  })
  c03Status: string;

  @Column('timestamp without time zone', {
    name: 'c03_data_status',
    nullable: true,
  })
  c03DataStatus: Date | null;

  @Column('varchar', {
    name: 'c04_observacao1',
    nullable: true,
    length: 250,
  })
  c04Observacao1: string;

  @Column('varchar', {
    name: 'c04_observacao2',
    nullable: true,
    length: 250,
  })
  c04Observacao2: string;

  @Column('numeric', {
    name: 'c04_qnt_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c04QntCot: string;

  @Column('numeric', {
    name: 'c04_valor_unit_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c04ValorUnitCot: string;

  @Column('numeric', {
    name: 'c04_valor_total_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c04ValorTotalCot: string;

  @Column('numeric', {
    name: 'c04_valor_desc_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c04ValorDescCot: string;

  @Column('numeric', {
    name: 'c04_valor_frete_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c04ValorFreteCot: string;

  @Column('numeric', {
    name: 'c04_valor_outro_cot',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  c04ValorOutroCot: string;

  @Column('numeric', {
    name: 'c04_valor_total_trib_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c04ValorTotalTribCot: string;

  @Column('varchar', {
    name: 'c04_status',
    nullable: true,
    length: 1,
    default: () => "'P'",
  })
  c04Status: string;

  @Column('timestamp without time zone', {
    name: 'c04_data_status',
    nullable: true,
  })
  c04DataStatus: Date | null;

  @Column('varchar', {
    name: 'c05_observacao1',
    nullable: true,
    length: 250,
  })
  c05Observacao1: string;

  @Column('varchar', {
    name: 'c05_observacao2',
    nullable: true,
    length: 250,
  })
  c05Observacao2: string;

  @Column('numeric', {
    name: 'c05_qnt_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c05QntCot: string;

  @Column('numeric', {
    name: 'c05_valor_unit_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c05ValorUnitCot: string;

  @Column('numeric', {
    name: 'c05_valor_total_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c05ValorTotalCot: string;

  @Column('numeric', {
    name: 'c05_valor_desc_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c05ValorDescCot: string;

  @Column('numeric', {
    name: 'c05_valor_frete_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c05ValorFreteCot: string;

  @Column('numeric', {
    name: 'c05_valor_outro_cot',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  c05ValorOutroCot: string;

  @Column('numeric', {
    name: 'c05_valor_total_trib_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c05ValorTotalTribCot: string;

  @Column('varchar', {
    name: 'c05_status',
    nullable: true,
    length: 1,
    default: () => "'P'",
  })
  c05Status: string;

  @Column('timestamp without time zone', {
    name: 'c05_data_status',
    nullable: true,
  })
  c05DataStatus: Date | null;

  @Column('varchar', {
    name: 'c06_observacao1',
    nullable: true,
    length: 250,
  })
  c06Observacao1: string;

  @Column('varchar', {
    name: 'c06_observacao2',
    nullable: true,
    length: 250,
  })
  c06Observacao2: string;

  @Column('numeric', {
    name: 'c06_qnt_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c06QntCot: string;

  @Column('numeric', {
    name: 'c06_valor_unit_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c06ValorUnitCot: string;

  @Column('numeric', {
    name: 'c06_valor_total_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c06ValorTotalCot: string;

  @Column('numeric', {
    name: 'c06_valor_desc_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c06ValorDescCot: string;

  @Column('numeric', {
    name: 'c06_valor_frete_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c06ValorFreteCot: string;

  @Column('numeric', {
    name: 'c06_valor_outro_cot',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  c06ValorOutroCot: string;

  @Column('numeric', {
    name: 'c06_valor_total_trib_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c06ValorTotalTribCot: string;

  @Column('varchar', {
    name: 'c06_status',
    nullable: true,
    length: 1,
    default: () => "'P'",
  })
  c06Status: string;

  @Column('timestamp without time zone', {
    name: 'c06_data_status',
    nullable: true,
  })
  c06DataStatus: Date | null;

  @Column('varchar', {
    name: 'c07_observacao1',
    nullable: true,
    length: 250,
  })
  c07Observacao1: string;

  @Column('varchar', {
    name: 'c07_observacao2',
    nullable: true,
    length: 250,
  })
  c07Observacao2: string;

  @Column('numeric', {
    name: 'c07_qnt_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c07QntCot: string;

  @Column('numeric', {
    name: 'c07_valor_unit_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c07ValorUnitCot: string;

  @Column('numeric', {
    name: 'c07_valor_total_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c07ValorTotalCot: string;

  @Column('numeric', {
    name: 'c07_valor_desc_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c07ValorDescCot: string;

  @Column('numeric', {
    name: 'c07_valor_frete_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c07ValorFreteCot: string;

  @Column('numeric', {
    name: 'c07_valor_outro_cot',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  c07ValorOutroCot: string;

  @Column('numeric', {
    name: 'c07_valor_total_trib_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c07ValorTotalTribCot: string;

  @Column('varchar', {
    name: 'c07_status',
    nullable: true,
    length: 1,
    default: () => "'P'",
  })
  c07Status: string;

  @Column('timestamp without time zone', {
    name: 'c07_data_status',
    nullable: true,
  })
  c07DataStatus: Date | null;

  @Column('varchar', {
    name: 'c08_observacao1',
    nullable: true,
    length: 250,
  })
  c08Observacao1: string;

  @Column('varchar', {
    name: 'c08_observacao2',
    nullable: true,
    length: 250,
  })
  c08Observacao2: string;

  @Column('numeric', {
    name: 'c08_qnt_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c08QntCot: string;

  @Column('numeric', {
    name: 'c08_valor_unit_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c08ValorUnitCot: string;

  @Column('numeric', {
    name: 'c08_valor_total_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c08ValorTotalCot: string;

  @Column('numeric', {
    name: 'c08_valor_desc_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c08ValorDescCot: string;

  @Column('numeric', {
    name: 'c08_valor_frete_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c08ValorFreteCot: string;

  @Column('numeric', {
    name: 'c08_valor_outro_cot',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  c08ValorOutroCot: string;

  @Column('numeric', {
    name: 'c08_valor_total_trib_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c08ValorTotalTribCot: string;

  @Column('varchar', {
    name: 'c08_status',
    nullable: true,
    length: 1,
    default: () => "'P'",
  })
  c08Status: string;

  @Column('timestamp without time zone', {
    name: 'c08_data_status',
    nullable: true,
  })
  c08DataStatus: Date | null;

  @Column('varchar', {
    name: 'c09_observacao1',
    nullable: true,
    length: 250,
  })
  c09Observacao1: string;

  @Column('varchar', {
    name: 'c09_observacao2',
    nullable: true,
    length: 250,
  })
  c09Observacao2: string;

  @Column('numeric', {
    name: 'c09_qnt_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c09QntCot: string;

  @Column('numeric', {
    name: 'c09_valor_unit_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c09ValorUnitCot: string;

  @Column('numeric', {
    name: 'c09_valor_total_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c09ValorTotalCot: string;

  @Column('numeric', {
    name: 'c09_valor_desc_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c09ValorDescCot: string;

  @Column('numeric', {
    name: 'c09_valor_frete_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c09ValorFreteCot: string;

  @Column('numeric', {
    name: 'c09_valor_outro_cot',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  c09ValorOutroCot: string;

  @Column('numeric', {
    name: 'c09_valor_total_trib_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c09ValorTotalTribCot: string;

  @Column('varchar', {
    name: 'c09_status',
    nullable: true,
    length: 1,
    default: () => "'P'",
  })
  c09Status: string;

  @Column('timestamp without time zone', {
    name: 'c09_data_status',
    nullable: true,
  })
  c09DataStatus: Date | null;

  @Column('varchar', {
    name: 'c10_observacao1',
    nullable: true,
    length: 250,
  })
  c10Observacao1: string;

  @Column('varchar', {
    name: 'c10_observacao2',
    nullable: true,
    length: 250,
  })
  c10Observacao2: string;

  @Column('numeric', {
    name: 'c10_qnt_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c10QntCot: string;

  @Column('numeric', {
    name: 'c10_valor_unit_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c10ValorUnitCot: string;

  @Column('numeric', {
    name: 'c10_valor_total_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c10ValorTotalCot: string;

  @Column('numeric', {
    name: 'c10_valor_desc_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c10ValorDescCot: string;

  @Column('numeric', {
    name: 'c10_valor_frete_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c10ValorFreteCot: string;

  @Column('numeric', {
    name: 'c10_valor_outro_cot',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  c10ValorOutroCot: string;

  @Column('numeric', {
    name: 'c10_valor_total_trib_cot',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  c10ValorTotalTribCot: string;

  @Column('varchar', {
    name: 'c10_status',
    nullable: true,
    length: 1,
    default: () => "'P'",
  })
  c10Status: string;

  @Column('timestamp without time zone', {
    name: 'c10_data_status',
    nullable: true,
  })
  c10DataStatus: Date | null;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUser)
  @JoinColumn([
    { name: 'c01_system_user_id_aprov', referencedColumnName: 'id' },
  ])
  c01SystemUserIdAprov: SystemUser;

  @OneToOne(() => SystemUser)
  @JoinColumn([
    { name: 'c02_system_user_id_aprov', referencedColumnName: 'id' },
  ])
  c02SystemUserIdAprov: SystemUser;

  @OneToOne(() => SystemUser)
  @JoinColumn([
    { name: 'c03_system_user_id_aprov', referencedColumnName: 'id' },
  ])
  c03SystemUserIdAprov: SystemUser;

  @OneToOne(() => SystemUser)
  @JoinColumn([
    { name: 'c04_system_user_id_aprov', referencedColumnName: 'id' },
  ])
  c04SystemUserIdAprov: SystemUser;

  @OneToOne(() => SystemUser)
  @JoinColumn([
    { name: 'c05_system_user_id_aprov', referencedColumnName: 'id' },
  ])
  c05SystemUserIdAprov: SystemUser;

  @OneToOne(() => SystemUser)
  @JoinColumn([
    { name: 'c06_system_user_id_aprov', referencedColumnName: 'id' },
  ])
  c06SystemUserIdAprov: SystemUser;

  @OneToOne(() => SystemUser)
  @JoinColumn([
    { name: 'c07_system_user_id_aprov', referencedColumnName: 'id' },
  ])
  c07SystemUserIdAprov: SystemUser;

  @OneToOne(() => SystemUser)
  @JoinColumn([
    { name: 'c08_system_user_id_aprov', referencedColumnName: 'id' },
  ])
  c08SystemUserIdAprov: SystemUser;

  @OneToOne(() => SystemUser)
  @JoinColumn([
    { name: 'c09_system_user_id_aprov', referencedColumnName: 'id' },
  ])
  c09SystemUserIdAprov: SystemUser;

  @OneToOne(() => SystemUser)
  @JoinColumn([
    { name: 'c10_system_user_id_aprov', referencedColumnName: 'id' },
  ])
  c10SystemUserIdAprov: SystemUser;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => FinCondPagrec,
    (finCondPagrec) => finCondPagrec.movCotacaoAnals,
  )
  @JoinColumn([{ name: 'c01_fin_cond_pagrec_id', referencedColumnName: 'id' }])
  c01FinCondPagrec: FinCondPagrec;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.movCotacaoAnals,
  )
  @JoinColumn([
    { name: 'c01_ger_pessoa_endereco_id', referencedColumnName: 'id' },
  ])
  c01GerPessoaEndereco: GerPessoaEndereco;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.movCotacaoAnals)
  @JoinColumn([{ name: 'c01_ger_pessoa_id', referencedColumnName: 'id' }])
  c01GerPessoa: GerPessoa;

  @ManyToOne(
    () => FinCondPagrec,
    (finCondPagrec) => finCondPagrec.movCotacaoAnals2,
  )
  @JoinColumn([{ name: 'c02_fin_cond_pagrec_id', referencedColumnName: 'id' }])
  c02FinCondPagrec: FinCondPagrec;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.movCotacaoAnals2,
  )
  @JoinColumn([
    { name: 'c02_ger_pessoa_endereco_id', referencedColumnName: 'id' },
  ])
  c02GerPessoaEndereco: GerPessoaEndereco;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.movCotacaoAnals2)
  @JoinColumn([{ name: 'c02_ger_pessoa_id', referencedColumnName: 'id' }])
  c02GerPessoa: GerPessoa;

  @ManyToOne(
    () => FinCondPagrec,
    (finCondPagrec) => finCondPagrec.movCotacaoAnals3,
  )
  @JoinColumn([{ name: 'c03_fin_cond_pagrec_id', referencedColumnName: 'id' }])
  c03FinCondPagrec: FinCondPagrec;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.movCotacaoAnals3,
  )
  @JoinColumn([
    { name: 'c03_ger_pessoa_endereco_id', referencedColumnName: 'id' },
  ])
  c03GerPessoaEndereco: GerPessoaEndereco;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.movCotacaoAnals3)
  @JoinColumn([{ name: 'c03_ger_pessoa_id', referencedColumnName: 'id' }])
  c03GerPessoa: GerPessoa;

  @ManyToOne(
    () => FinCondPagrec,
    (finCondPagrec) => finCondPagrec.movCotacaoAnals4,
  )
  @JoinColumn([{ name: 'c04_fin_cond_pagrec_id', referencedColumnName: 'id' }])
  c04FinCondPagrec: FinCondPagrec;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.movCotacaoAnals4,
  )
  @JoinColumn([
    { name: 'c04_ger_pessoa_endereco_id', referencedColumnName: 'id' },
  ])
  c04GerPessoaEndereco: GerPessoaEndereco;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.movCotacaoAnals4)
  @JoinColumn([{ name: 'c04_ger_pessoa_id', referencedColumnName: 'id' }])
  c04GerPessoa: GerPessoa;

  @ManyToOne(
    () => FinCondPagrec,
    (finCondPagrec) => finCondPagrec.movCotacaoAnals5,
  )
  @JoinColumn([{ name: 'c05_fin_cond_pagrec_id', referencedColumnName: 'id' }])
  c05FinCondPagrec: FinCondPagrec;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.movCotacaoAnals5,
  )
  @JoinColumn([
    { name: 'c05_ger_pessoa_endereco_id', referencedColumnName: 'id' },
  ])
  c05GerPessoaEndereco: GerPessoaEndereco;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.movCotacaoAnals5)
  @JoinColumn([{ name: 'c05_ger_pessoa_id', referencedColumnName: 'id' }])
  c05GerPessoa: GerPessoa;

  @ManyToOne(
    () => FinCondPagrec,
    (finCondPagrec) => finCondPagrec.movCotacaoAnals6,
  )
  @JoinColumn([{ name: 'c06_fin_cond_pagrec_id', referencedColumnName: 'id' }])
  c06FinCondPagrec: FinCondPagrec;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.movCotacaoAnals6,
  )
  @JoinColumn([
    { name: 'c06_ger_pessoa_endereco_id', referencedColumnName: 'id' },
  ])
  c06GerPessoaEndereco: GerPessoaEndereco;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.movCotacaoAnals6)
  @JoinColumn([{ name: 'c06_ger_pessoa_id', referencedColumnName: 'id' }])
  c06GerPessoa: GerPessoa;

  @ManyToOne(
    () => FinCondPagrec,
    (finCondPagrec) => finCondPagrec.movCotacaoAnals7,
  )
  @JoinColumn([{ name: 'c07_fin_cond_pagrec_id', referencedColumnName: 'id' }])
  c07FinCondPagrec: FinCondPagrec;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.movCotacaoAnals7,
  )
  @JoinColumn([
    { name: 'c07_ger_pessoa_endereco_id', referencedColumnName: 'id' },
  ])
  c07GerPessoaEndereco: GerPessoaEndereco;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.movCotacaoAnals7)
  @JoinColumn([{ name: 'c07_ger_pessoa_id', referencedColumnName: 'id' }])
  c07GerPessoa: GerPessoa;

  @ManyToOne(
    () => FinCondPagrec,
    (finCondPagrec) => finCondPagrec.movCotacaoAnals8,
  )
  @JoinColumn([{ name: 'c08_fin_cond_pagrec_id', referencedColumnName: 'id' }])
  c08FinCondPagrec: FinCondPagrec;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.movCotacaoAnals8,
  )
  @JoinColumn([
    { name: 'c08_ger_pessoa_endereco_id', referencedColumnName: 'id' },
  ])
  c08GerPessoaEndereco: GerPessoaEndereco;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.movCotacaoAnals8)
  @JoinColumn([{ name: 'c08_ger_pessoa_id', referencedColumnName: 'id' }])
  c08GerPessoa: GerPessoa;

  @ManyToOne(
    () => FinCondPagrec,
    (finCondPagrec) => finCondPagrec.movCotacaoAnals9,
  )
  @JoinColumn([{ name: 'c09_fin_cond_pagrec_id', referencedColumnName: 'id' }])
  c09FinCondPagrec: FinCondPagrec;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.movCotacaoAnals9,
  )
  @JoinColumn([
    { name: 'c09_ger_pessoa_endereco_id', referencedColumnName: 'id' },
  ])
  c09GerPessoaEndereco: GerPessoaEndereco;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.movCotacaoAnals9)
  @JoinColumn([{ name: 'c09_ger_pessoa_id', referencedColumnName: 'id' }])
  c09GerPessoa: GerPessoa;

  @ManyToOne(
    () => FinCondPagrec,
    (finCondPagrec) => finCondPagrec.movCotacaoAnas,
  )
  @JoinColumn([{ name: 'c10_fin_cond_pagrec_id', referencedColumnName: 'id' }])
  c10FinCondPagrec: FinCondPagrec;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.movCotacaoAnas,
  )
  @JoinColumn([
    { name: 'c10_ger_pessoa_endereco_id', referencedColumnName: 'id' },
  ])
  c10GerPessoaEndereco: GerPessoaEndereco;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.movCotacaoAnas)
  @JoinColumn([{ name: 'c10_ger_pessoa_id', referencedColumnName: 'id' }])
  c10GerPessoa: GerPessoa;

  @ManyToOne(() => GerItemserv, (gerItemserv) => gerItemserv.movCotacaoAnals)
  @JoinColumn([{ name: 'ger_itemserv_id', referencedColumnName: 'id' }])
  gerItemserv: GerItemserv;

  @ManyToOne(() => Mov, (mov) => mov.movCotacaoAnals)
  @JoinColumn([{ name: 'mov_id', referencedColumnName: 'id' }])
  mov: Mov;
}
