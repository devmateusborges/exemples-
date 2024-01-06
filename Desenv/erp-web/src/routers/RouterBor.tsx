import BorDispositivo from "../pages/modules/bor/BorDispositivo";
import BorDispositivoForm from "../pages/modules/bor/BorDispositivoForm";
import BorUnitParam from "../pages/modules/bor/BorUnitParam";
import BorUnitParamForm from "../pages/modules/bor/BorUnitParamForm";
import { ConstProgramUtil } from "../utils/ConstProgramUtil";

export default [
  {
    programId: ConstProgramUtil.cBordispositivoId,
    path: "bor/bordispositivo",
    element: <BorDispositivo />,
  },
  {
    programId: ConstProgramUtil.cBordispositivoId,
    path: "bor/bordispositivoform/:id",
    element: <BorDispositivoForm />,
  },
  {
    programId: ConstProgramUtil.cBorunitparamId,
    path: "bor/borunitparam",
    element: <BorUnitParam />,
  },
  {
    programId: ConstProgramUtil.cBorunitparamId,
    path: "bor/borunitparamform/:id",
    element: <BorUnitParamForm />,
  },
];
