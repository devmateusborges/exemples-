import { t } from "i18next";
import { capitalize } from "../../../utils/FuncUtil";
import FisCestService from "../../../services/modules/fis/FisCestService";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";
import GenericListPage from "../../generics/GenericListPage";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";
import { dataTableColumnsDet1 } from "./FisCestFormDet1";

const fisCestService = new FisCestService();

const FisCest: React.FC = () => {
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
        appField: "nr_cest",
        appHeader: capitalize(t("IN18NUMEROCESTDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
      },
      {
        appField: "data_validade",
        appHeader: capitalize(t("IN18DATAVALIDADEDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
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
      name: "fis_cest_ncm_childs",
      dataTableDataKey: "id",
      ...dataTableColumnsDet1,
    },
  ];

  return (
    <>
      <GenericListPage
        id="fiscest"
        appTitle={capitalize(t("IN18FISCESTDEFAULT"))}
        appShowTopBar
        appRouteForm="/private/fis/fiscestform"
        appProgramId={ConstProgramUtil.cFiscestId}
        appDataTableDetColumns={detsColumns}
        appDataTableColumns={dataTableColumns}
        appServiceDefault={fisCestService}
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

export default FisCest;
