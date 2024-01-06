import { Button } from "primereact/button";
import { Divider } from "primereact/divider";
import { useState } from "react";
import { useMediaQuery } from "react-responsive";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
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

const SendResetPasswordEmailPage: React.FC = () => {
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
      fieldName: "email",
      required: [true, "Email is required"],
      defaultValue: "",
      type: "text",
    },
  ];
  // ==============================
  const formControl = useFormControl({
    fieldControls,
  });
  // ==============================
  const handleResetPassword = async (e: any) => {
    const valid = await formControl.isValid();
    const formValue = await formControl.getValues();
    if (valid) {
      const result = await AuthService.authResetPassword(formValue);
      if (result) {
        toast.success("Confirmation sent to your email");
        navigate("/signin");
      }
    } else {
      throw formControl.getErrors();
    }
  };
  // ==============================
  return (
    <>
      <AppLayoutLoading text={textloading} />
      <AppLayoutInit>
        <div
          className="w-full lg:w-6  p-4 bg-white "
          style={{
            borderBottomRightRadius: "15px",
            borderTopRightRadius: isTabletOrMobile ? "0px" : "15px",
            borderBottomLeftRadius: isTabletOrMobile ? "15px" : "0px",
          }}
        >
          <div className="flex align-items-center justify-content-center mb-3">
            <span className="text-2xl font-medium text-900">
              RESET PASSWORD
            </span>
          </div>
          <div className="flex justify-content-center">
            <Button
              className="p-ripple ml-2 w-6 font-medium py-3 px-2 inline-flex align-items-center justify-content-center p-button-link"
              onClick={handleSignIn}
            >
              <i className="pi pi-lock mr-2" />
              <span>Login</span>
            </Button>
          </div>
          <Divider align="center" className="my-4">
            <span className="text-600  font-normal text-sm">OR</span>
          </Divider>

          <AppContainerFields>
            <AppFieldText
              appFormControl={formControl}
              name="email"
              className="col-12"
              appTitle="Email"
              appHelpText="Email"
            />
          </AppContainerFields>

          <Button
            onClick={handleResetPassword}
            label="RESET"
            className="w-full py-3 font-medium"
            loading={textloading !== ""}
          />
        </div>
      </AppLayoutInit>
    </>
  );
};

export default SendResetPasswordEmailPage;
