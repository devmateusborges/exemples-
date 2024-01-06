/* eslint-disable react/require-default-props */
import { Ripple } from "primereact/ripple";
import { classNames } from "primereact/utils";
import { useMediaQuery } from "react-responsive";

import IAppProps from "../../components/toolkit-react/interface/IAppProp";
import store from "../../store";
import { authMenuIndexAction, authShowMenuAction } from "../../store/AuthStore";
import { ConstUtil } from "../../utils/ConstUtil";

interface IAppLayoutMenuModule extends IAppProps {
  activeTab: number;
  classIcon: string;
  IconColor: string;
  indexTab: number;
  title?: string;
  title1?: string;
}

const AppLayoutMenuModule: React.FC<IAppLayoutMenuModule> = (
  props: IAppLayoutMenuModule
) => {
  // ==============================
  const isTabletOrMobile = useMediaQuery({
    query: ConstUtil.cisTabletOrMobile,
  });
  // ==============================
  return (
    <div className="pb-2 w-full">
      <a
        className={classNames(
          "p-ripple flex flex-row align-items-center cursor-pointer pt-2 pb-2 pl-2 ml-0 mr-0 hover:surface-400 justify-content-start   transition-duration-150 transition-colors ",
          {
            "surface-400 shadow-2  text-xl": props.activeTab === props.indexTab,
          },
          {
            "text-200 text-2xl": props.activeTab !== props.indexTab,
          }
        )}
        onClick={() => {
          store.dispatch(authShowMenuAction(true));
          store.dispatch(authMenuIndexAction(props.indexTab));
        }}
      >
        <div
          className={`w-10 md:w-9 flex ${
            isTabletOrMobile
              ? "justify-content-center"
              : "justify-content-start"
          }`}
        >
          <i
            style={{ color: props.IconColor }}
            className={`${props.classIcon}`}
          />
          {isTabletOrMobile ? undefined : props.title}

          <Ripple />
        </div>
      </a>
    </div>
  );
};
// ==============================
export default AppLayoutMenuModule;
