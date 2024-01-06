import { t } from "i18next";
import { capitalize } from "../../../utils/FuncUtil";
import IndCjdService from "../../../services/modules/ind/IndCjdService";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";
import GenericListPage from "../../generics/GenericListPage";

const indCjdService = new IndCjdService();

const IndCjd: React.FC = () => {
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
        appField: "nome_tecnico",
        appHeader: "Nome Técnico",
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

  const dataTableColumnsDet1 = {
    columns: [
      {
        appField: "id",
        appHeader: "ID",
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: true,
      },
      {
        appField: "ind_ftd_id_obj.nome",
        appHeader: "Indicador-Fonte de Dados de Ind/Rel - Nome",
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
      },
      {
        appField: "ind_ftd_id_obj.nome_tecnico",
        appHeader: "Indicador-Fonte de Dados de Ind/Rel - Nome Têcnico",
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
      },
    ],
  };

  const detsColumns = [
    {
      title: "Det 1",
      name: "ind_cjd_relac_ftd_childs",
      dataTableDataKey: "id",
      ...dataTableColumnsDet1,
    },
  ];

  return (
    <>
      <GenericListPage
        appTitle="IND-Conjuntos de Dados"
        appShowTopBar
        appRouteForm="/private/ind/indcjdform"
        appDataTableColumns={dataTableColumns}
        appDataTableDetColumns={detsColumns}
        appRowExpand
        appDataTableDataKey="id"
        appRefreshVisible
        appDeleteVisible
        appEditVisible
        appAddVisible
        appServiceDefault={indCjdService}
      />
    </>
  );
};

export default IndCjd;
