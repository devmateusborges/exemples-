import { memo } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldFile from "../../../components/toolkit-react/AppFieldFile";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import IAppDet from "../../../components/toolkit-react/interface/IAppDet";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";
import GenericFormDet from "../../generics/GenericFormDet";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";

interface IATest1Det2Form extends IAppDet {}
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
      appHeader: "Observação",
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appHidden: false,
      appDataType: "text",
    },
    {
      appField: "foto_analizada",
      appHeader: "Foto analizada",
      appSortable: false,
      appFilter: false,
      appFilterMatch: "contains",
      appDataType: "document",
    },
    {
      appField: "log_user_ins",
      appHeader: "Usuário de Inserção",
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appHidden: true,
      appDataType: "text",
    },
    {
      appField: "log_date_ins",
      appHeader: "Data de Inserção",
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appHidden: true,
      appDataType: "date",
    },
    {
      appField: "log_date_upd",
      appHeader: "Data de Alteração",
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appHidden: true,
      appDataType: "date",
    },
    {
      appField: "log_user_upd",
      appHeader: "Usuário de Alteração",
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appHidden: true,
      appDataType: "text",
    },
  ],
};

const Test1Det2Form: React.FC<IATest1Det2Form> = (props: IATest1Det2Form) => {
  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "observacao",
      required: [false, "Observacao is required"],
      maxValue: [250, "Maximum 250 characters for observacao"],
      defaultValue: "",
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
        name="test1a_childs"
        appGenericListOptions={{
          id: "test2listdet2",
          appHelpText: "Det 2",
          appDataTableColumns: dataTableColumnsDet2,
          appProgramId: ConstProgramUtil.cTstTest1Id,
          appDataTableDataValue: props.appDataTableDataValue,
          appDataTablePaginateMode: "local",
          appShowTopBar: true,
          appRefreshVisible: true,
          appAddVisible: true,
          appDeleteVisible: true,
          appButtonDeleteVisibleRow: true,
          appButtonEditVisibleRow: true,
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
              appTitle="Observação"
              appHelpText="Observação"
            />
            <AppFieldFile
              className="col-12"
              name="foto_analizada"
              appMany
              appDocumentValueObj={formControl.getValues()["foto_analizada"]}
              appFormControl={formControl}
            />
          </AppContainerFields>
        </div>
      </GenericFormDet>
    </>
  );
};

export default memo(Test1Det2Form);
