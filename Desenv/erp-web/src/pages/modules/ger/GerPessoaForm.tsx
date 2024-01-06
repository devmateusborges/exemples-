/* eslint-disable no-bitwise */
import { TabPanel, TabView } from "primereact/tabview";
import { useRef, useState } from "react";
import { t } from "i18next";
import _, { capitalize } from "lodash";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";

import GerPessoaService from "../../../services/modules/ger/GerPessoaService";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";

import GenericFormPage from "../../generics/GenericFormPage";
import GerPessoaDet1Form from "./GerPessoaDet1Form";
import GerPessoaDet2Form from "./GerPessoaDet2Form";
import AppFieldNumber from "../../../components/toolkit-react/AppFieldNumber";
import AppContainer from "../../../components/toolkit-react/AppContainer";
import AppContainerTitle from "../../../components/toolkit-react/AppContainerTitle";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppContainerDivider from "../../../components/toolkit-react/AppContainerDivider";

const gerPessoaService = new GerPessoaService();

const GerPessoaForm: React.FC = () => {
  // ==============================
  const dataTableDet1Ref = useRef<any>();
  const dataTableDet2Ref = useRef<any>();
  const [activeIndex, setActiveIndex] = useState(0);
  const [detActiveIndex, setDetActiveIndex] = useState(0);
  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_pes",
      required: [true, "Pessoa -Sigla is required"],
      defaultValue: "",
      type: "text",
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
      required: [true, ""],
      defaultValue: "S",
      type: "checkbox",
    },
    {
      fieldName: "razao_social",
      required: [true, "Razão Social is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "doc_cnpj",
      required: [true, "Documento - CNPJ is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "doc_cpf",
      required: [true, "Documento - CPF is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "doc_ie",
      required: [true, "Documento - IE is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "doc_im",
      required: [true, "Documento - IM is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "doc_cnae",
      required: [true, "Documento - CNAE is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "doc_junta",
      required: [true, "Documento - Junta is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "doc_rg",
      required: [true, "Documento - RG is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "doc_rg_org_exp",
      required: [true, "Documento - RG Orgão Expedidor is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "doc_crc",
      required: [true, "Documento - CRC is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "doc_crc_seq",
      required: [true, "Documento - CRC Sequência is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "doc_crc_org_exp",
      required: [true, "Documento - CRC Orgão Expedidor is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "doc_taf",
      required: [true, "Documento - AFT is required"],
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
      fieldName: "fis_regime",
      required: [true, "Regime is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "fone_1",
      required: [true, "Telefone1 is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "fone_2",
      required: [true, "Telefone2 is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "fone_3",
      required: [true, "Telefone3 is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "contato_1",
      required: [true, "Contato 1 is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "contato_2",
      required: [true, "Contato 2 is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "contato_3",
      required: [true, "Contato 3 is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "contrib_icms",
      required: [true, "Contribuição ICMS is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "nr_rntrc",
      required: [true, "Número RNTRC is required"],
      defaultValue: "",
      type: "numeric",
    },
    {
      fieldName: "nr_registro_est_cte",
      required: [true, "Número do Registro Estadual de CTE is required"],
      defaultValue: "",
      type: "numeric",
    },
    {
      fieldName: "data_valid",
      required: [true, "Data de Validação is required"],
      defaultValue: "",
      type: "date",
    },
  ];
  // ==============================

  const formControl = useFormControl({
    fieldControls,
  });

  // ==============================
  const detailsOptions = [
    { name: "ger_pessoa_conta_banco_childs", ref: dataTableDet1Ref },
    { name: "ger_pessoa_endereco_childs", ref: dataTableDet2Ref },
  ];
  // ==============================

  return (
    <>
      <GenericFormPage
        appServiceDefault={gerPessoaService}
        appFormControl={formControl}
        appTitle="GER-Pessoa Form"
        appRouteList="/private/ger/gerpessoa"
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
                name="sigla_pes"
                appTitle={capitalize(t("IN18PESSOASIGLADEFAULT"))}
                appHelpText="Pessoa -Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="razao_social"
                appTitle={capitalize(t("IN18RAZAOSOCIALDEFAULT"))}
                appHelpText="Razão Social Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="doc_cnpj"
                appTitle={capitalize(t("IN18DOCUMENTOCNPJDEFAULT"))}
                appHelpText="Documento - CNPJ Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="doc_cpf"
                appTitle={capitalize(t("IN18DOCUMENTOCPFDEFAULT"))}
                appHelpText="Documento - CPF Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="doc_ie"
                appTitle={capitalize(t("IN18DOCUMENTOIEDEFAULT"))}
                appHelpText="Documento - IE Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="doc_im"
                appTitle={capitalize(t("IN18DOCUMENTOIMDEFAULT"))}
                appHelpText="Documento - IM Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="doc_cnae"
                appTitle={capitalize(t("IN18DOCUMENTOCNAEDEFAULT"))}
                appHelpText="Documento - CNAE Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="doc_junta"
                appTitle={capitalize(t("IN18DOCUMENTOJUNTACOMERCIALDEFAULT"))}
                appHelpText="Documento - Junta Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="doc_rg"
                appTitle={capitalize(t("IN18DOCUMENTORGDEFAULT"))}
                appHelpText="Documento - RG Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="doc_rg_org_exp"
                appTitle={capitalize(t("IN18DOCUMENTORGORGAOEXPEDIDORDEFAULT"))}
                appHelpText="Documento - RG Orgão Expedidor Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="doc_crc"
                appTitle={capitalize(t("IN18DOCUMENTOCRCDEFAULT"))}
                appHelpText="Documento - CRC  Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="doc_crc_seq"
                appTitle={capitalize(t("IN18DOCUMENTOCRCSEQUENCIADEFAULT"))}
                appHelpText="Documento - CRC Sequência Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="doc_crc_org_exp"
                appTitle={capitalize(
                  t("IN18DOCUMENTOCRCORGAOEXPEDIDORDEFAULT")
                )}
                appHelpText="Documento - CRC Orgão Expedidor Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="doc_taf"
                appTitle={capitalize(t("IN18DOCUMENTOAFTDEFAULT"))}
                appHelpText="Documento - AFT Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="fis_regime"
                appTitle={capitalize(t("IN18REGIMEDEFAULT"))}
                appHelpText="Regime Help"
              />

              <AppFieldText
                appFormControl={formControl}
                name="nr_rntrc"
                appTitle={capitalize(t("IN18NUMERORNTRCDEFAULT"))}
                appHelpText="Número RNTRC Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nr_registro_est_cte"
                appTitle={capitalize(
                  t("IN18NUMERODOREGISTROESTADUALDECTEDEFAULT")
                )}
                appHelpText="Número do Registro Estadual de CTE Help"
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="contrib_icms"
                appTitle={capitalize(t("IN18CONTRIBUICAOICMSDEFAULT"))}
                appHelpText="Contribuição ICMS Help"
                appMinFractionDigits={0}
                appUseGrouping={false}
              />
              <AppFieldDate
                appFormControl={formControl}
                name="data_abertura"
                appTitle={capitalize(t("IN18DATAABERTURADEFAULT"))}
                appHelpText="Data Abertura Help"
              />
              <AppFieldDate
                appFormControl={formControl}
                name="data_valid"
                appTitle={capitalize(t("IN18DATADEVALIDACAODEFAULT"))}
                appHelpText="Data de Validação Help"
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
            </AppContainerFields>
          </TabPanel>
          <TabPanel header="Contato" className="p-0">
            <AppContainerFields>
              <AppFieldText
                appFormControl={formControl}
                name="fone_1"
                appTitle={capitalize(t("IN18TELEFONE1DEFAULT"))}
                appHelpText="Telefone1 Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="fone_2"
                appTitle={capitalize(t("IN18TELEFONE2DEFAULT"))}
                appHelpText="Telefone2 Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="fone_3"
                appTitle={capitalize(t("IN18TELEFONE3DEFAULT"))}
                appHelpText="Telefone3 Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="contato_1"
                appTitle={capitalize(t("IN18CONTATO1DEFAULT"))}
                appHelpText="Contato 1 Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="contato_2"
                appTitle={capitalize(t("IN18CONTATO2DEFAULT"))}
                appHelpText="Contato 2 Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="contato_3"
                appTitle={capitalize(t("IN18CONTATO3DEFAULT"))}
                appHelpText="Contato 3 Help"
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
                header={capitalize(t("IN18CONTADOBANCODEFAULT"))}
                className="p-0"
              >
                <GerPessoaDet1Form
                  appRef={dataTableDet1Ref}
                  appDataTableDataValue={
                    formControl.getValues()?.ger_pessoa_conta_banco_childs
                  }
                />
              </TabPanel>
              <TabPanel
                header={capitalize(t("IN18ENDERECODEFAULT"))}
                className="p-0"
              >
                <GerPessoaDet2Form
                  appRef={dataTableDet2Ref}
                  appDataTableDataValue={
                    formControl.getValues()?.ger_pessoa_endereco_childs
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

export default GerPessoaForm;
