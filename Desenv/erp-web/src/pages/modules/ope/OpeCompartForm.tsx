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
import OpeCompartService from "../../../services/modules/ope/OpeCompartService";
import OpeCompartStatusService from "../../../services/modules/ope/OpeCompartStatusService";
import OpeCompartSubgrupoService from "../../../services/modules/ope/OpeCompartSubgrupoService";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import GenericFormPage from "../../generics/GenericFormPage";

const opeCompartService = new OpeCompartService();
const opeCompartSubgrupoService = new OpeCompartSubgrupoService();
const opeCompartStatusService = new OpeCompartStatusService();
const sysTypeDescriptionService = new SysTypeDescriptionService();

const OpeCompartForm: React.FC = () => {
  // ==============================
  const [activeIndex, setActiveIndex] = useState(0);
  const [medicao_trab_centro_opt, setMedicao_trab_centro_opt] = useState([]);
  // ==============================
  useLayoutEffect(() => {
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_compart",
        "medicao_trab_centro"
      );
      setMedicao_trab_centro_opt(res);
    })();
  }, []);
  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_compart",
      required: [true, "Sigla is required"],
      maxValue: [50, "Maximum 50 characters for Sigla"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "nome",
      required: [true, "Nome is required"],
      maxValue: [100, "Maximum 100 characters for Nome"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "ativo",
      required: [false, ""],
      defaultValue: "S",
      type: "checkbox",
    },

    {
      fieldName: "capacidade",
      required: [true, "Capacidade is required"],
      maxValue: [18, "Maximum 18 characters for Capacidade"],
      defaultValue: "",
      type: "numeric",
    },
    {
      fieldName: "valida_itemserv",
      required: [false, ""],
      defaultValue: "N",
      type: "checkbox",
    },
    {
      fieldName: "medicao_trab_centro",
      required: [true, "Medição de Trabalho is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "data_aquisicao",
      required: [true, "Data Aquisição is required"],
      defaultValue: "",
      type: "date",
    },
    {
      fieldName: "data_status",
      required: [true, "Data Status is required"],
      defaultValue: "",
      type: "date",
    },
    {
      fieldName: "observacao",
      required: [true, "Observação is required"],
      maxValue: [250, "Maximum 250 characters for Observação"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "valor_aquisicao",
      required: [true, "Valor Aquisição is required"],
      maxValue: [18, "Maximum 18 characters for Valor Aquisição"],
      defaultValue: "",
      type: "numeric",
    },
    {
      fieldName: "numero_serie",
      required: [true, "Número Série is required"],
      maxValue: [100, "Maximum 100 characters for Número Série"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "data_baixa",
      required: [true, "Data Baixa is required"],
      defaultValue: "",
      type: "date",
    },
    {
      fieldName: "ope_compart_subgrupo_id",
      required: [true, "Subgrupo de Compartimento is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "ope_compart_status_id",
      required: [true, "Status de Compartimento is required"],
      defaultValue: "",
      type: "foreignkey",
    },
  ];

  const formControl = useFormControl({
    fieldControls,
  });
  return (
    <>
      <GenericFormPage
        appTitleClassIcon="pi pi-star text-red-500"
        appServiceDefault={opeCompartService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18OPECOMPARTIMENTODEFAULT"))}
        appRouteList="/private/ope/opecompart"
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
                name="sigla_compart"
                appTitle={capitalize(t("IN18COMPARTIMENTOSSIGLADEFAULT"))}
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
                name="observacao"
                appTitle={capitalize(t("IN18OBSERVACAODEFAULT"))}
                appHelpText="Observação Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="numero_serie"
                appTitle={capitalize(t("IN18NUMEROSERIEDEFAULT"))}
                appHelpText="Número Série Help"
              />
              <AppFieldDate
                appFormControl={formControl}
                name="data_baixa"
                appTitle={capitalize(t("IN18DATABAIXADEFAULT"))}
                appHelpText="Data Baixa do nascimento"
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="valor_aquisicao"
                appHelpText="Valor Aquisição Help"
                appTitle={capitalize(t("IN18VALORAQUISICAODEFAULT"))}
                appMaxFractionDigits={2}
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="capacidade"
                appHelpText="Capacidade Help"
                appTitle={capitalize(t("IN18CAPACIDADEDEFAULT"))}
                appMaxFractionDigits={6}
              />
              <AppFieldDate
                appFormControl={formControl}
                name="data_aquisicao"
                appTitle={capitalize(t("IN18DATAAQUISICAODEFAULT"))}
                appHelpText="Data Aquisição do nascimento"
              />
              <AppFieldDate
                appFormControl={formControl}
                name="data_status"
                appTitle={capitalize(t("IN18DATASTATUSDEFAULT"))}
                appHelpText="Data Status do nascimento"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={opeCompartSubgrupoService}
                name="ope_compart_subgrupo_id"
                appTitle={capitalize(
                  t("IN18SUBGRUPODECOMPARTIMENTOSIGLADEFAULT")
                )}
                appHelpText="Subgrupo de Compartimento"
                appOptionLabel="sigla_compart_subgrupo"
                appOptionValue="id"
                appDataKey="id"
                appServiceFilterId="id"
                appServiceFilterDescription="sigla_compart_subgrupo"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={opeCompartStatusService}
                name="ope_compart_status_id"
                appTitle={capitalize(
                  t("IN18SUBGRUPODECOMPARTIMENTONOMEDEFAULT")
                )}
                appHelpText="Status de Compartimento"
                appOptionLabel="sigla_compart_status"
                appOptionValue="id"
                appDataKey="id"
                appServiceFilterId="id"
                appServiceFilterDescription="sigla_compart_status"
              />

              <AppFieldRadioButton
                appFormControl={formControl}
                name="medicao_trab_centro"
                appTitle={capitalize(t("IN18MEDICAODETRABALHODEFAULT"))}
                appOptions={medicao_trab_centro_opt}
                appOptionsLabel="description_type"
                appOptionsValue="value_type"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="valida_itemserv"
                appTitle={capitalize(t("IN18VALIDAITEMSERVDEFAULT"))}
                appHelpText="Válida Itemserv Período Help"
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

export default OpeCompartForm;
