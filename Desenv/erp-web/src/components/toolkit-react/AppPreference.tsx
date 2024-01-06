/* eslint-disable react/require-default-props */
import { useEffect } from "react";
import { Button } from "primereact/button";
import { DataTable } from "primereact/datatable";
import { Column } from "primereact/column";
import { toast } from "react-toastify";
import { Dialog } from "primereact/dialog";
import _ from "lodash";
import { confirmDialog } from "primereact/confirmdialog";
import AppFieldDialogHelp from "./bases/AppFieldDialogHelp";
import AppFieldTitle from "./bases/AppFieldTitle";
import AppVisible from "./bases/AppVisible";
import AppFieldText from "./AppFieldText";
import AppFieldCheck from "./AppFieldCheck";
import useFormControl, { IFieldControl } from "./hooks/useFormControl";
import AppTopBar from "./AppTopBar";
import store from "../../store";
import IAppProps from "./interface/IAppProp";
import useState from "./hooks/useStateRef";

interface IAppPreference extends IAppProps {
  appDeleteVisible?: boolean;
  appEditVisible?: boolean;
  appAddVisible?: boolean;
  appSaveVisible?: boolean;
  appCheckVisible?: boolean;
  appServiceDefault?: Record<any, any>;
  appObjectId?: string;
  appObjectSubId?: string | undefined;
  appObjectType?: string;
  appUserId?: string;
  appOnSelected?: any;
  appVisible: any;
  appOnQueryDialogHide: any;
}
const AppPreference: React.FC<IAppPreference> = (props: IAppPreference) => {
  // ==============================
  const [preferenceSelected, setPreferenceSelected] = useState<any>([]);
  const [preferenceOptions, setPreferenceOptions] = useState([]);
  const [toggleForm, setToggleForm] = useState(false);
  const [cancelVisible, setCancelVisible] = useState(false);
  const [addVisible, setAddVisible] = useState(props.appAddVisible);
  const [displayHelp, setDisplayHelp] = useState(false);

  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "preference_description",
      required: [true, "Description is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "isdefault",
      required: [false, ""],
      defaultValue: "N",
      type: "checkbox",
    },
    {
      fieldName: "ispublic",
      required: [false, ""],
      defaultValue: "N",
      type: "checkbox",
    },
  ];
  // ==============================

  const formControl = useFormControl({
    fieldControls,
  });
  // ==============================

  const handleLoadList = async () => {
    if (props.appServiceDefault) {
      const res = await props.appServiceDefault.list({
        psysuserid: props.appUserId,
        pobjectid: props.appObjectId,
        pobjectsubid: props.appObjectSubId,
        pobjecttype: props.appObjectType,
      });
      setPreferenceOptions(res.items);
    }
  };
  // ==============================

  const handleDeleteList = async (rowData: Array<any>) => {
    // console.log(rowData);
    if (props.appServiceDefault) {
      if (rowData.length > 0) {
        for (const data of rowData) {
          const res = await props.appServiceDefault.delete(data.id);
          if (!res?.error) {
            toast.success(
              `Record ${data.preference_description} successfully deleted`
            );
          }
        }
        handleLoadList();
        setPreferenceSelected([]);
      } else {
        toast.warning("Select one or more records to be deleted");
      }
    }
  };

  // ==============================
  const handleEditList = async (rowData: any) => {
    const values = {
      preference_description: rowData.preference_description,
      isdefault: rowData.isdefault,
      ispublic: rowData.ispublic,
      value: rowData.value,
      id: rowData.id,
    };
    formControl.setValuesForm(values);
    setToggleForm(true);
  };
  // ==============================

  const handleSaveFormAux = async (obj: any) => {
    if (props.appServiceDefault) {
      const result = await props.appServiceDefault.save(obj);
      if (result) {
        toast.success("Save successfully");
        props.appOnQueryDialogHide();
      } else {
        formControl.handleResetForm();
      }
    }
  };
  // ==============================

  const handleSaveForm = async () => {
    const isValid = await formControl.isValid();
    if (isValid) {
      const obj = await formControl.getValues();
      // console.log("handleSaveForm-1", obj);
      let objAux = null;

      if (!_.isNull(obj.id as string) && !_.isEmpty(obj.id)) {
        objAux = {
          ...obj,
          id: formControl.getValues().id,
        };
      }

      if (props.appObjectSubId) {
        objAux = {
          ...obj,
          object_type: props.appObjectType,
          sys_user_id: props.appUserId,
          object_id: props.appObjectId,
          object_sub_id: props.appObjectSubId,
        };

        if (!Object.prototype.hasOwnProperty.call(objAux, "value")) {
          objAux["value"] =
            store.getState().pref.dataGridState[props.appObjectSubId];
        }
      }
      console.log("handleSaveForm-2", objAux);
      await handleSaveFormAux(objAux);
      handleLoadList();
      formControl.handleResetForm();
      setToggleForm(false);
    } else {
      for (const f of Object.entries(formControl.getErrors())) {
        toast.error(`${f[1]}`);
      }
    }
  };
  // ==============================

  const handleCancelForm = () => {
    setToggleForm(false);
    formControl.handleResetForm();
  };
  // ==============================

  useEffect(() => {
    (async () => {
      if (props.appVisible) {
        handleLoadList();
      }
    })();
  }, [props.appVisible]);
  // ==============================

  const buttons = (rowData: any) => {
    return (
      <div className="flex flex-row ">
        <AppVisible visible={props.appCheckVisible}>
          <div className="mr-5">
            <Button
              icon="pi pi-check text-xl"
              className="p-button-lg p-button-info"
              onClick={() => {
                if (rowData) {
                  props.appOnSelected(rowData);
                  props.appOnQueryDialogHide();
                }
              }}
            />
          </div>
        </AppVisible>

        <AppVisible visible={props.appSaveVisible}>
          <div className="pr-1">
            <Button
              icon="pi pi-save text-xl"
              className="p-button-lg p-button-primary"
              onClick={async () => {
                confirmDialog({
                  message: "Do you want to save preference ?",
                  header: "Confirmation",
                  icon: "pi pi-question-circle",
                  accept: async () => {
                    const obj = {
                      id: rowData.id,
                      unit_id: store.getState().auth.auth.unit.id,
                      object_type: rowData.object_type,
                      sys_user_id: rowData.sys_user_id,
                      object_id: rowData.object_id,
                      object_sub_id: rowData.object_sub_id,
                      preference_description: rowData.preference_description,
                      value:
                        store.getState().pref.dataGridState[
                          rowData.object_sub_id
                        ],
                      isdefault: rowData.isdefault,
                      ispublic: rowData.ispublic,
                    };

                    await handleSaveFormAux(obj);
                    handleLoadList();
                  },
                });
              }}
            />
          </div>
        </AppVisible>
        <AppVisible visible={props.appDeleteVisible}>
          <div className="pr-1">
            <Button
              icon="pi pi-trash text-xl"
              className="p-button-lg p-button-danger"
              aria-label="Delete"
              onClick={() => {
                confirmDialog({
                  message: "Do you want to delete preference ?",
                  header: "Confirmation",
                  icon: "pi pi-question-circle",
                  accept: () => {
                    handleDeleteList([rowData]);
                  },
                });
              }}
            />
          </div>
        </AppVisible>
        <AppVisible visible={props.appEditVisible}>
          <div className="pr-1">
            <Button
              icon="pi pi-pencil text-xl"
              className="p-button-lg p-button-secondary"
              onClick={() => {
                handleEditList(rowData);
              }}
            />
          </div>
        </AppVisible>
      </div>
    );
  };
  // ==============================

  const titleTemplate = () => {
    return (
      <div className="">
        <AppFieldTitle title="Preferences" />
        <AppFieldDialogHelp
          title="Preferences"
          helpText="Preferences of datatable"
          displayHelp={displayHelp}
          onDisplayHelp={setDisplayHelp}
        />
      </div>
    );
  };
  // ==============================

  return (
    <>
      <Dialog
        header={titleTemplate}
        visible={props.appVisible}
        className="w-12 sm:w-9 h-30rem p-0"
        onHide={() => props.appOnQueryDialogHide()}
      >
        <AppVisible visible={!toggleForm}>
          <div>
            <AppTopBar
              appCancelVisible={cancelVisible}
              appDeleteVisible
              appDeleteAction={() => {
                handleDeleteList(preferenceSelected);
              }}
              appCancelAction={() => {
                setCancelVisible(false);
                setAddVisible(true);
                setPreferenceSelected([]);
              }}
              appAddVisible={addVisible}
              appAddAction={() => {
                setToggleForm(true);
                formControl.setValuesDefaultForm();
              }}
            />
            <DataTable
              id={`dtpreference${props.id}`}
              value={preferenceOptions}
              scrollable
              scrollHeight="250px"
              size="small"
              onSelectionChange={(data) => setPreferenceSelected(data.value)}
              selection={preferenceSelected}
            >
              <Column selectionMode="multiple" style={{ maxWidth: "50px" }} />
              <Column body={buttons} style={{ minWidth: "200px" }} />
              <Column field="preference_description" header="Descrição" />
              <Column field="sys_user_id_obj.name" header="Owner" />
              <Column field="isdefault" header="Default" />
              <Column field="ispublic" header="Public" />
            </DataTable>
          </div>
        </AppVisible>
        <AppVisible visible={toggleForm}>
          <AppTopBar
            appSaveVisible
            appCancelVisible
            appSaveAction={handleSaveForm}
            appCancelAction={handleCancelForm}
          />
          <div className="grid pt-4">
            <AppFieldText
              name="preference_description"
              key="preference_description"
              appFormControl={formControl}
              appTitle="Description"
              className="col-12"
            />

            <AppFieldCheck
              name="ispublic"
              key="ispublic"
              appFormControl={formControl}
              appTitle="Public"
              className="col-6"
              appTrueValue="S"
              appFalseValue="N"
            />

            <AppFieldCheck
              name="isdefault"
              key="isdefault"
              appFormControl={formControl}
              appTitle="Default"
              className="col-6"
              appTrueValue="S"
              appFalseValue="N"
            />
          </div>
        </AppVisible>
      </Dialog>
    </>
  );
};

export default AppPreference;
