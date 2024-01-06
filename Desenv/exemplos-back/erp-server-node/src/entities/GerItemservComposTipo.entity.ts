import { Column, Entity, Index, OneToMany } from 'typeorm';
import { GerItemservCompos } from './GerItemservCompos.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_itemserv_compos_tipo', ['id'], { unique: true })
@Entity('ger_itemserv_compos_tipo', { schema: 'public' })
export class GerItemservComposTipo extends BaseEntity {
  @Column('varchar', { name: 'unit_id', length: 36 })
  unitId: string;

  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(
    () => GerItemservCompos,
    (gerItemservCompos) => gerItemservCompos.gerItemservComposTipo,
  )
  gerItemservCompos: GerItemservCompos[];
}
