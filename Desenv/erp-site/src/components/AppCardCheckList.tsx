"use client";
import { Card } from "primereact/card";

import React, { useState, useEffect } from "react";
import { Chip } from "primereact/chip";
import { AppProps } from "../utils/AppInterfaces";

interface AppCardCheckListProps extends AppProps {
  title: string;
  checklist: Array<String>;
}

const AppCardCheckList: React.FC<AppCardCheckListProps> = (props) => {
  return (
    <div className="border-radius shadow-2 white">
      <Card className="AppSobre-p-card">
        <div className="flex flex-column align-content-center">
          <h2 className="">{props.title}</h2>

          {props.checklist.map((item: any, index: number) => (
            <li key={index} className="AppSobre-li-options text-secondary flex">
              <i className="pi pi-check-circle text-green p-1 mr-2"></i>
              {item}
            </li>
          ))}
        </div>
      </Card>
    </div>
  );
};

export default AppCardCheckList;
