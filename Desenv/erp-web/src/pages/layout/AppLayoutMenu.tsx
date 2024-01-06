import { Button } from "primereact/button";
import { Ripple } from "primereact/ripple";
import { ScrollPanel } from "primereact/scrollpanel";
import { StyleClass } from "primereact/styleclass";
import { classNames } from "primereact/utils";
import { useCallback, useEffect, useMemo, useRef } from "react";
import { useMediaQuery } from "react-responsive";
import { Link } from "react-router-dom";
import AppVisible from "../../components/toolkit-react/bases/AppVisible";
import store, { useAppSelector } from "../../store";
import useState from "../../components/toolkit-react/hooks/useStateRef";
import IAppProps from "../../components/toolkit-react/interface/IAppProp";
import { AuthService } from "../../services/AuthService";
import { authShowMenuAction } from "../../store/AuthStore";
import { ConstUtil } from "../../utils/ConstUtil";
import { imageResultfacil3 } from "../../utils/ImageUtil";
import AppLayoutMenuModule from "./AppLayoutMenuModule";
import AppLayoutMenuOptions from "./AppLayoutMenuOptions";

interface IAppLayoutMenu extends IAppProps {
  appIndexTabMenu: number;
}

const AppLayoutMenu: React.FC<IAppLayoutMenu> = ({
  className,
  appIndexTabMenu,
}: IAppLayoutMenu) => {
  // ==============================
  const [moduleData, setModuleData, moduleDataRef] = useState<any>([]);
  const [moduleIndexData, setModuleIndexData] = useState<any>([]);
  const showMenu = useAppSelector((state) => state.auth.showMenu);
  const isTabletOrMobile = useMediaQuery({
    query: ConstUtil.cisTabletOrMobile,
  });

  // ==============================
  const onModuleFilter = async () => {
    const moduleDataFilter = await moduleDataRef.current.filter((item: any) => {
      return item.sys_module_order_visual == appIndexTabMenu;
    });
    setModuleIndexData(moduleDataFilter[0]);
  };
  // ==============================
  useEffect(() => {
    (async () => {
      const filterAux = {
        filter: {
          and: { login: store.getState().auth.auth.user.login },
        },
      };

      const resultModule = await AuthService.authListModule({
        pfilters: filterAux,
        findCache: true,
        saveCache: true,
      });
      setModuleData(resultModule);
      await onModuleFilter();
    })();
  }, []);
  // ==============================
  useEffect(() => {
    // console.log("appIndexTabMenu", appIndexTabMenu);
    (async () => {
      await onModuleFilter();
    })();
  }, [appIndexTabMenu]);
  // ==============================
  return (
    <>
      <div className="h-screen min-h-full z-5 absolute left-0 top-0 z-99999 shadow-1  w-full md:w-auto">
        <div className="flex h-full flex-row">
          <div
            className={`flex flex-column h-full ${
              store.getState().theme.classNameBg
            } flex-shrink-0 select-none ${
              isTabletOrMobile ? "w-5rem" : "w-15rem"
            } `}
          >
            <div className="bg-white ">
              <div
                className="flex align-items-center  justify-content-center flex-shrink-0 shadow-1"
                style={{ height: "55px" }}
              >
                <Link to="/private">
                  <img
                    src={imageResultfacil3}
                    alt="logo1"
                    height={isTabletOrMobile ? "30" : "50"}
                    width={isTabletOrMobile ? "60" : "80"}
                  />
                </Link>
              </div>
              <div
                className={`flex text-700   ${
                  isTabletOrMobile ? "text-md" : "text-2xl"
                } align-items-center justify-content-center font-bold pb-3 pt-3`}
              >
                Modules
              </div>
            </div>

            <div className="flex flex-column align-items-center justify-content-center overflow-y-auto scroll ">
              {moduleData.map((item: any) => (
                <AppLayoutMenuModule
                  key={item.sys_module_id}
                  activeTab={appIndexTabMenu}
                  title={item.sys_module_name}
                  title1={item.sys_module_sigla_module}
                  classIcon={`${item.sys_module_icon} text-5xl md:mr-2 `}
                  IconColor="surface-500"
                  indexTab={item.sys_module_order_visual}
                />
              ))}
            </div>
          </div>

          <div
            className={`  ${
              showMenu
                ? "flex flex-column h-full surface-100  flex-shrink-1 select-none align-content-center fadeinleft animation-duration-200"
                : "hidden "
            }  `}
            style={{ width: "100vw", maxWidth: "500px" }}
          >
            <AppLayoutMenuOptions
              className=" overflow-y-auto mt-3 "
              key={moduleIndexData?.sys_module_id}
              sysModuleId={moduleIndexData?.sys_module_id}
              title={moduleIndexData?.sys_module_name}
              title1={moduleIndexData?.sys_module_sigla_module}
              classIcon={`${moduleIndexData?.sys_module_icon} `}
              IconColor="white"
              indexTab={moduleIndexData?.sys_module_order_visual}
            />
          </div>
        </div>
      </div>
    </>
  );
};
// ==============================
export default AppLayoutMenu;
