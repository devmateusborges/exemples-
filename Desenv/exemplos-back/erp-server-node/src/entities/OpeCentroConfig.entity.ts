import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { OpeCentroSubtipo } from './OpeCentroSubtipo.entity';
import { OpeCentroTipo } from './OpeCentroTipo.entity';
import { SystemUnit } from './SystemUnit.entity';
import { GerEmpresa } from './GerEmpresa.entity';
import { GerItemservGrupo } from './GerItemservGrupo.entity';
import { GerItemserv } from './GerItemserv.entity';
import { GerItemservSubgrupo } from './GerItemservSubgrupo.entity';
import { MovOperacao } from './MovOperacao.entity';
import { OpeAtividade } from './OpeAtividade.entity';
import { OpeCentro1 } from './OpeCentro1.entity';
import { OpeCentro2 } from './OpeCentro2.entity';
import { OpeCentro2OrdTipo } from './OpeCentro2OrdTipo.entity';
import { OpeCentroGrupo } from './OpeCentroGrupo.entity';
import { OpeCentroSubgrupo } from './OpeCentroSubgrupo.entity';
import { OpeCompartGrupo } from './OpeCompartGrupo.entity';
import { OpeCompart } from './OpeCompart.entity';
import { OpeCompartSubgrupo } from './OpeCompartSubgrupo.entity';
import { OpeEstagio } from './OpeEstagio.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro_regra_config', ['id'], { unique: true })
@Entity('ope_centro_config', { schema: 'public' })
export class OpeCentroConfig extends BaseEntity {
  @Column('varchar', { name: 'tipo_regra', length: 1 })
  tipoRegra: string;

  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(
    () => OpeCentroSubtipo,
    (opeCentroSubtipo) => opeCentroSubtipo.opeCentroConfigs,
  )
  @JoinColumn([{ name: 'ope_centro_subtipo_id', referencedColumnName: 'id' }])
  opeCentroSubtipo: OpeCentroSubtipo;

  @ManyToOne(
    () => OpeCentroTipo,
    (opeCentroTipo) => opeCentroTipo.opeCentroConfigs,
  )
  @JoinColumn([{ name: 'ope_centro_tipo_id', referencedColumnName: 'id' }])
  opeCentroTipo: OpeCentroTipo;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerEmpresa, (gerEmpresa) => gerEmpresa.opeCentroConfigs)
  @JoinColumn([{ name: 'ger_empresa_id', referencedColumnName: 'id' }])
  gerEmpresa: GerEmpresa;

  @ManyToOne(
    () => GerItemservGrupo,
    (gerItemservGrupo) => gerItemservGrupo.opeCentroConfigs,
  )
  @JoinColumn([{ name: 'ger_itemserv_grupo_id', referencedColumnName: 'id' }])
  gerItemservGrupo: GerItemservGrupo;

  @ManyToOne(() => GerItemserv, (gerItemserv) => gerItemserv.opeCentroConfigs)
  @JoinColumn([{ name: 'ger_itemserv_id', referencedColumnName: 'id' }])
  gerItemserv: GerItemserv;

  @ManyToOne(
    () => GerItemservSubgrupo,
    (gerItemservSubgrupo) => gerItemservSubgrupo.opeCentroConfigs,
  )
  @JoinColumn([
    { name: 'ger_itemserv_subgrupo_id', referencedColumnName: 'id' },
  ])
  gerItemservSubgrupo: GerItemservSubgrupo;

  @ManyToOne(() => MovOperacao, (movOperacao) => movOperacao.opeCentroConfigs)
  @JoinColumn([{ name: 'mov_operacao_id', referencedColumnName: 'id' }])
  movOperacao: MovOperacao;

  @ManyToOne(
    () => OpeAtividade,
    (opeAtividade) => opeAtividade.opeCentroConfigs,
  )
  @JoinColumn([{ name: 'ope_atividade_id', referencedColumnName: 'id' }])
  opeAtividade: OpeAtividade;

  @ManyToOne(() => OpeCentro1, (opeCentro1) => opeCentro1.opeCentroConfigs)
  @JoinColumn([{ name: 'ope_centro1_id', referencedColumnName: 'id' }])
  opeCentro1: OpeCentro1;

  @ManyToOne(() => OpeCentro2, (opeCentro2) => opeCentro2.opeCentroConfigs)
  @JoinColumn([{ name: 'ope_centro2_id', referencedColumnName: 'id' }])
  opeCentro2: OpeCentro2;

  @ManyToOne(
    () => OpeCentro2OrdTipo,
    (opeCentro2OrdTipo) => opeCentro2OrdTipo.opeCentroConfigs,
  )
  @JoinColumn([{ name: 'ope_centro2_ord_tipo_id', referencedColumnName: 'id' }])
  opeCentro2OrdTipo: OpeCentro2OrdTipo;

  @ManyToOne(
    () => OpeCentroGrupo,
    (opeCentroGrupo) => opeCentroGrupo.opeCentroConfigs,
  )
  @JoinColumn([{ name: 'ope_centro_grupo_id', referencedColumnName: 'id' }])
  opeCentroGrupo: OpeCentroGrupo;

  @ManyToOne(
    () => OpeCentroSubgrupo,
    (opeCentroSubgrupo) => opeCentroSubgrupo.opeCentroConfigs,
  )
  @JoinColumn([{ name: 'ope_centro_subgrupo_id', referencedColumnName: 'id' }])
  opeCentroSubgrupo: OpeCentroSubgrupo;

  @ManyToOne(
    () => OpeCompartGrupo,
    (opeCompartGrupo) => opeCompartGrupo.opeCentroConfigs,
  )
  @JoinColumn([{ name: 'ope_compart_grupo_id', referencedColumnName: 'id' }])
  opeCompartGrupo: OpeCompartGrupo;

  @ManyToOne(() => OpeCompart, (opeCompart) => opeCompart.opeCentroConfigs)
  @JoinColumn([{ name: 'ope_compart_id', referencedColumnName: 'id' }])
  opeCompart: OpeCompart;

  @ManyToOne(
    () => OpeCompartSubgrupo,
    (opeCompartSubgrupo) => opeCompartSubgrupo.opeCentroConfigs,
  )
  @JoinColumn([{ name: 'ope_compart_subgrupo_id', referencedColumnName: 'id' }])
  opeCompartSubgrupo: OpeCompartSubgrupo;

  @ManyToOne(() => OpeEstagio, (opeEstagio) => opeEstagio.opeCentroConfigs)
  @JoinColumn([{ name: 'ope_estagio_id', referencedColumnName: 'id' }])
  opeEstagio: OpeEstagio;
}
