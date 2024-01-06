import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useLayoutEffect, useRef, useState } from "react";
import AppContainer from "../../../components/toolkit-react/AppContainer";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppContainerTitle from "../../../components/toolkit-react/AppContainerTitle";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import AppFieldDropdown from "../../../components/toolkit-react/AppFieldDropdown";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import SysLicenceService from "../../../services/modules/sys/SysLicenceService";
import SysPlanService from "../../../services/modules/sys/SysPlanService";
import SysService from "../../../services/modules/sys/SysService ";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import SysUserService from "../../../services/modules/sys/SysUserService";
import GenericFormPage from "../../generics/GenericFormPage";
import SysLicenceFormDet1 from "./SysLicenceFormDet1";

const sysLicenceService = new SysLicenceService();
const sysTypeDescriptionService = new SysTypeDescriptionService();
const sysPlanService = new SysPlanService();
const sysService = new SysService();
const sysUserService = new SysUserService();

const SysLicenceForm: React.FC = () => {
  const dataTableDet1Ref = useRef<any>();
  const [detActiveIndex, setDetActiveIndex] = useState(0);
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  const [Tipo_doc_opt, setTipo_doc_opt] = useState([]);
  const [Status_opt, setStatus_opt] = useState([]);

  // ==============================

  useLayoutEffect(() => {
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "sys_licence",
        "status"
      );
      setStatus_opt(res);
    })();
  }, []);
  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "code_licence",
      required: [true, "Licence - Sigla is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "nome_solicitante",
      required: [true, "Nome Solicitante is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "doc",
      required: [true, "Documento is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "end_logradouro",
      required: [true, "Endereço - Logradouro is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "end_bairro",
      required: [true, "Endereço - Bairro is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "end_numero",
      required: [true, "Endereço - Número is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "end_cidade",
      required: [true, "Endereço - Cidade is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "end_uf",
      required: [true, "Endereço - Unidade Federação is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "end_pais",
      required: [true, "Endereço - País is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "chamado_id",
      required: [true, "Chamado is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "status_data",
      required: [true, "Status Data is required"],
      defaultValue: "",
      type: "datetime",
    },
    {
      fieldName: "status_observacao",
      required: [true, "Status Observação Data is required"],
      defaultValue: "",
      type: "text",
      maxValue: [250, "Maximum 250 for valor"],
    },
    {
      fieldName: "sys_version",
      required: [true, "Sistema Versão is required"],
      defaultValue: "",
      type: "text",
      maxValue: [50, "Maximum 50 for valor"],
    },
    {
      fieldName: "sys_plan_id",
      required: [true, ""],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "sys_id",
      required: [true, ""],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "sys_user_id",
      required: [true, ""],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "status",
      required: [true, "Status is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "tipo_doc",
      required: [true, "Tipo Documento is required"],
      defaultValue: "",
      type: "radio",
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
  const detailsOptions = [
    { name: "sys_licence_restriction_childs", ref: dataTableDet1Ref },
  ];
  // ==============================

  return (
    <>
      <GenericFormPage
        appTitleClassIcon="pi pi-star text-red-500"
        appServiceDefault={sysLicenceService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18SYSLICENCASDEFAULT"))}
        appRouteList="/private/sys/syslicence"
        appDetailsOptions={detailsOptions}
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
                name="code_licence"
                appTitle={capitalize(t("IN18LICENCASIGLADEFAULT"))}
                appHelpText="Licence - Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome_solicitante"
                appTitle={capitalize(t("IN18SOLICITANTENOMEDEFAULT"))}
                appHelpText="Nome Solicitante Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="doc"
                appTitle={capitalize(t("IN18DOCUMENTODEFAULT"))}
                appHelpText="Documento Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="end_logradouro"
                appTitle={capitalize(t("IN18ENDERECOLOGRADOURODEFAULT"))}
                appHelpText="Endereço Logradouro Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="end_bairro"
                appTitle={capitalize(t("IN18ENDERECOBAIRRODEFAULT"))}
                appHelpText="Endereço Bairro Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="end_cidade"
                appTitle={capitalize(t("IN18ENDERECOCIDADEDEFAULT"))}
                appHelpText="Endereço cidade Solicitante Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="end_uf"
                appTitle={capitalize(t("IN18ENDERECOUNIDADEFEDERACAODEFAULT"))}
                appHelpText="Endereço - Unidade Federação Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="end_pais"
                appTitle={capitalize(t("IN18ENDERECOPAISDEFAULT"))}
                appHelpText="Endereço Pais Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="end_numero"
                appTitle={capitalize(t("IN18NUMEROENDERECODEFAULT"))}
                appHelpText="Endereço Numero Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="chamado_id"
                appTitle={capitalize(t("IN18CHAMADOIDENTIFICADORDEFAULT"))}
                appHelpText="Chamado Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="status_observacao"
                appTitle={capitalize(t("IN18STATUSOBSERVACAODEFAULT"))}
                appHelpText="Status Observação Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="sys_version"
                appTitle={capitalize(t("IN18VERSAODEFAULT"))}
                appHelpText="Sistema Versão Help"
              />
              <AppFieldDate
                appFormControl={formControl}
                name="status_data"
                appTitle={capitalize(t("IN18DATADOSTATUSDEFAULT"))}
                appHelpText="Data do Status Help"
                appShowTime
                appShowSeconds
              />
              <AppFieldText
                appFormControl={formControl}
                name="tipo_doc"
                appTitle={capitalize(t("IN18TIPODOCUMENTODEFAULT"))}
                appHelpText="Tipo Documento Help"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={sysPlanService}
                name="sys_plan_id"
                appTitle={capitalize(t("IN18PLANOSIGLADEFAULT"))}
                appHelpText="Sigla - Plano Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="code_plan"
                appServiceFilterDescription="code_plan"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={sysService}
                name="sys_id"
                appTitle={capitalize(t("IN18SISTEMASIGLADEFAULT"))}
                appHelpText="Sigla - Sistema Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="code_sys"
                appServiceFilterDescription="code_sys"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={sysUserService}
                name="sys_user_id"
                appTitle={capitalize(t("IN18USUARIOLOGINDEFAULT"))}
                appHelpText="Usuario Login Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="login"
                appServiceFilterDescription="login"
              />
              <AppFieldDropdown
                appFormControl={formControl}
                name="status"
                appTitle={capitalize(t("IN18STATUSDEFAULT"))}
                appOptions={Status_opt}
                appHelpText="Status Help"
                appOptionLabel="description_type"
                appOptionValue="value_type"
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
        <AppContainer className="w-full mt-2">
          <AppContainerTitle appTitle="Dets Form" appSmall />
          <div className="md:p-2">
            <TabView
              activeIndex={detActiveIndex}
              onTabChange={(e) => setActiveIndex(e.index)}
              renderActiveOnly={false}
              panelContainerClassName="p-0"
            >
              <TabPanel
                header="System-Restrição do Sistema x Licença"
                className="p-0"
              >
                <SysLicenceFormDet1
                  appRef={dataTableDet1Ref}
                  appDataTableDataValue={
                    formControl.getValues().sys_licence_restriction_childs
                  }
                />
              </TabPanel>
            </TabView>
          </div>
        </AppContainer>
      </GenericFormPage>
    </>
  );
};

export default SysLicenceForm;
