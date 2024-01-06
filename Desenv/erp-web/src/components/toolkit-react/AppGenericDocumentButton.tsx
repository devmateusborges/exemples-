/* eslint-disable react/require-default-props */
import { Button } from "primereact/button";
import { Menu } from "primereact/menu";
import { useRef, useState } from "react";
import IAppProps from "./interface/IAppProp";

interface IAppGenericDocumentButton extends IAppProps {
  appOptions: any;
}

const AppGenericDocumentButton: React.FC<IAppGenericDocumentButton> = (
  props: IAppGenericDocumentButton
) => {
  const ref = useRef<Menu>(null);

  // ==============================
  return (
    <>
      <Button
        icon="pi pi-file text-xl"
        className="p-button-secondary p-button-rounded p-button-outlined mr-3"
        onClick={(event) => {
          if (ref.current) {
            ref.current.toggle(event);
          }
        }}
        aria-haspopup
        aria-controls="popup_menu"
      />

      <Menu
        className="w-full sm:w-auto"
        model={[props.appOptions]}
        popup
        ref={ref}
        id="popup_menu"
      />
    </>
  );
};

export default AppGenericDocumentButton;
