import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import AppFieldNumber from "../../../components/toolkit-react/AppFieldNumber";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import CtbTipoSaldoService from "../../../services/modules/ctb/CtbTipoSaldoService";
import GenericFormPage from "../../generics/GenericFormPage";

const ctbTipoSaldoService = new CtbTipoSaldoService();

const CtbTipoSaldoForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_tipo_saldo",
      required: [true, "Tipo de Saldo - Sigla is required"],
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
      fieldName: "mes_ini_fechamento",
      required: [true, "Mês Inicial de Fechamento is required"],
      defaultValue: "",
      type: "numeric",
    },
    {
      fieldName: "mes_fin_fechamento",
      required: [true, "Mês Final de Fechamento is required"],
      defaultValue: "",
      type: "numeric",
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
        appServiceDefault={ctbTipoSaldoService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18CTBTIPODESALDODEFAULT"))}
        appRouteList="/private/ctb/ctbtiposaldo"
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
                name="sigla_tipo_saldo"
                appTitle={capitalize(t("IN18TIPOSALDOSIGLADEFAULT"))}
                appHelpText="Tipo de Saldo - Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="mes_ini_fechamento"
                appHelpText="Mês Inicial de Fechamento Help"
                appTitle={capitalize(t("IN18MESINICIALDEFECHAMENTODEFAULT"))}
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="mes_fin_fechamento"
                appHelpText="Mês Final de Fechamento Help"
                appTitle={capitalize(t("IN18MESFINALDEFECHAMENTODEFAULT"))}
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

export default CtbTipoSaldoForm;
