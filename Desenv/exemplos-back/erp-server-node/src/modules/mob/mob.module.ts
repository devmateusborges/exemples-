import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { MobUnitParam } from '../../entities/MobUnitParam.entity';

@Module({
  imports: [TypeOrmModule.forFeature([MobUnitParam])],
  providers: [],
  controllers: [],
  exports: [],
})
export class MobModule {}
