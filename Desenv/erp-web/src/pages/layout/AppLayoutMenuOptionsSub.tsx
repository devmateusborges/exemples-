import { Divider } from "primereact/divider";
import { Ripple } from "primereact/ripple";
import { ScrollPanel } from "primereact/scrollpanel";
import { classNames } from "primereact/utils";
import { toast } from "react-toastify";

import IAppProps from "../../components/toolkit-react/interface/IAppProp";
import SysProgramFavoriteService from "../../services/modules/sys/SysProgramFavoriteService";

interface IAppLayoutMenuOptionsSub extends IAppProps {
  sysProgramId: string;
  title: string;
  link: string;
  classIcon: string;
  subType: string;
  isFavorite: string;
  onClickSubMenu: (sysProgramId: any, link: any) => void;
}

const sysProgramFavoriteService = new SysProgramFavoriteService();

const AppLayoutMenuOptionsSub: React.FC<IAppLayoutMenuOptionsSub> = (
  props: IAppLayoutMenuOptionsSub
) => {
  // ==============================
  return (
    <div
      className="flex flex-column  ml-2 p-2 justify-content-between  hover:surface-400  cursor-pointer transition-duration-150 transition-colors border-round-sm"
      onClick={() => {
        props.onClickSubMenu(props.sysProgramId, props.link);
      }}
    >
      <div className="flex justify-content-between">
        <div className="text-sl md:text-xl lg:text-xl">
          <i className={`${props.classIcon} `} />
          <label className="ml-2 underline">{props.title}</label>
        </div>
        <div
          className="text-2xl hover:surface-500  transition-duration-150 transition-colors border-round-md"
          onClick={(e) => {
            (async () => {
              const r = await sysProgramFavoriteService.favorite(
                props.sysProgramId,
                props.isFavorite == "S" ? "N" : "S"
              );
              toast.success(r.msg);
            })();
          }}
        >
          <i
            className={`mdi mdi-star ${
              props.isFavorite == "S" ? "text-yellow-500" : "text-blue-200"
            }`}
          />
        </div>
      </div>
    </div>
  );
};
// ==============================
export default AppLayoutMenuOptionsSub;
