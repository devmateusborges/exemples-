import { TabPanel, TabView } from "primereact/tabview";
import { capitalize } from "lodash";
import { t } from "i18next";
import { useLayoutEffect, useRef, useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";

import GenericFormPage from "../../generics/GenericFormPage";
import AppFieldDropdown from "../../../components/toolkit-react/AppFieldDropdown";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import SysProgramService from "../../../services/modules/sys/SysProgramService";
import SysService from "../../../services/modules/sys/SysService ";
import AppContainer from "../../../components/toolkit-react/AppContainer";
import AppContainerTitle from "../../../components/toolkit-react/AppContainerTitle";
import SysProgramFormDet1 from "./SysProgramFormDet1";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import SysModuleService from "../../../services/modules/sys/SysModuleService";

const sysModuleService = new SysModuleService();

const sysProgramService = new SysProgramService();
const sysTypeDescriptionService = new SysTypeDescriptionService();
const SysProgramForm: React.FC = () => {
  // ==============================

  const [detActiveIndex, setDetActiveIndex] = useState(0);
  const [activeIndex, setActiveIndex] = useState(0);
  const dataTableDet1Ref = useRef<any>();
  const [Type_program_opt, setType_program_opt] = useState([]);
  const [Indicated_opt, setIndicated_opt] = useState([]);

  // ==============================

  useLayoutEffect(() => {
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "sys_program",
        "type_program"
      );
      setType_program_opt(res);
    })();
  }, []);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "code_program",
      required: [true, "Programa - Sigla is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 characters for Sigla"],
    },
    {
      fieldName: "name",
      required: [true, "Nome is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "controller",
      required: [true, "Controller is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "icon",
      required: [true, "Icon is required"],
      defaultValue: "",
      type: "text",
      maxValue: [50, "Maximum 50 for valor"],
    },
    {
      fieldName: "type_program",
      required: [true, "Tipo de Programa is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "sys_module_id",
      required: [true, "sistema de módulos is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "admin",
      required: [true, ""],
      defaultValue: "S",
      type: "checkbox",
    },
    {
      fieldName: "menu",
      required: [true, "Menu is required"],
      defaultValue: "S",
      type: "radio",
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
  const detailsOptions = [
    { name: "sys_plan_restriction_childs", ref: dataTableDet1Ref },
  ];
  // ==============================

  return (
    <>
      <GenericFormPage
        appServiceDefault={sysProgramService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18SYSPROGRAMADEFAULT"))}
        appRouteList="/private/sys/sysprogram"
        appDetailsOptions={detailsOptions}
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
                name="code_program"
                appTitle={capitalize(t("IN18PROGAMASIGLADEFAULT"))}
                appHelpText="Programa - Sigla Help"
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
                appHelpText="Icon Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="controller"
                appTitle={capitalize(t("IN18CONTROLLERDEFAULT"))}
                appHelpText="Descrião Help"
              />
              <AppFieldDropdown
                appFormControl={formControl}
                name="type_program"
                appTitle={capitalize(t("IN18TIPOPROGRAMADEFAULT"))}
                appOptions={Type_program_opt}
                appHelpText="Tipo Do Plano Help"
                appOptionLabel="description_type"
                appOptionValue="value_type"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={sysModuleService}
                name="sys_module_id"
                appTitle={capitalize(t("IN18MODULOSSIGLADEFAULT"))}
                appHelpText="Sistema Module Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="code_module"
                appServiceFilterDescription="code_module"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="admin"
                appTitle={capitalize(t("IN18ADMINDEFAULT"))}
                appHelpText="Admin Help"
                appTrueValue="S"
                appFalseValue="N"
                appTrueValueLabel="Sim"
                appFalseValueLabel="Não"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="menu"
                appTitle={capitalize(t("IN18MENUDEFAULT"))}
                appHelpText="Menu Help"
                appTrueValue="S"
                appFalseValue="N"
                appTrueValueLabel="Sim"
                appFalseValueLabel="Não"
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
            </AppContainerFields>
          </TabPanel>
        </TabView>
        <AppContainer className="w-full mt-2">
          <AppContainerTitle appTitle="Dets Form" appSmall />
          <div className="md:p-2">
            <TabView
              activeIndex={detActiveIndex}
              onTabChange={(e) => setDetActiveIndex(e.index)}
              renderActiveOnly={false}
              panelContainerClassName="p-0"
            >
              <TabPanel header="System-Programa x Ação" className="p-0">
                <SysProgramFormDet1
                  appRef={dataTableDet1Ref}
                  appDataTableDataValue={
                    formControl.getValues().sys_program_action_childs
                  }
                />
              </TabPanel>
            </TabView>
          </div>
        </AppContainer>
      </GenericFormPage>
    </>
  );
};

export default SysProgramForm;
