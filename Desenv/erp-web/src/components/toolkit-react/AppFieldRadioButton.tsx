/* eslint-disable react/require-default-props */
/* eslint func-names: ["error", "never"] */
import { Dialog } from "primereact/dialog";
import { RadioButton } from "primereact/radiobutton";
import { memo, useEffect, useState } from "react";

import AppFieldDialogHelp from "./bases/AppFieldDialogHelp";
import AppFieldErrors from "./bases/AppFieldErrors";
import AppFieldTitle from "./bases/AppFieldTitle";
import IAppProps from "./interface/IAppProp";
import IAppPropErrors from "./interface/IAppPropErrors";
import IAppPropName from "./interface/IAppPropName";

interface IAppFieldpRadioButton
  extends IAppProps,
    IAppPropErrors,
    IAppPropName {
  appFormControl?: any;
  appTitle: string;
  appValue?: string;
  appOptions: Array<Record<any, any>>;
  appOptionsLabel: string;
  appOptionsValue: string;
  appInputType?: string;
  appAutoComplete?: string;
  appOnChangeAction?: (e: any) => void;
  appOnBlurAction?: (e: any) => void;
}

const AppFieldRadioButton: React.FC<IAppFieldpRadioButton> = (
  props: IAppFieldpRadioButton
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

  const handleQueryBlur = (e: any) => {
    if (props.appOnBlurAction != undefined) {
      props.appOnBlurAction(e);
    } else if (props.appFormControl != undefined) {
      props.appFormControl.handleBlur(e);
    }
  };
  // ==============================

  const handleQueryChange = (e: any) => {
    if (props.appOnChangeAction != undefined) {
      props.appOnChangeAction(e);
    } else if (props.appFormControl != undefined) {
      /* props.appFormControl.handleChange(e); */
      props.appFormControl.setValueField(props.name, e.target.value);
    }
    handleQueryBlur(e);
  };
  // ==============================
  function radio(props: IAppFieldpRadioButton) {
    if (props.appOptions) {
      const res = props.appOptions.map((opt: any) => {
        return (
          <div
            key={props.id + opt[props.appOptionsValue]}
            className="flex pl-2 pb-1"
          >
            <RadioButton
              id={props.id + opt[props.appOptionsValue]}
              inputId={opt[props.appOptionsValue]}
              name={props.name}
              value={opt[props.appOptionsValue]}
              onChange={handleQueryChange}
              onClick={() => {
                console.log("teste");
              }}
              checked={(() => {
                const valueAux =
                  props.appValue ??
                  props.appFormControl.getValues()[props.name];

                return opt[props.appOptionsValue] === valueAux;
              })()}
            />
            <label
              className="ml-1"
              htmlFor={props.id + opt[props.appOptionsValue]}
            >
              {opt[props.appOptionsLabel]}
            </label>
          </div>
        );
      });
      return res;
    }
    return <></>;
  }
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

        <span className="grid ml-2 mt-1">{radio(props)}</span>
        <AppFieldErrors
          appErrors={(() => {
            return error;
          })()}
        />
      </div>
    </>
  );
};

export default memo(AppFieldRadioButton);
