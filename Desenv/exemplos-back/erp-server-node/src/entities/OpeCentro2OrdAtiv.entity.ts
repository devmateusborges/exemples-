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
import { OpeCentro2Ord } from './OpeCentro2Ord.entity';
import { OpeFrenteTrabalho } from './OpeFrenteTrabalho.entity';
import { OpeCentro2OrdItemserv } from './OpeCentro2OrdItemserv.entity';
import { OpeCentro2OrdRec } from './OpeCentro2OrdRec.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro2_ord_ativ', ['id'], { unique: true })
@Entity('ope_centro2_ord_ativ', { schema: 'public' })
export class OpeCentro2OrdAtiv extends BaseEntity {
  @Column('varchar', {
    name: 'observacao_interna',
    nullable: true,
    length: 250,
  })
  observacaoInterna: string;

  @Column('varchar', {
    name: 'observacao_externa',
    nullable: true,
    length: 250,
  })
  observacaoExterna: string;

  @Column('varchar', { name: 'ordem_exec', length: 3 })
  ordemExec: string;

  @Column('varchar', { name: 'tipo_executor', length: 1 })
  tipoExecutor: string;

  @Column('date', { name: 'data_valid', nullable: true })
  dataValid: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => OpeAtividade,
    (opeAtividade) => opeAtividade.opeCentro2OrdAtivs,
  )
  @JoinColumn([{ name: 'ope_atividade_id', referencedColumnName: 'id' }])
  opeAtividade: OpeAtividade;

  @ManyToOne(
    () => OpeCentro2Ord,
    (opeCentro2Ord) => opeCentro2Ord.opeCentro2OrdAtivs,
  )
  @JoinColumn([{ name: 'ope_centro2_ord_id', referencedColumnName: 'id' }])
  opeCentro2Ord: OpeCentro2Ord;

  @ManyToOne(
    () => OpeFrenteTrabalho,
    (opeFrenteTrabalho) => opeFrenteTrabalho.opeCentro2OrdAtivs,
  )
  @JoinColumn([{ name: 'ope_frente_trabalho_id', referencedColumnName: 'id' }])
  opeFrenteTrabalho: OpeFrenteTrabalho;

  @OneToMany(
    () => OpeCentro2OrdItemserv,
    (opeCentro2OrdItemserv) => opeCentro2OrdItemserv.opeCentro2OrdAtiv,
  )
  opeCentro2OrdItemservs: OpeCentro2OrdItemserv[];

  @OneToMany(
    () => OpeCentro2OrdRec,
    (opeCentro2OrdRec) => opeCentro2OrdRec.opeCentro2OrdAtiv,
  )
  opeCentro2OrdRecs: OpeCentro2OrdRec[];
}
