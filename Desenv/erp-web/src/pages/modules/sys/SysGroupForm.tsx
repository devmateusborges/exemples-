import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useLayoutEffect, useRef, useState } from "react";
import AppContainer from "../../../components/toolkit-react/AppContainer";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppContainerTitle from "../../../components/toolkit-react/AppContainerTitle";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import AppFieldDropdown from "../../../components/toolkit-react/AppFieldDropdown";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import SysGroupService from "../../../services/modules/sys/SysGroupService";
import SysProgramService from "../../../services/modules/sys/SysProgramService";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import GenericFormPage from "../../generics/GenericFormPage";
import SysGroupFormDet1 from "./SysGroupFormDet1";

const sysGroupService = new SysGroupService();

const SysGroupForm: React.FC = () => {
  const dataTableDet1Ref = useRef<any>();
  const [detActiveIndex, setDetActiveIndex] = useState(0);
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);

  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "code_group",
      required: [true, "Grupo - Sigla is required"],
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
  ];
  // ==============================
  const formControl = useFormControl({
    fieldControls,
  });

  // ==============================
  const detailsOptions = [
    { name: "sys_group_program_childs", ref: dataTableDet1Ref },
  ];
  // ==============================

  return (
    <>
      <GenericFormPage
        appTitleClassIcon="pi pi-star text-red-500"
        appServiceDefault={sysGroupService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18SYSGRUPOSDEFAULT"))}
        appRouteList="/private/sys/sysgroup"
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
                name="code_group"
                appTitle={capitalize(t("IN18GRUPOSIGLADEFAULT"))}
                appHelpText="Grupo - Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="name"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
            </AppContainerFields>
          </TabPanel>
        </TabView>
        <AppContainer className="w-full mt-2">
          <AppContainerTitle appTitle="Dets Form" appSmall />
          <div className="md:p-2">
            <TabView
              activeIndex={detActiveIndex}
              onTabChange={(e) => setActiveIndex(e.index)}
              renderActiveOnly={false}
              panelContainerClassName="p-0"
            >
              <TabPanel
                header="System-Grupo de Acesso x Programa"
                className="p-0"
              >
                <SysGroupFormDet1
                  appRef={dataTableDet1Ref}
                  appDataTableDataValue={
                    formControl.getValues().sys_group_program_childs
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

export default SysGroupForm;
