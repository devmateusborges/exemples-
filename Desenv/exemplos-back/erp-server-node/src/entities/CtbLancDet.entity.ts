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
import { CtbConta } from './CtbConta.entity';
import { CtbLanc } from './CtbLanc.entity';
import { OpeAtividade } from './OpeAtividade.entity';
import { OpeCentro2 } from './OpeCentro2.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ctb_lanc_det', ['id'], { unique: true })
@Entity('ctb_lanc_det', { schema: 'public' })
export class CtbLancDet extends BaseEntity {
  @Column('varchar', { name: 'tipo_dc', length: 1 })
  tipoDc: string;

  @Column('numeric', {
    name: 'valor',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor: string;

  @Column('varchar', {
    name: 'process_id',
    nullable: true,
    length: 36,
  })
  processId: string;

  @Column('varchar', { name: 'origem_tipo', length: 50 })
  origemTipo: string;

  @Column('varchar', { name: 'origem_id', length: 36 })
  origemId: string;

  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column('numeric', {
    name: 'qnt',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  qnt: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => CtbComp, (ctbComp) => ctbComp.ctbLancDets)
  @JoinColumn([{ name: 'ctb_comp_id', referencedColumnName: 'id' }])
  ctbComp: CtbComp;

  @ManyToOne(() => CtbConta, (ctbConta) => ctbConta.ctbLancDets)
  @JoinColumn([{ name: 'ctb_conta_id', referencedColumnName: 'id' }])
  ctbConta: CtbConta;

  @ManyToOne(() => CtbLanc, (ctbLanc) => ctbLanc.ctbLancDets, {
    onDelete: 'CASCADE',
  })
  @JoinColumn([{ name: 'ctb_lanc_id', referencedColumnName: 'id' }])
  ctbLanc: CtbLanc;

  @ManyToOne(() => OpeAtividade, (opeAtividade) => opeAtividade.ctbLancDets)
  @JoinColumn([{ name: 'ope_atividade_id', referencedColumnName: 'id' }])
  opeAtividade: OpeAtividade;

  @ManyToOne(() => OpeCentro2, (opeCentro2) => opeCentro2.ctbLancDets)
  @JoinColumn([{ name: 'ope_centro2_id', referencedColumnName: 'id' }])
  opeCentro2: OpeCentro2;
}
