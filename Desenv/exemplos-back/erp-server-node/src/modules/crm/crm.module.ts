import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { CrmAviso } from '../../entities/CrmAviso.entity';
import { CrmAvisoOrg } from '../../entities/CrmAvisoOrg.entity';
import { CrmChatGrupo } from '../../entities/CrmChatGrupo.entity';
import { CrmChatMsg } from '../../entities/CrmChatMsg.entity';
import { CrmClass } from '../../entities/CrmClass.entity';
import { CrmClassGrupo } from '../../entities/CrmClassGrupo.entity';
import { CrmClassSubgrupo } from '../../entities/CrmClassSubgrupo.entity';
import { CrmEtapa } from '../../entities/CrmEtapa.entity';
import { CrmEtapaProx } from '../../entities/CrmEtapaProx.entity';
import { CrmMov } from '../../entities/CrmMov.entity';
import { CrmMovAnexo } from '../../entities/CrmMovAnexo.entity';
import { CrmMovHist } from '../../entities/CrmMovHist.entity';
import { CrmMovTag } from '../../entities/CrmMovTag.entity';
import { CrmOrg } from '../../entities/CrmOrg.entity';
import { CrmPrioridade } from '../../entities/CrmPrioridade.entity';
import { CrmResposta } from '../../entities/CrmResposta.entity';
import { CrmStatus } from '../../entities/CrmStatus.entity';
import { CrmStatusProx } from '../../entities/CrmStatusProx.entity';
import { CrmTag } from '../../entities/CrmTag.entity';
import { CrmUnitParam } from '../../entities/CrmUnitParam.entity';

@Module({
  imports: [
    TypeOrmModule.forFeature([
      CrmAviso,
      CrmAvisoOrg,
      CrmChatGrupo,
      CrmChatMsg,
      CrmClass,
      CrmClassGrupo,
      CrmClassSubgrupo,
      CrmEtapa,
      CrmEtapaProx,
      CrmMov,
      CrmMovAnexo,
      CrmMovHist,
      CrmMovTag,
      CrmOrg,
      CrmPrioridade,
      CrmResposta,
      CrmStatus,
      CrmStatusProx,
      CrmTag,
      CrmUnitParam,
    ]),
  ],
  providers: [],
  controllers: [],
  exports: [],
})
export class CrmModule {}
