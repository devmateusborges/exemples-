/* eslint-disable react/require-default-props */
import { Dialog } from "primereact/dialog";
import { InputMask } from "primereact/inputmask";
import { memo, useEffect, useState } from "react";

import AppFieldDialogHelp from "./bases/AppFieldDialogHelp";
import AppFieldErrors from "./bases/AppFieldErrors";
import AppFieldTitle from "./bases/AppFieldTitle";
import IAppProps from "./interface/IAppProp";
import IAppPropErrors from "./interface/IAppPropErrors";
import IAppPropName from "./interface/IAppPropName";

interface IAppFieldMask extends IAppProps, IAppPropErrors, IAppPropName {
  appFormControl?: any;
  appTitle: string;
  appValue?: string;
  appMask: string;
  appOnChangeAction?: (e: any) => void;
  appOnBlurAction?: (e: any) => void;
}

const AppFieldMask: React.FC<IAppFieldMask> = (props: IAppFieldMask) => {
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
    let valueAux = props?.appValue;

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
  const handleQueryBlur = (e: any) => {
    if (props.appOnBlurAction != undefined) {
      props.appOnBlurAction(e);
    } else if (props.appFormControl != undefined) {
      props.appFormControl.handleBlur(e);
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
        <div className="">
          <AppFieldTitle required={props.appRequired} title={props.appTitle} />
          <AppFieldDialogHelp
            title={props.appTitle}
            helpText={props.appHelpText}
            displayHelp={displayHelp}
            onDisplayHelp={setDisplayHelp}
          />
        </div>

        <InputMask
          className="w-full"
          id={props.id}
          name={props.name}
          value={handleQueryValue()}
          mask={props.appMask}
          onChange={handleQueryChange}
          onBlur={handleQueryBlur}
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

export default memo(AppFieldMask);
