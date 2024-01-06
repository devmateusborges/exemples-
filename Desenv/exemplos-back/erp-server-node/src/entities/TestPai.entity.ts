import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { SystemDocument } from './SystemDocument.entity';
import { TestFilho_1 } from './TestFilho_1.entity';
import { TestFilho_2 } from './TestFilho_2.entity';
import { TestFilho_3 } from './TestFilho_3.entity';
import { TestFilho_4 } from './TestFilho_4.entity';
import { TestFka } from './TestFka.entity';
import { TestFkb } from './TestFkb.entity';
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_test_pai', ['id'], { unique: true })
@Entity('test_pai', { schema: 'public' })
export class TestPai extends BaseEntity {
  @Column('varchar', {
    name: 'campo_texto',
    nullable: true,
    length: 100,
  })
  campoTexto: string;

  @Column('text', { name: 'campo_texto_grande', nullable: true })
  campoTextoGrande: string;

  @Column('varchar', {
    name: 'campo_escondido',
    nullable: true,
    length: 100,
  })
  campoEscondido: string;

  @Column('varchar', {
    name: 'campo_combo',
    nullable: true,
    length: 100,
  })
  campoCombo: string;

  @Column('varchar', {
    name: 'campo_radio',
    nullable: true,
    length: 100,
  })
  campoRadio: string;

  @Column('varchar', {
    name: 'campo_data',
    nullable: true,
    length: 100,
  })
  campoData: string;

  @Column('varchar', {
    name: 'campo_numero',
    nullable: true,
    length: 100,
  })
  campoNumero: string;

  @Column('varchar', {
    name: 'campo_icon',
    nullable: true,
    length: 100,
  })
  campoIcon: string;

  @Column('varchar', {
    name: 'campo_cor',
    nullable: true,
    length: 100,
  })
  campoCor: string;

  @Column('varchar', {
    name: 'campo_senha',
    nullable: true,
    length: 100,
  })
  campoSenha: string;

  @Column('varchar', {
    name: 'campo_arquivo',
    nullable: true,
    length: 100,
  })
  campoArquivo: string;

  @Column('varchar', {
    name: 'campo_radio2',
    nullable: true,
    length: 100,
  })
  campoRadio2: string;

  @Column('varchar', {
    name: 'campo_combo2',
    nullable: true,
    length: 100,
  })
  campoCombo2: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => SystemDocument, (systemDocument) => systemDocument.testPai)
  systemDocuments: SystemDocument[];

  @OneToMany(() => TestFilho_1, (testFilho_1) => testFilho_1.testPai)
  testFilhoS: TestFilho_1[];

  @OneToMany(() => TestFilho_2, (testFilho_2) => testFilho_2.testPai)
  testFilhoS2: TestFilho_2[];

  @OneToMany(() => TestFilho_3, (testFilho_3) => testFilho_3.testPai)
  testFilhoS3: TestFilho_3[];

  @OneToMany(() => TestFilho_4, (testFilho_4) => testFilho_4.testPai)
  testFilhoS4: TestFilho_4[];

  @ManyToOne(() => TestFka, (testFka) => testFka.testPais)
  @JoinColumn([{ name: 'test_fka_id', referencedColumnName: 'id' }])
  testFka: TestFka;

  @ManyToOne(() => TestFkb, (testFkb) => testFkb.testPais)
  @JoinColumn([{ name: 'test_fkb_id', referencedColumnName: 'id' }])
  testFkb: TestFkb;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
