import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { TestFilho_1 } from '../../entities/TestFilho_1.entity';
import { TestFilho_2 } from '../../entities/TestFilho_2.entity';
import { TestFilho_3 } from '../../entities/TestFilho_3.entity';
import { TestFilho_4 } from '../../entities/TestFilho_4.entity';
import { TestFka } from '../../entities/TestFka.entity';
import { TestFkb } from '../../entities/TestFkb.entity';
import { TestPai } from '../../entities/TestPai.entity';

@Module({
  imports: [
    TypeOrmModule.forFeature([
      TestFilho_1,
      TestFilho_2,
      TestFilho_3,
      TestFilho_4,
      TestFka,
      TestFkb,
      TestPai,
    ]),
  ],
  providers: [],
  controllers: [],
  exports: [],
})
export class TstModule {}
