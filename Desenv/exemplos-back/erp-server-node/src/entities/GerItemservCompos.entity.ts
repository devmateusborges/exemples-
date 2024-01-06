import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { GerItemservComposTipo } from './GerItemservComposTipo.entity';
import { GerItemserv } from './GerItemserv.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_itemserv_compos', ['id'], { unique: true })
@Entity('ger_itemserv_compos', { schema: 'public' })
export class GerItemservCompos extends BaseEntity {
  @Column('numeric', {
    name: 'fator_mult',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  fatorMult: string;

  @Column('numeric', {
    name: 'qnt_compos',
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  qntCompos: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column('varchar', { name: 'ordem', length: 50 })
  ordem: string;

  @Column('numeric', {
    name: 'qnt_altura',
    nullable: true,
    precision: 18,
    scale: 6,
    default: () => '0',
  })
  qntAltura: string;

  @Column('numeric', {
    name: 'qnt_largura',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  qntLargura: string;

  @Column('numeric', {
    name: 'qnt_comprimento',
    nullable: true,
    precision: 18,
    scale: 6,
  })
  qntComprimento: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(
    () => GerItemservComposTipo,
    (gerItemservComposTipo) => gerItemservComposTipo.gerItemservCompos,
  )
  @JoinColumn([
    { name: 'ger_itemserv_compos_tipo_id', referencedColumnName: 'id' },
  ])
  gerItemservComposTipo: GerItemservComposTipo;

  @ManyToOne(() => GerItemserv, (gerItemserv) => gerItemserv.gerItemservCompos)
  @JoinColumn([{ name: 'ger_itemserv_id_de', referencedColumnName: 'id' }])
  gerItemservIdDe: GerItemserv;

  @ManyToOne(() => GerItemserv, (gerItemserv) => gerItemserv.gerItemservCompos2)
  @JoinColumn([{ name: 'ger_itemserv_id_para', referencedColumnName: 'id' }])
  gerItemservIdPara: GerItemserv;
}
