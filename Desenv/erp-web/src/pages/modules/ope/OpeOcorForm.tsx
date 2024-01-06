import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useLayoutEffect, useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldRadioButton from "../../../components/toolkit-react/AppFieldRadioButton";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import GerUmedidaService from "../../../services/modules/ger/GerUmedidaService";
import OpeOcorGrupoService from "../../../services/modules/ope/OpeOcorGrupoService";
import OpeOcorService from "../../../services/modules/ope/OpeOcorService";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import GenericFormPage from "../../generics/GenericFormPage";

const opeOcorService = new OpeOcorService();
const sysTypeDescriptionService = new SysTypeDescriptionService();
const opeOcorGrupoService = new OpeOcorGrupoService();
const gerUmedidaService = new GerUmedidaService();

const OpeOcorForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  const [tipo_opt, setTipo_opt] = useState([]);
  const [tipo_lanc_opt, setTipo_lanc_opt] = useState([]);
  // ==============================
  useLayoutEffect(() => {
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_ocor",
        "tipo"
      );
      setTipo_opt(res);
    })();
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_ocor",
        "tipo_lanc"
      );
      setTipo_lanc_opt(res);
    })();
  }, []);
  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_ocor",
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
      fieldName: "icon",
      required: [true, "Icon is required"],
      maxValue: [50, "Maximum 50 characters for Icon"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "tipo",
      required: [true, "Tipo is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "tipo_lanc",
      required: [true, "Tipo Lancamento is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "ope_ocor_grupo_id",
      required: [true, "Grupo de Ocorrência is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "ger_umedida_id",
      required: [true, "U. Medida is required"],
      defaultValue: "",
      type: "foreignkey",
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
        appServiceDefault={opeOcorService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18OPEOCORRENCIADEFAULT"))}
        appRouteList="/private/ope/opeocor"
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
                name="sigla_ocor"
                appTitle={capitalize(t("IN18GRUPODEOCORRENCIASIGLADEFAULT"))}
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
                name="icon"
                appTitle={capitalize(t("IN18ICONDEFAULT"))}
                appHelpText="Icon Help"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                name="ope_ocor_grupo_id"
                appTitle={capitalize(t("IN18GRUPODEOCORRENCIASIGLADEFAULT"))}
                appHelpText="Grupo de Ocorrência Help"
                appOptionLabel="sigla_ocor_grupo"
                appOptionValue="id"
                appDataKey="id"
                appServiceDefault={opeOcorGrupoService}
                appServiceFilterId="id"
                appServiceFilterDescription="sigla_ocor_grupo"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                name="ger_umedida_id"
                appTitle={capitalize(t("IN18UMEDIDASIGLADEFAULT"))}
                appHelpText="U. Medida Help"
                appOptionLabel="sigla_umedida"
                appOptionValue="id"
                appDataKey="id"
                appServiceDefault={gerUmedidaService}
                appServiceFilterId="id"
                appServiceFilterDescription="sigla_umedida"
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
                name="tipo_lanc"
                appTitle={capitalize(t("IN18TIPOLANCAMENTODEFAULT"))}
                appOptions={tipo_lanc_opt}
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

export default OpeOcorForm;
