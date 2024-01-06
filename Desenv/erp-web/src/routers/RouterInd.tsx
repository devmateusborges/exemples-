import Ind from "../pages/modules/ind/Ind";
import IndCjd from "../pages/modules/ind/IndCjd";
import IndCjdForm from "../pages/modules/ind/IndCjdForm";
import IndCnd from "../pages/modules/ind/IndCnd";
import IndCndForm from "../pages/modules/ind/IndCndForm";
import IndForm from "../pages/modules/ind/IndForm";
import IndFtd from "../pages/modules/ind/IndFtd";
import IndFtdForm from "../pages/modules/ind/IndFtdForm";
import IndGrupo from "../pages/modules/ind/IndGrupo";
import IndGrupoForm from "../pages/modules/ind/IndGrupoForm";
import IndPnl from "../pages/modules/ind/IndPnl";
import IndPnlForm from "../pages/modules/ind/IndPnlForm";
import IndPrm from "../pages/modules/ind/IndPrm";
import IndPrmForm from "../pages/modules/ind/IndPrmForm";
import IndRel from "../pages/modules/ind/IndRel";
import IndRelForm from "../pages/modules/ind/IndRelForm";
import IndSubGrupo from "../pages/modules/ind/IndSubGrupo";
import IndSubGrupoForm from "../pages/modules/ind/IndSubGrupoForm";
import IndUnitParam from "../pages/modules/ind/IndUnitParam";
import IndUnitParamForm from "../pages/modules/ind/IndUnitParamForm";
import { ConstProgramUtil } from "../utils/ConstProgramUtil";

export default [
  {
    programId: ConstProgramUtil.cIndcjdId,
    path: "ind/indcjd",
    element: <IndCjd />,
  },
  {
    programId: ConstProgramUtil.cIndcjdId,
    path: "ind/indcjdform/:id",
    element: <IndCjdForm />,
  },
  {
    programId: ConstProgramUtil.cIndcndId,
    path: "ind/indcnd",
    element: <IndCnd />,
  },
  {
    programId: ConstProgramUtil.cIndcndId,
    path: "ind/indcndform/:id",
    element: <IndCndForm />,
  },
  {
    programId: ConstProgramUtil.cIndftdId,
    path: "ind/indftd",
    element: <IndFtd />,
  },
  {
    programId: ConstProgramUtil.cIndftdId,
    path: "ind/indftdform/:id",
    element: <IndFtdForm />,
  },
  {
    programId: ConstProgramUtil.cIndgrupoId,
    path: "ind/indgrupo",
    element: <IndGrupo />,
  },
  {
    programId: ConstProgramUtil.cIndgrupoId,
    path: "ind/indgrupoform/:id",
    element: <IndGrupoForm />,
  },
  {
    programId: ConstProgramUtil.cIndindId,
    path: "ind/indind",
    element: <Ind />,
  },
  {
    programId: ConstProgramUtil.cIndindId,
    path: "ind/indindform/:id",
    element: <IndForm />,
  },
  {
    programId: ConstProgramUtil.cIndpnlId,
    path: "ind/indpnl",
    element: <IndPnl />,
  },
  {
    programId: ConstProgramUtil.cIndpnlId,
    path: "ind/indpnlform/:id",
    element: <IndPnlForm />,
  },
  {
    programId: ConstProgramUtil.cIndprmId,
    path: "ind/indprm",
    element: <IndPrm />,
  },
  {
    programId: ConstProgramUtil.cIndprmId,
    path: "ind/indprmform/:id",
    element: <IndPrmForm />,
  },
  {
    programId: ConstProgramUtil.cIndrelId,
    path: "ind/indrel",
    element: <IndRel />,
  },
  {
    programId: ConstProgramUtil.cIndrelId,
    path: "ind/indrelform/:id",
    element: <IndRelForm />,
  },
  {
    programId: ConstProgramUtil.cIndsubgrupoId,
    path: "ind/indsubgrupo",
    element: <IndSubGrupo />,
  },
  {
    programId: ConstProgramUtil.cIndsubgrupoId,
    path: "ind/indsubgrupoform/:id",
    element: <IndSubGrupoForm />,
  },
  {
    programId: ConstProgramUtil.cIndunitparamId,
    path: "ind/indunitparam",
    element: <IndUnitParam />,
  },
  {
    programId: ConstProgramUtil.cIndunitparamId,
    path: "ind/indunitparamform/:id",
    element: <IndUnitParamForm />,
  },
];
