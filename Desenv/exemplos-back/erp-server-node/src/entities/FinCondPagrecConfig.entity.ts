import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { FinCondPagrec } from './FinCondPagrec.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_cond_pagrec_config', ['id'], { unique: true })
@Entity('fin_cond_pagrec_config', { schema: 'public' })
export class FinCondPagrecConfig extends BaseEntity {
  @Column('integer', { name: 'qnt_dia' })
  qntDia: number;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => FinCondPagrec,
    (finCondPagrec) => finCondPagrec.finCondPagrecConfigs,
  )
  @JoinColumn([{ name: 'fin_cond_pag_rec_id', referencedColumnName: 'id' }])
  finCondPagRec: FinCondPagrec;
}
