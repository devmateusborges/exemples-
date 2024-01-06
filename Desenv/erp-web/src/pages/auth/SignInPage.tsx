import _ from "lodash";
import { Button } from "primereact/button";
import { Checkbox } from "primereact/checkbox";
import { Divider } from "primereact/divider";
import { useCallback, useEffect } from "react";
import { useMediaQuery } from "react-responsive";
import { useNavigate, useSearchParams } from "react-router-dom";
import { toast } from "react-toastify";

import { useTranslation, withTranslation, Trans } from "react-i18next";
import { confirmDialog } from "primereact/confirmdialog";
import AppFieldCheck from "../../components/toolkit-react/AppFieldCheck";
import AppFieldDropdownFk, {
  IAppFieldDropdownFkOptions,
} from "../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldText from "../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../components/toolkit-react/hooks/useFormControl";
import useState from "../../components/toolkit-react/hooks/useStateRef";
import { AuthService } from "../../services/AuthService";
import store, { useAppSelector } from "../../store";
import {
  signinRemembermeAction,
  authLangAction,
  authGmtAction,
  authCleanAction,
} from "../../store/AuthStore";

import { ConstUtil } from "../../utils/ConstUtil";
import AppLayoutInit from "../layout/AppLayoutInit";
import AppLayoutLoading from "../layout/AppLayoutLoading";
import { capitalize } from "../../utils/FuncUtil";
import AppFieldDropdown from "../../components/toolkit-react/AppFieldDropdown";
import { signInWithGoogle } from "../../firebase";

const SignInPage: React.FC = () => {
  // ==============================
  const isTabletOrMobile = useMediaQuery({
    query: ConstUtil.cisTabletOrMobile,
  });
  const [searchParams, setSearchParams] = useSearchParams();

  const navigate = useNavigate();
  const textloading = useAppSelector((state) => state.util.textloading);
  const auth = useAppSelector((state) => state.auth);
  const [i18nLang, setI18nLang] = useState<any>(undefined);
  const [i18nGmt, setI18nGmt] = useState<any>(undefined);
  const [i18nGmtOptions, setI18nGmtOptions] = useState<any>(undefined);
  const [i18nLangOptions, setI18nLangOptions] = useState<any>(undefined);

  const [dropdownDataUnitId, setDropdownDataUnitId] =
    useState<IAppFieldDropdownFkOptions>({ total: 0, items: [] });
  const dropdownRowsPageUnitId = 5;
  const { t, i18n } = useTranslation();
  const themeBorder = store.getState().theme.classNameBorder;
  const themeBg = store.getState().theme.classNameBg;
  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "login",
      required: [true, "Login is required"],
      defaultValue: auth.signinRememberme == "S" ? auth.auth.user.login : "",
    },
    {
      fieldName: "password",
      required: [true, "Password is required"],
    },
    {
      fieldName: "unit_id",
      required: [true, "Unidade is required"],
      defaultValue: auth.signinRememberme == "S" ? auth.auth.unit.id : "",
    },
    {
      fieldName: "rememberme",
      required: [false, ""],
      defaultValue: auth.signinRememberme,
    },
  ];
  const formControl = useFormControl({
    fieldControls,
  });

  useEffect(() => {
    if (searchParams.get("userdeactivated")) {
      toast.success("User deactivated successful");
      store.dispatch(authCleanAction());
    } else if (searchParams.get("passwordreseted")) {
      toast.success(
        "User password reseted successful, open your email to see the new password"
      );
    }
  }, []);
  // ==============================

  const handleSignUp = () => {
    navigate("/signup");
  };
  // ==============================
  const handleLogin = async (e: any) => {
    e.preventDefault();
    const valid = await formControl.isValid();
    const formValue = await formControl.getValues();
    const formValueAux = _.cloneDeep(formValue);
    delete formValueAux.rememberme;
    if (valid) {
      const result = await AuthService.authLogin(formValueAux);
      if (result) {
        store.dispatch(signinRemembermeAction(formValue.rememberme));
        navigate("/private");
      } else {
        formControl.handleResetForm();
      }
    } else {
      for (const f of Object.entries(formControl.getErrors())) {
        toast.error(`${f[1]}`);
      }
    }
  };
  // ==============================

  const handleChangeLogin = (e: any) => {
    formControl.setValueField("unit_id", "");
    formControl.handleChange(e);
  };
  // ==============================

  const handleDropdownUnitId = async (e: any): Promise<any> => {
    const filterAux = {
      filter: {
        and: {
          login: (await formControl.getValues()).login,
          name: e.filter || "%",
        },
        or: { id: e.value || "%" },
      },
    };

    const result = await AuthService.authListUnit({
      pfilters: filterAux,
      ppage: e.page,
      pper_page: dropdownRowsPageUnitId,
    });
    setDropdownDataUnitId(result);
  };

  const handleSelectedLangGmt = (i18nGmt: any) => {
    store.dispatch(authGmtAction(i18nGmt.value));
    setI18nGmt(i18nGmt.value);
  };
  // ==============================

  const handleSelectedLang = (event: any) => {
    const { value } = event;
    setI18nLang(value);
    i18n.changeLanguage(value);
    store.dispatch(authLangAction(value));
  };
  // ==============================

  useEffect(() => {
    (async () => {
      setI18nLangOptions((await AuthService.listI18nLang()).items);
      setI18nGmtOptions((await AuthService.listI18nGmt()).items);
    })();

    const i18nextLng = localStorage.getItem("i18nextLng");
    if (i18nextLng) {
      store.dispatch(authLangAction(i18nextLng));
    }

    const { i18nLang } = store.getState().auth;
    if (i18nLang) {
      setI18nLang(i18nLang);
    }

    const { i18nGmt } = store.getState().auth;
    if (!i18nGmt) {
      const date = new Date().getTimezoneOffset();
      const currentTimezone = (date / 60) * -1;
      // console.log(`GMT ${currentTimezone}`);
      store.dispatch(authGmtAction(currentTimezone.toString()));
      setI18nGmt(currentTimezone.toString());
    } else {
      setI18nGmt(i18nGmt);
    }
  }, []);

  const handleLoginSocial = async () => {
    try {
      const signInWithGoogleRes = await signInWithGoogle();
      console.log(signInWithGoogleRes);

      confirmDialog({
        message: (
          <div className="grid">
            <AppFieldDropdownFk
              className="col-12"
              appFormControl={formControl}
              appValue={formControl.getValues().unit_id}
              name="unit_id"
              appTitle="Unidade"
              appHelpText="yyyy"
              appOptions={dropdownDataUnitId}
              appOptionLabel="name"
              appOptionValue="id"
              appDataKey="id"
              appRowsPage={dropdownRowsPageUnitId}
              appOnFilterAction={(e: any) => {
                return handleDropdownUnitId(e);
              }}
            />
          </div>
        ),
        className: "w-full md:w-5",
        header: "Choose a unit",
        icon: "pi pi-exclamation-triangle",
        accept: () => {},
        reject: () => {},
      });
      /*     if (signInWithGoogleRes?.user?.email) {
      const result: any = await AuthService.authLoginGoogle({
        login: signInWithGoogleRes.user.email,
      });
    } */
    } catch (error) {
      console.error(error);
    }
  };
  return (
    <>
      <AppLayoutLoading text={textloading} />
      <AppLayoutInit>
        <div
          className="w-12 flex-grow-1 p-4 bg-white"
          style={{
            borderBottomRightRadius: "15px",
            borderTopRightRadius: isTabletOrMobile ? "0px" : "15px",
            borderBottomLeftRadius: isTabletOrMobile ? "15px" : "0px",
          }}
        >
          <div className="flex align-items-center justify-content-center mb-3">
            <span className="text-2xl font-medium text-900">LOGIN</span>
          </div>

          <div className=" flex sm:flex-row flex-column flex-column justify-content-center h-12">
            <Button
              type="button"
              className="p-ripple w-full font-medium m-1 border-1 surface-border surface-100 py-3 px-2 p-component hover:surface-200 active:surface-300 text-900 cursor-pointer transition-colors transition-duration-150 inline-flex align-items-center justify-content-center"
              onClick={handleLoginSocial}
            >
              <i className="pi pi-google text-700 mr-2" />
              <span>Sign in With Google</span>
            </Button>
          </div>

          <div className="w-12 flex justify-content-center">
            <Button
              type="button"
              className="p-ripple w-6 font-medium py-3 px-2 inline-flex align-items-center justify-content-center p-button-link"
              onClick={handleSignUp}
            >
              <i className="pi pi-user-plus mr-2" />
              <span>Sign Up</span>
            </Button>
          </div>
          <Divider align="center" className="my-4">
            <span className="text-600 font-normal text-sm">OR</span>
          </Divider>
          <AppFieldText
            className="col-12"
            appFormControl={formControl}
            name="login"
            appTitle="Username"
            appHelpText="yyyy"
            appOnChangeAction={handleChangeLogin}
          />
          <AppFieldText
            className="col-12"
            appFormControl={formControl}
            name="password"
            appTitle={capitalize(t("IN18SENHADEFAULT"))}
            appHelpText="yyyy"
            appInputType="password"
          />
          <AppFieldDropdownFk
            className="col-12"
            appFormControl={formControl}
            appValue={formControl.getValues().unit_id}
            name="unit_id"
            appTitle="Unidade"
            appHelpText="yyyy"
            appOptions={dropdownDataUnitId}
            appOptionLabel="name"
            appOptionValue="id"
            appDataKey="id"
            appRowsPage={dropdownRowsPageUnitId}
            appOnFilterAction={(e: any) => {
              return handleDropdownUnitId(e);
            }}
          />
          <div className="flex align-items-center justify-content-between">
            <div className="flex align-items-center">
              <AppFieldCheck
                appFormControl={formControl}
                name="rememberme"
                appTitle="Rememberme"
                appHelpText="yyyy"
                appFalseValue="N"
                appTrueValue="S"
              />
            </div>
            <a
              className="font-medium text-blue-500 hover:text-blue-700 cursor-pointer transition-colors transition-duration-150"
              onClick={() => {
                navigate("/resetpassword");
              }}
            >
              Forgot password?
            </a>
          </div>
          <div className=" grid justify-content-center mb-2">
            <div className="col-12 sm:col-6 flex justify-content-center">
              <AppFieldDropdown
                appTitle="Language"
                className="w-full mt-2"
                name="i18nLang"
                appValue={i18nLang}
                appPlaceholder="Linguagem"
                appOptions={i18nLangOptions}
                appOptionLabel="code"
                appOptionValue="code"
                appOnChangeAction={handleSelectedLang}
              />
            </div>
            <div className="col-12 sm:col-6 flex justify-content-center">
              <AppFieldDropdown
                appTitle="GMT"
                className="w-full mt-2"
                name="i18n_gmt"
                appValue={i18nGmt}
                appPlaceholder="GMT "
                appOptions={i18nGmtOptions}
                appOptionLabel="description_type"
                appOptionValue="value_type"
                appOnChangeAction={handleSelectedLangGmt}
              />
            </div>
          </div>
          <Button
            onClick={handleLogin}
            label="SIGN IN"
            className={`w-full py-3 font-medium ${themeBg} ${themeBorder}`}
            loading={textloading !== ""}
          />
        </div>
      </AppLayoutInit>
    </>
  );
};
// ==============================

export default SignInPage;
