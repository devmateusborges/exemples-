import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import FisUnitParamService from "../../../services/modules/fis/FisUnitParamService";
import GenericFormPage from "../../generics/GenericFormPage";

const fisUnitParamService = new FisUnitParamService();

const FisUnitParamForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "data_valid_ini",
      required: [true, "Data Validade Inicio is required"],
      defaultValue: "",
      type: "date",
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
        appServiceDefault={fisUnitParamService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18FISPARAMETROSDEFAULT"))}
        appRouteList="/private/fis/fisunitparam"
        appShowTopBar
      >
        <TabView
          activeIndex={activeIndex}
          onTabChange={(e) => setActiveIndex(e.index)}
          panelContainerClassName="p-0 md:p-2 mb-3"
        >
          <TabPanel header="General">
            <AppContainerFields>
              <AppFieldDate
                appFormControl={formControl}
                name="data_valid_ini"
                appTitle={capitalize(t("IN18DATAVALIDADEDEFAULT"))}
                appHelpText="Data Validade Inicio Help"
              />
            </AppContainerFields>
          </TabPanel>
        </TabView>
      </GenericFormPage>
    </>
  );
};

export default FisUnitParamForm;
