import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { TestFilho_1 } from './TestFilho_1.entity';
import { TestFilho_2 } from './TestFilho_2.entity';
import { TestFilho_3 } from './TestFilho_3.entity';
import { TestFilho_4 } from './TestFilho_4.entity';
import { SystemUnit } from './SystemUnit.entity';
import { TestPai } from './TestPai.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_test_fka', ['id'], { unique: true })
@Entity('test_fka', { schema: 'public' })
export class TestFka extends BaseEntity {
  @Column('varchar', { name: 'nome', length: 100 })
  nome: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => TestFilho_1, (testFilho_1) => testFilho_1.testFka)
  testFilhoS: TestFilho_1[];

  @OneToMany(() => TestFilho_2, (testFilho_2) => testFilho_2.testFka)
  testFilhoS2: TestFilho_2[];

  @OneToMany(() => TestFilho_3, (testFilho_3) => testFilho_3.testFka)
  testFilhoS3: TestFilho_3[];

  @OneToMany(() => TestFilho_4, (testFilho_4) => testFilho_4.testFka)
  testFilhoS4: TestFilho_4[];

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @OneToMany(() => TestPai, (testPai) => testPai.testFka)
  testPais: TestPai[];
}
