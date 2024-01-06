/* eslint-disable react/require-default-props */
/* eslint no-param-reassign: "error" */
import _ from "lodash";
import { v4 as uuid } from "uuid";
import React, { useEffect, useImperativeHandle } from "react";
import { toast } from "react-toastify";
import AppVisible from "../../components/toolkit-react/bases/AppVisible";
import useState from "../../components/toolkit-react/hooks/useStateRef";
import IAppProps from "../../components/toolkit-react/interface/IAppProp";
import IAppPropName from "../../components/toolkit-react/interface/IAppPropName";
import store from "../../store";
import GenericFormPage, { IGenericFormPage } from "./GenericFormPage";
import GenericListPage, { IGenericListPage } from "./GenericListPage";

interface IGenericFormDet extends IAppProps, IAppPropName {
  appGenericListOptions: IGenericListPage;
  appGenericFormOptions: IGenericFormPage;
  appSetQueryParams?: any;
}

const GenericFormDet = React.forwardRef<any, IGenericFormDet>(
  (props: IGenericFormDet, ref) => {
    const [toggleForm, setToggleForm] = useState(false);
    const { auth } = store.getState();
    const [
      dataTableDataValue,
      setDataTableDataValue,
      dataTableDataValueRef,
    ]: Array<any> = useState([]);
    const dataTableDataKey = "id";

    // ==============================

    useImperativeHandle(ref, () => {
      if (dataTableDataValueRef.current) {
        return dataTableDataValueRef.current;
      }
      return [];
    });
    // ==============================

    const cleanForm = () => {
      props?.appGenericFormOptions?.appFormControl.setValuesDefaultForm();
    };

    const removeItemDataTableValue = async (items: any, column: any) => {
      const keys: Array<string> = [];
      for (const item of items) {
        keys.push(item[column]);
      }
      return dataTableDataValueRef.current.filter((item: any) => {
        return !keys.includes(item[column]);
      });
    };
    // ==============================
    const handleQueryDeleteAux = async (items: any) => {
      const newDataTableDataValue = await removeItemDataTableValue(
        items,
        dataTableDataKey
      );

      /*     if (!res?.error) {
      toast.success(`Record ${obj.code} successfully deleted`);
    } */

      if (newDataTableDataValue != undefined) {
        setDataTableDataValue(newDataTableDataValue);
      }
    };
    const handleQueryDelete = async (items: any) => {
      if (props?.appGenericListOptions?.appOnQueryDelete !== undefined) {
        await props?.appGenericListOptions?.appOnQueryDelete(items);
      } else {
        await handleQueryDeleteAux(items);
      }
    };
    // ==============================

    const handleQueryEditAux = (row: any) => {
      if (row) {
        props?.appGenericFormOptions?.appFormControl.setValuesForm(row[0]);
        setToggleForm(true);
      }
    };
    const handleQueryEdit = (row: any) => {
      if (props?.appGenericListOptions?.appOnQueryEdit !== undefined) {
        props?.appGenericListOptions?.appOnQueryEdit(row);
      } else {
        handleQueryEditAux(row);
      }
    };
    // ==============================

    const handleQueryAddAux = (row: any) => {
      cleanForm();
      setToggleForm(true);
    };
    const handleQueryAdd = (row: any) => {
      if (props?.appGenericListOptions?.appOnQueryAdd !== undefined) {
        props?.appGenericListOptions?.appOnQueryAdd(row);
      } else {
        handleQueryAddAux(row);
      }
    };
    // ============================== FORM

    const handleLoadDataAux = (row: any) => {};
    const handleLoadData = (row: any) => {
      if (props?.appGenericFormOptions?.appOnQueryLoadData !== undefined) {
        props?.appGenericFormOptions?.appOnQueryLoadData(row);
      } else {
        handleLoadDataAux(row);
      }
    };
    // ==============================

    const handleSaveAux = async () => {
      const valid =
        await props?.appGenericFormOptions?.appFormControl.isValid();

      if (valid) {
        const valueForm = _.clone(
          props?.appGenericFormOptions?.appFormControl.getValues()
        );

        if (!Object.prototype.hasOwnProperty.call(valueForm, "id")) {
          valueForm["id"] = uuid();
        }

        const newDataTableDataValue = await removeItemDataTableValue(
          [valueForm],
          dataTableDataKey
        );

        const newValueForm = [...newDataTableDataValue, valueForm];
        setDataTableDataValue(newValueForm);
        cleanForm();
      } else {
        throw props?.appGenericFormOptions?.appFormControl.getErrors();
      }
    };
    const handleSave = async (newRecord = false) => {
      try {
        if (props?.appGenericFormOptions?.appOnQuerySave !== undefined) {
          await props?.appGenericFormOptions?.appOnQuerySave();
        } else {
          await handleSaveAux();
        }

        if (!newRecord) {
          setToggleForm(false);
        }
      } catch (error: any) {
        if (error) {
          for (const f of Object.entries(error)) {
            toast.error(`${f[1]}`);
          }
        }
      }
    };
    // ==============================

    const handleCancel = (row: any) => {
      if (props?.appGenericFormOptions?.appOnQueryCancel !== undefined) {
        props?.appGenericFormOptions?.appOnQueryCancel(row);
      } else {
        setToggleForm(false);
        cleanForm();
      }
    };
    // ==============================

    useEffect(() => {
      if (props.appGenericListOptions.appDataTableDataValue) {
        setDataTableDataValue(
          props.appGenericListOptions.appDataTableDataValue
        );
      } else {
        setDataTableDataValue([]);
      }
    }, [props.appGenericListOptions.appDataTableDataValue]);

    return (
      <>
        <AppVisible visible={!toggleForm}>
          <GenericListPage
            id={props?.appGenericListOptions?.id}
            appProgramId={props?.appGenericListOptions?.appProgramId}
            appTitle={props?.appGenericListOptions?.appTitle}
            appHelpText={props?.appGenericListOptions?.appHelpText}
            appDataTableDataValue={dataTableDataValue}
            appDataTablePaginateMode={
              props?.appGenericListOptions?.appDataTablePaginateMode
            }
            appShowTopBar={props?.appGenericListOptions?.appShowTopBar}
            appDataTableColumns={
              props?.appGenericListOptions?.appDataTableColumns
            }
            appDataTableDataKey={dataTableDataKey}
            appFavoriteVisible={
              props?.appGenericListOptions?.appFavoriteVisible
            }
            appAddVisible={props?.appGenericListOptions?.appAddVisible}
            appDeleteVisible={props?.appGenericListOptions?.appDeleteVisible}
            appEditVisible={props?.appGenericListOptions?.appEditVisible}
            appServiceDefault={props?.appGenericListOptions?.appServiceDefault}
            appButtonExtraTemplateRow={
              props?.appGenericListOptions?.appButtonExtraTemplateRow
            }
            appButtonExtraVisibleRow={
              props?.appGenericListOptions?.appButtonExtraVisibleRow
            }
            appButtonDeleteVisibleRow={
              props?.appGenericListOptions?.appButtonDeleteVisibleRow
            }
            appButtonEditVisibleRow={
              props?.appGenericListOptions?.appButtonEditVisibleRow
            }
            appPreferenceVisible={
              props?.appGenericListOptions?.appPreferenceVisible
            }
            appAddActionCode={props.appGenericListOptions.appAddActionCode}
            appEditActionCode={props.appGenericListOptions.appEditActionCode}
            appDeleteActionCode={
              props.appGenericListOptions.appDeleteActionCode
            }
            appSaveActionCode={props.appGenericListOptions.appSaveActionCode}
            appOnQueryAdd={handleQueryAdd}
            appOnQueryEdit={handleQueryEdit}
            appOnQueryDelete={handleQueryDelete}
            appSetQueryParams={props?.appSetQueryParams}
          />
        </AppVisible>

        <AppVisible visible={toggleForm}>
          <GenericFormPage
            appOnQueryLoadData={handleLoadData}
            appOnQueryCancel={handleCancel}
            appOnQuerySave={handleSave}
            appSaveActionCode={props.appGenericFormOptions.appSaveActionCode}
            appShowTopBar
          >
            {props.children}
          </GenericFormPage>
        </AppVisible>
      </>
    );
  }
);
export default GenericFormDet;
