"use client";
import React, { useState } from "react";
import { InputText } from "primereact/inputtext";
import { Button } from "primereact/button";
import { AppProps } from "@utils/AppInterfaces";

interface SearchProps extends AppProps {
  onChangeAction: (e: any) => void;
}

const SearchBlog: React.FC<SearchProps> = (props: SearchProps) => {
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
    </>
  );
};

export default SearchBlog;
