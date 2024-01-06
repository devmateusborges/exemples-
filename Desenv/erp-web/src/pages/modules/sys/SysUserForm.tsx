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
import SysTranslateLangService from "../../../services/modules/sys/SysTranslateLangService";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import SysUserService from "../../../services/modules/sys/SysUserService";
import GenericFormPage from "../../generics/GenericFormPage";

const sysUserService = new SysUserService();
const sysTranslateLangService = new SysTranslateLangService();
const sysTypeDescriptionService = new SysTypeDescriptionService();

const SysUserForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================
  const [Origem, setOrigem] = useState([]);
  // ==============================

  useLayoutEffect(() => {
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "sys_user",
        "origem"
      );
      setOrigem(res);
    })();
  }, []);
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "login",
      required: [true, "Login is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "name",
      required: [true, "Nome is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "password",
      required: [true, "Senha is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "email",
      required: [true, "Email is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "active_message",
      required: [true, "Ativar Menssagem is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "phone",
      required: [true, "Telefone is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "document",
      required: [true, "Telefone is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "image_url",
      required: [true, "Imagem Url externo is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "provider",
      required: [true, "fornecedor externo is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "provider_code",
      required: [true, "codigo fornecedor externo is required"],
      defaultValue: "",
      type: "text",
      maxValue: [50, "Maximum 50 for valor"],
    },
    {
      fieldName: "gtm_default",
      required: [true, "gtm_default externo is required"],
      defaultValue: "",
      type: "text",
      maxValue: [50, "Maximum 50 for valor"],
    },
    {
      fieldName: "login_ext",
      required: [true, "login externo is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "sys_tran_lang_id_default",
      required: [true, "Sistema-Traduzir idioma is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "origem",
      required: [true, "Origem externo is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "email_verified",
      required: [true, "Email Verificado is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "chat",
      required: [false, ""],
      defaultValue: "N",
      type: "checkbox",
    },
    {
      fieldName: "admin",
      required: [false, ""],
      defaultValue: "N",
      type: "checkbox",
    },
    {
      fieldName: "active",
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
        appServiceDefault={sysUserService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18SYSUSUARIOSDEFAULT"))}
        appRouteList="/private/sys/SysUser"
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
                name="login"
                appTitle={capitalize(t("IN18LOGINUSUARIODESTINODEFAULT"))}
                appHelpText="Login Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="name"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="password"
                appTitle={capitalize(t("IN18SENHADEFAULT"))}
                appHelpText="Senha Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="email"
                appTitle={capitalize(t("IN18EMAILDEFAULT"))}
                appHelpText="Email Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="active_message"
                appTitle={capitalize(t("IN18MENSAGEMDEATIVACAODEFAULT"))}
                appHelpText="Mensagem de Ativação Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="phone"
                appTitle={capitalize(t("IN18TELEFONEDEFAULT"))}
                appHelpText="Telefone Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="document"
                appTitle={capitalize(t("IN18TIPODODOCUMENTOPESSOADEFAULT"))}
                appHelpText="documento Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="login_ext"
                appTitle={capitalize(t("IN18LOGINEXTERNODEFAULT"))}
                appHelpText="Login externo Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="image_url"
                appTitle={capitalize(t("IN18URLDAIMAGEMDOUSUARIODEFAULT"))}
                appHelpText="image url Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="provider"
                appTitle={capitalize(t("IN18TIPODEFORNECEDORDEFAULT"))}
                appHelpText="Provaider Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="provider_code"
                appTitle={capitalize(t("IN18CODIGODOFORNECEDORDEFAULT"))}
                appHelpText="provider code Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="gtm_default"
                appTitle={capitalize(t("IN18GTMPADRAODEFAULT"))}
                appHelpText="gtm default Help"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={sysTranslateLangService}
                name="sys_tran_lang_id_default"
                appTitle={capitalize(t("IN18TRADUZIRIDIOMASIGLADEFAULT"))}
                appHelpText="Traduzir idioma Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="code"
                appServiceFilterDescription="code"
              />
              <AppFieldRadioButton
                appFormControl={formControl}
                name="origem"
                appTitle={capitalize(t("IN18USUARIOORIGEMNOMEDEFAULT"))}
                appHelpText="Origem Help"
                appOptions={Origem}
                appOptionsLabel="description_type"
                appOptionsValue="value_type"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="admin"
                appTitle={capitalize(t("IN18ADMINDEFAULT"))}
                appHelpText="Adiminstração Help"
                appTrueValue="S"
                appFalseValue="N"
                appTrueValueLabel="Sim"
                appFalseValueLabel="Não"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="chat"
                appTitle={capitalize(t("IN18CHATDEFAULT"))}
                appHelpText=" chat Help"
                appTrueValue="S"
                appFalseValue="N"
                appTrueValueLabel="Sim"
                appFalseValueLabel="Não"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="email_verified"
                appTitle={capitalize(t("IN18EMAILVERIFICADO/ADEFAULT"))}
                appHelpText="Email Verificados Help"
                appTrueValue="S"
                appFalseValue="N"
                appTrueValueLabel="Sim"
                appFalseValueLabel="Não"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="active"
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

export default SysUserForm;
