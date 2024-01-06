import CrmAviso from "../pages/modules/crm/CrmAviso";
import CrmAvisoForm from "../pages/modules/crm/CrmAvisoForm";
import CrmChatGrupo from "../pages/modules/crm/CrmChatGrupo";
import CrmChatGrupoForm from "../pages/modules/crm/CrmChatGrupoForm";
import CrmClass from "../pages/modules/crm/CrmClass";
import CrmClassForm from "../pages/modules/crm/CrmClassForm";
import CrmClassGrupo from "../pages/modules/crm/CrmClassGrupo";
import CrmClassGrupoForm from "../pages/modules/crm/CrmClassGrupoForm";
import CrmEtapa from "../pages/modules/crm/CrmEtapa";
import CrmEtapaForm from "../pages/modules/crm/CrmEtapaForm";
import CrmMov from "../pages/modules/crm/CrmMov";
import CrmMovForm from "../pages/modules/crm/CrmMovForm";
import CrmOrg from "../pages/modules/crm/CrmOrg";
import CrmOrgForm from "../pages/modules/crm/CrmOrgForm";
import CrmPrioridade from "../pages/modules/crm/CrmPrioridade";
import CrmPrioridadeForm from "../pages/modules/crm/CrmPrioridadeForm";
import CrmResposta from "../pages/modules/crm/CrmResposta";
import CrmRespostaForm from "../pages/modules/crm/CrmRespostaForm";
import CrmStatus from "../pages/modules/crm/CrmStatus";
import CrmStatusForm from "../pages/modules/crm/CrmStatusForm";
import CrmTag from "../pages/modules/crm/CrmTag";
import CrmTagForm from "../pages/modules/crm/CrmTagForm";
import CrmUnitParam from "../pages/modules/crm/CrmUnitParam";
import CrmUnitParamForm from "../pages/modules/crm/CrmUnitParamForm";
import { ConstProgramUtil } from "../utils/ConstProgramUtil";

export default [
  {
    programId: ConstProgramUtil.cCrmavisoId,
    path: "crm/crmaviso",
    element: <CrmAviso />,
  },
  {
    programId: ConstProgramUtil.cCrmavisoId,
    path: "crm/crmavisoform/:id",
    element: <CrmAvisoForm />,
  },
  {
    programId: ConstProgramUtil.cCrmchatgrupoId,
    path: "crm/crmchatgrupo",
    element: <CrmChatGrupo />,
  },
  {
    programId: ConstProgramUtil.cCrmchatgrupoId,
    path: "crm/crmchatgrupoform/:id",
    element: <CrmChatGrupoForm />,
  },
  {
    programId: ConstProgramUtil.cCrmclassId,
    path: "crm/crmclass",
    element: <CrmClass />,
  },
  {
    programId: ConstProgramUtil.cCrmclassId,
    path: "crm/crmclassform/:id",
    element: <CrmClassForm />,
  },
  {
    programId: ConstProgramUtil.cCrmclassgrupoId,
    path: "crm/crmclassgrupo",
    element: <CrmClassGrupo />,
  },
  {
    programId: ConstProgramUtil.cCrmclassgrupoId,
    path: "crm/crmclassgrupoform/:id",
    element: <CrmClassGrupoForm />,
  },
  {
    programId: ConstProgramUtil.cCrmetapaId,
    path: "crm/crmetapa",
    element: <CrmEtapa />,
  },
  {
    programId: ConstProgramUtil.cCrmetapaId,
    path: "crm/crmetapaform/:id",
    element: <CrmEtapaForm />,
  },
  {
    programId: ConstProgramUtil.cCrmmovId,
    path: "crm/crmmov",
    element: <CrmMov />,
  },
  {
    programId: ConstProgramUtil.cCrmmovId,
    path: "crm/crmmovform/:id",
    element: <CrmMovForm />,
  },
  {
    programId: ConstProgramUtil.cCrmorgId,
    path: "crm/crmorg",
    element: <CrmOrg />,
  },
  {
    programId: ConstProgramUtil.cCrmorgId,
    path: "crm/crmorgform/:id",
    element: <CrmOrgForm />,
  },
  {
    programId: ConstProgramUtil.cCrmprioridadeId,
    path: "crm/crmprioridade",
    element: <CrmPrioridade />,
  },
  {
    programId: ConstProgramUtil.cCrmprioridadeId,
    path: "crm/crmprioridadeform/:id",
    element: <CrmPrioridadeForm />,
  },
  {
    programId: ConstProgramUtil.cCrmrespostaId,
    path: "crm/crmresposta",
    element: <CrmResposta />,
  },
  {
    programId: ConstProgramUtil.cCrmrespostaId,
    path: "crm/crmrespostaform/:id",
    element: <CrmRespostaForm />,
  },
  {
    programId: ConstProgramUtil.cCrmstatusId,
    path: "crm/crmstatus",
    element: <CrmStatus />,
  },
  {
    programId: ConstProgramUtil.cCrmstatusId,
    path: "crm/crmstatusform/:id",
    element: <CrmStatusForm />,
  },
  {
    programId: ConstProgramUtil.cCrmtagId,
    path: "crm/crmtag",
    element: <CrmTag />,
  },
  {
    programId: ConstProgramUtil.cCrmtagId,
    path: "crm/crmtagform/:id",
    element: <CrmTagForm />,
  },
  {
    programId: ConstProgramUtil.cCrmunitparamId,
    path: "crm/crmunitparam",
    element: <CrmUnitParam />,
  },
  {
    programId: ConstProgramUtil.cCrmunitparamId,
    path: "crm/crmunitparamform/:id",
    element: <CrmUnitParamForm />,
  },
];
