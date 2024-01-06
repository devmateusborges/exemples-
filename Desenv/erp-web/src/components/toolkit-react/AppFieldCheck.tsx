/* eslint-disable react/require-default-props */
import { locale, addLocale } from "primereact/api";
import { Checkbox } from "primereact/checkbox";
import { memo, useEffect, useLayoutEffect, useRef, useState } from "react";

import AppFieldDialogHelp from "./bases/AppFieldDialogHelp";
import AppFieldErrors from "./bases/AppFieldErrors";
import AppFieldTitle from "./bases/AppFieldTitle";
import IAppProps from "./interface/IAppProp";
import IAppPropErrors from "./interface/IAppPropErrors";
import IAppPropName from "./interface/IAppPropName";

interface IAppFieldCheck extends IAppProps, IAppPropErrors, IAppPropName {
  appFormControl?: any;
  appTitle: string;
  appValue?: any;
  ref?: Checkbox | undefined;
  appTrueValue?: any;
  appTrueValueLabel?: string;
  appFalseValue?: any;
  appFalseValueLabel?: string;
  appCode?: string;
  appDescription?: string;
  appOnBlurAction?: (e: any) => void;
  appOnChangeAction?: (e: any) => void;
}

const AppFieldCheck: React.FC<IAppFieldCheck> = (props: IAppFieldCheck) => {
  // ==============================
  const [displayHelp, setDisplayHelp] = useState(false);
  const op = useRef<Checkbox | undefined>(props.ref);
  // ==============================

  const handleObj = (value: any) => {
    const eObj = {
      target: {
        type: "check_obj",
        name: `${props.name}_obj`,
        value: {
          [props.appCode ?? "code"]:
            value == props?.appTrueValue
              ? props?.appTrueValue
              : props?.appFalseValue,
          [props.appDescription ?? "description"]:
            value == props?.appTrueValue
              ? props?.appTrueValueLabel ?? "True"
              : props?.appFalseValueLabel ?? "False",
        },
      },
    };
    props.appFormControl?.handleChange(eObj);
  };
  // ==============================

  useEffect(() => {
    handleObj(props.appFormControl?.getValues()[props.name]);
  }, [
    props.appFormControl?.getValues()[props.name],
    props.appFormControl?.getValues()["rerender"],
  ]);
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
        <div className="flex">
          <AppFieldTitle required={props.appRequired} title={props.appTitle} />
          <AppFieldDialogHelp
            title={props.appTitle}
            helpText={props.appHelpText}
            displayHelp={displayHelp}
            onDisplayHelp={setDisplayHelp}
          />
        </div>

        <div className="p-2 pl-3 ">
          <Checkbox
            /* ref={op} */
            name={props.name}
            checked={(() => {
              const value =
                props.appValue ?? props.appFormControl?.getValues()[props.name];
              return value;
            })()}
            trueValue={props.appTrueValue}
            falseValue={props.appFalseValue}
            onBlur={(e) => {
              if (props?.appOnBlurAction) {
                props.appOnBlurAction(e);
              } else if (props.appFormControl != undefined) {
                props.appFormControl?.handleBlur(e);
              }
            }}
            onChange={(e) => {
              if (props?.appOnChangeAction) {
                props.appOnChangeAction(e);
              } else if (props.appFormControl != undefined) {
                props.appFormControl?.handleChange(e);
                handleObj(e.checked);
              }
            }}
          />
        </div>
        <AppFieldErrors
          appErrors={(() => {
            if (props.appFormControl != undefined) {
              return [props.appFormControl?.getTouchedErrors(props.name)];
            }
            return props.appErrors;
          })()}
        />
      </div>
    </>
  );
};

export default memo(AppFieldCheck);
