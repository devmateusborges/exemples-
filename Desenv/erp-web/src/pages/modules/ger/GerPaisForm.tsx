import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useEffect, useLayoutEffect, useRef, useState } from "react";
import AppContainer from "../../../components/toolkit-react/AppContainer";
import AppContainerDivider from "../../../components/toolkit-react/AppContainerDivider";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppContainerTitle from "../../../components/toolkit-react/AppContainerTitle";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import GerPaisService from "../../../services/modules/ger/GerPaisService";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";
import GenericFormPage from "../../generics/GenericFormPage";
import GerPaisDet1Form from "./GerPaisDet1Form";

const gerPaisService = new GerPaisService();

const GerPaisForm: React.FC = () => {
  // ==============================
  const [activeIndex, setActiveIndex] = useState(0);
  const dataTableDet1Ref = useRef<any>();
  const [detActiveIndex, setDetActiveIndex] = useState(0);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_pais",
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
      fieldName: "nr_pais",
      required: [true, "Número País is required"],
      maxValue: [50, "Maximum 50 characters for Número País"],
      defaultValue: "",
      type: "text",
    },
  ];
  // ==============================
  const formControl = useFormControl({
    fieldControls,
  });

  // ==============================
  const detailsOptions = [{ name: "ger_uf_childs", ref: dataTableDet1Ref }];
  // ==============================
  return (
    <>
      <GenericFormPage
        appServiceDefault={gerPaisService}
        appFormControl={formControl}
        appDetailsOptions={detailsOptions}
        appTitle={capitalize(t("IN18GERPAISDEFAULT"))}
        appRouteList="/private/ger/gerpais"
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
                name="sigla_pais"
                appTitle={capitalize(t("IN18PAISSIGLADEFAULT"))}
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
                name="nr_pais"
                appTitle={capitalize(t("IN18NUMEROPAISDEFAULT"))}
                appHelpText="Número País Help"
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
                header={capitalize(t("IN18UNIDADEDAFEDERACAODEFAULT"))}
                className="p-0"
              >
                <GerPaisDet1Form
                  appRef={dataTableDet1Ref}
                  appDataTableDataValue={formControl.getValues()?.ger_uf_childs}
                />
              </TabPanel>
            </TabView>
          </div>
        </AppContainer>
      </GenericFormPage>
    </>
  );
};

export default GerPaisForm;
