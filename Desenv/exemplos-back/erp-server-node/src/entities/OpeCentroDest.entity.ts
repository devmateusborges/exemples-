import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { FinPagrecBanco } from './FinPagrecBanco.entity';
import { FinPagrec } from './FinPagrec.entity';
import { MovItemserv } from './MovItemserv.entity';
import { OpeAtividade } from './OpeAtividade.entity';
import { OpeCentro1 } from './OpeCentro1.entity';
import { OpeCentro2 } from './OpeCentro2.entity';
import { OpeCentroRatTipo } from './OpeCentroRatTipo.entity';
import { OpeCompart } from './OpeCompart.entity';
import { OpePeriodo } from './OpePeriodo.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_centro_dest', ['id'], { unique: true })
@Entity('ope_centro_dest', { schema: 'public' })
export class OpeCentroDest extends BaseEntity {
  @Column('numeric', {
    name: 'valor',
    precision: 18,
    scale: 2,
    default: () => '0',
  })
  valor: string;

  @Column('numeric', { name: 'qnt', precision: 18, scale: 6 })
  qnt: string;

  @Column('varchar', { name: 'tipo_es', length: 1 })
  tipoEs: string;

  @Column('varchar', {
    name: 'tipo_ps',
    nullable: true,
    length: 1,
    default: () => "'P'",
  })
  tipoPs: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => FinPagrecBanco,
    (finPagrecBanco) => finPagrecBanco.opeCentroDests,
  )
  @JoinColumn([{ name: 'fin_pagrec_banco_id', referencedColumnName: 'id' }])
  finPagrecBanco: FinPagrecBanco;

  @ManyToOne(() => FinPagrec, (finPagrec) => finPagrec.opeCentroDests)
  @JoinColumn([{ name: 'fin_pagrec_id', referencedColumnName: 'id' }])
  finPagrec: FinPagrec;

  @ManyToOne(() => MovItemserv, (movItemserv) => movItemserv.opeCentroDests)
  @JoinColumn([{ name: 'mov_itemserv_id', referencedColumnName: 'id' }])
  movItemserv: MovItemserv;

  @ManyToOne(() => OpeAtividade, (opeAtividade) => opeAtividade.opeCentroDests)
  @JoinColumn([{ name: 'ope_atividade_id', referencedColumnName: 'id' }])
  opeAtividade: OpeAtividade;

  @ManyToOne(() => OpeCentro1, (opeCentro1) => opeCentro1.opeCentroDests)
  @JoinColumn([{ name: 'ope_centro1_id', referencedColumnName: 'id' }])
  opeCentro1: OpeCentro1;

  @ManyToOne(() => OpeCentro1, (opeCentro1) => opeCentro1.opeCentroDests2)
  @JoinColumn([{ name: 'ope_centro1_id_dest', referencedColumnName: 'id' }])
  opeCentro1IdDest: OpeCentro1;

  @ManyToOne(() => OpeCentro2, (opeCentro2) => opeCentro2.opeCentroDests)
  @JoinColumn([{ name: 'ope_centro2_id', referencedColumnName: 'id' }])
  opeCentro2: OpeCentro2;

  @ManyToOne(() => OpeCentro2, (opeCentro2) => opeCentro2.opeCentroDests2)
  @JoinColumn([{ name: 'ope_centro2_id_dest', referencedColumnName: 'id' }])
  opeCentro2IdDest: OpeCentro2;

  @ManyToOne(
    () => OpeCentroRatTipo,
    (opeCentroRatTipo) => opeCentroRatTipo.opeCentroDests,
  )
  @JoinColumn([{ name: 'ope_centro_rat_tipo_id', referencedColumnName: 'id' }])
  opeCentroRatTipo: OpeCentroRatTipo;

  @ManyToOne(() => OpeCompart, (opeCompart) => opeCompart.opeCentroDests)
  @JoinColumn([{ name: 'ope_compart_id', referencedColumnName: 'id' }])
  opeCompart: OpeCompart;

  @ManyToOne(() => OpePeriodo, (opePeriodo) => opePeriodo.opeCentroDests)
  @JoinColumn([{ name: 'ope_periodo_id_dest', referencedColumnName: 'id' }])
  opePeriodoIdDest: OpePeriodo;
}
