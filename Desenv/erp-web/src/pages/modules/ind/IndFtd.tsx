import { capitalize } from "lodash";
import { t } from "i18next";
import IndFtdService from "../../../services/modules/ind/IndFtdService";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";
import GenericListPage from "../../generics/GenericListPage";

const indFtdService = new IndFtdService();

const IndFtd: React.FC = () => {
  const dataTableColumns: IAppDataTableColumns = {
    columns: [
      {
        appField: "id",
        appHeader: "ID",
        appSortable: false,
        appFilter: false,
        appFilterMatch: "contains",
        appFilterGlobal: false,
        appHidden: true,
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
        appField: "config_ftd",
        appHeader: "Configuração SQL,Etc (JSON)",
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
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
        appField: "ind_cnd_id_obj.sigla_ind_cnd",
        appHeader: "Conexão - Sigla",
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
      },
      {
        appField: "ind_cnd_id_obj.nome",
        appHeader: "Conexão - Nome",
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
      },
      {
        appField: "log_user_ins",
        appHeader: "Usuário de Inserção",
        appSortable: false,
        appFilter: false,
        appFilterMatch: "contains",
        appFilterGlobal: false,
        appHidden: true,
      },
      {
        appField: "log_date_ins",
        appHeader: "Data de Inserção",
        appSortable: false,
        appFilter: false,
        appFilterMatch: "contains",
        appFilterGlobal: false,
        appHidden: true,
      },
      {
        appField: "log_date_upd",
        appHeader: "Data de Alteração",
        appSortable: false,
        appFilter: false,
        appFilterMatch: "contains",
        appFilterGlobal: false,
        appHidden: true,
      },
      {
        appField: "log_user_upd",
        appHeader: "Usuário de Alteração",
        appSortable: false,
        appFilter: false,
        appFilterMatch: "contains",
        appFilterGlobal: false,
        appHidden: true,
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
        appField: "ind_prm_id_obj.nome",
        appHeader: "Indicador-Parametros de Ind/Rel - Nome",
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
      },
      {
        appField: "ind_prm_id_obj.nome_tecnico",
        appHeader: "Indicador-Parametros de Ind/Rel - Nome têcnico",
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
      name: "ind_ftd_relac_prm_childs",
      dataTableDataKey: "id",
      ...dataTableColumnsDet1,
    },
  ];
  return (
    <>
      <GenericListPage
        appTitle="IND-Fonte de Dados"
        appShowTopBar
        appRouteForm="/private/ind/indftdform"
        appDataTableColumns={dataTableColumns}
        appDataTableDetColumns={detsColumns}
        appRowExpand
        appDataTableDataKey="id"
        appRefreshVisible
        appDeleteVisible
        appEditVisible
        appAddVisible
        appServiceDefault={indFtdService}
      />
    </>
  );
};

export default IndFtd;
