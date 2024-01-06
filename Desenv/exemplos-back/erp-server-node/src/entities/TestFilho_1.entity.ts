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

@Index('pk_test_filho_1', ['id'], { unique: true })
@Entity('test_filho_1', { schema: 'public' })
export class TestFilho_1 extends BaseEntity {
  @Column('varchar', {
    name: 'campo_texto',
    nullable: true,
    length: 100,
  })
  campoTexto: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => TestFka, (testFka) => testFka.testFilhoS)
  @JoinColumn([{ name: 'test_fka_id', referencedColumnName: 'id' }])
  testFka: TestFka;

  @ManyToOne(() => TestPai, (testPai) => testPai.testFilhoS)
  @JoinColumn([{ name: 'test_pai_id', referencedColumnName: 'id' }])
  testPai: TestPai;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;
}
