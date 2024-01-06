"use client";
import { Card } from "primereact/card";

import React, { useState, useEffect } from "react";
import { Chip } from "primereact/chip";
import { Button } from "primereact/button";

import { text } from "stream/consumers";
import { event } from "nextjs-google-analytics";
import { AppProps } from "../utils/AppInterfaces";

interface AppCardDemonstrationProps extends AppProps {
  text1?: string;
  text2?: string;
}

const AppCardDemonstration: React.FC<AppCardDemonstrationProps> = (props) => {
  return (
    <div className="grid blue  w-full ">
      <div className=" col-12 xl:col-6 md:col-12 sm:col-12  ">
        <div className="flex flex-column aling-content-start   align-items-start p-4 ">
          <div className="flex  aling-content-center align-items-center">
            <h2 className="text-white font-bold pb-1 ">
              <i className="pi pi-star text-50 mr-2 text-3xl"></i>
              {props.text1 ? props.text1 : "Peça uma demonstração gratuita!"}
            </h2>
          </div>
          <p className="lg:text-left  xl:text-left  md:text-left  sm:text-center text-white">
            {props.text2
              ? props.text2
              : "Preencha o formulário desta página e conheça o software, ou faleconosco pelo"}
          </p>
        </div>
      </div>
      <div
        className="
          col-12
          xl:col-6
          md:col-12
          sm:col-12
          flex
          
          xl:justify-content-end
          md:justify-content-center
          align-items-center
          flex-column
          xl:flex-row
          md:flex-row
         
        "
      >
        <div className="flex ">
          <Button
            className="p-button-outlined font-bold w-auto text-white m-2 h-3rem p-button-warning text-sm md:text-3xl lg:text-3xl xl:text-3xl scalein animation-duration-1000 animation-iteration-infinite border-round"
            label="TESTE GRÁTIS"
            onClick={() => {
              event("click_test_free", {
                category: "AppCardDemonstration",
                label: "Click test free",
              });
              window.open("/web/#/signup", "_blank");
            }}
          >
            <i className="pi pi-heart text-50 ml-2 text-lg md:text-3xl lg:text-3xl xl:text-3xl"></i>
          </Button>

          <Button
            className="font-bold w-auto text-white m-2 h-3rem p-button-success text-sm md:text-3xl lg:text-3xl xl:text-3xl border-round"
            label="WHATSAPP"
            onClick={() => {
              event("click_whatsapp", {
                category: "AppCardDemonstration",
                label: "Click Whatsapp",
              });
              window.open(
                "https://api.whatsapp.com/send/?phone=5599999999999&text&app_absent=0",
                "_blank"
              );
            }}
          >
            <i className="pi pi-comments text-50 ml-2 text-lg md:text-3xl lg:text-3xl xl:text-3xl"></i>
          </Button>
        </div>
      </div>
    </div>
  );
};

export default AppCardDemonstration;
