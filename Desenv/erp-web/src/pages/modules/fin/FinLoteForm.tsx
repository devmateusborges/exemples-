import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldNumber from "../../../components/toolkit-react/AppFieldNumber";
import AppFieldRadioButton from "../../../components/toolkit-react/AppFieldRadioButton";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import FinLoteService from "../../../services/modules/fin/FinLoteService";
import GerEmpresaService from "../../../services/modules/ger/GerEmpresaService";
import GenericFormPage from "../../generics/GenericFormPage";

const finLoteService = new FinLoteService();
const gerEmpresaService = new GerEmpresaService();

const FinLoteForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_fin_lote",
      required: [true, "Lote - Sigla is required"],
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
      fieldName: "data_lote",
      required: [true, "Data Lote is required"],
      defaultValue: "",
      type: "date",
    },
    {
      fieldName: "ger_empresa_id",
      required: [true, "Empresa is required"],
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
  // ==============================
  return (
    <>
      <GenericFormPage
        appTitleClassIcon="pi pi-star text-red-500"
        appServiceDefault={finLoteService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18FINLOTEDEFAULT"))}
        appRouteList="/private/fin/finlote"
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
                name="sigla_fin_lote"
                appTitle={capitalize(t("IN18LOTESIGLADEFAULT"))}
                appHelpText="Lote - Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldDate
                appFormControl={formControl}
                name="data_lote"
                appTitle={capitalize(t("IN18DATALOTEDEFAULT"))}
                appHelpText="Data Lote Help"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={gerEmpresaService}
                name="ger_empresa_id"
                appTitle={capitalize(t("IN18EMPRESASIGLADEFAULT"))}
                appHelpText="Empresa - Sigla Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="sigla_empresa"
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

export default FinLoteForm;
