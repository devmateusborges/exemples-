import { t } from "i18next";
import { TabPanel, TabView } from "primereact/tabview";
import { useState } from "react";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldFile from "../../../components/toolkit-react/AppFieldFile";
import AppFieldNumber from "../../../components/toolkit-react/AppFieldNumber";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import FisDocService from "../../../services/modules/fis/FisDocService";
import FisDocTipoService from "../../../services/modules/fis/FisDocTipoService";
import GerEmpresaService from "../../../services/modules/ger/GerEmpresaService";
import { capitalize } from "../../../utils/FuncUtil";
import GenericFormPage from "../../generics/GenericFormPage";

const fisDocService = new FisDocService();
const fisDocTipoService = new FisDocTipoService();
const gerEmpresaService = new GerEmpresaService();

const FisDocForm: React.FC = () => {
  // ==============================
  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "numero",
      required: [true, capitalize(t("IN18NUMERODEFAULT"))],
      defaultValue: "",
      type: "numeric",
    },
    {
      fieldName: "data_emissao",
      required: [true, capitalize(t("IN18DATAEMISSAODEFAULT"))],
      defaultValue: "",
      type: "date",
    },
    {
      fieldName: "serie",
      required: [true, capitalize(t("IN18NUMEROCONTADEFAULT"))],
      defaultValue: "",
      type: "text",
      maxValue: [3, `Maximum 3 for ${capitalize(t("IN18NUMEROCONTADEFAULT"))}`],
    },
    {
      fieldName: "numero_ini",
      required: [true, capitalize(t("IN18NUMEROINICIALDEFAULT"))],
      defaultValue: "",
      type: "numeric",
      maxValue: [
        10,
        `Maximum 10 for ${capitalize(t("IN18NUMEROINICIALDEFAULT"))}`,
      ],
    },
    {
      fieldName: "numero_fin",
      required: [true, capitalize(t("IN18NUMEROFINALDEFAULT"))],
      defaultValue: "",
      type: "numeric",
      maxValue: [
        10,
        `Maximum 10 for ${capitalize(t("IN18NUMEROFINALDEFAULT"))}`,
      ],
    },
    {
      fieldName: "data_autorizado",
      required: [true, capitalize(t("IN18DATAAUTORIZADODEFAULT"))],
      defaultValue: "",
      type: "date",
    },
    {
      fieldName: "data_cancelado",
      required: [true, capitalize(t("IN18DATACANCELADODEFAULT"))],
      defaultValue: "",
      type: "date",
    },
    {
      fieldName: "data_encerrado",
      required: [true, capitalize(t("IN18DATAENCERRADODEFAULT"))],
      defaultValue: "",
      type: "date",
    },
    {
      fieldName: "ambiente",
      required: [true, capitalize(t("IN18AMBIENTEDEFAULT"))],
      defaultValue: "",
      type: "numeric",
      maxValue: [10, `Maximum 10 for ${capitalize(t("IN18AMBIENTEDEFAULT"))}`],
    },
    {
      fieldName: "tipo_emissao",
      required: [true, capitalize(t("IN18TIPOEMISSAODEFAULT"))],
      defaultValue: "",
      type: "numeric",
      maxValue: [
        10,
        `Maximum 10 for ${capitalize(t("IN18TIPOEMISSAODEFAULT"))}`,
      ],
    },
    {
      fieldName: "status_sefaz",
      required: [true, capitalize(t("IN18CODIGOSEFAZDEFAULT"))],
      defaultValue: "",
      type: "numeric",
      maxValue: [
        10,
        `Maximum 10 for ${capitalize(t("IN18CODIGOSEFAZDEFAULT"))}`,
      ],
    },
    {
      fieldName: "numero_pre",
      required: [true, capitalize(t("IN18NUMEROPREDEFAULT"))],
      defaultValue: "",
      type: "numeric",
      maxValue: [10, `Maximum 10 for ${capitalize(t("IN18NUMEROPREDEFAULT"))}`],
    },
    {
      fieldName: "serie_pre",
      required: [true, capitalize(t("IN18SERIEPREDEFAULT"))],
      defaultValue: "",
      type: "numeric",
      maxValue: [3, `Maximum 3 for ${capitalize(t("IN18SERIEPREDEFAULT"))}`],
    },
    {
      fieldName: "chave",
      required: [true, capitalize(t("IN18CHAVEDEFAULT"))],
      defaultValue: "",
      type: "numeric",
      maxValue: [50, `Maximum 3 for ${capitalize(t("IN18CHAVEDEFAULT"))}`],
    },
    {
      fieldName: "fis_doc_tipo_id",
      required: [true, capitalize(t("IN18DOCUMENTONOMEDEFAULT"))],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "ger_empresa_id",
      required: [true, capitalize(t("IN18EMPRESASIGLADEFAULT"))],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "mov_id",
      required: [true, capitalize(t(""))],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "xml_assinado_childs",
      required: [true, "xml_assinado_childs xxx"],
      defaultValue: [],
    },
    {
      fieldName: "xml_protocolado_childs",
      required: [true, "xml_protocolado_childs xxx"],
      defaultValue: [],
    },
    {
      fieldName: "pdf_emitido_childs",
      required: [true, "pdf_emitido_childs xxx"],
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
        appServiceDefault={fisDocService}
        appFormControl={formControl}
        appTitle={capitalize(t("IN18FISDOCUMENTODEFAULT"))}
        appRouteList="/private/fis/fisdocform"
        appShowTopBar
      >
        <TabView
          activeIndex={activeIndex}
          onTabChange={(e) => setActiveIndex(e.index)}
          panelContainerClassName="p-0 md:p-2 mb-3"
        >
          <TabPanel header="General">
            <AppContainerFields>
              <AppFieldNumber
                appFormControl={formControl}
                name="numero"
                appHelpText={capitalize(t("IN18NUMERODEFAULT"))}
                appTitle={capitalize(t("IN18NUMERODEFAULT"))}
              />
              <AppFieldDate
                appFormControl={formControl}
                name="data_emissao"
                appTitle={capitalize(t("IN18DATAEMISSAODEFAULT"))}
                appHelpText={capitalize(t("IN18DATAEMISSAODEFAULT"))}
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="serie"
                appHelpText={capitalize(t("IN18NUMEROCONTADEFAULT"))}
                appTitle={capitalize(t("IN18NUMEROCONTADEFAULT"))}
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="numero_ini"
                appHelpText={capitalize(t("IN18NUMEROINICIALDEFAULT"))}
                appTitle={capitalize(t("IN18NUMEROINICIALDEFAULT"))}
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="numero_fin"
                appHelpText={capitalize(t("IN18NUMEROFINALDEFAULT"))}
                appTitle={capitalize(t("IN18NUMEROFINALDEFAULT"))}
              />
              <AppFieldDate
                appFormControl={formControl}
                name="data_autorizado"
                appTitle={capitalize(t("IN18DATAAUTORIZADODEFAULT"))}
                appHelpText={capitalize(t("IN18DATAAUTORIZADODEFAULT"))}
              />
              <AppFieldDate
                appFormControl={formControl}
                name="data_cancelado"
                appTitle={capitalize(t("IN18DATACANCELADODEFAULT"))}
                appHelpText={capitalize(t("IN18DATACANCELADODEFAULT"))}
              />
              <AppFieldDate
                appFormControl={formControl}
                name="data_encerrado"
                appTitle={capitalize(t("IN18DATAENCERRADODEFAULT"))}
                appHelpText={capitalize(t("IN18DATAENCERRADODEFAULT"))}
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="ambiente"
                appHelpText={capitalize(t("IN18AMBIENTEDEFAULT"))}
                appTitle={capitalize(t("IN18AMBIENTEDEFAULT"))}
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="tipo_emissao"
                appHelpText={capitalize(t("IN18TIPOEMISSAODEFAULT"))}
                appTitle={capitalize(t("IN18TIPOEMISSAODEFAULT"))}
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="status_sefaz"
                appHelpText={capitalize(t("IN18CODIGOSEFAZDEFAULT"))}
                appTitle={capitalize(t("IN18CODIGOSEFAZDEFAULT"))}
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="numero_pre"
                appHelpText={capitalize(t("IN18NUMEROPREDEFAULT"))}
                appTitle={capitalize(t("IN18NUMEROPREDEFAULT"))}
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="serie_pre"
                appHelpText={capitalize(t("IN18SERIEPREDEFAULT"))}
                appTitle={capitalize(t("IN18SERIEPREDEFAULT"))}
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="chave"
                appHelpText={capitalize(t("IN18CHAVEDEFAULT"))}
                appTitle={capitalize(t("IN18CHAVEDEFAULT"))}
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={fisDocTipoService}
                name="fis_doc_tipo_id"
                appTitle={capitalize(t("IN18DOCUMENTONOMEDEFAULT"))}
                appHelpText={capitalize(t("IN18DOCUMENTONOMEDEFAULT"))}
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="sigla_fis_doc_tipo"
                appOptionLabel="nome"
                appServiceFilterDescription="nome"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                appServiceDefault={gerEmpresaService}
                name="ger_empresa_id"
                appTitle={capitalize(t("IN18EMPRESASIGLADEFAULT"))}
                appHelpText={capitalize(t("IN18EMPRESASIGLADEFAULT"))}
                appDataKey="id"
                appOptionValue="id"
                appServiceFilterId="sigla_empresa"
                appOptionLabel="nome"
                appServiceFilterDescription="nome"
              />
              <AppFieldFile
                className="col-12"
                appMany
                name="xml_assinado_childs"
                appDocumentValueObj={
                  formControl.getValues()["xml_assinado_childs"]
                }
                appFormControl={formControl}
              />
              <AppFieldFile
                className="col-12"
                appMany
                name="xml_protocolado_childs"
                appDocumentValueObj={
                  formControl.getValues()["xml_protocolado_childs"]
                }
                appFormControl={formControl}
              />
              <AppFieldFile
                className="col-12"
                appMany
                name="pdf_emitido_childs"
                appDocumentValueObj={
                  formControl.getValues()["pdf_emitido_childs"]
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

export default FisDocForm;
