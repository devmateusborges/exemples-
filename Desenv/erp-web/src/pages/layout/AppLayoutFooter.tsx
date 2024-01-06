import IAppProps from "../../components/toolkit-react/interface/IAppProp";
import store, { useAppSelector } from "../../store";
import AppLayoutLoading from "./AppLayoutLoading";

interface IAppLayoutFooter extends IAppProps {}

const AppLayoutFooter: React.FC<IAppLayoutFooter> = ({
  className,
}: IAppLayoutFooter) => {
  // ==============================
  const textloading = useAppSelector((state) => state.util.textloading);
  const themeBg = store.getState().theme.classNameBg;
  // ==============================
  return (
    <>
      <div
        className={`flex align-items-b app-layout-footer flex-column justify-content-center pl-3 ${themeBg}`}
      >
        <span className="text-white font-bold">
          {process.env.NODE_ENV} - {process.env.REACT_APP_API_URL}
        </span>

        <span className="text-white font-bold">
          build - {process.env.REACT_APP_VERSION_BUILD}
        </span>
        <AppLayoutLoading text={textloading} />
      </div>
    </>
  );
};
// ==============================
export default AppLayoutFooter;
