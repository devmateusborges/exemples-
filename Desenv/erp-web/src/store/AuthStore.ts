import { createSlice, PayloadAction } from "@reduxjs/toolkit";

const initialStateAux = {
  auth: {
    access_token: "",
    unit: { id: "", sigla_unit: "", name: "" },
    user: { id: "", login: "", email: "", name: "" },
  },
  program: { total: 0, items: [] },
  programFavorite: { total: 0, items: [] },
  module: { total: 0, items: [] },
  menuIndex: 0,
  showMenu: false,
  signinRememberme: "N",
  i18nLang: undefined,
  i18nGmt: undefined,
};

const AuthStore = createSlice({
  name: "auth",

  initialState: initialStateAux,
  reducers: {
    authAction(state, action: PayloadAction<any>) {
      state.auth = action.payload;
    },
    authProgramAction(state, action: PayloadAction<any>) {
      state.program = action.payload;
    },
    authProgramFavoriteAction(state, action: PayloadAction<any>) {
      state.programFavorite = action.payload;
    },
    authModuleAction(state, action: PayloadAction<any>) {
      state.module = action.payload;
    },
    authCleanAction(state) {
      state.auth.access_token = initialStateAux.auth.access_token;
      state.program = initialStateAux.program;
      state.module = initialStateAux.module;
    },
    authMenuIndexAction(state, action: PayloadAction<any>) {
      state.menuIndex = action.payload;
    },
    authShowMenuAction(state, action: PayloadAction<any>) {
      state.showMenu = action.payload;
    },
    signinRemembermeAction(state, action: PayloadAction<any>) {
      // console.log("signinRemembermeAction", action.payload);
      state.signinRememberme = action.payload;
    },
    authLangAction(state, action: PayloadAction<any>) {
      state.i18nLang = action.payload;
    },
    authGmtAction(state, action: PayloadAction<any>) {
      state.i18nGmt = action.payload;
    },
  },
});

export const {
  authAction,
  authProgramAction,
  authProgramFavoriteAction,
  authModuleAction,
  authCleanAction,
  authMenuIndexAction,
  authShowMenuAction,
  signinRemembermeAction,
  authLangAction,
  authGmtAction,
} = AuthStore.actions;

export default AuthStore.reducer;
