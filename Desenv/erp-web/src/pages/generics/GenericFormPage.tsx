/* eslint-disable guard-for-in */
/* eslint-disable react/require-default-props */
import { confirmDialog } from "primereact/confirmdialog";
import { DataTableFilterMeta } from "primereact/datatable";
import React, { useCallback, useEffect, useMemo, useRef } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { toast } from "react-toastify";
import AppContainer from "../../components/toolkit-react/AppContainer";
import AppContainerTitle from "../../components/toolkit-react/AppContainerTitle";
import store, { useAppSelector } from "../../store";
import AppTopBar, {
  IAppTopBar,
} from "../../components/toolkit-react/AppTopBar";
import AppVisible from "../../components/toolkit-react/bases/AppVisible";
import useFormControl, {
  IFieldControl,
  IFormControl,
} from "../../components/toolkit-react/hooks/useFormControl";
import useState from "../../components/toolkit-react/hooks/useStateRef";
import IAppProps from "../../components/toolkit-react/interface/IAppProp";

interface IDetailOption {
  name: string;
  ref: any;
}

export interface IGenericFormPage extends IAppProps, IAppTopBar {
  appFormControl?: any;
  appServiceDefault?: any;
  appFieldControls?: Array<IFieldControl>;
  appTitle?: string;
  appShowTopBar?: boolean;
  appRouteList?: string;
  appOnQueryCancel?: any;
  appOnQuerySave?: any;
  appOnQueryLoadData?: any;
  appOnQuerySavePlus?: any;
  appDetailsOptions?: Array<IDetailOption>;
  appTitleClassIcon?: string;
}

const GenericFormPage: React.FC<IGenericFormPage> = (
  props: IGenericFormPage
) => {
  const navigate = useNavigate();
  const urlParams = useParams();

  const [formControl, setFormControl, formControlRef] = useState(
    props.appFormControl
  );

  const handleLoadData = async () => {
    if (urlParams?.id) {
      if (urlParams?.id != "new") {
        const dataForm = await props.appServiceDefault.findById(urlParams?.id);
        // console.log("useEffect > GenericForm", dataForm);
        // console.log(formControl);
        await formControl.handleResetForm();
        await formControl.setValuesForm(dataForm);
      }
    }
  };
  // ==============================

  const handleSaveAux = async () => {
    const valid = await formControl.isValid();
    const formValue = await formControl.getValues();
    console.log(formValue);
    if (props.appDetailsOptions != undefined) {
      for (const det of props.appDetailsOptions) {
        formValue[det.name] = det.ref.current ?? [];
      }
    }

    if (valid) {
      const result = await props.appServiceDefault.save(formValue);
      if (result) {
        toast.success("Save successfully");
      }
    } else {
      throw formControl.getErrors();
    }
  };

  // ==============================

  const handleSave = async (newRecord = false) => {
    confirmDialog({
      message: "Do you want to save record ?",
      header: "Confirmation",
      icon: "pi pi-question-circle",
      accept: async () => {
        try {
          if (props.appOnQuerySave != undefined) {
            await props.appOnQuerySave(newRecord);
          } else {
            await handleSaveAux();
          }

          if (newRecord) {
            if (props.appOnQuerySavePlus) {
              props.appOnQuerySavePlus();
            } else if (props.appRouteList) {
              const valid = await formControl.isValid();
              if (valid) {
                navigate(`${props.appRouteList}form/new`);
                formControl.setValuesDefaultForm();
              }
            }
          }
        } catch (error: any) {
          if (error) {
            for (const f of Object.entries(error)) {
              toast.error(`${f[1]}`);
            }
          }
        }
      },
      reject: () => {},
    });
  };

  // ==============================
  const handleCancel = () => {
    if (props.appOnQueryCancel != undefined) {
      props.appOnQueryCancel();
    } else if (props.appRouteList) {
      navigate(props.appRouteList);
    }
  };
  // ==============================
  useEffect(() => {
    if (props.appOnQueryLoadData) {
      props.appOnQueryLoadData();
    } else {
      handleLoadData();
    }
  }, [urlParams]);
  return (
    <>
      <AppContainer className="w-full">
        <AppVisible visible={props.appTitle}>
          <AppContainerTitle
            appClassTitleBg={store.getState().theme.classNameTitleBg}
            appClassTitleText={store.getState().theme.classNameTitleText}
            appClassIcon={props.appTitleClassIcon}
            appTitle={props.appTitle ?? ""}
            appHelpText={props.appHelpText}
          />
        </AppVisible>
        <AppVisible visible={props.appShowTopBar}>
          <AppTopBar
            appSaveVisible
            appCancelVisible
            appSavePlusVisible
            appSaveActionCode={props.appSaveActionCode ?? "SAVE"}
            appSavePlusAction={() => {
              handleSave(true);
            }}
            appSaveAction={() => {
              handleSave(false);
            }}
            appCancelAction={handleCancel}
          />
        </AppVisible>
        <div className="w-full pt-3 pb-2 md:pl-2 md:pr-2">{props.children}</div>
      </AppContainer>
    </>
  );
};
// ==============================
export default GenericFormPage;
