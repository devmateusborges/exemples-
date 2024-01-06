import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { GerPessoaEndereco } from './GerPessoaEndereco.entity';
import { Mov } from './Mov.entity';
import { OpeCentro2Equip } from './OpeCentro2Equip.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_mov_frete', ['id'], { unique: true })
@Entity('mov_frete', { schema: 'public' })
export class MovFrete extends BaseEntity {
  @Column('numeric', { name: 'valor_frete', precision: 18, scale: 6 })
  valorFrete: string;

  @Column('varchar', { name: 'adic_frete_base_cal_icms', length: 1 })
  adicFreteBaseCalIcms: string;

  @Column('numeric', { name: 'valor_base_calc', precision: 18, scale: 6 })
  valorBaseCalc: string;

  @Column('numeric', { name: 'perc_aliquota', precision: 18, scale: 6 })
  percAliquota: string;

  @Column('numeric', { name: 'valor_imposto', precision: 18, scale: 6 })
  valorImposto: string;

  @Column('numeric', { name: 'valor_pis', precision: 18, scale: 6 })
  valorPis: string;

  @Column('numeric', { name: 'valor_cofins', precision: 18, scale: 6 })
  valorCofins: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.movFretes,
  )
  @JoinColumn([
    { name: 'ger_pessoa_endereco_id_condutor', referencedColumnName: 'id' },
  ])
  gerPessoaEnderecoIdCondutor: GerPessoaEndereco;

  @ManyToOne(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.movFretes2,
  )
  @JoinColumn([
    { name: 'ger_pessoa_endereco_id_transp', referencedColumnName: 'id' },
  ])
  gerPessoaEnderecoIdTransp: GerPessoaEndereco;

  @ManyToOne(() => Mov, (mov) => mov.movFretes)
  @JoinColumn([{ name: 'mov_id', referencedColumnName: 'id' }])
  mov: Mov;

  @ManyToOne(
    () => OpeCentro2Equip,
    (opeCentro2Equip) => opeCentro2Equip.movFretes,
  )
  @JoinColumn([{ name: 'ope_centro2_id_equip', referencedColumnName: 'id' }])
  opeCentro2IdEquip: OpeCentro2Equip;
}
