import { Button } from "primereact/button";
import { Ripple } from "primereact/ripple";
import { Sidebar } from "primereact/sidebar";
import { StyleClass } from "primereact/styleclass";
import { classNames } from "primereact/utils";
import { useEffect, useRef, useState } from "react";

import IAppProps from "../../components/toolkit-react/interface/IAppProp";

interface IAppLayoutMenuProfile extends IAppProps {
  appShowMenuProfile: boolean;
  appOnShowMenuProfile: (show: boolean) => void;
}

const AppLayoutMenuProfile: React.FC<IAppLayoutMenuProfile> = ({
  className,
  appShowMenuProfile,
  appOnShowMenuProfile,
}: IAppLayoutMenuProfile) => {
  // ==============================
  return (
    <>
      <Sidebar
        visible={appShowMenuProfile}
        position="right"
        onHide={() => appOnShowMenuProfile(false)}
      >
        <h3>PROFILE</h3>
      </Sidebar>
    </>
  );
};
// ==============================
export default AppLayoutMenuProfile;
