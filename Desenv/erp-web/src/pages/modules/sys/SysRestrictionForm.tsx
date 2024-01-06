import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useLayoutEffect, useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldRadioButton from "../../../components/toolkit-react/AppFieldRadioButton";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import SysRestrictionService from "../../../services/modules/sys/SysRestrictionService";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import GenericFormPage from "../../generics/GenericFormPage";

const sysRestrictionService = new SysRestrictionService();
const sysTypeDescriptionService = new SysTypeDescriptionService();

const SysRestrictionForm: React.FC = () => {
  const [Type_value, setType_value] = useState([]);
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================
  useLayoutEffect(() => {
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "sys_restriction",
        "type_value"
      );
      setType_value(res);
    })();
  }, []);
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "code_restriction",
      required: [true, "Restriction - Sigla is required"],
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
      fieldName: "type_value",
      required: [true, "Tipo de Valor is required"],
      defaultValue: "",
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

  return (
    <>
      <GenericFormPage
        appTitleClassIcon="pi pi-star text-red-500"
        appServiceDefault={sysRestrictionService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18SYSRESTRICOESDEFAULT"))}
        appRouteList="/private/sys/sysrestriction"
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
                name="code_restriction"
                appTitle={capitalize(t("IN18RESTRICAOSIGLADEFAULT"))}
                appHelpText="Restrição - Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="name"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldRadioButton
                appFormControl={formControl}
                name="type_value"
                appTitle={capitalize(t("IN18TIPOVALORDEFAULT"))}
                appHelpText="icon Help"
                appOptions={Type_value}
                appOptionsLabel="description_type"
                appOptionsValue="value_type"
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

export default SysRestrictionForm;
