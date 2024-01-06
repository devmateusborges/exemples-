import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Mov } from '../../entities/Mov.entity';
import { MovLacre } from '../../entities/MovLacre.entity';
import { MovMedida } from '../../entities/MovMedida.entity';
import { MovCiot } from '../../entities/MovCiot.entity';
import { MovComp } from '../../entities/MovComp.entity';
import { MovCondutor } from '../../entities/MovCondutor.entity';
import { MovCotacao } from '../../entities/MovCotacao.entity';
import { MovCotacaoAnal } from '../../entities/MovCotacaoAnal.entity';
import { MovEntrega } from '../../entities/MovEntrega.entity';
import { MovEntregaDoc } from '../../entities/MovEntregaDoc.entity';
import { MovEstNivel } from '../../entities/MovEstNivel.entity';
import { MovFrete } from '../../entities/MovFrete.entity';
import { MovItemserv } from '../../entities/MovItemserv.entity';
import { MovOperacao } from '../../entities/MovOperacao.entity';
import { MovUnitParam } from '../../entities/MovUnitParam.entity';
import { MovTomador } from '../../entities/MovTomador.entity';
import { MovTipo } from '../../entities/MovTipo.entity';
import { MovStatus } from '../../entities/MovStatus.entity';
import { MovSeguradora } from '../../entities/MovSeguradora.entity';
import { MovReboque } from '../../entities/MovReboque.entity';
import { MovPercurso } from '../../entities/MovPercurso.entity';
import { MovPedagio } from '../../entities/MovPedagio.entity';
import { MovOrigem } from '../../entities/MovOrigem.entity';
import { MovOperacaoStatus } from '../../entities/MovOperacaoStatus.entity';

@Module({
  imports: [
    TypeOrmModule.forFeature([
      Mov,
      MovCiot,
      MovComp,
      MovCondutor,
      MovCotacao,
      MovCotacaoAnal,
      MovEntrega,
      MovEntregaDoc,
      MovEstNivel,
      MovFrete,
      MovItemserv,
      MovLacre,
      MovMedida,
      MovOperacao,
      MovOperacaoStatus,
      MovOrigem,
      MovPedagio,
      MovPercurso,
      MovReboque,
      MovSeguradora,
      MovStatus,
      MovTipo,
      MovTomador,
      MovUnitParam,
    ]),
  ],
  providers: [],
  controllers: [],
  exports: [],
})
export class MovModule {}
