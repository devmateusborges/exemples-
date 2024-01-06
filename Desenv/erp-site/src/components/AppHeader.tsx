"use client";
import React from "react";
import { AppProps } from "@utils/AppInterfaces";

interface AppHeaderProps extends AppProps {
  title?: React.ReactNode;
}

const AppHeader: React.FC<AppHeaderProps> = (props) => {
  return (
    <div
      className="
            w-full
            h-4rem
            flex
            align-items-center    
            justify-content-center
            border-bottom-1 
            border-200
            green
            text-white
            mb-3"
    >
      <h1 style={{ margin: "0" }} className="text-3xl">
        {props.title}
      </h1>
    </div>
  );
};

export default AppHeader;
