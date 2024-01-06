import { ProgressBar } from "primereact/progressbar";
import React from "react";

import AppVisible from "../../components/toolkit-react/bases/AppVisible";
import IAppProps from "../../components/toolkit-react/interface/IAppProp";

interface IAppLayoutLoading extends IAppProps {
  text: string | null;
}

const AppLayoutLoading: React.FC<IAppLayoutLoading> = (
  props: IAppLayoutLoading
) => {
  // ==============================
  return (
    <>
      <AppVisible visible={props.text}>
        <div
          style={{ zIndex: 9999 }}
          className="flex flex-column fixed w-full fadein animation-duration-1000"
        >
          <ProgressBar
            mode="indeterminate"
            className="w-full"
            style={{ height: "0.5em" }}
          />
          <div className="w-full flex fixed justify-content-center opacity-70">
            <h2 className="p-2 pl-3 pr-3 border-round-md surface-700 text-50 text-base">
              {props.text}
            </h2>
          </div>
        </div>
      </AppVisible>
    </>
  );
};
// ==============================
export default AppLayoutLoading;
