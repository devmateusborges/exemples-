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
import { OpeOcorCompartMovDet } from './OpeOcorCompartMovDet.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ope_compart_mov', ['id'], { unique: true })
@Entity('ope_ocor_compart_mov', { schema: 'public' })
export class OpeOcorCompartMov extends BaseEntity {
  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column('date', { name: 'data_mov', nullable: true })
  dataMov: string;

  @Column('varchar', { name: 'numero', nullable: true, length: 50 })
  numero: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerEmpresa, (gerEmpresa) => gerEmpresa.opeOcorCompartMovs)
  @JoinColumn([{ name: 'ger_empresa_id', referencedColumnName: 'id' }])
  gerEmpresa: GerEmpresa;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.opeOcorCompartMovs,
  )
  @JoinColumn([
    { name: 'ger_pessoa_endereco_id_exec', referencedColumnName: 'id' },
  ])
  gerPessoaEnderecoIdExec: GerPessoaEndereco;

  @OneToMany(
    () => OpeOcorCompartMovDet,
    (opeOcorCompartMovDet) => opeOcorCompartMovDet.opeCompartMov,
  )
  opeOcorCompartMovDets: OpeOcorCompartMovDet[];
}
