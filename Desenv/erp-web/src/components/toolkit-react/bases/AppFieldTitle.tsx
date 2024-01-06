/* eslint-disable react/require-default-props */
import { memo } from "react";

import IAppProps from "../interface/IAppProp";

interface IAppFieldTitle extends IAppProps {
  title?: string;
  required?: boolean;
}

const AppFieldTitle: React.FC<IAppFieldTitle> = (props: IAppFieldTitle) => {
  const onFontRequired = (required: any) => {
    if (required) {
      return "*";
    }
    return "";
  };

  const FontRequired = onFontRequired(props.required);
  return (
    <>
      <label className="ml-1  text-700 font-bold" htmlFor="AppInputText">
        {FontRequired}
        {props.title}
      </label>
    </>
  );
};

export default memo(AppFieldTitle);
