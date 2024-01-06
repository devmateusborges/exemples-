/* eslint-disable react/require-default-props */

import { Divider } from "primereact/divider";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import IAppProps from "../../components/toolkit-react/interface/IAppProp";
import AppLayoutInit from "./AppLayoutInit";

interface IAppLayoutRedirectPage extends IAppProps {
  text?: string;
  routeRedirect: string;
}

const AppLayoutRedirectPage: React.FC<IAppLayoutRedirectPage> = ({
  children,
  text,
  routeRedirect,
}: IAppLayoutRedirectPage) => {
  // ==============================
  const [count, setCount] = useState(2);
  const navigate = useNavigate();
  // ==============================
  useEffect(() => {
    const interval = setInterval(() => {
      setCount((currentCount) => currentCount - 1);
    }, 1000);

    count === 0 && navigate(routeRedirect);

    return () => clearInterval(interval);
  }, [count, navigate]);
  // ==============================
  return (
    <>
      <AppLayoutInit>
        <div
          className="w-full lg:w-6  p-4 bg-white "
          style={{
            borderBottomRightRadius: "15px",
            borderTopRightRadius: "15px",
          }}
        >
          <div className="flex align-items-center justify-content-center mb-3">
            <span className="text-2xl font-medium text-900">REDIRECT</span>
          </div>

          <Divider align="center" className="my-4" />

          <div className="flex flex-column align-items-center justify-content-center mb-3">
            <span className="text-xl  text-900">
              Redirecting you in <strong> {count}</strong> sec
            </span>
            <span className="text-2xl text-900 text-center mt-3">{text}</span>
            <div className="flex align-items-center justify-content-center mb-3">
              {children}
            </div>
          </div>
        </div>
      </AppLayoutInit>
    </>
  );
};

export default AppLayoutRedirectPage;
