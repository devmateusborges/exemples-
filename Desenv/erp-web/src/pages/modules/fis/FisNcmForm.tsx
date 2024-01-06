import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import FisNcmService from "../../../services/modules/fis/FisNcmService";
import GenericFormPage from "../../generics/GenericFormPage";

const fisNcmService = new FisNcmService();

const FisNcmForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "nome",
      required: [true, "Nome is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "nr_ncm",
      required: [true, "Numero NCM is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "data_validade",
      required: [true, "Data Validade is required"],
      defaultValue: "",
      type: "date",
    },
    {
      fieldName: "ativo",
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
        appServiceDefault={fisNcmService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18FISNCMDEFAULT"))}
        appRouteList="/private/fis/fisncm"
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
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />

              <AppFieldText
                appFormControl={formControl}
                name="nr_ncm"
                appHelpText="Numero NCM help"
                appTitle={capitalize(t("IN18NUMERONCMDEFAULT"))}
              />
              <AppFieldDate
                appFormControl={formControl}
                name="data_validade"
                appTitle={capitalize(t("IN18DATAVALIDADEFINALDEFAULT"))}
                appHelpText="Data Validade Help"
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

export default FisNcmForm;
