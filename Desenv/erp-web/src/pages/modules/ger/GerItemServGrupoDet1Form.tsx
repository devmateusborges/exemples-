import { memo, useRef } from "react";
import { t } from "i18next";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import IAppDet from "../../../components/toolkit-react/interface/IAppDet";
import CtbCompService from "../../../services/modules/ctb/CtbCompService";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";
import { capitalize, formatDateTimeColumn } from "../../../utils/FuncUtil";
import GenericFormDet from "../../generics/GenericFormDet";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";

const ctbCompService = new CtbCompService();

interface IAGerItemServGrupoDet1Form extends IAppDet {}
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
      appField: "sigla_ger_itemserv_subgrupo",
      appHeader: capitalize(t("IN18SUBGRUPOSIGLADEFAULTDEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
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
      appField: "ctb_comp_id_obj.nome",
      appHeader: capitalize(t("IN18COMPONENTENOMEDEFAULT")),
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

const GerItemServGrupoDet1Form: React.FC<IAGerItemServGrupoDet1Form> = (
  props: IAGerItemServGrupoDet1Form
) => {
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_ger_itemserv_subgrupo",
      required: [true, "Sigla - Subgrupo"],
      maxValue: [50, "Maximum 50 characters for Sigla"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "ctb_comp_id",
      required: [true, "CTB-Componente is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "nome",
      required: [true, "Nome is required"],
      maxValue: [100, "Maximum 100 characters for Nome"],
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
        name="ger_itemserv_subgrupo_childs"
        appGenericListOptions={{
          id: "geritemservsubgrupo",
          appHelpText: "Subgrupo",
          appProgramId: ConstProgramUtil.cGeritemservgrupoId,
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
              name="sigla_ger_itemserv_subgrupo"
              appTitle={capitalize(t("IN18SUBGRUPOSIGLADEFAULT"))}
              appHelpText="Sigla - Subgrupo Help"
            />
            <AppFieldText
              appFormControl={formControl}
              name="nome"
              appTitle={capitalize(t("IN18NOMEDEFAULT"))}
              appHelpText="Nome Help"
            />
            <AppFieldDropdownFk
              appFormControl={formControl}
              name="ctb_comp_id"
              appTitle={capitalize(t("IN18COMPONENTENOMEDEFAULT"))}
              appHelpText="CTB-Componente Help"
              appOptionLabel="nome"
              appOptionValue="id"
              appDataKey="id"
              appServiceDefault={ctbCompService}
              appServiceFilterId="id"
              appServiceFilterDescription="sigla_comp"
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

export default memo(GerItemServGrupoDet1Form);
