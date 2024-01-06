import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { GerCidade } from '../../entities/GerCidade.entity';
import { GerDevice } from '../../entities/GerDevice.entity';
import { GerDeviceParam } from '../../entities/GerDeviceParam.entity';
import { GerEmpresa } from '../../entities/GerEmpresa.entity';
import { GerEmpresaGrupo } from '../../entities/GerEmpresaGrupo.entity';
import { GerEmpresaPessoa } from '../../entities/GerEmpresaPessoa.entity';
import { GerEstNivel } from '../../entities/GerEstNivel.entity';
import { GerIndex } from '../../entities/GerIndex.entity';
import { GerIndexMov } from '../../entities/GerIndexMov.entity';
import { GerItemserv } from '../../entities/GerItemserv.entity';
import { GerItemservBarra } from '../../entities/GerItemservBarra.entity';
import { GerItemservCompos } from '../../entities/GerItemservCompos.entity';
import { GerItemservComposTipo } from '../../entities/GerItemservComposTipo.entity';
import { GerItemservGrupo } from '../../entities/GerItemservGrupo.entity';
import { GerItemservLocal } from '../../entities/GerItemservLocal.entity';
import { GerItemservLote } from '../../entities/GerItemservLote.entity';
import { GerItemservPessoa } from '../../entities/GerItemservPessoa.entity';
import { GerItemservSubgrupo } from '../../entities/GerItemservSubgrupo.entity';
import { GerItemservVar } from '../../entities/GerItemservVar.entity';
import { GerMarca } from '../../entities/GerMarca.entity';
import { GerMarcaModelo } from '../../entities/GerMarcaModelo.entity';
import { GerMarcaPessoa } from '../../entities/GerMarcaPessoa.entity';
import { GerNumeracao } from '../../entities/GerNumeracao.entity';
import { GerPais } from '../../entities/GerPais.entity';
import { GerPer } from '../../entities/GerPer.entity';
import { GerPessoa } from '../../entities/GerPessoa.entity';
import { GerPessoaContaBanco } from '../../entities/GerPessoaContaBanco.entity';
import { GerPessoaEndereco } from '../../entities/GerPessoaEndereco.entity';
import { GerProcessoBloq } from '../../entities/GerProcessoBloq.entity';
import { GerProcessoBloqUser } from '../../entities/GerProcessoBloqUser.entity';
import { GerUf } from '../../entities/GerUf.entity';
import { GerUmedida } from '../../entities/GerUmedida.entity';
import { GerUmedidaConv } from '../../entities/GerUmedidaConv.entity';
import { GerUnitParam } from '../../entities/GerUnitParam.entity';

@Module({
  imports: [
    TypeOrmModule.forFeature([
      GerCidade,
      GerDevice,
      GerDeviceParam,
      GerEmpresa,
      GerEmpresaGrupo,
      GerEmpresaPessoa,
      GerEstNivel,
      GerIndex,
      GerIndexMov,
      GerItemserv,
      GerItemservBarra,
      GerItemservCompos,
      GerItemservComposTipo,
      GerItemservGrupo,
      GerItemservLocal,
      GerItemservLote,
      GerItemservPessoa,
      GerItemservSubgrupo,
      GerItemservVar,
      GerMarca,
      GerMarcaModelo,
      GerMarcaPessoa,
      GerNumeracao,
      GerPais,
      GerPer,
      GerPessoa,
      GerPessoaContaBanco,
      GerPessoaEndereco,
      GerProcessoBloq,
      GerProcessoBloqUser,
      GerUf,
      GerUmedida,
      GerUmedidaConv,
      GerUnitParam,
    ]),
  ],
  providers: [],
  controllers: [],
  exports: [],
})
export class GerModule {}
