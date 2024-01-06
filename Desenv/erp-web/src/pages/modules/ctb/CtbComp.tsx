import { t } from "i18next";
import { capitalize, formatDateTimeColumn } from "../../../utils/FuncUtil";

import useDebounce from "../../../components/toolkit-react/hooks/useDebounce";
import CtbCompService from "../../../services/modules/ctb/CtbCompService";
import { apiParamsConvert } from "../../../utils/ApiUtil";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";
import GenericListPage from "../../generics/GenericListPage";

const ctbCompService = new CtbCompService();

const CtbComp: React.FC = () => {
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
        appField: "sigla_comp",
        appHeader: capitalize(t("IN18COMPONENTESIGLADEFAULT")),
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
        appField: "fator_calc_origem",
        appHeader: capitalize(t("IN18FATORCALCULOORIGEMDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "numeric",
      },
      {
        appField: "ger_umedida_id_obj.sigla_umedida",
        appHeader: capitalize(t("IN18UMEDIDASIGLADEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "ger_umedida_id_obj.nome",
        appHeader: capitalize(t("IN18UMEDIDANOMEDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "ctb_comp_grupo_id_obj.sigla_comp_grupo",
        appHeader: capitalize(t("IN18GRUPODOCOMPONENTESIGLADEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "ctb_comp_grupo_id_obj.nome",
        appHeader: capitalize(t("IN18GRUPODOCOMPONENTENOMEDEFAULT")),
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

  return (
    <>
      <GenericListPage
        id="ctbcomp"
        appTitle={capitalize(t("IN18CTBCOMPONENTEDEFAULT"))}
        appShowTopBar
        appRouteForm="/private/ctb/ctbcompform"
        appDataTableColumns={dataTableColumns}
        appDataTableDataKey="id"
        appRefreshVisible
        appDeleteVisible
        appEditVisible
        appAddVisible
        appServiceDefault={ctbCompService}
        appProgramId={ConstProgramUtil.cCtbcompId}
        appButtonDeleteVisibleRow
        appButtonEditVisibleRow
        appPreferenceVisible
        appFavoriteVisible
      />
    </>
  );
};

export default CtbComp;
