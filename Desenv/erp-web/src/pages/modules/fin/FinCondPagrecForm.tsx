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
import FinCondPagrecService from "../../../services/modules/fin/FinCondPagrecService";
import GenericFormPage from "../../generics/GenericFormPage";

const finCondPagrecService = new FinCondPagrecService();

const FinCondPagrecForm: React.FC = () => {
  // ==============================
  const [activeIndex, setActiveIndex] = useState(0);

  // ==============================s

  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_cond_pagamento",
      required: [true, "Condição de Pagamento - Sigla is required"],
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
      fieldName: "qnt_dia_ini",
      required: [true, "Quantidade Dias Inicial is required"],
      defaultValue: "",
      type: "numeric",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "considera_feriado",
      required: [false, "Considera Feriado is required"],
      defaultValue: "S",
      type: "checkbox",
    },
    {
      fieldName: "considera_final_sem",
      required: [false, "Considera Final de Semana is required"],
      defaultValue: "S",
      type: "checkbox",
    },
    {
      fieldName: "tipo_prazo",
      required: [false, "Tipo Prazo is required"],
      defaultValue: "S",
      type: "checkbox",
    },
    {
      fieldName: "observacao",
      required: [true, "Observação is required"],
      defaultValue: "",
      type: "text",
      maxValue: [250, "Maximum 250 for valor"],
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
        appServiceDefault={finCondPagrecService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18FINCONDICAODEPAGAMENTODEFAULT"))}
        appRouteList="/private/fin/fincondpagrec"
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
                name="sigla_cond_pagamento"
                appTitle={capitalize(t("IN18CONDICAODEPAGAMENTOSIGLADEFAULT"))}
                appHelpText="Condição de Pagamento - Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="qnt_dia_ini"
                appHelpText="Quantidade Dias Inicial Help"
                appTitle={capitalize(t("IN18QUANTIDADEDIASINICIALDEFAULT"))}
              />
              <AppFieldText
                appFormControl={formControl}
                name="observacao"
                appTitle={capitalize(t("IN18OBSERVACAODEFAULT"))}
                appHelpText="Observação Help"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="tipo_prazo"
                appTitle={capitalize(t("IN18TIPOPRAZODEFAULT"))}
                appHelpText="Tipo Prazo Help"
                appTrueValue="S"
                appFalseValue="N"
                appTrueValueLabel="Sim"
                appFalseValueLabel="Não"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="considera_feriado"
                appTitle={capitalize(t("IN18CONSIDERAFERIADODEFAULT"))}
                appHelpText="Considera Feriado Help"
                appTrueValue="S"
                appFalseValue="N"
                appTrueValueLabel="Sim"
                appFalseValueLabel="Não"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="considera_final_sem"
                appTitle={capitalize(t("IN18CONSIDERAFINALDESEMANADEFAULT"))}
                appHelpText="Considera Final de Semana Help"
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

export default FinCondPagrecForm;
