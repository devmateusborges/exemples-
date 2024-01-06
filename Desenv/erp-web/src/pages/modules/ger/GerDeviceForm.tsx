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
import GerDeviceService from "../../../services/modules/ger/GerDeviceService";
import GenericFormPage from "../../generics/GenericFormPage";
import GerDeviceDet1Form from "./GerDeviceDet1Form";

const gerDeviceService = new GerDeviceService();
const GerDeviceForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  const [detActiveIndex, setDetActiveIndex] = useState(0);
  const dataTableDet1Ref = useRef<any>();

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
      fieldName: "sigla_device",
      required: [true, "Dispositivo - Sigla  is required"],
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
    { name: "ger_device_param_childs", ref: dataTableDet1Ref },
  ];
  // ==============================

  return (
    <>
      <GenericFormPage
        appServiceDefault={gerDeviceService}
        appFormControl={formControl}
        appDetailsOptions={detailsOptions}
        appTitle={capitalize(t("IN18GERDISPOSITIVODEFAULT"))}
        appRouteList="/private/ger/gerdevice"
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
                name="sigla_device"
                appTitle={capitalize(t("IN18DISPOSITIVOSIGLADEFAULT"))}
                appHelpText="Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Help"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="ativo"
                appTitle={capitalize(t("IN18ATIVODEFAULT"))}
                appHelpText="Help"
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
                header={capitalize(t("IN18PARAMDEFAULT"))}
                className="p-0"
              >
                <GerDeviceDet1Form
                  appRef={dataTableDet1Ref}
                  appDataTableDataValue={
                    formControl.getValues()?.ger_device_param_childs
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

export default GerDeviceForm;
