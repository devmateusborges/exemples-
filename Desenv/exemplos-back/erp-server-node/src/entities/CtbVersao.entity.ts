import { Column, Entity, Index, OneToMany } from 'typeorm';
import { CtbLanc } from './CtbLanc.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ctb_versao', ['id'], { unique: true })
@Entity('ctb_versao', { schema: 'public' })
export class CtbVersao extends BaseEntity {
  @Column('varchar', { name: 'unit_id', length: 36 })
  unitId: string;

  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'sigla_versao', length: 50 })
  siglaVersao: string;

  @Column('varchar', { name: 'tipo_rp', length: 1 })
  tipoRp: string;

  @Column('varchar', { name: 'versao_atual', default: () => "'N'" })
  versaoAtual: string;

  @Column('date', { name: 'data_per_ini' })
  dataPerIni: string;

  @Column('date', { name: 'data_per_fin' })
  dataPerFin: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => CtbLanc, (ctbLanc) => ctbLanc.ctbVersao)
  ctbLancs: CtbLanc[];
}
