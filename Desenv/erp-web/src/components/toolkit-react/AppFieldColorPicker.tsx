import { memo, useEffect, useState } from "react";
import { SketchPicker, ColorChangeHandler } from "react-color";
import AppFieldDialogHelp from "./bases/AppFieldDialogHelp";
import AppFieldErrors from "./bases/AppFieldErrors";
import AppFieldTitle from "./bases/AppFieldTitle";
import IAppProps from "./interface/IAppProp";
import IAppPropErrors from "./interface/IAppPropErrors";
import IAppPropName from "./interface/IAppPropName";

interface IAppFieldColorPicker extends IAppProps, IAppPropErrors, IAppPropName {
  appTitle: string;
  appOnChangeAction?: any;
  appFormControl: any;
  appValue?: string;
  appReturnType?: "rgb" | "hsl" | "hex";
}

const AppFieldColorPicker: React.FC<IAppFieldColorPicker> = (
  props: IAppFieldColorPicker
) => {
  const [error, setError] = useState<any>(undefined);
  const [displayHelp, setDisplayHelp] = useState(false);

  // ==============================

  useEffect(() => {
    if (props.appFormControl) {
      setError([props.appFormControl.getErrors()[props.name]]);
    } else {
      setError(props.appErrors);
    }
  }, [props.appFormControl?.getErrors()[props.name], props.appErrors]);
  // ==============================

  const handleQueryValue = (): string | undefined => {
    const valueAux = props?.appValue;

    if (props.appFormControl) {
      return props.appFormControl.getValues()[props.name];
    }
    return valueAux ?? undefined;
  };

  // ==============================

  const handleQueryChange = (data: any) => {
    if (props.appOnChangeAction != undefined) {
      props.appOnChangeAction(data);
    } else if (props.appFormControl != undefined) {
      const value = data[props.appReturnType ?? "rgb"];
      props.appFormControl.setValueField(props.name, value);
    }
  };

  return (
    <div
      className={
        props.className ? props.className : "col-12 md:col-3 lg:col-3 xl:col-3"
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
      <div className="p-2 ">
        <SketchPicker color={handleQueryValue()} onChange={handleQueryChange} />
      </div>
      <AppFieldErrors
        appErrors={(() => {
          return error;
        })()}
      />
    </div>
  );
};

export default memo(AppFieldColorPicker);
