import { t } from "i18next";
import { capitalize } from "../../../utils/FuncUtil";
import OpeCentro2OrdStatusService from "../../../services/modules/ope/OpeCentro2OrdStatusService";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";
import GenericListPage from "../../generics/GenericListPage";

const opeCentro2OrdStatusService = new OpeCentro2OrdStatusService();

const OpeCentro2OrdStatus: React.FC = () => {
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
        appField: "sigla_ord_status",
        appHeader: capitalize(t("IN18STATUSDEORDEMSIGLADEFAULT")),
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
        appField: "tipo_status_obj.description",
        appHeader: capitalize(t("IN18TIPOSTATUSDEFAULT")),
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

  return (
    <>
      <GenericListPage
        id="/opecentro2ordstatus"
        appTitle={capitalize(t("IN18OPESTATUSDEORDEMDEFAULT"))}
        appServiceDefault={opeCentro2OrdStatusService}
        appRouteForm="/private/ope/opecentro2ordstatusform"
        appDataTableColumns={dataTableColumns}
        appDataTableDataKey="id"
        appShowTopBar
        appRefreshVisible
        appDeleteVisible
        appEditVisible
        appAddVisible
        appProgramId={ConstProgramUtil.cOpecentro2ordstatusId}
        appFavoriteVisible
        appButtonDeleteVisibleRow
        appButtonEditVisibleRow
        appPreferenceVisible
      />
    </>
  );
};

export default OpeCentro2OrdStatus;
