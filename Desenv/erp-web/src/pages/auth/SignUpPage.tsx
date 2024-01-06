import { Button } from "primereact/button";
import { Divider } from "primereact/divider";
import { useState } from "react";
import { useMediaQuery } from "react-responsive";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
import { confirmDialog } from "primereact/confirmdialog";
import AppContainerFields from "../../components/toolkit-react/AppContainerFields";

import AppFieldMask from "../../components/toolkit-react/AppFieldMask";
import AppFieldPassword from "../../components/toolkit-react/AppFieldPassword";
import AppFieldText from "../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../components/toolkit-react/hooks/useFormControl";
import { AuthService } from "../../services/AuthService";
import { useAppSelector } from "../../store";
import { ConstUtil } from "../../utils/ConstUtil";
import { UtilValidEmail } from "../../utils/FuncUtil";
import AppLayoutInit from "../layout/AppLayoutInit";
import AppLayoutLoading from "../layout/AppLayoutLoading";
import { signUpWithGoogle } from "../../firebase";

const SignUpPage: React.FC = () => {
  // ==============================
  const isTabletOrMobile = useMediaQuery({
    query: ConstUtil.cisTabletOrMobile,
  });
  const navigate = useNavigate();
  const textloading = useAppSelector((state) => state.util.textloading);
  // ==============================

  const handleSignIn = () => {
    navigate("/signin");
  };
  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "name",
      required: [true, "Name is required"],
    },
    {
      fieldName: "email",
      required: [true, "Email is required"],
    },
    {
      fieldName: "document",
      required: [true, "Document is required"],
    },
    {
      fieldName: "phone",
      required: [true, "Phone is required"],
    },
    {
      fieldName: "password",
      required: [true, "Password is required"],
    },
  ];

  const formControl = useFormControl({
    fieldControls,
  });
  // ==============================

  const handleRegister = async (e: any) => {
    e.preventDefault();

    const valid = await formControl.isValid();
    if (valid) {
      const i18nextLng = localStorage.getItem("i18nextLng");
      const data = {
        ...formControl.getValues(),
        sys_tran_lang_id_default: i18nextLng,
      };
      const result = await AuthService.authRegister(data);
      if (result) {
        if (
          !result?.data?.success &&
          result.data.msg == "EMAIL_AREADY_EXISTS"
        ) {
          confirmDialog({
            message:
              "User with this email already exists, want to change password ?",
            header: "Confirmation",
            icon: "pi pi-question-circle",
            accept: async () => {
              navigate("/resetpassword");
            },
          });
        } else {
          toast.success("Register user success");
          navigate("/signin");
        }
      } else {
        formControl.handleResetForm();
      }
    } else {
      for (const f of Object.entries(formControl.getErrors())) {
        toast.error(`${f[1]}`);
      }
    }
  };

  const handleRegisterSocialGoogle = async () => {
    await signUpWithGoogle();
  };
  // ==============================

  return (
    <>
      <AppLayoutLoading text={textloading} />
      <AppLayoutInit>
        <div
          className="w-12 flex-grow-1 p-4 bg-white "
          style={{
            borderBottomRightRadius: "15px",
            borderTopRightRadius: isTabletOrMobile ? "0px" : "15px",
            borderBottomLeftRadius: isTabletOrMobile ? "15px" : "0px",
          }}
        >
          <div className="flex align-items-center justify-content-center mb-3">
            <span className="text-2xl font-medium text-900">REGISTER</span>
          </div>
          <div className=" flex sm:flex-row flex-column flex-column justify-content-center h-12">
            <Button
              type="button"
              className="p-ripple w-full font-medium m-1 border-1 surface-border surface-100 py-3 px-2 p-component hover:surface-200 active:surface-300 text-900 cursor-pointer transition-colors transition-duration-150 inline-flex align-items-center justify-content-center"
              onClick={handleRegisterSocialGoogle}
            >
              <i className="pi pi-google text-700 mr-2" />
              <span>Sign in With Google</span>
            </Button>
          </div>
          <div className="w-12 flex justify-content-center">
            <Button
              type="button"
              className="p-ripple w-6 font-medium py-3 px-2 inline-flex align-items-center justify-content-center p-button-link"
              onClick={handleSignIn}
            >
              <i className="pi pi-user-plus mr-2" />
              <span>Login</span>
            </Button>
          </div>
          <Divider align="center" className="my-4">
            <span className="text-600  font-normal text-sm">OR</span>
          </Divider>
          <AppContainerFields>
            <AppFieldText
              className="col-12"
              name="name"
              appTitle="Name"
              appHelpText="yyyy"
              appErrors={[formControl.getTouchedErrors("name")]}
              appOnBlurAction={formControl.handleBlur}
              appOnChangeAction={formControl.handleChange}
              appValue={formControl.getValues().name}
            />

            <AppFieldMask
              className="col-12"
              name="document"
              appTitle="Document"
              appHelpText="yyyy"
              appErrors={[formControl.getTouchedErrors("document")]}
              appOnBlurAction={formControl.handleBlur}
              appOnChangeAction={formControl.handleChange}
              appValue={formControl.getValues().document}
              appMask="999.999.999-99"
            />

            <AppFieldMask
              className="col-12"
              name="phone"
              appTitle="Phone"
              appHelpText="yyyy"
              appErrors={[formControl.getTouchedErrors("phone")]}
              appOnBlurAction={formControl.handleBlur}
              appOnChangeAction={formControl.handleChange}
              appValue={formControl.getValues().phone}
              appMask="(99) 99999-9999"
            />

            <AppFieldText
              className="col-12"
              name="email"
              appTitle="Email for login"
              appHelpText="yyyy"
              appErrors={[formControl.getTouchedErrors("email")]}
              appOnBlurAction={formControl.handleBlur}
              appOnChangeAction={formControl.handleChange}
              appValue={formControl.getValues().email}
            />

            <AppFieldPassword
              className="col-12"
              name="password"
              appTitle="Password"
              appHelpText="yyyy"
              appErrors={[formControl.getTouchedErrors("password")]}
              appOnBlurAction={formControl.handleBlur}
              appOnChangeAction={formControl.handleChange}
              appValue={formControl.getValues().password}
            />
          </AppContainerFields>
          <Button
            onClick={handleRegister}
            label="SIGN UP"
            className="w-full py-3 font-medium"
            loading={textloading !== ""}
          />
        </div>
      </AppLayoutInit>
    </>
  );
};

export default SignUpPage;
