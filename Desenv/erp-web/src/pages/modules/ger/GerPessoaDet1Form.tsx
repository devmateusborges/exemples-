import { memo, useRef } from "react";
import { t } from "i18next";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import IAppDet from "../../../components/toolkit-react/interface/IAppDet";
import FinBancoService from "../../../services/modules/fin/FinBancoService";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";
import { capitalize, formatDateTimeColumn } from "../../../utils/FuncUtil";
import GenericFormDet from "../../generics/GenericFormDet";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";

const finBancoService = new FinBancoService();

interface IAGerPessoaDet1Form extends IAppDet {}
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
      appExport: true,
    },
    {
      appField: "agencia",
      appHeader: capitalize(t("IN18AGENCIADEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "conta",
      appHeader: capitalize(t("IN18CONTADEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "observacao",
      appHeader: capitalize(t("IN18OBSERVACAODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "fin_banco_id_obj.nome",
      appHeader: capitalize(t("IN18BANCONOMEDEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
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

const GerPessoaDet1Form: React.FC<IAGerPessoaDet1Form> = (
  props: IAGerPessoaDet1Form
) => {
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "agencia",
      required: [true, "Agencia is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 characters for agencia"],
    },
    {
      fieldName: "conta",
      required: [true, "Conta is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 characters for conta"],
    },
    {
      fieldName: "observacao",
      required: [true, "Observação is required"],
      defaultValue: "",
      type: "text",
      maxValue: [250, "Maximum 250 characters for observacao"],
    },
    {
      fieldName: "fin_banco_id",
      required: [true, "FIN-Banco is required"],
      defaultValue: "",
    },
    {
      fieldName: "ativo",
      required: [false, ""],
      defaultValue: "S",
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
        name="ger_pessoa_conta_banco_childs"
        appGenericListOptions={{
          id: "gerpessoadet1",
          appHelpText: "Conta do Banco",
          appProgramId: ConstProgramUtil.cGerpessoaId,
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
            name="agencia"
            appTitle={capitalize(t("IN18AGENCIADEFAULT"))}
            appHelpText="Agencia Help"
          />
          <AppFieldText
            appFormControl={formControl}
            name="conta"
            appTitle={capitalize(t("IN18CONTADEFAULT"))}
            appHelpText="Conta Help"
          />
          <AppFieldText
            appFormControl={formControl}
            name="observacao"
            appTitle={capitalize(t("IN18OBSERVACAODEFAULT"))}
            appHelpText="Observação Help"
          />

          <AppFieldDropdownFk
            appFormControl={formControl}
            name="fin_banco_id"
            appTitle={capitalize(t("IN18BANCONOMEDEFAULT"))}
            appHelpText="FIN-Banco Help"
            appOptionLabel="nome"
            appOptionValue="id"
            appDataKey="id"
            appServiceDefault={finBancoService}
            appServiceFilterId="id"
            appServiceFilterDescription="nome"
          />
          <AppFieldCheck
            appFormControl={formControl}
            name="ativo"
            appTitle={capitalize(t("IN18ATIVODEFAULT"))}
            appHelpText="Ativo Help"
            appTrueValue="S"
            appTrueValueLabel="Sim"
            appFalseValue="N"
            appFalseValueLabel="Não"
          />
        </div>
      </GenericFormDet>
    </>
  );
};

export default memo(GerPessoaDet1Form);
