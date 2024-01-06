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
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import FisCestService from "../../../services/modules/fis/FisCestService";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import GenericFormPage from "../../generics/GenericFormPage";
import FisCestFormDet1 from "./FisCestFormDet1";

const fisCestService = new FisCestService();

const FisCestForm: React.FC = () => {
  const dataTableDet1Ref = useRef<any>();
  const [detActiveIndex, setDetActiveIndex] = useState(0);
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);

  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "nome",
      required: [true, "Nome is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "nr_cest",
      required: [true, "Numero Cest is required"],
      defaultValue: "",
      type: "text",
      maxValue: [50, "Maximum 50 for valor"],
    },
    {
      fieldName: "data_validade",
      required: [true, "Data validade is required"],
      defaultValue: "",
      type: "date",
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
    { name: "fis_cest_ncm_childs", ref: dataTableDet1Ref },
  ];
  // ==============================

  return (
    <>
      <GenericFormPage
        appTitleClassIcon="pi pi-star text-red-500"
        appServiceDefault={fisCestService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18FISCESTDEFAULT"))}
        appRouteList="/private/fis/fiscest"
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
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nr_cest"
                appTitle={capitalize(t("IN18NUMEROCESTDEFAULT"))}
                appHelpText="Numero Cest Help"
              />
              <AppFieldDate
                appFormControl={formControl}
                name="data_validade"
                appTitle={capitalize(t("IN18DATAVALIDADEDEFAULT"))}
                appHelpText="Data de Validade"
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
        <AppContainer className="w-full mt-2">
          <AppContainerTitle appTitle="Dets Form" appSmall />
          <div className="md:p-2">
            <TabView
              activeIndex={detActiveIndex}
              onTabChange={(e) => setActiveIndex(e.index)}
              renderActiveOnly={false}
              panelContainerClassName="p-0"
            >
              <TabPanel
                header={capitalize(t("IN18FISCALCESTXNCMDEFAULT"))}
                className="p-0"
              >
                <FisCestFormDet1
                  appRef={dataTableDet1Ref}
                  appDataTableDataValue={
                    formControl.getValues().fis_cest_ncm_childs
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

export default FisCestForm;
