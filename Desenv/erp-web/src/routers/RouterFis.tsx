import FinBanco from "../pages/modules/fin/FinBanco";
import FinBancoForm from "../pages/modules/fin/FinBancoForm";
import FisCertificado from "../pages/modules/fis/FisCertificado";
import FisCertificadoForm from "../pages/modules/fis/FisCertificadoForm";
import FisCest from "../pages/modules/fis/FisCest";
import FisCestForm from "../pages/modules/fis/FisCestForm";
import FisCfop from "../pages/modules/fis/FisCfop";
import FisCfopForm from "../pages/modules/fis/FisCfopForm";
import FisDoc from "../pages/modules/fis/FisDoc";
import FisDocForm from "../pages/modules/fis/FisDocForm";
import FisDocTipo from "../pages/modules/fis/FisDocTipo";
import FisDocTipoForm from "../pages/modules/fis/FisDocTipoForm";
import FisIbpt from "../pages/modules/fis/FisIbpt";
import FisIbptForm from "../pages/modules/fis/FisIbptForm";
import FisNbs from "../pages/modules/fis/FisNbs";
import FisNbsForm from "../pages/modules/fis/FisNbsForm";
import FisNcm from "../pages/modules/fis/FisNcm";
import FisNcmForm from "../pages/modules/fis/FisNcmForm";
import FisObs from "../pages/modules/fis/FisObs";
import FisObsForm from "../pages/modules/fis/FisObsForm";
import FisTributo from "../pages/modules/fis/FisTributo";
import FisTributoForm from "../pages/modules/fis/FisTributoForm";
import FisUnitParam from "../pages/modules/fis/FisUnitParam";
import FisUnitParamForm from "../pages/modules/fis/FisUnitParamForm";
import { ConstProgramUtil } from "../utils/ConstProgramUtil";

export default [
  {
    programId: ConstProgramUtil.cFiscertificadoId,
    path: "fis/fiscertificado",
    element: <FisCertificado />,
  },
  {
    programId: ConstProgramUtil.cFiscertificadoId,
    path: "fis/fiscertificadoform/:id",
    element: <FisCertificadoForm />,
  },
  {
    programId: ConstProgramUtil.cFiscestId,
    path: "fis/fiscest",
    element: <FisCest />,
  },
  {
    programId: ConstProgramUtil.cFiscestId,
    path: "fis/fiscestform/:id",
    element: <FisCestForm />,
  },
  {
    programId: ConstProgramUtil.cFiscfopId,
    path: "fis/fiscfop",
    element: <FisCfop />,
  },
  {
    programId: ConstProgramUtil.cFiscfopId,
    path: "fis/fiscfopform/:id",
    element: <FisCfopForm />,
  },
  {
    programId: ConstProgramUtil.cFisdocId,
    path: "fis/fisdoc",
    element: <FisDoc />,
  },
  {
    programId: ConstProgramUtil.cFisdocId,
    path: "fis/fisdocform/:id",
    element: <FisDocForm />,
  },
  {
    programId: ConstProgramUtil.cFisdoctipoId,
    path: "fis/fisdoctipo",
    element: <FisDocTipo />,
  },
  {
    programId: ConstProgramUtil.cFisdoctipoId,
    path: "fis/fisdoctipoform/:id",
    element: <FisDocTipoForm />,
  },
  {
    programId: ConstProgramUtil.cFisibptId,
    path: "fis/fisibpt",
    element: <FisIbpt />,
  },
  {
    programId: ConstProgramUtil.cFisibptId,
    path: "fis/fisibptform/:id",
    element: <FisIbptForm />,
  },
  {
    programId: ConstProgramUtil.cFisnbsId,
    path: "fis/fisnbs",
    element: <FisNbs />,
  },
  {
    programId: ConstProgramUtil.cFisnbsId,
    path: "fis/fisnbsform/:id",
    element: <FisNbsForm />,
  },
  {
    programId: ConstProgramUtil.cFisncmId,
    path: "fis/fisncm",
    element: <FisNcm />,
  },
  {
    programId: ConstProgramUtil.cFisncmId,
    path: "fis/fisncmform/:id",
    element: <FisNcmForm />,
  },
  {
    programId: ConstProgramUtil.cFisobsId,
    path: "fis/fisobs",
    element: <FisObs />,
  },
  {
    programId: ConstProgramUtil.cFisobsId,
    path: "fis/fisobsform/:id",
    element: <FisObsForm />,
  },
  {
    programId: ConstProgramUtil.cFistributoId,
    path: "fis/fistributo",
    element: <FisTributo />,
  },
  {
    programId: ConstProgramUtil.cFistributoId,
    path: "fis/fistributoform/:id",
    element: <FisTributoForm />,
  },
  {
    programId: ConstProgramUtil.cFisunitparamId,
    path: "fis/fisunitparam",
    element: <FisUnitParam />,
  },
  {
    programId: ConstProgramUtil.cFisunitparamId,
    path: "fis/fisunitparamform/:id",
    element: <FisUnitParamForm />,
  },
];
