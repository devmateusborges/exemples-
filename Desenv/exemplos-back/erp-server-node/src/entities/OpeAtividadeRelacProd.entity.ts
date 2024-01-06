import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { OpeAtividade } from './OpeAtividade.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_atividade_prod', ['id'], { unique: true })
@Entity('ope_atividade_relac_prod', { schema: 'public' })
export class OpeAtividadeRelacProd extends BaseEntity {
  @Column('varchar', { name: 'ordem_visual', length: 1 })
  ordemVisual: string;

  @ManyToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => OpeAtividade,
    (opeAtividade) => opeAtividade.opeAtividadeRelacProds,
  )
  @JoinColumn([{ name: 'ope_atividade_id', referencedColumnName: 'id' }])
  opeAtividade: OpeAtividade;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(
    () => OpeAtividade,
    (opeAtividade) => opeAtividade.opeAtividadeRelacProds2,
  )
  @JoinColumn([{ name: 'ope_atividade_id_prod', referencedColumnName: 'id' }])
  opeAtividadeIdProd: OpeAtividade;
}
