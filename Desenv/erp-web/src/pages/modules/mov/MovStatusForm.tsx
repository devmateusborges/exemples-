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
import MovStatusService from "../../../services/modules/mov/MovStatusService";
import MovTipoService from "../../../services/modules/mov/MovTipoService";
import SysProgramService from "../../../services/modules/sys/SysProgramService";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import GenericFormPage from "../../generics/GenericFormPage";

const movStatusService = new MovStatusService();
const movTipoService = new MovTipoService();
const gerNumeracaoService = new GerNumeracaoService();

const sysTypeDescriptionService = new SysTypeDescriptionService();

const MovStatusForm: React.FC = () => {
  // ==============================
  const [Tipo_status_opt, setTipo_status_opt] = useState([]);
  // ==============================

  useLayoutEffect(() => {
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "mov_status",
        "tipo_status"
      );
      setTipo_status_opt(res);
    })();
  }, []);
  const [activeIndex, setActiveIndex] = useState(0);

  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_mov_status",
      required: [true, "Status do Movimento - Sigla is required"],
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
      fieldName: "tipo_status",
      required: [true, "Tipo Status is required"],
      defaultValue: "",
      type: "radio",
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

  return (
    <>
      <GenericFormPage
        appTitleClassIcon="pi pi-star text-red-500"
        appServiceDefault={movStatusService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18MOVSTATUSDOMOVIMENTODEFAULT"))}
        appRouteList="/private/mov/movstatus"
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
                name="sigla_mov_status"
                appTitle={capitalize(t("IN18STATUSDOMOVIMENTOSIGLADEFAULT"))}
                appHelpText="Status do Movimento - Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldDropdown
                appFormControl={formControl}
                name="tipo_status"
                appTitle={capitalize(t("IN18TIPOSTATUSDEFAULT"))}
                appOptions={Tipo_status_opt}
                appHelpText="Tipo do Status Help"
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
              />
            </AppContainerFields>
          </TabPanel>
        </TabView>
      </GenericFormPage>
    </>
  );
};

export default MovStatusForm;
