import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useRef, useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import OpeAtividadeGrupoService from "../../../services/modules/ope/OpeAtividadeGrupoService";
import GenericFormPage from "../../generics/GenericFormPage";

const opeAtividadeGrupoService = new OpeAtividadeGrupoService();

const OpeAtividadeGrupoFrom: React.FC = () => {
  // ==============================
  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_atividade_grupo",
      required: [true, "Grupo de Atividade - Sigla is required"],
      defaultValue: "",
      type: "text",
      maxValue: [50, "Maximum 50 characters for Grupo de Atividade - Sigla"],
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
      required: [true, "Ativo is required"],
      defaultValue: "S",
      type: "checkbox",
    },
    {
      fieldName: "ordem",
      required: [true, "Ordem is required"],
      defaultValue: "",
      type: "text",
      maxValue: [3, "Maximum 3 characters for Ordem"],
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
        appServiceDefault={opeAtividadeGrupoService}
        appFormControl={formControl}
        appTitle="OPE-Grupo de Atividade Form"
        appRouteList="/private/ope/opeatividadegrupo"
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
                name="sigla_atividade_grupo"
                appTitle={capitalize(t("IN18GRUPODEATIVIDADESIGLADEFAULT"))}
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
                name="ordem"
                appTitle={capitalize(t("IN18ORDEMDEFAULT"))}
                appHelpText="Ordem Help"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="ativo"
                appTitle={capitalize(t("IN18ATIVODEFAULT"))}
                appHelpText="Ativo"
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

export default OpeAtividadeGrupoFrom;
