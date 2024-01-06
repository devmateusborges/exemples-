import { memo, useRef } from "react";
import { t } from "i18next";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import AppFieldNumber from "../../../components/toolkit-react/AppFieldNumber";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import IAppDet from "../../../components/toolkit-react/interface/IAppDet";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";
import { capitalize, formatDateTimeColumn } from "../../../utils/FuncUtil";
import GenericFormDet from "../../generics/GenericFormDet";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";

interface IAGerDeviceDet1Form extends IAppDet {}

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
      appField: "sigla_param",
      appHeader: capitalize(t("IN18SIGLAPARAMETRODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "valor_tx",
      appHeader: capitalize(t("IN18VALORTEXTODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "valor_dt",
      appHeader: capitalize(t("IN18VALORDATADEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "date",
      appExport: true,
    },
    {
      appField: "valor_nm",
      appHeader: capitalize(t("IN18VALORDATADEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "numeric",
      appExport: true,
    },
    {
      appField: "observacao",
      appHeader: capitalize(t("IN18SIGLAPARAMETRODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "log_user_ins",
      appHeader: capitalize(t("IN18OBSERVACAODEFAULT")),
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

const GerDeviceDet1Form: React.FC<IAGerDeviceDet1Form> = (
  props: IAGerDeviceDet1Form
) => {
  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_param",
      required: [true, "Sigla - Parametro is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "valor_tx",
      required: [true, "Valor Texto is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "valor_dt",
      required: [true, "Valor Data is required"],
      defaultValue: "",
      type: "date",
    },
    {
      fieldName: "valor_nm",
      required: [true, "Valor Numero is required"],
      defaultValue: "",
      type: "numeric",
    },
    {
      fieldName: "observacao",
      required: [true, "Observação is required"],
      defaultValue: "",
      type: "text",
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
        name="ger_device_param_childs"
        appGenericListOptions={{
          id: "gerdevicedet1",
          appHelpText: "Param",
          appProgramId: ConstProgramUtil.cGerdeviceId,
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
        <div className="p-0 md:p-2">
          <AppContainerFields>
            <AppFieldText
              appFormControl={formControl}
              name="sigla_param"
              appTitle={capitalize(t("IN18SIGLAPARAMETRODEFAULT"))}
              appHelpText="Sigla - Parametro Help"
            />
            <AppFieldText
              appFormControl={formControl}
              name="observacao"
              appTitle={capitalize(t("IN18SIGLAPARAMETRODEFAULT"))}
              appHelpText="Observação Help"
            />
            <AppFieldText
              appFormControl={formControl}
              name="valor_tx"
              appTitle={capitalize(t("IN18VALORTEXTODEFAULT"))}
              appHelpText="Valor Texto Help"
            />
            <AppFieldNumber
              appFormControl={formControl}
              name="valor_nm"
              appTitle={capitalize(t("IN18VALORNUMERODEFAULT"))}
              appHelpText="Valor Numero Help"
              appMinFractionDigits={6}
            />
            <AppFieldDate
              appFormControl={formControl}
              name="valor_dt"
              appTitle={capitalize(t("IN18VALORDATADEFAULT"))}
              appHelpText="Valor Data Help"
            />
          </AppContainerFields>
        </div>
      </GenericFormDet>
    </>
  );
};

export default memo(GerDeviceDet1Form);
