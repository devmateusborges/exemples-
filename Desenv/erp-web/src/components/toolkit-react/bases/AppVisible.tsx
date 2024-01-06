import { memo } from "react";

import IAppProps from "../interface/IAppProp";

interface IAppVisible extends IAppProps {
  visible: boolean | undefined | string | null;
}

const AppVisible: React.FC<IAppVisible> = ({
  className,
  children,
  visible,
}: IAppVisible) => {
  return (
    <>
      {(() => {
        if (visible === "" || !visible) {
          return <></>;
        }
        return <>{children}</>;
      })()}
    </>
  );
};

export default memo(AppVisible);
