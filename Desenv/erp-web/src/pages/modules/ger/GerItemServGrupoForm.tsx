import { useRef, useState } from "react";
import { capitalize } from "lodash";
import { t } from "i18next";
import { TabPanel, TabView } from "primereact/tabview";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import GerItemServGrupoService from "../../../services/modules/ger/GerItemServGrupoService";
import GenericFormPage from "../../generics/GenericFormPage";
import GerItemServGrupoDet1Form from "./GerItemServGrupoDet1Form";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppContainer from "../../../components/toolkit-react/AppContainer";
import AppContainerTitle from "../../../components/toolkit-react/AppContainerTitle";
import AppContainerDivider from "../../../components/toolkit-react/AppContainerDivider";

const gerItemServGrupoService = new GerItemServGrupoService();

const GerItemServGrupoForm: React.FC = () => {
  // ==============================

  const [detActiveIndex, setDetActiveIndex] = useState(0);
  const [activeIndex, setActiveIndex] = useState(0);
  const dataTableDet1Ref = useRef<any>();

  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_ger_itemserv_grupo",
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
    { name: "ger_itemserv_subgrupo_childs", ref: dataTableDet1Ref },
  ];

  // ==============================

  return (
    <>
      <GenericFormPage
        appServiceDefault={gerItemServGrupoService}
        appFormControl={formControl}
        appDetailsOptions={detailsOptions}
        appTitle={capitalize(t("IN18GERGRUPODEITEM/SERVICODEFAULT"))}
        appRouteList="/private/ger/geritemservgrupo"
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
                name="sigla_ger_itemserv_grupo"
                appTitle={capitalize(t("IN18GRUPOITEM/SERVICOSIGLADEFAULT"))}
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
              <TabPanel
                header={capitalize(t("IN18SUBGRUPODEFAULT"))}
                className="p-0"
              >
                <GerItemServGrupoDet1Form
                  appRef={dataTableDet1Ref}
                  appDataTableDataValue={
                    formControl.getValues()?.ger_itemserv_subgrupo_childs
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

export default GerItemServGrupoForm;
