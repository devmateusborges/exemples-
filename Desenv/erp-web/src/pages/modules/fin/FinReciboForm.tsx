import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useLayoutEffect, useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldNumber from "../../../components/toolkit-react/AppFieldNumber";
import AppFieldRadioButton from "../../../components/toolkit-react/AppFieldRadioButton";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import FinReciboService from "../../../services/modules/fin/FinReciboService";
import GerPessoaEnderecoService from "../../../services/modules/ger/GerPessoaEnderecoService";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import GenericFormPage from "../../generics/GenericFormPage";

const finReciboService = new FinReciboService();
const gerPessoaEnderecoService = new GerPessoaEnderecoService();
const sysTypeDescriptionService = new SysTypeDescriptionService();

const FinReciboForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  const [status_opt, setStatus_opt] = useState([]);
  // ==============================

  useLayoutEffect(() => {
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "fin_recibo",
        "status"
      );
      setStatus_opt(res);
    })();
  }, []);
  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "nome_pessoa",
      required: [true, "Pessoa - Nome is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "nr_doc_pessoa",
      required: [true, "Número do Documento - Pessoa is required"],
      defaultValue: "",
      type: "text",
      maxValue: [50, "Maximum 50 for valor"],
    },
    {
      fieldName: "tipo_doc_pessoa",
      required: [true, "Tipo do Documento - Pessoa is required"],
      defaultValue: "",
      type: "text",
      maxValue: [50, "Maximum 50 for valor"],
    },
    {
      fieldName: "status",
      required: [true, "Status is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "valor",
      required: [true, "Valor Período is required"],
      defaultValue: "",
      type: "numeric",
      minValue: [2, "Minimum 2 characters for valor"],
      maxValue: [18, "Maximum 18 for valor"],
    },
    {
      fieldName: "data_recibo",
      required: [true, "Data Recibo is required"],
      defaultValue: "",
      type: "date",
    },
    {
      fieldName: "conteudo",
      required: [true, "Conteudo Recibo is required"],
      defaultValue: "",
      type: "text",
      maxValue: [250, "Maximum 250 for valor"],
    },
    {
      fieldName: "ger_pessoa_endereco_id",
      required: [true, "Pessoa Endereço is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "status_observacao",
      required: [true, "Status Observção is required"],
      defaultValue: "",
      type: "text",
      maxValue: [250, "Maximum 250 for valor"],
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
        appServiceDefault={finReciboService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18FINRECIBODEFAULT"))}
        appRouteList="/private/fin/finrecibo"
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
                name="nome_pessoa"
                appTitle={capitalize(t("IN18PESSOANOMEDEFAULT"))}
                appHelpText="Pessoa - Nome Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nr_doc_pessoa"
                appTitle={capitalize(t("IN18NUMERODODOCUMENTOPESSOADEFAULT"))}
                appHelpText="Número do Documento - Pessoa Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="tipo_doc_pessoa"
                appTitle={capitalize(t("IN18TIPODODOCUMENTOPESSOADEFAULT"))}
                appHelpText="Tipo do Documento - Pessoa Help"
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="valor"
                appHelpText="Valor"
                appTitle={capitalize(t("IN18TIPOVALORDEFAULT"))}
                appMinFractionDigits={4}
              />
              <AppFieldText
                appFormControl={formControl}
                name="status_observacao"
                appTitle={capitalize(t("IN18STATUSOBSERVCAODEFAULT"))}
                appHelpText="Status Observção Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="conteudo"
                appTitle={capitalize(t("IN18CONTEUDODEFAULT"))}
                appHelpText="Conteudo Help"
              />
              <AppFieldDate
                appFormControl={formControl}
                name="data_recibo"
                appTitle={capitalize(t("IN18DATARECIBODEFAULT"))}
                appHelpText="Data Recibo Help"
              />
              <AppFieldRadioButton
                appFormControl={formControl}
                name="status"
                appTitle={capitalize(t("IN18TIPOSTATUSDEFAULT"))}
                appOptions={status_opt}
                appOptionsLabel="description_type"
                appOptionsValue="value_type"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={gerPessoaEnderecoService}
                name="ger_pessoa_endereco_id"
                appTitle={capitalize(t("IN18ENDERECODAPESSOAEMAILDEFAULT"))}
                appHelpText="Endereço da Pessoa - Email Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="email"
                appServiceFilterDescription="email"
              />
            </AppContainerFields>
          </TabPanel>
        </TabView>
      </GenericFormPage>
    </>
  );
};

export default FinReciboForm;
