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
import GerPessoaService from "../../../services/modules/ger/GerPessoaService";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";
import { capitalize, formatDateTimeColumn } from "../../../utils/FuncUtil";
import GenericFormDet from "../../generics/GenericFormDet";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";

const gerPessoaService = new GerPessoaService();

interface IAGerItemservDet4Form extends IAppDet {}
export const dataTableColumnsDet4: IAppDataTableColumns = {
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
      appField: "cod_itemserv_ext",
      appHeader: capitalize(t("IN18CODIGOEXTERNOITEM/SERVICODAPESSOADEFAULT")),
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
      appField: "ativo_obj.description",
      appHeader: capitalize(t("IN18ATIVODEFAULT")),
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
const GerItemservDet4Form: React.FC<IAGerItemservDet4Form> = (
  props: IAGerItemservDet4Form
) => {
  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "cod_itemserv_ext",
      required: [true, "Código Externo Item/Serviço da Pessoa is required"],
      maxValue: [
        50,
        "Maximum 50 characters for Código Externo Item/Serviço da Pessoa",
      ],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "ger_pessoa_id",
      required: [true, "GER-Pessoa is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "ger_pessoa_id_obj",
      required: [false, ""],
      defaultValue: "",
      type: "foreignkey",
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
        name="ger_itemserv_pessoa_childs"
        appGenericListOptions={{
          id: "geritemservdet4",
          appHelpText: "Pessoa",
          appProgramId: ConstProgramUtil.cGeritemservId,
          appDataTableColumns: dataTableColumnsDet4,
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
          appAddActionCode: "ADD_DET3",
          appEditActionCode: "EDIT_DET3",
          appDeleteActionCode: "DELETE_DET3",
          appSaveActionCode: "SAVE_DET3",
        }}
        appGenericFormOptions={{
          appFormControl: formControl,
        }}
      >
        <div className="p-0 md:p-2">
          <AppContainerFields>
            <AppFieldText
              appFormControl={formControl}
              name="cod_itemserv_ext"
              appTitle={capitalize(
                t("IN18CODIGOEXTERNOITEM/SERVICODAPESSOADEFAULT")
              )}
              appHelpText="Código Externo Item/Serviço da Pessoa Help"
            />
            <AppFieldDropdownFk
              appFormControl={formControl}
              name="ger_pessoa_id"
              appTitle={capitalize(t("IN18PESSOANOMEDEFAULT"))}
              appHelpText="GER-Pessoa Help"
              appOptionLabel="nome"
              appOptionValue="id"
              appDataKey="id"
              appServiceDefault={gerPessoaService}
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
          </AppContainerFields>
        </div>
      </GenericFormDet>
    </>
  );
};

export default memo(GerItemservDet4Form);
