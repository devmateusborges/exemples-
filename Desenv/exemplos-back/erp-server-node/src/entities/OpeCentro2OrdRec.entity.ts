import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { CtbComp } from './CtbComp.entity';
import { GerPessoaEndereco } from './GerPessoaEndereco.entity';
import { OpeCentro1 } from './OpeCentro1.entity';
import { OpeCentro2 } from './OpeCentro2.entity';
import { OpeCentro2OrdAtiv } from './OpeCentro2OrdAtiv.entity';
import { OpeCompart } from './OpeCompart.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro2_ord_rec', ['id'], { unique: true })
@Entity('ope_centro2_ord_rec', { schema: 'public' })
export class OpeCentro2OrdRec extends BaseEntity {
  @Column('varchar', {
    name: 'observacao_interna',
    nullable: true,
    length: 250,
  })
  observacaoInterna: string;

  @Column('varchar', {
    name: 'observacao_externa',
    nullable: true,
    length: 250,
  })
  observacaoExterna: string;

  @Column('numeric', {
    name: 'qnt_rend',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  qntRend: string;

  @Column('numeric', {
    name: 'perc_util',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  percUtil: string;

  @Column('numeric', {
    name: 'qnt_total_util',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  qntTotalUtil: string;

  @Column('numeric', {
    name: 'valor_unit_util',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorUnitUtil: string;

  @Column('numeric', {
    name: 'valor_total_util',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  valorTotalUtil: string;

  @Column('date', { name: 'data_valid', nullable: true })
  dataValid: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => CtbComp, (ctbComp) => ctbComp.opeCentro2OrdRecs)
  @JoinColumn([{ name: 'ctb_comp_id', referencedColumnName: 'id' }])
  ctbComp: CtbComp;

  @ManyToOne(() => CtbComp, (ctbComp) => ctbComp.opeCentro2OrdRecs2)
  @JoinColumn([{ name: 'ctb_comp_id_imp01', referencedColumnName: 'id' }])
  ctbCompIdImp: CtbComp;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.opeCentro2OrdRecs,
  )
  @JoinColumn([
    { name: 'ger_pessoa_endereco_id_exec', referencedColumnName: 'id' },
  ])
  gerPessoaEnderecoIdExec: GerPessoaEndereco;

  @ManyToOne(() => OpeCentro1, (opeCentro1) => opeCentro1.opeCentro2OrdRecs)
  @JoinColumn([{ name: 'ope_centro1_id', referencedColumnName: 'id' }])
  opeCentro1: OpeCentro1;

  @ManyToOne(() => OpeCentro1, (opeCentro1) => opeCentro1.opeCentro2OrdRecs2)
  @JoinColumn([{ name: 'ope_centro1_id_imp01', referencedColumnName: 'id' }])
  opeCentro1IdImp: OpeCentro1;

  @ManyToOne(() => OpeCentro2, (opeCentro2) => opeCentro2.opeCentro2OrdRecs)
  @JoinColumn([{ name: 'ope_centro2_id', referencedColumnName: 'id' }])
  opeCentro2: OpeCentro2;

  @ManyToOne(() => OpeCentro2, (opeCentro2) => opeCentro2.opeCentro2OrdRecs2)
  @JoinColumn([{ name: 'ope_centro2_id_imp01', referencedColumnName: 'id' }])
  opeCentro2IdImp: OpeCentro2;

  @ManyToOne(
    () => OpeCentro2OrdAtiv,
    (opeCentro2OrdAtiv) => opeCentro2OrdAtiv.opeCentro2OrdRecs,
  )
  @JoinColumn([{ name: 'ope_centro2_ord_ativ_id', referencedColumnName: 'id' }])
  opeCentro2OrdAtiv: OpeCentro2OrdAtiv;

  @ManyToOne(() => OpeCompart, (opeCompart) => opeCompart.opeCentro2OrdRecs)
  @JoinColumn([{ name: 'ope_compart_id', referencedColumnName: 'id' }])
  opeCompart: OpeCompart;
}
