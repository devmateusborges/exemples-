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
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_fis_certificado', ['id'], { unique: true })
@Entity('fis_certificado', { schema: 'public' })
export class FisCertificado extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column('varchar', { name: 'ativo', length: 1 })
  ativo: string;

  @Column('varchar', {
    name: 'nome_arq_certificado',
    nullable: true,
    length: 250,
  })
  nomeArqCertificado: string;

  @Column('varchar', { name: 'senha', nullable: true, length: 50 })
  senha: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(() => GerEmpresa, (gerEmpresa) => gerEmpresa.fisCertificado)
  gerEmpresas: GerEmpresa[];
}
