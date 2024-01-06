import { ScrollPanel } from "primereact/scrollpanel";
import { Skeleton } from "primereact/skeleton";
import { useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";

import AppContainer from "../../components/toolkit-react/AppContainer";
import AppContainerFields from "../../components/toolkit-react/AppContainerFields";
import AppContainerTitle from "../../components/toolkit-react/AppContainerTitle";
import useState from "../../components/toolkit-react/hooks/useStateRef";
import IAppProps from "../../components/toolkit-react/interface/IAppProp";
import SysProgramFavoriteService from "../../services/modules/sys/SysProgramFavoriteService";
import store, { useAppSelector } from "../../store";
import { authShowMenuAction } from "../../store/AuthStore";
import { imageResultfacil3 } from "../../utils/ImageUtil";
import AppLayoutLoading from "./AppLayoutLoading";
import AppLayoutMenuFavoriteSub from "./AppLayoutMenuFavoriteSub";
import AppLayoutMenuOptionsSub from "./AppLayoutMenuOptionsSub";

interface IAppLayoutMenuFavorite extends IAppProps {}

const sysProgramFavoriteService = new SysProgramFavoriteService();

const AppLayoutMenuFavorite: React.FC<IAppLayoutMenuFavorite> = ({
  children,
  className,
}: IAppLayoutMenuFavorite) => {
  // ==============================
  const navigate = useNavigate();
  const textloading = useAppSelector((state) => state.util.textloading);
  const programFavoriteData = useAppSelector(
    (state) => state.auth.programFavorite
  );
  // ==============================
  useEffect(() => {
    (async () => {
      const filterAux = {
        filter: {
          and: { login: store.getState().auth.auth.user.login },
        },
      };

      await sysProgramFavoriteService.list({
        pfilters: filterAux,
        cache: true,
      });
    })();
  }, []);
  // ==============================
  const onOpenSubMenu = async (sysProgramId: any, link: any) => {
    await store.dispatch(authShowMenuAction(false));
    await navigate(link);
  };
  // ==============================
  return (
    <>
      <AppLayoutLoading text={textloading} />
      <AppContainer className="">
        <AppContainerTitle
          appClassTitleBg={store.getState().theme.classNameTitleBg}
          appClassTitleText={store.getState().theme.classNameTitleText}
          appTitle="Favorite"
        />

        <div className="flex  flex-column align-items-center p-5">
          <div className="flex flex-wrap justify-content-center card-container gap-3">
            {programFavoriteData.items.map((item: any) => (
              <AppLayoutMenuFavoriteSub
                key={item.sys_program_id}
                sysProgramId={item.sys_program_id}
                title={item.sys_program_name}
                link={item.sys_program_controller}
                classIcon={item.sys_program_icon}
                subType={item.sys_program_type_program}
                onClickSubMenu={(sysProgramId: any, link: any) => {
                  // console.log(sysProgramId, link);
                  onOpenSubMenu(sysProgramId, link);
                }}
              />
            ))}
          </div>
        </div>
        {children}
      </AppContainer>
    </>
  );
};
// ==============================
export default AppLayoutMenuFavorite;
