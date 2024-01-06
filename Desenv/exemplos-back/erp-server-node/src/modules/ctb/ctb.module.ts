import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { CtbCentro } from '../../entities/CtbCentro.entity';
import { CtbCentroGrupo } from '../../entities/CtbCentroGrupo.entity';
import { CtbComp } from '../../entities/CtbComp.entity';
import { CtbCompGrupo } from '../../entities/CtbCompGrupo.entity';
import { CtbConta } from '../../entities/CtbConta.entity';
import { CtbContaGrupo } from '../../entities/CtbContaGrupo.entity';
import { CtbContaVersao } from '../../entities/CtbContaVersao.entity';
import { CtbHistorico } from '../../entities/CtbHistorico.entity';
import { CtbLanc } from '../../entities/CtbLanc.entity';
import { CtbLancDet } from '../../entities/CtbLancDet.entity';
import { CtbLote } from '../../entities/CtbLote.entity';
import { CtbTipoSaldo } from '../../entities/CtbTipoSaldo.entity';
import { CtbUnitParam } from '../../entities/CtbUnitParam.entity';
import { CtbVersao } from '../../entities/CtbVersao.entity';

@Module({
  imports: [
    TypeOrmModule.forFeature([
      CtbCentro,
      CtbCentroGrupo,
      CtbComp,
      CtbCompGrupo,
      CtbConta,
      CtbContaGrupo,
      CtbContaVersao,
      CtbHistorico,
      CtbLanc,
      CtbLancDet,
      CtbLote,
      CtbTipoSaldo,
      CtbUnitParam,
      CtbVersao,
    ]),
  ],
  providers: [],
  controllers: [],
  exports: [],
})
export class CtbModule {}
