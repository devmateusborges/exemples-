import { t } from "i18next";
import { capitalize } from "../../../utils/FuncUtil";
import OpeAtividadeService from "../../../services/modules/ope/OpeAtividadeService";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";
import GenericListPage from "../../generics/GenericListPage";
import { dataTableColumnsDet1 } from "./OpeAtividadeDet1Form";

const opeAtividadeService = new OpeAtividadeService();

const OpeAtividade: React.FC = () => {
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
        appField: "sigla_atividade",
        appHeader: capitalize(t("IN18ATIVIDADESIGLADEFAULT")),
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
        appField: "parada_obj.description",
        appHeader: capitalize(t("IN18PARADADEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "index_bor",
        appHeader: capitalize(t("IN18INDEXATIVIDADEBORDODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "largura",
        appHeader: capitalize(t("IN18QUANTIDADELARGURADEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "valida_seq_medicao_trab_centro_obj.description",
        appHeader: capitalize(t("IN18VALIDASEQUENCIAMEDICAODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "valida_saldo_area_aberta_obj.description",
        appHeader: capitalize(t("IN18VALIDASALDOAREAEMABERTODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "valida_prev_itemserv_obj.description",
        appHeader: capitalize(t("IN18VALIDAPREVISAOITEM/SERVICODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "valida_prev_rec_obj.description",
        appHeader: capitalize(t("IN18VALIDAPREVISAORECURSODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "valida_regra_config_obj.description",
        appHeader: capitalize(t("IN18VALIDAREGRACONFIGURAVELDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "valida_tipo_executor_obj.description",
        appHeader: capitalize(t("IN18VALIDATIPOEXECUTORDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "valida_rec_equip_obj.description",
        appHeader: capitalize(t("IN18OBRIGARECURSODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "valida_rec_pessoa_obj.description",
        appHeader: capitalize(t("IN18OBRIGARECURSOPESSOADEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "valida_itemserv_i_obj.description",
        appHeader: capitalize(t("IN18OBRIGAITEMDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "valida_itemserv_s_obj.description",
        appHeader: capitalize(t("IN18OBRIGASERVICODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "valida_tipo_prop_rec_equip_obj.description",
        appHeader: capitalize(t("IN18VALIDATIPOPROPRECURSODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "valida_tipo_prop_rec_pessoa_obj.description",
        appHeader: capitalize(t("IN18VALIDATIPOPROPPESSOADEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "valida_tot_area_acum_per_centro_plan_obj.description",
        appHeader: capitalize(t("IN18PLANEJAMENTODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "valida_tot_area_acum_per_centro_exec_obj.description",
        appHeader: capitalize(t("IN18EXECUCAODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "valida_tot_area_ord_exec_obj.description",
        appHeader: capitalize(t("IN18VALIDATOTALDEAREA/PRODDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
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
        appField: "ope_atividade_grupo_id_obj.sigla_atividade_grupo",
        appHeader: capitalize(t("IN18GRUPODEATIVIDADESIGLADEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "ope_atividade_grupo_id_obj.nome",
        appHeader: capitalize(t("IN18GRUPODEATIVIDADENOMEDEFAULT")),
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
      title: "Operação-Relacionamento de Atividade Produtivas",
      name: "ope_atividade_relac_prod_childs",
      dataTableDataKey: "id",
      ...dataTableColumnsDet1,
    },
  ];

  return (
    <>
      <GenericListPage
        id="opeatividade"
        appTitle={capitalize(t("IN18OPEATIVIDADEDEFAULT"))}
        appProgramId={ConstProgramUtil.cOpeatividadeId}
        appRouteForm="/private/ope/opeatividadeform"
        appDataTableColumns={dataTableColumns}
        appDataTableDetColumns={detsColumns}
        appServiceDefault={opeAtividadeService}
        appDataTableDataKey="id"
        appShowTopBar
        appRowExpand
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

export default OpeAtividade;
