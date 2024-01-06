import { confirmDialog } from "primereact/confirmdialog";
import { TabPanel, TabView } from "primereact/tabview";
import { useEffect, useRef, useState } from "react";
import { toast } from "react-toastify";
import { capitalize } from "lodash";
import { t } from "i18next";
import { Button } from "primereact/button";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppContainerTitle from "../../../components/toolkit-react/AppContainerTitle";
import AppFieldDate from "../../../components/toolkit-react/AppFieldDate";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import AppTopBar from "../../../components/toolkit-react/AppTopBar";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import GerEmpresaService from "../../../services/modules/ger/GerEmpresaService";
import GerTipoPeriodoService from "../../../services/modules/ger/GerTipoPeriodoService";
import { formatDateColumn } from "../../../utils/FuncUtil";
import GerPerService from "../../../services/modules/ger/GerPerService";
import store from "../../../store";
import GenericListPage from "../../generics/GenericListPage";
import AppDataTable, {
  IAppDataTableColumns,
} from "../../../components/toolkit-react/AppDataTable";
import SysProcessLogService from "../../../services/modules/sys/SysProcessLogService";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";

const gerTipoPeriodoService = new GerTipoPeriodoService();
const gerEmpresaService = new GerEmpresaService();
const gerPerService = new GerPerService();
const sysProcessLogService = new SysProcessLogService();
const GerPerGerarForm: React.FC = () => {
  // ==============================
  const [activeIndex, setActiveIndex] = useState(0);
  const dataTableRef = useRef();
  const [dataValue, setDataValue] = useState([]);
  const [dateIniProcessIni, setDateIniProcessIni] = useState<string>();
  const [dateIniProcessFin, setDateIniProcessFin] = useState<string>();
  const [error, setError] = useState<string>("N");
  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "pgerpertipo",
      required: [true, "Tipo periodo is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "pgerempresaid",
      required: [true, "Empresa is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "pano",
      required: [true, "Ano is required"],
      defaultValue: "",
      type: "date",
    },
    {
      fieldName: "pcodeprocess",
      required: [true, "Código do processo is required"],
      defaultValue: "",
      type: "text",
    },
  ];

  // ==============================
  const formControl = useFormControl({
    fieldControls,
  });
  // ==============================

  const handleValidate = async () => {
    const isValid = await formControl.isValid();

    if (isValid) {
      const data = formControl.getValues();
      return data;
    }

    const errors = formControl.getErrors();
    for (const f of Object.entries(errors)) {
      toast.error(`${f[1]}`);
    }
    return false;
  };
  // ==============================
  const messageTemplate = (data: any, message: string) => {
    return (
      <>
        <span>{message}</span>
        <br />
        <div>
          <br />
          Tipo periodo: [
          <span className="text-600">{data.pgerpertipo_obj.nome}</span>]
          <br />
          Empresa: [
          <span className="text-600">{data.pgerempresaid_obj.nome}</span>]
          <br />
          Ano: [
          <span className="text-600">
            {formatDateColumn(new Date(data.pano), {
              year: "numeric",
            })}
          </span>
          ]
          <br />
          Código do processo: [
          <span className="text-600">{data.pcodeprocess}</span>]
          <br />
        </div>
      </>
    );
  };
  // ==============================

  const handleFilterLogAux = async () => {
    const filter = {
      pfilters: {
        filter: {
          and: {
            date_ini_process: {
              gte: dateIniProcessIni,
              and: { date_ini_process: { lte: dateIniProcessFin } },
            },
            error,
          },
        },
        sort: { date_ini_process: "desc" },
      },
    };
    return filter;
  };
  // ==============================

  const handleProcess = async () => {
    const data = await handleValidate();

    if (data) {
      confirmDialog({
        message: messageTemplate(data, "Do you want to process ?"),
        header: "Confirmation",
        icon: "pi pi-question-circle",
        className: "text-lg",
        accept: async () => {
          data["psysuserid"] = store.getState().auth.auth.user.id;
          /* data["pgerpertipo"] = "x"; */
          const res = await gerPerService.generatePer(data);

          const filter: any = await handleFilterLogAux();

          if (res.data.code == 200) {
            toast.success("Processed");
            filter.pfilters.filter.and["error"] = "N";
          } else {
            toast.success("Process failure");
            filter.pfilters.filter.and["error"] = "S";
          }
          const logs = await sysProcessLogService.list(filter);

          setDataValue(logs.items);
          setActiveIndex(1);
        },
      });
    }
  };

  // ==============================
  const handleFilterLog = async () => {
    const filter: any = await handleFilterLogAux();

    const logs = await sysProcessLogService.list(filter);

    setDataValue(logs.items);
  };
  // ==============================
  const dataTableColumns: IAppDataTableColumns = {
    columns: [
      {
        appField: "id",
        appHeader: "ID",
        appSortable: true,
        appFilter: false,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: true,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "type_process",
        appHeader: "Tipo do Processo",
        appSortable: true,
        appFilter: false,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "code_process",
        appHeader: "Código do processo",
        appSortable: true,
        appFilter: false,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "sys_user_id_obj.name",
        appHeader: "Usuário",
        appSortable: true,
        appFilter: false,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appDataType: "text",
        appExport: true,
      },

      {
        appField: "date_ini_process",
        appHeader: "Data Inicial do Processo",
        appSortable: true,
        appFilter: false,
        appFilterMatch: "contains",
        appFilterGlobal: false,
        appDataType: "date",
        appExport: true,
      },
      {
        appField: "date_fin_process",
        appHeader: "Data Final do Processo",
        appSortable: true,
        appFilter: false,
        appFilterMatch: "contains",
        appFilterGlobal: false,
        appDataType: "date",
        appExport: true,
      },

      {
        appField: "param_process",
        appHeader: "Parametros do Processo",
        appSortable: true,
        appFilter: false,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "error",
        appHeader: "Erro",
        appSortable: true,
        appFilter: false,
        appFilterMatch: "contains",
        appFilterGlobal: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "message_process",
        appHeader: "Mensagem",
        appSortable: true,
        appFilter: false,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appDataType: "text",
        appExport: true,
      },

      {
        appField: "log_user_ins",
        appHeader: capitalize(t("IN18USUARIODEINSERCAODEFAULT")),
        appSortable: true,
        appFilter: false,
        appFilterMatch: "contains",
        appFilterGlobal: false,
        appHidden: true,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "log_date_ins",
        appHeader: capitalize(t("IN18DATADEINSERCAODEFAULT")),
        appSortable: true,
        appFilter: false,
        appFilterMatch: "contains",
        appFilterGlobal: false,
        appHidden: true,
        appDataType: "date",
        appExport: true,
      },
      {
        appField: "log_date_upd",
        appHeader: capitalize(t("IN18DATADEALTERACAODEFAULT")),
        appSortable: true,
        appFilter: false,
        appFilterMatch: "contains",
        appFilterGlobal: false,
        appHidden: true,
        appDataType: "date",
        appExport: true,
      },
      {
        appField: "log_user_upd",
        appHeader: capitalize(t("IN18USUARIODEALTERACAODEFAULT")),
        appSortable: true,
        appFilter: false,
        appFilterMatch: "contains",
        appFilterGlobal: false,
        appHidden: true,
        appDataType: "text",
        appExport: true,
      },
    ],
  };
  // ==============================
  useEffect(() => {
    const dateIni = new Date();
    const dateFin = new Date();
    dateIni.setDate(dateIni.getDate() - 7);
    dateIni.setHours(21, 0, 0);
    dateFin.setHours(20, 59, 59);

    setDateIniProcessIni(dateIni.toJSON());
    setDateIniProcessFin(dateFin.toJSON());
  }, []);
  // ==============================

  return (
    <>
      <AppContainerTitle
        appTitle="Form Gerar períodos"
        appHelpText="Form Gerar períodos Help"
      />
      <AppTopBar
        appProcessVisible
        appProcessAction={handleProcess}
        appProgramId={ConstProgramUtil.cGerpergerarId}
        appProcessActionCode="PROCESS"
        appFavoriteVisible
      />
      <div className="pt-4 border-400 border-1 bg-white">
        <TabView
          activeIndex={activeIndex}
          onTabChange={(e) => setActiveIndex(e.index)}
          panelContainerClassName="p-0 md:p-2 mb-3"
          renderActiveOnly={false}
        >
          <TabPanel header="Parameters">
            <AppContainerFields>
              <AppFieldText
                appFormControl={formControl}
                name="pcodeprocess"
                appTitle="Código do processo"
                appHelpText="Código do processo Help"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                name="pgerpertipo"
                appTitle="Tipo periodo"
                appHelpText="Tipo periodo Help"
                appOptionLabel="nome"
                appOptionValue="id"
                appDataKey="id"
                appServiceDefault={gerTipoPeriodoService}
                appServiceFilterId="id"
                appServiceFilterDescription="sigla_per_tipo"
              />
              <AppFieldDropdownFk
                appFormControl={formControl}
                name="pgerempresaid"
                appTitle="Empresa"
                appHelpText="Empresa Help"
                appOptionLabel="nome"
                appOptionValue="id"
                appDataKey="id"
                appServiceDefault={gerEmpresaService}
                appServiceFilterId="id"
                appServiceFilterDescription="sigla_empresa"
              />
              <AppFieldDate
                appFormControl={formControl}
                name="pano"
                appTitle="Ano"
                appHelpText="Ano Help"
                appDateFormat="yy"
                appView="year"
              />
            </AppContainerFields>
          </TabPanel>
          <TabPanel header="Logs">
            <div className="col-12 flex justify-content-start flex-column">
              <div>
                <Button
                  icon="pi pi-filter"
                  className="p-button-secondary p-button-outlined ml-2 text-xl"
                  label="Filter"
                  onClick={handleFilterLog}
                />
              </div>
            </div>
            <AppContainerFields>
              <AppFieldDate
                name="pdateiniprocessini"
                appValue={dateIniProcessIni}
                appTitle="Data Inicial"
                appHelpText="Data Inicial Help"
                appShowSeconds
                appShowTime
                appOnChangeAction={(data) => {
                  setDateIniProcessIni(data.target.value);
                }}
              />
              <AppFieldDate
                name="pdateiniprocessfin"
                appValue={dateIniProcessFin}
                appTitle="Data Final"
                appHelpText="Data Final Help"
                appShowSeconds
                appShowTime
                appOnChangeAction={(data) => {
                  setDateIniProcessFin(data.target.value);
                }}
              />
              <AppFieldCheck
                appValue={error}
                name="error"
                appTitle="Erro"
                appHelpText="Erro Help"
                appTrueValue="S"
                appFalseValue="N"
                appTrueValueLabel="Sim"
                appFalseValueLabel="Não"
                appOnChangeAction={(data) => {
                  setError(data.target.checked);
                }}
              />
            </AppContainerFields>
            <div className="mt-4">
              <AppDataTable
                ref={dataTableRef}
                id="dt"
                appStateStorage="custom"
                appDataKey="id"
                appPaginateMode="local"
                appDataValue={dataValue}
                appColumns={dataTableColumns}
                appShowHeader
                appUserId={store.getState().auth.auth.user.id}
              />
            </div>
          </TabPanel>
        </TabView>
      </div>
    </>
  );
};

export default GerPerGerarForm;
