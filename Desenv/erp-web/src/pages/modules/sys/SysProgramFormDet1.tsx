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
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import SysProgramService from "../../../services/modules/sys/SysProgramService";
import AppFieldNumber from "../../../components/toolkit-react/AppFieldNumber";
import SysRestrictionService from "../../../services/modules/sys/SysRestrictionService";
import SysActionService from "../../../services/modules/sys/SysAction";

const sysActionService = new SysActionService();

interface IASysProgramDet1Form extends IAppDet {}

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
      appField: "sys_action_id_obj.code",
      appHeader: capitalize(t("IN18CODIGODAACAODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "sys_action_id_obj.name",
      appHeader: capitalize(t("IN18SISTEMADEACAONOMEDEFAULT")),
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

// ==============================
const sysProgramDet1Form: React.FC<IASysProgramDet1Form> = (
  props: IASysProgramDet1Form
) => {
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sys_action_id",
      required: [true, "Sistem-Ação is required"],
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
        name="sys_program_action_childs"
        appGenericListOptions={{
          id: "sysprogramactiondet1",
          appHelpText: "Sistema Progama Help",
          appDataTableColumns: dataTableColumnsDet1,
          appProgramId: ConstProgramUtil.cSysprogramId,
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
            <AppFieldDropdownFk
              appFormControl={formControl}
              appServiceDefault={sysActionService}
              name="sys_action_id"
              appTitle={capitalize(t("IN18SISTEMADEACAONOMEDEFAULT"))}
              appHelpText="Sistem-Ação Help"
              appDataKey="id"
              appOptionValue="id"
              appServiceFilterId="id"
              appOptionLabel="code"
              appServiceFilterDescription="code"
            />
          </AppContainerFields>
        </div>
      </GenericFormDet>
    </>
  );
};

export default memo(sysProgramDet1Form);
