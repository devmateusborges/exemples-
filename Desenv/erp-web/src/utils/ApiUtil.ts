/* eslint-disable no-param-reassign */
import axios, {
  AxiosError,
  AxiosInstance,
  AxiosRequestConfig,
  AxiosResponse,
} from "axios";
import _, { lowerCase } from "lodash";
import { FunctionComponent } from "react";
import { toast } from "react-toastify";

import { IAppDataTableColumn } from "../components/toolkit-react/AppDataTable";
import { authAction } from "../store/AuthStore";
import { textloadingAction } from "../store/UtilStore";

let store: any;

export const injectStore = (_store: any) => {
  store = _store;
};

const onRequest = (config: AxiosRequestConfig): AxiosRequestConfig => {
  // console.info("CONFIGINTERCEPTOR REQUEST", JSON.stringify(config));
  store.dispatch(textloadingAction("Resquest from server"));
  const { auth } = store.getState();
  if (auth.auth?.access_token && config.headers) {
    config.headers.authorization = `Bearer ${auth.auth?.access_token}`;
    // TODO colocar gtm e language no ultimo na sys_user inves store
    // TODO passar o ID do sistema WEB padrao no cabeçalho para usar o server
    config.headers["x-gtm"] = "-3";
    config.headers["x-unitid"] = auth.auth?.unit?.id;
    config.headers["x-lang"] = auth.i18nLang;
  }

  config.timeout = 60000;

  if (lowerCase(config.method) == "post" && config.url != "auth/login") {
    config.data["unit_id"] = auth.auth?.unit?.id;

    for (const f of Object.entries(config.data)) {
      // console.log("apiutil>", f);

      if (f[0].indexOf("_childs", 0) > 0) {
        if (!_.isNull(config.data[f[0]]) && !_.isEmpty(config.data[f[0]])) {
          config.data[f[0]].map((item: any) => {
            item["unit_id"] = auth.auth?.unit?.id;
            return item;
          });
        }
      }
    }
  }

  return config;
};

const onRequestError = (error: AxiosError): Promise<AxiosError> => {
  console.error("CONFIGINTERCEPTOR REQUEST ERROR", JSON.stringify(error));

  store.dispatch(textloadingAction(""));
  return Promise.reject(error);
};

const onResponse = (response: AxiosResponse): AxiosResponse => {
  // console.info("CONFIGINTERCEPTOR RESPONSE", JSON.stringify(response));
  store.dispatch(textloadingAction(""));
  return response;
};

const onResponseError = (error: any): Promise<AxiosError> => {
  console.error("CONFIGINTERCEPTOR RESPONSE ERROR", JSON.stringify(error));
  store.dispatch(textloadingAction(""));
  if (error?.response?.data?.msg) {
    if (error?.response?.data?.name == "VALIDATION_ERROR") {
      for (const e of Object.entries(error?.response?.data?.msg as object)) {
        toast.error(`${e[0]}: ${e[1]}`);
      }
    } else {
      toast.error(`Error ${JSON.stringify(error?.response?.data?.msg)}`);
    }
  } else {
    toast.error(`Error generic request server, verify log`);
  }

  return Promise.reject(error);
};

const configInterceptor = (axiosInstance: AxiosInstance): AxiosInstance => {
  axiosInstance.interceptors.request.use(onRequest, onRequestError);
  axiosInstance.interceptors.response.use(onResponse, onResponseError);
  return axiosInstance;
};

export const api = configInterceptor(
  axios.create({ baseURL: process.env.REACT_APP_API_URL })
);

export const apiParamsOperatorConvert = async (operator: any): Promise<any> => {
  // TODO ajustar todos tipos de operator filter converte 'startsWith' | 'contains' | 'notContains' | 'endsWith' | 'equals' | 'notEquals' | 'in' | 'lt' | 'lte' | 'gt' | 'gte' | 'between' | 'dateIs' | 'dateIsNot' | 'dateBefore' | 'dateAfter' | 'custom';
  let result = "";
  switch (operator) {
    case "equals":
      result = "equals";
      break;
    case "contains":
      result = "like";
      break;
    default:
      result = "like";
  }
  return result;
};

export const apiParamsConvert = async (
  params: any,
  columns: any
): Promise<any> => {
  // console.log("apiParamsConvert-params", params);

  let pfilters: any;
  let pFilterGlobal: any;
  if (params?.lazyParams?.filters) {
    for (const fkey of Object.keys(params.lazyParams.filters)) {
      let fvalue = params.lazyParams.filters[fkey].value;
      const foperator = await apiParamsOperatorConvert(
        params.lazyParams.filters[fkey].matchMode
      );
      if (fvalue !== null && fvalue !== "") {
        if (foperator === "like") {
          fvalue = `%${fvalue}%`;
        }

        if (fkey === "global") {
          const columnsFilterGlobal = columns.filter(
            (item: IAppDataTableColumn) => {
              if (item.appFilterGlobal) {
                return true;
              }
              return false;
            }
          );
          for (const colFilter of columnsFilterGlobal) {
            const filterObjGlobal = { [colFilter.appField]: { like: fvalue } };
            pFilterGlobal = { ...pFilterGlobal, ...filterObjGlobal };
          }
        } else {
          const columnsFilterField = columns.filter(
            (item: IAppDataTableColumn) => {
              if (item.appField == fkey) {
                return true;
              }
              return false;
            }
          );

          if (columnsFilterField[0].appFilterField) {
            const filterObj = {
              [columnsFilterField[0].appFilterField]: { [foperator]: fvalue },
            };
            pfilters = { ...pfilters, ...filterObj };
          } else {
            const filterObj = { [fkey]: { [foperator]: fvalue } };
            pfilters = { ...pfilters, ...filterObj };
          }
        }
      }
    }
    pfilters = { filter: { and: pfilters, or: pFilterGlobal } };
  }

  let porders: any;
  let pordersAux: any;
  let orderObj: any;
  let orderObjAux: any;
  if (params?.lazyParams?.multiSortMeta) {
    for (const obj of params.lazyParams.multiSortMeta) {
      let orderAux = "asc";
      if (obj.order === -1) {
        orderAux = "desc";
      }
      orderObjAux = { [obj.field]: orderAux };
      orderObj = { ...orderObj, ...orderObjAux };
    }
    pordersAux = { sort: orderObj };
    porders = { ...pordersAux };
  }

  const pfiltersAux = { ...pfilters, ...porders };
  const paramsAux = {
    ppage: (params.lazyParams?.page ? params.lazyParams.page : 0) + 1,
    pper_page: params.lazyParams?.rows ? params.lazyParams.rows : 5,
    pfilters: JSON.stringify(pfiltersAux),
  };
  // console.log("apiParamsConvert-paramsAux", paramsAux);
  return paramsAux;
};
