/* eslint-disable react/require-default-props */
import { values } from "lodash";
import { SelectButton } from "primereact/selectbutton";
import { useState } from "react";
import IAppProps from "./interface/IAppProp";
import IAppPropErrors from "./interface/IAppPropErrors";
import IAppPropName from "./interface/IAppPropName";

interface IAppFieldSelectButtonLang
  extends IAppProps,
    IAppPropErrors,
    IAppPropName {
  appValue?: string;
  appOptions?: any;
  appOptionLabel: string;
  appOptionValue: string;
  justifyTemplate: any;
  appOnChangeAction: (e: any) => void;
}

const AppFieldSelectButtonLang: React.FC<IAppFieldSelectButtonLang> = (
  props: IAppFieldSelectButtonLang
) => {
  return (
    <SelectButton
      value={props.appValue}
      options={props.appOptions}
      onChange={(event) => {
        // console.log(event);

        return props.appOnChangeAction(event);
      }}
      itemTemplate={props.justifyTemplate}
      optionLabel={props.appOptionLabel}
    />
  );
};

export default AppFieldSelectButtonLang;
