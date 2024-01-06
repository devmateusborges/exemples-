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
import AppFieldRadioButton from "../../../components/toolkit-react/AppFieldRadioButton";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import GerNumeracaoService from "../../../services/modules/ger/GerNumeracaoService";
import MovOperacaoService from "../../../services/modules/mov/MovOperacaoService";
import MovTipoService from "../../../services/modules/mov/MovTipoService";
import SysProgramService from "../../../services/modules/sys/SysProgramService";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import GenericFormPage from "../../generics/GenericFormPage";
import MovOperacaoFormDet1 from "./MovOperacaoFormDet1";

const movOperacaoService = new MovOperacaoService();
const movTipoService = new MovTipoService();
const gerNumeracaoService = new GerNumeracaoService();

const sysTypeDescriptionService = new SysTypeDescriptionService();

const MovOperacaoForm: React.FC = () => {
  const dataTableDet1Ref = useRef<any>();
  const [detActiveIndex, setDetActiveIndex] = useState(0);
  // ==============================
  const [Tipo_es_opt, setTipo_es_opt] = useState([]);
  const [Finalidade_doc, setFinalidade_doc_opt] = useState([]);
  // ==============================

  useLayoutEffect(() => {
    (async () => {
      let res = await sysTypeDescriptionService.getDescription(
        "mov_operacao",
        "tipo_es"
      );
      setTipo_es_opt(res);
      res = await sysTypeDescriptionService.getDescription(
        "mov_operacao",
        "finalidade_doc"
      );
      setFinalidade_doc_opt(res);
    })();
  }, []);
  const [activeIndex, setActiveIndex] = useState(0);

  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_mov_operacao",
      required: [true, "Operação do Movimento - Sigla is required"],
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
      fieldName: "configuracao",
      required: [true, "Nome is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "finalidade_doc",
      required: [true, "Finalidade Documento is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "tipo_es",
      required: [true, "Tipo Entrada/Saida is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "mov_tipo_id",
      required: [true, "Tipo de Movimento is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "ger_numeracao_id",
      required: [true, "Geral-Numeração is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "ativo",
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
    { name: "mov_operacao_status_childs", ref: dataTableDet1Ref },
  ];
  // ==============================

  return (
    <>
      <GenericFormPage
        appTitleClassIcon="pi pi-star text-red-500"
        appServiceDefault={movOperacaoService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18MOVOPERACAODEMOVIMENTODEFAULT"))}
        appRouteList="/private/mov/movoperacao"
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
                name="sigla_mov_operacao"
                appTitle={capitalize(t("IN18OPERACAODOMOVIMENTOSIGLADEFAULT"))}
                appHelpText="Grupo - Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="configuracao"
                appTitle={capitalize(t("IN18CONFIGURACAODEFAULT"))}
                appHelpText="Configuração Help"
              />
              <AppFieldRadioButton
                appFormControl={formControl}
                name="tipo_es"
                appTitle={capitalize(t("IN18TIPOESDEFAULT"))}
                appOptions={Tipo_es_opt}
                appHelpText="Tipo ES Help"
                appOptionsLabel="description_type"
                appOptionsValue="value_type"
              />
              <AppFieldDropdown
                appFormControl={formControl}
                name="finalidade_doc"
                appTitle={capitalize(t("IN18STATUSDEFAULT"))}
                appOptions={Finalidade_doc}
                appHelpText="Finalidade do Documento Help"
                appOptionLabel="description_type"
                appOptionValue="value_type"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={gerNumeracaoService}
                name="ger_numeracao_id"
                appTitle={capitalize(t("IN18NUMERACAONOMEDEFAULT"))}
                appHelpText="Geral-Numeração Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="sigla_ger_numeracao"
                appServiceFilterDescription="sigla_ger_numeracao"
              />

              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={movTipoService}
                name="mov_tipo_id"
                appTitle={capitalize(t("IN18TIPODOMOVIMENTOSIGLADEFAULT"))}
                appHelpText="Tipo de Movimento Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="sigla_mov_tipo"
                appServiceFilterDescription="sigla_mov_tipo"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="ativo"
                appTitle={capitalize(t("IN18ATIVODEFAULT"))}
                appHelpText="Ativo Help"
                appTrueValue="S"
                appFalseValue="N"
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
              <TabPanel header="Operação x Status do Movimento" className="p-0">
                <MovOperacaoFormDet1
                  appRef={dataTableDet1Ref}
                  appDataTableDataValue={
                    formControl.getValues().mov_operacao_status_childs
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

export default MovOperacaoForm;
