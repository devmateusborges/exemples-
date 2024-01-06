import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { GerUf } from './GerUf.entity';
import { GerEmpresa } from './GerEmpresa.entity';
import { GerPessoaEndereco } from './GerPessoaEndereco.entity';
import { Mov } from './Mov.entity';
import { MovEntrega } from './MovEntrega.entity';
import { MovPercurso } from './MovPercurso.entity';
import { OpeCentro2Equip } from './OpeCentro2Equip.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ger_cidade', ['id'], { unique: true })
@Entity('ger_cidade', { schema: 'public' })
export class GerCidade extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', { name: 'nr_cidade', length: 50 })
  nrCidade: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => GerUf, (gerUf) => gerUf.gerCidades)
  @JoinColumn([{ name: 'ger_uf_id', referencedColumnName: 'id' }])
  gerUf: GerUf;

  @OneToMany(() => GerEmpresa, (gerEmpresa) => gerEmpresa.endGerCidade)
  gerEmpresas: GerEmpresa[];

  @OneToMany(
    () => GerPessoaEndereco,
    (gerPessoaEndereco) => gerPessoaEndereco.endGerCidade,
  )
  gerPessoaEnderecos: GerPessoaEndereco[];

  @OneToMany(() => Mov, (mov) => mov.gerCidadeIdCarreg)
  movs: Mov[];

  @OneToMany(() => Mov, (mov) => mov.gerCidadeIdDescarreg)
  movs2: Mov[];

  @OneToMany(() => MovEntrega, (movEntrega) => movEntrega.gerCidade)
  movEntregas: MovEntrega[];

  @OneToMany(() => MovPercurso, (movPercurso) => movPercurso.gerCidade)
  movPercursos: MovPercurso[];

  @OneToMany(
    () => OpeCentro2Equip,
    (opeCentro2Equip) => opeCentro2Equip.gerCidade,
  )
  opeCentro2Equips: OpeCentro2Equip[];
}
