import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { FisCertificado } from '../../entities/FisCertificado.entity';
import { FisCest } from '../../entities/FisCest.entity';
import { FisCestNcm } from '../../entities/FisCestNcm.entity';
import { FisCfop } from '../../entities/FisCfop.entity';
import { FisDoc } from '../../entities/FisDoc.entity';
import { FisDocEvento } from '../../entities/FisDocEvento.entity';
import { FisDocTipo } from '../../entities/FisDocTipo.entity';
import { FisIbpt } from '../../entities/FisIbpt.entity';
import { FisNbs } from '../../entities/FisNbs.entity';
import { FisNcm } from '../../entities/FisNcm.entity';
import { FisObs } from '../../entities/FisObs.entity';
import { FisTributacao } from '../../entities/FisTributacao.entity';
import { FisTributo } from '../../entities/FisTributo.entity';
import { FisUnitParam } from '../../entities/FisUnitParam.entity';

@Module({
  imports: [
    TypeOrmModule.forFeature([
      FisCertificado,
      FisCest,
      FisCestNcm,
      FisCfop,
      FisDoc,
      FisDocEvento,
      FisDocTipo,
      FisIbpt,
      FisNbs,
      FisNcm,
      FisObs,
      FisTributacao,
      FisTributo,
      FisUnitParam,
    ]),
  ],
  providers: [],
  controllers: [],
  exports: [],
})
export class FisModule {}
