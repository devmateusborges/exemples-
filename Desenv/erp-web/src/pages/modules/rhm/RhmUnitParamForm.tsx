import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import RhmUnitParamService from "../../../services/modules/rhm/RhmUnitParamService";
import GenericFormPage from "../../generics/GenericFormPage";

const rhmUnitParamService = new RhmUnitParamService();

const RhmUnitParamForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);

  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "data_valid_ini",
      required: [true, "Validar Data Inicio is required"],
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
        appServiceDefault={rhmUnitParamService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18RHMPARAMETROSDEFAULT"))}
        appRouteList="/private/rhm/rhmunitparam"
        appShowTopBar
      >
        <div className="w-full p-2">
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
                  appHelpText="Validar Data Inicio Help"
                />
              </AppContainerFields>
            </TabPanel>
          </TabView>
        </div>
      </GenericFormPage>
    </>
  );
};

export default RhmUnitParamForm;
