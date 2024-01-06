import GerCidade from "../pages/modules/ger/GerCidade";
import GerCidadeForm from "../pages/modules/ger/GerCidadeForm";
import GerDevice from "../pages/modules/ger/GerDevice";
import GerDeviceForm from "../pages/modules/ger/GerDeviceForm";
import GerEmpresa from "../pages/modules/ger/GerEmpresa";
import GerEmpresaForm from "../pages/modules/ger/GerEmpresaForm";
import GerEmpresaGrupo from "../pages/modules/ger/GerEmpresaGrupo";
import GerEmpresaGrupoForm from "../pages/modules/ger/GerEmpresaGrupoForm";
import GerEstNivel from "../pages/modules/ger/GerEstNivel";
import GerEstNivelForm from "../pages/modules/ger/GerEstNivelForm";
import GerIndex from "../pages/modules/ger/GerIndex";
import GerIndexForm from "../pages/modules/ger/GerIndexForm";
import GerItemserv from "../pages/modules/ger/GerItemserv";
import GerItemservCompos from "../pages/modules/ger/GerItemservCompos";
import GerItemservComposForm from "../pages/modules/ger/GerItemservComposForm";
import GerItemservComposTipo from "../pages/modules/ger/GerItemservComposTipo";
import GerItemservComposTipoForm from "../pages/modules/ger/GerItemservComposTipoForm";
import GerItemservForm from "../pages/modules/ger/GerItemservForm";
import GerItemServGrupo from "../pages/modules/ger/GerItemServGrupo";
import GerItemServGrupoForm from "../pages/modules/ger/GerItemServGrupoForm";
import GerItemservVar from "../pages/modules/ger/GerItemservVar";
import GerItemservVarForm from "../pages/modules/ger/GerItemservVarForm";
import GerMarca from "../pages/modules/ger/GerMarca";
import GerMarcaForm from "../pages/modules/ger/GerMarcaForm";
import GerNumeracao from "../pages/modules/ger/GerNumeracao";
import GerNumeracaoForm from "../pages/modules/ger/GerNumeracaoForm";
import GerPais from "../pages/modules/ger/GerPais";
import GerPaisForm from "../pages/modules/ger/GerPaisForm";
import GerPessoa from "../pages/modules/ger/GerPessoa";
import GerPessoaForm from "../pages/modules/ger/GerPessoaForm";
import GerProcessoBloq from "../pages/modules/ger/GerProcessoBloq";
import GerProcessoBloqForm from "../pages/modules/ger/GerProcessoBloqForm";
import GerUmedida from "../pages/modules/ger/GerUmedida";
import GerUmedidaForm from "../pages/modules/ger/GerUmedidaForm";
import GerUnitParam from "../pages/modules/ger/GerUnitParam";
import GerUnitParamForm from "../pages/modules/ger/GerUnitParamForm";
import GerPerGerarForm from "../pages/modules/ger/GerPerGerarForm";
import { ConstProgramUtil } from "../utils/ConstProgramUtil";

export default [
  {
    programId: ConstProgramUtil.cGercidadeId,
    path: "ger/gercidade",
    element: <GerCidade />,
  },
  {
    programId: ConstProgramUtil.cGercidadeId,
    path: "ger/gercidadeform/:id",
    element: <GerCidadeForm />,
  },
  {
    programId: ConstProgramUtil.cGerdeviceId,
    path: "ger/gerdevice",
    element: <GerDevice />,
  },
  {
    programId: ConstProgramUtil.cGerdeviceId,
    path: "ger/gerdeviceform/:id",
    element: <GerDeviceForm />,
  },
  {
    programId: ConstProgramUtil.cGerempresaId,
    path: "ger/gerempresa",
    element: <GerEmpresa />,
  },
  {
    programId: ConstProgramUtil.cGerempresaId,
    path: "ger/gerempresaform/:id",
    element: <GerEmpresaForm />,
  },
  {
    programId: ConstProgramUtil.cGerempresagrupoId,
    path: "ger/gerempresagrupo",
    element: <GerEmpresaGrupo />,
  },
  {
    programId: ConstProgramUtil.cGerempresagrupoId,
    path: "ger/gerempresagrupoform/:id",
    element: <GerEmpresaGrupoForm />,
  },
  {
    programId: ConstProgramUtil.cGerestnivelId,
    path: "ger/gerestnivel",
    element: <GerEstNivel />,
  },
  {
    programId: ConstProgramUtil.cGerestnivelId,
    path: "ger/gerestnivelform/:id",
    element: <GerEstNivelForm />,
  },
  {
    programId: ConstProgramUtil.cGerindexId,
    path: "ger/gerindex",
    element: <GerIndex />,
  },
  {
    programId: ConstProgramUtil.cGerindexId,
    path: "ger/gerindexform/:id",
    element: <GerIndexForm />,
  },
  {
    programId: ConstProgramUtil.cGeritemservvarId,
    path: "ger/geritemservvar",
    element: <GerItemservVar />,
  },
  {
    programId: ConstProgramUtil.cGeritemservvarId,
    path: "ger/geritemservvarform/:id",
    element: <GerItemservVarForm />,
  },
  {
    programId: ConstProgramUtil.cGermarcaId,
    path: "ger/germarca",
    element: <GerMarca />,
  },
  {
    programId: ConstProgramUtil.cGermarcaId,
    path: "ger/germarcaform/:id",
    element: <GerMarcaForm />,
  },
  {
    programId: ConstProgramUtil.cGernumeracaoId,
    path: "ger/gernumeracao",
    element: <GerNumeracao />,
  },
  {
    programId: ConstProgramUtil.cGernumeracaoId,
    path: "ger/gernumeracaoform/:id",
    element: <GerNumeracaoForm />,
  },
  {
    programId: ConstProgramUtil.cGerpaisId,
    path: "ger/gerpais",
    element: <GerPais />,
  },
  {
    programId: ConstProgramUtil.cGerpaisId,
    path: "ger/gerpaisform/:id",
    element: <GerPaisForm />,
  },
  {
    programId: ConstProgramUtil.cGerpessoaId,
    path: "ger/gerpessoa",
    element: <GerPessoa />,
  },
  {
    programId: ConstProgramUtil.cGerpessoaId,
    path: "ger/gerpessoaform/:id",
    element: <GerPessoaForm />,
  },
  {
    programId: ConstProgramUtil.cGerprocessobloqId,
    path: "ger/gerprocessobloq",
    element: <GerProcessoBloq />,
  },
  {
    programId: ConstProgramUtil.cGerprocessobloqId,
    path: "ger/gerprocessobloqform/:id",
    element: <GerProcessoBloqForm />,
  },
  {
    programId: ConstProgramUtil.cGerumedidaId,
    path: "ger/gerumedida",
    element: <GerUmedida />,
  },
  {
    programId: ConstProgramUtil.cGerumedidaId,
    path: "ger/gerumedidaform/:id",
    element: <GerUmedidaForm />,
  },
  {
    programId: ConstProgramUtil.cGerunitparamId,
    path: "ger/gerunitparam",
    element: <GerUnitParam />,
  },
  {
    programId: ConstProgramUtil.cGerunitparamId,
    path: "ger/gerunitparamform/:id",
    element: <GerUnitParamForm />,
  },
  {
    programId: ConstProgramUtil.cGeritemservId,
    path: "ger/geritemserv",
    element: <GerItemserv />,
  },
  {
    programId: ConstProgramUtil.cGeritemservId,
    path: "ger/geritemservform/:id",
    element: <GerItemservForm />,
  },
  {
    programId: ConstProgramUtil.cGeritemservgrupoId,
    path: "ger/geritemservgrupo",
    element: <GerItemServGrupo />,
  },
  {
    programId: ConstProgramUtil.cGeritemservgrupoId,
    path: "ger/geritemservgrupoform/:id",
    element: <GerItemServGrupoForm />,
  },
  {
    programId: ConstProgramUtil.cGeritemservcompostipoId,
    path: "ger/geritemservcompostipo",
    element: <GerItemservComposTipo />,
  },
  {
    programId: ConstProgramUtil.cGeritemservcompostipoId,
    path: "ger/geritemservcompostipoform/:id",
    element: <GerItemservComposTipoForm />,
  },
  {
    programId: ConstProgramUtil.cGeritemservcomposId,
    path: "ger/geritemservcompos",
    element: <GerItemservCompos />,
  },
  {
    programId: ConstProgramUtil.cGeritemservcomposId,
    path: "ger/geritemservcomposform/:id",
    element: <GerItemservComposForm />,
  },
  {
    programId: ConstProgramUtil.cGerpergerarId,
    path: "ger/gerpergerar",
    element: <GerPerGerarForm />,
  },
];
