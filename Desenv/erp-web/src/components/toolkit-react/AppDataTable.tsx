/* eslint-disable guard-for-in */
/* eslint-disable no-return-assign */
/* eslint-disable no-nested-ternary */
/* eslint-disable react/require-default-props */

import { Menu, MenuProps } from "primereact/menu";
import { FilterMatchMode, FilterOperator } from "primereact/api";
import { Button } from "primereact/button";
import { Column, ColumnSelectionModeType } from "primereact/column";
import {
  DataTable,
  DataTableFilterDisplayType,
  DataTableFilterMeta,
  DataTableSelectionModeType,
  DataTableStateStorageType,
} from "primereact/datatable";
import { InputText } from "primereact/inputtext";
import { TabPanel, TabView } from "primereact/tabview";
import React, {
  memo,
  useCallback,
  useEffect,
  useImperativeHandle,
  useLayoutEffect,
  useMemo,
  useRef,
} from "react";
import { MultiSelect } from "primereact/multiselect";
import _ from "lodash";
import { v4 as uuid } from "uuid";
import AppVisible from "./bases/AppVisible";
import useState from "./hooks/useStateRef";
import IAppProps from "./interface/IAppProp";
import store from "../../store";
import { dataGridStateAction } from "../../store/PreferenceStore";
import AppPreference from "./AppPreference";
import {
  formatCurrencyColumn,
  formatDateTimeColumn,
  openDownloadFolder,
} from "../../utils/FuncUtil";
import AppGenericAction from "./AppGenericAction";
import { ConstUtil } from "../../utils/ConstUtil";
import AppGenericDocumentButton from "./AppGenericDocumentButton";

export interface IAppDataTable extends IAppProps {
  appLanguage?: any;
  appDataValue?: any;
  appPaginateMode?: "server" | "local" | undefined;
  appDataKey: string;
  appHelpText?: string;
  appFilterDisplay?: DataTableFilterDisplayType;
  appDataTableSelectionMode?: DataTableSelectionModeType;
  appColumnSelectionMode?: ColumnSelectionModeType;
  appColumns: IAppDataTableColumns;
  appRowExpansionTemplate?: any;
  appShowHeader?: boolean;
  appDataSelected?: any;
  appLoading?: boolean;
  appGlobalFilterFields?: Array<string>;
  appOnSelect?: any;
  appSetQueryParams?: any;
  appButtonExtraTemplateRow?: any;
  appButtonExtraVisibleRow?: any;
  appButtonDeleteVisibleRow?: any;
  appSetButtonQueryDeleteRow?: any;
  appButtonEditVisibleRow?: any;
  appSetButtonQueryEditRow?: any;
  appDataTableDetColumns?: Array<IAppDataTableDetColumns>;
  appRowExpand?: boolean;
  appSplitButtonsExtra?: Array<any>;
  appStateStorage?: DataTableStateStorageType;
  appProgramId?: string;
  appUserId: string;
  appPreferenceVisible?: boolean;
  appPreferenceService?: any;
  appPreferenceDeleteVisible?: boolean;
  appPreferenceEditVisible?: boolean;
  appPreferenceSaveVisible?: boolean;
  appPreferenceCheckVisible?: boolean;
  appPreferenceAddVisible?: boolean;
  appMenuBars?: boolean;
  appColumnSelection?: boolean;
}

export interface IAppDataTableColumn {
  style?: object;
  className?: string;
  appField: string;
  appHeader: string;
  appSortable?: boolean;
  appFilter?: boolean;
  appFilterMatch?: string;
  appFilterGlobal?: boolean;
  appFilterPlaceholder?: string;
  appFilterField?: string;
  appAlign?: any;
  appDataType?: "date" | "numeric" | "file" | "img" | "text" | "document";
  appDataTypeNMinDig?: number;
  appBody?: any;
  appVisible?: boolean;
  appHidden?: boolean;
  appMinWidth?: string;
  appMaxWidth?: string;
  whiteSpace?:
    | "-moz-pre-wrap"
    | "break-spaces"
    | "normal"
    | "nowrap"
    | "pre"
    | "pre-line"
    | "pre-wrap"
    | undefined;
  appRef?: any;
  appExport?: boolean;
}

export interface IAppDataTableColumns {
  columns: Array<IAppDataTableColumn>;
}

export interface IAppDataTableDetColumns {
  title: string;
  name: string;
  columns: Array<IAppDataTableColumn>;
  dataValue?: any;
}

const lazyParamsInitial = {
  first: 0,
  rows: 5,
  page: 0,
  sortField: "",
  sortOrder: null,
  multiSortMeta: null,
  filters: { global: { value: null, matchMode: FilterMatchMode.CONTAINS } },
};

const AppDataTable = React.forwardRef<any, IAppDataTable>(
  (props: IAppDataTable, ref) => {
    // ==============================
    const dt = useRef<DataTable>(null);
    const [loading, setLoading] = useState(props.appLoading);
    const [selected, setSelected, selectedRef] = useState(
      props.appDataSelected
    );
    const [data, setData] = useState([]);
    const [total, setTotal] = useState(0);
    const [filters, setFilters] = useState<any>({});
    const [filterGlobal, setFilterGlobal] = useState("");
    const [lazyParams, setLazyParams, lazyParamsRef] =
      useState<any>(lazyParamsInitial);
    const [filterCols, setFilterCols] = useState<DataTableFilterMeta>({});
    const [expandedRows, setExpandedRows] = useState<any>(undefined);
    const [detExpandedRowsActiveIndex, setExpandedRowsDetActiveIndex] =
      useState(0);
    const menu = useRef<Menu>(null);

    const [selectedColumns, setSelectedColumns] = useState<
      Array<IAppDataTableColumn>
    >(() => {
      return props.appColumns?.columns.filter((col) => col.appHidden != true);
    });
    const [dialogPreference, setDialogPreference] = useState(false);

    // ==============================
    const columnsFilter = (columns: IAppDataTableColumns) => {
      return columns.columns.filter((item: IAppDataTableColumn) => {
        if (item.appFilter) {
          return true;
        }
        return false;
      });
    };
    // ==============================
    useEffect(() => {
      let filterConvert = {};
      const filterColsAux = columnsFilter(props.appColumns);
      (async () => {
        for (const col of filterColsAux) {
          const ColAux = {
            [col.appField]: { value: null, matchMode: col.appFilterMatch },
          };
          filterConvert = { ...filterConvert, ...ColAux };
        }
        setFilterCols(filterConvert);
      })();
    }, []);

    // ==============================
    const handleSetQueryParams = () => {
      if (props.appSetQueryParams) {
        props.appSetQueryParams({ lazyParams: lazyParamsRef.current });
        setFilters(lazyParamsRef.current?.filters);
      }
      // console.log("AppDataTable-appSetApiParams-data", data);
    };
    // ==============================
    useEffect(() => {
      // console.log("AppDataTable-appSetApiParams", lazyParams);
      handleSetQueryParams();
    }, [lazyParams]);

    // ==============================
    useLayoutEffect(() => {
      setLoading(props.appLoading);
      if (
        props.appPaginateMode == "server" ||
        props.appPaginateMode == undefined
      ) {
        setData(props.appDataValue?.items ?? []);
        setTotal(props.appDataValue?.total ?? 0);
      } else if (props.appPaginateMode == "local") {
        setData(props?.appDataValue ?? []);
        setTotal(props?.appDataValue ?? 0);
      }

      if (
        Object.keys(lazyParams.filters).length > 1 &&
        Object.keys(lazyParams.filters)[0] !== "global"
      ) {
        const filterAux = { ...lazyParams.filters };
        filterAux["global"] = {
          value: filterGlobal,
          matchMode: FilterMatchMode.CONTAINS,
        };
        setFilters(filterAux);
        // console.log("useEffect-filters-1", filterAux);
      } else {
        const filterAux = { ...filterCols };
        filterAux["global"] = {
          value: filterGlobal,
          matchMode: FilterMatchMode.CONTAINS,
        };
        setFilters(filterAux);
        // console.log("useEffect-filters-2", filterAux);
      }
    }, [props.appLoading, props.appDataValue]);
    // ==============================
    useEffect(() => {
      // console.log("useEffect-appDataSelected-1", appDataSelected);
      setSelected(props.appDataSelected);
      // console.log("useEffect-appDataSelected-2", selected);
    }, [props.appDataSelected]);

    // ==============================
    const handleSelectionChange = useCallback((event: any) => {
      const { value } = event;
      setSelected(value);
      props.appOnSelect(value);
    }, []);
    // ==============================
    const handlePage = useCallback((event: any) => {
      const lazyParamsAux: any = _.clone(lazyParamsRef.current);

      lazyParamsAux["first"] = event.first;
      lazyParamsAux["page"] = event.page;
      lazyParamsAux["rows"] = event.rows;
      lazyParamsAux["pageCount"] = event.pageCount;

      setLazyParams(lazyParamsAux);
    }, []);
    // ==============================
    const handleSort = useCallback(async (event: any) => {
      const lazyParamsAux: any = _.clone(lazyParamsRef.current);

      lazyParamsAux["multiSortMeta"] = event.multiSortMeta;
      lazyParamsAux["sortField"] = event.sortField;
      lazyParamsAux["sortOrder"] = event.sortOrder;

      setLazyParams(lazyParamsAux);
    }, []);
    // ==============================
    const handleFilter = useCallback((event: any) => {
      const lazyParamsAux: any = _.clone(lazyParamsRef.current);

      lazyParamsAux["filters"] = event.filters;
      setLazyParams(lazyParamsAux);
    }, []);

    const handleExportCSV = () => {
      if (dt.current) {
        if (selectedRef.current && selectedRef.current.length > 0) {
          dt.current.exportCSV({ selectionOnly: true });
        } else {
          dt.current.exportCSV({ selectionOnly: false });
        }
      }
    };

    const formatColumnsData = (data: any) => {
      const dataAux: any = [];
      const columns = [];
      let columnsLoaded = false;
      // ==============================

      for (const dataCol of data) {
        const dataAuxObj: any = {};
        // ==============================
        for (const col of selectedColumns) {
          if (col.appExport) {
            const key = col.appField.split(".");
            let valueAux = dataCol;
            // ==============================

            for (const keyAux of key) {
              if (col.appDataType == "date") {
                if (valueAux[keyAux]) {
                  valueAux = formatDateTimeColumn(new Date(valueAux[keyAux]));
                } else {
                  valueAux = null;
                }
              } else {
                valueAux = valueAux[keyAux];
              }
            }
            // ==============================

            dataAuxObj[col.appHeader] = valueAux;
            if (!columnsLoaded) {
              columns.push({ title: col.appHeader, dataKey: col.appHeader });
            }
          }
        }
        // ==============================
        dataAux.push(dataAuxObj);
        columnsLoaded = true;
      }
      return [dataAux, columns];
    };
    const saveAsExcelFile = (buffer: any, fileName: any) => {
      import("file-saver").then((module) => {
        if (module && module.default) {
          const EXCEL_TYPE =
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;charset=UTF-8";
          const EXCEL_EXTENSION = ".xlsx";
          const data = new Blob([buffer], {
            type: EXCEL_TYPE,
          });

          module.default.saveAs(
            data,
            `${fileName}_export_${new Date().getTime()}${EXCEL_EXTENSION}`
          );
        }
      });
    };
    const handleExportXlsx = (data: any) => {
      import("xlsx").then((xlsx) => {
        let valueAux: any = [];
        if (selectedRef.current && selectedRef.current.length > 0) {
          valueAux = selectedRef.current;
        } else if (dt.current) {
          valueAux = dt.current.props.value;
        }
        // eslint-disable-next-line prefer-destructuring
        valueAux = formatColumnsData(valueAux)[0];
        const worksheet = xlsx.utils.json_to_sheet(valueAux);

        const workbook = { Sheets: { data: worksheet }, SheetNames: ["data"] };
        const excelBuffer = xlsx.write(workbook, {
          bookType: "xlsx",
          type: "array",
        });
        saveAsExcelFile(excelBuffer, uuid());
      });
    };

    const exportPdf = () => {
      import("jspdf").then((jsPDF) => {
        import("jspdf-autotable").then(async () => {
          let valueAux: any = [];

          if (selectedRef.current && selectedRef.current.length > 0) {
            valueAux = selectedRef.current;
          } else if (dt.current) {
            valueAux = dt.current.props.value;
          }

          const res = formatColumnsData(valueAux);

          // eslint-disable-next-line new-cap
          const doc: any = new jsPDF.default();
          doc.autoTable(res[1], res[0]);
          doc.save(uuid());
        });
      });
    };

    // ==============================
    const handleFilterGlobal = useCallback((event: any) => {
      const { value } = event.target;
      const filterAux = { ...lazyParams.filters };
      filterAux.global["value"] = value;

      const lazyParamsAux = { ...lazyParams };
      lazyParamsAux.filters["global"]["value"] = value;

      setFilters(filterAux);
      setFilterGlobal(value);
      setLazyParams(lazyParamsAux);
    }, []);
    // ==============================
    const appRefreshQuey = useCallback(() => {
      setLazyParams(lazyParamsInitial);
    }, []);

    // ==============================
    const appRestoreTableState = useCallback((state) => {
      if (dt.current) {
        dt.current.restoreTableState(state);
        if (state.selectedcolumns) {
          const orderedSelectedColumns = props.appColumns?.columns.filter(
            (col: any) =>
              state.selectedcolumns.some(
                (sCol: any) => sCol.appField == col.appField
              )
          );
          setSelectedColumns(orderedSelectedColumns);
        }
      }
    }, []);

    // ==============================
    useImperativeHandle(ref, () => {
      const res: any = {
        appRefreshQuey,
        appRestoreTableState,
        appReload: handleSetQueryParams,
      };
      return res;
    });

    // ==============================
    const handleColumnToggle = useCallback((event: any) => {
      const selectedColumns = event.value;
      const orderedSelectedColumns = props.appColumns?.columns.filter(
        (col: any) =>
          selectedColumns.some((sCol: any) => sCol.appField == col.appField)
      );
      setSelectedColumns(orderedSelectedColumns);
    }, []);
    // ==============================
    const onCustomSaveState = (state: any) => {
      const stateAux = { ...state, selectedcolumns: selectedColumns };

      if (props.id) {
        store.dispatch(
          dataGridStateAction({
            key: props.id,
            state: JSON.stringify(stateAux),
          })
        );
      }
    };
    // ==============================
    const renderHeader = useMemo(() => {
      let items = [
        {
          label: "Options",
          items: [
            {
              label: "Export CSV",
              icon: "pi pi-download",
              command: handleExportCSV,
            },
            {
              label: "Export XLSX",
              icon: "pi pi-download",
              command: handleExportXlsx,
            },
            {
              label: "Export PDF",
              icon: "pi pi-download",
              command: exportPdf,
            },
          ],
        },
      ];

      if (props.appPreferenceVisible) {
        items.unshift({
          label: "Preferences",
          items: [
            {
              label: "Preferences",
              icon: "pi pi-cog",
              command: () => {
                setDialogPreference(true);
              },
            },
          ],
        });
      }

      if (props.appSplitButtonsExtra) {
        items = [...items, ...props.appSplitButtonsExtra];
      }

      return (
        <>
          <div className="flex flex-column sm:flex-row justify-content-between align-items-center p-0 m-0">
            <div className="flex flex-row align-items-center">
              <AppVisible visible={props.appMenuBars ?? true}>
                <Menu model={items} popup ref={menu} />
                <Button
                  className="p-button-secondary p-button-outlined mr-2"
                  icon="pi pi-bars"
                  onClick={(event) => {
                    if (menu.current) {
                      menu.current.toggle(event);
                    }
                  }}
                  aria-haspopup
                />
              </AppVisible>
              <AppVisible visible={props.appColumnSelection ?? true}>
                <MultiSelect
                  value={selectedColumns}
                  options={props.appColumns?.columns}
                  optionLabel="appHeader"
                  onChange={handleColumnToggle}
                  className="w-15rem sm:w-15rem"
                />
              </AppVisible>
            </div>
            <div className="mt-2 sm:mt-0">
              <span className="p-input-icon-left m-0 p-0">
                <i className="pi pi-filter" />

                <InputText
                  value={filterGlobal}
                  onChange={handleFilterGlobal}
                  placeholder="Search"
                  style={{ width: "18em" }}
                />
              </span>
            </div>
          </div>
        </>
      );
    }, [filterGlobal, selectedColumns, props.appSplitButtonsExtra]);
    // ==============================
    const buttons = (rowData: any) => {
      return (
        <div className="flex flex-row justify-content-center align-items-center ">
          <AppVisible visible={props.appButtonEditVisibleRow}>
            <div className="pr-1">
              <AppGenericAction
                appIcon="pi pi-pencil text-xl"
                className="p-button-secondary p-button-outlined ml-2 text-xl"
                appOnAction={() => {
                  if (props.appSetButtonQueryEditRow != undefined) {
                    props.appSetButtonQueryEditRow(rowData);
                  }
                }}
                appProgramId={props.appProgramId}
                appActionCode="EDIT"
              />
            </div>
          </AppVisible>
          <AppVisible visible={props.appButtonDeleteVisibleRow}>
            <div className="pr-1">
              <AppGenericAction
                appIcon="pi pi-trash text-xl"
                className="p-button-secondary p-button-outlined ml-2 text-xl"
                appOnAction={() => {
                  if (props.appSetButtonQueryDeleteRow != undefined) {
                    props.appSetButtonQueryDeleteRow(rowData);
                  }
                }}
                appProgramId={props.appProgramId}
                appActionCode="DELETE"
              />
            </div>
          </AppVisible>
          <AppVisible visible={props.appButtonExtraVisibleRow}>
            {props.appButtonExtraTemplateRow ? (
              props.appButtonExtraTemplateRow(rowData)
            ) : (
              <></>
            )}
          </AppVisible>
        </div>
      );
    };
    // ==============================
    const handleColumnBody = (column: any, rowData: any) => {
      if (column.appBody) {
        return column.appBody(rowData);
      }
      if (rowData) {
        const columnAux = column.appField.split(".");
        let rowDataAux = rowData;
        let columnValue: any;

        if (columnAux.length > 1) {
          for (const t of columnAux) {
            if (
              rowDataAux &&
              Object.prototype.hasOwnProperty.call(rowDataAux, t)
            ) {
              rowDataAux = rowDataAux[t];
            }
          }
          columnValue = rowDataAux;
        } else {
          columnValue = rowDataAux[columnAux[0]];
        }

        if (column.appDataType == "date") {
          if (columnValue) {
            return formatDateTimeColumn(new Date(columnValue));
          }
        }

        if (column.appDataType == "numeric") {
          if (columnValue) {
            return formatCurrencyColumn(columnValue);
          }
        }

        if (column.appDataType == "currency") {
          // TODO passar minDig no column obj e adicionar $
          if (columnValue) {
            const lang = store.getState().auth.i18nLang;
            return formatCurrencyColumn(columnValue, lang);
          }
        }

        if (column.appDataType == "document") {
          const menuObjs: any = {
            label: "Arquivos",
            items: [],
          };

          for (const document of columnValue) {
            menuObjs.items.push({
              label: document.filename,
              icon: !document?.new ? "pi pi-download" : "",
              command: () => {
                if (!document?.new) {
                  openDownloadFolder(
                    `${process.env.REACT_APP_API_URL}/${ConstUtil.sysDocumentDownloadOpenRoute}/${document.id}-${document.filename}`
                  );
                }
              },
            });
          }

          return (
            <>
              <AppGenericDocumentButton appOptions={menuObjs} />
            </>
          );
        }

        return columnValue;
      }
      return undefined;
    };
    // ==============================
    const rowExpansionDetTemplate = (row: any) => {
      if (props.appRowExpand) {
        if (props.appDataTableDetColumns) {
          if (props.appDataTableDetColumns) {
            const childs = props.appDataTableDetColumns;

            return (
              <TabView
                activeIndex={detExpandedRowsActiveIndex}
                onTabChange={(e) => setExpandedRowsDetActiveIndex(e.index)}
              >
                {childs.map((child: any) => {
                  return (
                    <TabPanel header={child.title ?? ""} key={child?.name}>
                      <DataTable
                        id={`dt${props?.id}det${child?.name}`}
                        value={row[child.name]}
                        responsiveLayout="scroll"
                        size="small"
                        scrollHeight="30rem"
                        filterDisplay="row"
                        className="max-h-30rem"
                      >
                        {child.columns.map((column: any) => (
                          <Column
                            key={column.appField}
                            field={column.appField}
                            filterField={column.appField}
                            header={column.appHeader}
                            sortable={
                              column.appSortable ? column.appSortable : false
                            }
                            filter={column.appFilter ? column.appFilter : false}
                            filterPlaceholder={column.appFilterPlaceholder}
                            style={{
                              ...column.style,
                              minWidth: column.appMinWidth
                                ? column.appMinWidth
                                : "10px",
                              maxWidth: column.appMaxWidth
                                ? column.appMaxWidth
                                : "10px",
                              whiteSpace: column.whiteSpace
                                ? column.whiteSpace
                                : "nowrap",
                            }}
                            align={column.appAlign}
                            className={column.className}
                            dataType={column.appDataType}
                            body={(rowData) => {
                              return handleColumnBody(column, rowData);
                            }}
                            hidden={column.appHidden ? column.appHidden : false}
                          />
                        ))}
                      </DataTable>
                    </TabPanel>
                  );
                })}
              </TabView>
            );
          }
        } else {
          console.error("Obrigatório appDataTableDetColumns para appRowExpand");
        }
      }

      return <></>;
    };

    // ==============================

    return (
      <>
        <AppPreference
          id={props.id}
          appDeleteVisible={props.appPreferenceDeleteVisible}
          appEditVisible={props.appPreferenceEditVisible}
          appSaveVisible={props.appPreferenceSaveVisible}
          appCheckVisible={props.appPreferenceCheckVisible}
          appAddVisible={props.appPreferenceAddVisible}
          appServiceDefault={props.appPreferenceService}
          appUserId={props.appUserId}
          appObjectId={props.appProgramId}
          appObjectSubId={props.id}
          appObjectType="DATATABLE_STATE"
          appVisible={dialogPreference}
          appOnQueryDialogHide={() => setDialogPreference(false)}
          appOnSelected={async (data: any) => {
            appRestoreTableState(JSON.parse(data?.value));
          }}
        />

        <DataTable
          ref={dt}
          value={data}
          rowHover
          cellSelection
          dragSelection
          responsiveLayout="scroll"
          loading={loading}
          dataKey={props.appDataKey}
          className="shadow-2"
          header={
            props.appGlobalFilterFields
              ? renderHeader
              : props.appShowHeader
              ? renderHeader
              : null
          }
          selection={selected}
          selectionMode={
            props.appDataTableSelectionMode
              ? props.appDataTableSelectionMode
              : "checkbox"
          }
          filters={filters}
          filterDisplay={
            props.appFilterDisplay ? props.appFilterDisplay : "row"
          }
          size="small"
          globalFilterFields={props.appGlobalFilterFields}
          sortMode="multiple"
          removableSort
          multiSortMeta={lazyParams.multiSortMeta}
          lazy={
            props.appPaginateMode == undefined
              ? true
              : props.appPaginateMode == "server"
          }
          paginator
          first={lazyParams.first}
          rows={lazyParams.rows}
          totalRecords={total}
          paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown"
          currentPageReportTemplate="{first} to {last} of {totalRecords}"
          rowsPerPageOptions={[5, 10, 25, 50]}
          emptyMessage="No row(s) found."
          onSelectionChange={handleSelectionChange}
          onPage={handlePage}
          onSort={handleSort}
          onFilter={handleFilter}
          expandedRows={expandedRows}
          onRowToggle={(e) => setExpandedRows(e.data)}
          rowExpansionTemplate={
            props.appRowExpansionTemplate ?? rowExpansionDetTemplate
          }
          stateStorage={props.appStateStorage}
          customSaveState={onCustomSaveState}
        >
          <Column expander={props.appRowExpand} style={{ width: "3em" }} />

          <Column
            selectionMode={
              props.appColumnSelectionMode
                ? props.appColumnSelectionMode
                : "multiple"
            }
            headerStyle={{ width: "3em" }}
          />
          <Column body={buttons} />
          {selectedColumns.map((column) => (
            <Column
              resizeable={false}
              key={column.appField}
              field={column.appField}
              filterField={column.appField}
              header={column.appHeader}
              sortable={column.appSortable ? column.appSortable : false}
              filter={column.appFilter ? column.appFilter : false}
              filterPlaceholder={column.appFilterPlaceholder}
              style={{
                ...column.style,
                minWidth: column.appMinWidth ?? "200px",
                maxWidth: column.appMaxWidth ?? "1000px",
                whiteSpace: column.whiteSpace ?? "nowrap",
              }}
              align={column.appAlign}
              className={column.className}
              dataType={column.appDataType}
              body={(rowData) => {
                return handleColumnBody(column, rowData);
              }}
            />
          ))}
        </DataTable>
      </>
    );
  }
);
// ==============================
export default memo(AppDataTable);
