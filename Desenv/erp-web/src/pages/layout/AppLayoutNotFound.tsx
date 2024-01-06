import { Skeleton } from "primereact/skeleton";
import { Link } from "react-router-dom";

import AppContainer from "../../components/toolkit-react/AppContainer";
import IAppProps from "../../components/toolkit-react/interface/IAppProp";
import { imageResultfacil3 } from "../../utils/ImageUtil";

interface IAppNotFound extends IAppProps {}

const AppNotFound: React.FC<IAppNotFound> = ({
  children,
  className,
}: IAppNotFound) => {
  // ==============================
  return (
    <>
      <AppContainer className="">
        <div className="flex  flex-column align-items-center">
          <Link to="/private">
            <img src={imageResultfacil3} alt="logo1" height="100" width="180" />
          </Link>
          <div className="field col-12 md:col-6">
            <Skeleton className="mb-2" />
            <Skeleton width="10rem" className="mb-2" />
            <Skeleton width="5rem" className="mb-2" />
            <Skeleton height="2rem" className="mb-2" />
            <Skeleton width="10rem" height="4rem" />
          </div>
          <h1>Page not found</h1>
        </div>
        {children}
      </AppContainer>
    </>
  );
};
// ==============================
export default AppNotFound;
