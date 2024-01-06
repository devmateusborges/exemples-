import { Badge } from "primereact/badge";
import { Button } from "primereact/button";
import { Ripple } from "primereact/ripple";
import { StyleClass } from "primereact/styleclass";
import { useRef } from "react";
import { useMediaQuery } from "react-responsive";
import { useNavigate } from "react-router-dom";

import IAppProps from "../../components/toolkit-react/interface/IAppProp";
import store from "../../store";
import { authCleanAction, authShowMenuAction } from "../../store/AuthStore";
import { ConstUtil } from "../../utils/ConstUtil";
import { imageResultfacil3 } from "../../utils/ImageUtil";

interface IAppLayoutMenuHeader extends IAppProps {
  appOnShowMenuProfile: (show: boolean) => void;
}

const AppLayoutMenuHeader: React.FC<IAppLayoutMenuHeader> = ({
  className,
  appOnShowMenuProfile,
}: IAppLayoutMenuHeader) => {
  // ==============================
  const btnRefBars = useRef(null);
  const btnRefBarsMobile = useRef(null);
  const navigate = useNavigate();
  const isTabletOrMobile = useMediaQuery({
    query: ConstUtil.cisTabletOrMobile,
  });
  const themeText = store.getState().theme.classNameText;
  const themeBorder = store.getState().theme.classNameBorder;
  const themeBg = store.getState().theme.classNameBg;

  // ==============================
  const handleSignout = () => {
    store.dispatch(authCleanAction());
  };
  // ==============================
  return (
    <>
      <div className="flex justify-content-between lg:justify-content-start align-items-center pt-2 pb-2 pl-4 pr-4  shadow-2 surface-section surface-border relative lg:static z-1">
        <div className="flex">
          {!isTabletOrMobile && (
            <>
              <Button
                ref={btnRefBars}
                className={`p-button m-1 ${themeBg} ${themeBorder} `}
                onClick={() => {
                  store.dispatch(authShowMenuAction(true));
                }}
              >
                <i className="pi pi-bars text-3xl " />
                <Ripple />
              </Button>
            </>
          )}
        </div>
        <img
          src={imageResultfacil3}
          alt="logo2"
          height="30"
          className="block lg:hidden"
        />
        <StyleClass
          nodeRef={btnRefBarsMobile}
          selector="@next"
          enterClassName="hidden"
          enterActiveClassName="fadein"
          leaveToClassName="hidden"
          leaveActiveClassName="fadeout"
          hideOnOutsideClick
        >
          <Button
            ref={btnRefBarsMobile}
            className={`p-button p-button-primary ml-1 ml-2 block lg:hidden ${themeBg} ${themeBorder}`}
          >
            <i className="pi pi-ellipsis-v text-2xl" />
            <Ripple />
          </Button>
        </StyleClass>
        <ul
          className="list-none p-0 m-0 hidden lg:flex lg:align-items-center select-none lg:flex-row lg:w-full
    surface-section border-1 lg:border-none surface-border right-0 top-100 z-1 shadow-2 lg:shadow-none absolute lg:static"
        >
          <li>
            <Button
              className={` ${
                isTabletOrMobile
                  ? `p-button-text ${themeText}`
                  : `p-button p-button-primary p-button-outlined ml-1 ml-2 ${themeText} ${themeBorder}`
              }`}
              onClick={() => {
                navigate("sys/sysprogramfavorite");
              }}
            >
              <i className="mdi mdi-star lg:text-2xl mr-2 lg:mr-0" />
              <span className="block lg:hidden font-medium">Favorites</span>
              <Ripple />
            </Button>
          </li>

          <li>
            <Button
              className={` ${
                isTabletOrMobile
                  ? `p-button-text ${themeText}`
                  : `p-button p-button-primary p-button-outlined ml-1 ml-2 ${themeText} ${themeBorder}`
              }`}
              onClick={() => {
                navigate("sys/sysnotification");
              }}
            >
              <i className="mdi mdi-bell lg:text-2xl mr-2 lg:mr-0 p-overlay-badge">
                <Badge severity="danger" />
              </i>
              <span className="block lg:hidden font-medium">Notifications</span>
              <Ripple />
            </Button>
          </li>
          <li className="border-top-1 surface-border lg:border-top-none lg:ml-auto">
            <Button
              className={` ${
                isTabletOrMobile
                  ? `p-button-text ${themeText}`
                  : `p-button p-button-primary p-button-outlined ml-1 ml-2 ${themeText} ${themeBorder}`
              }`}
              onClick={() => appOnShowMenuProfile(true)}
            >
              <i className="pi pi-user lg:text-2xl mr-2 lg:mr-0 " />
              <span className="block lg:hidden font-medium">Profile</span>
              <Ripple />
            </Button>
          </li>
          <li>
            <Button
              className={` ${
                isTabletOrMobile
                  ? `p-button-text ${themeText}`
                  : `p-button p-button-primary p-button-outlined ml-1 ml-2 ${themeText} ${themeBorder}`
              }`}
              onClick={handleSignout}
            >
              <i className="pi pi-sign-out lg:text-2xl mr-2 lg:mr-0" />
              <span className="block lg:hidden font-medium">Exit</span>
              <Ripple />
            </Button>
          </li>
        </ul>
      </div>
    </>
  );
};
// ==============================
export default AppLayoutMenuHeader;
