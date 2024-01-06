import { Column, Entity, Index, OneToMany } from 'typeorm';
import { FisDoc } from './FisDoc.entity';
import { Mov } from './Mov.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fis_doc_tipo', ['id'], { unique: true })
@Entity('fis_doc_tipo', { schema: 'public' })
export class FisDocTipo extends BaseEntity {
  @Column('varchar', { name: 'modelo', length: 50 })
  modelo: string;

  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => FisDoc, (fisDoc) => fisDoc.fisDocTipo)
  fisDocs: FisDoc[];

  @OneToMany(() => Mov, (mov) => mov.fisDocTipo)
  movs: Mov[];
}
