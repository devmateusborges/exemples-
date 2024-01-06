import { memo, useRef } from "react";
import { t } from "i18next";
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

interface IAGerPaisDet1Form extends IAppDet {}
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
      appField: "sigla_uf",
      appHeader: capitalize(t("IN18UFSIGLADEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
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
      appField: "nr_uf",
      appHeader: capitalize(t("IN18NUMEROUFDEFAULT")),
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

const GerPaisDet1Form: React.FC<IAGerPaisDet1Form> = (
  props: IAGerPaisDet1Form
) => {
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_uf",
      required: [true, "Sigla"],
      maxValue: [50, "Maximum 50 characters for Sigla"],
      defaultValue: "",
    },
    {
      fieldName: "nome",
      required: [true, "Nome is required"],
      maxValue: [100, "Maximum 100 characters for Nome"],
      defaultValue: "",
    },
    {
      fieldName: "nr_uf",
      required: [true, "Número UF is required"],
      maxValue: [50, "Maximum 50 characters for Número UF"],
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
        name="ger_uf_childs"
        appGenericListOptions={{
          id: "gerufdet1",
          appHelpText: "UF",
          appProgramId: ConstProgramUtil.cGerpaisId,
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
            name="sigla_uf"
            appTitle={capitalize(t("IN18UFSIGLADEFAULT"))}
            appHelpText="Sigla Help"
          />
          <AppFieldText
            appFormControl={formControl}
            name="nome"
            appTitle={capitalize(t("IN18NOMEDEFAULT"))}
            appHelpText="Nome Help"
          />
          <AppFieldText
            appFormControl={formControl}
            name="nr_uf"
            appTitle={capitalize(t("IN18NUMEROUFDEFAULT"))}
            appHelpText="Número País Help"
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

export default memo(GerPaisDet1Form);
