import { initReactI18next } from "react-i18next";
import i18n from "i18next";
import LanguageDetector from "i18next-browser-languagedetector";
import resourcesAux from "./assets/i18n/locales.json";

(async () => {
  i18n
    .use(LanguageDetector)
    .use(initReactI18next)
    .init({
      resources: resourcesAux,
      debug: false,
      fallbackLng: "en-US",
      saveMissing: true,
      interpolation: {
        escapeValue: false,
      },
    });
})();

export default i18n;
