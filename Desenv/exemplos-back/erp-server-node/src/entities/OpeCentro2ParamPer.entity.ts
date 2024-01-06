import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { GerEmpresa } from './GerEmpresa.entity';
import { OpeCentro2 } from './OpeCentro2.entity';
import { OpeFrenteTrabalho } from './OpeFrenteTrabalho.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro2_param_per', ['id'], { unique: true })
@Entity('ope_centro2_param_per', { schema: 'public' })
export class OpeCentro2ParamPer extends BaseEntity {
  @Column('date', { name: 'dt_valid_ini', default: () => 'now()' })
  dtValidIni: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerEmpresa, (gerEmpresa) => gerEmpresa.opeCentro2ParamPers)
  @JoinColumn([{ name: 'ger_empresa_id', referencedColumnName: 'id' }])
  gerEmpresa: GerEmpresa;

  @ManyToOne(() => OpeCentro2, (opeCentro2) => opeCentro2.opeCentro2ParamPers)
  @JoinColumn([{ name: 'ope_centro2_id', referencedColumnName: 'id' }])
  opeCentro2: OpeCentro2;

  @ManyToOne(
    () => OpeFrenteTrabalho,
    (opeFrenteTrabalho) => opeFrenteTrabalho.opeCentro2ParamPers,
  )
  @JoinColumn([{ name: 'ope_frente_trabalho_id', referencedColumnName: 'id' }])
  opeFrenteTrabalho: OpeFrenteTrabalho;
}
