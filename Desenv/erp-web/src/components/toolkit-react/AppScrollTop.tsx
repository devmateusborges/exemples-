import { useEffect } from "react";
import { useLocation } from "react-router-dom";

import IAppProps from "./interface/IAppProp";

interface IAppScrollTop extends IAppProps {}

const AppScrollTop: React.FC<IAppScrollTop> = ({ children }: IAppScrollTop) => {
  // ==============================
  const location = useLocation();
  // ==============================
  useEffect(() => {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  }, [location]);

  return <>{children}</>;
};

export default AppScrollTop;
