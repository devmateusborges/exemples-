/* eslint-disable react/require-default-props */
import { Button } from "primereact/button";
import { toast } from "react-toastify";
import { AuthService } from "../../services/AuthService";
import IAppProps from "./interface/IAppProp";

interface IAppGenericAction extends IAppProps {
  appProgramId?: string;
  appActionCode?: string;
  appLabel?: string;
  appIcon?: string;
  appOnAction: any;
}

const AppGenericAction: React.FC<IAppGenericAction> = (
  props: IAppGenericAction
) => {
  const verifyActionAccess = async (e: any) => {
    if (props.appProgramId && props.appActionCode) {
      const isValid = await AuthService.authProgramActionAccess(
        props.appProgramId,
        props.appActionCode
      );

      if (isValid) {
        props.appOnAction(e);
      } else {
        toast.warning("Insufficient permission!");
      }
    } else {
      props.appOnAction(e);
    }
  };
  // ==============================
  return (
    <>
      <Button
        icon={props.appIcon}
        className={`${props.className} ${props.classNameBorder} ${props.classNameText}`}
        label={props.appLabel}
        aria-label={props.appLabel}
        onClick={(e) => verifyActionAccess(e)}
      />
    </>
  );
};

export default AppGenericAction;
