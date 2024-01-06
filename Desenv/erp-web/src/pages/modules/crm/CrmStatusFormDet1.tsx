import { t } from "i18next";
import { memo, useLayoutEffect, useState } from "react";
import AppFieldDropdown from "../../../components/toolkit-react/AppFieldDropdown";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import IAppDet from "../../../components/toolkit-react/interface/IAppDet";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";
import { capitalize } from "../../../utils/FuncUtil";
import GenericFormDet from "../../generics/GenericFormDet";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";
import AppFieldNumber from "../../../components/toolkit-react/AppFieldNumber";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import CrmStatusService from "../../../services/modules/crm/CrmStatusService";

const sysTypeDescriptionService = new SysTypeDescriptionService();
const crmStatusService = new CrmStatusService();
interface IACrmStatusProxDet1Form extends IAppDet {}

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
      appField: "ordem",
      appHeader: capitalize(t("IN18ORDEMDEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "numeric",
      appExport: true,
    },
    {
      appField: "tipo_status_ant",
      appHeader: capitalize(t("IN18STATUSDEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appHidden: false,
      appExport: true,
    },
    {
      appField: "crm_status_id_prox_obj.sigla_status",
      appHeader: capitalize(t("IN18TIPOSTATUSDEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appHidden: false,
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

// ==============================
const crmStatusProxDet1Form: React.FC<IACrmStatusProxDet1Form> = (
  props: IACrmStatusProxDet1Form
) => {
  // ==============================

  const [Tipo_status_ant_opt, setTipo_status_ant_opt] = useState([]);

  // ==============================

  useLayoutEffect(() => {
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "crm_status_prox",
        "tipo_status_ant"
      );
      setTipo_status_ant_opt(res);
    })();
  }, []);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "ordem",
      required: [true, "Ordem is required"],
      defaultValue: "",
      type: "numeric",
      maxValue: [50, "Maximum 50 for valor"],
    },
    {
      fieldName: "tipo_status_ant",
      required: [true, "Tipo Status Anterior is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "crm_status_id_prox",
      required: [true, "Status is required"],
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
        name="crm_status_prox_childs"
        appGenericListOptions={{
          id: "crmstatusproxdet1",
          appHelpText: "crm_status_prox_childs",
          appDataTableColumns: dataTableColumnsDet1,
          appProgramId: ConstProgramUtil.cCrmstatusId,
          appDataTableDataValue: props.appDataTableDataValue,
          appDataTablePaginateMode: "local",
          appShowTopBar: true,
          appRefreshVisible: true,
          appAddVisible: true,
          appDeleteVisible: true,
          appButtonDeleteVisibleRow: true,
          appButtonEditVisibleRow: true,
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
              name="ordem"
              appTitle={capitalize(t("IN18ORDEMDEFAULT"))}
              appHelpText="Sigla do Grupo de Classificação"
            />
            <AppFieldDropdown
              appFormControl={formControl}
              name="tipo_status_ant"
              appTitle={capitalize(t("IN18TIPOSTATUSDEFAULT"))}
              appOptions={Tipo_status_ant_opt}
              appHelpText="Tipo Status Help"
              appOptionLabel="description_type"
              appOptionValue="value_type"
            />
            <AppFieldDropdownFk
              appFormControl={formControl}
              appServiceDefault={crmStatusService}
              name="crm_status_id_prox"
              appTitle={capitalize(
                t("IN18ATENDIMENTOSTATUSPROXIMOSILGLADEFAULT")
              )}
              appHelpText="Atendimento-Status próximo Help"
              appDataKey="id"
              appOptionValue="id"
              appServiceFilterId="id"
              appOptionLabel="sigla_status"
              appServiceFilterDescription="sigla_status"
            />
          </AppContainerFields>
        </div>
      </GenericFormDet>
    </>
  );
};

export default memo(crmStatusProxDet1Form);
