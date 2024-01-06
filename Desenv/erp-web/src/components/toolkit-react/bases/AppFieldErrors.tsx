/* eslint-disable react/require-default-props */
import { memo } from "react";

import IAppProps from "../interface/IAppProp";
import IAppPropErrors from "../interface/IAppPropErrors";

interface IAppFieldErrors extends IAppProps, IAppPropErrors {}

const AppFieldErrors: React.FC<IAppFieldErrors> = (props: IAppFieldErrors) => {
  return (
    <>
      {(() => {
        if (Array.isArray(props?.appErrors)) {
          if (props.appErrors?.length > 0) {
            if (props.appErrors[0] !== undefined) {
              return props.appErrors.map((error) => (
                <div key={error}>
                  <small className="p-error  font-white">- {error}</small>{" "}
                  <br />
                </div>
              ));
            }
          }
        }
        return <></>;
      })()}
    </>
  );
};

export default memo(AppFieldErrors);
