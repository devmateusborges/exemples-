import { t } from "i18next";
import { capitalize } from "lodash";
import { Divider } from "primereact/divider";
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
import GerMarcaService from "../../../services/modules/ger/GerMarcaService";
import GenericFormPage from "../../generics/GenericFormPage";
import GerMarcaDet1Form from "./GerMarcaDet1Form";
import GerMarcaDet2Form from "./GerMarcaDet2Form";

const gerMarcaService = new GerMarcaService();

const GerMarcaForm: React.FC = () => {
  // ==============================

  const dataTableDet1Ref = useRef<any>();
  const dataTableDet2Ref = useRef<any>();
  const [activeIndex, setActiveIndex] = useState(0);
  const [detActiveIndex, setDetActiveIndex] = useState(0);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_ger_marca",
      required: [true, "Sigla"],
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
  ];
  // ==============================

  const formControl = useFormControl({
    fieldControls,
  });
  // ==============================
  const detailsOptions = [
    { name: "ger_marca_modelo_childs", ref: dataTableDet1Ref },
    { name: "ger_marca_pessoa_childs", ref: dataTableDet2Ref },
  ];
  // ==============================
  return (
    <>
      <GenericFormPage
        appServiceDefault={gerMarcaService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18GERMARCADEFAULT"))}
        appRouteList="/private/ger/germarca"
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
                name="sigla_ger_marca"
                appTitle={capitalize(t("IN18MARCASIGLADEFAULT"))}
                appHelpText="Sigla Help"
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
              <TabPanel header="Modelo" className="p-0">
                <GerMarcaDet1Form
                  appRef={dataTableDet1Ref}
                  appDataTableDataValue={
                    formControl.getValues()?.ger_marca_modelo_childs
                  }
                />
              </TabPanel>
              <TabPanel header="Pessoa" className="p-0">
                <GerMarcaDet2Form
                  appRef={dataTableDet2Ref}
                  appDataTableDataValue={
                    formControl.getValues()?.ger_marca_pessoa_childs
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

export default GerMarcaForm;
