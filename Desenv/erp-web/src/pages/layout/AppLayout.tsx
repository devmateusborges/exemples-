import { ScrollTop } from "primereact/scrolltop";
import React, { useEffect, useState } from "react";
import { useMediaQuery } from "react-responsive";
import { Outlet } from "react-router-dom";

import useMousePosition from "../../components/toolkit-react/hooks/useMousePosition";
import IAppProps from "../../components/toolkit-react/interface/IAppProp";
import store, { useAppSelector } from "../../store";
import { authMenuIndexAction, authShowMenuAction } from "../../store/AuthStore";
import { ConstUtil } from "../../utils/ConstUtil";
import AppLayoutFooter from "./AppLayoutFooter";
import AppLayoutMenu from "./AppLayoutMenu";
import AppLayoutMenuHeader from "./AppLayoutMenuHeader";
import AppLayoutMenuProfile from "./AppLayoutMenuProfile";

interface IAppLayout extends IAppProps {}

const AppLayout: React.FC<IAppLayout> = ({ className }: IAppLayout) => {
  // ==============================
  const [showMenuProfile, setShowMenuProfile] = useState(false);
  const indexTabMenu = useAppSelector((state) => state.auth.menuIndex);
  const isTabletOrMobile = useMediaQuery({
    query: ConstUtil.cisTabletOrMobile,
  });

  // ==============================
  return (
    <>
      <AppLayoutMenu appIndexTabMenu={indexTabMenu} />

      <div
        className="h-full max-w-full flex scalein animation-duration-500 "
        style={{ marginLeft: isTabletOrMobile ? "65px" : "192px" }}
      >
        <div className="h-full w-full flex flex-column">
          <AppLayoutMenuProfile
            appShowMenuProfile={showMenuProfile}
            appOnShowMenuProfile={(show) => {
              setShowMenuProfile(show);
            }}
          />
          <AppLayoutMenuHeader
            appOnShowMenuProfile={() => {
              setShowMenuProfile(!showMenuProfile);
            }}
          />
          <div
            className="overflow-auto h-full flex-grow-1 flex md:pr-3 md:pl-3 pt-3 flex-column mb-2 "
            onMouseEnter={() => {
              store.dispatch(authShowMenuAction(false));
            }}
          >
            <Outlet />
            <ScrollTop
              target="parent"
              threshold={800}
              className="app-custom-scrolltop p-4"
            />
          </div>

          <AppLayoutFooter />
        </div>
      </div>
    </>
  );
};
// ==============================
export default AppLayout;
