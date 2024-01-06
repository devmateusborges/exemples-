import PrimeReact from "primereact/api";
import { ConfirmDialog } from "primereact/confirmdialog";
import React, { Suspense } from "react";
import ReactDOM from "react-dom";
import { BrowserRouter, HashRouter, Route, Routes } from "react-router-dom";
import { ToastContainer } from "react-toastify";
import "./styles/layout.css";
import { ProgressSpinner } from "primereact/progressspinner";
import AppScrollTop from "./components/toolkit-react/AppScrollTop";
import reportWebVitals from "./reportWebVitals";
import "./i18n";
import { injectStore } from "./utils/ApiUtil";
import store, { persitor } from "./store";
import App from "./App";

injectStore(store);

PrimeReact.ripple = true;

ReactDOM.render(
  <React.StrictMode>
    <Suspense
      fallback={
        <div className="w-full h-full flex justify-content-center align-items-center">
          <ProgressSpinner />
        </div>
      }
    >
      <HashRouter>
        <AppScrollTop>
          <ToastContainer
            position="top-center"
            autoClose={3000}
            hideProgressBar={false}
            newestOnTop={false}
            closeOnClick
            rtl={false}
            pauseOnFocusLoss
            draggable
            pauseOnHover
            bodyStyle={{ fontSize: "14px" }}
          />
          <ConfirmDialog />
          <App />
        </AppScrollTop>
      </HashRouter>
    </Suspense>
  </React.StrictMode>,
  document.getElementById("root")
);
reportWebVitals();
