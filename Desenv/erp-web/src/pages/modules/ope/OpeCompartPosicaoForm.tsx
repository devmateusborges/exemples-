import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useLayoutEffect, useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldNumber from "../../../components/toolkit-react/AppFieldNumber";
import AppFieldRadioButton from "../../../components/toolkit-react/AppFieldRadioButton";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import OpeCompartPosicaoService from "../../../services/modules/ope/OpeCompartPosicaoService";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import GenericFormPage from "../../generics/GenericFormPage";

const opeCompartPosicaoService = new OpeCompartPosicaoService();
const sysTypeDescriptionService = new SysTypeDescriptionService();

const OpeOpeCompartPosicaoForm: React.FC = () => {
  // ==============================
  const [activeIndex, setActiveIndex] = useState(0);

  const [posicao_opt, setPosicao_opt] = useState([]);
  const [banda_montagem_opt, setBanda_montagem_opt] = useState([]);
  const [lado_montagem_opt, setLado_montagem_opt] = useState([]);
  // ==============================
  useLayoutEffect(() => {
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_compart_posicao",
        "posicao"
      );
      setPosicao_opt(res);
    })();
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_compart_posicao",
        "banda_montagem"
      );
      setBanda_montagem_opt(res);
    })();
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_compart_posicao",
        "lado_montagem"
      );
      setLado_montagem_opt(res);
    })();
  }, []);
  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_compart_posicao",
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
      fieldName: "numero_eixo",
      required: [true, "Número Eixo is required"],
      maxValue: [9, "Maximum 9 characters for Número Eixo"],
      defaultValue: "",
      type: "numeric",
    },
    {
      fieldName: "posicao",
      required: [true, "Posição is required"],
      defaultValue: "",
      type: "radio",
    },

    {
      fieldName: "banda_montagem",
      required: [true, "Banda Montagem is required"],
      defaultValue: "",
      type: "radio",
    },

    {
      fieldName: "lado_montagem",
      required: [true, "Lado Montagem is required"],
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
        appServiceDefault={opeCompartPosicaoService}
        appFormControl={formControl}
        appTitle="OPE-Posição de Compartimento Form"
        appRouteList="/private/ope/opecompartposicao"
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
                name="sigla_compart_posicao"
                appTitle={capitalize(
                  t("IN18POSICAODOCOMPARTIMENTOSIGLADEFAULT")
                )}
                appHelpText="Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />

              <AppFieldNumber
                appFormControl={formControl}
                name="numero_eixo"
                appHelpText="Número Eixo"
                appTitle={capitalize(t("IN18NUMEROEIXODEFAULT"))}
                appUseGrouping={false}
              />

              <AppFieldRadioButton
                appFormControl={formControl}
                name="posicao"
                appTitle={capitalize(t("IN18POSICAODEFAULT"))}
                appOptions={posicao_opt}
                appOptionsLabel="description_type"
                appOptionsValue="value_type"
              />
              <AppFieldRadioButton
                appFormControl={formControl}
                name="banda_montagem"
                appTitle={capitalize(t("IN18BANDAMONTAGEMDEFAULT"))}
                appOptions={banda_montagem_opt}
                appOptionsLabel="description_type"
                appOptionsValue="value_type"
              />
              <AppFieldRadioButton
                appFormControl={formControl}
                name="lado_montagem"
                appTitle={capitalize(t("IN18LADOMONTAGEMDEFAULT"))}
                appOptions={lado_montagem_opt}
                appOptionsLabel="description_type"
                appOptionsValue="value_type"
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

export default OpeOpeCompartPosicaoForm;
