import { useEffect, useState } from "react";

import IAppProps from "../../components/toolkit-react/interface/IAppProp";
import { useAppSelector } from "../../store";
import AppLayoutRedirectPage from "./AppLayoutRedirect";

interface IAppLayoutPrivate extends IAppProps {}

const AppLayoutPrivate: React.FC<IAppLayoutPrivate> = ({
  children,
}: IAppLayoutPrivate) => {
  // ==============================
  const authenticated = useAppSelector((state) => state.auth.auth);
  // console.log("authenticated", authenticated);
  // ==============================
  return (
    <>
      {(() => {
        if (authenticated?.access_token) {
          return <> {children} </>;
        }
        return (
          <>
            <AppLayoutRedirectPage
              text="You are not authenticated"
              routeRedirect="/signin"
            />
          </>
        );
      })()}
    </>
  );
};
// ==============================
export default AppLayoutPrivate;
