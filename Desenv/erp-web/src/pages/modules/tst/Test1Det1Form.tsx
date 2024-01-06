import { memo, useRef } from "react";
import { Menu } from "primereact/menu";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldNumber from "../../../components/toolkit-react/AppFieldNumber";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import IAppDet from "../../../components/toolkit-react/interface/IAppDet";
import FinBancoService from "../../../services/modules/fin/FinBancoService";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";
import { formatDateTimeColumn } from "../../../utils/FuncUtil";
import GenericFormDet from "../../generics/GenericFormDet";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";
import AppFieldFile from "../../../components/toolkit-react/AppFieldFile";

const finBancoService = new FinBancoService();

interface IATest1Det1Form extends IAppDet {}

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
    },
    {
      appField: "codigo",
      appHeader: "Código",
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
    },
    {
      appField: "quantidade",
      appHeader: "Quantidade",
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "numeric",
    },
    {
      appField: "valor_total",
      appHeader: "Valor total",
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "numeric",
    },
    {
      appField: "valor_unit",
      appHeader: "Valor unitario",
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "numeric",
    },
    {
      appField: "sys_document_foto",
      appHeader: "Fotos",
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

const Test1Det1Form: React.FC<IATest1Det1Form> = (props: IATest1Det1Form) => {
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "codigo",
      required: [true, "Code is required"],
      defaultValue: "",
    },
    {
      fieldName: "quantidade",
      required: [true, "Quantidade is required"],
      defaultValue: "",
    },
    {
      fieldName: "valor_total",
      required: [true, "Valor total is required"],
      defaultValue: "",
    },
    {
      fieldName: "valor_unit",
      required: [true, "Valor unitario is required"],
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
        name="test1_childs"
        appGenericListOptions={{
          id: "test1listdet1",
          appHelpText: "Det 1",
          appDataTableColumns: dataTableColumnsDet1,
          appProgramId: ConstProgramUtil.cTstTest1Id,
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
            <AppFieldText
              appFormControl={formControl}
              name="codigo"
              appTitle="Code"
              appHelpText="Código"
            />
            <AppFieldNumber
              appFormControl={formControl}
              name="quantidade"
              appHelpText="Quantidade"
              appTitle="Quantidade"
              appMinFractionDigits={4}
            />
            <AppFieldNumber
              appFormControl={formControl}
              name="valor_total"
              appHelpText="Valor total"
              appTitle="Valor total"
              appMinFractionDigits={4}
            />
            <AppFieldNumber
              appFormControl={formControl}
              name="valor_unit"
              appHelpText="Valor unitario"
              appTitle="Valor unitario"
              appMinFractionDigits={4}
            />
            <AppFieldFile
              className="col-12"
              name="sys_document_foto"
              appDocumentValueObj={formControl.getValues()["sys_document_foto"]}
              appFormControl={formControl}
            />
          </AppContainerFields>
        </div>
      </GenericFormDet>
    </>
  );
};

export default memo(Test1Det1Form);
