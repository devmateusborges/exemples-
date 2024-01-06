import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import CrmClassService from "../../../services/modules/crm/CrmClassService";
import CrmClassSubgrupoService from "../../../services/modules/crm/CrmClassSubgrupoService";
import GenericFormPage from "../../generics/GenericFormPage";

const crmClassService = new CrmClassService();
const crmClassSubgrupoService = new CrmClassSubgrupoService();

const CrmClassForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_class",
      required: [true, "Class - Sigla is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "nome",
      required: [true, "Nome is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "ativo",
      required: [false, ""],
      defaultValue: "S",
      type: "checkbox",
    },
    {
      fieldName: "crm_class_subgrupo_id",
      required: [false, ""],
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
        appServiceDefault={crmClassService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18CRMCLASSEDEFAULT"))}
        appRouteList="/private/crm/crmclass"
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
                name="sigla_class"
                appTitle={capitalize(t("IN18CLASSESIGLADEFAULT"))}
                appHelpText="Class - Sigla Help"
              />

              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />

              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={crmClassSubgrupoService}
                name="crm_class_subgrupo_id"
                appTitle={capitalize(t("IN18CLASSESUBGRUPODEFAULT"))}
                appHelpText="Classe Subgrupo Grupo Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="sigla_class_subgrupo"
                appServiceFilterDescription="sigla_class_subgrupo"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="ativo"
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

export default CrmClassForm;
