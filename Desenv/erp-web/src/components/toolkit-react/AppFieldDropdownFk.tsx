/* eslint-disable no-param-reassign */
/* eslint-disable react/require-default-props */
import { Button } from "primereact/button";
import { Dialog } from "primereact/dialog";
import { Dropdown } from "primereact/dropdown";
import { InputText } from "primereact/inputtext";
import { Paginator } from "primereact/paginator";
import { ProgressSpinner } from "primereact/progressspinner";
import { Skeleton } from "primereact/skeleton";
import { memo, useEffect, useRef } from "react";

import AppFieldDialogHelp from "./bases/AppFieldDialogHelp";
import AppFieldErrors from "./bases/AppFieldErrors";
import AppFieldTitle from "./bases/AppFieldTitle";
import AppVisible from "./bases/AppVisible";
import useDebounce from "./hooks/useDebounce";
import useState from "./hooks/useStateRef";
import IAppProps from "./interface/IAppProp";
import IAppPropErrors from "./interface/IAppPropErrors";
import IAppPropName from "./interface/IAppPropName";

export interface IAppFieldDropdownFkOptions {
  total: number;
  items: Array<object>;
}

interface IAppFieldDropdownFk extends IAppProps, IAppPropErrors, IAppPropName {
  appFormControl?: any;
  appTitle: string;
  appValue?: any;
  appOptions?: IAppFieldDropdownFkOptions;
  appOptionLabel: string;
  appOptionValue: string;
  appDataKey: string;
  appRowsPage?: number;
  appServiceDefault?: Record<any, any>;
  appServiceMethodDefault?: string;
  appServiceFilterDefault?: Record<any, any>;
  appServiceFilterId?: string;
  appServiceFilterDescription?: string;
  appOnChangeAction?: (e: any) => void;
  appOnBlurAction?: (e: any) => void;
  appOnFilterAction?: (e: any) => Promise<any>;
}

const AppFieldDropdownFk: React.FC<IAppFieldDropdownFk> = (
  props: IAppFieldDropdownFk
) => {
  const [displayHelp, setDisplayHelp] = useState(false);
  const [loading, setLoading, loadingRef] = useState<boolean>(false);
  const [Items, setItems] = useState<any>([]);
  const [filter, setFilter, filterRef] = useState<any>("");
  const [show, setShow, showRef] = useState<any>(false);
  const filterInputRef = useRef<any>();
  const [pageCurrent, setPageCurrent, pageCurrentRef] = useState<number>(0);
  const [pageRowFirst, setPageRowFirst] = useState<number>(1);
  const [pageRowTotalRecords, setPageRowTotalRecords] = useState<number>(1);
  const [dropdownData, setDropdownData] = useState<IAppFieldDropdownFkOptions>({
    total: 0,
    items: [],
  });

  const valueAux =
    props.appValue ?? props.appFormControl.getValues()[props.name];

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

  useEffect(() => {
    let options = props?.appOptions;
    if (!options) {
      options = dropdownData;
    }
    if (!options?.items) {
      setItems([
        { [props.appOptionValue]: null, [props.appOptionLabel]: null },
      ]);
      setPageRowTotalRecords(1);
    } else {
      // console.log("appOptions", appOptions);
      setItems(options.items);
      setPageRowTotalRecords(options.total);
    }
  }, [props.appOptions, dropdownData]);
  // ==============================

  const onFilterReset = (options: any) => {
    setFilter("");
    options.reset();
    filterInputRef && filterInputRef.current.focus();
  };
  // ==============================

  const handleDropdownFktId = async (e: any): Promise<any> => {
    if (
      props.appServiceDefault &&
      props.appServiceFilterDescription &&
      props.appServiceFilterId
    ) {
      const filterAux = {
        filter: {
          and: {
            [props.appServiceFilterDescription]: { like: e.filter || "%" },
            [props.appServiceFilterId]: { like: e.value || "%" },
          },
        },
      };

      let serviceMethodDefault = "list";
      if (props.appServiceMethodDefault) {
        serviceMethodDefault = props.appServiceMethodDefault;
      }
      const result = await props.appServiceDefault[serviceMethodDefault]({
        pfilters: props.appServiceFilterDefault
          ? props.appServiceFilterDefault
          : filterAux,
        ppage: e.page || 1,
        pper_page: props.appRowsPage ? props.appRowsPage : 5,
      });
      setDropdownData(result);
    }
  };
  // ==============================

  const onFilter = async (event: any, options: any) => {
    setLoading(true);
    const filterAux = event.target.value;
    setFilter(filterAux);
    const paramsFilter = {
      value: valueAux,
      filter: filterAux,
      page: valueAux
        ? 1
        : (pageCurrentRef.current ? pageCurrentRef.current : 0) + 1,
    };

    if (props.appOnFilterAction != undefined) {
      await props.appOnFilterAction(paramsFilter);
    } else {
      await handleDropdownFktId(paramsFilter);
    }

    setLoading(false);
  };
  // ==============================

  const onPageChange = (event: any) => {
    setPageRowFirst(event.first);
    setPageCurrent(event.page);
    onFilter({ target: { value: filterInputRef.current.value } }, null);
  };
  // ==============================

  const refreshFilter = () => {
    if (valueAux == undefined || valueAux == "" || valueAux == null) {
      setItems([]);
    } else {
      onFilter({ target: { value: filterInputRef?.current?.value } }, null);
    }
  };
  // ==============================

  const filterTemplate = (options: any) => {
    const { filterOptions } = options;
    // ==============================
    const filterAux = filter ?? "";
    return (
      <div className="flex flex-column gap-1  ">
        <div
          className="flex p-2 justify-content-around"
          style={{ borderTopRightRadius: "5px", borderTopLeftRadius: "5px" }}
        >
          <InputText
            value={filterAux}
            ref={filterInputRef}
            onChange={(e) => onFilter(e, filterOptions)}
            className="col-10"
          />
          <Button
            className=" p-button-rounded p-button-danger "
            icon="pi pi-times"
            onClick={() => onFilterReset(filterOptions)}
          />
        </div>

        <Paginator
          className="col-12 m-0 border-noround"
          first={pageRowTotalRecords == 1 ? 1 : pageRowFirst}
          rows={props.appRowsPage ? props.appRowsPage : 5}
          totalRecords={pageRowTotalRecords}
          onPageChange={onPageChange}
        />
      </div>
    );
  };
  // ==============================

  const handleQueryValue = (): string => {
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
        return item[props.appDataKey] == e.target.value;
      });

      props.appFormControl.handleChange(e);

      const eObj = {
        target: {
          name: `${e.target.name}_obj`,
          value: itemFiltered[0],
        },
      };
      props.appFormControl.handleChange(eObj);
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
    refreshFilter();
  }, [valueAux]);
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

        <Dropdown
          className="w-full"
          id={props.id}
          name={props.name}
          value={handleQueryValue()}
          options={Items}
          optionLabel={props.appOptionLabel}
          optionValue={props.appOptionValue}
          dataKey={props.appDataKey}
          onBlur={handleQueryBlur}
          onChange={handleQueryChange}
          filter
          showClear
          showFilterClear
          showOnFocus
          dropdownIcon={loading ? "pi pi-spinner" : "pi pi-chevron-down"}
          filterTemplate={filterTemplate}
          onShow={() => {
            setShow(true);
            onFilter({ target: { value: filterInputRef.current.value } }, null);
            filterInputRef && filterInputRef.current.focus();
          }}
          onHide={() => {
            setShow(false);
          }}
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
