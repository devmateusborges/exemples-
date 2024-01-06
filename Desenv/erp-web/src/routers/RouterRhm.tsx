import RhmUnitParam from "../pages/modules/rhm/RhmUnitParam";
import RhmUnitParamForm from "../pages/modules/rhm/RhmUnitParamForm";
import { ConstProgramUtil } from "../utils/ConstProgramUtil";

export default [
  {
    programId: ConstProgramUtil.cRhmunitparamId,
    path: "rhm/rhmunitparam",
    element: <RhmUnitParam />,
  },
  {
    programId: ConstProgramUtil.cRhmunitparamId,
    path: "rhm/rhmunitparamform/:id",
    element: <RhmUnitParamForm />,
  },
];
