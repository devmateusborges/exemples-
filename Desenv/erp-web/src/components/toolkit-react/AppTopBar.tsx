/* eslint-disable react/require-default-props */
import { Button } from "primereact/button";
import { useEffect } from "react";
import { useMediaQuery } from "react-responsive";
import { toast } from "react-toastify";
import store, { useAppSelector } from "../../store";
import useState from "./hooks/useStateRef";
import { ConstUtil } from "../../utils/ConstUtil";
import AppVisible from "./bases/AppVisible";
import IAppProps from "./interface/IAppProp";
import SysProgramFavoriteService from "../../services/modules/sys/SysProgramFavoriteService";
import AppGenericAction from "./AppGenericAction";

export interface IAppTopBar extends IAppProps {
  appAddAction?: any;
  appEditAction?: any;
  appDeleteAction?: any;
  appSaveAction?: any;
  appCancelAction?: any;
  appOptionsAction?: any;
  appFavoriteAction?: any;
  appRefreshAction?: any;
  appAddVisible?: boolean;
  appEditVisible?: boolean;
  appDeleteVisible?: boolean;
  appSaveVisible?: boolean;
  appCancelVisible?: boolean;
  appOptionsVisible?: boolean;
  appFavoriteVisible?: boolean;
  appRefreshVisible?: boolean;
  appButtonExtraVisible?: boolean;
  appSavePlusVisible?: boolean;
  appSavePlusAction?: any;
  appButtonExtra?: any;
  appProgramId?: any;
  appAddActionCode?: string;
  appEditActionCode?: string;
  appDeleteActionCode?: string;
  appSaveActionCode?: string;
  appProcessVisible?: boolean;
  appProcessAction?: any;
  appRevokeVisible?: boolean;
  appRevokeAction?: any;
  appProcessActionCode?: string;
  appRevokeActionCode?: string;
}

const sysProgramFavoriteService = new SysProgramFavoriteService();

const AppTopBar: React.FC<IAppTopBar> = (props: IAppTopBar) => {
  // ==============================
  const isTabletOrMobile = useMediaQuery({
    query: ConstUtil.cisTabletOrMobile,
  });
  const [programFilter, setProgramFilter] = useState<any>();
  const programDataStore = useAppSelector((state) => state.auth.program);
  // ==============================
  useEffect(() => {
    (async () => {
      if (props.appProgramId != undefined) {
        const resultProgramFilter = await programDataStore.items.filter(
          (item: any) => {
            return item.sys_program_id === props.appProgramId;
          }
        );
        setProgramFilter(resultProgramFilter[0]);
      }
    })();
  }, [programDataStore]);
  // ==============================
  useEffect(() => {}, [store.getState().theme]);
  // ==============================
  return (
    <>
      {/* pl-3 pt-3 app-menu-left */}

      <div className="  flex flex-row justify-content-between   surface-0 h-4rem p-0">
        <div className=" flex flex-row flex-grow-1 align-items-center p-0 p-2">
          <AppVisible visible={props.appAddVisible ?? false}>
            <AppGenericAction
              appIcon="pi pi-plus text-xl"
              className="p-button-secondary p-button-outlined ml-2 text-xl"
              classNameBorder={store.getState().theme.classNameBorder}
              classNameText={store.getState().theme.classNameText}
              appLabel={isTabletOrMobile ? undefined : "Add"}
              appOnAction={props.appAddAction}
              appProgramId={props.appProgramId}
              appActionCode={props.appAddActionCode}
            />
          </AppVisible>
          <AppVisible visible={props.appEditVisible ?? false}>
            <AppGenericAction
              appIcon="pi pi-pencil text-xl"
              className="p-button-secondary p-button-outlined ml-2 text-xl"
              appLabel={isTabletOrMobile ? "" : "Edit"}
              classNameBorder={store.getState().theme.classNameBorder}
              classNameText={store.getState().theme.classNameText}
              appOnAction={props.appEditAction}
              appProgramId={props.appProgramId}
              appActionCode={props.appEditActionCode}
            />
          </AppVisible>
          <AppVisible visible={props.appDeleteVisible ?? false}>
            <AppGenericAction
              appIcon="pi pi-trash text-xl"
              className="p-button-secondary p-button-outlined ml-2 text-xl"
              appLabel={isTabletOrMobile ? "" : "Delete"}
              classNameBorder={store.getState().theme.classNameBorder}
              classNameText={store.getState().theme.classNameText}
              appOnAction={props.appDeleteAction}
              appProgramId={props.appProgramId}
              appActionCode={props.appDeleteActionCode}
            />
          </AppVisible>
          <AppVisible visible={props.appSaveVisible ?? false}>
            <AppGenericAction
              appIcon="pi pi-save text-xl"
              className="p-button-secondary p-button-outlined ml-2 text-xl"
              appLabel={isTabletOrMobile ? "" : "Save"}
              classNameBorder={store.getState().theme.classNameBorder}
              classNameText={store.getState().theme.classNameText}
              appOnAction={props.appSaveAction}
              appProgramId={props.appProgramId}
              appActionCode={props.appSaveActionCode}
            />
          </AppVisible>
          <AppVisible visible={props.appSavePlusVisible ?? false}>
            <AppGenericAction
              appIcon="pi pi-save text-xl"
              className="p-button-secondary p-button-outlined ml-2 text-xl"
              appLabel={isTabletOrMobile ? "+" : "Save +"}
              classNameBorder={store.getState().theme.classNameBorder}
              classNameText={store.getState().theme.classNameText}
              appOnAction={props.appSavePlusAction}
              appProgramId={props.appProgramId}
              appActionCode={props.appSaveActionCode}
            />
          </AppVisible>
          <AppVisible visible={props.appCancelVisible ?? false}>
            <AppGenericAction
              appIcon="pi pi-ban text-xl"
              className="p-button-secondary p-button-outlined ml-2 text-xl"
              appLabel={isTabletOrMobile ? "" : "Cancel"}
              classNameBorder={store.getState().theme.classNameBorder}
              classNameText={store.getState().theme.classNameText}
              appOnAction={props.appCancelAction}
            />
          </AppVisible>
          <AppVisible visible={props.appRefreshVisible ?? false}>
            <AppGenericAction
              appIcon="pi pi-refresh text-xl"
              className="p-button-secondary p-button-outlined ml-2 text-xl"
              appLabel={isTabletOrMobile ? "" : "Refresh"}
              classNameBorder={store.getState().theme.classNameBorder}
              classNameText={store.getState().theme.classNameText}
              appOnAction={props.appRefreshAction}
            />
          </AppVisible>
          <AppVisible visible={props.appProcessVisible ?? false}>
            <AppGenericAction
              appIcon="pi pi-bolt text-xl"
              className="p-button-secondary p-button-outlined ml-2 text-xl"
              appLabel={isTabletOrMobile ? "" : "Process"}
              classNameBorder={store.getState().theme.classNameBorder}
              classNameText={store.getState().theme.classNameText}
              appOnAction={props.appProcessAction}
              appProgramId={props.appProgramId}
              appActionCode={props.appProcessActionCode}
            />
          </AppVisible>
          <AppVisible visible={props.appRevokeVisible ?? false}>
            <AppGenericAction
              appIcon="pi pi-undo text-xl"
              className="p-button-secondary p-button-outlined ml-2 text-xl"
              appLabel={isTabletOrMobile ? "" : "Revoke"}
              classNameBorder={store.getState().theme.classNameBorder}
              classNameText={store.getState().theme.classNameText}
              appOnAction={props.appRevokeAction}
              appProgramId={props.appProgramId}
              appActionCode={props.appRevokeActionCode}
            />
          </AppVisible>
          <AppVisible visible={props.appButtonExtraVisible ?? false}>
            {props.appButtonExtra}
          </AppVisible>
        </div>
        <div className="flex flex-row align-items-center  p-0">
          <AppVisible visible={props.appOptionsVisible ?? false}>
            <AppGenericAction
              appIcon="pi pi-bars text-xl"
              className="p-button-lg  p-button-help mr-2 text-xl"
              appOnAction={props.appOptionsAction}
            />
          </AppVisible>
          <AppVisible visible={props.appFavoriteVisible ?? false}>
            <AppGenericAction
              appIcon="mdi mdi-star text-xl"
              className={` ${
                programFilter?.sys_program_is_favorite == "S"
                  ? "text-yellow-500"
                  : "text-blue-200"
              } p-button-text mr-3`}
              appOnAction={() => {
                if (props.appFavoriteAction != undefined) {
                  props.appFavoriteAction();
                } else {
                  (async () => {
                    const r = await sysProgramFavoriteService.favorite(
                      programFilter.sys_program_id,
                      programFilter.sys_program_is_favorite == "S" ? "N" : "S"
                    );
                    toast.success(r.msg);
                  })();
                }
              }}
            />
          </AppVisible>
        </div>
      </div>
    </>
  );
};

export default AppTopBar;
