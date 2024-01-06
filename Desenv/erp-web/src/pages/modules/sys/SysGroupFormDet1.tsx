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
import SysGroupService from "../../../services/modules/sys/SysGroupService";
import SysProgramService from "../../../services/modules/sys/SysProgramService";

const sysProgramService = new SysProgramService();

interface IASysGroupDet1Form extends IAppDet {}

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
      appField: "sys_program_id_obj.code_program",
      appHeader: capitalize(t("IN18SISTEMAPROGRAMASIGLADEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "sys_program_id_obj.name",
      appHeader: capitalize(t("IN18SISTEMAPROGRAMANOMEDEFAULT")),
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
const sysGroupDet1Form: React.FC<IASysGroupDet1Form> = (
  props: IASysGroupDet1Form
) => {
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sys_program_id",
      required: [true, ""],
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
        name="sys_group_program_childs"
        appGenericListOptions={{
          id: "sysgroupprogramdet1",
          appHelpText: "Det 1",
          appDataTableColumns: dataTableColumnsDet1,
          appProgramId: ConstProgramUtil.cSysgroupId,
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
              appServiceDefault={sysProgramService}
              name="sys_program_id"
              appTitle={capitalize(t("IN18SISTEMAPROGRAMASIGLADEFAULT"))}
              appHelpText="System-Programa Help"
              appDataKey="id"
              appOptionValue="id"
              appServiceFilterId="id"
              appOptionLabel="code_program"
              appServiceFilterDescription="code_program"
            />
          </AppContainerFields>
        </div>
      </GenericFormDet>
    </>
  );
};

export default memo(sysGroupDet1Form);
