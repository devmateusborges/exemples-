import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { BorDispositivo } from '../../entities/BorDispositivo.entity';
import { BorMov } from '../../entities/BorMov.entity';
import { BorMovAtual } from '../../entities/BorMovAtual.entity';
import { BorMsg } from '../../entities/BorMsg.entity';
import { BorTel } from '../../entities/BorTel.entity';
import { BorUnitParam } from '../../entities/BorUnitParam.entity';

@Module({
  imports: [
    TypeOrmModule.forFeature([
      BorDispositivo,
      BorMov,
      BorMovAtual,
      BorMsg,
      BorTel,
      BorUnitParam,
    ]),
  ],
  providers: [],
  controllers: [],
  exports: [],
})
export class BorModule {}
