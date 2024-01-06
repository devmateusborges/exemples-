/* eslint-disable no-param-reassign */
/* eslint-disable react/require-default-props */
import { Dropdown } from "primereact/dropdown";
import { memo, useEffect, useRef } from "react";

import AppFieldDialogHelp from "./bases/AppFieldDialogHelp";
import AppFieldErrors from "./bases/AppFieldErrors";
import AppFieldTitle from "./bases/AppFieldTitle";
import useState from "./hooks/useStateRef";
import IAppProps from "./interface/IAppProp";
import IAppPropErrors from "./interface/IAppPropErrors";
import IAppPropName from "./interface/IAppPropName";

interface IAppFieldDropdown extends IAppProps, IAppPropErrors, IAppPropName {
  appFormControl?: any;
  appTitle?: string;
  appValue?: any;
  appOptions?: any;
  appOptionLabel: string;
  appOptionValue: string;
  appFilter?: boolean;
  appPlaceholder?: string;
  appOnChangeAction?: (e: any) => void;
  appOnBlurAction?: (e: any) => void;
}

const AppFieldDropdownFk: React.FC<IAppFieldDropdown> = (
  props: IAppFieldDropdown
) => {
  const [displayHelp, setDisplayHelp] = useState(false);
  const [loading, setLoading, loadingRef] = useState<boolean>(true);
  const [Items, setItems] = useState<any>([]);
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

  const titleTemplate = (props: IAppFieldDropdown) => {
    if (props.appTitle) {
      return (
        <div className="">
          <AppFieldTitle required={props.appRequired} title={props.appTitle} />
          <AppFieldDialogHelp
            title={props.appTitle}
            helpText={props.appHelpText}
            displayHelp={displayHelp}
            onDisplayHelp={setDisplayHelp}
          />
        </div>
      );
    }
    return <></>;
  };
  // ==============================

  const handleQueryValue = (): string => {
    const valueAux = props?.appValue;

    if (props?.appFormControl) {
      return props.appFormControl.getValues()[props.name];
    }
    return valueAux ?? "";
  };
  // ==============================

  const handleQueryChange = (e: any) => {
    if (props.appOnChangeAction != undefined) {
      props.appOnChangeAction(e);
    } else if (props.appFormControl != undefined) {
      const itemFiltered = Items.filter((item: any) => {
        return item[props.appOptionValue] == e.target.value;
      });

      props.appFormControl.setValueField(props.name, e.target.value);

      if (itemFiltered.length > 0) {
        itemFiltered[0]["description"] = itemFiltered[0][props.appOptionLabel];

        const eObj = {
          target: {
            name: `${e.target.name}_obj`,
            value: itemFiltered[0],
          },
        };
        props.appFormControl.handleChange(eObj);
      }
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

  useEffect(() => {
    const options = props?.appOptions;
    if (options) {
      setItems(options);
      setLoading(false);
    }
  }, [props.appOptions]);
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
        {titleTemplate(props)}

        <Dropdown
          className="w-full"
          id={props.id}
          name={props.name}
          value={handleQueryValue()}
          placeholder={props.appPlaceholder}
          options={Items}
          optionLabel={props.appOptionLabel}
          optionValue={props.appOptionValue}
          onBlur={handleQueryBlur}
          onChange={handleQueryChange}
          filter={props.appFilter}
          showClear
          showFilterClear
          showOnFocus
          dropdownIcon={loading ? "pi pi-spinner" : "pi pi-chevron-down"}
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

export default memo(AppFieldDropdownFk);
