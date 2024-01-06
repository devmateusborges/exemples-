import { Dialog } from "primereact/dialog";
import { memo, useState } from "react";

import AppFieldDialogHelp from "./bases/AppFieldDialogHelp";
import IAppProps from "./interface/IAppProp";
import { StyleSheet } from "./utils/StyleSheet";

interface IAppContainerTitle extends IAppProps {
  appTitle: string;
  appSmall?: boolean;
  appIconColor?: string;
  appClassIcon?: string;
  appClassTitleText?: string;
  appClassTitleBg?: string;
}

const styles = StyleSheet.create({
  local: {
    paddingLeft: "5px",
    paddingRight: "5px",
    marginTop: "8px",
  },
});

const AppContainerTitle: React.FC<IAppContainerTitle> = (
  props: IAppContainerTitle
) => {
  // ==============================
  const [displayHelp, setDisplayHelp] = useState(false);
  // ==============================
  return (
    <>
      <div
        className={`flex pl-3  p-2 shadow-1 ${
          props.appClassTitleText ? props.appClassTitleBg : "surface-200"
        }  text-sm  font-bold`}
        style={{
          borderTopLeftRadius: "3px",
          borderTopRightRadius: "3px",
          borderBottomLeftRadius: "3px",
          borderBottomRightRadius: "3px",
        }}
      >
        <a
          className={`mt-1 mb-1 uppercase ${
            props.appClassTitleText ? props.appClassTitleText : "text-800"
          }  ${props.appSmall ? "text-lg" : "text-2xl"}`}
        >
          <i
            className={` ${props.appClassIcon} ${
              props.appSmall ? "text-lg" : "text-2xl"
            } ${props.appClassIcon ? "mr-3" : ""} `}
          />
          {props.appTitle}
        </a>
        {(() => {
          if (props.appHelpText) {
            return (
              <>
                <AppFieldDialogHelp
                  className="ml-2 text-white text-lg mt-1"
                  title={props.appTitle}
                  helpText={props.appHelpText}
                  displayHelp={displayHelp}
                  onDisplayHelp={setDisplayHelp}
                />
              </>
            );
          }
          return <></>;
        })()}
      </div>
    </>
  );
};

export default memo(AppContainerTitle);
