import { Button } from "primereact/button";
import { Column } from "primereact/column";
import { DataTable } from "primereact/datatable";
import { TabPanel, TabView } from "primereact/tabview";
import { useEffect, useRef, useState } from "react";

import { Dialog } from "primereact/dialog";
import { t } from "i18next";
import { Menu } from "primereact/menu";
import useDebounce from "../../../components/toolkit-react/hooks/useDebounce";
import Test1Service from "../../../services/modules/tst/Test1Service";
import { apiParamsConvert } from "../../../utils/ApiUtil";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";
import {
  capitalize,
  formatCurrencyColumn,
  formatDateTimeColumn,
} from "../../../utils/FuncUtil";

import AppFieldTitle from "../../../components/toolkit-react/bases/AppFieldTitle";
import AppFieldDialogHelp from "../../../components/toolkit-react/bases/AppFieldDialogHelp";
import { dataTableColumnsDet1 } from "./Test1Det1Form";
import { dataTableColumnsDet2 } from "./Test1Det2Form";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";
import GenericListPage from "../../generics/GenericListPage";

const test1Service = new Test1Service();

const Test1: React.FC = () => {
  // const { debounce } = useDebounce();
  // const [queryParams, setQueryParams] = useState<any>({});
  // const [queryData, setQueryData] = useState({});
  const [detExpandedRowsActiveIndex, setExpandedRowsDetActiveIndex] =
    useState(0);

  const dataTableColumns: IAppDataTableColumns = {
    columns: [
      {
        appField: "id",
        appHeader: "ID",
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: true,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "codigo",
        appHeader: "Código",
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appMinWidth: "200px",
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "descricao",
        appHeader: "Descrição",
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "dt_nascimento",
        appHeader: "Data de nascimento",
        appSortable: true,
        appDataType: "date",
        appExport: true,
      },
      {
        appField: "quantidade",
        appHeader: "Quantidade",
        appAlign: "right",
        appSortable: true,
        appDataType: "numeric",
        appExport: true,
      },
      {
        appField: "test1_fk_id_obj.id",
        appHeader: "Test1Fk - ID",
        appSortable: true,
        appFilter: true,
        appHidden: true,
        appFilterMatch: "contains",
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "test1_fk_id_obj.codigo",
        appHeader: "Test1Fk - Código",
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "radio_obj.code",
        appHeader: "Radio Código",
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "radio_obj.description",
        appHeader: "Radio Descrição",
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "ativo_obj.description",
        appHeader: "Ativo",
        appSortable: true,
        appFilter: false,
        appFilterMatch: "contains",
        appFilterGlobal: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "sys_document_childs",
        appHeader: "Arquivos",
        appSortable: false,
        appFilter: false,
        appFilterMatch: "contains",
        appDataType: "document",
      },
      {
        appField: "log_user_ins",
        appHeader: capitalize(t("IN18USUARIODEINSERCAODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: true,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "log_date_ins",
        appHeader: capitalize(t("IN18DATADEINSERCAODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: true,
        appDataType: "date",
        appExport: true,
      },
      {
        appField: "log_date_upd",
        appHeader: capitalize(t("IN18DATADEALTERACAODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: true,
        appDataType: "date",
        appExport: true,
      },
      {
        appField: "log_user_upd",
        appHeader: capitalize(t("IN18USUARIODEALTERACAODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: true,
        appDataType: "text",
        appExport: true,
      },
    ],
  };
  // Utilizado como alternativa ao serviceDefault
  /* useEffect(() => {
    debounce(() => {
      (async () => {
        const result = await test1Service.list(
          await apiParamsConvert(queryParams, dataTableColumns.columns)
        );
        setQueryData(result);
      })();
    });
  }, [queryParams]); */
  /* const dataTableRef = useRef<IAppDataTableChild>(); */

  const detsColumns = [
    {
      title: "Det 1",
      name: "test1_childs",
      ...dataTableColumnsDet1,
    },
    {
      title: "Det 2",
      name: "test1a_childs",
      ...dataTableColumnsDet2,
    },
  ];
  const buttonExtraTemplate = (rowData: any) => {
    return (
      <>
        <div className="pr-1">
          <Button
            icon="pi pi-bolt text-xl"
            className="p-button-secondary p-button-outlined"
            aria-label="Extra"
            onClick={() => {
              console.log("Button Extra 1 >>> ", rowData);
            }}
          />
        </div>
        <div className="pr-1">
          <Button
            icon="pi pi-star text-xl"
            className="p-button-secondary p-button-outlined"
            aria-label="Extra"
            onClick={() => {
              console.log("Button Extra 2 >>> ", rowData);
            }}
          />
        </div>
      </>
    );
  };

  // Utilizado como customização para o template padrao appRowExpansionDetTemplate do dataTable, nao necessita passar appDataTableDetColumns
  /* const rowExpansionDetTemplate = (row: any) => {
    const childs = detsColumns;

    return (
      <TabView
        activeIndex={detExpandedRowsActiveIndex}
        onTabChange={(e) => setExpandedRowsDetActiveIndex(e.index)}
        className="w-full"
      >
        {childs.map((child: any) => {
          return (
            <TabPanel header={`${child.title} Custom`} key={child?.name}>
              <DataTable
                id={`dtTest1Listdet${child?.name}`}
                value={row[child.name]}
                responsiveLayout="scroll"
                filterDisplay="row"
              >
                {child.columns.map((column: any) => (
                  <Column
                    key={column.appField}
                    field={column.appField}
                    filterField={column.appField}
                    header={column.appHeader}
                    sortable={column.appSortable ? column.appSortable : false}
                    filter={column.appFilter ? column.appFilter : false}
                    filterPlaceholder={column.appFilterPlaceholder}
                    style={
                      column.appMinWidth
                        ? { ...column.style, minWidth: column.appMinWidth }
                        : { ...column.style, minWidth: "200px" }
                    }
                    className={column.className}
                    dataType={column.appDataType}
                    body={column.appBody}
                    hidden={column.appHidden ? column.appHidden : false}
                  />
                ))}
              </DataTable>
            </TabPanel>
          );
        })}
      </TabView>
    );
    return <></>;
  };
 */
  const splitButtonsExtra = [
    {
      label: "Custom",
      items: [
        {
          label: "Item custom",
          icon: "pi pi-circle",
          command: () => {},
        },
      ],
    },
  ];

  return (
    <>
      <GenericListPage
        id="Test1List"
        appProgramId={ConstProgramUtil.cTstTest1Id}
        appTitle={capitalize(t("i18nTest1Titulo"))}
        // help devera vir da tabela program
        appHelpText="xxx"
        // Utilizado como alternativa ao serviceDefault
        // appDataTableDataValue={queryData}
        appShowTopBar
        appRouteForm="/private/tst/test1form"
        appDataTableColumns={dataTableColumns}
        appDataTableDetColumns={detsColumns}
        appRowExpand
        // Utilizado como customização para o template padrao appRowExpansionDetTemplate do dataTable, nao necessita passar appDataTableDetColumns
        // appRowExpansionDetTemplate={rowExpansionDetTemplate}
        appDataTableDataKey="id"
        appDataTableGlobalFilterFields={["code"]}
        appRefreshVisible
        appFavoriteVisible
        appAddVisible
        appDeleteVisible
        appEditVisible
        appServiceDefault={test1Service}
        appSplitButtonsExtra={splitButtonsExtra}
        appButtonExtraTemplateRow={buttonExtraTemplate}
        appButtonExtraVisibleRow
        appButtonDeleteVisibleRow
        appButtonEditVisibleRow
        appPreferenceVisible
        // Utilizado como alternativa ao serviceDefault
        // appOnQueryDelete={async (item) => {
        //   console.log("GenericListPage>appOnQueryDelete", item);
        // }}
        // Utilizado como alternativa ao serviceDefault
        // appSetQueryParams={(params: any) => {
        //   setQueryParams(params);
        // }}
      />
    </>
  );
};

export default Test1;
