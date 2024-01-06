import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useLayoutEffect, useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";

import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import FinReciboTipoService from "../../../services/modules/fin/FinReciboTipoService";
import GenericFormPage from "../../generics/GenericFormPage";

const finReciboTipoService = new FinReciboTipoService();

const FinReciboTipoForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);

  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_fin_recibo_tipo",
      required: [true, "Tipo de Recibo - Sigla is required"],
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
      fieldName: "padrao",
      required: [false, ""],
      defaultValue: "N",
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
        appServiceDefault={finReciboTipoService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18FINTIPODERECIBODEFAULT"))}
        appRouteList="/private/fin/finrecibotipo"
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
                name="sigla_fin_recibo_tipo"
                appTitle={capitalize(t("IN18TIPODERECIBOSIGLADEFAULT"))}
                appHelpText="Tipo de Recibo - Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="padrao"
                appTitle={capitalize(t("IN18VALORPADRAODEFAULT"))}
                appHelpText="Padrão Help"
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

export default FinReciboTipoForm;
