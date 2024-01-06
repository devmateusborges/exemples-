import { Skeleton } from "primereact/skeleton";
import { Link } from "react-router-dom";

import AppContainer from "../../components/toolkit-react/AppContainer";
import IAppProps from "../../components/toolkit-react/interface/IAppProp";
import { imageResultfacil3 } from "../../utils/ImageUtil";
import AppLayoutLoading from "./AppLayoutLoading";
import store, { useAppSelector } from "../../store";
import AppContainerTitle from "../../components/toolkit-react/AppContainerTitle";

interface IAppLayoutMenuNotification extends IAppProps {}

const AppLayoutMenuNotification: React.FC<IAppLayoutMenuNotification> = ({
  children,
  className,
}: IAppLayoutMenuNotification) => {
  const textloading = useAppSelector((state) => state.util.textloading);
  // ==============================
  return (
    <>
      <AppLayoutLoading text={textloading} />
      <AppContainer className="">
        <AppContainerTitle
          appClassTitleBg={store.getState().theme.classNameTitleBg}
          appClassTitleText={store.getState().theme.classNameTitleText}
          appTitle="Notification"
        />

        <h1>Notification</h1>
      </AppContainer>
    </>
  );
};
// ==============================
export default AppLayoutMenuNotification;
