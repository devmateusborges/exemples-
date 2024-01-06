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
import GerItemservVarService from "../../../services/modules/ger/GerItemservVarService";
import OpeCicloVarService from "../../../services/modules/ope/OpeCicloVarService";
import GenericFormPage from "../../generics/GenericFormPage";

const gerItemservVarService = new GerItemservVarService();
const opeCicloVarService = new OpeCicloVarService();
const GerItemservVarForm: React.FC = () => {
  // ==============================
  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_itemserv_var",
      required: [true, "Sigla is required"],
      maxValue: [50, "Maximum 50 characters for Sigla"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "nome",
      required: [true, "Nome is required"],
      maxValue: [100, "Maximum 100 characters for Nome"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "ativo",
      required: [false, ""],
      defaultValue: "S",
      type: "checkbox",
    },
    {
      fieldName: "ope_ciclo_var_id",
      required: [true, "Ciclo da Variedade is required"],
      defaultValue: "",
      type: "foreignkey",
    },
  ];

  const formControl = useFormControl({
    fieldControls,
  });
  return (
    <>
      <GenericFormPage
        appTitleClassIcon="pi pi-star text-red-500"
        appServiceDefault={gerItemservVarService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18GERVARIACAODOITEM/SERVICODEFAULT"))}
        appRouteList="/private/ger/geritemservvar"
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
                name="sigla_itemserv_var"
                appTitle={capitalize(
                  t("IN18VARIACAODOITEM/SERVICOSIGLADEFAULT")
                )}
                appHelpText="Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                name="ope_ciclo_var_id"
                appTitle={capitalize(t("IN18CICLODAVARIEDADESIGLADEFAULT"))}
                appHelpText="Ciclo da Variedade Help"
                appOptionLabel="sigla_ope_ciclo_var"
                appServiceDefault={opeCicloVarService}
                appOptionValue="id"
                appDataKey="id"
                appServiceFilterId="id"
                appServiceFilterDescription="sigla_ope_ciclo_var"
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

export default GerItemservVarForm;
