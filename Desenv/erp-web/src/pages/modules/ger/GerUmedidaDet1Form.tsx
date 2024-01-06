import { memo, useRef } from "react";
import { t } from "i18next";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldNumber from "../../../components/toolkit-react/AppFieldNumber";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import IAppDet from "../../../components/toolkit-react/interface/IAppDet";
import GerUmedidaService from "../../../services/modules/ger/GerUmedidaService";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";
import { capitalize, formatDateTimeColumn } from "../../../utils/FuncUtil";
import GenericFormDet from "../../generics/GenericFormDet";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";

interface IAGerItemservDet1Form extends IAppDet {}
const gerUmedidaService = new GerUmedidaService();

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
      appField: "fator_mult",
      appHeader: capitalize(t("IN18FATORMULTIPLACAODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "numeric",
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
      appField: "ger_umedida_id_para_obj.sigla_umedida",
      appHeader: capitalize(t("IN18UMEDIDAPARASIGLADEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
    },
    {
      appField: "ger_umedida_id_para_obj.nome",
      appHeader: capitalize(t("IN18UMEDIDAPARANOMEDEFAULT")),
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

const GerItemservDet1Form: React.FC<IAGerItemservDet1Form> = (
  props: IAGerItemservDet1Form
) => {
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "fator_mult",
      required: [true, "Fator Multiplacao is required"],
      maxValue: [18, "Maximum 18 characters for Fator Multiplacao"],
      defaultValue: "",
      type: "numeric",
    },
    {
      fieldName: "ger_umedida_id_para",
      required: [true, "Para GER-Umedida is required"],
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
        name="ger_umedida_conv_childs"
        appGenericListOptions={{
          id: "gerumedidadet1",
          appHelpText: "Conversão",
          appProgramId: ConstProgramUtil.cGerumedidaId,
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
            <AppFieldNumber
              appFormControl={formControl}
              name="fator_mult"
              appTitle={capitalize(t("IN18FATORMULTIPLACAODEFAULT"))}
              appHelpText="Fator Multiplacao Help"
              appMinFractionDigits={6}
            />
            <AppFieldDropdownFk
              appFormControl={formControl}
              appServiceDefault={gerUmedidaService}
              name="ger_umedida_id_para"
              appTitle={capitalize(t("IN18UMEDIDAPARASIGLADEFAULT"))}
              appHelpText="Para GER-Umedida Help"
              appOptionLabel="sigla_umedida"
              appOptionValue="id"
              appDataKey="id"
              appServiceFilterId="id"
              appServiceFilterDescription="sigla_umedida"
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

export default memo(GerItemservDet1Form);
