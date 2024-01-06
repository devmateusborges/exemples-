"use client";
import React, { useEffect, useRef, useState } from "react";
import { InputText } from "primereact/inputtext";
import { InputMask } from "primereact/inputmask";
import { InputTextarea } from "primereact/inputtextarea";
import { Dropdown } from "primereact/dropdown";
import { Button } from "primereact/button";

import * as yup from "yup";
import { Toast } from "primereact/toast";
import { useRouter } from "next/navigation";

import { useDispatch, useSelector } from "react-redux";
import { event } from "nextjs-google-analytics";
import { AppProps, DataForm } from "../utils/AppInterfaces";
import { RootState } from "../store";

interface AppContactProps extends AppProps {
  title?: React.ReactNode;
  option?: number;
}

const AppContact: React.FC<AppContactProps> = (props) => {
  const router = useRouter();
  const contatoOrigin = useSelector(
    (state: RootState) => state.util.contatoOrigin
  );
  const [contatoOriginAux, setContatoOriginAux] = useState(0);

  useEffect(() => {
    if (props.option) {
      setContatoOriginAux(props.option);
    } else {
      setContatoOriginAux(contatoOrigin);
    }
  }, []);

  const [dataFormValues, setDataFormValues] = useState<DataForm>({});
  const [datastatus, setDataStatus] = useState({
    type: "",
    error: { input: "", message: "" },
  });
  const options = [
    { code: 1, name: "DÚVIDAS/SUPORTE" },
    { code: 2, name: "DEMONSTRAÇÃO" },
    { code: 3, name: "TRABALHE CONOSCO" },
    { code: 4, name: "FINANCEIRO" },
  ];

  const validate = async () => {
    let schema = yup.object().shape({
      Dropdown: yup
        .object()
        .required({ input: "Dropdown", message: "Selecione uma Opção!" }),
      Conteudo: yup.string(),
      Telephone: yup
        .string()
        .required({ input: "Telephone", message: "* Telefone obrigatório" }),
      Email: yup
        .string()
        .required({ input: "Email", message: "* E-mail obrigatório" })
        .email({ input: "Email", message: "Preencha com Email valido" }),
      Nome: yup
        .string()
        .required({ input: "Name", message: "* Nome obrigatório" }),
    });

    try {
      await schema.validate(dataFormValues);
      return true;
    } catch (err: any) {
      setDataStatus({
        type: "error",
        error: { input: err.errors[0].input, message: err.errors[0].message },
      });
      return false;
    }
  };
  const handleInputChange = (e: any) => {
    const { name, value } = e.target;
    setDataFormValues({ ...dataFormValues, [name]: value });
  };

  const handlerSubmit = async (e: any) => {
    e.preventDefault();

    event("send_appcontact", {
      category: "appcontact",
      label: "Send contact",
    });

    if (!(await validate())) return;

    const saveDataForm = true;

    if (saveDataForm) {
      setDataStatus({
        type: "success",
        error: { input: "", message: "tudo ok" },
      });

      const formData = new FormData(e.target);
      const data = Object.fromEntries(formData);
    } else {
      setDataStatus({
        type: "error",
        error: {
          input: "error",
          message: "Erro: Usuário não cadastrado com sucesso!",
        },
      });
    }
  };

  return (
    <>
      {datastatus.type === "success" ? (
        <p style={{ color: "green" }}>{datastatus.error.message}</p>
      ) : (
        ""
      )}
      <div
        style={{ maxWidth: "400px" }}
        className=" flex justify-content-start w-10"
      >
        <div className="card w-full">
          <form onSubmit={handlerSubmit}>
            <div className="field ">
              <label htmlFor="name" className="block">
                Nome Completo*
              </label>
              <InputText
                className={` inputfield  w-full ${
                  datastatus.type === "error" &&
                  datastatus.error.input == "Name"
                    ? "p-invalid"
                    : ""
                } `}
                id="input_nome"
                name="Nome"
                onChange={handleInputChange}
                value={dataFormValues.Nome || ""}
              />
              {datastatus.type === "error" &&
              datastatus.error.input == "Name" ? (
                <p style={{ color: "red" }} className="text-base">
                  {datastatus.error.message}
                </p>
              ) : (
                ""
              )}
            </div>
            <div className="field">
              <label htmlFor="email" className="block">
                Email*
              </label>
              <InputText
                className={` inputfield  w-full ${
                  datastatus.type === "error" &&
                  datastatus.error.input == "Email"
                    ? "p-invalid"
                    : ""
                } `}
                id="Email"
                name="Email"
                onChange={handleInputChange}
                value={dataFormValues.Email || ""}
              />
              {datastatus.type === "error" &&
              datastatus.error.input == "Email" ? (
                <p className="text-base" style={{ color: "red" }}>
                  {datastatus.error.message}
                </p>
              ) : (
                ""
              )}
            </div>
            <div className="field">
              <label htmlFor="telephone" className="block">
                Telefone*
              </label>
              <InputMask
                name="Telephone"
                className={` inputfield  w-full ${
                  datastatus.type === "error" &&
                  datastatus.error.input == "Telephone"
                    ? "p-invalid"
                    : ""
                } `}
                id="telephone"
                mask="(99) 99999-9999"
                onChange={handleInputChange}
                value={dataFormValues.Telephone || ""}
              />
              {datastatus.type === "error" &&
              datastatus.error.input == "Telephone" ? (
                <p className="text-base" style={{ color: "red" }}>
                  {datastatus.error.message}
                </p>
              ) : (
                ""
              )}
            </div>
            <div className="field">
              <label htmlFor="content" className="block">
                Quer adicionar algo?
              </label>
              <InputTextarea
                name="Conteudo"
                className={` inputfield  w-full ${
                  datastatus.type === "error" &&
                  datastatus.error.input == "Conteudo"
                    ? "p-invalid"
                    : ""
                } `}
                id="content"
                onChange={handleInputChange}
                value={dataFormValues.Conteudo || ""}
              />
              {datastatus.type === "error" &&
              datastatus.error.input == "Conteudo" ? (
                <p className="text-base" style={{ color: "red" }}>
                  {datastatus.error.message}
                </p>
              ) : (
                ""
              )}
            </div>
            <div className="field">
              <label htmlFor="content" className="block">
                Selecione tipo*
              </label>
              <Dropdown
                name="Dropdown"
                value={dataFormValues.Dropdown || options[contatoOriginAux]}
                className={`   inputfield  w-full ${
                  datastatus.type === "error" &&
                  datastatus.error.input == "Dropdown"
                    ? "p-invalid"
                    : ""
                }`}
                options={options}
                optionLabel="name"
                onChange={handleInputChange}
              />
              {datastatus.type === "error" &&
              datastatus.error.input == "Dropdown" ? (
                <p className="text-red-100">{datastatus.error.message}</p>
              ) : (
                ""
              )}
            </div>
            <div className="field">
              <Button
                type="submit"
                icon="pi pi-check"
                className="p-button-lg w-full p-mt-2 "
                label="Enviar"
              />
            </div>
          </form>
        </div>
      </div>
    </>
  );
};

export default AppContact;
