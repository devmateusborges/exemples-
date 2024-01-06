import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useLayoutEffect, useRef, useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldRadioButton from "../../../components/toolkit-react/AppFieldRadioButton";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import OpeOcorTipoService from "../../../services/modules/ope/OpeOcorTipoService";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import GenericFormPage from "../../generics/GenericFormPage";

const sysTypeDescriptionService = new SysTypeDescriptionService();
const opeOcorTipoService = new OpeOcorTipoService();

const OpeOcorTipoForm: React.FC = () => {
  // ==============================
  const [activeIndex, setActiveIndex] = useState(0);
  const [tipo_opt, setTipo_opt] = useState([]);
  const [obrig_ope_compart_opt, setObrig_ope_compart_opt] = useState([]);
  // ==============================
  useLayoutEffect(() => {
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_ocor_tipo",
        "tipo"
      );
      setTipo_opt(res);
    })();

    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_ocor_tipo",
        "obrig_ope_compart"
      );
      setObrig_ope_compart_opt(res);
    })();
  }, []);
  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_ocor_tipo",
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
      fieldName: "tipo",
      required: [true, "Tipo is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "obrig_ope_compart",
      required: [true, "Usuário de Inserção is required"],
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
        appServiceDefault={opeOcorTipoService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18OPETIPODEOCORRENCIADEFAULT"))}
        appRouteList="/private/ope/opeocortipo"
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
                name="sigla_ocor_tipo"
                appTitle={capitalize(t("IN18TIPODEOCORRENCIASIGLADEFAULT"))}
                appHelpText="Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldRadioButton
                appFormControl={formControl}
                name="tipo"
                appTitle={capitalize(t("IN18TIPODEFAULT"))}
                appOptions={tipo_opt}
                appOptionsLabel="description_type"
                appOptionsValue="value_type"
              />
              <AppFieldRadioButton
                appFormControl={formControl}
                name="obrig_ope_compart"
                appTitle={capitalize(t("IN18OBRIGACOMPARTIMENTODEFAULT"))}
                appOptions={obrig_ope_compart_opt}
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

export default OpeOcorTipoForm;
