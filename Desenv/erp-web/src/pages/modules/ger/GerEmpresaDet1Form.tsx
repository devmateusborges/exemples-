import { memo, useLayoutEffect, useRef, useState } from "react";
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
import AppFieldDropdown from "../../../components/toolkit-react/AppFieldDropdown";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";

const gerPessoaService = new GerPessoaService();

interface IAEmpresaDet1Form extends IAppDet {}
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
      appField: "tipo",
      appHeader: capitalize(t("IN18TIPODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "ger_pessoa_id_obj.nome",
      appHeader: capitalize(t("IN18PESSOANOMEDEFAULT")),
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
const sysTypeDescriptionService = new SysTypeDescriptionService();

const gerEmpresaDet1Form: React.FC<IAEmpresaDet1Form> = (
  props: IAEmpresaDet1Form
) => {
  const [tipo_opt, setTipo_opt] = useState([]);
  // ==============================

  useLayoutEffect(() => {
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ger_empresa_pessoa",
        "tipo"
      );
      setTipo_opt(res);
    })();
  }, []);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "observacao",
      required: [true, "Observação is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "tipo",
      required: [true, "Tipo is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "ger_pessoa_id",
      required: [true, "Pessoa is required"],
      defaultValue: "",
      type: "foreignkey",
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
        name="ger_empresa_pessoa_childs"
        appGenericListOptions={{
          id: "gerempresadet1",
          appHelpText: "ger_empresa_pessoa_childs",
          appProgramId: ConstProgramUtil.cGerempresaId,
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
            <AppFieldDropdown
              appFormControl={formControl}
              name="tipo"
              appTitle={capitalize(t("IN18TIPODEFAULT"))}
              appOptions={tipo_opt}
              appHelpText="Tipo Help"
              appOptionLabel="description_type"
              appOptionValue="value_type"
            />
          </AppContainerFields>
        </div>
      </GenericFormDet>
    </>
  );
};

export default memo(gerEmpresaDet1Form);
