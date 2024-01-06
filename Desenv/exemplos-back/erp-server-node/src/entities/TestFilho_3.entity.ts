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

@Index('pk_test_filho_3_campo_unico', ['id'], { unique: true })
@Entity('test_filho_3', { schema: 'public' })
export class TestFilho_3 extends BaseEntity {
  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => TestFka, (testFka) => testFka.testFilhoS3)
  @JoinColumn([{ name: 'test_fka_id', referencedColumnName: 'id' }])
  testFka: TestFka;

  @ManyToOne(() => TestPai, (testPai) => testPai.testFilhoS3)
  @JoinColumn([{ name: 'test_pai_id', referencedColumnName: 'id' }])
  testPai: TestPai;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
