import SysDocumentCategory from "../pages/modules/sys/SysDocumentCategory";
import SysDocumentCategoryForm from "../pages/modules/sys/SysDocumentCategoryForm";
import SysGroup from "../pages/modules/sys/SysGroup";
import SysGroupForm from "../pages/modules/sys/SysGroupForm";
import SysGroupProgramFeature from "../pages/modules/sys/SysGroupProgramFeature";
import SysGroupProgramFeatureForm from "../pages/modules/sys/SysGroupProgramFeatureForm";
import SysLicence from "../pages/modules/sys/SysLicence";
import SysLicenceForm from "../pages/modules/sys/SysLicenceForm";
import SysModule from "../pages/modules/sys/SysModule";
import SysModuleForm from "../pages/modules/sys/SysModuleForm";
import SysPlan from "../pages/modules/sys/SysPlan";
import SysPlanForm from "../pages/modules/sys/SysPlanForm";
import SysProgram from "../pages/modules/sys/SysProgram";
import SysProgramForm from "../pages/modules/sys/SysProgramForm";
import RedefinePasswordPage from "../pages/modules/sys/SysRedefinePasswordPage";
import SysRestriction from "../pages/modules/sys/SysRestriction";
import SysRestrictionForm from "../pages/modules/sys/SysRestrictionForm";
import SysUnit from "../pages/modules/sys/SysUnit";
import SysUnitForm from "../pages/modules/sys/SysUnitForm";
import SysUnitParam from "../pages/modules/sys/SysUnitParam";
import SysUnitParamForm from "../pages/modules/sys/SysUnitParamForm";
import SysUser from "../pages/modules/sys/SysUser";
import SysUserForm from "../pages/modules/sys/SysUserForm";

import { ConstProgramUtil } from "../utils/ConstProgramUtil";

export default [
  {
    programId: ConstProgramUtil.cSysgroupId,
    path: "sys/sysgroup",
    element: <SysGroup />,
  },
  {
    programId: ConstProgramUtil.cSysgroupId,
    path: "sys/sysgroupform/:id",
    element: <SysGroupForm />,
  },
  {
    programId: ConstProgramUtil.cSyslicenceId,
    path: "sys/syslicence",
    element: <SysLicence />,
  },
  {
    programId: ConstProgramUtil.cSyslicenceId,
    path: "sys/syslicenceform/:id",
    element: <SysLicenceForm />,
  },
  {
    programId: ConstProgramUtil.cSysmoduleId,
    path: "sys/sysmodule",
    element: <SysModule />,
  },
  {
    programId: ConstProgramUtil.cSysmoduleId,
    path: "sys/sysmoduleform/:id",
    element: <SysModuleForm />,
  },
  {
    programId: ConstProgramUtil.cSysplanId,
    path: "sys/sysplan",
    element: <SysPlan />,
  },
  {
    programId: ConstProgramUtil.cSysplanId,
    path: "sys/sysplanform/:id",
    element: <SysPlanForm />,
  },
  {
    programId: ConstProgramUtil.cSysprogramId,
    path: "sys/sysprogram",
    element: <SysProgram />,
  },
  {
    programId: ConstProgramUtil.cSysprogramId,
    path: "sys/sysprogramform/:id",
    element: <SysProgramForm />,
  },
  {
    programId: ConstProgramUtil.cSysrestrictionId,
    path: "sys/sysrestriction",
    element: <SysRestriction />,
  },
  {
    programId: ConstProgramUtil.cSysrestrictionId,
    path: "sys/sysrestrictionform/:id",
    element: <SysRestrictionForm />,
  },
  {
    programId: ConstProgramUtil.cSysunitId,
    path: "sys/sysunit",
    element: <SysUnit />,
  },
  {
    programId: ConstProgramUtil.cSysunitId,
    path: "sys/sysunitform/:id",
    element: <SysUnitForm />,
  },
  {
    programId: ConstProgramUtil.cSysunitparamId,
    path: "sys/sysunitparam",
    element: <SysUnitParam />,
  },
  {
    programId: ConstProgramUtil.cSysunitparamId,
    path: "sys/sysunitparamform/:id",
    element: <SysUnitParamForm />,
  },
  {
    programId: ConstProgramUtil.cSysuserId,
    path: "sys/sysuser",
    element: <SysUser />,
  },
  {
    programId: ConstProgramUtil.cSysuserId,
    path: "sys/sysuserform/:id",
    element: <SysUserForm />,
  },
  {
    programId: ConstProgramUtil.cSysDocumentCategoryID,
    path: "sys/sysdocumentcategory",
    element: <SysDocumentCategory />,
  },
  {
    programId: ConstProgramUtil.cSysDocumentCategoryID,
    path: "sys/sysdocumentcategoryform/:id",
    element: <SysDocumentCategoryForm />,
  },
  {
    programId: ConstProgramUtil.cSysRedefinePasswordId,
    path: "sys/redefinepassword",
    element: <RedefinePasswordPage />,
  },
];
