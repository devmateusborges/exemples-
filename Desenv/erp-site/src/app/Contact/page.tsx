"use client";
import React from "react";
import AppContact from "@components/AppContact";
import AppHeader from "@components/AppHeader";
import { Skeleton } from "primereact/skeleton";

const ContactPage: React.FC = () => {
  return (
    <>
      <div className="sub-topbar  ">
        <AppHeader title="CONTATO" />
        <div className="flex justify-content-center">
          <AppContact className="lg:w-30rem xl:w-30rem md:w-30rem" />
        </div>
      </div>
    </>
  );
};

export default ContactPage;
