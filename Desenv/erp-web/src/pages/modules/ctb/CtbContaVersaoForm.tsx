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
import CtbContaVersaoService from "../../../services/modules/ctb/CtbContaVersaoService";
import GenericFormPage from "../../generics/GenericFormPage";

const ctbContaVersaoService = new CtbContaVersaoService();

const CtbContaVersaoForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_versao",
      required: [true, "Versão - Sigla is required"],
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
      fieldName: "data_valid_ini",
      required: [true, "Data Validade Inicial is required"],
      defaultValue: "",
      type: "date",
    },
    {
      fieldName: "versao_atual",
      required: [true, "Versão Atual is required"],
      defaultValue: "S",
      type: "checkbox",
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
        appServiceDefault={ctbContaVersaoService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18CTBVERSAODECONTADEFAULT"))}
        appRouteList="/private/ctb/ctbcontaversao"
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
                name="sigla_versao"
                appTitle={capitalize(t("IN18VERSAOSIGLADEFAULT"))}
                appHelpText="Versão - Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldDate
                appFormControl={formControl}
                name="data_valid_ini"
                appTitle={capitalize(t("IN18DATAVALIDADEINICIALDEFAULT"))}
                appHelpText="Data Validade Inicial"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="versao_atual"
                appTitle={capitalize(t("IN18VERSAOATUALDEFAULT"))}
                appHelpText="Versão Atual Help"
                appTrueValue="S"
                appFalseValue="N"
                appTrueValueLabel="Sim"
                appFalseValueLabel="Não"
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

export default CtbContaVersaoForm;
