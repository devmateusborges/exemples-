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
import CrmOrgService from "../../../services/modules/crm/CrmOrgService";
import GenericFormPage from "../../generics/GenericFormPage";

const crmOrgService = new CrmOrgService();

const CrmOrgForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_org",
      required: [true, "Organização - Sigla is required"],
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
      fieldName: "ger_visual_user",
      required: [
        true,
        "Gerente visualiza atendimento de outros usuários is required",
      ],
      defaultValue: "N",
      type: "checkbox",
    },
    {
      fieldName: "user_visual_user",
      required: [
        true,
        "Usuário visualiza atendimento de outros usuários is required",
      ],
      defaultValue: "S",
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
        appTitleClassIcon="pi pi-star text-red-500"
        appServiceDefault={crmOrgService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18CRMORGANIZACAODEFAULT"))}
        appRouteList="/private/crm/crmorg"
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
                name="sigla_org"
                appTitle={capitalize(t("IN18ORGANIZACAOSIGLADEFAULT"))}
                appHelpText="Organização - Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="ger_visual_user"
                appTitle={capitalize(
                  t("IN18GERENTEVISUALIZAATENDIMENTODEOUTROSUSUARIOSDEFAULT")
                )}
                appHelpText="Gerente visualiza Help"
                appTrueValue="S"
                appFalseValue="N"
                appTrueValueLabel="Sim"
                appFalseValueLabel="Não"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="user_visual_user"
                appTitle={capitalize(
                  t("IN18USUARIOVISUALIZAATENDIMENTODEOUTROSUSUARIOSDEFAULT")
                )}
                appHelpText="Usuário visualiza atendimento de outros usuários Help"
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

export default CrmOrgForm;
