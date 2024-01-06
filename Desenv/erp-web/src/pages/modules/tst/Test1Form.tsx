import { confirmDialog } from "primereact/confirmdialog";
import { Divider } from "primereact/divider";
import { RadioButton } from "primereact/radiobutton";
import { useEffect, useLayoutEffect, useRef, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { toast } from "react-toastify";

import { TabView, TabPanel } from "primereact/tabview";
import { ScrollPanel } from "primereact/scrollpanel";
import { useMediaQuery } from "react-responsive";
import { InputNumber } from "primereact/inputnumber";
import { InputText } from "primereact/inputtext";
import AppContainer from "../../../components/toolkit-react/AppContainer";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppContainerTitle from "../../../components/toolkit-react/AppContainerTitle";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import AppFieldDropdownFk, {
  IAppFieldDropdownFkOptions,
} from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldMask from "../../../components/toolkit-react/AppFieldMask";
import AppFieldNumber from "../../../components/toolkit-react/AppFieldNumber";
import AppFieldRadioButton from "../../../components/toolkit-react/AppFieldRadioButton";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import AppTopBar from "../../../components/toolkit-react/AppTopBar";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import Test1FkService from "../../../services/modules/tst/Test1FkService";
import Test1Service from "../../../services/modules/tst/Test1Service";
import { useAppSelector } from "../../../store";
import GenericFormDet from "../../generics/GenericFormDet";
import GenericFormPage from "../../generics/GenericFormPage";
import AppLayoutLoading from "../../layout/AppLayoutLoading";
import { ConstUtil } from "../../../utils/ConstUtil";
import Test1Det1Form from "./Test1Det1Form";
import AppFieldFile from "../../../components/toolkit-react/AppFieldFile";
import Test1Det2Form from "./Test1Det2Form";
import AppContainerDivider from "../../../components/toolkit-react/AppContainerDivider";

const test1Service = new Test1Service();
const test1FkService = new Test1FkService();

const Test1Form: React.FC = () => {
  const isTabletOrMobile = useMediaQuery({
    query: ConstUtil.cisTabletOrMobile,
  });
  const dataTableDet1Ref = useRef<any>();
  const dataTableDet2Ref = useRef<any>();
  const [value, setValue1] = useState<any>(0);
  // ==============================
  /* const navigate = useNavigate();
   */
  const urlParams = useParams();
  // ==============================
  const [detActiveIndex, setDetActiveIndex] = useState(0);
  const [activeIndex, setActiveIndex] = useState(0);
  // ==============================

  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "codigo",
      required: [true, "Code is required"],
      defaultValue: "",
      type: "text",
      maxValue: [4, "Maximum 4 characters for code"],
      minValue: [2, "Minimum 2 characters for code"],
    },
    {
      fieldName: "descricao",
      required: [true, "Descricao is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "dt_nascimento",
      required: [true, "Data do nascimento is required"],
      type: "date",
    },

    {
      fieldName: "dthr_nascimento",
      required: [true, "Data e Hora do nascimento is required"],
      defaultValue: "",
      type: "datetime",
    },
    {
      fieldName: "hr_nascimento",
      required: [true, "Hora do nascimento is required"],
      defaultValue: "",
      type: "time",
    },

    {
      fieldName: "quantidade",
      required: [true, "Quantidade is required"],
      defaultValue: "",
      maxValue: [4, "Maximum 4 for quantidade"],
      minValue: [2, "Minimum 2 characters for quantidade"],
      type: "numeric",
    },
    {
      fieldName: "cpfcnpj",
      required: [true, "CPF/CNPJ is required"],
      defaultValue: "",
      type: "mask",
    },
    {
      fieldName: "valor",
      required: [true, "Valor is required"],
      defaultValue: "",
      maxValue: [4, "Maximum 4 for valor"],
      minValue: [2, "Minimum 2 characters for valor"],
      type: "numeric",
    },
    {
      fieldName: "radio",
      required: [true, "Radio is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "ativo",
      required: [false, ""],
      defaultValue: "S",
      type: "checkbox",
    },
    {
      fieldName: "test1_fk_id",
      required: [true, "Test is required"],
      type: "foreignkey",
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

  // Usado para customizar o appOnLoadData
  /*   const handleLoadData = async () => {
    if (urlParams?.id) {
      if (urlParams?.id != "new") {
        const dataForm = await test1Service.findById(urlParams?.id);
        console.log("useEffect>dataForm", dataForm);
        await formControl.handleResetForm();
        await formControl.setValuesForm(dataForm);
      }
    }
  }; */

  // ==============================
  // Usado para customizar o appOnSave
  /*   const handleSave = async () => {
    const valid = await formControl.isValid();
    const formValue = await formControl.getValues();

    formValue.test1_childs = dataTableDet1Ref.current;

    if (valid) {
      const result = await test1Service.save(formValue);
      if (result) {
        toast.success("Save successfully");
      } else {
        formControl.handleResetForm();
      }
    } else {
      for (const f of Object.entries(formControl.getErrors())) {
        toast.error(`${f[1]}`);
      }
    }
  }; */
  // ==============================
  const OptRadio = [
    {
      name: "testexxxxxxxxxx1",
      value: "OPT1",
    },
    {
      name: "testexxxxxxxxxx2",
      value: "OPT2",
    },
    {
      name: "testexxxxxxxxxx3",
      value: "OPT3",
    },
    {
      name: "testexxxxxxxxxx4",
      value: "OPT4",
    },
    {
      name: "testexxxxxxxxxx5",
      value: "OPT5",
    },
    {
      name: "teste6",
      value: "OPT6",
    },
  ];
  // ==============================

  // const handleDropdownTestFktId = async (e: any): Promise<any> => {
  //   const filterAux = {
  //     filter: {
  //       and: {
  //         descricao: { like: e.filter || "%" },
  //       },
  //       or: { id: e.value || "%" },
  //     },
  //   };

  //   const test1FkService = new Test1FkService();
  //   const result = await test1FkService.list({
  //     pfilters: filterAux,
  //     ppage: e.page,
  //     pper_page: dropdownRowsPageTestFkId,
  //   });

  //   setDropdownDataTestFkId(result);
  // };
  // ==============================
  const detailsOptions = [
    { name: "test1_childs", ref: dataTableDet1Ref },
    { name: "test1a_childs", ref: dataTableDet2Ref },
  ];
  // ==============================

  return (
    <>
      <GenericFormPage
        appTitleClassIcon="pi pi-star text-red-500"
        appServiceDefault={test1Service}
        appFormControl={formControl}
        appDetailsOptions={detailsOptions}
        // Ultiliza para customizar loadData e save, se nao passar ele usa o appServiceDefault com metodos padrao para save e load
        // appOnLoadData={handleLoadData}
        /*         appOnQuerySave={handleSave()} */
        /* appOnQuerySave={(a: any) => {
          console.log("Save: ", formControl.getValues());
        }} */
        appTitle="Test 1 Form"
        appRouteList="/private/tst/test1"
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
                name="codigo"
                appTitle="Code"
                appHelpText="Código"
              />
              <AppFieldText
                appFormControl={formControl}
                name="descricao"
                appTitle="Descrição"
                appHelpText="Descrição"
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="valor"
                appHelpText="Valor"
                appTitle="Valor"
                appMinFractionDigits={4}
              />
              <AppFieldDate
                appFormControl={formControl}
                name="dt_nascimento"
                appTitle="Data do nascimento"
                appHelpText="Data do nascimento"
              />
              <AppFieldDate
                appFormControl={formControl}
                name="dthr_nascimento"
                appTitle="Data e Hora do nascimento"
                appHelpText="Data e Hora do nascimento"
                appShowTime
                appShowSeconds
              />
              <AppFieldDate
                appFormControl={formControl}
                name="hr_nascimento"
                appTitle="Hora do nascimento"
                appHelpText="Hora do nascimento"
                appTimeOnly
                appShowSeconds
              />
              <AppFieldMask
                appFormControl={formControl}
                name="cpfcnpj"
                appTitle="CPF/CNPJ"
                appMask="999.999.999-99"
              />
              <AppFieldNumber
                appFormControl={formControl}
                name="quantidade"
                appHelpText="Quantidade"
                appTitle="Quantidade"
                appMinFractionDigits={2}
                appMaxFractionDigits={5}
              />
              <AppFieldRadioButton
                appFormControl={formControl}
                name="radio"
                appTitle="Opts"
                appOptions={OptRadio}
                appOptionsLabel="name"
                appOptionsValue="value"
              />
              <AppFieldCheck
                appFormControl={formControl}
                name="ativo"
                appTitle="Ativo"
                appHelpText="Ativo"
                appTrueValue="S"
                appFalseValue="N"
                appTrueValueLabel="Sim"
                appFalseValueLabel="Não"
                // appCode="teste"
                // appDescription="teste22"
              />
              <Divider />
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
          <TabPanel header="teste icon divider">
            <AppContainerFields>
              <AppFieldDropdownFk
                appFormControl={formControl}
                // appValue={formControl.getValues().test1_fk_id}
                name="test1_fk_id"
                appTitle="Test"
                appHelpText="yyyy"
                appOptionLabel="descricao"
                appOptionValue="id"
                appDataKey="id"
                appServiceDefault={test1FkService}
                appServiceFilterId="id"
                appServiceFilterDescription="descricao"
                // appRowsPage={dropdownRowsPageTestFkId}
                // Utiliza para customizar pois pode ser simples usando appServiceDefault, appServiceFilterId,appServiceFilterDescription
                // appOptions={dropdownDataTestFkId}
                // appOnFilterAction={(e: any) => {
                //  return handleDropdownTestFktId(e);
                // }}
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
              <TabPanel header="Det 1" className="p-0">
                <Test1Det1Form
                  appRef={dataTableDet1Ref}
                  appDataTableDataValue={formControl.getValues()?.test1_childs}
                />
              </TabPanel>
              <TabPanel header="Det 2" className="p-0">
                <Test1Det2Form
                  appRef={dataTableDet2Ref}
                  appDataTableDataValue={formControl.getValues()?.test1a_childs}
                />
              </TabPanel>
            </TabView>
          </div>
        </AppContainer>
      </GenericFormPage>
    </>
  );
};
// ==============================
export default Test1Form;
