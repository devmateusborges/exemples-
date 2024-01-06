import FinBanco from "../pages/modules/fin/FinBanco";
import FinBancoForm from "../pages/modules/fin/FinBancoForm";
import FinClass from "../pages/modules/fin/FinClass";
import FinClassAgrup from "../pages/modules/fin/FinClassAgrup";
import FinClassAgrupForm from "../pages/modules/fin/FinClassAgrupForm";
import FinClassForm from "../pages/modules/fin/FinClassForm";
import FinClassGrupo from "../pages/modules/fin/FinClassGrupo";
import FinClassGrupoForm from "../pages/modules/fin/FinClassGrupoForm";
import FinCondPagrec from "../pages/modules/fin/FinCondPagrec";
import FinCondPagrecForm from "../pages/modules/fin/FinCondPagrecForm";
import FinConta from "../pages/modules/fin/FinConta";
import FinContaForm from "../pages/modules/fin/FinContaForm";
import FinDocTipo from "../pages/modules/fin/FinDocTipo";
import FinDocTipoForm from "../pages/modules/fin/FinDocTipoForm";
import FinLote from "../pages/modules/fin/FinLote";
import FinLoteForm from "../pages/modules/fin/FinLoteForm";
import FinPagrecVersao from "../pages/modules/fin/FinPagrecVersao";
import FinPagrecVersaoForm from "../pages/modules/fin/FinPagrecVersaoForm";
import FinRecibo from "../pages/modules/fin/FinRecibo";
import FinReciboForm from "../pages/modules/fin/FinReciboForm";
import FinReciboTipo from "../pages/modules/fin/FinReciboTipo";
import FinReciboTipoForm from "../pages/modules/fin/FinReciboTipoForm";
import FinTipoVariacao from "../pages/modules/fin/FinTipoVariacao";
import FinTipoVariacaoForm from "../pages/modules/fin/FinTipoVariacaoForm";
import FinUnitParam from "../pages/modules/fin/FinUnitParam";
import FinUnitParamForm from "../pages/modules/fin/FinUnitParamForm";
import { ConstProgramUtil } from "../utils/ConstProgramUtil";

export default [
  {
    programId: ConstProgramUtil.cFinbancoId,
    path: "fin/finbanco",
    element: <FinBanco />,
  },
  {
    programId: ConstProgramUtil.cFinbancoId,
    path: "fin/finbancoform/:id",
    element: <FinBancoForm />,
  },
  {
    programId: ConstProgramUtil.cFinclassId,
    path: "fin/finclass",
    element: <FinClass />,
  },
  {
    programId: ConstProgramUtil.cFinclassId,
    path: "fin/finclassform/:id",
    element: <FinClassForm />,
  },
  {
    programId: ConstProgramUtil.cFinclassagrupId,
    path: "fin/finclassagrup",
    element: <FinClassAgrup />,
  },
  {
    programId: ConstProgramUtil.cFinclassagrupId,
    path: "fin/finclassagrupform/:id",
    element: <FinClassAgrupForm />,
  },
  {
    programId: ConstProgramUtil.cFinclassgrupoId,
    path: "fin/finclassgrupo",
    element: <FinClassGrupo />,
  },
  {
    programId: ConstProgramUtil.cFinclassgrupoId,
    path: "fin/finclassgrupoform/:id",
    element: <FinClassGrupoForm />,
  },
  {
    programId: ConstProgramUtil.cFincondpagrecId,
    path: "fin/fincondpagrec",
    element: <FinCondPagrec />,
  },
  {
    programId: ConstProgramUtil.cFincondpagrecId,
    path: "fin/fincondpagrecform/:id",
    element: <FinCondPagrecForm />,
  },
  {
    programId: ConstProgramUtil.cFincontaId,
    path: "fin/finconta",
    element: <FinConta />,
  },
  {
    programId: ConstProgramUtil.cFincontaId,
    path: "fin/fincontaform/:id",
    element: <FinContaForm />,
  },
  {
    programId: ConstProgramUtil.cFindoctipoId,
    path: "fin/findoctipo",
    element: <FinDocTipo />,
  },
  {
    programId: ConstProgramUtil.cFindoctipoId,
    path: "fin/findoctipoform/:id",
    element: <FinDocTipoForm />,
  },
  {
    programId: ConstProgramUtil.cFinloteId,
    path: "fin/finlote",
    element: <FinLote />,
  },
  {
    programId: ConstProgramUtil.cFinloteId,
    path: "fin/finloteform/:id",
    element: <FinLoteForm />,
  },
  {
    programId: ConstProgramUtil.cFinpagrecversaoId,
    path: "fin/finpagrecversao",
    element: <FinPagrecVersao />,
  },
  {
    programId: ConstProgramUtil.cFinpagrecversaoId,
    path: "fin/finpagrecversaoform/:id",
    element: <FinPagrecVersaoForm />,
  },
  {
    programId: ConstProgramUtil.cFinrecibotipoId,
    path: "fin/finrecibotipo",
    element: <FinReciboTipo />,
  },
  {
    programId: ConstProgramUtil.cFinrecibotipoId,
    path: "fin/finrecibotipoform/:id",
    element: <FinReciboTipoForm />,
  },
  {
    programId: ConstProgramUtil.cFintipovariacaoId,
    path: "fin/fintipovariacao",
    element: <FinTipoVariacao />,
  },
  {
    programId: ConstProgramUtil.cFintipovariacaoId,
    path: "fin/fintipovariacaoform/:id",
    element: <FinTipoVariacaoForm />,
  },
  {
    programId: ConstProgramUtil.cFinunitparamId,
    path: "fin/finunitparam",
    element: <FinUnitParam />,
  },
  {
    programId: ConstProgramUtil.cFinunitparamId,
    path: "fin/finunitparamform/:id",
    element: <FinUnitParamForm />,
  },
  {
    programId: ConstProgramUtil.cFinreciboId,
    path: "fin/finrecibo",
    element: <FinRecibo />,
  },
  {
    programId: ConstProgramUtil.cFinreciboId,
    path: "fin/finreciboform/:id",
    element: <FinReciboForm />,
  },
];
