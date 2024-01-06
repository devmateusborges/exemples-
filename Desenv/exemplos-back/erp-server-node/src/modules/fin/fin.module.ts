import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { FinBanco } from '../../entities/FinBanco.entity';
import { FinClass } from '../../entities/FinClass.entity';
import { FinClassAgrup } from '../../entities/FinClassAgrup.entity';
import { FinClassAgrupGrupo } from '../../entities/FinClassAgrupGrupo.entity';
import { FinClassGrupo } from '../../entities/FinClassGrupo.entity';
import { FinCondPagrec } from '../../entities/FinCondPagrec.entity';
import { FinCondPagrecConfig } from '../../entities/FinCondPagrecConfig.entity';
import { FinConta } from '../../entities/FinConta.entity';
import { FinDocTipo } from '../../entities/FinDocTipo.entity';
import { FinLote } from '../../entities/FinLote.entity';
import { FinPagrec } from '../../entities/FinPagrec.entity';
import { FinPagrecBaixa } from '../../entities/FinPagrecBaixa.entity';
import { FinPagrecBaixaVar } from '../../entities/FinPagrecBaixaVar.entity';
import { FinPagrecBanco } from '../../entities/FinPagrecBanco.entity';
import { FinPagrecBancoExtrato } from '../../entities/FinPagrecBancoExtrato.entity';
import { FinPagrecBancoTransf } from '../../entities/FinPagrecBancoTransf.entity';
import { FinPagrecClass } from '../../entities/FinPagrecClass.entity';
import { FinPagrecOrigem } from '../../entities/FinPagrecOrigem.entity';
import { FinPagrecParc } from '../../entities/FinPagrecParc.entity';
import { FinPagrecParcVar } from '../../entities/FinPagrecParcVar.entity';
import { FinPagrecPrev } from '../../entities/FinPagrecPrev.entity';
import { FinPagrecPrevDest } from '../../entities/FinPagrecPrevDest.entity';
import { FinPagrecPrevVar } from '../../entities/FinPagrecPrevVar.entity';
import { FinPagrecTipo } from '../../entities/FinPagrecTipo.entity';
import { FinPagrecVersao } from '../../entities/FinPagrecVersao.entity';
import { FinRecibo } from '../../entities/FinRecibo.entity';
import { FinReciboTipo } from '../../entities/FinReciboTipo.entity';
import { FinTipoVariacao } from '../../entities/FinTipoVariacao.entity';
import { FinUnitParam } from '../../entities/FinUnitParam.entity';

@Module({
  imports: [
    TypeOrmModule.forFeature([
      FinBanco,
      FinClass,
      FinClassAgrup,
      FinClassAgrupGrupo,
      FinClassGrupo,
      FinCondPagrec,
      FinCondPagrecConfig,
      FinConta,
      FinDocTipo,
      FinLote,
      FinPagrec,
      FinPagrecBaixa,
      FinPagrecBaixaVar,
      FinPagrecBanco,
      FinPagrecBancoExtrato,
      FinPagrecBancoTransf,
      FinPagrecClass,
      FinPagrecOrigem,
      FinPagrecParc,
      FinPagrecParcVar,
      FinPagrecPrev,
      FinPagrecPrevDest,
      FinPagrecPrevVar,
      FinPagrecTipo,
      FinPagrecVersao,
      FinRecibo,
      FinReciboTipo,
      FinTipoVariacao,
      FinUnitParam,
    ]),
  ],
  providers: [],
  controllers: [],
  exports: [],
})
export class FinModule {}
