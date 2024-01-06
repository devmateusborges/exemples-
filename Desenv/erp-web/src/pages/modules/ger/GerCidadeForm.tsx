import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useRef, useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldNumber from "../../../components/toolkit-react/AppFieldNumber";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import GerCidadeService from "../../../services/modules/ger/GerCidadeService";
import GerUfService from "../../../services/modules/ger/GerUfService";
import GenericFormPage from "../../generics/GenericFormPage";

const gerCidadeService = new GerCidadeService();
const gerUfService = new GerUfService();
const GerCidadeForm: React.FC = () => {
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
      fieldName: "nr_cidade",
      required: [true, "Número da cidade is required"],
      defaultValue: "",
      type: "text",
      maxValue: [50, "Maximum 50 characters for Número da cidade"],
    },
    {
      fieldName: "ger_uf_id",
      required: [true, "Unidade Federação is required"],
      defaultValue: "",
      type: "foreignkey",
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
  return (
    <>
      <GenericFormPage
        appServiceDefault={gerCidadeService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18GERCIDADEDEFAULT"))}
        appRouteList="/private/ger/gercidade"
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
                appHelpText="Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nr_cidade"
                appHelpText="Help"
                appTitle={capitalize(t("IN18NUMEROCIDADEDEFAULT"))}
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                name="ger_uf_id"
                appTitle={capitalize(t("IN18UFSIGLADEFAULT"))}
                appHelpText="Uf - Sigla Help "
                appOptionLabel="sigla_uf"
                appOptionValue="id"
                appDataKey="id"
                appServiceDefault={gerUfService}
                appServiceFilterId="id"
                appServiceFilterDescription="sigla_uf"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="ativo"
                appTitle={capitalize(t("IN18ATIVODEFAULT"))}
                appHelpText="Help"
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

export default GerCidadeForm;
