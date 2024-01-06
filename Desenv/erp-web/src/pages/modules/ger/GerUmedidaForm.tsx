import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useRef, useState } from "react";
import AppContainer from "../../../components/toolkit-react/AppContainer";
import AppContainerDivider from "../../../components/toolkit-react/AppContainerDivider";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppContainerTitle from "../../../components/toolkit-react/AppContainerTitle";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import GerUmedidaService from "../../../services/modules/ger/GerUmedidaService";
import GenericFormPage from "../../generics/GenericFormPage";
import GerUmedidaDet1Form from "./GerUmedidaDet1Form";

const gerUmedidaService = new GerUmedidaService();

const GerUmedidaForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  const [detActiveIndex, setDetActiveIndex] = useState(0);
  const dataTableDet1Ref = useRef<any>();

  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "nome",
      required: [true, "Nome is required"],
      maxValue: [50, "Maximum 50 characters for Sigla"],
      type: "text",
    },
    {
      fieldName: "sigla_umedida",
      required: [true, "U. Medida - Sigla is required"],
      maxValue: [100, "Maximum 100 characters for Nome"],
      defaultValue: "",
      type: "text",
    },

    {
      fieldName: "ativo",
      required: [true, ""],
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
    { name: "ger_umedida_conv_childs", ref: dataTableDet1Ref },
  ];
  // ==============================

  return (
    <>
      <GenericFormPage
        appServiceDefault={gerUmedidaService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18GERUMEDIDADEFAULT"))}
        appRouteList="/private/ger/gerumedida"
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
                name="sigla_umedida"
                appTitle={capitalize(t("IN18UMEDIDASIGLADEFAULT"))}
                appHelpText="U. Medida - Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
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
                header={capitalize(t("IN18CONVERSAODEFAULT"))}
                className="p-0"
              >
                <GerUmedidaDet1Form
                  appDataTableDataValue={
                    formControl.getValues()?.ger_umedida_conv_childs
                  }
                  appRef={dataTableDet1Ref}
                />
              </TabPanel>
            </TabView>
          </div>
        </AppContainer>
      </GenericFormPage>
    </>
  );
};

export default GerUmedidaForm;
