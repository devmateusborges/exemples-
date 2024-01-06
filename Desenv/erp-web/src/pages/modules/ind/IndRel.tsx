import { t } from "i18next";
import { capitalize } from "../../../utils/FuncUtil";
import IndRelService from "../../../services/modules/ind/IndRelService";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";
import GenericListPage from "../../generics/GenericListPage";

const indRelService = new IndRelService();

const IndRel: React.FC = () => {
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
        appField: "tipo_obj.description",
        appHeader: "Tipo",
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
      },
      {
        appField: "ind_ftd_id_obj.nome_tecnico",
        appHeader: "Fonte de Dados - Nome Técnico",
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
      },
      {
        appField: "ind_ftd_id_obj.nome",
        appHeader: "Fonte de Dados - Nome",
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
      },

      {
        appField: "ind_cjd_id_obj.nome_tecnico",
        appHeader: "Nome Técnico - Conjunto Dados",
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
      },
      {
        appField: "ind_cjd_id_obj.nome",
        appHeader: "Conjunto Dados - Nome",
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
        appField: "var_nome_tecnico",
        appHeader: "Nome da Variável - Técnico",
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
      },
      {
        appField: "var_nome_descritivo",
        appHeader: "Nome da Variável - Descritivo",
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
      },
      {
        appField: "var_agrupavel_obj.description",
        appHeader: "Agrupável",
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
      },
      {
        appField: "ordem_padrao",
        appHeader: "Ordem Padrão",
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
      },
      {
        appField: "largura",
        appHeader: "Largura",
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
      },
      {
        appField: "visivel_obj.description",
        appHeader: "Visível",
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
      name: "ind_rel_var_childs",
      dataTableDataKey: "id",
      ...dataTableColumnsDet1,
    },
  ];

  return (
    <>
      <GenericListPage
        appTitle="IND-Relatórios"
        appShowTopBar
        appRouteForm="/private/ind/indrelform"
        appDataTableColumns={dataTableColumns}
        appDataTableDetColumns={detsColumns}
        appRowExpand
        appDataTableDataKey="id"
        appRefreshVisible
        appDeleteVisible
        appEditVisible
        appAddVisible
        appServiceDefault={indRelService}
      />
    </>
  );
};

export default IndRel;
