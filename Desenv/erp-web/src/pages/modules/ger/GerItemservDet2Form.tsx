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

interface IAGerItemservDet2Form extends IAppDet {}
export const dataTableColumnsDet2: IAppDataTableColumns = {
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
      appField: "desc_local1",
      appHeader: capitalize(t("IN18DESCRICAO1DEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "desc_local2",
      appHeader: capitalize(t("IN18DESCRICAO2DEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "desc_local3",
      appHeader: capitalize(t("IN18DESCRICAO3DEFAULT")),
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
const GerItemservDet2Form: React.FC<IAGerItemservDet2Form> = (
  props: IAGerItemservDet2Form
) => {
  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "observacao",
      required: [true, "Observação is required"],
      maxValue: [250, "Maximum 250 characters for Observação"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "desc_local1",
      required: [true, "Descrição 1 is required"],
      maxValue: [50, "Maximum 50 characters for Descrição 1"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "desc_local2",
      required: [true, "Descrição 2 is required"],
      maxValue: [100, "Maximum 100 characters for Descrição 2"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "desc_local3",
      required: [true, "Descrição 3 is required"],
      maxValue: [100, "Maximum 100 characters for Descrição 3"],
      defaultValue: "",
      type: "text",
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
        name="ger_itemserv_local_childs"
        appGenericListOptions={{
          id: "geritemservdet2",
          appHelpText: "Local",
          appProgramId: ConstProgramUtil.cGeritemservId,
          appDataTableColumns: dataTableColumnsDet2,
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
          appAddActionCode: "ADD_DET1",
          appEditActionCode: "EDIT_DET1",
          appDeleteActionCode: "DELETE_DET1",
          appSaveActionCode: "SAVE_DET1",
        }}
        appGenericFormOptions={{
          appFormControl: formControl,
        }}
      >
        <div className="p-0 md:p-2">
          <AppContainerFields>
            <AppFieldText
              appFormControl={formControl}
              name="observacao"
              appTitle={capitalize(t("IN18OBSERVACAODEFAULT"))}
              appHelpText="Observação Help"
            />

            <AppFieldText
              appFormControl={formControl}
              name="desc_local1"
              appTitle={capitalize(t("IN18DESCRICAO1DEFAULT"))}
              appHelpText="Descrição 1 Help"
            />

            <AppFieldText
              appFormControl={formControl}
              name="desc_local2"
              appTitle={capitalize(t("IN18DESCRICAO2DEFAULT"))}
              appHelpText="Descrição 2 Help"
            />

            <AppFieldText
              appFormControl={formControl}
              name="desc_local3"
              appTitle={capitalize(t("IN18DESCRICAO3DEFAULT"))}
              appHelpText="Descrição 3 Help"
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

export default memo(GerItemservDet2Form);
