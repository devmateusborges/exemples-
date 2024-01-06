import { t } from "i18next";
import { capitalize } from "../../../utils/FuncUtil";
import { useEffect, useState } from "react";

import useDebounce from "../../../components/toolkit-react/hooks/useDebounce";
import SysGroupProgramFeatureService from "../../../services/modules/sys/SysGroupProgramFeatureService";

import { apiParamsConvert } from "../../../utils/ApiUtil";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";
import GenericListPage from "../../generics/GenericListPage";

const sysGroupProgramFeatureService = new SysGroupProgramFeatureService();

const SysGroupProgramFeature: React.FC = () => {
  const dataTableColumns: IAppDataTableColumns = {
    columns: [
      {
        appField: "id",
        appHeader: "ID",
        appSortable: false,
        appFilter: false,
        appFilterMatch: "contains",
        appFilterGlobal: false,
        appHidden: true,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "identity_feature",
        appHeader: capitalize(t("IN18USUARIODEINSERCAODEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "sys_group_id_obj.name",
        appHeader: capitalize(t("IN18GROUPONOMEDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
      },
      {
        appField: "sys_program_id_obj.name",
        appHeader: capitalize(t("IN18SISTEMAPROGRAMANOMEDEFAULT")),
        appSortable: true,
        appFilter: true,
        appFilterMatch: "contains",
        appFilterGlobal: true,
        appHidden: false,
        appDataType: "text",
        appExport: true,
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

  return (
    <>
      <GenericListPage
        appTitle={capitalize(t("IN18SYSFUNCIONALIDADEDOPROGRAMAGRUPODEFAULT"))}
        appShowTopBar
        appRouteForm="/private/sys/sysgroupprogramfeatureform"
        appDataTableColumns={dataTableColumns}
        appDataTableDataKey="id"
        appRefreshVisible
        appDeleteVisible
        appEditVisible
        appAddVisible
        appServiceDefault={sysGroupProgramFeatureService}
      />
    </>
  );
};

export default SysGroupProgramFeature;
