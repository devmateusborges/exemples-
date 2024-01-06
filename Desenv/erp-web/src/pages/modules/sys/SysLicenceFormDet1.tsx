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
import SysLicenceService from "../../../services/modules/sys/SysLicenceService";
import AppFieldNumber from "../../../components/toolkit-react/AppFieldNumber";
import SysRestrictionService from "../../../services/modules/sys/SysRestrictionService";

const sysRestrictionService = new SysRestrictionService();

interface IASysLicenceDet1Form extends IAppDet {}

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
      appField: "value_restriction",
      appHeader: capitalize(t("IN18VALORDARESTRICAODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "numeric",
      appExport: true,
    },
    {
      appField: "value_restriction_blocked",
      appHeader: capitalize(t("IN18VALORDARESTRICAOBLOQUEADADEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "numeric",
      appExport: true,
    },
    {
      appField: "days_blocked",
      appHeader: capitalize(t("IN18DIASPARABLOQUEIODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "numeric",
      appExport: true,
    },
    {
      appField: "days_blocked_extra",
      appHeader: capitalize(t("IN18DIASPARABLOQUEIOEXTRADEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "numeric",
      appExport: true,
    },
    {
      appField: "sys_restriction_id_obj.code_restriction",
      appHeader: capitalize(t("IN18RESTRICAODESISTEMASIGLADEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "sys_restriction_id_obj.name",
      appHeader: capitalize(t("IN18RESTRICAODESISTEMANOMEDEFAULT")),
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
const SysLicenceDet1Form: React.FC<IASysLicenceDet1Form> = (
  props: IASysLicenceDet1Form
) => {
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "value_restriction",
      required: [true, "Valor da Restrição is required"],
      defaultValue: "",
      type: "numeric",
      maxValue: [35, "Maximum 35 for valor"],
    },
    {
      fieldName: "value_restriction_blocked",
      required: [true, "Valor da Restricao - Bloqueada is required"],
      defaultValue: "",
      type: "numeric",
      maxValue: [35, "Maximum 35 for valor"],
    },
    {
      fieldName: "days_blocked",
      required: [true, "Dias para Bloqueio is required"],
      defaultValue: "",
      type: "numeric",
      maxValue: [35, "Maximum 35 for valor"],
    },
    {
      fieldName: "days_blocked_extra",
      required: [true, "Dias para Bloqueio is required"],
      defaultValue: "",
      type: "numeric",
      maxValue: [35, "Maximum 35 for valor"],
    },
    {
      fieldName: "sys_restriction_id",
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
        name="sys_licence_restriction_childs"
        appGenericListOptions={{
          id: "syslicencerestrictiondet1",
          appHelpText: "Det 1",
          appDataTableColumns: dataTableColumnsDet1,
          appProgramId: ConstProgramUtil.cSyslicenceId,
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
              name="value_restriction"
              appHelpText="Valor da Restrição Help"
              appTitle={capitalize(t("IN18VALORDARESTRICAODEFAULT"))}
            />
            <AppFieldNumber
              appFormControl={formControl}
              name="value_restriction_blocked"
              appHelpText="Valor da Restricao - Bloqueada Help"
              appTitle={capitalize(t("IN18DIASPARABLOQUEIODEFAULT"))}
            />
            <AppFieldNumber
              appFormControl={formControl}
              name="days_blocked"
              appHelpText="Dias para Bloqueio Help"
              appTitle={capitalize(t("IN18DIASPARABLOQUEIODEFAULT"))}
            />
            <AppFieldNumber
              appFormControl={formControl}
              name="days_blocked_extra"
              appHelpText="Dias para Bloqueio Help"
              appTitle={capitalize(t("IN18DIASPARABLOQUEIOEXTRADEFAULT"))}
            />
            <AppFieldDropdownFk
              appFormControl={formControl}
              appServiceDefault={sysRestrictionService}
              name="sys_restriction_id"
              appTitle={capitalize(t("IN18RESTRICAODESISTEMASIGLADEFAULT"))}
              appHelpText="System-Licenças Help"
              appDataKey="id"
              appOptionValue="id"
              appServiceFilterId="id"
              appOptionLabel="code_restriction"
              appServiceFilterDescription="code_restriction"
            />
          </AppContainerFields>
        </div>
      </GenericFormDet>
    </>
  );
};

export default memo(SysLicenceDet1Form);
