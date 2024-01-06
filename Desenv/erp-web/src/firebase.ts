/* eslint-disable no-undef */
/* eslint-disable prettier/prettier */
/* eslint-disable no-promise-executor-return */
import {
  getToken,
  getMessaging,
  onMessage,
  deleteToken,
} from "firebase/messaging";
import { initializeApp } from "firebase/app";
import { getAuth, signInWithPopup, GoogleAuthProvider } from "firebase/auth";
import { toast } from "react-toastify";
import SysNotificationTokenService from "./services/modules/sys/SysNotificationTokenService";
import { AuthService } from "./services/AuthService";

const firebaseConfig = {
  apiKey: process.env.REACT_APP_FIREBASE_API_KEY,
  authDomain: process.env.REACT_APP_FIREBASE_AUTH_DOMAIN,
  databaseURL: process.env.REACT_APP_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.REACT_APP_FIREBASE_PROJECT_ID,
  storageBucket: process.env.REACT_APP_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.REACT_APP_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.REACT_APP_FIREBASE_APP_ID,
};

const firebaseApp = initializeApp(firebaseConfig);
const messaging = getMessaging(firebaseApp);

export const getOrRegisterSw = async () => {
  if ("serviceWorker" in navigator) {
    let sw;

    sw = await window.navigator.serviceWorker.getRegistration(
      "/firebase-push-notification-scope"
    );

    if (!sw) {
      sw = await window.navigator.serviceWorker.register(
        "/firebase-messaging-sw.js",
        { scope: "/firebase-push-notification-scope" }
      );
    }
    return sw;
  }

  throw new Error("The browser doesn`t support service worker.");
};

export const getFirebaseToken = async () => {
  // TODO apos login pegar esse token que deve ser quadado na store e validar com novo se for igual apoas alogado precisa atualziar a unit e user id no banco notif_token
  const sysNotificationTokenService = new SysNotificationTokenService();
  const sw = await getOrRegisterSw();
  const tokenFb = await getToken(messaging, {
    vapidKey: process.env.REACT_APP_FIREBASE_VAPID_KEY,
    serviceWorkerRegistration: sw,
  });
  await sysNotificationTokenService.save({
    token: tokenFb,
    data_token: "",
  });
  return tokenFb;
};

export const onMessageListener = () =>
  new Promise((resolve) => {
    onMessage(messaging, (payload) => {
      console.log("FIREBASE: Received foreground message: ", payload);

      resolve(payload);
    });
  });

// TODO Analisar melhor forma, talvez no servidor limpar por periodo se incluir novamente tudo bem.
//  deleteToken(messaging)

const auth = getAuth(firebaseApp);

const googleProvider = new GoogleAuthProvider();

export const signUpWithGoogle = async () => {
  const socialGoogleResult: any = await signInWithPopup(auth, googleProvider);
  const date = new Date().getTimezoneOffset();
  const currentTimezone = (date / 60) * -1;
  const gmt = currentTimezone.toString();

  socialGoogleResult["sys_tran_lang_id_default"] =
    localStorage.getItem("i18nextLng");
  socialGoogleResult["gtm_default"] = gmt;

  const authRegisterSocialGoogleResult =
    await AuthService.authRegisterSocialGoogle(socialGoogleResult);

  console.log(authRegisterSocialGoogleResult);
  if (authRegisterSocialGoogleResult.status == 201) {
    toast.success("Register user success");
    // navigate("/signin");
  }

  return socialGoogleResult;
};

export const signInWithGoogle = async () => {
  const socialGoogleResult: any = await signInWithPopup(auth, googleProvider);

  return socialGoogleResult;
};
