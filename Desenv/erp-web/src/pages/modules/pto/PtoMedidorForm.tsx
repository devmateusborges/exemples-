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
import PtoMedidorService from "../../../services/modules/pto/PtoMedidorService";
import GenericFormPage from "../../generics/GenericFormPage";

const ptoMedidorService = new PtoMedidorService();

const PtoMedidorForm: React.FC = () => {
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
      fieldName: "sigla_medidor",
      required: [true, "Medidor - sigla is required"],
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
  ];
  // ==============================

  const formControl = useFormControl({
    fieldControls,
  });
  return (
    <>
      <GenericFormPage
        appServiceDefault={ptoMedidorService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18PTOMEDIDORDEFAULT"))}
        appRouteList="/private/pto/ptomedidor"
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
                name="sigla_medidor"
                appTitle={capitalize(t("IN18MEDIDORSIGLADEFAULT"))}
                appHelpText="Help"
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

export default PtoMedidorForm;
