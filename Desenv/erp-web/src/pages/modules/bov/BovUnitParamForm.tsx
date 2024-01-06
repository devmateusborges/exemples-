import { t } from "i18next";
import { capitalize } from "lodash";
import { useState } from "react";
import { TabPanel, TabView } from "primereact/tabview";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import GenericFormPage from "../../generics/GenericFormPage";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import BovUnitParamService from "../../../services/modules/bov/BovUnitParamService";

const bovUnitParamService = new BovUnitParamService();

const BovUnitParamForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "data_valid_ini",
      required: [true, "Data validade is required"],
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
        appServiceDefault={bovUnitParamService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18BOVPARAMETROSDEFAULT"))}
        appRouteList="/private/bov/bovunitparam"
        appShowTopBar
      >
        <TabView
          activeIndex={activeIndex}
          onTabChange={(e) => setActiveIndex(e.index)}
          panelContainerClassName="p-0 md:p-2 mb-3"
        >
          <TabPanel header="General ">
            <AppContainerFields>
              <AppFieldDate
                appFormControl={formControl}
                name="data_valid_ini"
                appTitle={capitalize(t("IN18DATAVALIDADEDEFAULT"))}
                appHelpText="Data Validade Help"
              />
            </AppContainerFields>
          </TabPanel>
        </TabView>
      </GenericFormPage>
    </>
  );
};

export default BovUnitParamForm;
