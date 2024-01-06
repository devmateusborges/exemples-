import { t } from "i18next";
import { capitalize } from "lodash";
import { Divider } from "primereact/divider";
import { TabPanel, TabView } from "primereact/tabview";
import { useState } from "react";
import AppFieldColorPicker from "../../../components/toolkit-react/AppFieldColorPicker";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldNumber from "../../../components/toolkit-react/AppFieldNumber";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import SysModuleService from "../../../services/modules/sys/SysModuleService";
import SysService from "../../../services/modules/sys/SysService ";
import GenericFormPage from "../../generics/GenericFormPage";

const sysModuleService = new SysModuleService();
const sysService = new SysService();
const SysModuleForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "code_module",
      required: [true, "Modulo - Sigla is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "name",
      required: [true, "Nome is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "icon",
      required: [true, "Icon is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "color",
      required: [true, "Color is required"],
      defaultValue: "",
      type: "text",
      maxValue: [50, "Maximum 50 for valor"],
    },
    {
      fieldName: "order_visual",
      required: [true, "Color is required"],
      defaultValue: "",
      type: "numeric",
      maxValue: [32, "Maximum 32 for valor"],
    },
    {
      fieldName: "sys_id",
      required: [false, ""],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "active",
      required: [false, ""],
      defaultValue: "S",
      type: "checkbox",
    },
  ];
  // ==============================
  const formControl = useFormControl({
    fieldControls,
  });
  // ==============================

  return (
    <>
      <GenericFormPage
        appTitleClassIcon="pi pi-star text-red-500"
        appServiceDefault={sysModuleService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18SysModuleDEFAULT"))}
        appRouteList="/private/sys/sysmodule"
        appShowTopBar
      >
        <TabView
          activeIndex={activeIndex}
          onTabChange={(e) => setActiveIndex(e.index)}
          panelContainerClassName="p-0 md:p-2 mb-3"
        >
          <TabPanel header="General ">
            <AppContainerFields>
              <AppFieldText
                appFormControl={formControl}
                name="code_module"
                appTitle={capitalize(t("IN18MODULOSSIGLADEFAULT"))}
                appHelpText="Grupo - Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="name"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="icon"
                appTitle={capitalize(t("IN18ICONDEFAULT"))}
                appHelpText="icon Help"
              />

              <AppFieldNumber
                appFormControl={formControl}
                name="order_visual"
                appTitle={capitalize(t("IN18ORDERVISUALDEFAULT"))}
                appHelpText="Order visual Help"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={sysService}
                name="sys_id"
                appTitle={capitalize(t("IN18RESTRICAODESISTEMASIGLADEFAULT"))}
                appHelpText="Sistema - Sigla Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="code_sys"
                appServiceFilterDescription="code_sys"
              />

              <AppFieldCheck
                appFormControl={formControl}
                name="active"
                appTitle={capitalize(t("IN18ATIVODEFAULT"))}
                appHelpText="Ativo Help"
                appTrueValue="S"
                appFalseValue="N"
                appTrueValueLabel="Sim"
                appFalseValueLabel="Não"
              />

              <AppFieldColorPicker
                className="col-12"
                appTitle={capitalize(t("IN18COLORDEFAULT"))}
                appFormControl={formControl}
                name="color"
                appHelpText="Color Help"
                appReturnType="hex"
              />
            </AppContainerFields>
          </TabPanel>
        </TabView>
      </GenericFormPage>
    </>
  );
};

export default SysModuleForm;
