import { memo, useRef } from "react";
import { t } from "i18next";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import IAppDet from "../../../components/toolkit-react/interface/IAppDet";
import GerPessoaService from "../../../services/modules/ger/GerPessoaService";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";
import { capitalize, formatDateTimeColumn } from "../../../utils/FuncUtil";
import GenericFormDet from "../../generics/GenericFormDet";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";

const gerPessoaService = new GerPessoaService();

interface IAGerMarcaDet2Form extends IAppDet {}
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
      appField: "ger_pessoa_id_obj.nome",
      appHeader: capitalize(t("IN18PESSOANOMEDEFAULT")),
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

const GerMarcaDet2Form: React.FC<IAGerMarcaDet2Form> = (
  props: IAGerMarcaDet2Form
) => {
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "observacao",
      required: [true, "Observação"],
      maxValue: [250, "Maximum 250 characters for Observação"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "ger_pessoa_id",
      required: [true, "Pessoa is required"],
      defaultValue: "",
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
        name="ger_marca_pessoa_childs"
        appGenericListOptions={{
          id: "germarcadet2",
          appHelpText: "Pessoa",
          appProgramId: ConstProgramUtil.cGermarcaId,
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
            <AppFieldDropdownFk
              appFormControl={formControl}
              name="ger_pessoa_id"
              appTitle={capitalize(t("IN18PESSOANOMEDEFAULT"))}
              appHelpText="Pessoa Help"
              appOptionLabel="nome"
              appOptionValue="id"
              appDataKey="id"
              appServiceDefault={gerPessoaService}
              appServiceFilterId="id"
              appServiceFilterDescription="nome"
            />
          </AppContainerFields>
        </div>
      </GenericFormDet>
    </>
  );
};

export default memo(GerMarcaDet2Form);
