import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { FinDocTipo } from './FinDocTipo.entity';
import { SystemUnit } from './SystemUnit.entity';
import { MovOperacao } from './MovOperacao.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_numeracao', ['id'], { unique: true })
@Entity('ger_numeracao', { schema: 'public' })
export class GerNumeracao extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'serie', length: 3 })
  serie: string;

  @Column('integer', { name: 'ultimo_nr' })
  ultimoNr: number;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => FinDocTipo, (finDocTipo) => finDocTipo.gerNumeracao)
  finDocTipos: FinDocTipo[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(() => MovOperacao, (movOperacao) => movOperacao.gerNumeracao)
  movOperacaos: MovOperacao[];
}
