import { useState } from "react";
import { capitalize } from "lodash";
import { t } from "i18next";
import { TabPanel, TabView } from "primereact/tabview";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import GenericFormPage from "../../generics/GenericFormPage";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import BorUnitParamService from "../../../services/modules/bor/BorUnitParamService";

const borUnitParamService = new BorUnitParamService();

const BorUnitParamForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "unit_id",
      required: [false, ""],
      defaultValue: "",
      type: "foreignkey",
    },
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
        appServiceDefault={borUnitParamService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18BORPARAMETROSDEFAULT"))}
        appRouteList="/private/bor/borunitparam"
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

export default BorUnitParamForm;
