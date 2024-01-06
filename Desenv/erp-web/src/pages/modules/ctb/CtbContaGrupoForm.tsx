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
import CtbContaGrupoService from "../../../services/modules/ctb/CtbContaGrupoService";
import CtbContaVersaoService from "../../../services/modules/ctb/CtbContaVersaoService";
import GenericFormPage from "../../generics/GenericFormPage";

const ctbContaGrupoService = new CtbContaGrupoService();

const ctbContaVersaoService = new CtbContaVersaoService();

const CtbContaGrupoForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_conta_grupo",
      required: [true, "Grupo de Conta - Sigla is required"],
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
      fieldName: "estrutura",
      required: [true, "Estrutura is required"],
      defaultValue: "",
      type: "text",
      maxValue: [50, "Maximum 50 for valor"],
    },
    {
      fieldName: "ctb_conta_versao_id",
      required: [false, ""],
      defaultValue: "",
      type: "foreignkey",
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
        appServiceDefault={ctbContaGrupoService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18CTBGRUPODECONTADEFAULT"))}
        appRouteList="/private/ctb/ctbcontagrupo"
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
                name="sigla_conta_grupo"
                appTitle={capitalize(t("IN18GRUPODECONTASIGLADEFAULT"))}
                appHelpText="Grupo de Conta - Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="estrutura"
                appTitle={capitalize(t("IN18ESTRUTURADEFAULT"))}
                appHelpText="Estrutura Help"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={ctbContaVersaoService}
                name="ctb_conta_versao_id"
                appTitle={capitalize(t("IN18VERSAOCONTACONTABILSIGLADEFAULT"))}
                appHelpText="Versão de Conta Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="sigla_versao"
                appServiceFilterDescription="sigla_versao"
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

export default CtbContaGrupoForm;
