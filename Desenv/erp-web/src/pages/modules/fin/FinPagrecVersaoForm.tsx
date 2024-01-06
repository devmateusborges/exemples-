import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useLayoutEffect, useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import AppFieldDropdown from "../../../components/toolkit-react/AppFieldDropdown";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldNumber from "../../../components/toolkit-react/AppFieldNumber";
import AppFieldRadioButton from "../../../components/toolkit-react/AppFieldRadioButton";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import FinPagrecVersaoService from "../../../services/modules/fin/FinPagrecVersaoService";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import GenericFormPage from "../../generics/GenericFormPage";

const finPagrecVersaoService = new FinPagrecVersaoService();
const sysTypeDescriptionService = new SysTypeDescriptionService();

const FinPagrecVersaoForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  const [Tipo_per, setTipo_per] = useState([]);
  // ==============================

  useLayoutEffect(() => {
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "fin_pagrec_versao",
        "tipo_per"
      );
      setTipo_per(res);
    })();
  }, []);
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
      fieldName: "data_per_ini",
      required: [true, "Data Período Inicial is required"],
      defaultValue: "",
      type: "date",
    },
    {
      fieldName: "data_per_fin",
      required: [true, "Data Período Final is required"],
      defaultValue: "",
      type: "date",
    },
    {
      fieldName: "versao_atual",
      required: [false, ""],
      defaultValue: "N",
      type: "checkbox",
    },
    {
      fieldName: "tipo_per",
      required: [true, "Tipo Período is required"],
      defaultValue: "",
      type: "radio",
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
        appServiceDefault={finPagrecVersaoService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18FINVERSAODEPAG/RECDEFAULT"))}
        appRouteList="/private/fin/finpagrecversao"
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
                name="data_per_ini"
                appTitle={capitalize(t("IN18DATAPERIODOINICIALDEFAULT"))}
                appHelpText="Data Período Inicial Help"
              />
              <AppFieldDate
                appFormControl={formControl}
                name="data_per_fin"
                appTitle={capitalize(t("IN18DATAPERIODOFINALDEFAULT"))}
                appHelpText="Data Período Final Help"
              />
              <AppFieldRadioButton
                appFormControl={formControl}
                name="tipo_per"
                appTitle={capitalize(t("IN18TIPODEFAULT"))}
                appHelpText="Tipo per Help"
                appOptions={Tipo_per}
                appOptionsLabel="description_type"
                appOptionsValue="value_type"
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

export default FinPagrecVersaoForm;
