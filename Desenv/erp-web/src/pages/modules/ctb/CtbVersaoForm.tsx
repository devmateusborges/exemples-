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
import CtbVersaoService from "../../../services/modules/ctb/CtbVersaoService";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import GenericFormPage from "../../generics/GenericFormPage";

const ctbVersaoService = new CtbVersaoService();
const sysTypeDescriptionService = new SysTypeDescriptionService();

const CtbVersaoForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);

  const [tipo_rp_opt, setTipo_rp_opt] = useState([]);
  // ==============================

  useLayoutEffect(() => {
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ctb_versao",
        "tipo_rp"
      );
      setTipo_rp_opt(res);
    })();
  }, []);

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
      fieldName: "tipo_rp",
      required: [true, "Tipo RP is required"],
      defaultValue: "",
      type: "checkbox",
    },
    {
      fieldName: "versao_atual",
      required: [false, ""],
      defaultValue: "",
      type: "checkbox",
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
        appServiceDefault={ctbVersaoService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18CTBVERSAODEFAULT"))}
        appRouteList="/private/ctb/ctbversao"
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

              <AppFieldRadioButton
                appFormControl={formControl}
                name="tipo_rp"
                appTitle={capitalize(t("IN18TIPORPDEFAULT"))}
                appOptions={tipo_rp_opt}
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
              <AppFieldDate
                appFormControl={formControl}
                name="data_per_ini"
                appHelpText="Data Período Inicial Help"
                appTitle={capitalize(t("IN18DATAPERIODOINICIALDEFAULT"))}
              />
              <AppFieldDate
                appFormControl={formControl}
                name="data_per_fin"
                appHelpText="Data Período Final Help"
                appTitle={capitalize(t("IN18DATAPERIODOFINALDEFAULT"))}
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

export default CtbVersaoForm;
