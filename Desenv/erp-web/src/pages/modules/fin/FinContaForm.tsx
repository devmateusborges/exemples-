import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useLayoutEffect, useState } from "react";
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
import FinBancoService from "../../../services/modules/fin/FinBancoService";
import FinContaService from "../../../services/modules/fin/FinContaService";
import GerEmpresaService from "../../../services/modules/ger/GerEmpresaService";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import GenericFormPage from "../../generics/GenericFormPage";

const finContaService = new FinContaService();
const gerEmpresaService = new GerEmpresaService();
const finBancoService = new FinBancoService();

const FinContaForm: React.FC = () => {
  // ==============================
  const [activeIndex, setActiveIndex] = useState(0);

  // ==============================s

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
      fieldName: "nr_agencia",
      required: [true, "Numero Agência is required"],
      defaultValue: "",
      type: "text",
      maxValue: [50, "Maximum 50 for valor"],
    },
    {
      fieldName: "nr_conta",
      required: [true, "Número Conta is required"],
      defaultValue: "",
      type: "text",
      maxValue: [50, "Maximum 50 for valor"],
    },
    {
      fieldName: "ger_empresa_id",
      required: [true, "Empresa is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "fin_banco_id",
      required: [true, "Banco is required"],
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
        appServiceDefault={finContaService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18FINCONTADEFAULT"))}
        appRouteList="/private/fin/finconta"
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
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nr_conta"
                appTitle={capitalize(t("IN18NUMEROCONTADEFAULT"))}
                appHelpText="Número Conta Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nr_agencia"
                appTitle={capitalize(t("IN18NUMEROAGENCIADEFAULT"))}
                appHelpText="Numero Agência Help"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={gerEmpresaService}
                name="ger_empresa_id"
                appTitle={capitalize(t("IN18EMPRESASIGLADEFAULT"))}
                appHelpText="Empresa Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="sigla_empresa"
                appServiceFilterDescription="sigla_empresa"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={finBancoService}
                name="fin_banco_id"
                appTitle={capitalize(t("IN18BANCONOMEDEFAULT"))}
                appHelpText="Banco Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="nome"
                appServiceFilterDescription="nome"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="ativo"
                appTitle="Ativo"
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

export default FinContaForm;
