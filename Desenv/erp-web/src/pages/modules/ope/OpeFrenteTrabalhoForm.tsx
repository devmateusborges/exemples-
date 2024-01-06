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
import GerEmpresaService from "../../../services/modules/ger/GerEmpresaService";
import OpeFrenteTrabalhoService from "../../../services/modules/ope/OpeFrenteTrabalhoService";
import GenericFormPage from "../../generics/GenericFormPage";

const opeFrenteTrabalhoService = new OpeFrenteTrabalhoService();
const gerEmpresaService = new GerEmpresaService();

const OpeFrenteTrabalhoForm: React.FC = () => {
  // ==============================
  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_frente_trabalho",
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
      fieldName: "ger_empresa_id",
      required: [true, "Empresa is required"],
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
        appServiceDefault={opeFrenteTrabalhoService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18OPEFRENTETRABALHODEFAULT"))}
        appRouteList="/private/ope/opefrentetrabalho"
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
                name="sigla_frente_trabalho"
                appTitle={capitalize(t("IN18FRENTEDETRABALHOSIGLADEFAULT"))}
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
                name="ger_empresa_id"
                appTitle={capitalize(t("IN18EMPRESASIGLADEFAULT"))}
                appHelpText="Empresa Help"
                appOptionLabel="sigla_empresa"
                appOptionValue="id"
                appDataKey="id"
                appServiceDefault={gerEmpresaService}
                appServiceFilterId="id"
                appServiceFilterDescription="sigla_empresa"
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

export default OpeFrenteTrabalhoForm;
