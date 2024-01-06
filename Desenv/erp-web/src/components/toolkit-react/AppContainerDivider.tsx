/* eslint-disable react/require-default-props */
import { Divider, DividerAlignType } from "primereact/divider";
import { Fieldset } from "primereact/fieldset";
import { memo } from "react";

import IAppProps from "./interface/IAppProp";

interface IAppContainerDivider extends IAppProps {
  appPosition: DividerAlignType;
  appTitle?: string;
  appClassIcon?: string;
}

const AppContainerDivider: React.FC<IAppContainerDivider> = (
  props: IAppContainerDivider
) => {
  // ==============================
  return (
    <Divider align={props.appPosition}>
      <div className="inline-flex align-items-center text-3xl text-800">
        <i
          className={
            props.appClassIcon ? props.appClassIcon : "mdi mdi-table text-3xl "
          }
        />
        <b>{props.appTitle}</b>
      </div>
    </Divider>
  );
};

export default memo(AppContainerDivider);
