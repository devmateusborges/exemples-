import { t } from "i18next";
import { capitalize } from "../../../utils/FuncUtil";
import SysPlanService from "../../../services/modules/sys/SysPlanService";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";
import GenericListPage from "../../generics/GenericListPage";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";
import { dataTableColumnsDet1 } from "./SysPlanFormDet1";

const sysPlanService = new SysPlanService();

const SysPlan: React.FC = () => {
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
        appField: "code_plan",
        appHeader: capitalize(t("IN18PLANOSIGLADEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "name",
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
        appField: "active_obj.description",
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
        appField: "type_plan_obj.description",
        appHeader: capitalize(t("IN18TIPOPLANODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "description",
        appHeader: capitalize(t("IN18DESCRICAODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "indicated_obj.description",
        appHeader: capitalize(t("IN18INDICADODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "sys_id_obj.code_sys",
        appHeader: capitalize(t("IN18RESTRICAODESISTEMASIGLADEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "sys_id_obj.name",
        appHeader: capitalize(t("IN18RESTRICAODESISTEMANOMEDEFAULT")),
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

  const detsColumns = [
    {
      title: "Det 1",
      name: "sys_plan_restriction_childs",
      dataTableDataKey: "id",
      ...dataTableColumnsDet1,
    },
  ];
  return (
    <>
      <GenericListPage
        id="sysplan"
        appTitle={capitalize(t("IN18SYSPLANODEFAULT"))}
        appShowTopBar
        appRouteForm="/private/sys/sysplanform"
        appProgramId={ConstProgramUtil.cSysplanId}
        appDataTableDetColumns={detsColumns}
        appDataTableColumns={dataTableColumns}
        appServiceDefault={sysPlanService}
        appDataTableDataKey="id"
        appRowExpand
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

export default SysPlan;
