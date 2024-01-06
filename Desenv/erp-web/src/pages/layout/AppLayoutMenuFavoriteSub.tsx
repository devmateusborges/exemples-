import { Button } from "primereact/button";
import { Divider } from "primereact/divider";
import { Ripple } from "primereact/ripple";
import { ScrollPanel } from "primereact/scrollpanel";
import { classNames } from "primereact/utils";
import { toast } from "react-toastify";

import IAppProps from "../../components/toolkit-react/interface/IAppProp";
import SysProgramFavoriteService from "../../services/modules/sys/SysProgramFavoriteService";

interface IAppLayoutMenuFavoriteSub extends IAppProps {
  sysProgramId: string;
  title: string;
  link: string;
  classIcon: string;
  subType: string;
  onClickSubMenu: (sysProgramId: any, link: any) => void;
}

const sysProgramFavoriteService = new SysProgramFavoriteService();

const AppLayoutMenuFavoriteSub: React.FC<IAppLayoutMenuFavoriteSub> = (
  props: IAppLayoutMenuFavoriteSub
) => {
  // ==============================
  return (
    <div className="flex flex-column shadow-2 w-18rem h-4rem surface-card h-full  p-2 justify-content-between  hover:surface-400  transition-duration-150 transition-colors border-round-md">
      <div className="flex justify-content-between">
        <span className="text-xl ">
          <i className={`${props.classIcon} `} />
          <a
            className="ml-2"
            onClick={() => {
              props.onClickSubMenu(props.sysProgramId, props.link);
            }}
          >
            {props.title}
          </a>
        </span>
        <span
          className="text-2xl hover:surface-500  transition-duration-150 transition-colors border-round-md"
          onClick={(e) => {
            (async () => {
              const r = await sysProgramFavoriteService.favorite(
                props.sysProgramId,
                "N"
              );
              toast.success(r.msg);
            })();
          }}
        >
          <i className="mdi mdi-star text-yellow-500" />
        </span>
      </div>
    </div>
  );
};
export default AppLayoutMenuFavoriteSub;
