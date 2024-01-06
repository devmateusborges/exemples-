import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { BovUnitParam } from '../../entities/BovUnitParam.entity';

@Module({
  imports: [TypeOrmModule.forFeature([BovUnitParam])],
  providers: [],
  controllers: [],
  exports: [],
})
export class BovModule {}
