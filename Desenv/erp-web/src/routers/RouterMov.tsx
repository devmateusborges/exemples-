import MovOperacao from "../pages/modules/mov/MovOperacao";
import MovOperacaoForm from "../pages/modules/mov/MovOperacaoForm";
import MovStatus from "../pages/modules/mov/MovStatus";
import MovStatusForm from "../pages/modules/mov/MovStatusForm";
import MovTipo from "../pages/modules/mov/MovTipo";
import MovTipoForm from "../pages/modules/mov/MovTipoForm";
import MovUnitParam from "../pages/modules/mov/MovUnitParam";
import MovUnitParamForm from "../pages/modules/mov/MovUnitParamForm";
import { ConstProgramUtil } from "../utils/ConstProgramUtil";

export default [
  {
    programId: ConstProgramUtil.cMovoperacaoId,
    path: "mov/movoperacaoform/:id",
    element: <MovOperacaoForm />,
  },
  {
    programId: ConstProgramUtil.cMovoperacaoId,
    path: "mov/movoperacao",
    element: <MovOperacao />,
  },
  {
    programId: ConstProgramUtil.cMovstatusId,
    path: "mov/movstatus",
    element: <MovStatus />,
  },
  {
    programId: ConstProgramUtil.cMovstatusId,
    path: "mov/movstatusform/:id",
    element: <MovStatusForm />,
  },
  {
    programId: ConstProgramUtil.cMovtipoId,
    path: "mov/movtipo",
    element: <MovTipo />,
  },
  {
    programId: ConstProgramUtil.cMovtipoId,
    path: "mov/movtipoform/:id",
    element: <MovTipoForm />,
  },
  {
    programId: ConstProgramUtil.cMovunitparamId,
    path: "mov/movunitparam",
    element: <MovUnitParam />,
  },
  {
    programId: ConstProgramUtil.cMovunitparamId,
    path: "mov/movunitparamform/:id",
    element: <MovUnitParamForm />,
  },
];
