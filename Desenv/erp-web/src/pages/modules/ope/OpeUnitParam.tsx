import { t } from "i18next";
import { capitalize } from "../../../utils/FuncUtil";
import OpeUnitParamService from "../../../services/modules/ope/OpeUnitParamService";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";
import GenericListPage from "../../generics/GenericListPage";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";

const opeUnitParamService = new OpeUnitParamService();

const OpeUnitParam: React.FC = () => {
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
        appField: "data_valid_ini",
        appHeader: capitalize(t("IN18DATAVALIDADEDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "date",
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

  return (
    <>
      <GenericListPage
        id="opeunitparam"
        appTitle={capitalize(t("IN18OPEPARAMETROSDEFAULT"))}
        appRouteForm="/private/ope/opeunitparamform"
        appDataTableColumns={dataTableColumns}
        appServiceDefault={opeUnitParamService}
        appProgramId={ConstProgramUtil.cOpeunitparamId}
        appDataTableDataKey="id"
        appShowTopBar
        appRefreshVisible
        appDeleteVisible
        appEditVisible
        appAddVisible
        appFavoriteVisible
        appButtonDeleteVisibleRow
        appButtonEditVisibleRow
        appPreferenceVisible
      />
    </>
  );
};

export default OpeUnitParam;
