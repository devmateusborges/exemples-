import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useLayoutEffect, useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import AppFieldNumber from "../../../components/toolkit-react/AppFieldNumber";
import AppFieldRadioButton from "../../../components/toolkit-react/AppFieldRadioButton";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import FinClassService from "../../../services/modules/fin/FinClassService";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import GenericFormPage from "../../generics/GenericFormPage";

const finClassService = new FinClassService();
const sysTypeDescriptionService = new SysTypeDescriptionService();

const FinClassForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  const [tipo_es, set_tipo_es] = useState([]);
  const [tipo_fluxo, set_tipo_fluxo] = useState([]);
  const [fixo_variavel, set_fixo_variavel] = useState([]);

  // ==============================

  useLayoutEffect(() => {
    (async () => {
      let res = await sysTypeDescriptionService.getDescription(
        "fin_class",
        "tipo_es"
      );
      set_tipo_es(res);

      res = await sysTypeDescriptionService.getDescription(
        "fin_class",
        "tipo_fluxo"
      );
      set_tipo_fluxo(res);

      res = await sysTypeDescriptionService.getDescription(
        "fin_class",
        "fixo_variavel"
      );
      set_fixo_variavel(res);
    })();
  }, []);

  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_class",
      required: [true, "Classe - Sigla is required"],
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
      fieldName: "tipo_es",
      required: [true, "Tipo Entrada/Saída is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "tipo_fluxo",
      required: [true, "Considerado como Pag ou Rec is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "fixo_variavel",
      required: [true, "Fixo Variavel is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "tipo_prev",
      required: [false, "Tipo Prev is required"],
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
        appServiceDefault={finClassService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18FINCLASSEDEFAULT"))}
        appRouteList="/private/fin/finclass"
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
                name="sigla_class"
                appTitle={capitalize(t("IN18CLASSESIGLADEFAULT"))}
                appHelpText="Classe - Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldRadioButton
                appFormControl={formControl}
                name="fixo_variavel"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appOptions={fixo_variavel}
                appOptionsLabel="description_type"
                appOptionsValue="value_type"
              />
              <AppFieldRadioButton
                appFormControl={formControl}
                name="tipo_fluxo"
                appTitle={capitalize(t("IN18CONSIDERADOPAG/RECDEFAULT"))}
                appOptions={tipo_fluxo}
                appOptionsLabel="description_type"
                appOptionsValue="value_type"
              />
              <AppFieldRadioButton
                appFormControl={formControl}
                name="tipo_es"
                appTitle={capitalize(t("IN18TIPOENTRADA/SAIDADEFAULT"))}
                appOptions={tipo_es}
                appOptionsLabel="description_type"
                appOptionsValue="value_type"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="tipo_prev"
                appTitle={capitalize(t("IN18TIPOPREVISAODEFAULT"))}
                appHelpText="Tipo Previsão Help"
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

export default FinClassForm;
