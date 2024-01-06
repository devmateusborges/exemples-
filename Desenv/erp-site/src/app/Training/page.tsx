"use client";
import AppHeader from "@components/AppHeader";
import React, { useEffect, useState } from "react";
import { Column } from "primereact/column";
import { TreeTable } from "primereact/treetable";

import { InputText } from "primereact/inputtext";
import TrainingService from "@services/TrainingService";

const TrainingPage: React.FC = () => {
  const nodeservice = new TrainingService();

  const [dataTreinamentos, setDataTreinamentos] = useState([]);
  const [dataFilter, setDataFilter] = useState(null);

  useEffect(() => {
    nodeservice.getData().then((data: any) => setDataTreinamentos(data));
  }, []);

  const getHeader = (globalFilterKey: string) => {
    return (
      <div className="text-right">
        <div className="p-input-icon-left">
          <i className="pi pi-search"></i>
          <InputText type="search" placeholder="Global Search" size={50} />
        </div>
      </div>
    );
  };

  return (
    <>
      <div className="sub-topbar min-h-screen  ">
        <AppHeader title="TREINAMENTO" />
        <TreeTable
          value={dataTreinamentos}
          globalFilter={dataFilter}
          filterMode="strict"
        >
          <Column
            field="descricao"
            header="Descrição"
            filter
            filterPlaceholder="Descrição"
            expander
          >
            <span className="sm-visible"></span>
            <span className="sm-visible"></span>
          </Column>

          <Column
            field="horas"
            header="Horas"
            filter
            filterPlaceholder="Horas"
          ></Column>

          <Column
            field="tipo"
            header="Tipo"
            filter
            filterPlaceholder="Tipo"
          ></Column>
        </TreeTable>
      </div>
    </>
  );
};

export default TrainingPage;
