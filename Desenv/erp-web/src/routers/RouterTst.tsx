import Test1 from "../pages/modules/tst/Test1";
import Test1Form from "../pages/modules/tst/Test1Form";
import { ConstProgramUtil } from "../utils/ConstProgramUtil";

export default [
  {
    programId: ConstProgramUtil.cTstTest1Id,
    path: "tst/test1",
    element: <Test1 />,
  },
  {
    programId: ConstProgramUtil.cTstTest1Id,
    path: "tst/test1form/:id",
    element: <Test1Form />,
  },
];
