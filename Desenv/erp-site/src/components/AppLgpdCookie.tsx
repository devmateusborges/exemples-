"use client";
import React, { useEffect, useState } from "react";
import { Button } from "primereact/button";

import { useRouter } from "next/navigation";

import { event } from "nextjs-google-analytics";
import { AppProps } from "@utils/AppInterfaces";

interface AppLgpdCookieProps extends AppProps {}

const AppLgpdCookie: React.FC<AppLgpdCookieProps> = () => {
  const router = useRouter();
  const [dataDisplay, setDataDisplay] = useState(true);

  useEffect(() => {}, [dataDisplay]);

  const handleAccepted = () => {
    event("accepted_applgpdcookie", {
      category: "applgpdcookie",
      label: "Accepted lgpd",
    });
    setDataDisplay(false);
  };

  const handleDenied = () => {
    event("denied_applgpdcookie", {
      category: "applgpdcookie",
      label: "Denied lgpd",
    });

    setDataDisplay(false);
  };

  const handleAcceptedPrivacyPolicy = () => {
    event("accepted_applgpdcookie", {
      category: "applgpdcookie",
      label: "Accepted privacy terms",
    });

    router.push("/PrivacyPolicy");
  };

  return (
    <>
      {(() => {
        if (dataDisplay) {
          return (
            <div
              className="
                                          grid
                                          pt-5
                                          pb-5
                                          pl-5
                                          pr-5
                                          xl:pl-8 xl:pr-8
                                          md:pl-8 md:pr-8
                                          w-full
                                          div-lgpd
                                          surface-800
                                          shadow-5
                                          
                                        "
            >
              <div className="col-12 xl:col-6 md:col-6 sm:12">
                <p className="text-50">
                  <i className="pi pi-lock text-2xl  mr-2"></i>
                  Utilizamos cookies no site para melhorar sua experiência. Ao
                  continuar navegando, você concorda com a nossa
                  <br />
                  <span className="ml-1">
                    <a
                      className="cursor-pointer"
                      onClick={() => {
                        handleAcceptedPrivacyPolicy();
                      }}
                    >
                      ACESSE POLÍTICA DE PRIVACIDADE
                    </a>
                  </span>
                </p>
              </div>
              <div
                className="col-12
                           xl:col-6
                           md:col-6
                           grid
                           justify-content-end
                           align-items-center
                           mt-5
                           md:mt-0
                           lg:mt-0
                           xl:mt-0"
              >
                <Button
                  onClick={() => {
                    handleAccepted();
                  }}
                  label="CONCORDAR E FECHAR"
                  className="p-2 m-2 col-12 md:col-6 lg:col-6 xl:col-6 border-round"
                >
                  <i className="pi pi-check "></i>
                </Button>
                <Button
                  label="DECLINAR"
                  className="p-button-danger p-2 m-2 col-12 md:col-6 lg:col-6 xl:col-6 border-round"
                  onClick={() => {
                    handleDenied();
                  }}
                >
                  <i className="pi pi-times "></i>
                </Button>
              </div>
            </div>
          );
        }
      })()}
    </>
  );
};

export default AppLgpdCookie;
