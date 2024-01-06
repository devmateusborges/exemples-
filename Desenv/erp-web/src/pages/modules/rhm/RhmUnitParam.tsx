import { t } from "i18next";
import { capitalize, formatDateTimeColumn } from "../../../utils/FuncUtil";
import useDebounce from "../../../components/toolkit-react/hooks/useDebounce";
import RhmUnitParamService from "../../../services/modules/rhm/RhmUnitParamService";
import { apiParamsConvert } from "../../../utils/ApiUtil";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";
import GenericListPage from "../../generics/GenericListPage";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";

const rhmUnitParamService = new RhmUnitParamService();

const RhmUnitParam: React.FC = () => {
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
        id="rhmunitparam"
        appTitle={capitalize(t("IN18RHMPARAMETROSDEFAULT"))}
        appShowTopBar
        appRouteForm="/private/rhm/rhmunitparamform"
        appDataTableColumns={dataTableColumns}
        appDataTableDataKey="id"
        appRefreshVisible
        appDeleteVisible
        appEditVisible
        appAddVisible
        appServiceDefault={rhmUnitParamService}
        appProgramId={ConstProgramUtil.cRhmunitparamId}
        appButtonDeleteVisibleRow
        appButtonEditVisibleRow
        appPreferenceVisible
        appFavoriteVisible
      />
    </>
  );
};

export default RhmUnitParam;
