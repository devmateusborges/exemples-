/* eslint-disable react/require-default-props */
import { Skeleton } from "primereact/skeleton";
import { memo, useEffect, useState } from "react";

import IAppProps from "./interface/IAppProp";

import { randomArray } from "../../utils/FuncUtil";

interface IAppContainer extends IAppProps {
  loading?: boolean;
  autoClose?: boolean;
  timeClose?: number;
}

const arraySkeleton = randomArray(100);

const AppContainer: React.FC<IAppContainer> = (props: IAppContainer) => {
  // ==============================
  const [openDiv, setOpenDiv] = useState<boolean>(props.loading ?? true);
  // ==============================
  useEffect(() => {
    let timeOut: any = null;
    if (props.autoClose ?? true) {
      timeOut = setTimeout(() => {
        setOpenDiv(false);
      }, props.timeClose || 1000);
    }
    return () => {
      if (timeOut) {
        clearTimeout(timeOut);
      }
    };
  }, []);
  // ==============================
  return (
    <>
      <div
        className={`${props.className} relative  bg-white scalein animation-duration-300 mb-2`}
        style={props.style}
      >
        {openDiv ? (
          <div className="overflow-hidden border-round-sm absolute w-full h-full bg-white z-2 m-0">
            <div className="grid formgrid p-2 relative">
              {arraySkeleton.map((item) => {
                return (
                  <div key={item} className="field col-12 md:col-4">
                    <Skeleton
                      height="1rem"
                      width="6rem"
                      /* borderRadius="0.375rem" */
                      className="mb-2 border-round-md"
                    />
                    <Skeleton
                      height="2rem"
                      /* borderRadius="0.375rem" */
                      className="border-round-md"
                    />
                  </div>
                );
              })}
            </div>
          </div>
        ) : (
          <></>
        )}
        {props.children}
      </div>
    </>
  );
};

export default memo(AppContainer);
