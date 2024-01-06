import React, { useState, useEffect, useRef, useMemo } from "react";
import { Menubar, MenubarStartTemplate } from "primereact/menubar";
import { ProgressBar } from "primereact/progressbar";
import { useRouter } from "next/navigation";
import Image from "next/image";
import { useSelector, useDispatch } from "react-redux";
import { contatoOrigin } from "../store/UtilStore";
import { AppProps } from "@utils/AppInterfaces";
import { RootState } from "@store/index";
import Link from "next/link";

interface AppTopbarProps extends AppProps {
  title?: React.ReactNode;
  start?: MenubarStartTemplate;
}

const AppTopbar: React.FC<AppTopbarProps> = (props) => {
  const router = useRouter();
  const utilDispatch = useDispatch();
  const util = useSelector((state: RootState) => state.util);

  const items = [
    {
      label: "INICIO",
      command: () => {
        router.push("/");
      },
    },
    {
      label: "BLOG",
      command: () => {
        router.push("/Blog");
      },
    },
    {
      label: "CONTATO",
      command: () => {
        utilDispatch(contatoOrigin(1));
        router.push("/Contact");
      },
    },
    {
      label: "PREÇO",
      command: () => {
        router.push("/Pricing");
      },
    },
    {
      label: "AJUDA",
      command: () => {
        router.push("/HelpCenter");
      },
    },
    {
      label: "LOGIN",
      command: () => {
        window.open("/web", "_blank");
      },
    },
  ];

  const logo = (
    <div className="topbar-logo">
      <Link href="/">
        <Image
          style={{ width: "120px" }}
          src="assets/images/resultfacil_branco.svg"
          alt="logo"
          width={70}
          height={70}
        />
      </Link>
    </div>
  );

  const progressbar = useMemo(
    () => (
      <ProgressBar
        mode="indeterminate"
        style={{ height: "0.5em" }}
        className="z-5"
        // TODO  resolver o click v-show="loading_request"
      />
    ),
    []
  );

  return (
    <>
      <div className="AppTopbar-topbar-show flex flex-column fixed w-full z-1 white">
        <div className="AppTopbar-topbar shadow-4">
          <div className="w-full absolute">
            {(() => {
              if (util.loading) {
                return <>{progressbar}</>;
              }
            })()}
          </div>
          <div className="pl-8 pr-8">
            <Menubar
              model={items}
              start={logo}
              style={{ color: "white" }}
              className="AppTopbar-topbar  topbar-menu font-bold"
            >
              <div className="flex align-items-center">
                <div
                  className="flex justify-content-center cursor-pointer"
                  style={{ width: "45px" }}
                >
                  <Image
                    src="assets/images/images-icons/br.svg"
                    className="Languages fadeout fadein"
                    alt=""
                    width={100}
                    height={100}
                  />
                  <Image
                    src="/images-icons/es.svg"
                    className="Languages fadeout fadein"
                    alt=""
                    width={100}
                    height={100}
                  />
                  <Image
                    src="/images-icons/us.svg"
                    className="Languages fadeout fadein"
                    alt=""
                    width={100}
                    height={100}
                  />
                </div>

                <div className="topbar-logo">
                  <Link href="/">
                    <Image
                      style={{ width: "120px" }}
                      src="/images/resultfacil_branco.svg"
                      alt={""}
                      width={120}
                      height={120}
                    />
                  </Link>
                </div>
              </div>
              <template style={{ paddingTop: "20px" }}>
                <a
                  className="font-bold"
                  //TODO RESOLVE CLICKING @click="redirect(item.url)"
                  style={{ color: "white", padding: "0 10px 0 10px" }}
                >
                  {/*TODO RESOLVE items   item label */}
                </a>
              </template>
            </Menubar>
          </div>
        </div>
      </div>
    </>
  );
};

export default AppTopbar;
