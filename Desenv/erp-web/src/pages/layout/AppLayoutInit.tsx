import { useMediaQuery } from "react-responsive";

import IAppProps from "../../components/toolkit-react/interface/IAppProp";
import store from "../../store";
import { ConstUtil } from "../../utils/ConstUtil";
import { imageResultfacil3branco } from "../../utils/ImageUtil";

interface IAppLayoutInit extends IAppProps {}
const AppLayoutInit: React.FC<IAppLayoutInit> = (props: IAppLayoutInit) => {
  // ==============================
  const isTabletOrMobile = useMediaQuery({
    query: ConstUtil.cisTabletOrMobile,
  });
  // ==============================
  const themeBg = store.getState().theme.classNameBg;
  // ==============================
  return (
    <>
      <div
        className="overflow-auto w-full h-screen flex align-items-center justify-content-center"
        style={{
          backgroundImage: `url(${`${process.env.PUBLIC_URL}/img/resultfacil.jpg`})`,
          backgroundRepeat: "no-repeat",
        }}
      >
        <div className="flex md:w-8 w-12 lg:flex-row lg:h-auto h-full w-full flex-column shadow-1 border-round-md">
          <div
            className={`flex align-items-center justify-content-center flex-column ${themeBg} fg:w-8 w-12`}
            style={{
              borderBottomLeftRadius: isTabletOrMobile ? "0px" : "15px",
              borderTopLeftRadius: isTabletOrMobile ? "0px" : "15px",
            }}
          >
            <img src={imageResultfacil3branco} alt="logo" className="w-8" />
            <h3 className="text-white">
              Build - {process.env.REACT_APP_VERSION_BUILD}
            </h3>
          </div>
          {props.children}
        </div>
      </div>
    </>
  );
};
// ==============================
export default AppLayoutInit;
