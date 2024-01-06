import React, { useEffect, useState } from "react";
import { Provider } from "react-redux";
import { Route, Routes } from "react-router-dom";
import { PersistGate } from "redux-persist/integration/react";
import { toast } from "react-toastify";
import SendResetPasswordEmailPage from "./pages/auth/SendResetPasswordEmailPage";
import { getFirebaseToken, onMessageListener } from "./firebase";
import SignInPage from "./pages/auth/SignInPage";
import SignUpPage from "./pages/auth/SignUpPage";
import AppLayout from "./pages/layout/AppLayout";
import AppLayoutAuthorization from "./pages/layout/AppLayoutAuthorization";
import AppLayoutMenuFavorite from "./pages/layout/AppLayoutMenuFavorite";
import AppLayoutMenuNotification from "./pages/layout/AppLayoutMenuNotification";
import AppLayoutNotFound from "./pages/layout/AppLayoutNotFound";
import AppLayoutPrivate from "./pages/layout/AppLayoutPrivate";
import RouterBor from "./routers/RouterBor";
import RouterBov from "./routers/RouterBov";
import RouterCms from "./routers/RouterCms";
import RouterCrm from "./routers/RouterCrm";
import RouterCtb from "./routers/RouterCtb";
import RouterFin from "./routers/RouterFin";
import RouterFis from "./routers/RouterFis";
import RouterGer from "./routers/RouterGer";
import RouterInd from "./routers/RouterInd";
import RouterMob from "./routers/RouterMob";
import RouterMov from "./routers/RouterMov";
import RouterOpe from "./routers/RouterOpe";
import RouterPto from "./routers/RouterPto";
import RouterRhm from "./routers/RouterRhm";
import RouterSys from "./routers/RouterSys";
import RouterTst from "./routers/RouterTst";
import store, { persitor } from "./store";

const App: React.FC = () => {
  const [showNotificationBanner, setShowNotificationBanner] = useState(
    Notification.permission != "granted"
  );

  const [notification, setNotification] = useState({ title: "", body: "" });

  const handleGetFirebaseToken = async () => {
    try {
      console.log("Init getFirebaseToken");
      const firebaseToken = await getFirebaseToken();
      console.log("Firebase token: ", firebaseToken);
      if (firebaseToken) {
        setShowNotificationBanner(false);
      }
    } catch (error: any) {
      console.error(
        "An error occured while retrieving firebase token. ",
        error
      );
    }
  };

  onMessageListener()
    .then((payload: any) => {
      console.log("APP: Received foreground message: ", payload);
      if (payload) {
        setNotification({
          title: payload?.notification?.title,
          body: payload?.notification?.body,
        });
      }
    })
    .catch((err) =>
      console.log("An error occured while retrieving foreground message. ", err)
    );

  useEffect(() => {
    if (notification?.title) {
      // TODO pode melhor nitifcation FIREBASE com titulo e clics etc.
      toast.warn(notification?.body);
    }
  }, [notification]);

  useEffect(() => {
    handleGetFirebaseToken();
  }, []);

  return (
    <div className="h-full w-full">
      <Provider store={store}>
        <PersistGate loading={null} persistor={persitor}>
          {showNotificationBanner && (
            <div className="app-push-notification-banner">
              <span>The app needs permission to</span>
              <a
                href="#"
                className="app-push-notification-banner-link"
                onClick={handleGetFirebaseToken}
              >
                ENABLE PUSH NOTIFICATIONS.
              </a>
            </div>
          )}
          <Routes>
            <Route path="/" element={<SignInPage />} />
            <Route path="signin" element={<SignInPage />} />
            <Route path="signup" element={<SignUpPage />} />

            <Route
              path="resetpassword"
              element={<SendResetPasswordEmailPage />}
            />
            <Route
              path="private"
              element={
                <AppLayoutPrivate>
                  <AppLayout />
                </AppLayoutPrivate>
              }
            >
              <Route
                path="sys/sysprogramfavorite"
                element={<AppLayoutMenuFavorite />}
              />
              <Route
                path="sys/sysnotification"
                element={<AppLayoutMenuNotification />}
              />

              {RouterBor.map(({ programId, path, element }) => (
                <Route
                  key={path}
                  path={path}
                  element={
                    <AppLayoutAuthorization programId={programId}>
                      {element}
                    </AppLayoutAuthorization>
                  }
                />
              ))}
              {RouterBov.map(({ programId, path, element }) => (
                <Route
                  key={path}
                  path={path}
                  element={
                    <AppLayoutAuthorization programId={programId}>
                      {element}
                    </AppLayoutAuthorization>
                  }
                />
              ))}
              {RouterCms.map(({ programId, path, element }) => (
                <Route
                  key={path}
                  path={path}
                  element={
                    <AppLayoutAuthorization programId={programId}>
                      {element}
                    </AppLayoutAuthorization>
                  }
                />
              ))}
              {RouterCrm.map(({ programId, path, element }) => (
                <Route
                  key={path}
                  path={path}
                  element={
                    <AppLayoutAuthorization programId={programId}>
                      {element}
                    </AppLayoutAuthorization>
                  }
                />
              ))}
              {RouterCtb.map(({ programId, path, element }) => (
                <Route
                  key={path}
                  path={path}
                  element={
                    <AppLayoutAuthorization programId={programId}>
                      {element}
                    </AppLayoutAuthorization>
                  }
                />
              ))}
              {RouterFin.map(({ programId, path, element }) => (
                <Route
                  key={path}
                  path={path}
                  element={
                    <AppLayoutAuthorization programId={programId}>
                      {element}
                    </AppLayoutAuthorization>
                  }
                />
              ))}
              {RouterFis.map(({ programId, path, element }) => (
                <Route
                  key={path}
                  path={path}
                  element={
                    <AppLayoutAuthorization programId={programId}>
                      {element}
                    </AppLayoutAuthorization>
                  }
                />
              ))}
              {RouterGer.map(({ programId, path, element }) => (
                <Route
                  key={path}
                  path={path}
                  element={
                    <AppLayoutAuthorization programId={programId}>
                      {element}
                    </AppLayoutAuthorization>
                  }
                />
              ))}
              {RouterInd.map(({ programId, path, element }) => (
                <Route
                  key={path}
                  path={path}
                  element={
                    <AppLayoutAuthorization programId={programId}>
                      {element}
                    </AppLayoutAuthorization>
                  }
                />
              ))}
              {RouterMob.map(({ programId, path, element }) => (
                <Route
                  key={path}
                  path={path}
                  element={
                    <AppLayoutAuthorization programId={programId}>
                      {element}
                    </AppLayoutAuthorization>
                  }
                />
              ))}
              {RouterMov.map(({ programId, path, element }) => (
                <Route
                  key={path}
                  path={path}
                  element={
                    <AppLayoutAuthorization programId={programId}>
                      {element}
                    </AppLayoutAuthorization>
                  }
                />
              ))}
              {RouterOpe.map(({ programId, path, element }) => (
                <Route
                  key={path}
                  path={path}
                  element={
                    <AppLayoutAuthorization programId={programId}>
                      {element}
                    </AppLayoutAuthorization>
                  }
                />
              ))}
              {RouterPto.map(({ programId, path, element }) => (
                <Route
                  key={path}
                  path={path}
                  element={
                    <AppLayoutAuthorization programId={programId}>
                      {element}
                    </AppLayoutAuthorization>
                  }
                />
              ))}
              {RouterRhm.map(({ programId, path, element }) => (
                <Route
                  key={path}
                  path={path}
                  element={
                    <AppLayoutAuthorization programId={programId}>
                      {element}
                    </AppLayoutAuthorization>
                  }
                />
              ))}
              {RouterSys.map(({ programId, path, element }) => (
                <Route
                  key={path}
                  path={path}
                  element={
                    <AppLayoutAuthorization programId={programId}>
                      {element}
                    </AppLayoutAuthorization>
                  }
                />
              ))}
              {RouterTst.map(({ programId, path, element }) => (
                <Route
                  key={path}
                  path={path}
                  element={
                    <AppLayoutAuthorization programId={programId}>
                      {element}
                    </AppLayoutAuthorization>
                  }
                />
              ))}

              <Route
                path="*"
                element={
                  <main style={{ padding: "1rem" }}>
                    <AppLayoutNotFound />
                  </main>
                }
              />
            </Route>
          </Routes>
        </PersistGate>
      </Provider>
    </div>
  );
};

export default App;
