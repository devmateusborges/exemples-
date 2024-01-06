"use client";
import React, { useEffect, useState } from "react";
import { InputText } from "primereact/inputtext";
import { Button } from "primereact/button";
import { AppProps, CardItem } from "@utils/AppInterfaces";
import AppCards from "./AppCards";

interface AppSearchProps extends AppProps {
  search?: string;
  items?: any;
  title?: React.ReactNode;
  onChangeAction: (e: any) => void;
}

const AppSearch: React.FC<AppSearchProps> = (props: AppSearchProps) => {
  const [search, setSearch] = useState("");

  return (
    <>
      <div style={{ margin: "5vh" }} className="flex justify-content-center">
        <InputText
          value={search}
          onChange={(e) => {
            setSearch(e.target.value);
            props.onChangeAction(e.target.value);
          }}
          className="w-full text-base p-2 sm:w-7 border-round"
          type="text"
          placeholder="Pesquisar ..."
        />
        <Button icon="pi pi-search" className="p-button-rounded ml-2" />
      </div>
      {(() => {
        if (search && props.items == "") {
          return <h1>Não encontrado</h1>;
        }
      })()}
    </>
  );
};

export default AppSearch;
