import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { GerMarca } from './GerMarca.entity';
import { GerPessoa } from './GerPessoa.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_marca_pessoa', ['id'], { unique: true })
@Entity('ger_marca_pessoa', { schema: 'public' })
export class GerMarcaPessoa extends BaseEntity {
  @Column('varchar', {
    name: 'observacao',
    nullable: true,
    length: 250,
  })
  observacao: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerMarca, (gerMarca) => gerMarca.gerMarcaPessoas, {
    onDelete: 'CASCADE',
    onUpdate: 'CASCADE',
  })
  @JoinColumn([{ name: 'ger_marca_id', referencedColumnName: 'id' }])
  gerMarca: GerMarca;

  @ManyToOne(() => GerPessoa, (gerPessoa) => gerPessoa.gerMarcaPessoas)
  @JoinColumn([{ name: 'ger_pessoa_id', referencedColumnName: 'id' }])
  gerPessoa: GerPessoa;
}
