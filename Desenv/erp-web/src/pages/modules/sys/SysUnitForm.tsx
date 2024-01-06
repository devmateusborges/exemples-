import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import SysUnitManagerService from "../../../services/modules/sys/SysUnitManagerService";
import SysUnitService from "../../../services/modules/sys/SysUnitService";
import GenericFormPage from "../../generics/GenericFormPage";

const sysUnitService = new SysUnitService();
const sysUnitManagerService = new SysUnitManagerService();
const SysUnitForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "code_unit",
      required: [true, "Sigla da Unidade is required"],
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
      fieldName: "active",
      required: [false, ""],
      defaultValue: "S",
      type: "checkbox",
    },
    {
      fieldName: "sys_unit_manager_id",
      required: [true, "Gestora de Unidade is required"],
      defaultValue: "",
      type: "foreignkey",
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
        appServiceDefault={sysUnitService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18UNIDADESIGLADEFAULT"))}
        appRouteList="/private/sys/SysUnit"
        appShowTopBar
      >
        <TabView
          activeIndex={activeIndex}
          onTabChange={(e) => setActiveIndex(e.index)}
          panelContainerClassName="p-0 md:p-2 mb-3"
        >
          <TabPanel header="General">
            <AppContainerFields>
              <AppFieldText
                appFormControl={formControl}
                name="code_unit"
                appTitle={capitalize(t("IN18SISTEMAUNIDADESIGLADEFAULT"))}
                appHelpText="Grupo - Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="name"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />{" "}
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={sysUnitManagerService}
                name="sys_unit_manager_id"
                appTitle={capitalize(t("IN18GESTORADEUNIDADENOMEDEFAULT"))}
                appHelpText="Gestora de Unidade Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="name"
                appServiceFilterDescription="name"
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
      </GenericFormPage>
    </>
  );
};

export default SysUnitForm;
