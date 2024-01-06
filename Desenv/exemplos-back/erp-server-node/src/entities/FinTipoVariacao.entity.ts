import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { FinPagrecBaixaVar } from './FinPagrecBaixaVar.entity';
import { FinPagrecParcVar } from './FinPagrecParcVar.entity';
import { FinPagrecPrevVar } from './FinPagrecPrevVar.entity';
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fin_tipo_variacao', ['id'], { unique: true })
@Entity('fin_tipo_variacao', { schema: 'public' })
export class FinTipoVariacao extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'tipo', length: 1 })
  tipo: string;

  @Column('varchar', { name: 'valor_positivo', length: 1 })
  valorPositivo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => FinPagrecBaixaVar,
    (finPagrecBaixaVar) => finPagrecBaixaVar.finTipoVariacao,
  )
  finPagrecBaixaVars: FinPagrecBaixaVar[];

  @OneToMany(
    () => FinPagrecParcVar,
    (finPagrecParcVar) => finPagrecParcVar.finTipoVariacao,
  )
  finPagrecParcVars: FinPagrecParcVar[];

  @OneToMany(
    () => FinPagrecPrevVar,
    (finPagrecPrevVar) => finPagrecPrevVar.finTipoVariacao,
  )
  finPagrecPrevVars: FinPagrecPrevVar[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
