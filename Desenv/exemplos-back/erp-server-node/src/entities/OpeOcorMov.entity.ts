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
import { GerEmpresa } from './GerEmpresa.entity';
import { GerPessoaEndereco } from './GerPessoaEndereco.entity';
import { OpeOcorTipo } from './OpeOcorTipo.entity';
import { OpeOcorMovDest } from './OpeOcorMovDest.entity';
import { OpeOcorMovDet } from './OpeOcorMovDet.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_ocor_mov', ['id'], { unique: true })
@Entity('ope_ocor_mov', { schema: 'public' })
export class OpeOcorMov extends BaseEntity {
  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column('date', { name: 'data_mov' })
  dataMov: string;

  @Column('varchar', { name: 'numero', length: 50 })
  numero: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerEmpresa, (gerEmpresa) => gerEmpresa.opeOcorMovs)
  @JoinColumn([{ name: 'ger_empresa_id', referencedColumnName: 'id' }])
  gerEmpresa: GerEmpresa;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.opeOcorMovs,
  )
  @JoinColumn([
    { name: 'ger_pessoa_endereco_id_exec', referencedColumnName: 'id' },
  ])
  gerPessoaEnderecoIdExec: GerPessoaEndereco;

  @ManyToOne(() => OpeOcorTipo, (opeOcorTipo) => opeOcorTipo.opeOcorMovs)
  @JoinColumn([{ name: 'ope_ocor_tipo_id', referencedColumnName: 'id' }])
  opeOcorTipo: OpeOcorTipo;

  @OneToMany(
    () => OpeOcorMovDest,
    (opeOcorMovDest) => opeOcorMovDest.opeOcorMov,
  )
  opeOcorMovDests: OpeOcorMovDest[];

  @OneToMany(() => OpeOcorMovDet, (opeOcorMovDet) => opeOcorMovDet.opeOcorMov)
  opeOcorMovDets: OpeOcorMovDet[];
}
