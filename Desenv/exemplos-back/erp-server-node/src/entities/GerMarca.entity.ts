import { Column, Entity, Index, OneToMany } from 'typeorm';
import { GerMarcaModelo } from './GerMarcaModelo.entity';
import { GerMarcaPessoa } from './GerMarcaPessoa.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_marca', ['id'], { unique: true })
@Entity('ger_marca', { schema: 'public' })
export class GerMarca extends BaseEntity {
  @Column('varchar', { name: 'unit_id', length: 36 })
  unitId: string;

  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => GerMarcaModelo, (gerMarcaModelo) => gerMarcaModelo.gerMarca)
  gerMarcaModelos: GerMarcaModelo[];

  @OneToMany(() => GerMarcaPessoa, (gerMarcaPessoa) => gerMarcaPessoa.gerMarca)
  gerMarcaPessoas: GerMarcaPessoa[];
}
