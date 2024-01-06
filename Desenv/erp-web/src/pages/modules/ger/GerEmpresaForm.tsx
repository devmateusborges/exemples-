import { Divider } from "primereact/divider";
import { TabPanel, TabView } from "primereact/tabview";
import { useLayoutEffect, useRef, useState } from "react";
import { capitalize } from "lodash";
import { t } from "i18next";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";

import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldMask from "../../../components/toolkit-react/AppFieldMask";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import FisCertificadoService from "../../../services/modules/fis/FisCertificadoService";
import GerCidadeService from "../../../services/modules/ger/GerCidadeService";
import GerEmpresaService from "../../../services/modules/ger/GerEmpresaService";

import GerEmpresaDet1Form from "./GerEmpresaDet1Form";
import GenericFormPage from "../../generics/GenericFormPage";
import AppContainerTitle from "../../../components/toolkit-react/AppContainerTitle";
import AppContainer from "../../../components/toolkit-react/AppContainer";
import GerEmpresaGrupoService from "../../../services/modules/ger/GerEmpresaGrupoService";
import AppFieldDropdown from "../../../components/toolkit-react/AppFieldDropdown";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import AppContainerDivider from "../../../components/toolkit-react/AppContainerDivider";

const gerCidadeService = new GerCidadeService();
const fisCertificadoService = new FisCertificadoService();
const gerEmpresaService = new GerEmpresaService();
const gerEmpresaGrupoService = new GerEmpresaGrupoService();
const sysTypeDescriptionService = new SysTypeDescriptionService();
const GerEmpresaForm: React.FC = () => {
  // ==============================

  const [detActiveIndex, setDetActiveIndex] = useState(0);
  const [activeIndex, setActiveIndex] = useState(0);
  const dataTableDet1Ref = useRef<any>();
  const [fis_regime_trib_nfs_opt, setFis_regime_trib_nfs_opt] = useState([]);
  const [fis_provedor_nfs_opt, setFis_provedor_nfs_opt] = useState([]);
  const [fis_regime_opt, setFis_regime_opt_opt] = useState([]);

  // ==============================

  useLayoutEffect(() => {
    (async () => {
      let res = await sysTypeDescriptionService.getDescription(
        "ger_empresa",
        "fis_regime_trib_nfs"
      );
      setFis_regime_trib_nfs_opt(res);

      res = await sysTypeDescriptionService.getDescription(
        "ger_empresa",
        "fis_provedor_nfs"
      );
      setFis_provedor_nfs_opt(res);

      res = await sysTypeDescriptionService.getDescription(
        "ger_empresa",
        "fis_regime"
      );
      setFis_regime_opt_opt(res);
    })();
  }, []);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_empresa",
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
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "ativo",
      required: [false, ""],
      defaultValue: "S",
      type: "checkbox",
    },
    {
      fieldName: "razao_social",
      required: [true, "Razão Social is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 characters for Razão Social"],
    },
    {
      fieldName: "fis_regime",
      required: [false, ""],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "end_logradouro",
      required: [true, "Endereço Logradouro is required"],
      maxValue: [100, "Maximum 100 characters for Endereço Logradouro"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "end_logradouro_nr",
      required: [true, "Numero Endereço is required"],
      maxValue: [10, "Maximum 10 characters for Endereço Logradouro"],
      defaultValue: "",
      type: "text",
    },

    {
      fieldName: "end_bairro",
      required: [true, "Bairro is required"],
      maxValue: [100, "Maximum 100 characters for Bairro"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "end_complemento",
      required: [true, "Endereço Complemento is required"],
      maxValue: [100, "Maximum 100 characters for Endereço Complemento"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "end_cep",
      required: [true, "Endereço Cep is required"],
      maxValue: [100, "Maximum 100 characters for Endereço Cep"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "fone_1",
      required: [true, "Telefone 1 is required"],
      maxValue: [100, "Maximum 100 characters for Telefone 1"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "fone_2",
      required: [true, "Telefone 2 is required"],
      maxValue: [100, "Maximum 100 characters for Telefone 2"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "fone_3",
      required: [true, "Telefone 3 is required"],
      maxValue: [100, "Maximum 100 characters for Telefone 3"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "contato_1",
      required: [true, "Contato 1 is required"],
      maxValue: [100, "Maximum 100 characters for Contato 1"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "contato_2",
      required: [true, "Contato 2 is required"],
      maxValue: [100, "Maximum 100 characters for Contato 2"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "contato_3",
      required: [true, "Contato 3 is required"],
      maxValue: [100, "Maximum 100 characters for Contato 3"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "email_1",
      required: [true, "Email is required"],
      maxValue: [255, "Maximum 255 characters for Email"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "doc_cnpj",
      required: [true, "Documento - CNPJ is required"],
      maxValue: [50, "Maximum 50 characters for Documento - CNPJ"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "doc_ie",
      required: [true, "Documento - Ins.Estadual is required"],
      maxValue: [50, "Maximum 50 characters for Documento - Ins.Estadual"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "doc_im",
      required: [true, "Documento - Ins.Municipal is required"],
      maxValue: [50, "Maximum 50 characters for Documento - Ins.Municipal"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "doc_cnae",
      required: [true, "Documento - CNAE is required"],
      maxValue: [50, "Maximum 50 characters for Documento - CNAE"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "doc_junta",
      required: [true, "Documento - Junta Comercial is required"],
      maxValue: [50, "Maximum 50 characters for Documento - Junta Comercial"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "doc_rntrc",
      required: [true, "Documento - RNTRC is required"],
      maxValue: [100, "Maximum 100 characters for Documento - RNTRC"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "data_abertura",
      required: [true, "Data Abertura is required"],
      defaultValue: "",
      type: "date",
    },
    {
      fieldName: "fis_dfe_ambiente",
      required: [true, "Ambiente Transmissão DFE is required"],
      maxValue: [1, "Maximum 1 characters for Ambiente Transmissão DFE"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "fis_dfe_api_token",
      required: [true, "Token da API de DFE is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "fis_regime_trib_nfs",
      required: [false, ""],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "fis_provedor_nfs",
      required: [false, ""],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "fis_incent_cultura",
      required: [false, ""],
      defaultValue: "S",
      type: "checkbox",
    },
    {
      fieldName: "fis_incent_fiscal_nfs",
      required: [false, ""],
      defaultValue: "S",
      type: "checkbox",
    },
    {
      fieldName: "data_validade_a1",
      required: [true, "Data Validade Certificado A1 is required"],
      defaultValue: "",
      type: "date",
    },
    {
      fieldName: "data_validade_a3",
      required: [true, "Data Validade Certificado A3 is required"],
      defaultValue: "",
      type: "date",
    },
    {
      fieldName: "end_ger_cidade_id",
      required: [true, "Cidade is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "fis_certificado_id",
      required: [true, "Certificado is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "ger_empresa_grupo_id",
      required: [true, "Grupo de Empresa is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "doc_cpf",
      required: [true, "Doc. CPF is required"],
      maxValue: [50, "Maximum 50 characters for Doc - CPF"],
      defaultValue: "",
      type: "text",
    },
  ];

  // ==============================

  const formControl = useFormControl({
    fieldControls,
  });

  // ==============================
  const detailsOptions = [
    { name: "ger_empresa_pessoa_childs", ref: dataTableDet1Ref },
  ];
  // ==============================

  return (
    <>
      <GenericFormPage
        appServiceDefault={gerEmpresaService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18GEREMPRESADEFAULT"))}
        appRouteList="/private/ger/gerempresa"
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
                name="sigla_empresa"
                appTitle={capitalize(t("IN18EMPRESASIGLADEFAULT"))}
                appHelpText="Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="razao_social"
                appTitle={capitalize(t("IN18RAZAOSOCIALDEFAULT"))}
                appHelpText="Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="end_logradouro"
                appTitle={capitalize(t("IN18ENDERECOLOGRADOURODEFAULT"))}
                appHelpText="Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="end_logradouro_nr"
                appTitle={capitalize(t("IN18NUMEROENDERECODEFAULT"))}
                appHelpText="Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="end_bairro"
                appTitle={capitalize(t("IN18BAIRRODEFAULT"))}
                appHelpText="Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="end_complemento"
                appTitle={capitalize(t("IN18ENDERECOCOMPLEMENTODEFAULT"))}
                appHelpText="Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="end_cep"
                appTitle={capitalize(t("IN18ENDERECOCEPDEFAULT"))}
                appHelpText="Help"
              />
              <AppFieldMask
                appFormControl={formControl}
                name="fone_1"
                appTitle={capitalize(t("IN18TELEFONE1DEFAULT"))}
                appMask="(99) 9999-9999?9"
              />
              <AppFieldMask
                appFormControl={formControl}
                name="fone_2"
                appTitle={capitalize(t("IN18TELEFONE2DEFAULT"))}
                appMask="(99) 9999-9999?9"
              />
              <AppFieldMask
                appFormControl={formControl}
                name="fone_3"
                appTitle={capitalize(t("IN18TELEFONE3DEFAULT"))}
                appMask="(99) 9999-9999?9"
              />
              <AppFieldText
                appFormControl={formControl}
                name="contato_1"
                appTitle={capitalize(t("IN18CONTATO1DEFAULT"))}
                appHelpText="Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="contato_2"
                appTitle={capitalize(t("IN18CONTATO2DEFAULT"))}
                appHelpText="Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="contato_3"
                appTitle={capitalize(t("IN18CONTATO3DEFAULT"))}
                appHelpText="Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="email_1"
                appTitle={capitalize(t("IN18EMAILDEFAULT"))}
                appHelpText="Help"
              />
              <AppFieldMask
                appFormControl={formControl}
                name="doc_cnpj"
                appTitle={capitalize(t("IN18DOCUMENTOCNPJDEFAULT"))}
                appHelpText="Help"
                appMask="99.999.999/9999-99"
              />
              <AppFieldMask
                appFormControl={formControl}
                name="doc_cpf"
                appTitle={capitalize(t("IN18DOCUMENTOCPFDEFAULT"))}
                appMask="999999999/99"
                appHelpText="Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="doc_ie"
                appTitle={capitalize(t("IN18DOCUMENTOINSESTADUALDEFAULT"))}
                appHelpText="Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="doc_im"
                appTitle={capitalize(t("IN18DOCUMENTOINSMUNICIPALDEFAULT"))}
                appHelpText="Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="doc_cnae"
                appTitle={capitalize(t("IN18DOCUMENTOCNAEDEFAULT"))}
                appHelpText="Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="doc_junta"
                appTitle={capitalize(t("IN18DOCUMENTOJUNTACOMERCIALDEFAULT"))}
                appHelpText="Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="doc_rntrc"
                appTitle={capitalize(t("IN18DOCUMENTORNTRCDEFAULT"))}
                appHelpText="Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="fis_dfe_ambiente"
                appTitle={capitalize(t("IN18AMBIENTETRANSMISSAODFEDEFAULT"))}
                appHelpText="Ambiente Transmissão DFE Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="fis_dfe_api_token"
                appTitle={capitalize(t("IN18TOKENDAAPIDEDFEDEFAULT"))}
                appHelpText="Token da API de DFE Help"
              />
              <AppFieldDate
                appFormControl={formControl}
                name="data_validade_a1"
                appTitle={capitalize(t("IN18DATAVALIDADECERTIFICADOA1DEFAULT"))}
                appHelpText="Data Validade Certificado A1 Help"
                appShowTime
                appShowSeconds
              />
              <AppFieldDate
                appFormControl={formControl}
                name="data_validade_a3"
                appTitle={capitalize(t("IN18DATAVALIDADECERTIFICADOA3DEFAULT"))}
                appHelpText="Data Validade Certificado A3 Help"
                appShowTime
                appShowSeconds
              />

              <AppFieldDate
                appFormControl={formControl}
                name="data_abertura"
                appTitle={capitalize(t("IN18DATAABERTURADEFAULT"))}
                appHelpText="Data Abertura Help"
                appShowTime
                appShowSeconds
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="fis_incent_cultura"
                appTitle={capitalize(t("IN18INCENTIVACULTURADEFAULT"))}
                appHelpText="Incentiva Cultura Help"
                appTrueValue="S"
                appTrueValueLabel="Sim"
                appFalseValue="N"
                appFalseValueLabel="Não"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="fis_incent_fiscal_nfs"
                appTitle={capitalize(
                  t("IN18POSSUEINCENTIVOFISCALDANFSDEFAULT")
                )}
                appHelpText="Possue incentivo fiscal da NFS Help"
                appTrueValue="S"
                appTrueValueLabel="Sim"
                appFalseValue="N"
                appFalseValueLabel="Não"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="ativo"
                appTitle={capitalize(t("IN18ATIVODEFAULT"))}
                appHelpText="Ativo Help"
                appTrueValue="S"
                appTrueValueLabel="Sim"
                appFalseValue="N"
                appFalseValueLabel="Não"
              />
              <Divider />

              <AppFieldDropdownFk
                appFormControl={formControl}
                name="fis_certificado_id"
                appTitle={capitalize(t("IN18CERTIFICADONOMEDEFAULT"))}
                appHelpText="Certificado Help"
                appOptionLabel="nome"
                appOptionValue="id"
                appDataKey="id"
                appServiceDefault={fisCertificadoService}
                appServiceFilterId="id"
                appServiceFilterDescription="nome"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                name="end_ger_cidade_id"
                appTitle={capitalize(t("IN18CIDADENOMEDEFAULT"))}
                appHelpText="Cidade Help"
                appOptionLabel="nome"
                appOptionValue="id"
                appDataKey="id"
                appServiceDefault={gerCidadeService}
                appServiceFilterId="id"
                appServiceFilterDescription="nome"
              />

              <AppFieldDropdownFk
                appFormControl={formControl}
                name="ger_empresa_grupo_id"
                appTitle="Grupo de Empresa"
                appHelpText="Grupo de Empresa Help"
                appOptionLabel="sigla_ger_empresa_grupo"
                appOptionValue="id"
                appDataKey="id"
                appServiceDefault={gerEmpresaGrupoService}
                appServiceFilterId="id"
                appServiceFilterDescription="sigla_ger_empresa_grupo"
              />
              <AppFieldDropdown
                appFormControl={formControl}
                name="fis_regime_trib_nfs"
                appTitle={capitalize(t("IN18REGIMETRIBUTACAODEFAULT"))}
                appOptions={fis_regime_trib_nfs_opt}
                appHelpText="Regime Tributação Help"
                appOptionLabel="description_type"
                appOptionValue="value_type"
              />
              <AppFieldDropdown
                appFormControl={formControl}
                name="fis_provedor_nfs"
                appTitle={capitalize(t("IN18PROVEDOREMISSAODEFAULT"))}
                appOptions={fis_provedor_nfs_opt}
                appHelpText="Provedor Emissão Help"
                appOptionLabel="description_type"
                appOptionValue="value_type"
              />
              <AppFieldDropdown
                appFormControl={formControl}
                name="fis_regime"
                appTitle={capitalize(t("IN18TIPOREGIMEDEFAULT"))}
                appOptions={fis_regime_opt}
                appHelpText="Tipo Regime Help"
                appOptionLabel="description_type"
                appOptionValue="value_type"
              />
            </AppContainerFields>
          </TabPanel>
        </TabView>
        <AppContainer className="w-full mt-2">
          <AppContainerDivider appPosition="left" appTitle="Dets Form" />
          <div className="md:p-2">
            <TabView
              activeIndex={detActiveIndex}
              onTabChange={(e) => setDetActiveIndex(e.index)}
              renderActiveOnly={false}
              panelContainerClassName="p-0"
            >
              <TabPanel
                header={capitalize(t("IN18PESSOADEFAULT"))}
                className="p-0"
              >
                <GerEmpresaDet1Form
                  appRef={dataTableDet1Ref}
                  appDataTableDataValue={
                    formControl.getValues().ger_empresa_pessoa_childs
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

export default GerEmpresaForm;
