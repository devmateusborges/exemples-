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
import { FinDocTipo } from './FinDocTipo.entity';
import { FinPagrecTipo } from './FinPagrecTipo.entity';
import { GerPessoa } from './GerPessoa.entity';
import { OpeCentroRatTipo } from './OpeCentroRatTipo.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_unit_param', ['id'], { unique: true })
@Entity('fin_unit_param', { schema: 'public' })
export class FinUnitParam extends BaseEntity {
  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'system_unit_id', referencedColumnName: 'id' }])
  systemUnit: SystemUnit;

  @ManyToOne(
    () => FinCondPagrec,
    (finCondPagrec) => finCondPagrec.finUnitParams,
  )
  @JoinColumn([{ name: 'fin_cond_pagrec_id', referencedColumnName: 'id' }])
  finCondPagrec: FinCondPagrec;

  @ManyToOne(() => FinDocTipo, (finDocTipo) => finDocTipo.finUnitParams)
  @JoinColumn([{ name: 'fin_doc_tipo_id', referencedColumnName: 'id' }])
  finDocTipo: FinDocTipo;

  @ManyToOne(
    () => FinPagrecTipo,
    (finPagrecTipo) => finPagrecTipo.finUnitParams,
  )
  @JoinColumn([{ name: 'fin_pagrec_tipo_id', referencedColumnName: 'id' }])
  finPagrecTipo: FinPagrecTipo;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.finUnitParams)
  @JoinColumn([{ name: 'ger_pessoa_id', referencedColumnName: 'id' }])
  gerPessoa: GerPessoa;

  @ManyToOne(
    () => OpeCentroRatTipo,
    (opeCentroRatTipo) => opeCentroRatTipo.finUnitParams,
  )
  @JoinColumn([{ name: 'ope_centro_rat_tipo_id', referencedColumnName: 'id' }])
  opeCentroRatTipo: OpeCentroRatTipo;
}
