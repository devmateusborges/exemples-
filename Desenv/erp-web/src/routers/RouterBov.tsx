import BovUnitParam from "../pages/modules/bov/BovUnitParam";
import BovUnitParamForm from "../pages/modules/bov/BovUnitParamForm";
import { ConstProgramUtil } from "../utils/ConstProgramUtil";

export default [
  {
    programId: ConstProgramUtil.cBovunitparamId,
    path: "bov/bovunitparam",
    element: <BovUnitParam />,
  },
  {
    programId: ConstProgramUtil.cBovunitparamId,
    path: "bov/bovunitparamform/:id",
    element: <BovUnitParamForm />,
  },
];
