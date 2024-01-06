import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useLayoutEffect, useRef, useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDropdown from "../../../components/toolkit-react/AppFieldDropdown";
import AppFieldRadioButton from "../../../components/toolkit-react/AppFieldRadioButton";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import OpeCentro2OrdTipoService from "../../../services/modules/ope/OpeCentro2OrdTipoService";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import GenericFormPage from "../../generics/GenericFormPage";

const opeCentro2OrdTipoService = new OpeCentro2OrdTipoService();
const sysTypeDescriptionService = new SysTypeDescriptionService();

const OpeCentro2OrdTipoForm: React.FC = () => {
  // ==============================
  const [activeIndex, setActiveIndex] = useState(0);
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
  // ==============================

  useLayoutEffect(() => {
    (async () => {
      /* TODO-OPE nao tem type_description */
      const res = await sysTypeDescriptionService.getDescription(
        "ope_centro2_ord_tipo",
        "valida_saldo_area_aberta"
      );
      setValida_saldo_area_aberta_opt(res);
    })();

    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_centro2_ord_tipo",
        "valida_prev_itemserv"
      );
      setValida_prev_itemserv_opt(res);
    })();
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_centro2_ord_tipo",
        "valida_prev_rec"
      );
      setValida_prev_rec_opt(res);
    })();
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_centro2_ord_tipo",
        "valida_regra_config"
      );
      setValida_regra_config_opt(res);
    })();
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_centro2_ord_tipo",
        "valida_tipo_executor"
      );
      setValida_tipo_executor_opt(res);
    })();
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_centro2_ord_tipo",
        "valida_rec_equip"
      );
      setValida_rec_equip_opt(res);
    })();
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_centro2_ord_tipo",
        "valida_rec_pessoa"
      );
      setValida_rec_pessoa_opt(res);
    })();
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_centro2_ord_tipo",
        "valida_itemserv_i"
      );
      setValida_itemserv_i_opt(res);
    })();
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_centro2_ord_tipo",
        "valida_itemserv_s"
      );
      setValida_itemserv_s_opt(res);
    })();
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_centro2_ord_tipo",
        "valida_tipo_prop_rec_equip"
      );
      setValida_tipo_prop_rec_equip_opt(res);
    })();
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_centro2_ord_tipo",
        "valida_tipo_prop_rec_pessoa"
      );
      setValida_tipo_prop_rec_pessoa_opt(res);
    })();
  }, []);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_ord_tipo",
      required: [true, "Tipo de Ordem - Sigla is required"],
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
      defaultValue: "S",
      type: "checkbox",
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
      required: [true, "Válida Recurso is required"],
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
      required: [true, "Valida tipo prop. Recurso - Equipamento is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "valida_tipo_prop_rec_pessoa",
      required: [true, "Valida tipo prop. Recurso - Pessoa is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "valida_rec_pessoa",
      required: [true, "Obriga Recurso is required"],
      defaultValue: "",
      type: "radio",
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
        appServiceDefault={opeCentro2OrdTipoService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18OPETIPODEORDEMDEFAULT"))}
        appRouteList="/private/ope/opecentro2ordtipo"
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
                name="sigla_ord_tipo"
                appTitle={capitalize(t("IN18TIPODEORDEMSIGLADEFAULT"))}
                appHelpText="Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />

              <AppFieldDropdown
                appFormControl={formControl}
                name="valida_saldo_area_aberta"
                appTitle={capitalize(t("IN18VALIDASALDOAREAEMABERTODEFAULT"))}
                appOptions={valida_saldo_area_aberta_opt}
                appHelpText="Válida saldo Área em aberto Pessoa Help"
                appOptionLabel="description_type"
                appOptionValue="value_type"
              />

              <AppFieldDropdown
                appFormControl={formControl}
                name="valida_prev_itemserv"
                appTitle={capitalize(
                  t("IN18VALIDAPREVISAOITEM/SERVICODEFAULT")
                )}
                appOptions={valida_prev_itemserv_opt}
                appHelpText="Válida previsão Item/Serviço Pessoa Help"
                appOptionLabel="description_type"
                appOptionValue="value_type"
              />

              <AppFieldDropdown
                appFormControl={formControl}
                name="valida_prev_rec"
                appTitle={capitalize(t("IN18VALIDAPREVISAORECURSODEFAULT"))}
                appOptions={valida_prev_rec_opt}
                appHelpText="Válida previsão Recurso Pessoa Help"
                appOptionLabel="description_type"
                appOptionValue="value_type"
              />

              <AppFieldDropdown
                appFormControl={formControl}
                name="valida_regra_config"
                appTitle={capitalize(t("IN18VALIDAREGRACONFIGURAVELDEFAULT"))}
                appOptions={valida_regra_config_opt}
                appHelpText="Válida regra configurável Pessoa Help"
                appOptionLabel="description_type"
                appOptionValue="value_type"
              />

              <AppFieldDropdown
                appFormControl={formControl}
                name="valida_tipo_executor"
                appTitle={capitalize(t("IN18VALIDATIPOEXECUTORDEFAULT"))}
                appOptions={valida_tipo_executor_opt}
                appHelpText="Válida tipo executor Pessoa Help"
                appOptionLabel="description_type"
                appOptionValue="value_type"
              />

              <AppFieldDropdown
                appFormControl={formControl}
                name="valida_rec_equip"
                appTitle={capitalize(t("IN18VALIDARECURSODEFAULT"))}
                appOptions={valida_rec_equip_opt}
                appHelpText="Válida Recurso Pessoa Help"
                appOptionLabel="description_type"
                appOptionValue="value_type"
              />

              <AppFieldDropdown
                appFormControl={formControl}
                name="valida_rec_pessoa"
                appTitle={capitalize(t("IN18OBRIGARECURSODEFAULT"))}
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
                appHelpText="Obriga Item Pessoa Help"
                appOptionLabel="description_type"
                appOptionValue="value_type"
              />

              <AppFieldDropdown
                appFormControl={formControl}
                name="valida_itemserv_s"
                appTitle={capitalize(t("IN18OBRIGASERVICODEFAULT"))}
                appOptions={valida_itemserv_s_opt}
                appHelpText="Obriga Serviço Pessoa Help"
                appOptionLabel="description_type"
                appOptionValue="value_type"
              />

              <AppFieldDropdown
                appFormControl={formControl}
                name="valida_tipo_prop_rec_equip"
                appTitle={capitalize(
                  t("IN18VALIDATIPOPROPRECURSOEQUIPAMENTODEFAULT")
                )}
                appOptions={valida_tipo_prop_rec_equip_opt}
                appHelpText="Valida tipo prop. Recurso - Equipamento Pessoa Help"
                appOptionLabel="description_type"
                appOptionValue="value_type"
              />

              <AppFieldDropdown
                appFormControl={formControl}
                name="valida_tipo_prop_rec_pessoa"
                appTitle={capitalize(
                  t("IN18VALIDATIPOPROPRECURSOPESSOADEFAULT")
                )}
                appOptions={valida_tipo_prop_rec_pessoa_opt}
                appHelpText="Valida tipo prop. Recurso - Pessoa Pessoa Help"
                appOptionLabel="description_type"
                appOptionValue="value_type"
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

export default OpeCentro2OrdTipoForm;
