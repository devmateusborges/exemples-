import { Button } from "primereact/button";
import { Skeleton } from "primereact/skeleton";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import AppContainer from "../../components/toolkit-react/AppContainer";

import IAppProps from "../../components/toolkit-react/interface/IAppProp";
import { AuthService } from "../../services/AuthService";
import SysProgramActionService from "../../services/modules/sys/SysProgramActionService";
import store, { useAppSelector } from "../../store";
import { authShowMenuAction } from "../../store/AuthStore";
import { imageResultfacil3 } from "../../utils/ImageUtil";
import AppLayoutRedirectPage from "./AppLayoutRedirect";

interface IAppLayoutAuthorization extends IAppProps {
  programId: string;
}

const AppLayoutAuthorization: React.FC<IAppLayoutAuthorization> = (
  props: IAppLayoutAuthorization
) => {
  const [auth, setAuth] = useState<any>(false);
  // ==============================
  useEffect(() => {
    (async () => {
      const result = await AuthService.authListProgram({
        pfilters: {
          filter: {
            and: {
              login: store.getState().auth.auth.user.login,
              pvsysprogramid: props.programId,
            },
          },
        },
        saveCache: false,
      });
      /* console.log("AppLayoutAuthorization", result); */

      if (result.length > 0) {
        setAuth(true);
      } else {
        setAuth(false);
      }
    })();
  }, []);
  // ==============================
  return (
    <>
      {(() => {
        if (auth) {
          return <> {props.children} </>;
        }
        return (
          <>
            <AppContainer className="">
              <div className="flex  flex-column align-items-center mb-2">
                <Link to="/private">
                  <img
                    src={imageResultfacil3}
                    alt="logo1"
                    height="100"
                    width="180"
                  />
                </Link>

                <h1>No authorization to access</h1>
                <a>Id:{props.programId}</a>

                <Button
                  className="p-button-rounded p-button-primary p-button-text text-2xl  m-1 mt-3 mb-3"
                  label="Click for acess menu"
                  onClick={() => {
                    store.dispatch(authShowMenuAction(true));
                  }}
                />
              </div>
            </AppContainer>
          </>
        );
      })()}
    </>
  );
};
// ==============================
export default AppLayoutAuthorization;
