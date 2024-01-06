import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { OpeAtividade } from '../../entities/OpeAtividade.entity';
import { OpeAtividadeGrupo } from '../../entities/OpeAtividadeGrupo.entity';
import { OpeAtividadeRelacProd } from '../../entities/OpeAtividadeRelacProd.entity';
import { OpeAtividadeSistema } from '../../entities/OpeAtividadeSistema.entity';
import { OpeCentro1 } from '../../entities/OpeCentro1.entity';
import { OpeCentro2 } from '../../entities/OpeCentro2.entity';
import { OpeCentro2Area } from '../../entities/OpeCentro2Area.entity';
import { OpeCentro2Equip } from '../../entities/OpeCentro2Equip.entity';
import { OpeCentro2Estoque } from '../../entities/OpeCentro2Estoque.entity';
import { OpeCentro2MapaCoord } from '../../entities/OpeCentro2MapaCoord.entity';
import { OpeCentro2MapaGeometria } from '../../entities/OpeCentro2MapaGeometria.entity';
import { OpeCentro2MovMedia } from '../../entities/OpeCentro2MovMedia.entity';
import { OpeCentro2Ord } from '../../entities/OpeCentro2Ord.entity';
import { OpeCentro2OrdAtiv } from '../../entities/OpeCentro2OrdAtiv.entity';
import { OpeCentro2OrdDest } from '../../entities/OpeCentro2OrdDest.entity';
import { OpeCentro2OrdItemserv } from '../../entities/OpeCentro2OrdItemserv.entity';
import { OpeCentro2OrdRec } from '../../entities/OpeCentro2OrdRec.entity';
import { OpeCentro2OrdStatus } from '../../entities/OpeCentro2OrdStatus.entity';
import { OpeCentro2OrdTipo } from '../../entities/OpeCentro2OrdTipo.entity';
import { OpeCentro2ParamPer } from '../../entities/OpeCentro2ParamPer.entity';
import { OpeCentro2Pessoa } from '../../entities/OpeCentro2Pessoa.entity';
import { OpeCentroConfig } from '../../entities/OpeCentroConfig.entity';
import { OpeCentroDest } from '../../entities/OpeCentroDest.entity';
import { OpeCentroGrupo } from '../../entities/OpeCentroGrupo.entity';
import { OpeCentroPrev } from '../../entities/OpeCentroPrev.entity';
import { OpeCentroPrevDest } from '../../entities/OpeCentroPrevDest.entity';
import { OpeCentroRatFator } from '../../entities/OpeCentroRatFator.entity';
import { OpeCentroRatPeriodo } from '../../entities/OpeCentroRatPeriodo.entity';
import { OpeCentroRatTipo } from '../../entities/OpeCentroRatTipo.entity';
import { OpeCentroRend } from '../../entities/OpeCentroRend.entity';
import { OpeCentroRendFator } from '../../entities/OpeCentroRendFator.entity';
import { OpeCentroSubgrupo } from '../../entities/OpeCentroSubgrupo.entity';
import { OpeCentroSubtipo } from '../../entities/OpeCentroSubtipo.entity';
import { OpeCentroTipo } from '../../entities/OpeCentroTipo.entity';
import { OpeCentroVersao } from '../../entities/OpeCentroVersao.entity';
import { OpeCicloVar } from '../../entities/OpeCicloVar.entity';
import { OpeCompart } from '../../entities/OpeCompart.entity';
import { OpeCompartGrupo } from '../../entities/OpeCompartGrupo.entity';
import { OpeCompartItemserv } from '../../entities/OpeCompartItemserv.entity';
import { OpeCompartMedida } from '../../entities/OpeCompartMedida.entity';
import { OpeCompartOcor } from '../../entities/OpeCompartOcor.entity';
import { OpeCompartPosicao } from '../../entities/OpeCompartPosicao.entity';
import { OpeCompartStatus } from '../../entities/OpeCompartStatus.entity';
import { OpeCompartSubgrupo } from '../../entities/OpeCompartSubgrupo.entity';
import { OpeCompartTipo } from '../../entities/OpeCompartTipo.entity';
import { OpeEspac } from '../../entities/OpeEspac.entity';
import { OpeEstagio } from '../../entities/OpeEstagio.entity';
import { OpeFrenteTrabalho } from '../../entities/OpeFrenteTrabalho.entity';
import { OpeOcor } from '../../entities/OpeOcor.entity';
import { OpeOcorCompartMov } from '../../entities/OpeOcorCompartMov.entity';
import { OpeOcorCompartMovDet } from '../../entities/OpeOcorCompartMovDet.entity';
import { OpeOcorGrupo } from '../../entities/OpeOcorGrupo.entity';
import { OpeOcorMov } from '../../entities/OpeOcorMov.entity';
import { OpeOcorMovDest } from '../../entities/OpeOcorMovDest.entity';
import { OpeOcorMovDet } from '../../entities/OpeOcorMovDet.entity';
import { OpeOcorPrev } from '../../entities/OpeOcorPrev.entity';
import { OpeOcorStatus } from '../../entities/OpeOcorStatus.entity';
import { OpeOcorTipo } from '../../entities/OpeOcorTipo.entity';
import { OpePeriodo } from '../../entities/OpePeriodo.entity';
import { OpeRegiao } from '../../entities/OpeRegiao.entity';
import { OpeTipoSolo } from '../../entities/OpeTipoSolo.entity';
import { OpeUnitParam } from '../../entities/OpeUnitParam.entity';

@Module({
  imports: [
    TypeOrmModule.forFeature([
      OpeAtividade,
      OpeAtividadeGrupo,
      OpeAtividadeRelacProd,
      OpeAtividadeSistema,
      OpeCentro1,
      OpeCentro2,
      OpeCentro2Area,
      OpeCentro2Equip,
      OpeCentro2Estoque,
      OpeCentro2MapaCoord,
      OpeCentro2MapaGeometria,
      OpeCentro2MovMedia,
      OpeCentro2Ord,
      OpeCentro2OrdAtiv,
      OpeCentro2OrdDest,
      OpeCentro2OrdItemserv,
      OpeCentro2OrdRec,
      OpeCentro2OrdStatus,
      OpeCentro2OrdTipo,
      OpeCentro2ParamPer,
      OpeCentro2Pessoa,
      OpeCentroConfig,
      OpeCentroDest,
      OpeCentroGrupo,
      OpeCentroPrev,
      OpeCentroPrevDest,
      OpeCentroRatFator,
      OpeCentroRatPeriodo,
      OpeCentroRatTipo,
      OpeCentroRend,
      OpeCentroRendFator,
      OpeCentroSubgrupo,
      OpeCentroSubtipo,
      OpeCentroTipo,
      OpeCentroVersao,
      OpeCicloVar,
      OpeCompart,
      OpeCompartGrupo,
      OpeCompartItemserv,
      OpeCompartMedida,
      OpeCompartOcor,
      OpeCompartPosicao,
      OpeCompartStatus,
      OpeCompartSubgrupo,
      OpeCompartTipo,
      OpeEspac,
      OpeEstagio,
      OpeFrenteTrabalho,
      OpeOcor,
      OpeOcorCompartMov,
      OpeOcorCompartMovDet,
      OpeOcorGrupo,
      OpeOcorMov,
      OpeOcorMovDest,
      OpeOcorMovDet,
      OpeOcorPrev,
      OpeOcorStatus,
      OpeOcorTipo,
      OpePeriodo,
      OpeRegiao,
      OpeTipoSolo,
      OpeUnitParam,
    ]),
  ],
  providers: [],
  controllers: [],
  exports: [],
})
export class OpeModule {}
