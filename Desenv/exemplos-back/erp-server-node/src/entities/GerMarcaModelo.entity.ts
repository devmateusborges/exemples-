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
import { GerMarca } from './GerMarca.entity';
import { OpeCentro2 } from './OpeCentro2.entity';
import { OpeCentro2MovMedia } from './OpeCentro2MovMedia.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_marca_modelo', ['id'], { unique: true })
@Entity('ger_marca_modelo', { schema: 'public' })
export class GerMarcaModelo extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => GerMarca, (gerMarca) => gerMarca.gerMarcaModelos, {
    onDelete: 'CASCADE',
  })
  @JoinColumn([{ name: 'ger_marca_id', referencedColumnName: 'id' }])
  gerMarca: GerMarca;

  @OneToMany(() => OpeCentro2, (opeCentro2) => opeCentro2.gerMarcaModelo)
  opeCentros: OpeCentro2[];

  @OneToMany(
    () => OpeCentro2MovMedia,
    (opeCentro2MovMedia) => opeCentro2MovMedia.gerMarcaModelo,
  )
  opeCentro2MovMedias: OpeCentro2MovMedia[];
}
