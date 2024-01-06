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
import { OpeAtividade } from './OpeAtividade.entity';
import { OpeCentroVersao } from './OpeCentroVersao.entity';
import { OpeCentroRendFator } from './OpeCentroRendFator.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro_rend', ['id'], { unique: true })
@Entity('ope_centro_rend', { schema: 'public' })
export class OpeCentroRend extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => OpeAtividade, (opeAtividade) => opeAtividade.opeCentroRends)
  @JoinColumn([{ name: 'ope_atividade_id', referencedColumnName: 'id' }])
  opeAtividade: OpeAtividade;

  @ManyToOne(
    () => OpeCentroVersao,
    (opeCentroVersao) => opeCentroVersao.opeCentroRends,
  )
  @JoinColumn([{ name: 'ope_centro_versao_id', referencedColumnName: 'id' }])
  opeCentroVersao: OpeCentroVersao;

  @OneToMany(
    () => OpeCentroRendFator,
    (opeCentroRendFator) => opeCentroRendFator.opeCentroRend,
  )
  opeCentroRendFators: OpeCentroRendFator[];
}
