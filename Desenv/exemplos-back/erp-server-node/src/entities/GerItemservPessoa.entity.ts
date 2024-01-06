import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { GerItemserv } from './GerItemserv.entity';
import { GerPessoa } from './GerPessoa.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_itemserv_pessoa', ['id'], { unique: true })
@Entity('ger_itemserv_pessoa', { schema: 'public' })
export class GerItemservPessoa extends BaseEntity {
  @Column('varchar', { name: 'cod_itemserv_ext', length: 50 })
  codItemservExt: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerItemserv, (gerItemserv) => gerItemserv.gerItemservPessoas)
  @JoinColumn([{ name: 'ger_itemserv_id', referencedColumnName: 'id' }])
  gerItemserv: GerItemserv;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.gerItemservPessoas)
  @JoinColumn([{ name: 'ger_pessoa_id', referencedColumnName: 'id' }])
  gerPessoa: GerPessoa;
}
