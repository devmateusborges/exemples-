import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { OpeCentro2 } from './OpeCentro2.entity';
import { OpeCompart } from './OpeCompart.entity';
import { OpeOcor } from './OpeOcor.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_ocor_prev', ['id'], { unique: true })
@Entity('ope_ocor_prev', { schema: 'public' })
export class OpeOcorPrev extends BaseEntity {
  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column('date', { name: 'data_ult_solucao', nullable: true })
  dataUltSolucao: string;

  @Column('integer', { name: 'qnt_limite', default: () => '0' })
  qntLimite: number;

  @Column('integer', { name: 'qnt_aviso', default: () => '0' })
  qntAviso: number;

  @Column('integer', { name: 'qnt_dia_limite', default: () => '0' })
  qntDiaLimite: number;

  @Column('integer', { name: 'qnt_dia_aviso', default: () => '0' })
  qntDiaAviso: number;

  @Column('date', { name: 'data_valid_ini' })
  dataValidIni: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => OpeCentro2, (opeCentro2) => opeCentro2.opeOcorPrevs)
  @JoinColumn([{ name: 'ope_centro2_id', referencedColumnName: 'id' }])
  opeCentro2: OpeCentro2;

  @ManyToOne(() => OpeCompart, (opeCompart) => opeCompart.opeOcorPrevs)
  @JoinColumn([{ name: 'ope_compart_id', referencedColumnName: 'id' }])
  opeCompart: OpeCompart;

  @ManyToOne(() => OpeOcor, (opeOcor) => opeOcor.opeOcorPrevs)
  @JoinColumn([{ name: 'ope_ocor_id', referencedColumnName: 'id' }])
  opeOcor: OpeOcor;
}
