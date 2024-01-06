import OpeAtividade from "../pages/modules/ope/OpeAtividade";
import OpeAtividadeForm from "../pages/modules/ope/OpeAtividadeForm";
import OpeAtividadeGrupo from "../pages/modules/ope/OpeAtividadeGrupo";
import OpeAtividadeGrupoFrom from "../pages/modules/ope/OpeAtividadeGrupoFrom";
import OpeAtividadeSistema from "../pages/modules/ope/OpeAtividadeSistema";
import OpeAtividadeSistemaForm from "../pages/modules/ope/OpeAtividadeSistemaForm";
import OpeCentro1 from "../pages/modules/ope/OpeCentro1";
import OpeCentro1Form from "../pages/modules/ope/OpeCentro1Form";
import OpeCentro2 from "../pages/modules/ope/OpeCentro2";
import OpeCentro2Form from "../pages/modules/ope/OpeCentro2Form";
import OpeCentro2MovMedia from "../pages/modules/ope/OpeCentro2MovMedia";
import OpeCentro2MovMediaForm from "../pages/modules/ope/OpeCentro2MovMediaForm";
import OpeCentro2OrdStatus from "../pages/modules/ope/OpeCentro2OrdStatus";
import OpeCentro2OrdStatusForm from "../pages/modules/ope/OpeCentro2OrdStatusForm";
import OpeCentro2OrdTipo from "../pages/modules/ope/OpeCentro2OrdTipo";
import OpeCentro2OrdTipoForm from "../pages/modules/ope/OpeCentro2OrdTipoForm";
import OpeCentroConfig from "../pages/modules/ope/OpeCentroConfig";
import OpeCentroConfigForm from "../pages/modules/ope/OpeCentroConfigForm";
import OpeCentroGrupo from "../pages/modules/ope/OpeCentroGrupo";
import OpeCentroGrupoForm from "../pages/modules/ope/OpeCentroGrupoForm";
import OpeCentroRatTipo from "../pages/modules/ope/OpeCentroRatTipo";
import OpeCentroRatTipoForm from "../pages/modules/ope/OpeCentroRatTipoForm";
import OpeCentroRend from "../pages/modules/ope/OpeCentroRend";
import OpeCentroRendForm from "../pages/modules/ope/OpeCentroRendForm";
import OpeCentroTipo from "../pages/modules/ope/OpeCentroTipo";
import OpeCentroTipoForm from "../pages/modules/ope/OpeCentroTipoForm";
import OpeCentroVersao from "../pages/modules/ope/OpeCentroVersao";
import OpeCentroVersaoForm from "../pages/modules/ope/OpeCentroVersaoForm";
import OpeCicloVar from "../pages/modules/ope/OpeCicloVar";
import OpeCicloVarForm from "../pages/modules/ope/OpeCicloVarForm";
import OpeCompart from "../pages/modules/ope/OpeCompart";
import OpeCompartForm from "../pages/modules/ope/OpeCompartForm";
import OpeCompartGrupo from "../pages/modules/ope/OpeCompartGrupo";
import OpeCompartGrupoForm from "../pages/modules/ope/OpeCompartGrupoForm";
import OpeCompartMedida from "../pages/modules/ope/OpeCompartMedida";
import OpeCompartMedidaForm from "../pages/modules/ope/OpeCompartMedidaForm";
import OpeCompartOcor from "../pages/modules/ope/OpeCompartOcor";
import OpeCompartOcorForm from "../pages/modules/ope/OpeCompartOcorForm";
import OpeCompartPosicao from "../pages/modules/ope/OpeCompartPosicao";
import OpeCompartPosicaoForm from "../pages/modules/ope/OpeCompartPosicaoForm";
import OpeCompartStatus from "../pages/modules/ope/OpeCompartStatus";
import OpeCompartStatusForm from "../pages/modules/ope/OpeCompartStatusForm";
import OpeCompartTipo from "../pages/modules/ope/OpeCompartTipo";
import OpeCompartTipoForm from "../pages/modules/ope/OpeCompartTipoForm";
import OpeEspac from "../pages/modules/ope/OpeEspac";
import OpeEspacForm from "../pages/modules/ope/OpeEspacForm";
import OpeEstagio from "../pages/modules/ope/OpeEstagio";
import OpeEstagioForm from "../pages/modules/ope/OpeEstagioForm";
import OpeFrenteTrabalho from "../pages/modules/ope/OpeFrenteTrabalho";
import OpeFrenteTrabalhoForm from "../pages/modules/ope/OpeFrenteTrabalhoForm";
import OpeOcor from "../pages/modules/ope/OpeOcor";
import OpeOcorCompartMov from "../pages/modules/ope/OpeOcorCompartMov";
import OpeOcorCompartMovForm from "../pages/modules/ope/OpeOcorCompartMovForm";
import OpeOcorForm from "../pages/modules/ope/OpeOcorForm";
import OpeOcorGrupo from "../pages/modules/ope/OpeOcorGrupo";
import OpeOcorGrupoForm from "../pages/modules/ope/OpeOcorGrupoForm";
import OpeOcorStatus from "../pages/modules/ope/OpeOcorStatus";
import OpeOcorStatusForm from "../pages/modules/ope/OpeOcorStatusForm";
import OpeOcorTipo from "../pages/modules/ope/OpeOcorTipo";
import OpeOcorTipoForm from "../pages/modules/ope/OpeOcorTipoForm";
import OpePeriodo from "../pages/modules/ope/OpePeriodo";
import OpePeriodoForm from "../pages/modules/ope/OpePeriodoForm";
import OpeRegiao from "../pages/modules/ope/OpeRegiao";
import OpeRegiaoForm from "../pages/modules/ope/OpeRegiaoForm";
import OpeTipoSolo from "../pages/modules/ope/OpeTipoSolo";
import OpeTipoSoloForm from "../pages/modules/ope/OpeTipoSoloForm";
import OpeUnitParam from "../pages/modules/ope/OpeUnitParam";
import OpeUnitParamForm from "../pages/modules/ope/OpeUnitParamForm";
import { ConstProgramUtil } from "../utils/ConstProgramUtil";

export default [
  {
    programId: ConstProgramUtil.cOpeatividadeId,
    path: "ope/opeatividade",
    element: <OpeAtividade />,
  },
  {
    programId: ConstProgramUtil.cOpeatividadeId,
    path: "ope/opeatividadeform/:id",
    element: <OpeAtividadeForm />,
  },
  {
    programId: ConstProgramUtil.cOpecentro1Id,
    path: "ope/opecentro1",
    element: <OpeCentro1 />,
  },
  {
    programId: ConstProgramUtil.cOpecentro1Id,
    path: "ope/opecentro1form/:id",
    element: <OpeCentro1Form />,
  },
  {
    programId: ConstProgramUtil.cOpecentro2Id,
    path: "ope/opecentro2",
    element: <OpeCentro2 />,
  },
  {
    programId: ConstProgramUtil.cOpecentro2Id,
    path: "ope/opecentro2form/:id",
    element: <OpeCentro2Form />,
  },
  {
    programId: ConstProgramUtil.cOpecentroconfigId,
    path: "ope/opecentroconfig",
    element: <OpeCentroConfig />,
  },
  {
    programId: ConstProgramUtil.cOpecentroconfigId,
    path: "ope/opecentroconfigform/:id",
    element: <OpeCentroConfigForm />,
  },
  {
    programId: ConstProgramUtil.cOpecentrogrupoId,
    path: "ope/opecentrogrupo",
    element: <OpeCentroGrupo />,
  },
  {
    programId: ConstProgramUtil.cOpecentrogrupoId,
    path: "ope/opecentrogrupoform/:id",
    element: <OpeCentroGrupoForm />,
  },
  {
    programId: ConstProgramUtil.cOpecentrorendId,
    path: "ope/opecentrorend",
    element: <OpeCentroRend />,
  },
  {
    programId: ConstProgramUtil.cOpecentrorendId,
    path: "ope/opecentrorendform/:id",
    element: <OpeCentroRendForm />,
  },
  {
    programId: ConstProgramUtil.cOpecentrotipoId,
    path: "ope/opecentrotipo",
    element: <OpeCentroTipo />,
  },
  {
    programId: ConstProgramUtil.cOpecentrotipoId,
    path: "ope/opecentrotipoform/:id",
    element: <OpeCentroTipoForm />,
  },
  {
    programId: ConstProgramUtil.cOpecentroversaoId,
    path: "ope/opecentroversao",
    element: <OpeCentroVersao />,
  },
  {
    programId: ConstProgramUtil.cOpecentroversaoId,
    path: "ope/opecentroversaoform/:id",
    element: <OpeCentroVersaoForm />,
  },
  {
    programId: ConstProgramUtil.cOpeciclovarId,
    path: "ope/opeciclovar",
    element: <OpeCicloVar />,
  },
  {
    programId: ConstProgramUtil.cOpeciclovarId,
    path: "ope/opeciclovarform/:id",
    element: <OpeCicloVarForm />,
  },
  {
    programId: ConstProgramUtil.cOpecompartId,
    path: "ope/opecompart",
    element: <OpeCompart />,
  },
  {
    programId: ConstProgramUtil.cOpecompartId,
    path: "ope/opecompartform/:id",
    element: <OpeCompartForm />,
  },
  {
    programId: ConstProgramUtil.cOpecompartgrupoId,
    path: "ope/opecompartgrupo",
    element: <OpeCompartGrupo />,
  },
  {
    programId: ConstProgramUtil.cOpecompartgrupoId,
    path: "ope/opecompartgrupoform/:id",
    element: <OpeCompartGrupoForm />,
  },
  {
    programId: ConstProgramUtil.cOpecompartocorId,
    path: "ope/opecompartocor",
    element: <OpeCompartOcor />,
  },
  {
    programId: ConstProgramUtil.cOpecompartocorId,
    path: "ope/opecompartocorform/:id",
    element: <OpeCompartOcorForm />,
  },
  {
    programId: ConstProgramUtil.cOpecomparttipoId,
    path: "ope/opecomparttipo",
    element: <OpeCompartTipo />,
  },
  {
    programId: ConstProgramUtil.cOpecomparttipoId,
    path: "ope/opecomparttipoform/:id",
    element: <OpeCompartTipoForm />,
  },
  {
    programId: ConstProgramUtil.cOpeespacId,
    path: "ope/opeespac",
    element: <OpeEspac />,
  },
  {
    programId: ConstProgramUtil.cOpeespacId,
    path: "ope/opeespacform/:id",
    element: <OpeEspacForm />,
  },
  {
    programId: ConstProgramUtil.cOpeestagioId,
    path: "ope/opeestagio",
    element: <OpeEstagio />,
  },
  {
    programId: ConstProgramUtil.cOpeestagioId,
    path: "ope/opeestagioform/:id",
    element: <OpeEstagioForm />,
  },
  {
    programId: ConstProgramUtil.cOpeocorgrupoId,
    path: "ope/opeocorgrupo",
    element: <OpeOcorGrupo />,
  },
  {
    programId: ConstProgramUtil.cOpeocorgrupoId,
    path: "ope/opeocorgrupoform/:id",
    element: <OpeOcorGrupoForm />,
  },
  {
    programId: ConstProgramUtil.cOpeocorstatusId,
    path: "ope/opeocorstatus",
    element: <OpeOcorStatus />,
  },
  {
    programId: ConstProgramUtil.cOpeocorstatusId,
    path: "ope/opeocorstatusform/:id",
    element: <OpeOcorStatusForm />,
  },
  {
    programId: ConstProgramUtil.cOpeocortipoId,
    path: "ope/opeocortipo",
    element: <OpeOcorTipo />,
  },
  {
    programId: ConstProgramUtil.cOpeocortipoId,
    path: "ope/opeocortipoform/:id",
    element: <OpeOcorTipoForm />,
  },
  {
    programId: ConstProgramUtil.cOpeperiodoId,
    path: "ope/opeperiodo",
    element: <OpePeriodo />,
  },
  {
    programId: ConstProgramUtil.cOpeperiodoId,
    path: "ope/opeperiodoform/:id",
    element: <OpePeriodoForm />,
  },
  {
    programId: ConstProgramUtil.cOperegiaoId,
    path: "ope/operegiao",
    element: <OpeRegiao />,
  },
  {
    programId: ConstProgramUtil.cOperegiaoId,
    path: "ope/operegiaoform/:id",
    element: <OpeRegiaoForm />,
  },
  {
    programId: ConstProgramUtil.cOpetiposoloId,
    path: "ope/opetiposolo",
    element: <OpeTipoSolo />,
  },
  {
    programId: ConstProgramUtil.cOpetiposoloId,
    path: "ope/opetiposoloform/:id",
    element: <OpeTipoSoloForm />,
  },
  {
    programId: ConstProgramUtil.cOpeunitparamId,
    path: "ope/opeunitparam",
    element: <OpeUnitParam />,
  },
  {
    programId: ConstProgramUtil.cOpeunitparamId,
    path: "ope/opeunitparamform/:id",
    element: <OpeUnitParamForm />,
  },
  {
    programId: ConstProgramUtil.cOpeocorcompartmovId,
    path: "ope/opeocorcompartmov",
    element: <OpeOcorCompartMov />,
  },
  {
    programId: ConstProgramUtil.cOpeocorcompartmovId,
    path: "ope/opeocorcompartmovform/:id",
    element: <OpeOcorCompartMovForm />,
  },
  {
    programId: ConstProgramUtil.cOpefrentetrabalhoId,
    path: "ope/opefrentetrabalho",
    element: <OpeFrenteTrabalho />,
  },
  {
    programId: ConstProgramUtil.cOpefrentetrabalhoId,
    path: "ope/opefrentetrabalhoform/:id",
    element: <OpeFrenteTrabalhoForm />,
  },
  {
    programId: ConstProgramUtil.cOpeocorId,
    path: "ope/opeocor",
    element: <OpeOcor />,
  },
  {
    programId: ConstProgramUtil.cOpeocorId,
    path: "ope/opeocorform/:id",
    element: <OpeOcorForm />,
  },
  {
    programId: ConstProgramUtil.cOpecompartstatusId,
    path: "ope/opecompartstatus",
    element: <OpeCompartStatus />,
  },
  {
    programId: ConstProgramUtil.cOpecompartstatusId,
    path: "ope/opecompartstatusform/:id",
    element: <OpeCompartStatusForm />,
  },
  {
    programId: ConstProgramUtil.cOpecompartposicaoId,
    path: "ope/opecompartposicao",
    element: <OpeCompartPosicao />,
  },
  {
    programId: ConstProgramUtil.cOpecompartposicaoId,
    path: "ope/opecompartposicaoform/:id",
    element: <OpeCompartPosicaoForm />,
  },
  {
    programId: ConstProgramUtil.cOpecompartmedidaId,
    path: "ope/opecompartmedida",
    element: <OpeCompartMedida />,
  },
  {
    programId: ConstProgramUtil.cOpecompartmedidaId,
    path: "ope/opecompartmedidaform/:id",
    element: <OpeCompartMedidaForm />,
  },
  {
    programId: ConstProgramUtil.cOpecentrorattipoId,
    path: "ope/opecentrorattipo",
    element: <OpeCentroRatTipo />,
  },
  {
    programId: ConstProgramUtil.cOpecentrorattipoId,
    path: "ope/opecentrorattipoform/:id",
    element: <OpeCentroRatTipoForm />,
  },
  {
    programId: ConstProgramUtil.cOpecentro2ordtipoId,
    path: "ope/opecentro2ordtipo",
    element: <OpeCentro2OrdTipo />,
  },
  {
    programId: ConstProgramUtil.cOpecentro2ordtipoId,
    path: "ope/opecentro2ordtipoform/:id",
    element: <OpeCentro2OrdTipoForm />,
  },
  {
    programId: ConstProgramUtil.cOpecentro2ordstatusId,
    path: "ope/opecentro2ordstatus",
    element: <OpeCentro2OrdStatus />,
  },
  {
    programId: ConstProgramUtil.cOpecentro2ordstatusId,
    path: "ope/opecentro2ordstatusform/:id",
    element: <OpeCentro2OrdStatusForm />,
  },
  {
    programId: ConstProgramUtil.cOpecentro2movmediaId,
    path: "ope/opecentro2movmedia",
    element: <OpeCentro2MovMedia />,
  },
  {
    programId: ConstProgramUtil.cOpecentro2movmediaId,
    path: "ope/opecentro2movmediaform/:id",
    element: <OpeCentro2MovMediaForm />,
  },
  {
    programId: ConstProgramUtil.cOpeatividadesistemaId,
    path: "ope/opeatividadesistema",
    element: <OpeAtividadeSistema />,
  },
  {
    programId: ConstProgramUtil.cOpeatividadesistemaId,
    path: "ope/opeatividadesistemaform/:id",
    element: <OpeAtividadeSistemaForm />,
  },
  {
    programId: ConstProgramUtil.cOpeatividadegrupoId,
    path: "ope/opeatividadegrupo",
    element: <OpeAtividadeGrupo />,
  },
  {
    programId: ConstProgramUtil.cOpeatividadegrupoId,
    path: "ope/opeatividadegrupoform/:id",
    element: <OpeAtividadeGrupoFrom />,
  },
  {
    programId: ConstProgramUtil.cOpeperiodoId,
    path: "ope/opeperiodo",
    element: <OpePeriodo />,
  },
  {
    programId: ConstProgramUtil.cOpeperiodoId,
    path: "ope/opeperiodoform/:id",
    element: <OpePeriodo />,
  },
];
