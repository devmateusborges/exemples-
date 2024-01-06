/* eslint-disable react/require-default-props */
import { FileUpload } from "primereact/fileupload";
import { Image } from "primereact/image";
import { memo, useEffect, useLayoutEffect, useState } from "react";
import { v4 as uuid } from "uuid";
import { useMediaQuery } from "react-responsive";
import { confirmDialog } from "primereact/confirmdialog";
import store from "../../store";

import IAppProps from "./interface/IAppProp";
import IAppPropErrors from "./interface/IAppPropErrors";
import IAppPropName from "./interface/IAppPropName";
import AppGenericAction from "./AppGenericAction";
import AppVisible from "./bases/AppVisible";
import { ConstUtil } from "../../utils/ConstUtil";
import { openDownloadFolder } from "../../utils/FuncUtil";
import AppFieldErrors from "./bases/AppFieldErrors";

interface IAppFieldFile extends IAppProps, IAppPropErrors, IAppPropName {
  appFormControl?: any;
  appLoadDocument?: boolean;
  appOnFileSelected?: any;
  appDocumentValueObj?: any;
  appMany?: boolean;
}

const AppFieldFile: React.FC<IAppFieldFile> = (props: IAppFieldFile) => {
  const [error, setError] = useState<any>(undefined);
  // ==============================
  useEffect(() => {
    if (props.appFormControl) {
      setError([props.appFormControl.getErrors()[props.name]]);
    } else {
      setError(props.appErrors);
    }
  }, [props.appFormControl?.getErrors()[props.name], props.appErrors]);
  // ==============================
  const isTabletOrMobile = useMediaQuery({
    query: ConstUtil.cisTabletOrMobile,
  });
  const [documentObj, setDocumentObj]: any = useState([]);
  const imageExtensions = [
    "application/gif",
    "application/jpeg",
    "application/bmp",
    "application/png",
    "application/webp",
    "application/bmp",
  ];
  // ==============================
  const handleQueryBlur = () => {
    if (props.appFormControl != undefined) {
      props.appFormControl.handleBlur({ target: { name: props.name } });
    }
  };
  // ==============================

  const customBase64Uploader = async (event: any) => {
    const file = event.files[0];

    const reader = new FileReader();
    reader.readAsDataURL(file);
    setDocumentObj({ filename: file.name, objectURL: file.objectURL });
    reader.onloadend = () => {
      if (reader.result) {
        const [header, base64data] = reader.result.toString().split(",");

        if (props.appOnFileSelected) {
          file.result = base64data;
          props.appOnFileSelected(reader);
        }

        if (props.appFormControl) {
          let content_type = file.type.split("/");
          content_type = `application/${content_type[1]}`;

          const document = {
            id: uuid(),
            file64: base64data,
            filename: file.name,
            objectURL: file.objectURL,
            code_document: file.name.toUpperCase(),
            content_type,
            new: true,
          };
          if (props.appMany) {
            let fileOld = props.appFormControl.getValues()[props.name];
            if (!fileOld) {
              fileOld = [];
            }
            props.appFormControl.setValueField(props.name, [
              ...fileOld,
              document,
            ]);
          } else {
            props.appFormControl.setValueField(props.name, [document]);
          }
          handleQueryBlur();
        }
      }
    };
  };

  // ==============================
  useEffect(() => {
    if (props.appFormControl.getValues()[props.name]) {
      setDocumentObj(props.appFormControl.getValues()[props.name]);
    }
  }, [props.appFormControl.getValues()[props.name]]);
  // ==============================
  const handleRemoveDocument = (id: string) => {
    confirmDialog({
      message: "Do you want to detele document ?",
      header: "Confirmation",
      icon: "pi pi-question-circle",
      accept: async () => {
        if (id == "all") {
          props.appFormControl.setValueField(props.name, []);
        } else if (props.appFormControl) {
          const oldFiles = props.appFormControl.getValues()[props.name];
          const newFiles = oldFiles.filter((file: any) => file.id != id);

          props.appFormControl.setValueField(props.name, newFiles);
        }
      },
    });
  };
  // ==============================
  const handleDownloadDocument = (filename: string) => {
    openDownloadFolder(
      `${process.env.REACT_APP_API_URL}/${ConstUtil.sysDocumentDownloadOpenRoute}/${filename}`
    );
  };
  // ==============================
  const ItemTemplate = () => {
    if (documentObj.length > 0) {
      return documentObj.map((doc: any) => {
        return (
          <div
            key={doc.id}
            className="p-3 flex align-items-center justify-content-between"
          >
            <div>
              <AppVisible
                visible={
                  imageExtensions.includes(doc.content_type) &&
                  !isTabletOrMobile
                }
              >
                <Image
                  className="mr-3"
                  src={
                    !doc?.new
                      ? `${process.env.REACT_APP_API_URL}/${ConstUtil.sysDocumentDownloadRoute}/${doc.id}`
                      : doc.objectURL
                  }
                  alt="Image"
                  width="80"
                  height="60"
                  preview
                />
              </AppVisible>
            </div>

            <div className="flex-grow-1">{doc.filename}</div>
            <div className="max-w-7rem flex flex-row justify-content-end">
              <AppVisible visible={!doc?.new}>
                <AppGenericAction
                  appIcon="pi pi-arrow-down text-xl"
                  className="p-button-secondary p-button-rounded p-button-outlined mr-3"
                  appOnAction={() => {
                    handleDownloadDocument(`${doc.id}-${doc.filename}`);
                  }}
                />
              </AppVisible>
              <AppGenericAction
                appIcon="pi pi-trash text-xl"
                className="p-button-secondary p-button-rounded p-button-outlined mr-3"
                appOnAction={() => {
                  handleRemoveDocument(doc.id);
                }}
              />
            </div>
          </div>
        );
      });
    }
    return (
      <div className="w-full flex justify-content-center p-3">
        Select one file
      </div>
    );
  };

  return (
    <>
      <div
        className={` ${
          props.className
            ? props.className
            : "col-12 md:col-3 lg:col-3 xl:col-3"
        }`}
      >
        <div className="flex flex-column surface-100 border-round-top-md">
          <div className="surface-200 p-3 flex flex-row justify-content-between">
            <FileUpload
              mode="basic"
              accept="*"
              maxFileSize={10000000}
              onUpload={customBase64Uploader}
              auto
            />

            <AppVisible visible={documentObj.length > 0}>
              <AppGenericAction
                appIcon="pi pi-trash text-xl"
                className="p-button-secondary p-button-rounded p-button-outlined mr-3"
                appOnAction={() => {
                  handleRemoveDocument("all");
                }}
              />
            </AppVisible>
          </div>
          <div className=" max-h-20rem overflow-auto">
            <ItemTemplate />
          </div>
        </div>
        <AppFieldErrors
          appErrors={(() => {
            return error;
          })()}
        />
      </div>
    </>
  );
};

export default memo(AppFieldFile);
