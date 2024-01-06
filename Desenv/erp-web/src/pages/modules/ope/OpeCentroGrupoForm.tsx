import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useRef, useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import OpeCentroGrupoService from "../../../services/modules/ope/OpeCentroGrupoService";
import OpeCentroSubTipoService from "../../../services/modules/ope/OpeCentroSubTipoService";
import GenericFormPage from "../../generics/GenericFormPage";

const opeCentroGrupoService = new OpeCentroGrupoService();

const opeCentroSubTipo = new OpeCentroSubTipoService();

const OpeCentroGrupoForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_centro_grupo",
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
      maxValue: [100, "Maximum 100 characters for Nome"],
    },

    {
      fieldName: "ativo",
      required: [false, ""],
      defaultValue: "S",
      type: "checkbox",
    },
    {
      fieldName: "ope_centro_subtipo_id",
      required: [false, "Centro Subtipo is required"],
      defaultValue: "S",
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
        appServiceDefault={opeCentroGrupoService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18OPECENTROGRUPODEFAULT"))}
        appRouteList="/private/ope/opecentrogrupo"
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
                name="sigla_centro_grupo"
                appTitle={capitalize(t("IN18GRUPOCENTROSIGLADEFAULT"))}
                appHelpText="Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />

              <AppFieldDropdownFk
                appFormControl={formControl}
                name="ope_centro_subtipo_id"
                appTitle={capitalize(t("IN18CENTROSUBTIPONOMEDEFAULT"))}
                appHelpText="Centro Subtipo Help"
                appOptionLabel="nome"
                appOptionValue="id"
                appDataKey="id"
                appServiceDefault={opeCentroSubTipo}
                appServiceFilterId="id"
                appServiceFilterDescription="nome"
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

export default OpeCentroGrupoForm;
