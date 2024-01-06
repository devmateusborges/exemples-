/* eslint-disable react/require-default-props */
import { Dialog } from "primereact/dialog";
import { Password } from "primereact/password";
import { memo, useEffect, useState } from "react";

import AppFieldDialogHelp from "./bases/AppFieldDialogHelp";
import AppFieldErrors from "./bases/AppFieldErrors";
import AppFieldTitle from "./bases/AppFieldTitle";
import AppVisible from "./bases/AppVisible";
import IAppProps from "./interface/IAppProp";
import IAppPropErrors from "./interface/IAppPropErrors";
import IAppPropName from "./interface/IAppPropName";

interface IAppFieldPassword extends IAppProps, IAppPropErrors, IAppPropName {
  appFormControl?: any;
  appTitle: string;
  appValue?: string;
  appAutoComplete?: string;
  appOnChangeAction?: (e: any) => void;
  appOnBlurAction?: (e: any) => void;
}

const AppFieldPassword: React.FC<IAppFieldPassword> = (
  props: IAppFieldPassword
) => {
  // ==============================
  const [displayHelp, setDisplayHelp] = useState(false);
  const [error, setError] = useState<any>(undefined);
  // ==============================
  useEffect(() => {
    if (props.appFormControl) {
      setError([props.appFormControl.getErrors()[props.name]]);
    } else {
      setError(props.appErrors);
    }
  }, [props.appFormControl?.getErrors()[props.name], props.appErrors]);
  // ==============================

  const handleQueryValue = (): string => {
    let valueAux = props.appValue;

    if (props?.appFormControl) {
      valueAux = props.appFormControl.getValues()[props.name];
    }

    return valueAux ?? "";
  };

  // ==============================

  const handleQueryChange = (e: any) => {
    if (props.appOnChangeAction != undefined) {
      props.appOnChangeAction(e);
    } else if (props.appFormControl != undefined) {
      props.appFormControl.setValueField(props.name, e.target.value);
    }
  };
  // ==============================

  return (
    <>
      <div
        className={
          props.className
            ? props.className
            : "col-12 md:col-3 lg:col-3 xl:col-3"
        }
      >
        <AppVisible visible={props.appTitle}>
          <div className="">
            <AppFieldTitle
              required={props.appRequired}
              title={props.appTitle}
            />
            <AppFieldDialogHelp
              title={props.appTitle}
              helpText={props.appHelpText}
              displayHelp={displayHelp}
              onDisplayHelp={setDisplayHelp}
            />
          </div>
        </AppVisible>
        <Password
          id={props.id}
          autoComplete={props.appAutoComplete}
          name={props.name}
          value={handleQueryValue()}
          onChange={handleQueryChange}
        />
        <AppFieldErrors
          appErrors={(() => {
            return error;
          })()}
        />
      </div>
    </>
  );
};

export default memo(AppFieldPassword);
