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
import FisNcmService from "../../../services/modules/fis/FisNcmService";

const fisNcmService = new FisNcmService();

interface IAFisCestDet1Form extends IAppDet {}

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
      appField: "fis_ncm_id_obj.nr_ncm",
      appHeader: capitalize(t("IN18NCMNUMERODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "fis_ncm_id_obj.nome",
      appHeader: capitalize(t("IN18NCMNOMEDEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
  ],
};

// ==============================
const fisCestDet1Form: React.FC<IAFisCestDet1Form> = (
  props: IAFisCestDet1Form
) => {
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "fis_ncm_id",
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
        name="crm_status_prox_childs"
        appGenericListOptions={{
          id: "fiscestdet1",
          appHelpText: "Det 1",
          appDataTableColumns: dataTableColumnsDet1,
          appProgramId: ConstProgramUtil.cFiscestId,
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
              appServiceDefault={fisNcmService}
              name="fis_ncm_id"
              appTitle={capitalize(t("IN18FISNCMDEFAULT"))}
              appHelpText="fiscal NCM Help"
              appDataKey="id"
              appOptionValue="id"
              appServiceFilterId="id"
              appOptionLabel="nome"
              appServiceFilterDescription="nome"
            />
          </AppContainerFields>
        </div>
      </GenericFormDet>
    </>
  );
};

export default memo(fisCestDet1Form);
