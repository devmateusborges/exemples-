import { t } from "i18next";
import { capitalize } from "../../../utils/FuncUtil";
import CrmStatusService from "../../../services/modules/crm/CrmStatusService";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";
import GenericListPage from "../../generics/GenericListPage";
import { dataTableColumnsDet1 } from "./CrmStatusFormDet1";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";

const crmStatusService = new CrmStatusService();

const CrmStatus: React.FC = () => {
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
        appField: "sigla_status",
        appHeader: capitalize(t("IN18STATUSSIGLADEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
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
        appDataType: "text",
        appHidden: false,
      },
      {
        appField: "obrig_motivo_obj.description",
        appHeader: capitalize(t("IN18OBRIGAMOTIVODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
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
      name: "crm_status_prox_childs",
      dataTableDataKey: "id",
      ...dataTableColumnsDet1,
    },
  ];
  return (
    <>
      <GenericListPage
        id="crmstatus"
        appTitle={capitalize(t("IN18CRMSTATUSDEFAULT"))}
        appShowTopBar
        appRouteForm="/private/crm/crmstatusform"
        appProgramId={ConstProgramUtil.cCrmstatusId}
        appDataTableDetColumns={detsColumns}
        appDataTableColumns={dataTableColumns}
        appServiceDefault={crmStatusService}
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

export default CrmStatus;
