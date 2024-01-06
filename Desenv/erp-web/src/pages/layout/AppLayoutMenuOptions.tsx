import { Button } from "primereact/button";
import { Divider } from "primereact/divider";
import { InputText } from "primereact/inputtext";
import { ScrollPanel } from "primereact/scrollpanel";
import { SelectButton } from "primereact/selectbutton";
import { classNames } from "primereact/utils";
import { memo, useCallback, useEffect, useMemo } from "react";
import { useMediaQuery } from "react-responsive";
import { useNavigate } from "react-router-dom";

import useState from "../../components/toolkit-react/hooks/useStateRef";
import IAppProps from "../../components/toolkit-react/interface/IAppProp";
import { AuthService } from "../../services/AuthService";
import store, { useAppSelector } from "../../store";
import { authShowMenuAction } from "../../store/AuthStore";
import { ConstUtil } from "../../utils/ConstUtil";
import AppLayoutMenuOptionsSub from "./AppLayoutMenuOptionsSub";

interface IAppLayoutMenuOptions extends IAppProps {
  sysModuleId: string;
  title: string;
  title1: string;
  classIcon: string;
  IconColor: string;
  indexTab: number;
}

const AppLayoutMenuOptions: React.FC<IAppLayoutMenuOptions> = (
  props: IAppLayoutMenuOptions
) => {
  // ==============================
  const navigate = useNavigate();
  const [typeProgramSelect, setTypeProgramSelect, typeProgramSelectRef] =
    useState<any>("T");
  const [searchProgram, setSearchProgram, SearchProgramRef] = useState<any>("");
  const authenticated = useAppSelector((state) => state.auth.auth);
  const programDataStore = useAppSelector((state) => state.auth.program);
  const [programData, setProgramData, programDataRef] = useState<any>([]);
  const isTabletOrMobile = useMediaQuery({
    query: ConstUtil.cisTabletOrMobile,
  });
  const themeBg = store.getState().theme.classNameBg;

  // ==============================
  // TODO Buscar do type BD
  const typeProgram = [
    { name: "Table", value: "T", icon: "mdi mdi-table" },
    { name: "Entries", value: "L", icon: "mdi mdi-file-arrow-up-down" },
    { name: "Processing", value: "P", icon: "mdi mdi-database-cog-outline" },
    { name: "Utilities", value: "U", icon: "mdi mdi-tools" },
  ];
  // ==============================

  useEffect(() => {
    (async () => {
      const filterAux = {
        filter: {
          and: { login: store.getState().auth.auth.user.login },
        },
        sysModuleId: props.sysModuleId,
      };
      await AuthService.authListProgram({
        pfilters: filterAux,
        findCache: true,
        saveCache: true,
      });
    })();
  }, []);
  useEffect(() => {
    (async () => {
      // console.log("<<< ", programDataStore);

      // console.log("sysModuleId", props.sysModuleId);
      let resultProgramFilter = await programDataStore.items.filter(
        (item: any) => {
          return item.sys_module_id === props.sysModuleId;
        }
      );

      // console.log("resultProgramFilter", resultProgramFilter);
      if (typeProgramSelectRef.current) {
        const resultTypeProgramFilter = await resultProgramFilter.filter(
          (item: any) => {
            return (
              item.sys_program_type_program === typeProgramSelectRef.current
            );
          }
        );
        resultProgramFilter = resultTypeProgramFilter;
      }

      if (SearchProgramRef.current) {
        const resultSearchProgramFilter = await resultProgramFilter.filter(
          (item: any) => {
            return (
              item.sys_program_name
                .toUpperCase()
                .search(SearchProgramRef.current.toUpperCase()) !== -1
            );
          }
        );
        resultProgramFilter = resultSearchProgramFilter;
      }

      await setProgramData(resultProgramFilter);
    })();
  }, [typeProgramSelect, searchProgram, programDataStore]);
  // ==============================
  const onOpenSubMenu = async (sysProgramId: any, link: any) => {
    await store.dispatch(authShowMenuAction(false));
    await navigate(link);
  };
  // ==============================
  const typeProgramTemplate = (option: any) => {
    return (
      <span>
        <i className={option.icon} /> {isTabletOrMobile ? "" : option.name}
      </span>
    );
  };
  // ==============================
  return (
    <div className="flex flex-column h-full w-full surface-100   shadow-2">
      {props.children}
      <div
        className={`${
          isTabletOrMobile ? "text-lg" : "text-3xl"
        }  w-full p-3 text-white font-bold ${themeBg}`}
        onClick={() => {
          console.log("Menu hide");
          store.dispatch(authShowMenuAction(false));
        }}
      >
        <Button
          icon="pi pi-times text-xl"
          className="p-button p-button-text  text-white mr-3 "
          onClick={() => {
            store.dispatch(authShowMenuAction(false));
          }}
        />
        <i
          className={`${props.classIcon}  ${
            isTabletOrMobile ? "text-xl" : "text-4xl"
          } pr-2`}
        />
        {props.title} {props.title1 ? `(${props.title1})` : undefined}
      </div>
      <div className="flex  flex-column  mb-3 ">
        <div className="col-12 p-2">
          <div className="p-inputgroup mt-3">
            <span className="p-inputgroup-addon">
              <i className="pi pi-search" />
            </span>
            <InputText
              value={searchProgram}
              onChange={(e) => setSearchProgram(e.target.value)}
              placeholder="Search"
            />
            <Button
              icon="pi pi-times"
              className="p-button-danger"
              onClick={() => {
                setSearchProgram("");
              }}
            />
          </div>
        </div>
        <Divider />
        <div className="flex w-full  justify-content-center mr-2 ml-2">
          <SelectButton
            className="text-sm"
            value={typeProgramSelect}
            options={typeProgram}
            onChange={(e) => {
              (async () => {
                setTypeProgramSelect(e.value);
              })();
            }}
            itemTemplate={typeProgramTemplate}
            optionLabel="name"
          />
        </div>
        <Divider />
      </div>

      <ScrollPanel className="overflow-y-auto">
        <div className="pt-1">
          {programData.map((item: any) => (
            <AppLayoutMenuOptionsSub
              key={item.sys_program_id}
              sysProgramId={item.sys_program_id}
              title={item.sys_program_name}
              link={item.sys_program_controller}
              classIcon={item.sys_program_icon}
              subType={item.sys_program_type_program}
              isFavorite={item.sys_program_is_favorite}
              onClickSubMenu={(sysProgramId: any, link: any) => {
                // console.log(sysProgramId, link);
                onOpenSubMenu(sysProgramId, link);
              }}
            />
          ))}
        </div>
      </ScrollPanel>
      <div className="p-2">
        <Divider />
        <div className="text-md ">
          <strong>User:</strong> {authenticated?.user?.login}
        </div>
        <div className="text-md ">
          <strong>Unit:</strong> {authenticated?.unit?.name}
        </div>
      </div>
    </div>
  );
};
// ==============================
export default AppLayoutMenuOptions;
