import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { PtoMarcacao } from '../../entities/PtoMarcacao.entity';
import { PtoMedidor } from '../../entities/PtoMedidor.entity';
import { PtoUnitParam } from '../../entities/PtoUnitParam.entity';

@Module({
  imports: [TypeOrmModule.forFeature([PtoMarcacao, PtoMedidor, PtoUnitParam])],
  providers: [],
  controllers: [],
  exports: [],
})
export class PtoModule {}
