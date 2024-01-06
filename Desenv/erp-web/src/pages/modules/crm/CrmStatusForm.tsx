import { t } from "i18next";
import { capitalize } from "lodash";
import { TabPanel, TabView } from "primereact/tabview";
import { useLayoutEffect, useRef, useState } from "react";
import AppContainer from "../../../components/toolkit-react/AppContainer";
import AppContainerDivider from "../../../components/toolkit-react/AppContainerDivider";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppContainerTitle from "../../../components/toolkit-react/AppContainerTitle";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDropdown from "../../../components/toolkit-react/AppFieldDropdown";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import CrmStatusService from "../../../services/modules/crm/CrmStatusService";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import GenericFormPage from "../../generics/GenericFormPage";
import CrmClassGrupoDet1Form from "./CrmClassGrupoDet1Form";
import CrmStatusFormDet1 from "./CrmStatusFormDet1";

const crmStatusService = new CrmStatusService();
const sysTypeDescriptionService = new SysTypeDescriptionService();

const CrmStatusForm: React.FC = () => {
  const dataTableDet1Ref = useRef<any>();
  const [detActiveIndex, setDetActiveIndex] = useState(0);
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  const [Tipo_status_opt, setTipo_status_opt] = useState([]);

  // ==============================

  useLayoutEffect(() => {
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "crm_status",
        "tipo_status"
      );
      setTipo_status_opt(res);
    })();
  }, []);
  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "sigla_status",
      required: [true, "Status - Sigla is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "nome",
      required: [true, "Nome is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "tipo_status",
      required: [true, "Nome is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "obrig_motivo",
      required: [true, ""],
      defaultValue: "S",
      type: "checkbox",
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
    { name: "crm_status_prox_childs", ref: dataTableDet1Ref },
  ];
  // ==============================

  return (
    <>
      <GenericFormPage
        appTitleClassIcon="pi pi-star text-red-500"
        appServiceDefault={crmStatusService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18CRMSTATUSDEFAULT"))}
        appRouteList="/private/crm/crmstatus"
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
                name="sigla_status"
                appTitle={capitalize(t("IN18STATUSSIGLADEFAULT"))}
                appHelpText="Status - Sigla Help"
              />

              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldDropdown
                appFormControl={formControl}
                name="tipo_status"
                appTitle={capitalize(t("IN18TIPOSTATUSDEFAULT"))}
                appOptions={Tipo_status_opt}
                appHelpText="Tipo Status Help"
                appOptionLabel="description_type"
                appOptionValue="value_type"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="obrig_motivo"
                appTitle={capitalize(t("IN18OBRIGAMOTIVODEFAULT"))}
                appHelpText="Obriga motivo Help"
                appTrueValue="S"
                appFalseValue="N"
                appTrueValueLabel="Sim"
                appFalseValueLabel="Não"
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
          <AppContainerDivider appPosition="left" appTitle="Dets Form" />
          <div className="md:p-2">
            <TabView
              activeIndex={detActiveIndex}
              onTabChange={(e) => setActiveIndex(e.index)}
              renderActiveOnly={false}
              panelContainerClassName="p-0"
            >
              <TabPanel header="Atendimento-Próximo Status" className="p-0">
                <CrmStatusFormDet1
                  appRef={dataTableDet1Ref}
                  appDataTableDataValue={
                    formControl.getValues().crm_status_prox_childs
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

export default CrmStatusForm;
