/* eslint-disable consistent-return */
/* eslint-disable react/require-default-props */
import _ from "lodash";
import moment, { MomentInput } from "moment";
import { locale, addLocale } from "primereact/api";
import { Calendar } from "primereact/calendar";
import { memo, useEffect, useRef, useState } from "react";
import AppFieldDialogHelp from "./bases/AppFieldDialogHelp";
import AppFieldErrors from "./bases/AppFieldErrors";
import AppFieldTitle from "./bases/AppFieldTitle";
import IAppProps from "./interface/IAppProp";
import IAppPropErrors from "./interface/IAppPropErrors";
import IAppPropName from "./interface/IAppPropName";

interface IAppFieldDate extends IAppProps, IAppPropErrors, IAppPropName {
  appFormControl?: any;
  appTitle: string;
  appValue?: any;
  ref?: any;
  appDateFormat?: string;
  appShowTime?: boolean;
  appTimeOnly?: boolean;
  appShowSeconds?: boolean;
  appView?: string;
  appOnChangeAction?: (e: any) => void;
  appOnBlurAction?: (e: any) => void;
  appOnFocusAction?: (e: any) => void;
  appOnInputAction?: (e: any) => void;
  appOnSelectAction?: (e: any) => void;
}

const AppFieldDate: React.FC<IAppFieldDate> = (props: IAppFieldDate) => {
  // ==============================
  const [displayHelp, setDisplayHelp] = useState(false);
  const op = useRef<Calendar>(null);
  const [error, setError] = useState<any>(undefined);
  // ==============================
  useEffect(() => {
    if (props?.appFormControl) {
      setError([props.appFormControl.getErrors()[props.name]]);
    } else {
      setError(props.appErrors);
    }
  }, [props.appFormControl?.getErrors()[props.name], props.appErrors]);
  // ==============================
  addLocale("br", {
    firstDayOfWeek: 1,
    dayNames: [
      "domingo",
      "segunda",
      "terça",
      "quarta",
      "quinta",
      "sexta",
      "sábado",
    ],
    dayNamesShort: ["dom", "seg", "ter", "qua", "qui", "sex", "sáb"],
    dayNamesMin: ["D", "S", "T", "Q", "Q", "S", "S"],
    monthNames: [
      "Janeiro",
      "fevereiro",
      "março",
      "abril",
      "maio",
      "junho",
      "julho",
      "agosto",
      "setembro",
      "outubro",
      "novembro",
      "dezembro",
    ],
    monthNamesShort: [
      "jan",
      "fev",
      "mar",
      "abr",
      "mai",
      "jun",
      "jul",
      "ago",
      "sep",
      "out",
      "nov",
      "dez",
    ],
    today: "Hoje",
    clear: "Limpar",
  });

  locale("br");
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
        <div className="flex flex-row">
          <AppFieldTitle required={props.appRequired} title={props.appTitle} />
          <AppFieldDialogHelp
            title={props.appTitle}
            helpText={props.appHelpText}
            displayHelp={displayHelp}
            onDisplayHelp={setDisplayHelp}
          />
        </div>

        <Calendar
          ref={props.ref ?? op}
          id={props.id}
          name={props.name}
          view={props.appView}
          className="w-full"
          showTime={props.appShowTime ? props.appShowTime : false}
          timeOnly={props.appTimeOnly ? props.appTimeOnly : false}
          showSeconds={props.appShowSeconds ? props.appShowSeconds : false}
          inputClassName="w-full"
          value={(() => {
            let date = null;
            if (props.appFormControl != undefined) {
              date = props.appFormControl.getValues()[props.name];
            } else {
              date = props.appValue;
            }
            // console.log("AppFieldDate", date);
            if (!_.isNull(date as string) && !_.isEmpty(date)) {
              if ((date as string).indexOf("T") <= 0) {
                date += "T00:00:00";
              }
              return moment(
                date as MomentInput,
                "YYYY-MM-DDTHH:mm:ss"
              ).toDate();
            }
            return undefined;
          })()}
          dateFormat={
            props.appDateFormat == undefined ? "dd/mm/yy" : props.appDateFormat
          }
          showIcon
          onChange={(e) => {
            let eAux = null;
            const dateValid =
              e?.target?.value instanceof Date && !_.isNull(e?.target?.value);
            if (dateValid) {
              const eValue = e?.target?.value;
              const eValueDate = moment(eValue as MomentInput);
              let eValueDateAux = null;
              if (props.appTimeOnly) {
                const eValueDateHourAux = eValueDate.format("HH:mm:ss");
                eValueDateAux = `1900-01-01T${eValueDateHourAux}`;
              } else {
                eValueDateAux = eValueDate.format("YYYY-MM-DDTHH:mm:ss");
              }

              eAux = {
                target: { name: props.name, value: eValueDateAux },
              };
            } else {
              eAux = { target: { name: props.name, value: undefined } };
            }
            if (props.appOnChangeAction != undefined) {
              props.appOnChangeAction(eAux);
            } else if (props.appFormControl != undefined) {
              props.appFormControl.handleChange(eAux);
            }
          }}
          onFocus={(e) => {
            if (props.appOnFocusAction != undefined) {
              props.appOnFocusAction(e);
            }
          }}
          onBlur={(e) => {
            if (props.appOnBlurAction != undefined) {
              props?.appOnBlurAction(e);
            } else if (props.appFormControl != undefined) {
              props.appFormControl.handleBlur(e);
            }
          }}
          onInput={(e) => {
            if (props.appOnInputAction != undefined) {
              props?.appOnInputAction(e);
            }
          }}
          onSelect={(e) => {
            if (props.appOnSelectAction != undefined) {
              props?.appOnSelectAction(e);
            }
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
// ==============================
export default memo(AppFieldDate);
