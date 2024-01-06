import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import GerEstNivelService from "../../../services/modules/ger/GerEstNivelService";
import GenericFormPage from "../../generics/GenericFormPage";

const gerEstNivelService = new GerEstNivelService();
const GerEstNivelForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_ger_est_nivel",
      required: [true, "Sigla is required"],
      defaultValue: "",
      type: "text",
      maxValue: [50, "Maximum 50 characters for Sigla"],
    },
    {
      fieldName: "nome",
      required: [true, "Nome is required"],
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
    {
      fieldName: "observacao",
      required: [true, "Observação is required"],
      defaultValue: "",
      type: "text",
      maxValue: [250, "Maximum 250 characters for Observação"],
    },
    {
      fieldName: "bloq_mov_solic",
      required: [false, ""],
      defaultValue: "N",
      type: "checkbox",
    },
    {
      fieldName: "bloq_mov_pedido",
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
        appServiceDefault={gerEstNivelService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18GERNIVELDEESTOQUEDEFAULT"))}
        appRouteList="/private/ger/gerestnivel"
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
                name="sigla_ger_est_nivel"
                appTitle={capitalize(t("IN18NIVELDEESTOQUESIGLADEFAULT"))}
                appHelpText="Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="observacao"
                appTitle={capitalize(t("IN18OBSERVACAODEFAULT"))}
                appHelpText="Observação Help"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="bloq_mov_solic"
                appTitle={capitalize(
                  t("IN18BLOQUEIAMOVIMENTODESOLICITACAODEFAULT")
                )}
                appHelpText="Bloqueia Movimento de Solicitação Help"
                appTrueValue="S"
                appTrueValueLabel="Sim"
                appFalseValue="N"
                appFalseValueLabel="Não"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="bloq_mov_pedido"
                appTitle={capitalize(t("IN18BLOQUEIAMOVIMENTODEPEDIDODEFAULT"))}
                appHelpText="Bloqueia Movimento de Pedido Help"
                appTrueValue="S"
                appTrueValueLabel="Sim"
                appFalseValue="N"
                appFalseValueLabel="Não"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="ativo"
                appTitle={capitalize(t("IN18ATIVODEFAULT"))}
                appHelpText="Ativo Help"
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

export default GerEstNivelForm;
