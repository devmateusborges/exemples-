import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { BorDispositivo } from './BorDispositivo.entity';
import { OpeCentro2Ord } from './OpeCentro2Ord.entity';
import { SystemUnit } from './SystemUnit.entity';
import { OpeCentro2 } from './OpeCentro2.entity';
import { OpeFrenteTrabalho } from './OpeFrenteTrabalho.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro2_pessoa', ['id'], { unique: true })
@Entity('ope_centro2_pessoa', { schema: 'public' })
export class OpeCentro2Pessoa extends BaseEntity {
  @Column('varchar', {
    name: 'pto_idenf_tipo',
    nullable: true,
    length: 1,
  })
  ptoIdenfTipo: string;

  @Column('varchar', {
    name: 'pto_idenf',
    nullable: true,
    length: 50,
  })
  ptoIdenf: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => BorDispositivo,
    (borDispositivo) => borDispositivo.opeCentro2Pessoa,
  )
  borDispositivos: BorDispositivo[];

  @OneToMany(
    () => OpeCentro2Ord,
    (opeCentro2Ord) => opeCentro2Ord.opeCentro2PessoaIdSolic,
  )
  opeCentro2Ords: OpeCentro2Ord[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => OpeCentro2, (opeCentro2) => opeCentro2.opeCentro2Pessoas)
  @JoinColumn([{ name: 'ope_centro2_id', referencedColumnName: 'id' }])
  opeCentro2: OpeCentro2;

  @ManyToOne(
    () => OpeFrenteTrabalho,
    (opeFrenteTrabalho) => opeFrenteTrabalho.opeCentro2Pessoas,
  )
  @JoinColumn([{ name: 'ope_frente_trabalho_id', referencedColumnName: 'id' }])
  opeFrenteTrabalho: OpeFrenteTrabalho;
}
