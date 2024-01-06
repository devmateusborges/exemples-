"use client";
import { Card } from "primereact/card";

import React, { useState, useEffect } from "react";
import { Chip } from "primereact/chip";
import { AppProps } from "@utils/AppInterfaces";

interface AppCardSolutionsProps extends AppProps {
  title: string;
  content?: string;
  comingSoon?: boolean;
}

const AppCardSolutions: React.FC<AppCardSolutionsProps> = (props) => {
  return (
    <Card className="shadow-2 relative">
      <div className="absolute" style={{ right: 20, top: -15 }}>
        {(() => {
          if (props.comingSoon) {
            return <Chip label="EM BREVE" className="yellow  " />;
          }
        })()}
      </div>
      <div className="flex align-items-center  grid col-12 ">
        <div className="flex align-items-center xl:col-9 lg:col-9 md:col-9 sm:col-9">
          <i className="pi pi-check-circle text-green m-3 text-3xl"></i>
          <h3 className=" m-0 text-xl">{props.title}</h3>
        </div>
      </div>

      <p className="text-secondary text-center text-md xl:text-lg lg:text-lg p-2">
        {props.content}
      </p>
    </Card>
  );
};

export default AppCardSolutions;
