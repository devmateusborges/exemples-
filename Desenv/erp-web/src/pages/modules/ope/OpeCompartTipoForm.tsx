import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useLayoutEffect, useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldNumber from "../../../components/toolkit-react/AppFieldNumber";
import AppFieldRadioButton from "../../../components/toolkit-react/AppFieldRadioButton";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import OpeCompartMedidaService from "../../../services/modules/ope/OpeCompartMedidaService";
import OpeCompartTipoService from "../../../services/modules/ope/OpeCompartTipoService";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import GenericFormPage from "../../generics/GenericFormPage";

const opeCompartTipoService = new OpeCompartTipoService();
const opeCompartMedidaService = new OpeCompartMedidaService();
const sysTypeDescriptionService = new SysTypeDescriptionService();

const OpeCompartTipoForm: React.FC = () => {
  // ==============================
  const [activeIndex, setActiveIndex] = useState(0);
  const [tipo_compart_opt, setTipo_compart_opt] = useState([]);
  // ==============================
  useLayoutEffect(() => {
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_compart_tipo",
        "tipo_compart"
      );
      setTipo_compart_opt(res);
    })();
  }, []);
  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_compart_tipo",
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
      fieldName: "tipo_compart",
      required: [true, "Tipo Compartimento is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "qnt_lonas",
      required: [true, "Quantidades Lonas is required"],
      maxValue: [18, "Maximum 18 characters for Quantidades Lonas"],
      defaultValue: "",
      type: "numeric",
    },
    {
      fieldName: "qnt_sulco_min",
      required: [true, "Quantidade Sulco MínimoAtivo is required"],
      maxValue: [18, "Maximum 18 characters for Quantidade Sulco MínimoAtivo"],
      defaultValue: "",
      type: "numeric",
    },
    {
      fieldName: "qnt_sulco_max",
      required: [true, "Quantidade Sulco Máximo is required"],
      maxValue: [18, "Maximum 18 characters for Quantidade Sulco Máximo"],
      defaultValue: "",
      type: "numeric",
    },
    {
      fieldName: "ope_compart_medida_id",
      required: [true, "Medida de Compartimento is required"],
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
        appServiceDefault={opeCompartTipoService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18OPETIPODECOMPARTIMENTODEFAULT"))}
        appRouteList="/private/ope/opecomparttipo"
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
                name="sigla_compart_tipo"
                appTitle={capitalize(t("IN18TIPODECOMPARTIMENTOSIGLADEFAULT"))}
                appHelpText="Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="qnt_lonas"
                appHelpText="Quantidades Lonas Help"
                appTitle={capitalize(t("IN18QUANTIDADESLONASDEFAULT"))}
                appMaxFractionDigits={3}
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="qnt_sulco_min"
                appHelpText="Quantidade Sulco MínimoAtivo Help"
                appTitle={capitalize(
                  t("IN18QUANTIDADESULCOMINIMOATIVODEFAULT")
                )}
                appMaxFractionDigits={3}
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="qnt_sulco_max"
                appHelpText="Quantidade Sulco Máximo Help"
                appTitle={capitalize(t("IN18QUANTIDADESULCOMAXIMODEFAULT"))}
                appMaxFractionDigits={3}
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                name="ope_compart_medida_id"
                appTitle={capitalize(
                  t("IN18MEDIDADECOMPARTIMENTOSIGLADEFAULT")
                )}
                appHelpText="Medida de Compartimento Help"
                appOptionLabel="sigla_compart_medida"
                appOptionValue="id"
                appDataKey="id"
                appServiceDefault={opeCompartMedidaService}
                appServiceFilterId="id"
                appServiceFilterDescription="sigla_compart_medida"
              />
              <AppFieldRadioButton
                appFormControl={formControl}
                name="tipo_compart"
                appTitle={capitalize(t("IN18TIPOCOMPARTIMENTODEFAULT"))}
                appOptions={tipo_compart_opt}
                appOptionsLabel="description_type"
                appOptionsValue="value_type"
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

export default OpeCompartTipoForm;
