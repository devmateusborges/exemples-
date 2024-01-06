import { TabPanel, TabView } from "primereact/tabview";
import { useLayoutEffect, useRef, useState } from "react";
import AppContainer from "../../../components/toolkit-react/AppContainer";
import AppContainerDivider from "../../../components/toolkit-react/AppContainerDivider";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppContainerTitle from "../../../components/toolkit-react/AppContainerTitle";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDropdown from "../../../components/toolkit-react/AppFieldDropdown";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldNumber from "../../../components/toolkit-react/AppFieldNumber";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import CtbCompService from "../../../services/modules/ctb/CtbCompService";
import FisCestService from "../../../services/modules/fis/FisCestService";
import FisNbsService from "../../../services/modules/fis/FisNbsService";
import FisNcmService from "../../../services/modules/fis/FisNcmService";
import GerItemservService from "../../../services/modules/ger/GerItemservService";
import GerItemservSubGrupoService from "../../../services/modules/ger/GerItemservSubGrupoService";
import GerUmedidaService from "../../../services/modules/ger/GerUmedidaService";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import GenericFormPage from "../../generics/GenericFormPage";
import GerItemservDet1Form from "./GerItemservDet1Form";
import GerItemservDet2Form from "./GerItemservDet2Form";
import GerItemservDet3Form from "./GerItemservDet3Form";
import GerItemservDet4Form from "./GerItemservDet4Form";

const gerItemservService = new GerItemservService();
const fisNcmService = new FisNcmService();
const gerUmedidaService = new GerUmedidaService();
const fisCestService = new FisCestService();
const fisNbsService = new FisNbsService();
const ctbCompService = new CtbCompService();
const gerItemservSubGrupoService = new GerItemservSubGrupoService();
/* TODO-GER ainda nao tem service */
/* ger_itemserv_subgrupo_id; */

const sysTypeDescriptionService = new SysTypeDescriptionService();

const GerItemservForm: React.FC = () => {
  // ==============================

  const [activeIndex, setActiveIndex] = useState(0);
  const [detActiveIndex, setDetActiveIndex] = useState(0);
  const dataTableDet1Ref = useRef<any>();
  const dataTableDet2Ref = useRef<any>();
  const dataTableDet3Ref = useRef<any>();
  const dataTableDet4Ref = useRef<any>();
  const [tipo_opt, setTipo_opt] = useState([]);
  const [tipo_ctb_comp_opt, setTipo_ctb_comp_opt] = useState([]);
  const [tipo_composicao_opt, setTipo_composicao_opt] = useState([]);
  // ==============================
  useLayoutEffect(() => {
    (async () => {
      let res = await sysTypeDescriptionService.getDescription(
        "ger_itemserv",
        "tipo"
      );
      setTipo_opt(res);
      res = await sysTypeDescriptionService.getDescription(
        "ger_itemserv",
        "tipo_ctb_comp"
      );
      setTipo_ctb_comp_opt(res);
      res = await sysTypeDescriptionService.getDescription(
        "ger_itemserv",
        "tipo_composicao"
      );
      setTipo_composicao_opt(res);
    })();
  }, []);
  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "nome",
      required: [true, "Nome is required"],
      maxValue: [100, "Maximum 100 characters for Nome"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "ativo",
      required: [true, ""],
      defaultValue: "S",
      type: "checkbox",
    },
    {
      fieldName: "referencia1",
      required: [true, "Referência 1 is required"],
      maxValue: [50, "Maximum 50 characters for Referência 1"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "referencia2",
      required: [true, "Referência 2 is required"],
      maxValue: [50, "Maximum 50 characters for Referência 2"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "referencia3",
      required: [true, "Referência 3 is required"],
      maxValue: [50, "Maximum 50 characters for Referência 3"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "tipo",
      required: [true, "Tipo is required"],
      defaultValue: "",
      type: "checkbox",
    },
    {
      fieldName: "tipo_ctb_comp",
      required: [true, "Tipo Componente is required"],
      defaultValue: "",
      type: "checkbox",
    },
    {
      fieldName: "origem_fiscal",
      required: [true, "Origem Fiscal is required"],
      maxValue: [9, "Maximum 9 characters for Origem Fiscal"],
      defaultValue: "",
      type: "numeric",
    },
    {
      fieldName: "fis_doc_cnae_nfs",
      required: [true, "Documento CNAE da NFS is required"],
      maxValue: [50, "Maximum 50 characters for Documento Cnae da NFS"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "fis_sigla_servico_municipio",
      required: [true, "Município Serviço - Sigla is required"],
      maxValue: [50, "Maximum 50 characters for Município Serviço - Sigla"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "sigla_itemserv",
      required: [true, "Sigla is required"],
      maxValue: [15, "Maximum 15 characters for Sigla"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "nome_alternativo",
      required: [true, "Nome Alternativo is required"],
      maxValue: [100, "Maximum 100 characters for Nome Alternativo"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "tipo_composicao",
      required: [true, "Tipo Composição is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "fis_sigla_servico",
      required: [true, "Serviço - Sigla is required"],
      maxValue: [50, "Maximum 50 characters for Serviço - Sigla"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "ger_itemserv_subgrupo_id",
      required: [false, "GER-Subgrupo de Item/Serviço is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "fis_ncm_id",
      required: [true, "FIS-Ncm is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "ger_umedida_id",
      required: [true, "GER-U.Medida is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "fis_cest_id",
      required: [true, "FIS-Cest is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "fis_nbs_id",
      required: [true, "FIS-Listagem NBS is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "ctb_comp_id",
      required: [true, "CTB-Componente is required"],
      defaultValue: "",
      type: "foreignkey",
    },
  ];
  // ==============================

  const formControl = useFormControl({
    fieldControls,
  });
  // ==============================

  const detailsOptions = [
    { name: "ger_itemserv_barra_childs", ref: dataTableDet1Ref },
    { name: "ger_itemserv_local_childs", ref: dataTableDet2Ref },
    { name: "ger_itemserv_lote_childs", ref: dataTableDet3Ref },
    { name: "ger_itemserv_pessoa_childs", ref: dataTableDet4Ref },
  ];
  // ==============================

  return (
    <>
      <GenericFormPage
        appServiceDefault={gerItemservService}
        appDetailsOptions={detailsOptions}
        appFormControl={formControl}
        appTitle="GER-Item/Serviço Form"
        appRouteList="/private/ger/geritemserv"
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
                name="sigla_itemserv"
                appTitle="Sigla"
                appHelpText="Sigla Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="fis_sigla_servico_municipio"
                appTitle="Município Serviço - Sigla"
                appHelpText="Município Serviço Help - Sigla"
              />
              <AppFieldText
                appFormControl={formControl}
                name="fis_sigla_servico"
                appTitle="Serviço - Sigla"
                appHelpText="Serviço Help - Sigla"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome"
                appTitle="Nome"
                appHelpText="Nome Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="nome_alternativo"
                appTitle="Nome Alternativo"
                appHelpText="Nome Alternativo Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="referencia1"
                appTitle="Referência 1"
                appHelpText="Referência 1 Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="referencia2"
                appTitle="Referência 2"
                appHelpText="Referência 2 Help"
              />
              <AppFieldText
                appFormControl={formControl}
                name="referencia3"
                appTitle="Referência 3"
                appHelpText="Referência 3 Help"
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="origem_fiscal"
                appTitle="Origem Fiscal"
                appHelpText="Origem Fiscal Help"
                appMinFractionDigits={0}
              />
              <AppFieldText
                appFormControl={formControl}
                name="fis_doc_cnae_nfs"
                appTitle="Documento CNAE da NFS"
                appHelpText="Documento CNAE da NFS Help"
              />

              <AppFieldDropdownFk
                appServiceDefault={gerItemservSubGrupoService}
                appFormControl={formControl}
                name="ger_itemserv_subgrupo_id"
                appTitle="GER-Subgrupo de Item/Serviço"
                appHelpText="GER-Subgrupo de Item/Serviço Help"
                appServiceFilterDescription="sigla_ger_itemserv_subgrupo"
                appOptionLabel="sigla_ger_itemserv_subgrupo"
                appOptionValue="id"
                appDataKey="id"
                appServiceFilterId="id"
              />
              <AppFieldDropdownFk
                appServiceDefault={fisNcmService}
                appFormControl={formControl}
                name="fis_ncm_id"
                appTitle="FIS-Ncm"
                appHelpText="FIS-Ncm Help"
                appServiceFilterDescription="nome"
                appOptionLabel="nome"
                appOptionValue="id"
                appDataKey="id"
                appServiceFilterId="id"
              />
              <AppFieldDropdownFk
                appServiceDefault={gerUmedidaService}
                appFormControl={formControl}
                name="ger_umedida_id"
                appTitle="GER-U.Medida"
                appHelpText="GER-U.Medida Help"
                appServiceFilterDescription="nome"
                appOptionLabel="nome"
                appOptionValue="id"
                appDataKey="id"
                appServiceFilterId="id"
              />
              <AppFieldDropdownFk
                appServiceDefault={fisCestService}
                appFormControl={formControl}
                name="fis_cest_id"
                appTitle="FIS-Cest"
                appHelpText="FIS-Cest Help"
                appServiceFilterDescription="nome"
                appOptionLabel="nome"
                appOptionValue="id"
                appDataKey="id"
                appServiceFilterId="id"
              />
              <AppFieldDropdownFk
                appServiceDefault={fisNbsService}
                appFormControl={formControl}
                name="fis_nbs_id"
                appTitle="FIS-Listagem NBS"
                appHelpText="FIS-Listagem NBS Help"
                appServiceFilterDescription="nome"
                appOptionLabel="nome"
                appOptionValue="id"
                appDataKey="id"
                appServiceFilterId="id"
              />
              <AppFieldDropdownFk
                appServiceDefault={ctbCompService}
                appFormControl={formControl}
                name="ctb_comp_id"
                appTitle="CTB-Componente"
                appHelpText="CTB-Componente Help"
                appServiceFilterDescription="nome"
                appOptionLabel="nome"
                appOptionValue="id"
                appDataKey="id"
                appServiceFilterId="id"
              />
              <AppFieldDropdown
                appFormControl={formControl}
                name="tipo"
                appTitle="Tipo"
                appOptions={tipo_opt}
                appHelpText="Tipo Help"
                appOptionLabel="description_type"
                appOptionValue="value_type"
              />
              <AppFieldDropdown
                appFormControl={formControl}
                name="tipo_ctb_comp"
                appTitle="Tipo Componente"
                appOptions={tipo_ctb_comp_opt}
                appHelpText="Tipo Help"
                appOptionLabel="description_type"
                appOptionValue="value_type"
              />
              <AppFieldDropdown
                appFormControl={formControl}
                name="tipo_composicao"
                appTitle="Tipo Composição"
                appOptions={tipo_composicao_opt}
                appHelpText="Tipo Composição Help"
                appOptionLabel="description_type"
                appOptionValue="value_type"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="ativo"
                appTitle="Ativo"
                appHelpText="Ativo Help"
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
              <TabPanel header="Código de barra" className="p-0">
                <GerItemservDet1Form
                  appRef={dataTableDet1Ref}
                  appDataTableDataValue={
                    formControl.getValues()?.ger_itemserv_barra_childs
                  }
                />
              </TabPanel>

              <TabPanel header="Local" className="p-0">
                <GerItemservDet2Form
                  appRef={dataTableDet2Ref}
                  appDataTableDataValue={
                    formControl.getValues()?.ger_itemserv_local_childs
                  }
                />
              </TabPanel>

              <TabPanel header="Lote" className="p-0">
                <GerItemservDet3Form
                  appRef={dataTableDet3Ref}
                  appDataTableDataValue={
                    formControl.getValues()?.ger_itemserv_lote_childs
                  }
                />
              </TabPanel>

              <TabPanel header="Pessoa" className="p-0">
                <GerItemservDet4Form
                  appRef={dataTableDet4Ref}
                  appDataTableDataValue={
                    formControl.getValues()?.ger_itemserv_pessoa_childs
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

export default GerItemservForm;
