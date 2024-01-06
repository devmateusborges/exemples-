import { Divider } from "primereact/divider";
import { TabPanel, TabView } from "primereact/tabview";
import { useLayoutEffect, useRef, useState } from "react";
import { capitalize } from "lodash";
import { t } from "i18next";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";

import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldMask from "../../../components/toolkit-react/AppFieldMask";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import FisCertificadoService from "../../../services/modules/fis/FisCertificadoService";
import GerCidadeService from "../../../services/modules/ger/GerCidadeService";

import GenericFormPage from "../../generics/GenericFormPage";
import AppContainerTitle from "../../../components/toolkit-react/AppContainerTitle";
import AppContainer from "../../../components/toolkit-react/AppContainer";
import AppFieldDropdown from "../../../components/toolkit-react/AppFieldDropdown";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import SysPlanService from "../../../services/modules/sys/SysPlanService";
import SysService from "../../../services/modules/sys/SysService ";
import SysPlanFormDet1 from "./SysPlanFormDet1";

const sysService = new SysService();

const sysPlanService = new SysPlanService();
const sysTypeDescriptionService = new SysTypeDescriptionService();
const SysPlanForm: React.FC = () => {
  // ==============================

  const [detActiveIndex, setDetActiveIndex] = useState(0);
  const [activeIndex, setActiveIndex] = useState(0);
  const dataTableDet1Ref = useRef<any>();
  const [Type_plan_opt, setType_plan_opt] = useState([]);
  const [Indicated_opt, setIndicated_opt] = useState([]);

  // ==============================

  useLayoutEffect(() => {
    (async () => {
      let res = await sysTypeDescriptionService.getDescription(
        "sys_plan",
        "type_plan"
      );
      setType_plan_opt(res);

      res = await sysTypeDescriptionService.getDescription(
        "sys_plan",
        "indicated"
      );
      setIndicated_opt(res);
    })();
  }, []);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "code_plan",
      required: [true, "Plano - Sigla is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 characters for Sigla"],
    },
    {
      fieldName: "name",
      required: [true, "Nome is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 for valor"],
    },
    {
      fieldName: "description",
      required: [true, "Descrição is required"],
      defaultValue: "",
      type: "text",
      maxValue: [250, "Maximum 250 for valor"],
    },
    {
      fieldName: "type_plan",
      required: [true, "Tipo do Plano is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "indicated",
      required: [true, "Indicado is required"],
      defaultValue: "S",
      type: "checkbox",
    },
    {
      fieldName: "sys_id",
      required: [true, "Sistema is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "active",
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
    { name: "sys_plan_restriction_childs", ref: dataTableDet1Ref },
  ];
  // ==============================

  return (
    <>
      <GenericFormPage
        appServiceDefault={sysPlanService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18SYSPLANODEFAULT"))}
        appRouteList="/private/sys/sysplan"
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
                name="code_plan"
                appTitle={capitalize(t("IN18PLANOSIGLADEFAULT"))}
                appHelpText="Plano - Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="name"
                appTitle={capitalize(t("IN18NOMEDEFAULT"))}
                appHelpText="Nome Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="description"
                appTitle={capitalize(t("IN18DESCRICAODEFAULT"))}
                appHelpText="Descrião Help"
              />
              <AppFieldDropdown
                appFormControl={formControl}
                name="type_plan"
                appTitle={capitalize(t("IN18TIPOPLANODEFAULT"))}
                appOptions={Type_plan_opt}
                appHelpText="Tipo Do Plano Help"
                appOptionLabel="description_type"
                appOptionValue="value_type"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={sysService}
                name="sys_id"
                appTitle={capitalize(t("IN18RESTRICAODESISTEMASIGLADEFAULT"))}
                appHelpText="Sistema Help"
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="id"
                appOptionLabel="code_sys"
                appServiceFilterDescription="code_sys"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="indicated"
                appTitle={capitalize(t("IN18INDICADODEFAULT"))}
                appHelpText="Indicado Help"
                appTrueValue="S"
                appFalseValue="N"
                appTrueValueLabel="Sim"
                appFalseValueLabel="Não"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="active"
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
              onTabChange={(e) => setDetActiveIndex(e.index)}
              renderActiveOnly={false}
              panelContainerClassName="p-0"
            >
              <TabPanel
                header="System-Plano de Utilização x Restrição"
                className="p-0"
              >
                <SysPlanFormDet1
                  appRef={dataTableDet1Ref}
                  appDataTableDataValue={
                    formControl.getValues().sys_plan_restriction_childs
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

export default SysPlanForm;
