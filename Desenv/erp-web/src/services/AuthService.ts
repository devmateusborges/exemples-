import {
  ILoginRequest,
  ILoginSocialRequest,
  IRedefinePasswordRequest,
  IRegisterRequest,
  IResetPasswordRequest,
} from "../interfaces/AuthInterfaces";
import store from "../store";
import {
  authAction,
  authProgramAction,
  authModuleAction,
  authProgramFavoriteAction,
} from "../store/AuthStore";
import { api } from "../utils/ApiUtil";

// ==============================
const authLogin = async (data: ILoginRequest): Promise<any> => {
  const result = await api.post<any>(`auth/login`, data);
  // console.log("authLogin", result);
  if (result?.data?.access_token) {
    await store.dispatch(authAction(result.data));
  }
  return result?.data;
};

const authLoginGoogle = async (data: ILoginSocialRequest) => {
  return api.post<any>("auth/logingoogle", data);
};

// ==============================
const authRegister = async (data: IRegisterRequest): Promise<any> => {
  return api.post<any>(`auth/register`, data);
};
// ==============================
const authResetPassword = async (data: IResetPasswordRequest): Promise<any> => {
  return api.post<any>(`auth/sendresetpasswordemail`, data);
};
// ==============================
const authRedefinePassword = async (
  data: IRedefinePasswordRequest
): Promise<any> => {
  return api.post<any>(`auth/sendredefinepasswordemail`, data);
};
// ==============================
const authRegisterSocialGoogle = async (data: any): Promise<any> => {
  return api.post<any>(`auth/registersocialgoogle`, data);
};

// ==============================
export const authListUnit = async (params: any): Promise<any> => {
  const result = await api.get<any>(`/auth/getunitbyuserlogin/`, {
    params,
  });
  return result?.data;
};
// ==============================
const authListProgram = async (params: any): Promise<any> => {
  let resultAux = [];
  const { program } = await store.getState().auth;
  if (program?.total > 0 && params.findCache) {
    if (params.sysModuleId) {
      resultAux = await program.items.filter((item: any) => {
        return item?.sys_module_id == params.sysModuleId;
      });
    } else {
      resultAux = await program.items;
    }

    // console.log("authListProgram-com-store");
  } else {
    const result = await api.get<any>(`/auth/getprogrambyuserlogin/`, {
      params,
    });

    if (params?.saveCache) {
      store.dispatch(authProgramAction(result.data));
    }

    if (params.sysModuleId) {
      resultAux = await result.data.items.filter((item: any) => {
        return item?.sys_module_id == params.sysModuleId;
      });
    } else {
      resultAux = await result.data.items;
    }
    // console.log("authListProgram-sem-store");
  }
  return resultAux;
};
// ==============================
const authListModule = async (params: any): Promise<any> => {
  let resultAux = [];
  const { module } = await store.getState().auth;
  if (module?.total > 0 && params.findCache) {
    resultAux = module.items;
    // console.log("authListModule-com-store");
  } else {
    const result = await api.get<any>(`/auth/getmodulebyuserlogin/`, {
      params,
    });
    if (params.saveCache) {
      store.dispatch(authModuleAction(result.data));
    }
    resultAux = await result.data.items;
    // console.log("authListModule-sem-store");
  }
  return resultAux;
};

// ==============================
const authProgramActionAccess = async (
  pProgramId: string,
  pActionCode: string
): Promise<any> => {
  const result = await api.get<any>(`/auth/getprogramactionbyuserlogin/`, {
    params: {
      pfilters: {
        filter: {
          and: {
            login: store.getState().auth.auth.user.login,
            pvsysprogramid: pProgramId,
          },
        },
      },
      saveCache: false,
    },
  });
  let resultAux = false;

  for (const action of result.data.items) {
    if (action.sys_action_code === pActionCode) {
      resultAux = true;
    }
  }

  return resultAux;
};

// ==============================
const listI18nGmt = async (): Promise<any> => {
  const result = await api.get<any>(`/auth/i18ngmt`);
  return result?.data;
};
// ==============================
const listI18nLang = async (): Promise<any> => {
  const result = await api.get<any>(`/auth/i18nlang`);
  return result?.data;
};
// ==============================
export const AuthService = {
  authLogin,
  authRegister,
  authResetPassword,
  authListUnit,
  authListProgram,
  authListModule,
  authProgramActionAccess,
  listI18nGmt,
  listI18nLang,
  authRedefinePassword,
  authLoginGoogle,
  authRegisterSocialGoogle,
};
