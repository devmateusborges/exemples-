/* eslint-disable jsx-a11y/mouse-events-have-key-events */
/* eslint-disable react/require-default-props */
import { Dialog } from "primereact/dialog";
import { memo } from "react";

import IAppProps from "../interface/IAppProp";
import AppVisible from "./AppVisible";

interface IAppFieldDialogHelp extends IAppProps {
  title?: string;
  helpText?: string;
  displayHelp: boolean;
  onDisplayHelp: (show: boolean) => void;
}

const AppFieldDialogHelp: React.FC<IAppFieldDialogHelp> = (
  props: IAppFieldDialogHelp
) => {
  return (
    <>
      <AppVisible visible={props.helpText}>
        <a
          className={`${
            props.className || "text-500"
          } border-circle   cursor-pointer font-bold ml-1`}
          onClick={() => {
            props.onDisplayHelp(true);
          }}
        >
          <i className="pi pi-question-circle text-sm" />
        </a>
        <Dialog
          header={`Help for ${props.title}`}
          visible={props.displayHelp}
          onHide={() => {
            props.onDisplayHelp(false);
          }}
          breakpoints={{ "960px": "75vw" }}
          style={{ width: "50vw" }}
          onClick={() => {
            props.onDisplayHelp(false);
          }}
        >
          <p>{props.helpText}</p>
        </Dialog>
      </AppVisible>
    </>
  );
};

export default memo(AppFieldDialogHelp);
