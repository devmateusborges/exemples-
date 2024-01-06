import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { TestFka } from './TestFka.entity';
import { TestPai } from './TestPai.entity';
import { SystemUnit } from './SystemUnit.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_test_filho_2', ['id'], { unique: true })
@Entity('test_filho_2', { schema: 'public' })
export class TestFilho_2 extends BaseEntity {
  @Column('varchar', {
    name: 'campo_texto',
    nullable: true,
    length: 100,
  })
  campoTexto: string;

  @Column('varchar', {
    name: 'campo_combo',
    nullable: true,
    length: 100,
  })
  campoCombo: string;

  @Column('date', { name: 'campo_data', nullable: true })
  campoData: string;

  @Column('varchar', {
    name: 'campo_radio',
    nullable: true,
    length: 2,
  })
  campoRadio: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => TestFka, (testFka) => testFka.testFilhoS2)
  @JoinColumn([{ name: 'test_fka_id', referencedColumnName: 'id' }])
  testFka: TestFka;

  @ManyToOne(() => TestPai, (testPai) => testPai.testFilhoS2)
  @JoinColumn([{ name: 'test_pai_id', referencedColumnName: 'id' }])
  testPai: TestPai;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
