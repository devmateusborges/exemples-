import { t } from "i18next";
import { Button } from "primereact/button";
import { useEffect } from "react";
import { useMediaQuery } from "react-responsive";
import { useNavigate, useParams, useSearchParams } from "react-router-dom";
import { toast } from "react-toastify";
import AppContainer from "../../../components/toolkit-react/AppContainer";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppContainerTitle from "../../../components/toolkit-react/AppContainerTitle";
import AppFieldPassword from "../../../components/toolkit-react/AppFieldPassword";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";

import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import { AuthService } from "../../../services/AuthService";
import { useAppSelector } from "../../../store";
import { ConstUtil } from "../../../utils/ConstUtil";
import { capitalize } from "../../../utils/FuncUtil";
import AppLayoutInit from "../../layout/AppLayoutInit";
import AppLayoutLoading from "../../layout/AppLayoutLoading";

const RedefinePasswordPage: React.FC = () => {
  // ==============================
  const [searchParams, setSearchParams] = useSearchParams();
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "password",
      required: [true, "Password is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "newpassword",
      required: [true, "New password is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "confirmnewpassword",
      required: [true, "Confirm new password required"],
      defaultValue: "",
      type: "text",
    },
  ];
  // ==============================
  const formControl = useFormControl({
    fieldControls,
  });

  useEffect(() => {
    if (searchParams.get("passwordredefined")) {
      toast.success("Password redefined");
    }
  }, []);

  // ==============================
  const handleResetPassword = async () => {
    const valid = await formControl.isValid();
    const formValue = await formControl.getValues();
    try {
      if (valid) {
        if (formValue.confirmnewpassword == formValue.newpassword) {
          const dataForm = { ...formValue };
          delete dataForm.confirmnewpassword;
          const result = await AuthService.authRedefinePassword(dataForm);

          if (result) {
            toast.success("Confirmation sent to your email");
          }
        } else {
          toast.warning("New password and Confirm new password different");
        }
      } else {
        throw formControl.getErrors();
      }
    } catch (error) {
      if (error) {
        for (const f of Object.entries(error)) {
          toast.error(`${f[1]}`);
        }
      }
    }
  };

  // ==============================

  return (
    <>
      <AppContainer className="w-full">
        <AppContainerTitle
          appTitle={capitalize(t("IN18NSYSREDEFINEPASSWORD"))}
          appHelpText={capitalize(t("IN18NSYSREDEFINEPASSWORDHELP"))}
        />

        <div className="border-400 border-1 w-full pt-3 pb-2 md:pl-2 md:pr-2">
          <AppContainerFields>
            <AppFieldPassword
              appFormControl={formControl}
              name="password"
              appTitle="Password"
              appHelpText="Old Password"
              /* appOnBlurAction={formControl.handleBlur} */
            />
            <AppFieldPassword
              appFormControl={formControl}
              name="newpassword"
              appTitle="New password"
              appHelpText="New password"
              /* appOnBlurAction={formControl.handleBlur} */
            />
            <AppFieldPassword
              appFormControl={formControl}
              name="confirmnewpassword"
              appTitle="Confirm new password"
              appHelpText="Confirm new password"
              /* appOnBlurAction={formControl.handleBlur} */
            />
          </AppContainerFields>
          <div className="w-full flex justify-content-center mt-5">
            <Button
              onClick={handleResetPassword}
              label="Redefine password"
              className="w-auto py-3 font-medium"
            />
          </div>
        </div>
      </AppContainer>
    </>
  );
};

export default RedefinePasswordPage;
