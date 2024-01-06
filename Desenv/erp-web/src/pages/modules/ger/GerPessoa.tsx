import { t } from "i18next";
import { capitalize, formatDateTimeColumn } from "../../../utils/FuncUtil";
import GerPessoaService from "../../../services/modules/ger/GerPessoaService";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";
import GenericListPage from "../../generics/GenericListPage";
import { dataTableColumnsDet1 } from "./GerPessoaDet1Form";
import { dataTableColumnsDet2 } from "./GerPessoaDet2Form";

const gerPessoaService = new GerPessoaService();

const GerPessoa: React.FC = () => {
  // ==============================

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
        appField: "sigla_pes",
        appHeader: capitalize(t("IN18PESSOASIGLADEFAULT")),
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
        appField: "razao_social",
        appHeader: capitalize(t("IN18RAZAOSOCIALDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "doc_cnpj",
        appHeader: capitalize(t("IN18DOCUMENTOCNPJDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "doc_cpf",
        appHeader: capitalize(t("IN18DOCUMENTOCPFDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "doc_ie",
        appHeader: capitalize(t("IN18DOCUMENTOIEDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "doc_im",
        appHeader: capitalize(t("IN18DOCUMENTOIMDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "doc_cnae",
        appHeader: capitalize(t("IN18DOCUMENTOCNAEDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "doc_junta",
        appHeader: capitalize(t("IN18DOCUMENTOJUNTACOMERCIALDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "doc_rg",
        appHeader: capitalize(t("IN18DOCUMENTORGDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "doc_crc",
        appHeader: capitalize(t("IN18DOCUMENTOCRCDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "doc_rg_org_exp",
        appHeader: capitalize(t("IN18DOCUMENTORGORGAOEXPEDIDORDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "doc_crc_seq",
        appHeader: capitalize(t("IN18DOCUMENTOCRCSEQUENCIADEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "doc_crc_org_exp",
        appHeader: capitalize(t("IN18DOCUMENTOCRCORGAOEXPEDIDORDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "doc_taf",
        appHeader: capitalize(t("IN18DOCUMENTOAFTDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "data_abertura",
        appHeader: capitalize(t("IN18DATAABERTURADEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "date",
        appExport: true,
      },
      {
        appField: "fis_regime",
        appHeader: capitalize(t("IN18REGIMEDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "fone_1",
        appHeader: capitalize(t("IN18TELEFONE1DEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "fone_2",
        appHeader: capitalize(t("IN18TELEFONE2DEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "fone_3",
        appHeader: capitalize(t("IN18TELEFONE3DEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "contato_1",
        appHeader: capitalize(t("IN18CONTATO1DEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "contato_2",
        appHeader: capitalize(t("IN18CONTATO2DEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "contato_3",
        appHeader: capitalize(t("IN18CONTATO3DEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "contrib_icms",
        appHeader: capitalize(t("IN18CONTRIBUICAOICMSDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "nr_rntrc",
        appHeader: capitalize(t("IN18NUMERORNTRCDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "nr_registro_est_cte",
        appHeader: capitalize(t("IN18NUMERODOREGISTROESTADUALDECTEDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "data_valid",
        appHeader: capitalize(t("IN18DATADEVALIDACAODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "date",
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

  // ==============================

  const detsColumns = [
    {
      title: "Conta do Banco",
      name: "ger_pessoa_conta_banco_childs",
      ...dataTableColumnsDet1,
    },
    {
      title: "Endereço",
      name: "ger_pessoa_endereco_childs",
      ...dataTableColumnsDet2,
    },
  ];
  // ==============================

  return (
    <>
      <GenericListPage
        id="gerpessoa"
        appTitle={capitalize(t("IN18GERPESSOADEFAULT"))}
        appShowTopBar
        appRouteForm="/private/ger/gerpessoaform"
        appProgramId={ConstProgramUtil.cGerpessoaId}
        appServiceDefault={gerPessoaService}
        appDataTableColumns={dataTableColumns}
        appDataTableDetColumns={detsColumns}
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

export default GerPessoa;
