"use client";
import "primereact/resources/themes/bootstrap4-light-blue/theme.css";
import "primereact/resources/primereact.min.css";
import "primeicons/primeicons.css";
import "primeflex/primeflex.css";
import "@styles/layout.scss";
import { GoogleAnalytics } from "nextjs-google-analytics";
import { Provider } from "react-redux";

import AppLgpdCookie from "@components/AppLgpdCookie";
import AppTopbar from "@components/AppTopbar";
import AppFooter from "@components/AppFooter";
import store from "@store/index";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <GoogleAnalytics />
        <Provider store={store}>
          <AppLgpdCookie id="AppLgpdCookie" />
          <AppTopbar id="AppMenuTopBar" />
          {children}
          <AppFooter id={"AppFooter"} />
        </Provider>
      </body>
    </html>
  );
}
