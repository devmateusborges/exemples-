import { t } from "i18next";
import { capitalize } from "../../../utils/FuncUtil";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";
import BorUnitParamService from "../../../services/modules/bor/BorUnitParamService";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";
import GenericListPage from "../../generics/GenericListPage";

const borUnitParamService = new BorUnitParamService();

const BorUnitParam: React.FC = () => {
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
        id="borunitparam"
        appTitle={capitalize(t("IN18BORPARAMETROSDEFAULT"))}
        appProgramId={ConstProgramUtil.cBorunitparamId}
        appShowTopBar
        appServiceDefault={borUnitParamService}
        appRouteForm="/private/bor/borunitparamform"
        appDataTableColumns={dataTableColumns}
        appDataTableDataKey="id"
        appRefreshVisible
        appDeleteVisible
        appEditVisible
        appAddVisible
        appButtonDeleteVisibleRow
        appButtonEditVisibleRow
        appPreferenceVisible
        appFavoriteVisible
      />
    </>
  );
};

export default BorUnitParam;
