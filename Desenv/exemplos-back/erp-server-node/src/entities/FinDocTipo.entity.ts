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
import { GerNumeracao } from './GerNumeracao.entity';
import { FinPagrec } from './FinPagrec.entity';
import { FinPagrecBaixa } from './FinPagrecBaixa.entity';
import { FinPagrecParc } from './FinPagrecParc.entity';
import { FinUnitParam } from './FinUnitParam.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_doc_tipo', ['id'], { unique: true })
@Entity('fin_doc_tipo', { schema: 'public' })
export class FinDocTipo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'nr_doc', nullable: true, length: 50 })
  nrDoc: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerNumeracao, (gerNumeracao) => gerNumeracao.finDocTipos, {
    onUpdate: 'CASCADE',
  })
  @JoinColumn([{ name: 'ger_numeracao_id', referencedColumnName: 'id' }])
  gerNumeracao: GerNumeracao;

  @OneToMany(() => FinPagrec, (finPagrec) => finPagrec.finDocTipo)
  finPagrecs: FinPagrec[];

  @OneToMany(
    () => FinPagrecBaixa,
    (finPagrecBaixa) => finPagrecBaixa.finDocTipo,
  )
  finPagrecBaixas: FinPagrecBaixa[];

  @OneToMany(() => FinPagrecParc, (finPagrecParc) => finPagrecParc.finDocTipo)
  finPagrecParcs: FinPagrecParc[];

  @OneToMany(() => FinUnitParam, (finUnitParam) => finUnitParam.finDocTipo)
  finUnitParams: FinUnitParam[];
}
