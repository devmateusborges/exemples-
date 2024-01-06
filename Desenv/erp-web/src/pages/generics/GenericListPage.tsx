/* eslint-disable consistent-return */
/* eslint-disable no-bitwise */
/* eslint-disable array-callback-return */
/* eslint-disable react/require-default-props */
import { Column } from "primereact/column";
import { confirmDialog } from "primereact/confirmdialog";
import { DataTable, DataTableFilterMeta } from "primereact/datatable";
import {
  useCallback,
  useEffect,
  useLayoutEffect,
  useMemo,
  useRef,
} from "react";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";

import { Dialog } from "primereact/dialog";
import { promises } from "stream";
import AppContainer from "../../components/toolkit-react/AppContainer";

import AppContainerTitle from "../../components/toolkit-react/AppContainerTitle";
import AppDataTable, {
  IAppDataTable,
  IAppDataTableColumns,
  IAppDataTableDetColumns,
} from "../../components/toolkit-react/AppDataTable";
import AppTopBar, {
  IAppTopBar,
} from "../../components/toolkit-react/AppTopBar";
import AppVisible from "../../components/toolkit-react/bases/AppVisible";
import useState from "../../components/toolkit-react/hooks/useStateRef";
import IAppProps from "../../components/toolkit-react/interface/IAppProp";
import store, { useAppSelector } from "../../store";
import {
  dataSelectedAction,
  dataSelectedCleanAction,
} from "../../store/CrudStore";
import { apiParamsConvert } from "../../utils/ApiUtil";
import SysUserPreferenceService from "../../services/modules/sys/SysUserPreferenceService";

export interface IGenericListPage extends IAppProps, IAppTopBar {
  appProgramId?: any;
  appServiceDefault?: any;
  appRouteForm?: string;
  appShowTopBar: boolean;
  appTitle?: string;
  appDataTableDataValue?: any;
  appDataTablePaginateMode?: "server" | "local" | undefined;
  appDataTableDataKey?: string;
  appDataTableColumns: IAppDataTableColumns;
  appDataTableDetColumns?: Array<IAppDataTableDetColumns>;
  appDataTableGlobalFilterFields?: string[];
  appOnQueryDelete?: any;
  appOnQueryEdit?: any;
  appOnQueryAdd?: any;
  appSetQueryParams?: any;
  appButtonExtraTemplateRow?: any;
  appButtonExtraVisibleRow?: any;
  appButtonDeleteVisibleRow?: any;
  appButtonEditVisibleRow?: any;
  appSetButtonQueryDeleteRow?: any;
  appSetButtonQueryEditRow?: any;
  appRowExpansionDetTemplate?: any;
  appRowExpand?: boolean;
  appSplitButtonsExtra?: Array<any>;
  appPreferenceVisible?: boolean;
}

export interface IAppDataTableChild {
  appRefreshQuey: any;
  appRestoreTableState: any;
  appReload: any;
}

const sysUserPreferenceService = new SysUserPreferenceService();

const GenericListPage: React.FC<IGenericListPage> = (
  props: IGenericListPage
) => {
  // ==============================
  const dataTableRef = useRef<IAppDataTableChild>();
  const dataTableName = `dt${props?.id}`;
  const [dataValue, setDataValue, dataValueRef] = useState<any>(
    props.appDataTableDataValue ?? []
  );
  const navigate = useNavigate();
  const textloading = useAppSelector((state) => state.util.textloading);
  const selectedRows = useAppSelector(
    (state) => state.crud.dataSelected[dataTableName]
  );

  // ==============================
  useLayoutEffect(() => {
    setDataValue(props.appDataTableDataValue);
  }, [props.appDataTableDataValue]);
  // ==============================

  const handleDeleteAux = useCallback((rows: any) => {
    confirmDialog({
      message: "Do you want to delete record(s) ?",
      header: "Confirmation",
      icon: "pi pi-question-circle",
      accept: () => {
        if (props.appOnQueryDelete != undefined) {
          props.appOnQueryDelete(rows);
        } else if (props.appServiceDefault != undefined) {
          for (const obj of rows) {
            props.appServiceDefault.delete(obj.id).then(async (res: any) => {
              if (!res?.error) {
                toast.success(`Record ${obj.code ?? ""} successfully deleted`);
                dataTableRef?.current?.appReload();
              }
            });
          }
        }
        store.dispatch(dataSelectedCleanAction(dataTableName));
      },
      reject: () => {},
    });
  }, []);

  const handleDelete = useCallback(
    (e: any) => {
      // console.log("handleDelete", selectedRows);
      if (props.appDeleteAction !== undefined) {
        props.appDeleteAction(e, selectedRows);
      } else if (selectedRows && selectedRows.length > 0) {
        handleDeleteAux(selectedRows);
      } else {
        toast.warning("Select one or more records to be deleted");
      }
    },
    [selectedRows]
  );
  // ==============================
  const handleEditAux = useCallback((rows: any) => {
    if (props.appOnQueryEdit != undefined) {
      props.appOnQueryEdit(rows);
    } else if (props.appRouteForm != undefined) {
      navigate(`${props.appRouteForm}/${rows[0].id}`);
    }
  }, []);

  const handleEdit = useCallback(
    (e: any) => {
      // console.log("handleEdit", selectedRows);
      if (props.appEditAction !== undefined) {
        props.appEditAction(e, selectedRows);
      } else if (selectedRows && selectedRows.length > 0) {
        handleEditAux(selectedRows);
      } else {
        toast.warning("Select one or more records to be edit");
      }
    },
    [selectedRows]
  );
  // ==============================
  const handleAddAux = useCallback(() => {
    if (props?.appOnQueryAdd !== undefined) {
      props.appOnQueryAdd();
    } else {
      navigate(`${props.appRouteForm}/new`);
    }
  }, []);
  // ==============================
  const handleAdd = useCallback(() => {
    if (props.appAddAction !== undefined) {
      props.appAddAction();
    } else {
      handleAddAux();
    }
  }, []);

  // ==============================
  const handleRefresh = useCallback(() => {
    // console.log("handleRefresh");
    if (props.appRefreshAction !== undefined) {
      props.appRefreshAction();
    } else {
      dataTableRef?.current?.appRefreshQuey();
    }
  }, []);
  // ==============================
  const handleSelectedRows = useCallback((paramSelect: any) => {
    // console.log("GenericListPage>handleSelectedRows", paramSelect);
    const dataSelect = { [dataTableName]: paramSelect };

    store.dispatch(dataSelectedAction(dataSelect));
  }, []);
  // ==============================
  const handleSetQueryParams = useCallback(async (param: any) => {
    // console.log("GenericListPage>handleSetQueryParams", param);
    if (props.appSetQueryParams != undefined) {
      props.appSetQueryParams(param);
    } else if (props.appServiceDefault != undefined) {
      props.appServiceDefault
        .list(await apiParamsConvert(param, props.appDataTableColumns.columns))
        .then((res: any) => {
          setDataValue(res);
        });
    }
  }, []);
  // ==============================
  const handleSetButtonQueryDelete = useCallback(async (row: any) => {
    handleDeleteAux([row]);
  }, []);
  // ==============================
  const handleSetButtonQueryEdit = useCallback(async (row: any) => {
    handleEditAux([row]);
  }, []);

  // ==============================
  return (
    <>
      <AppContainer className="">
        <AppVisible visible={props.appTitle}>
          <AppContainerTitle
            appClassTitleBg={store.getState().theme.classNameTitleBg}
            appClassTitleText={store.getState().theme.classNameTitleText}
            appTitle={props.appTitle ?? ""}
            appHelpText={props.appHelpText}
          />
        </AppVisible>
        <AppVisible visible={props.appShowTopBar}>
          <AppTopBar
            appProgramId={props.appProgramId}
            appAddVisible={props.appAddVisible}
            appEditVisible={props.appEditVisible}
            appDeleteVisible={props.appDeleteVisible}
            appSaveVisible={props.appSaveVisible}
            appCancelVisible={props.appCancelVisible}
            appOptionsVisible={props.appOptionsVisible}
            appFavoriteVisible={props.appFavoriteVisible}
            appRefreshVisible={props.appRefreshVisible}
            appAddActionCode={props.appAddActionCode ?? "ADD"}
            appEditActionCode={props.appEditActionCode ?? "EDIT"}
            appDeleteActionCode={props.appDeleteActionCode ?? "DELETE"}
            appSaveActionCode={props.appSaveActionCode ?? "SAVE"}
            appAddAction={handleAdd}
            appEditAction={handleEdit}
            appDeleteAction={handleDelete}
            appSaveAction={props.appSaveAction}
            appCancelAction={props.appCancelAction}
            appOptionsAction={props.appOptionsAction}
            appFavoriteAction={props.appFavoriteAction}
            appRefreshAction={handleRefresh}
          />
        </AppVisible>

        <AppDataTable
          id={`dt${props?.id}`}
          ref={dataTableRef}
          appStateStorage="custom"
          appDataValue={dataValue}
          appRowExpansionTemplate={props.appRowExpansionDetTemplate}
          appDataTableDetColumns={props.appDataTableDetColumns}
          appRowExpand={props.appRowExpand}
          appPaginateMode={props.appDataTablePaginateMode}
          appDataKey={props.appDataTableDataKey ?? "id"}
          appColumns={props.appDataTableColumns}
          appButtonExtraTemplateRow={props.appButtonExtraTemplateRow}
          appButtonExtraVisibleRow={props.appButtonExtraVisibleRow}
          appButtonDeleteVisibleRow={props.appButtonDeleteVisibleRow}
          appButtonEditVisibleRow={props.appButtonEditVisibleRow}
          appGlobalFilterFields={props.appDataTableGlobalFilterFields}
          appDataSelected={selectedRows}
          appSplitButtonsExtra={props.appSplitButtonsExtra}
          appOnSelect={handleSelectedRows}
          appSetQueryParams={handleSetQueryParams}
          appSetButtonQueryDeleteRow={handleSetButtonQueryDelete}
          appSetButtonQueryEditRow={handleSetButtonQueryEdit}
          appProgramId={props.appProgramId}
          appPreferenceVisible={props.appPreferenceVisible}
          appPreferenceService={sysUserPreferenceService}
          appPreferenceDeleteVisible
          appPreferenceEditVisible
          appPreferenceSaveVisible
          appPreferenceCheckVisible
          appPreferenceAddVisible
          appShowHeader
          appUserId={store.getState().auth.auth.user.id}
        />
      </AppContainer>
    </>
  );
};
// ==============================
export default GenericListPage;
