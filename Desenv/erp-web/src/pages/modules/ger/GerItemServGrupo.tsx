import { t } from "i18next";
import { capitalize, formatDateTimeColumn } from "../../../utils/FuncUtil";
import GerItemServGrupoService from "../../../services/modules/ger/GerItemServGrupoService";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";
import GenericListPage from "../../generics/GenericListPage";
import { dataTableColumnsDet1 } from "./GerItemServGrupoDet1Form";

const gerItemServGrupoService = new GerItemServGrupoService();

const GerItemServGrupo: React.FC = () => {
  // ==============================

  const dataTableColumns: IAppDataTableColumns = {
    columns: [
      {
        appField: "id",
        appHeader: "ID",
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: true,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "sigla_ger_itemserv_grupo",
        appHeader: capitalize(t("IN18GRUPOITEM/SERVICOSIGLADEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "nome",
        appHeader: capitalize(t("IN18NOMEDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "ativo_obj.description",
        appHeader: capitalize(t("IN18ATIVODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "log_user_ins",
        appHeader: capitalize(t("IN18USUARIODEINSERCAODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: true,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "log_date_ins",
        appHeader: capitalize(t("IN18DATADEINSERCAODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: true,
        appDataType: "date",
        appExport: true,
      },
      {
        appField: "log_date_upd",
        appHeader: capitalize(t("IN18DATADEALTERACAODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: true,
        appDataType: "date",
        appExport: true,
      },
      {
        appField: "log_user_upd",
        appHeader: capitalize(t("IN18USUARIODEALTERACAODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: true,
        appDataType: "text",
        appExport: true,
      },
    ],
  };
  // ==============================

  const detsColumns = [
    {
      title: "Subgrupo",
      name: "ger_itemserv_subgrupo_childs",
      ...dataTableColumnsDet1,
    },
  ];
  // ==============================

  return (
    <>
      <GenericListPage
        id="geritemservgrupo"
        appTitle={capitalize(t("IN18GERGRUPODEITEM/SERVICODEFAULT"))}
        appRouteForm="/private/ger/geritemservgrupoform"
        appProgramId={ConstProgramUtil.cGeritemservgrupoId}
        appServiceDefault={gerItemServGrupoService}
        appDataTableColumns={dataTableColumns}
        appDataTableDetColumns={detsColumns}
        appDataTableDataKey="id"
        appRowExpand
        appShowTopBar
        appRefreshVisible
        appDeleteVisible
        appEditVisible
        appAddVisible
        appFavoriteVisible
        appPreferenceVisible
        appButtonDeleteVisibleRow
        appButtonEditVisibleRow
      />
    </>
  );
};

export default GerItemServGrupo;
