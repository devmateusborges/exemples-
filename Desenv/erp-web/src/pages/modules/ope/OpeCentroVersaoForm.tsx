import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useLayoutEffect, useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import AppFieldRadioButton from "../../../components/toolkit-react/AppFieldRadioButton";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import OpeCentroVersaoService from "../../../services/modules/ope/OpeCentroVersaoService";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import GenericFormPage from "../../generics/GenericFormPage";

const opeCentroVersaoService = new OpeCentroVersaoService();
const sysTypeDescriptionService = new SysTypeDescriptionService();
const OpeCentroVersaoForm: React.FC = () => {
  // ==============================
  const [activeIndex, setActiveIndex] = useState(0);
  const [tipo_per_opt, setTipo_per_opt] = useState([]);
  // ==============================
  useLayoutEffect(() => {
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_centro_versao",
        "tipo_per"
      );
      setTipo_per_opt(res);
    })();
  }, []);
  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_versao",
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
      fieldName: "data_per_ini",
      required: [true, "Data Período Inicial is required"],
      defaultValue: "",
      type: "date",
    },
    {
      fieldName: "versao_atual",
      required: [true, "Versão Atual is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "data_per_fin",
      required: [true, "Data Período Final is required"],
      defaultValue: "",
      type: "date",
    },
    {
      fieldName: "tipo_per",
      required: [true, "Tipo Período is required"],
      defaultValue: "",
      type: "radio",
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
        appServiceDefault={opeCentroVersaoService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18OPECENTROVERSAODEFAULT"))}
        appRouteList="/private/ope/opecentroversao"
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
                name="sigla_versao"
                appTitle={capitalize(t("IN18VERSAODECENTROSIGLADEFAULT"))}
                appHelpText="Sigla Help"
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
                appHelpText="Data Período Inicial"
              />
              <AppFieldDate
                appFormControl={formControl}
                name="data_per_fin"
                appTitle={capitalize(t("IN18DATAPERIODOFINALDEFAULT"))}
                appHelpText="Data Período Final"
              />
              <AppFieldRadioButton
                appFormControl={formControl}
                name="tipo_per"
                appTitle={capitalize(t("IN18TIPOPERIODODEFAULT"))}
                appOptions={tipo_per_opt}
                appOptionsLabel="description_type"
                appOptionsValue="value_type"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="versao_atual"
                appTitle={capitalize(t("IN18VERSAOATUALDEFAULT"))}
                appHelpText="Versão atual Help"
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

export default OpeCentroVersaoForm;
