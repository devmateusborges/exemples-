import PtoMedidor from "../pages/modules/pto/PtoMedidor";
import PtoMedidorForm from "../pages/modules/pto/PtoMedidorForm";
import PtoUnitParam from "../pages/modules/pto/PtoUnitParam";
import PtoUnitParamForm from "../pages/modules/pto/PtoUnitParamForm";
import { ConstProgramUtil } from "../utils/ConstProgramUtil";

export default [
  {
    programId: ConstProgramUtil.cPtomedidorId,
    path: "pto/ptomedidor",
    element: <PtoMedidor />,
  },
  {
    programId: ConstProgramUtil.cPtomedidorId,
    path: "pto/ptomedidorform/:id",
    element: <PtoMedidorForm />,
  },
  {
    programId: ConstProgramUtil.cPtounitparamId,
    path: "pto/ptounitparam",
    element: <PtoUnitParam />,
  },
  {
    programId: ConstProgramUtil.cPtounitparamId,
    path: "pto/ptounitparamform/:id",
    element: <PtoUnitParamForm />,
  },
];
