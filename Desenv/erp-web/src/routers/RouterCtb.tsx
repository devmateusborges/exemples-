import CtbCentro from "../pages/modules/ctb/CtbCentro";
import CtbCentroForm from "../pages/modules/ctb/CtbCentroForm";
import CtbCentroGrupo from "../pages/modules/ctb/CtbCentroGrupo";
import CtbCentroGrupoForm from "../pages/modules/ctb/CtbCentroGrupoForm";
import CtbComp from "../pages/modules/ctb/CtbComp";
import CtbCompForm from "../pages/modules/ctb/CtbCompForm";
import CtbCompGrupo from "../pages/modules/ctb/CtbCompGrupo";
import CtbCompGrupoForm from "../pages/modules/ctb/CtbCompGrupoForm";
import CtbContaGrupo from "../pages/modules/ctb/CtbContaGrupo";
import CtbContaGrupoForm from "../pages/modules/ctb/CtbContaGrupoForm";
import CtbContaVersao from "../pages/modules/ctb/CtbContaVersao";
import CtbContaVersaoForm from "../pages/modules/ctb/CtbContaVersaoForm";
import CtbHistorico from "../pages/modules/ctb/CtbHistorico";
import CtbHistoricoForm from "../pages/modules/ctb/CtbHistoricoForm";
import CtbLote from "../pages/modules/ctb/CtbLote";
import CtbLoteForm from "../pages/modules/ctb/CtbLoteForm";
import CtbTipoSaldo from "../pages/modules/ctb/CtbTipoSaldo";
import CtbTipoSaldoForm from "../pages/modules/ctb/CtbTipoSaldoForm";
import CtbUnitParam from "../pages/modules/ctb/CtbUnitParam";
import CtbUnitParamForm from "../pages/modules/ctb/CtbUnitParamForm";
import CtbVersao from "../pages/modules/ctb/CtbVersao";
import CtbVersaoForm from "../pages/modules/ctb/CtbVersaoForm";
import { ConstProgramUtil } from "../utils/ConstProgramUtil";

export default [
  {
    programId: ConstProgramUtil.cCtbcentroId,
    path: "ctb/ctbcentro",
    element: <CtbCentro />,
  },
  {
    programId: ConstProgramUtil.cCtbcentroId,
    path: "ctb/ctbcentroform/:id",
    element: <CtbCentroForm />,
  },
  {
    programId: ConstProgramUtil.cCtbcentrogrupoId,
    path: "ctb/ctbcentrogrupo",
    element: <CtbCentroGrupo />,
  },
  {
    programId: ConstProgramUtil.cCtbcentrogrupoId,
    path: "ctb/ctbcentrogrupoform/:id",
    element: <CtbCentroGrupoForm />,
  },
  {
    programId: ConstProgramUtil.cCtbcompId,
    path: "ctb/ctbcomp",
    element: <CtbComp />,
  },
  {
    programId: ConstProgramUtil.cCtbcompId,
    path: "ctb/ctbcompform/:id",
    element: <CtbCompForm />,
  },
  {
    programId: ConstProgramUtil.cCtbcompgrupoId,
    path: "ctb/ctbcompgrupo",
    element: <CtbCompGrupo />,
  },
  {
    programId: ConstProgramUtil.cCtbcompgrupoId,
    path: "ctb/ctbcompgrupoform/:id",
    element: <CtbCompGrupoForm />,
  },
  {
    programId: ConstProgramUtil.cCtbcontagrupoId,
    path: "ctb/ctbcontagrupo",
    element: <CtbContaGrupo />,
  },
  {
    programId: ConstProgramUtil.cCtbcontagrupoId,
    path: "ctb/ctbcontagrupoform/:id",
    element: <CtbContaGrupoForm />,
  },
  {
    programId: ConstProgramUtil.cCtbcontaversaoId,
    path: "ctb/ctbcontaversao",
    element: <CtbContaVersao />,
  },
  {
    programId: ConstProgramUtil.cCtbcontaversaoId,
    path: "ctb/ctbcontaversaoform/:id",
    element: <CtbContaVersaoForm />,
  },
  {
    programId: ConstProgramUtil.cCtbhistoricoId,
    path: "ctb/ctbhistorico",
    element: <CtbHistorico />,
  },
  {
    programId: ConstProgramUtil.cCtbhistoricoId,
    path: "ctb/ctbhistoricoform/:id",
    element: <CtbHistoricoForm />,
  },
  {
    programId: ConstProgramUtil.cCtbloteId,
    path: "ctb/ctblote",
    element: <CtbLote />,
  },
  {
    programId: ConstProgramUtil.cCtbloteId,
    path: "ctb/ctbloteform/:id",
    element: <CtbLoteForm />,
  },
  {
    programId: ConstProgramUtil.cCtbtiposaldoId,
    path: "ctb/ctbtiposaldo",
    element: <CtbTipoSaldo />,
  },
  {
    programId: ConstProgramUtil.cCtbtiposaldoId,
    path: "ctb/ctbtiposaldoform/:id",
    element: <CtbTipoSaldoForm />,
  },
  {
    programId: ConstProgramUtil.cCtbunitparamId,
    path: "ctb/ctbunitparam",
    element: <CtbUnitParam />,
  },
  {
    programId: ConstProgramUtil.cCtbunitparamId,
    path: "ctb/ctbunitparamform/:id",
    element: <CtbUnitParamForm />,
  },
  {
    programId: ConstProgramUtil.cCtbversaoId,
    path: "ctb/ctbversao",
    element: <CtbVersao />,
  },
  {
    programId: ConstProgramUtil.cCtbversaoId,
    path: "ctb/ctbversaoform/:id",
    element: <CtbVersaoForm />,
  },
];
