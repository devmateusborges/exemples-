import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useLayoutEffect, useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldRadioButton from "../../../components/toolkit-react/AppFieldRadioButton";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import BorDispositivoService from "../../../services/modules/bor/BorDispositivoService";
import OpeCentro2EquipService from "../../../services/modules/ope/OpeCentro2EquipService";
import OpeCentro2PessoaService from "../../../services/modules/ope/OpeCentro2PessoaService";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import GenericFormPage from "../../generics/GenericFormPage";

const borDispositivoService = new BorDispositivoService();
const opeCentro2EquipService = new OpeCentro2EquipService();
const opeCentro2PessoaService = new OpeCentro2PessoaService();
const sysTypeDescriptionService = new SysTypeDescriptionService();

const BorDispositivoForm: React.FC = () => {
  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================
  const [tipo_opt, setTipo_opt] = useState([]);
  // ==============================

  useLayoutEffect(() => {
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "bor_dispositivo",
        "tipo"
      );
      setTipo_opt(res);
    })();
  }, []);
  const fieldControls: Array<IFieldControl> = [
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
      fieldName: "tipo",
      required: [true, "Tipo Dispositivo is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "numero_serie",
      required: [true, "Número de Série is required"],
      defaultValue: "",
      type: "text",
      maxValue: [50, "Maximum 50 for valor"],
    },
    {
      fieldName: "ope_centro2_equip_id",
      required: [false, ""],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "ope_centro2_pessoa_id",
      required: [false, ""],
      defaultValue: "",
      type: "foreignkey",
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
        appServiceDefault={borDispositivoService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18BORDISPOSITIVODEFAULT"))}
        appRouteList="/private/bor/bordispositivo"
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
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="numero_serie"
                appHelpText="Número de Série help"
                appTitle={capitalize(t("IN18NUMERODESERIEDEFAULT"))}
              />
              <AppFieldRadioButton
                appFormControl={formControl}
                name="tipo"
                appTitle={capitalize(t("IN18TIPODEFAULT"))}
                appOptions={tipo_opt}
                appOptionsLabel="description_type"
                appOptionsValue="value_type"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={opeCentro2EquipService}
                name="ope_centro2_equip_id"
                appTitle={capitalize(
                  t(
                    "IN18OPERACAODADOSDEEQUIPAMENTODOCENTRONIVEL2DEENTRADA/SAIDAPLACADEFAULT"
                  )
                )}
                appHelpText="Operação-Dados de Equipamento do Centro Nível 2 de Entrada/Saída Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="placa"
                appServiceFilterDescription="placa"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={opeCentro2PessoaService}
                name="ope_centro2_pessoa_id"
                appTitle={capitalize(
                  t(
                    "IN18OPERACAODADOSDEPESSOADOCENTRONIVEL2DEENTRADA/SAIDATIPODEIDENTIFICACAODOPONTODEFAULT"
                  )
                )}
                appHelpText="Operação-Dados de Pessoa do Centro Nível 2 de Entrada/Saída Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="pto_idenf_tipo"
                appServiceFilterDescription="pto_idenf_tipo"
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

export default BorDispositivoForm;
