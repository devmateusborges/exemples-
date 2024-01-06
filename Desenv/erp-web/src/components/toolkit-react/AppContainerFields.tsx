/* eslint-disable react/require-default-props */
import { Fieldset } from "primereact/fieldset";
import { memo } from "react";

import IAppProps from "./interface/IAppProp";

interface IAppContainerFields extends IAppProps {
  title?: string;
  classNameParent?: string;
}

const AppContainerFields: React.FC<IAppContainerFields> = (
  props: IAppContainerFields
) => {
  // ==============================
  return <div className="grid m-0 ">{props.children}</div>;
};

export default memo(AppContainerFields);
