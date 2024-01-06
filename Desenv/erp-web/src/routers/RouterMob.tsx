import MobUnitParam from "../pages/modules/mob/MobUnitParam";
import MobUnitParamForm from "../pages/modules/mob/MobUnitParamForm";
import { ConstProgramUtil } from "../utils/ConstProgramUtil";

export default [
  {
    programId: ConstProgramUtil.cMobunitparamId,
    path: "mob/mobunitparam",
    element: <MobUnitParam />,
  },
  {
    programId: ConstProgramUtil.cMobunitparamId,
    path: "mob/mobunitparamform/:id",
    element: <MobUnitParamForm />,
  },
];
