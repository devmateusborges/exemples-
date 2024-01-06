/* eslint-disable no-throw-literal */
/* eslint-disable prefer-destructuring */

import React, { useEffect, useMemo, useCallback, useLayoutEffect } from "react";

import { v4 as uuid } from "uuid";
import useState from "./useStateRef";

export interface IFieldControl {
  fieldName: string;
  required: [boolean, string];
  defaultValue?: any;
  maxValue?: [number, string];
  minValue?: [number, string];
  regex?: [string, string];
  asyncCustomValidate?: [any, string];
  type?:
    | "text"
    | "date"
    | "datetime"
    | "time"
    | "mask"
    | "numeric"
    | "radio"
    | "checkbox"
    | "foreignkey";
}

export interface IFormControl {
  handleCustomValidate?: (values: any) => any;
  fieldControls?: Array<IFieldControl>;
}

const useFormControl = ({
  handleCustomValidate,
  fieldControls = [],
}: IFormControl) => {
  // ==============================
  const getInitialValue = useCallback(() => {
    const initialValue: any = {};
    for (const f of fieldControls) {
      if (f.defaultValue) {
        initialValue[f.fieldName] = f.defaultValue;
      }
    }

    return initialValue;
  }, []);
  // ==============================
  const [touched, setTouchedFields, touchedRef] = useState<any>({});
  const [errors, setErrors, errorsRef] = useState<any>({});
  const [values, setValues, valuesRef] = useState<any>(getInitialValue());

  // ==============================
  const validateValues = useCallback(
    async (values: any) => {
      // console.log("validateValues", values);
      if (handleCustomValidate !== undefined) {
        const errosAux = await handleCustomValidate(values);

        for (const f of Object.entries(errosAux)) {
          setTouchedFields({
            ...touched,
            [f[0]]: true,
          });
        }
        return errosAux;
      }
      return null;
    },
    [values]
  );
  // ==============================
  const handleCleanError = (fieldName: string) => {
    if (Object.prototype.hasOwnProperty.call(errorsRef.current, fieldName)) {
      delete errorsRef.current[fieldName];
    }
  };
  const handleSetErrors = (fieldName: string, value: string) => {
    const errorFields =
      {
        ...errorsRef.current,
        [fieldName]: value,
      } ?? {};

    setErrors(errorFields);
  };

  const validMinMax = async (f: any) => {
    if (
      (Object.prototype.hasOwnProperty.call(f, "maxValue") && f.maxValue) ||
      (Object.prototype.hasOwnProperty.call(f, "minValue") && f.minValue)
    ) {
      let valueAux = valuesRef.current[f.fieldName];
      if (valueAux !== null && valueAux !== undefined && valueAux !== "") {
        if (f.type == "numeric") {
          valueAux = valueAux.toString().split(".")[0];
        } else if (f.type == "text") {
          valueAux = valueAux.toString();
        }

        if (f.maxValue) {
          if (valueAux.length > f.maxValue[0]) {
            handleSetErrors(f.fieldName, f.maxValue[1]);
            throw "invalid";
          }
        }

        if (f.minValue) {
          if (valueAux.length < f.minValue[0]) {
            handleSetErrors(f.fieldName, f.minValue[1]);
            throw "invalid";
          }
        }
      }
    }
    return true;
  };
  const validRequired = async (f: any) => {
    if (f.required[0]) {
      if (
        valuesRef.current[f.fieldName] == null ||
        valuesRef.current[f.fieldName] == undefined ||
        valuesRef.current[f.fieldName] == ""
      ) {
        handleSetErrors(f.fieldName, f.required[1]);
        throw "invalid";
      }
    }
    return true;
  };
  // ==============================
  const isValid = async () => {
    setErrors({});
    let isValid = true;
    for (const f of fieldControls) {
      const isValidAux = true;
      // TODO implementar demais validacoes
      try {
        await validMinMax(f);
        await validRequired(f);
      } catch (error: any) {
        if (isValid) {
          isValid = false;
        }
      }
    }
    const errorFieldsValidate = await validateValues(values);

    if (errorFieldsValidate && Object.keys(errorFieldsValidate).length != 0) {
      setErrors(errorFieldsValidate);
      return false;
    }
    return isValid;
  };
  // ==============================
  const handleResetForm = useCallback(async () => {
    const reset = values;
    for (const r of Object.entries(reset)) {
      reset[r[0]] = "";
    }

    setValues(reset);
  }, [values]);
  // ==============================
  const setValueField = useCallback(
    async (fieldName: string, value: any) => {
      const valuesAux = { ...valuesRef.current, [fieldName]: value };
      setValues(valuesAux);
      // isValid();
      handleCleanError(fieldName);
    },
    [values]
  );
  // ==============================
  const delField = useCallback(async (fieldName: string) => {
    delete valuesRef.current[fieldName];
    // setValues(valuesAux);
    // isValid();
  }, []);
  // ==============================
  const setValuesForm = useCallback(
    async (dataForm: any) => {
      setValues(dataForm);
    },
    [values]
  );
  // ==============================
  const setValuesDefaultForm = useCallback(async () => {
    setValues(await getInitialValue());

    setValueField("rerender", uuid());
  }, []);
  // ==============================
  const getTouchedErrors = useCallback(
    (field: any) => {
      if (touchedRef.current[field] && errorsRef.current[field]) {
        return errorsRef.current[field] as string;
      }
      return undefined;
    },
    [touched, errors]
  );
  // ==============================
  const getErrors = useCallback(() => {
    return errorsRef.current;
  }, []);
  // ==============================
  const getValues = useCallback(() => {
    return valuesRef.current;
  }, [values]);
  // ==============================
  const handleChange = useCallback(
    (event: any) => {
      const fieldName = event.target?.name;
      let valueAux = "";

      if (event.target?.type === "checkbox") {
        valueAux = event.target?.checked;
      } else if (event.target?.type === "radio") {
        valueAux = event.value;
      } else {
        valueAux = event.target?.value;
      }

      const valuesMerge = {
        ...valuesRef.current,
        [fieldName]: valueAux,
      };
      setValues(valuesMerge);

      // TODO  handleCleanError
      handleCleanError(fieldName);
      // isValid();
    },
    [values]
  );
  // ==============================
  const handleBlur = useCallback(
    (event: any) => {
      // TODO ajustar para file
      const fieldName = event.target?.name;
      setTouchedFields({
        ...touched,
        [fieldName]: true,
      });
      // TODO validar somente o campo do onblur
      // isValid();
    },
    [values]
  );
  // ==============================
  return {
    getValues,
    setValueField,
    setValuesForm,
    setValuesDefaultForm,
    getTouchedErrors,
    touched,
    handleBlur,
    getErrors,
    handleChange,
    handleResetForm,
    isValid,
    fieldControls,
    delField,
  };
};
// ==============================
export default useFormControl;
