import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { CtbHistorico } from './CtbHistorico.entity';
import { CtbLote } from './CtbLote.entity';
import { CtbVersao } from './CtbVersao.entity';
import { GerEmpresa } from './GerEmpresa.entity';
import { CtbLancDet } from './CtbLancDet.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ctb_lanc', ['id'], { unique: true })
@Entity('ctb_lanc', { schema: 'public' })
export class CtbLanc extends BaseEntity {
  @Column('varchar', { name: 'numero_lanc', length: 50 })
  numeroLanc: string;

  @Column('date', { name: 'data_lanc' })
  dataLanc: string;

  @Column('varchar', { name: 'historico', length: 250 })
  historico: string;

  @Column('varchar', {
    name: 'status',
    length: 2,
    default: () => "'PD'",
  })
  status: string;

  @Column('varchar', {
    name: 'status_observacao',
    nullable: true,
    length: 250,
  })
  statusObservacao: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => CtbHistorico, (ctbHistorico) => ctbHistorico.ctbLancs)
  @JoinColumn([{ name: 'ctb_historico_id', referencedColumnName: 'id' }])
  ctbHistorico: CtbHistorico;

  @ManyToOne(() => CtbLote, (ctbLote) => ctbLote.ctbLancs)
  @JoinColumn([{ name: 'ctb_lote_id', referencedColumnName: 'id' }])
  ctbLote: CtbLote;

  @ManyToOne(() => CtbVersao, (ctbVersao) => ctbVersao.ctbLancs)
  @JoinColumn([{ name: 'ctb_versao_id', referencedColumnName: 'id' }])
  ctbVersao: CtbVersao;

  @ManyToOne(() => GerEmpresa, (gerEmpresa) => gerEmpresa.ctbLancs)
  @JoinColumn([{ name: 'ger_empresa_id', referencedColumnName: 'id' }])
  gerEmpresa: GerEmpresa;

  @OneToMany(() => CtbLancDet, (ctbLancDet) => ctbLancDet.ctbLanc)
  ctbLancDets: CtbLancDet[];
}
