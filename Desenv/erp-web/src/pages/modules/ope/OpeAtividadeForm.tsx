import { t } from "i18next";
import { capitalize } from "lodash";
import { Divider } from "primereact/divider";
import { TabPanel, TabView } from "primereact/tabview";
import { useEffect, useLayoutEffect, useRef, useState } from "react";
import AppContainer from "../../../components/toolkit-react/AppContainer";
import AppContainerDivider from "../../../components/toolkit-react/AppContainerDivider";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppContainerTitle from "../../../components/toolkit-react/AppContainerTitle";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDropdown from "../../../components/toolkit-react/AppFieldDropdown";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldNumber from "../../../components/toolkit-react/AppFieldNumber";
import AppFieldRadioButton from "../../../components/toolkit-react/AppFieldRadioButton";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import GerUmedidaService from "../../../services/modules/ger/GerUmedidaService";
import OpeAtividadeGrupoService from "../../../services/modules/ope/OpeAtividadeGrupoService";
import OpeAtividadeService from "../../../services/modules/ope/OpeAtividadeService";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import GenericFormPage from "../../generics/GenericFormPage";
import OpeAtividadeDet1Form from "./OpeAtividadeDet1Form";

const opeAtividadeService = new OpeAtividadeService();
const gerUmedidaService = new GerUmedidaService();
const opeAtividadeGrupoService = new OpeAtividadeGrupoService();
const sysTypeDescriptionService = new SysTypeDescriptionService();

const OpeAtividadeForm: React.FC = () => {
  // ==============================
  const [detActiveIndex, setDetActiveIndex] = useState(0);
  const [activeIndex, setActiveIndex] = useState(0);
  const dataTableDet1Ref = useRef<any>();
  const [
    valida_seq_medicao_trab_centro_opt,
    setValida_seq_medicao_trab_centro_opt,
  ] = useState([]);
  const [valida_saldo_area_aberta_opt, setValida_saldo_area_aberta_opt] =
    useState([]);

  const [valida_prev_itemserv_opt, setValida_prev_itemserv_opt] = useState([]);
  const [valida_prev_rec_opt, setValida_prev_rec_opt] = useState([]);
  const [valida_regra_config_opt, setValida_regra_config_opt] = useState([]);
  const [valida_tipo_executor_opt, setValida_tipo_executor_opt] = useState([]);
  const [valida_rec_equip_opt, setValida_rec_equip_opt] = useState([]);
  const [valida_rec_pessoa_opt, setValida_rec_pessoa_opt] = useState([]);
  const [valida_itemserv_i_opt, setValida_itemserv_i_opt] = useState([]);
  const [valida_itemserv_s_opt, setValida_itemserv_s_opt] = useState([]);
  const [valida_tipo_prop_rec_equip_opt, setValida_tipo_prop_rec_equip_opt] =
    useState([]);
  const [valida_tipo_prop_rec_pessoa_opt, setValida_tipo_prop_rec_pessoa_opt] =
    useState([]);
  const [
    valida_tot_area_acum_per_centro_plan_opt,
    setValida_tot_area_acum_per_centro_plan_opt,
  ] = useState([]);
  const [
    valida_tot_area_acum_per_centro_exec_opt,
    setValida_tot_area_acum_per_centro_exec_opt,
  ] = useState([]);
  const [valida_tot_area_ord_exec_opt, setValida_tot_area_ord_exec_opt] =
    useState([]);
  // ==============================

  useLayoutEffect(() => {
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_atividade",
        "valida_seq_medicao_trab_centro"
      );
      setValida_seq_medicao_trab_centro_opt(res);
    })();

    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_atividade",
        "valida_saldo_area_aberta"
      );
      setValida_saldo_area_aberta_opt(res);
    })();

    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_atividade",
        "valida_prev_itemserv"
      );
      setValida_prev_itemserv_opt(res);
    })();

    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_atividade",
        "valida_prev_rec"
      );
      setValida_prev_rec_opt(res);
    })();

    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_atividade",
        "valida_regra_config"
      );
      setValida_regra_config_opt(res);
    })();

    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_atividade",
        "valida_tipo_executor"
      );
      setValida_tipo_executor_opt(res);
    })();

    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_atividade",
        "valida_rec_equip"
      );
      setValida_rec_equip_opt(res);
    })();

    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_atividade",
        "valida_rec_pessoa"
      );
      setValida_rec_pessoa_opt(res);
    })();

    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_atividade",
        "valida_itemserv_i"
      );
      setValida_itemserv_i_opt(res);
    })();

    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_atividade",
        "valida_itemserv_s"
      );
      setValida_itemserv_s_opt(res);
    })();

    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_atividade",
        "valida_tipo_prop_rec_equip"
      );
      setValida_tipo_prop_rec_equip_opt(res);
    })();

    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_atividade",
        "valida_tipo_prop_rec_pessoa"
      );
      setValida_tipo_prop_rec_pessoa_opt(res);
    })();

    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_atividade",
        "valida_tot_area_acum_per_centro_plan"
      );
      setValida_tot_area_acum_per_centro_plan_opt(res);
    })();

    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_atividade",
        "valida_tot_area_acum_per_centro_exec"
      );
      setValida_tot_area_acum_per_centro_exec_opt(res);
    })();

    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_atividade",
        "valida_tot_area_ord_exec"
      );
      setValida_tot_area_ord_exec_opt(res);
    })();
  }, []);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_atividade",
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
      maxValue: [100, "Maximum 100 characters for Nome"],
    },
    {
      fieldName: "ativo",
      required: [false, ""],
      defaultValue: "",
      type: "checkbox",
    },
    {
      fieldName: "parada",
      required: [true, "Parada is required"],
      defaultValue: "",
      type: "checkbox",
    },
    {
      fieldName: "index_bor",
      required: [true, "Index Atividade Bordo is required"],
      defaultValue: "",
      type: "text",
      maxValue: [50, "Maximum 50 characters for Index Atividade Bordo"],
    },
    {
      fieldName: "largura",
      required: [true, "Largura is required"],
      defaultValue: "",
      type: "numeric",
      maxValue: [18, "Maximum 18 characters for Largura"],
    },
    {
      fieldName: "valida_seq_medicao_trab_centro",
      required: [true, "Válida sequência medição is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "valida_saldo_area_aberta",
      required: [true, "Válida saldo Área em aberto is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "valida_prev_itemserv",
      required: [true, "Válida previsão Item/Serviço is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "valida_prev_rec",
      required: [true, "Válida previsão Recurso is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "valida_regra_config",
      required: [true, "Válida regra configurável is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "valida_tipo_executor",
      required: [true, "Válida tipo executor is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "valida_rec_equip",
      required: [true, "Obriga Recurso is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "valida_rec_pessoa",
      required: [true, "Obriga Recurso Pessoa is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "valida_itemserv_i",
      required: [true, "Obriga Item is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "valida_itemserv_s",
      required: [true, "Obriga Serviço is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "valida_tipo_prop_rec_equip",
      required: [true, "Válida tipo prop. Recurso is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "valida_tipo_prop_rec_pessoa",
      required: [true, "Válida tipo prop. Pessoa is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "valida_tot_area_acum_per_centro_plan",
      required: [true, "Planejamento is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "valida_tot_area_acum_per_centro_exec",
      required: [true, "Execução is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "valida_tot_area_ord_exec",
      required: [true, "Válida total de area/prod is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "ger_umedida_id",
      required: [true, "U. Medida - is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "ope_atividade_grupo_id",
      required: [true, "Grupo de Atividade - is required"],
      defaultValue: "",
      type: "foreignkey",
    },
  ];

  // ==============================
  const formControl = useFormControl({
    fieldControls,
  });
  // ==============================
  const detailsOptions = [
    { name: "ope_atividade_relac_prod_childs", ref: dataTableDet1Ref },
  ];
  // ==============================
  return (
    <GenericFormPage
      appTitleClassIcon="pi pi-star text-red-500"
      appServiceDefault={opeAtividadeService}
      appFormControl={formControl}
      appDetailsOptions={detailsOptions}
      appTitle="OPE-Atividade Form"
      appRouteList="/private/ope/opeatividade"
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
              name="sigla_atividade"
              appTitle={capitalize(t("IN18ATIVIDADESIGLADEFAULT"))}
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
              name="index_bor"
              appTitle={capitalize(t("IN18INDEXATIVIDADEBORDODEFAULT"))}
              appHelpText="Index Atividade Bordo Help"
            />
            <AppFieldNumber
              appFormControl={formControl}
              name="largura"
              appTitle={capitalize(t("IN18QUANTIDADELARGURADEFAULT"))}
              appHelpText="Largura Help"
              appMaxFractionDigits={6}
            />
            <AppFieldDropdownFk
              appFormControl={formControl}
              name="ger_umedida_id"
              appTitle={capitalize(t("IN18UMEDIDASIGLADEFAULT"))}
              appHelpText="U. Medida Help"
              appOptionLabel="nome"
              appOptionValue="id"
              appDataKey="id"
              appServiceDefault={gerUmedidaService}
              appServiceFilterId="id"
              appServiceFilterDescription="sigla_umedida"
            />
            <AppFieldDropdownFk
              appFormControl={formControl}
              name="ope_atividade_grupo_id"
              appTitle={capitalize(t("IN18GRUPODEATIVIDADESIGLADEFAULT"))}
              appHelpText="Grupo de Atividade Help"
              appOptionLabel="nome"
              appOptionValue="id"
              appDataKey="id"
              appServiceDefault={opeAtividadeGrupoService}
              appServiceFilterId="id"
              appServiceFilterDescription="sigla_atividade_grupo"
            />

            <AppFieldDropdown
              appFormControl={formControl}
              name="valida_seq_medicao_trab_centro"
              appTitle={capitalize(t("IN18VALIDASEQUENCIAMEDICAODEFAULT"))}
              appOptions={valida_seq_medicao_trab_centro_opt}
              appHelpText="Válida sequência medição Help"
              appOptionLabel="description_type"
              appOptionValue="value_type"
            />

            <AppFieldDropdown
              appFormControl={formControl}
              name="valida_saldo_area_aberta"
              appTitle={capitalize(t("IN18VALIDASALDOAREAEMABERTODEFAULT"))}
              appOptions={valida_saldo_area_aberta_opt}
              appHelpText="Válida saldo Área em aberto Help"
              appOptionLabel="description_type"
              appOptionValue="value_type"
            />

            <AppFieldDropdown
              appFormControl={formControl}
              name="valida_prev_itemserv"
              appTitle={capitalize(t("IN18VALIDAPREVISAOITEM/SERVICODEFAULT"))}
              appOptions={valida_prev_itemserv_opt}
              appHelpText="Válida previsão Item/Serviço Help"
              appOptionLabel="description_type"
              appOptionValue="value_type"
            />

            <AppFieldDropdown
              appFormControl={formControl}
              name="valida_prev_rec"
              appTitle={capitalize(t("IN18VALIDAPREVISAORECURSODEFAULT"))}
              appOptions={valida_prev_rec_opt}
              appHelpText="Válida previsão Recurso Help"
              appOptionLabel="description_type"
              appOptionValue="value_type"
            />

            <AppFieldDropdown
              appFormControl={formControl}
              name="valida_regra_config"
              appTitle={capitalize(t("IN18VALIDAREGRACONFIGURAVELDEFAULT"))}
              appOptions={valida_regra_config_opt}
              appHelpText="Válida regra configurável Help"
              appOptionLabel="description_type"
              appOptionValue="value_type"
            />

            <AppFieldDropdown
              appFormControl={formControl}
              name="valida_tipo_executor"
              appTitle={capitalize(t("IN18VALIDATIPOEXECUTORDEFAULT"))}
              appOptions={valida_tipo_executor_opt}
              appHelpText="Válida tipo executor Help"
              appOptionLabel="description_type"
              appOptionValue="value_type"
            />

            <AppFieldDropdown
              appFormControl={formControl}
              name="valida_rec_equip"
              appTitle={capitalize(t("IN18OBRIGARECURSODEFAULT"))}
              appOptions={valida_rec_equip_opt}
              appHelpText="Obriga Recurso Help"
              appOptionLabel="description_type"
              appOptionValue="value_type"
            />

            <AppFieldDropdown
              appFormControl={formControl}
              name="valida_rec_pessoa"
              appTitle={capitalize(t("IN18OBRIGARECURSOPESSOADEFAULT"))}
              appOptions={valida_rec_pessoa_opt}
              appHelpText="Obriga Recurso Pessoa Help"
              appOptionLabel="description_type"
              appOptionValue="value_type"
            />

            <AppFieldDropdown
              appFormControl={formControl}
              name="valida_itemserv_i"
              appTitle={capitalize(t("IN18OBRIGAITEMDEFAULT"))}
              appOptions={valida_itemserv_i_opt}
              appHelpText="Obriga Item Help"
              appOptionLabel="description_type"
              appOptionValue="value_type"
            />

            <AppFieldDropdown
              appFormControl={formControl}
              name="valida_itemserv_s"
              appTitle={capitalize(t("IN18OBRIGASERVICODEFAULT"))}
              appOptions={valida_itemserv_s_opt}
              appHelpText="Obriga Serviço Help"
              appOptionLabel="description_type"
              appOptionValue="value_type"
            />

            <AppFieldDropdown
              appFormControl={formControl}
              name="valida_tipo_prop_rec_equip"
              appTitle={capitalize(t("IN18VALIDATIPOPROPRECURSODEFAULT"))}
              appOptions={valida_tipo_prop_rec_equip_opt}
              appHelpText="Válida tipo prop. Recurso Help"
              appOptionLabel="description_type"
              appOptionValue="value_type"
            />

            <AppFieldDropdown
              appFormControl={formControl}
              name="valida_tipo_prop_rec_pessoa"
              appTitle={capitalize(t("IN18VALIDATIPOPROPPESSOADEFAULT"))}
              appOptions={valida_tipo_prop_rec_pessoa_opt}
              appHelpText="Válida tipo prop. Pessoa Help"
              appOptionLabel="description_type"
              appOptionValue="value_type"
            />

            <AppFieldDropdown
              appFormControl={formControl}
              name="valida_tot_area_acum_per_centro_plan"
              appTitle={capitalize(t("IN18PLANEJAMENTODEFAULT"))}
              appOptions={valida_tot_area_acum_per_centro_plan_opt}
              appHelpText="Planejamento Help"
              appOptionLabel="description_type"
              appOptionValue="value_type"
            />

            <AppFieldDropdown
              appFormControl={formControl}
              name="valida_tot_area_acum_per_centro_exec"
              appTitle={capitalize(t("IN18EXECUCAODEFAULT"))}
              appOptions={valida_tot_area_acum_per_centro_exec_opt}
              appHelpText="Execução Help"
              appOptionLabel="description_type"
              appOptionValue="value_type"
            />

            <AppFieldDropdown
              appFormControl={formControl}
              name="valida_tot_area_ord_exec"
              appTitle={capitalize(t("IN18VALIDATOTALDEAREA/PRODDEFAULT"))}
              appOptions={valida_tot_area_ord_exec_opt}
              appHelpText="Válida total de area/prod Help"
              appOptionLabel="description_type"
              appOptionValue="value_type"
            />

            <AppFieldCheck
              appFormControl={formControl}
              name="parada"
              appTitle={capitalize(t("IN18PARADADEFAULT"))}
              appHelpText="Parada Help"
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
              header="Operação-Relacionamento de Atividade Produtivas"
              className="p-0"
            >
              <OpeAtividadeDet1Form
                appRef={dataTableDet1Ref}
                appDataTableDataValue={
                  formControl.getValues()?.ope_atividade_relac_prod_childs
                }
              />
            </TabPanel>
          </TabView>
        </div>
      </AppContainer>
    </GenericFormPage>
  );
};

export default OpeAtividadeForm;
