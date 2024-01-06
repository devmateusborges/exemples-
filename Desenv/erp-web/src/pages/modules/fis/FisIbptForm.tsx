import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldNumber from "../../../components/toolkit-react/AppFieldNumber";
import AppFieldRadioButton from "../../../components/toolkit-react/AppFieldRadioButton";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import FisIbptService from "../../../services/modules/fis/FisIbptService";
import FisNbsService from "../../../services/modules/fis/FisNbsService";
import FisNcmService from "../../../services/modules/fis/FisNcmService";
import GerUfService from "../../../services/modules/ger/GerUfService";
import GenericFormPage from "../../generics/GenericFormPage";

const fisIbptService = new FisIbptService();
const fisNbsService = new FisNbsService();
const fisNcmService = new FisNcmService();
const gerUfService = new GerUfService();

const FisIbptForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "data_validade_ini",
      required: [true, "Data validade inicial is required"],
      defaultValue: "",
      type: "date",
    },
    {
      fieldName: "data_validade_fin",
      required: [true, "Data Validade Final is required"],
      defaultValue: "",
      type: "date",
    },
    {
      fieldName: "perc_nacional",
      required: [true, "Perc nacional is required"],
      defaultValue: "",
      type: "numeric",
      maxValue: [50, "Maximum 50 for valor"],
    },
    {
      fieldName: "perc_importado",
      required: [true, "Perc importado is required"],
      defaultValue: "",
      type: "numeric",
      maxValue: [50, "Maximum 50 for valor"],
    },
    {
      fieldName: "perc_municipal",
      required: [true, "Perc municipal is required"],
      defaultValue: "",
      type: "numeric",
      maxValue: [50, "Maximum 50 for valor"],
    },
    {
      fieldName: "fis_nbs_id",
      required: [true, "Fiscal-Nbs is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "fis_ncm_id",
      required: [true, "Fiscal-Ncm is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "ger_uf_id",
      required: [true, "Geral-Unidade Federação is required"],
      defaultValue: "",
      type: "foreignkey",
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
        appServiceDefault={fisIbptService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18FISIBPTDEFAULT"))}
        appRouteList="/private/fis/fisibpt"
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
                name="data_validade_ini"
                appTitle={capitalize(t("IN18DATAVALIDADEINICIODEFAULT"))}
                appHelpText="Data Validade inicial Help"
              />
              <AppFieldDate
                appFormControl={formControl}
                name="data_validade_fin"
                appTitle={capitalize(t("IN18DATAVALIDADEFINALDEFAULT"))}
                appHelpText="Data Validade final Help"
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="perc_nacional"
                appHelpText="Perc nacional Help"
                appTitle={capitalize(t("IN18PERCNACIONALDEFAULT"))}
                appMinFractionDigits={4}
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="perc_importado"
                appHelpText="Perc importado Help"
                appTitle={capitalize(t("IN18PERCIMPORTADODEFAULT"))}
                appMinFractionDigits={4}
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="perc_municipal"
                appHelpText="Perc municipal Help"
                appTitle={capitalize(t("IN18PERCMUNICIPALDEFAULT"))}
                appMinFractionDigits={4}
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={fisNbsService}
                name="fis_nbs_id"
                appTitle={capitalize(t("IN18NBSNOMEDEFAULT"))}
                appHelpText="Nbs - nome Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="nome"
                appServiceFilterDescription="nome"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={fisNcmService}
                name="fis_ncm_id"
                appTitle={capitalize(t("IN18NCMNOMEDEFAULT"))}
                appHelpText="Ncm - nome Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="nome"
                appServiceFilterDescription="nome"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={gerUfService}
                name="ger_uf_id"
                appTitle={capitalize(t("IN18UFNOMEDEFAULT"))}
                appHelpText="Uf - Sigla Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="sigla_uf"
                appServiceFilterDescription="sigla_uf"
              />
            </AppContainerFields>
          </TabPanel>
        </TabView>
      </GenericFormPage>
    </>
  );
};

export default FisIbptForm;
