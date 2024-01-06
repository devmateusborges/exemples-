import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldNumber from "../../../components/toolkit-react/AppFieldNumber";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import GerNumeracaoService from "../../../services/modules/ger/GerNumeracaoService";
import GenericFormPage from "../../generics/GenericFormPage";

const gerNumeracaoService = new GerNumeracaoService();

const GerNumeracaoForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_ger_numeracao",
      required: [true, "Númeração - Sigla"],
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
      fieldName: "serie",
      required: [true, "Série is required"],
      maxValue: [3, "Maximum 3 characters for Série"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "ultimo_nr",
      required: [true, "Ultimo Número is required"],
      maxValue: [9, "Maximum 9 characters for Ultimo Número"],
      defaultValue: "",
      type: "numeric",
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
        appServiceDefault={gerNumeracaoService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18GERNUMERACAODEFAULT"))}
        appRouteList="/private/ger/gernumeracao"
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
                name="sigla_ger_numeracao"
                appTitle={capitalize(t("IN18NUMERACAOSIGLADEFAULT"))}
                appHelpText="Sigla - Númeração Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="serie"
                appTitle={capitalize(t("IN18SERIEDEFAULT"))}
                appHelpText="Série Help"
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="ultimo_nr"
                appTitle={capitalize(t("IN18ULTIMONUMERODEFAULT"))}
                appHelpText="Ultimo Número Help"
                appUseGrouping={false}
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="ativo"
                appTitle={capitalize(t("IN18ATIVODEFAULT"))}
                appHelpText="Ativo Help"
                appTrueValue="S"
                appTrueValueLabel="Sim"
                appFalseValue="N"
                appFalseValueLabel="Não"
              />
            </AppContainerFields>
          </TabPanel>
        </TabView>
      </GenericFormPage>
    </>
  );
};

export default GerNumeracaoForm;
