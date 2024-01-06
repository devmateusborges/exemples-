import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldNumber from "../../../components/toolkit-react/AppFieldNumber";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import CtbCompGrupoService from "../../../services/modules/ctb/CtbCompGrupoService";
import CtbCompService from "../../../services/modules/ctb/CtbCompService";
import GerUmedidaService from "../../../services/modules/ger/GerUmedidaService";
import GenericFormPage from "../../generics/GenericFormPage";

const ctbCompService = new CtbCompService();

const ctbCompGrupoService = new CtbCompGrupoService();
const gerUmedidaService = new GerUmedidaService();

const CtbCompForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_comp",
      required: [true, "Componente - Sigla is required"],
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
      fieldName: "ativo",
      required: [false, ""],
      defaultValue: "S",
      type: "checkbox",
    },
    {
      fieldName: "fator_calc_origem",
      required: [true, "Fator Cálculo Origem is required"],
      defaultValue: "",
      type: "numeric",
      minValue: [6, "Minimum 6 characters for valor"],
      maxValue: [18, "Maximum 18 for valor"],
    },
    {
      fieldName: "ger_umedida_id",
      required: [false, ""],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "ctb_comp_grupo_id",
      required: [false, ""],
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
        appServiceDefault={ctbCompService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18CTBCOMPONENTEDEFAULT"))}
        appRouteList="/private/ctb/ctbcomp"
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
                name="sigla_comp"
                appTitle={capitalize(t("IN18COMPONENTESIGLADEFAULT"))}
                appHelpText="Componente - Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="fator_calc_origem"
                appHelpText="Fator Cálculo Origem Help"
                appTitle={capitalize(t("IN18FATORCALCULOORIGEMDEFAULT"))}
                appMinFractionDigits={6}
                appMaxFractionDigits={18}
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={gerUmedidaService}
                name="ger_umedida_id"
                appTitle={capitalize(t("IN18UMEDIDASIGLADEFAULT"))}
                appHelpText="Geral-U.Medida Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="sigla_umedida"
                appServiceFilterDescription="sigla_umedida"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={ctbCompGrupoService}
                name="ctb_comp_grupo_id"
                appTitle={capitalize(t("IN18GRUPODOCOMPONENTESIGLADEFAULT"))}
                appHelpText="Grupo de Componente Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="sigla_comp_grupo"
                appServiceFilterDescription="sigla_comp_grupo"
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

export default CtbCompForm;
