import { t } from "i18next";
import { memo } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import IAppDet from "../../../components/toolkit-react/interface/IAppDet";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";
import { capitalize, formatDateTimeColumn } from "../../../utils/FuncUtil";
import GenericFormDet from "../../generics/GenericFormDet";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import MovStatusService from "../../../services/modules/mov/MovStatusService";

const movStatusService = new MovStatusService();

interface IAMovOperacaoDet1Form extends IAppDet {}

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
      appField: "mov_status_id_obj.sigla_mov_status",
      appHeader: capitalize(t("IN18STATUSDOMOVIMENTOSIGLADEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "mov_status_id_obj.nome",
      appHeader: capitalize(t("IN18STATUSDOMOVIMENTONOMEDEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "mov_status_id_prox_obj.sigla_mov_status",
      appHeader: capitalize(t("IN18STATUSDOMOVIMENTOPROXIMOSIGLADEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "mov_status_id_prox_obj.nome",
      appHeader: capitalize(t("IN18STATUSDOMOVIMENTOPROXIMONOMEDEFAULT")),
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

const movOperacaoDet1Form: React.FC<IAMovOperacaoDet1Form> = (
  props: IAMovOperacaoDet1Form
) => {
  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "mov_status_id",
      required: [true, "Status do Movimento is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "mov_status_id_prox",
      required: [true, "Movimento - Próximo is required"],
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
        name="mov_operacao_status_childs"
        appGenericListOptions={{
          id: "movoperacaostatusdet1",
          appHelpText: "Status do Movimento Help",
          appProgramId: ConstProgramUtil.cMovoperacaoId,
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
            <AppFieldDropdownFk
              appFormControl={formControl}
              appServiceDefault={movStatusService}
              name="mov_status_id"
              appTitle={capitalize(t("IN18STATUSDOMOVIMENTOSIGLADEFAULT"))}
              appHelpText="Status do Movimento Help"
              appDataKey="id"
              appOptionValue="id"
              appServiceFilterId="id"
              appOptionLabel="sigla_mov_status"
              appServiceFilterDescription="sigla_mov_status"
            />
            <AppFieldDropdownFk
              appFormControl={formControl}
              appServiceDefault={movStatusService}
              name="mov_status_id_prox"
              appTitle={capitalize(
                t("IN18STATUSDOMOVIMENTOPROXIMOSIGLADEFAULT")
              )}
              appHelpText="Movimento - Próximo Help"
              appDataKey="id"
              appOptionValue="id"
              appServiceFilterId="id"
              appOptionLabel="sigla_mov_status"
              appServiceFilterDescription="sigla_mov_status"
            />
          </AppContainerFields>
        </div>
      </GenericFormDet>
    </>
  );
};

export default memo(movOperacaoDet1Form);
