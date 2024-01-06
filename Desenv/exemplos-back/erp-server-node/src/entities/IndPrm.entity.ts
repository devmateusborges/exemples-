import { Column, Entity, Index, OneToMany } from 'typeorm';
import { IndFtdRelacPrm } from './IndFtdRelacPrm.entity';
import { IndRelRelacPrm } from './IndRelRelacPrm.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ind_prm', ['id'], { unique: true })
@Entity('ind_prm', { schema: 'public' })
export class IndPrm extends BaseEntity {
  @Column('varchar', { name: 'nome', nullable: true, length: 250 })
  nome: string;

  @Column('varchar', { name: 'ativo', nullable: true, length: 1 })
  ativo: string;

  @Column('varchar', {
    name: 'nome_tecnico',
    nullable: true,
    length: 100,
  })
  nomeTecnico: string;

  @Column('varchar', { name: 'tipo_dado', length: 2 })
  tipoDado: string;

  @Column('varchar', {
    name: 'tipo_entrada',
    nullable: true,
    length: 2,
  })
  tipoEntrada: string;

  @Column('varchar', {
    name: 'internal',
    nullable: true,
    length: 1,
    default: () => "'N'",
  })
  internal: string;

  @Column('varchar', {
    name: 'busca_tabela',
    nullable: true,
    length: 50,
  })
  buscaTabela: string;

  @Column('varchar', {
    name: 'busca_campo_nome',
    nullable: true,
    length: 50,
  })
  buscaCampoNome: string;

  @Column('varchar', {
    name: 'busca_campo_id',
    nullable: true,
    length: 50,
  })
  buscaCampoId: string;

  @Column('varchar', {
    name: 'busca_valores',
    nullable: true,
    length: 250,
  })
  buscaValores: string;

  @Column('varchar', {
    name: 'obrigatorio',
    nullable: true,
    length: 1,
  })
  obrigatorio: string;

  @Column('text', { name: 'valor_padrao', nullable: true })
  valorPadrao: string;

  @Column('varchar', { name: 'visivel', nullable: true, length: 1 })
  visivel: string;

  @Column('varchar', {
    name: 'busca_tabela_classe',
    nullable: true,
    length: 50,
  })
  buscaTabelaClasse: string;

  @Column('varchar', {
    name: 'busca_campo_nome_classe',
    nullable: true,
    length: 50,
  })
  buscaCampoNomeClasse: string;

  @Column('varchar', {
    name: 'busca_campo_id_classe',
    nullable: true,
    length: 50,
  })
  buscaCampoIdClasse: string;

  @Column('varchar', {
    name: 'valor_prefixo',
    nullable: true,
    length: 250,
  })
  valorPrefixo: string;

  @Column('varchar', {
    name: 'valor_sufixo',
    nullable: true,
    length: 250,
  })
  valorSufixo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => IndFtdRelacPrm, (indFtdRelacPrm) => indFtdRelacPrm.indPrm)
  indFtdRelacPrms: IndFtdRelacPrm[];

  @OneToMany(() => IndRelRelacPrm, (indRelRelacPrm) => indRelRelacPrm.indPrm)
  indRelRelacPrms: IndRelRelacPrm[];
}
