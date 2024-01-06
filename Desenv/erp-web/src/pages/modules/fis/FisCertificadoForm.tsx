import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import AppFieldFile from "../../../components/toolkit-react/AppFieldFile";
import AppFieldNumber from "../../../components/toolkit-react/AppFieldNumber";
import AppFieldRadioButton from "../../../components/toolkit-react/AppFieldRadioButton";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import FisCertificadoService from "../../../services/modules/fis/FisCertificadoService";
import GenericFormPage from "../../generics/GenericFormPage";

const fisCertificadoService = new FisCertificadoService();

const FisCertificadoForm: React.FC = () => {
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
      fieldName: "senha",
      required: [true, "Numero do Banco is required"],
      defaultValue: "",
      type: "text",
      maxValue: [50, "Maximum 50 for valor"],
    },
    {
      fieldName: "ativo",
      required: [false, ""],
      defaultValue: "S",
      type: "checkbox",
    },
    {
      fieldName: "sys_document_childs",
      required: [true, "Document is required"],
      defaultValue: [],
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
        appServiceDefault={fisCertificadoService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18FISCERTIFICADODEFAULT"))}
        appRouteList="/private/fis/fiscertificado"
        appShowTopBar
      >
        <TabView
          activeIndex={activeIndex}
          onTabChange={(e) => setActiveIndex(e.index)}
          panelContainerClassName="p-0 md:p-2 mb-3"
        >
          <TabPanel header="General">
            <AppContainerFields>
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="senha"
                appTitle={capitalize(t("IN18SENHADEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="ativo"
                appTitle="Ativo"
                appHelpText="Ativo Help"
                appTrueValue="S"
                appFalseValue="N"
                appTrueValueLabel="Sim"
                appFalseValueLabel="Não"
              />
              <AppFieldFile
                className="col-12"
                appMany
                name="sys_document_childs"
                appDocumentValueObj={
                  formControl.getValues()["sys_document_childs"]
                }
                appFormControl={formControl}
              />
            </AppContainerFields>
          </TabPanel>
        </TabView>
      </GenericFormPage>
    </>
  );
};

export default FisCertificadoForm;
