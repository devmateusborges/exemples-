import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { GerUmedida } from './GerUmedida.entity';
import { SystemUnit } from './SystemUnit.entity';
import { OpeOcorGrupo } from './OpeOcorGrupo.entity';
import { OpeOcorMovDet } from './OpeOcorMovDet.entity';
import { OpeOcorPrev } from './OpeOcorPrev.entity';
import { SystemDocument } from './SystemDocument.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_ocor', ['id'], { unique: true })
@Entity('ope_ocor', { schema: 'public' })
export class OpeOcor extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_ocor', length: 50 })
  siglaOcor: string;

  @Column('varchar', { name: 'icon', length: 50 })
  icon: string;

  @Column('varchar', { name: 'tipo', length: 1 })
  tipo: string;

  @Column('varchar', { name: 'tipo_lanc', length: 1 })
  tipoLanc: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => GerUmedida, (gerUmedida) => gerUmedida.opeOcors)
  @JoinColumn([{ name: 'ger_umedida_id', referencedColumnName: 'id' }])
  gerUmedida: GerUmedida;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => OpeOcorGrupo, (opeOcorGrupo) => opeOcorGrupo.opeOcors)
  @JoinColumn([{ name: 'ope_ocor_grupo_id', referencedColumnName: 'id' }])
  opeOcorGrupo: OpeOcorGrupo;

  @OneToMany(() => OpeOcorMovDet, (opeOcorMovDet) => opeOcorMovDet.opeOcor)
  opeOcorMovDets: OpeOcorMovDet[];

  @OneToMany(() => OpeOcorPrev, (opeOcorPrev) => opeOcorPrev.opeOcor)
  opeOcorPrevs: OpeOcorPrev[];

  @OneToMany(() => SystemDocument, (systemDocument) => systemDocument.opeOcor)
  systemDocuments: SystemDocument[];
}
