import { Action, configureStore, ThunkAction } from "@reduxjs/toolkit";
import { TypedUseSelectorHook, useDispatch, useSelector } from "react-redux";
import { combineReducers } from "redux";
import { persistReducer, persistStore } from "redux-persist";
import storage from "redux-persist/lib/storage";
import thunk from "redux-thunk";

import AuthStore from "./AuthStore";
import CrudStore from "./CrudStore";
import UtilStore from "./UtilStore";
import PreferenceStore from "./PreferenceStore";
import ThemeStore from "./ThemeStore";

const persistConfig = {
  key: "root",
  storage,
  blacklist: ["util", "crud"],
};
const rootReducer = combineReducers({
  util: UtilStore,
  auth: AuthStore,
  crud: CrudStore,
  pref: PreferenceStore,
  theme: ThemeStore,
});

const persistedReducer = persistReducer(persistConfig, rootReducer);

const store = configureStore({
  reducer: persistedReducer,
  devTools: process.env.NODE_ENV !== "production",
  middleware: [thunk],
});

export type RootState = ReturnType<typeof store.getState>;

export type AppDispatch = typeof store.dispatch;

export type AppThunk = ThunkAction<void, RootState, null, Action<string>>;

export const useAppDispatch = () => useDispatch<AppDispatch>();
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;

export const persitor = persistStore(store);
export default store;
