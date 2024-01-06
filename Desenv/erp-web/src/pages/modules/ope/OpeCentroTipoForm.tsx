import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useLayoutEffect, useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldRadioButton from "../../../components/toolkit-react/AppFieldRadioButton";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import OpeCentroTipoService from "../../../services/modules/ope/OpeCentroTipoService";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import GenericFormPage from "../../generics/GenericFormPage";

const opeCentroTipoService = new OpeCentroTipoService();
const sysTypeDescriptionService = new SysTypeDescriptionService();

const OpeCentroTipoForm: React.FC = () => {
  // ==============================
  const [tipo_es_opt, setTipo_es_opt] = useState([]);
  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================
  useLayoutEffect(() => {
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ope_centro_tipo",
        "tipo_es"
      );
      setTipo_es_opt(res);
    })();
  }, []);
  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "nome",
      required: [true, "Nome is required"],
      maxValue: [100, "Maximum 100 characters for Nome"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "tipo_es",
      required: [true, "Tipo ES is required"],
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
        appServiceDefault={opeCentroTipoService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18OPETIPODECENTRODEFAULT"))}
        appRouteList="/private/ope/opecentrotipo"
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

              <AppFieldRadioButton
                appFormControl={formControl}
                name="tipo_es"
                appTitle={capitalize(t("IN18TIPOESDEFAULT"))}
                appOptions={tipo_es_opt}
                appOptionsLabel="description_type"
                appOptionsValue="value_type"
              />
            </AppContainerFields>
          </TabPanel>
        </TabView>
      </GenericFormPage>
    </>
  );
};

export default OpeCentroTipoForm;
