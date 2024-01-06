import { memo, useRef } from "react";
import { t } from "i18next";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import IAppDet from "../../../components/toolkit-react/interface/IAppDet";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";
import { capitalize, formatDateTimeColumn } from "../../../utils/FuncUtil";
import GenericFormDet from "../../generics/GenericFormDet";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";

interface IAGerItemservDet3Form extends IAppDet {}
export const dataTableColumnsDet3: IAppDataTableColumns = {
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
      appField: "sigla_ger_itemserv_lote",
      appHeader: capitalize(t("IN18LOTESIGLADEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
    },
    {
      appField: "ativo_obj.description",
      appHeader: capitalize(t("IN18ATIVODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
    },
    {
      appField: "observacao",
      appHeader: capitalize(t("IN18OBSERVACAODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
    },
    {
      appField: "data_ini",
      appHeader: capitalize(t("IN18DATAINICIALDEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "date",
    },
    {
      appField: "data_fin",
      appHeader: capitalize(t("IN18DATAFINALDEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "date",
    },
    {
      appField: "data_validade",
      appHeader: capitalize(t("IN18DATAINICIALDEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "date",
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
const GerItemservDet3Form: React.FC<IAGerItemservDet3Form> = (
  props: IAGerItemservDet3Form
) => {
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_ger_itemserv_lote",
      required: [true, "Sigla lote is required"],
      maxValue: [100, "Maximum 100 characters for Sigla"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "observacao",
      required: [true, "Observação is required"],
      maxValue: [250, "Maximum 250 characters for Observação"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "data_ini",
      required: [true, "Data inicial de barra is required"],
      defaultValue: "",
      type: "date",
    },
    {
      fieldName: "data_fin",
      required: [true, "Data final de barra is required"],
      defaultValue: "",
      type: "date",
    },
    {
      fieldName: "data_validade",
      required: [true, "Data de validade de barra is required"],
      defaultValue: "",
      type: "date",
    },

    {
      fieldName: "ativo",
      required: [false, ""],
      defaultValue: "S",
      type: "checkbox",
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
        name="ger_itemserv_lote_childs"
        appGenericListOptions={{
          id: "geritemservdet3",
          appHelpText: "Lote",
          appProgramId: ConstProgramUtil.cGeritemservId,
          appDataTableColumns: dataTableColumnsDet3,
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
          appAddActionCode: "ADD_DET2",
          appEditActionCode: "EDIT_DET2",
          appDeleteActionCode: "DELETE_DET2",
          appSaveActionCode: "SAVE_DET2",
        }}
        appGenericFormOptions={{
          appFormControl: formControl,
        }}
      >
        <div className="p-0 md:p-2">
          <AppContainerFields>
            <AppFieldText
              appFormControl={formControl}
              name="sigla_ger_itemserv_lote"
              appTitle={capitalize(t("IN18LOTESIGLADEFAULT"))}
              appHelpText="Sigla lote Help"
            />
            <AppFieldText
              appFormControl={formControl}
              name="observacao"
              appTitle={capitalize(t("IN18OBSERVACAODEFAULT"))}
              appHelpText="Observação Help"
            />
            <AppFieldDate
              appFormControl={formControl}
              name="data_ini"
              appTitle={capitalize(t("IN18DATAINICIALDEFAULT"))}
              appHelpText="Data inicial de barra Help"
            />
            <AppFieldDate
              appFormControl={formControl}
              name="data_fin"
              appTitle={capitalize(t("IN18DATAFINALDEFAULT"))}
              appHelpText="Data final de barra Help"
            />
            <AppFieldDate
              appFormControl={formControl}
              name="data_validade"
              appTitle={capitalize(t("IN18DATAVALIDADEDEFAULT"))}
              appHelpText="Data de validade de barra Help"
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
          </AppContainerFields>
        </div>
      </GenericFormDet>
    </>
  );
};

export default memo(GerItemservDet3Form);
