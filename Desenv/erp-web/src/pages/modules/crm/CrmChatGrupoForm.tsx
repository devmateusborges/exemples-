import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useLayoutEffect, useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldRadioButton from "../../../components/toolkit-react/AppFieldRadioButton";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import CrmChatGrupoService from "../../../services/modules/crm/CrmChatGrupoService";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import SysUserService from "../../../services/modules/sys/SysUserService";
import GenericFormPage from "../../generics/GenericFormPage";

const crmChatGrupoService = new CrmChatGrupoService();
const sysUserService = new SysUserService();

const CrmChatGrupoForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  const sysTypeDescriptionService = new SysTypeDescriptionService();
  // ==============================
  const [tipo_opt, setTipo_opt] = useState([]);

  useLayoutEffect(() => {
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "crm_chat_grupo",
        "tipo"
      );
      setTipo_opt(res);
    })();
  }, []);
  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_chat_grupo",
      required: [true, "Chat Grupo - Sigla is required"],
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
      fieldName: "tipo",
      required: [true, "Tipo is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "senha",
      required: [true, "Senha is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "acesso_privado",
      required: [true, "Acesso_privado is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "sys_user_id_dest",
      required: [false, ""],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "sys_user_id_orig",
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
        appServiceDefault={crmChatGrupoService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18CRMGRUPOSDOCHATDEFAULT"))}
        appRouteList="/private/crm/crmchatgrupo"
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
                name="sigla_chat_grupo"
                appTitle={capitalize(t("IN18CHATGRUPOSIGLADEFAULT"))}
                appHelpText="Chat Grupo - Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="senha"
                appTitle={capitalize(t("IN18SENHADEFAULT"))}
                appHelpText="Senha Help"
              />
              <AppFieldRadioButton
                appFormControl={formControl}
                name="tipo"
                appTitle={capitalize(t("IN18TIPODEFAULT"))}
                appOptions={tipo_opt}
                appOptionsLabel="description_type"
                appOptionsValue="value_type"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={sysUserService}
                name="sys_user_id_dest"
                appTitle="Usuário Destino"
                appHelpText="Usuário Destino Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="name"
                appServiceFilterDescription="name"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={sysUserService}
                name="sys_user_id_orig"
                appTitle="Usuário Origem"
                appHelpText="Usuário Origem Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="name"
                appServiceFilterDescription="name"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="acesso_privado"
                appTitle={capitalize(t("IN18ACESSOPRIVADODEFAULT"))}
                appHelpText="Acesso Privado Help"
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

export default CrmChatGrupoForm;
