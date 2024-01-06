import { t } from "i18next";
import { memo, useRef } from "react";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import IAppDet from "../../../components/toolkit-react/interface/IAppDet";
import FinBancoService from "../../../services/modules/fin/FinBancoService";
import OpeAtividadeService from "../../../services/modules/ope/OpeAtividadeService";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";
import { capitalize, formatDateTimeColumn } from "../../../utils/FuncUtil";
import GenericFormDet from "../../generics/GenericFormDet";

interface IAGerPessoaDet1Form extends IAppDet {}
const opeAtividadeService = new OpeAtividadeService();
// ==============================
export const dataTableColumnsDet1: IAppDataTableColumns = {
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
    },
    {
      appField: "ordem_visual",
      appHeader: capitalize(t("IN18ORDEMVISUALIZACAODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
    },
    {
      appField: "ope_atividade_id_prod_obj.sigla_atividade",
      appHeader: capitalize(t("IN18USUARIODEINSERCAODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
    },
    {
      appField: "ope_atividade_id_prod_obj.nome",
      appHeader: capitalize(t("IN18ATIVIDADEPRODNOMEDEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
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
// ==============================

const GerPessoaDet1Form: React.FC<IAGerPessoaDet1Form> = (
  props: IAGerPessoaDet1Form
) => {
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "ordem_visual",
      required: [true, "Ordem Visualização is required"],
      maxValue: [1, "Maximum 1 characters for Ordem Visualização"],
      defaultValue: "",
    },
    {
      fieldName: "ope_atividade_id_prod",
      required: [true, "Atividade Prod is required"],
      defaultValue: "",
    },
  ];
  // ==============================

  const formControl = useFormControl({
    fieldControls,
  });
  // ==============================

  return (
    <>
      <GenericFormDet
        ref={props.appRef}
        name="ope_atividade_relac_prod_childs"
        appGenericListOptions={{
          id: "opeatividaderelacproddet1",
          appHelpText: "Operação-Relacionamento de Atividade Produtivas",
          appProgramId: ConstProgramUtil.cOpeatividadeId,
          appDataTableColumns: dataTableColumnsDet1,
          appDataTableDataValue: props.appDataTableDataValue,
          appDataTablePaginateMode: "local",
          appShowTopBar: true,
          appRefreshVisible: true,
          appAddVisible: true,
          appDeleteVisible: true,
          appEditVisible: true,
          appButtonDeleteVisibleRow: true,
          appButtonEditVisibleRow: true,
          appPreferenceVisible: true,
          appAddActionCode: "ADD_DET0",
          appEditActionCode: "EDIT_DET0",
          appDeleteActionCode: "DELETE_DET0",
          appSaveActionCode: "SAVE_DET0",
        }}
        appGenericFormOptions={{
          appFormControl: formControl,
        }}
      >
        <div className="grid m-0">
          <AppFieldText
            appFormControl={formControl}
            name="ordem_visual"
            appTitle={capitalize(t("IN18ORDEMVISUALIZACAODEFAULT"))}
            appHelpText="Ordem Visualização Help"
          />

          <AppFieldDropdownFk
            appFormControl={formControl}
            name="ope_atividade_id_prod"
            appTitle={capitalize(t("IN18ATIVIDADEPRODNOMEDEFAULT"))}
            appHelpText="Atividade Prod Help"
            appOptionLabel="nome"
            appOptionValue="id"
            appDataKey="id"
            appServiceDefault={opeAtividadeService}
            appServiceFilterId="id"
            appServiceFilterDescription="sigla_atividade"
          />
        </div>
      </GenericFormDet>
    </>
  );
};

export default memo(GerPessoaDet1Form);
